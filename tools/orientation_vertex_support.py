from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Callable, Iterable, Sequence

BitTuple = tuple[int, ...]
Edge = tuple[int, int]
BooleanFunction = Callable[[BitTuple], int]


@dataclass(frozen=True)
class OrientationReport:
    orientation: BitTuple
    weight: int
    vertices: frozenset[int]

    @property
    def vertex_support(self) -> int:
        return len(self.vertices)


def hypercube(n: int) -> Iterable[BitTuple]:
    if n < 0:
        raise ValueError("n must be nonnegative")
    return product((0, 1), repeat=n)


def minimal_orientation(num_variables: int, f: BooleanFunction) -> BitTuple:
    orientation = [0] * num_variables
    for x in hypercube(num_variables):
        fx = int(f(x))
        if fx not in (0, 1):
            raise ValueError("function must be Boolean")
        if fx == 0:
            continue
        for i, bit in enumerate(x):
            if bit or orientation[i]:
                continue
            y = list(x)
            y[i] = 1
            fy = int(f(tuple(y)))
            if fy not in (0, 1):
                raise ValueError("function must be Boolean")
            if fy == 0:
                orientation[i] = 1
    return tuple(orientation)


def analyze_orientation(
    f: BooleanFunction,
    edge_variables: Sequence[Edge],
) -> OrientationReport:
    orientation = minimal_orientation(len(edge_variables), f)
    vertices: set[int] = set()
    for bit, edge in zip(orientation, edge_variables, strict=True):
        if bit:
            u, v = edge
            if u == v:
                raise ValueError("edge variables must use distinct endpoints")
            vertices.update((u, v))
    return OrientationReport(
        orientation=orientation,
        weight=sum(orientation),
        vertices=frozenset(vertices),
    )


def main() -> None:
    edges = ((0, 1), (0, 2), (1, 2))

    monotone_triangle = lambda x: int(all(x))
    negated_star = lambda x: int((not x[0]) and (not x[1]))
    negated_disjoint = lambda x: int((not x[0]) and (not x[2]))

    report = analyze_orientation(monotone_triangle, edges)
    assert report.orientation == (0, 0, 0)
    assert report.weight == 0
    assert report.vertex_support == 0

    report = analyze_orientation(negated_star, edges)
    assert report.orientation == (1, 1, 0)
    assert report.weight == 2
    assert report.vertices == frozenset({0, 1, 2})

    report = analyze_orientation(negated_disjoint, edges)
    assert report.orientation == (1, 0, 1)
    assert report.weight == 2
    assert report.vertices == frozenset({0, 1, 2})

    print("orientation vertex-support verifier: PASS")


if __name__ == "__main__":
    main()
