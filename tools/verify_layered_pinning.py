from __future__ import annotations

from dataclasses import dataclass, replace
from itertools import product
from typing import Iterable


@dataclass(frozen=True)
class Instance:
    layers: tuple[tuple[int, ...], ...]
    masks: tuple[frozenset[int], ...]
    edges: frozenset[tuple[int, int]]
    allowed_assignments: tuple[tuple[tuple[int, ...], ...], ...]
    assignment_masks: tuple[tuple[frozenset[int], ...], ...]


def edge_key(u: int, v: int) -> tuple[int, int]:
    return (u, v) if u < v else (v, u)


def valid_vertex_tuple(instance: Instance, vertices: tuple[int, ...]) -> bool:
    if len(vertices) != len(instance.layers):
        return False
    for r, v in enumerate(vertices):
        if v not in instance.layers[r] or v not in instance.masks[r]:
            return False
    return all(
        edge_key(vertices[r], vertices[s]) in instance.edges
        for r in range(len(vertices))
        for s in range(r + 1, len(vertices))
    )


def assignment_choices(instance: Instance, vertices: tuple[int, ...]) -> Iterable[tuple[tuple[int, ...], ...]]:
    per_layer: list[list[tuple[int, ...]]] = []
    for r, v in enumerate(vertices):
        layer = instance.layers[r]
        local_index = layer.index(v)
        candidates = instance.allowed_assignments[r][local_index]
        masks = instance.assignment_masks[r]
        filtered = [
            bits
            for bits in candidates
            if len(bits) == len(masks) and all(bit in masks[j] for j, bit in enumerate(bits))
        ]
        per_layer.append(filtered)
    return product(*per_layer)


def decide(instance: Instance) -> bool:
    for vertices in product(*instance.layers):
        if not valid_vertex_tuple(instance, vertices):
            continue
        if any(True for _ in assignment_choices(instance, vertices)):
            return True
    return False


def pin_vertices(instance: Instance, prefix: tuple[int, ...]) -> Instance:
    masks = list(instance.masks)
    for r, vertex in enumerate(prefix):
        masks[r] = frozenset({vertex})
    return replace(instance, masks=tuple(masks))


def pin_assignment_bit(instance: Instance, layer: int, bit_index: int, value: int) -> Instance:
    all_masks = [list(layer_masks) for layer_masks in instance.assignment_masks]
    all_masks[layer][bit_index] = frozenset({value})
    return replace(instance, assignment_masks=tuple(tuple(x) for x in all_masks))


def witnesses(instance: Instance) -> list[tuple[tuple[int, ...], tuple[tuple[int, ...], ...]]]:
    out = []
    for vertices in product(*instance.layers):
        if not valid_vertex_tuple(instance, vertices):
            continue
        for assignments in assignment_choices(instance, vertices):
            out.append((vertices, assignments))
    return out


def demo_instance() -> Instance:
    layers = ((0, 1), (2, 3), (4, 5))
    masks = tuple(frozenset(layer) for layer in layers)
    edges = frozenset(
        edge_key(u, v)
        for u, v in [
            (0, 2), (0, 4), (2, 4),
            (1, 3), (1, 5), (3, 5),
            (0, 3),
        ]
    )
    allowed_assignments = (
        (((0, 0), (1, 1)), ((0, 1),)),
        (((0, 0),), ((1, 0), (1, 1))),
        (((0, 1),), ((1, 0),)),
    )
    assignment_masks = tuple(
        tuple(frozenset({0, 1}) for _ in range(2))
        for _ in layers
    )
    return Instance(layers, masks, edges, allowed_assignments, assignment_masks)


def verify_vertex_pinning(instance: Instance) -> None:
    original = witnesses(instance)
    for k in range(len(instance.layers) + 1):
        prefixes = {witness[0][:k] for witness in original}
        candidates = product(*(instance.layers[r] for r in range(k)))
        for prefix in candidates:
            expected = prefix in prefixes
            observed = decide(pin_vertices(instance, prefix))
            assert observed == expected, (prefix, expected, observed)


def verify_assignment_pinning(instance: Instance) -> None:
    base_witnesses = witnesses(instance)
    assert base_witnesses
    for layer in range(len(instance.layers)):
        for bit_index in range(2):
            for value in (0, 1):
                expected = any(assignments[layer][bit_index] == value for _, assignments in base_witnesses)
                observed = decide(pin_assignment_bit(instance, layer, bit_index, value))
                assert observed == expected, (layer, bit_index, value, expected, observed)


if __name__ == "__main__":
    instance = demo_instance()
    verify_vertex_pinning(instance)
    verify_assignment_pinning(instance)
    print("layered vertex pinning: PASS")
    print("assignment-bit pinning: PASS")
    print("witness count:", len(witnesses(instance)))
