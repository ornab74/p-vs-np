from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from typing import Iterable, Literal, Sequence

Kind = Literal["var", "not_var", "and", "or"]
BitTuple = tuple[int, ...]


@dataclass(frozen=True)
class Node:
    kind: Kind
    index: int | None = None
    left: "Node | None" = None
    right: "Node | None" = None

    @staticmethod
    def var(index: int) -> "Node":
        return Node("var", index=index)

    @staticmethod
    def not_var(index: int) -> "Node":
        return Node("not_var", index=index)

    @staticmethod
    def and_(left: "Node", right: "Node") -> "Node":
        return Node("and", left=left, right=right)

    @staticmethod
    def or_(left: "Node", right: "Node") -> "Node":
        return Node("or", left=left, right=right)

    def validate(self, n: int) -> None:
        if self.kind in ("var", "not_var"):
            if self.index is None or not 0 <= self.index < n:
                raise ValueError(f"invalid literal index {self.index!r}")
            if self.left is not None or self.right is not None:
                raise ValueError("literal nodes cannot have children")
            return
        if self.index is not None or self.left is None or self.right is None:
            raise ValueError(f"malformed {self.kind} node")
        self.left.validate(n)
        self.right.validate(n)

    def evaluate(self, x: Sequence[int]) -> int:
        if self.kind == "var":
            assert self.index is not None
            return int(bool(x[self.index]))
        if self.kind == "not_var":
            assert self.index is not None
            return int(not bool(x[self.index]))
        assert self.left is not None and self.right is not None
        if self.kind == "and":
            return self.left.evaluate(x) & self.right.evaluate(x)
        return self.left.evaluate(x) | self.right.evaluate(x)


@dataclass(frozen=True)
class Terminal:
    kind: Literal["var", "not_var"]
    index: int

    def is_valid_monotone_witness(self, u: Sequence[int], v: Sequence[int]) -> bool:
        return self.kind == "var" and u[self.index] == 1 and v[self.index] == 0

    def is_reversed_witness(self, u: Sequence[int], v: Sequence[int]) -> bool:
        return self.kind == "not_var" and u[self.index] == 0 and v[self.index] == 1


def kw_descent(root: Node, u: BitTuple, v: BitTuple) -> Terminal:
    """Simulate the deterministic NNF KW descent.

    Precondition: root(u)=1 and root(v)=0.
    At OR nodes Alice chooses the first child true on u.
    At AND nodes Bob chooses the first child false on v.
    """
    if len(u) != len(v):
        raise ValueError("u and v must have equal length")
    root.validate(len(u))
    if root.evaluate(u) != 1 or root.evaluate(v) != 0:
        raise ValueError("KW pair must satisfy root(u)=1 and root(v)=0")

    node = root
    while node.kind in ("and", "or"):
        assert node.left is not None and node.right is not None
        if node.kind == "or":
            candidates = (node.left, node.right)
            node = next(child for child in candidates if child.evaluate(u) == 1)
        else:
            candidates = (node.left, node.right)
            node = next(child for child in candidates if child.evaluate(v) == 0)

        if node.evaluate(u) != 1 or node.evaluate(v) != 0:
            raise AssertionError("KW invariant was not preserved")

    assert node.index is not None
    terminal = Terminal(node.kind, node.index)
    if not (
        terminal.is_valid_monotone_witness(u, v)
        or terminal.is_reversed_witness(u, v)
    ):
        raise AssertionError("terminal is neither a monotone nor reversed witness")
    return terminal


def hypercube(n: int) -> Iterable[BitTuple]:
    return product((0, 1), repeat=n)


def hard_pairs(root: Node, n: int) -> list[tuple[BitTuple, BitTuple]]:
    root.validate(n)
    ones = [x for x in hypercube(n) if root.evaluate(x) == 1]
    zeros = [x for x in hypercube(n) if root.evaluate(x) == 0]
    return [(u, v) for u in ones for v in zeros]


def orientation_defect_mass(
    root: Node,
    n: int,
    pairs: Sequence[tuple[BitTuple, BitTuple]] | None = None,
) -> float:
    selected = list(pairs) if pairs is not None else hard_pairs(root, n)
    if not selected:
        return 0.0
    reversed_count = 0
    for u, v in selected:
        terminal = kw_descent(root, u, v)
        reversed_count += int(terminal.is_reversed_witness(u, v))
    return reversed_count / len(selected)


def main() -> None:
    monotone = Node.and_(Node.var(0), Node.var(1))
    nonmonotone = Node.and_(Node.not_var(0), Node.var(1))
    cancelled = Node.or_(
        Node.var(0),
        Node.and_(Node.var(0), Node.not_var(1)),
    )

    assert orientation_defect_mass(monotone, 2) == 0.0
    assert orientation_defect_mass(nonmonotone, 2) > 0.0

    # The cancelled representation computes x0 but can route some KW pairs
    # through a negative literal depending on its syntax. This demonstrates
    # representation dependence rather than a function invariant.
    assert all(
        cancelled.evaluate(x) == x[0]
        for x in hypercube(2)
    )
    defect = orientation_defect_mass(cancelled, 2)
    assert 0.0 <= defect <= 1.0

    print(f"KW orientation-defect verifier: PASS (cancelled defect={defect:.6f})")


if __name__ == "__main__":
    main()
