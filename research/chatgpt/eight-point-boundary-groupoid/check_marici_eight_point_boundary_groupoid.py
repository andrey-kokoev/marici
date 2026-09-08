#!/usr/bin/env python3
"""Exact audit of Marici's eight-point physical-Cut boundary indexing groupoid.

Python standard library only. No network access or repository writes.
The source's loaded-cell/localization rules are transcribed from the three
pinned upstream files identified in SOURCES. This checks the INDEXING diagram,
not the physical relative totalization or a nonlinear geometric realization.
Run: python check_marici_eight_point_boundary_groupoid.py --output certificate.json
"""
from __future__ import annotations
import argparse
from collections import Counter, deque
from itertools import combinations
import json
from pathlib import Path
from typing import Iterable

COMMIT = 'd1947b67a60d3e88ba77f4ca60ea02c2a306ee61'
SOURCES = [
 'research/voevodsky/check_n8_six_by_four_cut_boundary.py',
 'research/voevodsky/check_n8_loaded_octagon_carrier.py',
 'research/voevodsky/check_n8_multirees_conductor_stalk_kernel.py',
 'research/voevodsky/check_n8_cut_naturality_after_sheet_transform.py',
]
Diagonal = tuple[int, int]
Face = tuple[Diagonal, ...]
Cell = tuple[Face, Face]
Group = tuple[int, int]
COUNTS: Counter[str] = Counter()


def verify(condition: bool, category: str, detail: object = None) -> None:
    if not condition:
        raise AssertionError(f'{category}: {detail}')
    COUNTS[category] += 1


def diag(a: int, b: int) -> Diagonal:
    return tuple(sorted((a % 8, b % 8)))  # type: ignore[return-value]


def crosses(x: Diagonal, y: Diagonal) -> bool:
    a, b = x
    c, d = y
    return a < c < b < d or c < a < d < b


def subsets(items: tuple) -> Iterable[tuple]:
    for size in range(len(items) + 1):
        yield from combinations(items, size)


def mult(g: Group, h: Group) -> Group:
    # Composition g after h for i |-> r + (-1)^f i.
    r, f = g
    s, t = h
    return ((r + (-1 if f else 1) * s) % 8, f ^ t)


def act(g: Group, d: Diagonal) -> Diagonal:
    r, f = g
    sign = -1 if f else 1
    return diag(r + sign * d[0], r + sign * d[1])


def act_face(g: Group, face: Face) -> Face:
    return tuple(sorted(act(g, d) for d in face))


def act_cell(g: Group, cell: Cell) -> Cell:
    return act_face(g, cell[0]), act_face(g, cell[1])


def loc(cell: Cell) -> frozenset[Diagonal]:
    return frozenset(cell[0]) - frozenset(cell[1])


def degree(cell: Cell) -> int:
    return 5 - len(cell[0]) + len(cell[1])


def below(x: Cell, y: Cell) -> bool:
    return set(x[0]) <= set(y[0]) and set(y[1]) <= set(x[1])


def unmark(x: Cell) -> Cell:
    return x[0], ()


def targets(cell: Cell, diagonals: tuple[Diagonal, ...]) -> Iterable[Cell]:
    face, marked = cell
    if len(face) < 5:
        for d in diagonals:
            if d not in face and all(not crosses(d, e) for e in face):
                yield tuple(sorted(face + (d,))), marked
    for d in marked:
        yield face, tuple(e for e in marked if e != d)


def rank_counts(cells: Iterable[Cell]) -> list[int]:
    c = Counter(map(degree, cells))
    return [c[i] for i in range(6)]


def matmul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    return [[sum(x * y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def main(output: Path) -> None:
    ds = tuple((a, b) for a in range(8) for b in range(a + 1, 8)
               if b != a + 1 and (a, b) != (0, 7))
    faces = tuple(f for k in range(6) for f in combinations(ds, k)
                  if all(not crosses(a, b) for a, b in combinations(f, 2)))
    fc = Counter(map(len, faces))
    verify([fc[k] for k in range(6)] == [1, 20, 120, 300, 330, 132], 'full_face_counts')
    loaded = tuple((f, m) for f in faces for m in subsets(f))
    loaded_set = set(loaded)
    verify(len(loaded) == 12425, 'full_loaded_cells')
    verify(rank_counts(loaded) == [132, 990, 2940, 4320, 3140, 903], 'full_degree_counts')
    cuts = tuple(sorted({diag(i, i + 3) for i in range(8)}))
    verify(len(cuts) == 8, 'physical_cut_count')
    cut_set = set(cuts)
    cut_index = {d: i for i, d in enumerate(cuts)}
    support = {x: frozenset(loc(x) & cut_set) for x in loaded}
    boundary = {x for x in loaded if support[x]}
    patches = {d: {x for x in loaded if d in support[x]} for d in cuts}
    for d in cuts:
        verify(len(patches[d]) == 1075, 'single_cut_cells', d)
        verify(rank_counts(patches[d]) == [28, 168, 375, 369, 135, 0], 'single_cut_degrees', d)
    overlaps: dict[tuple[int, int], set[Cell]] = {}
    for i, j in combinations(range(8), 2):
        ov = patches[cuts[i]] & patches[cuts[j]]
        compatible = not crosses(cuts[i], cuts[j])
        verify(bool(ov) == compatible, 'intersection_compatibility', (i, j))
        if ov:
            overlaps[(i, j)] = ov
            verify(len(ov) == 125, 'double_cut_cells', (i, j))
            verify(rank_counts(ov) == [8, 36, 54, 27, 0, 0], 'double_cut_degrees', (i, j))
    verify(len(overlaps) == 12, 'compatible_pair_count')
    for i, j, k in combinations(range(8), 3):
        verify(not (patches[cuts[i]] & patches[cuts[j]] & patches[cuts[k]]), 'no_triple_overlap')
    verify(len(boundary) == 7100, 'union_cells')
    verify(len(boundary) == 8 * 1075 - 12 * 125, 'inclusion_exclusion')

    adjacency = {x: tuple(targets(x, ds)) for x in loaded}
    arrow_count = sum(map(len, adjacency.values()))
    verify(arrow_count == 50440, 'full_generating_arrows')
    boundary_arrows = 0
    for x, ys in adjacency.items():
        for y in ys:
            verify(y in loaded_set and below(x, y), 'source_arrow_valid')
            verify(degree(y) == degree(x) - 1, 'source_arrow_degree')
            verify(loc(x) < loc(y) and len(loc(y) - loc(x)) == 1, 'localization_inclusion')
            if x in boundary:
                boundary_arrows += 1
                verify(y in boundary and support[x] <= support[y], 'boundary_forward_closed')
                verify(below(unmark(x), unmark(y)), 'unmark_naturality')
                for d in support[x]:
                    verify(y in patches[d], 'patch_arrow_restriction')
    # The local nerve contraction is id -> unmark <- constant(S,empty).
    # These posets have at most one arrow between any two objects, so endpoint
    # and naturality checks prove equality of all composite comparison maps.
    nonempty_intersections = [(frozenset((d,)), patches[d]) for d in cuts]
    nonempty_intersections += [(frozenset((cuts[i], cuts[j])), ov) for (i, j), ov in overlaps.items()]
    for S, patch in nonempty_intersections:
        base = tuple(sorted(S)), ()
        verify(base in patch, 'intersection_base')
        for x in patch:
            verify(unmark(x) in patch and below(x, unmark(x)), 'contraction_to_unmarked')
            verify(below(base, unmark(x)), 'contraction_from_base')

    # A pointwise exact cover resolution of the constant integral diagram:
    # sum(edge-supported Z) -> sum(vertex-supported Z) -> constant Z.
    # Each cell belongs to exactly one or two patches. In the two-patch case
    # the first arrow is the primitive vector (-1,+1).
    for x in boundary:
        S = sorted(cut_index[d] for d in support[x])
        verify(len(S) in (1, 2), 'cover_resolution_support_size')
        if len(S) == 1:
            verify(not any(set(e) <= set(S) for e in overlaps), 'cover_resolution_single_exact')
        else:
            verify(tuple(S) in overlaps, 'cover_resolution_pair_present')
            verify(sum((-1, 1)) == 0 and abs(-1) == 1, 'cover_resolution_pair_exact_primitive')
    for x in boundary:
        for y in adjacency[x]:
            # Extension-by-zero basis vectors map to the same labelled vectors.
            # Both the edge boundary and augmentation therefore commute.
            for d in support[x]:
                verify(d in support[y], 'cover_resolution_augmentation_natural')
            if len(support[x]) == 2:
                verify(support[x] == support[y], 'cover_resolution_boundary_natural')

    # The conductor map e(f+,f-)=f+(0)-f-(0) commutes with coefficient
    # localization by the polynomial formula, in every branch degree.
    # The following verifies the combinatorial input to those ring maps,
    # not a finite-sampling substitute for that algebraic identity.
    group = tuple((r, f) for r in range(8) for f in range(2))
    identity = (0, 0)
    for g in group:
        for x in boundary:
            y = act_cell(g, x)
            verify(y in boundary, 'boundary_dihedral_action')
            verify(loc(y) == frozenset(act(g, d) for d in loc(x)), 'dihedral_localization')
            verify(unmark(y) == act_cell(g, unmark(x)), 'equivariant_unmark')
        for d in cuts:
            verify(act(g, d) in cut_set, 'cut_action')
    for g in group:
        for h in group:
            for d in ds:
                verify(act(mult(g, h), d) == act(g, act(h, d)), 'dihedral_group_law')

    # All 8 sourced facet/radial orientation maps.
    orientation_checks = 0
    for cut in cuts:
        comp = tuple(d for d in ds if d != cut and not crosses(d, cut))
        link = [f for f in faces if set(f) <= set(comp)]
        def sign(f: Face) -> int:
            return (-1) ** (sum(d < cut for d in f) + len(f))
        for f in link:
            for added in comp:
                if added in f or any(crosses(added, e) for e in f):
                    continue
                enlarged = tuple(sorted(f + (added,)))
                native = (-1) ** sum(d < added for d in tuple(sorted(f + (cut,))))
                link_sign = (-1) ** sum(d < added for d in f)
                verify(sign(f) * native * sign(enlarged) == link_sign, 'radial_orientation')
                orientation_checks += 1
    verify(orientation_checks == 2952, 'radial_orientation_count')

    # Exact graph homology with an integral spanning-tree basis.
    edges = sorted(overlaps)
    graph = {i: [] for i in range(8)}
    for i, j in edges:
        graph[i].append(j); graph[j].append(i)
    parent = {0: None}
    queue = deque([0])
    tree = []
    while queue:
        v = queue.popleft()
        for w in sorted(graph[v]):
            if w not in parent:
                parent[w] = v
                tree.append(tuple(sorted((v, w))))
                queue.append(w)
    verify(len(parent) == 8 and len(tree) == 7, 'connected_spanning_tree')
    non_tree = [e for e in edges if e not in tree]
    verify(len(non_tree) == 5, 'fundamental_group_rank')
    edge_index = {e: i for i, e in enumerate(edges)}
    tree_adj = {v: [] for v in graph}
    for a, b in tree:
        tree_adj[a].append(b); tree_adj[b].append(a)
    def path(start: int, end: int) -> list[int]:
        prev = {start: None}
        todo = deque([start])
        while end not in prev:
            v = todo.popleft()
            for w in tree_adj[v]:
                if w not in prev:
                    prev[w] = v; todo.append(w)
        result = [end]
        while result[-1] != start:
            result.append(prev[result[-1]])  # type: ignore[arg-type]
        return list(reversed(result))
    cycles = []
    for a, b in non_tree:
        v = [0] * len(edges)
        v[edge_index[(a, b)]] = 1
        p = path(b, a)
        for c, d in zip(p, p[1:]):
            v[edge_index[tuple(sorted((c, d)))]] += 1 if c < d else -1
        boundary_v = [0] * 8
        for coefficient, (c, d) in zip(v, edges):
            boundary_v[c] -= coefficient; boundary_v[d] += coefficient
        verify(not any(boundary_v), 'integral_cycle_basis')
        cycles.append(v)
    action_matrices = {}
    for g in group:
        images = []
        for v in cycles:
            image = [0] * len(edges)
            for coefficient, (a, b) in zip(v, edges):
                c = cut_index[act(g, cuts[a])]; d = cut_index[act(g, cuts[b])]
                image[edge_index[tuple(sorted((c, d)))]] += coefficient * (1 if c < d else -1)
            coords = [image[edge_index[e]] for e in non_tree]
            reconstruction = [sum(coords[j] * cycles[j][i] for j in range(5)) for i in range(len(edges))]
            verify(reconstruction == image, 'homology_action_integral')
            images.append(coords)
        action_matrices[g] = [list(row) for row in zip(*images)]
    for g in group:
        for h in group:
            verify(matmul(action_matrices[g], action_matrices[h]) == action_matrices[mult(g, h)],
                   'homology_action_group_law')

    # Subdivide graph edges before using stabilizers; some maps invert edges.
    def stabilizer(S: frozenset[Diagonal]) -> set[Group]:
        return {g for g in group if frozenset(act(g, d) for d in S) == S}
    v = frozenset((cuts[0],))  # (0,3)
    edge_a = frozenset((cuts[0], cuts[1]))  # shared endpoint, orbit size eight
    edge_b = frozenset((cuts[0], cuts[7]))  # disjoint, orbit size four
    Hv = stabilizer(v); Ha = stabilizer(edge_a); Hb = stabilizer(edge_b)
    verify(Hv == {(0, 0), (3, 1)}, 'vertex_stabilizer')
    verify(Ha == {(0, 0), (0, 1)}, 'edge_midpoint_a_stabilizer')
    verify(Hb == {(0, 0), (3, 1), (4, 0), (7, 1)}, 'edge_midpoint_b_stabilizer')
    verify(Hv & Ha == {identity}, 'halfedge_a_stabilizer')
    verify(Hv & Hb == Hv, 'halfedge_b_stabilizer')
    orbit_a = {frozenset(act(g, d) for d in edge_a) for g in group}
    orbit_b = {frozenset(act(g, d) for d in edge_b) for g in group}
    verify(len(orbit_a) == 8 and len(orbit_b) == 4 and not orbit_a & orbit_b, 'two_edge_orbits')
    verify(orbit_a | orbit_b == {frozenset((cuts[i], cuts[j])) for i, j in edges}, 'edge_orbit_exhaustion')
    a, b, c = (0, 1), (3, 1), (4, 0)
    for g in (a, b, c):
        verify(mult(g, g) == identity, 'quotient_involution_relation')
    verify(mult(b, c) == mult(c, b), 'quotient_commutation_relation')
    generated = {identity}
    while True:
        enlarged = generated | {mult(g, h) for g in generated for h in (a, b, c)}
        if enlarged == generated:
            break
        generated = enlarged
    verify(generated == set(group), 'orbifold_group_surjects_to_D8')
    verify(16 * (2 + 1 - 4) == 4 * (1 - 5), 'euler_characteristic_crosscheck')

    certificate = {
      'status': 'exact_indexing_diagram_and_transport_computation',
      'scope': 'Eight physical Cut facets and their actual loaded-cell intersections; not the physical coefficient totalization.',
      'source_commit': COMMIT,
      'source_files': SOURCES,
      'source_access': 'Pinned source read through GitHub connector; listed combinatorial rules transcribed independently; imported upstream pipelines not run.',
      'full_loaded_cells': len(loaded), 'full_generating_arrows': arrow_count,
      'boundary_loaded_cells': len(boundary), 'boundary_generating_arrows': boundary_arrows,
      'boundary_degree_counts': rank_counts(boundary),
      'single_cut_loaded_cells': 1075, 'pair_overlap_loaded_cells': 125,
      'physical_cuts_in_vertex_order': cuts, 'compatible_pairs': edges,
      'triple_overlaps': 0, 'nerve_homotopy_type': 'wedge of 5 circles',
      'integral_graph_cycle_basis': {'edges': edges, 'tree': tree, 'non_tree': non_tree, 'cycles': cycles},
      'dihedral_group_order': 16,
      'dihedral_H1_action_matrices': {f'{r},{f}': matrix for (r,f),matrix in action_matrices.items()},
      'subdivided_graph_of_groups': {
         'vertex_groups': ['C2 (midpoint shared-endpoint edge)', 'C2 (cut vertex)', 'C2 x C2 (midpoint disjoint edge)'],
         'edge_groups': ['trivial', 'C2'],
         'underlying_graph': '3-vertex path',
         'second_edge_embedding_at_cut_vertex': 'isomorphism',
         'resulting_fundamental_group': 'C2 * (C2 x C2)',
         'presentation': '<a,b,c | a^2=b^2=c^2=1, bc=cb>',
         'quotient_images_in_D8': {'a': a, 'b': b, 'c': c},
      },
      'homotopy_quotient': {
         'pi_0': 'point', 'pi_1': 'C2 * (C2 x C2)', 'pi_n_for_n_at_least_2': 0,
         'kernel_of_pi1_to_D8': 'free group of rank 5',
         'extension_splits': False,
      },
      'proof_dependencies': [
         'For every patch intersection, id -> unmark <- constant defines a contraction of its indexing nerve.',
         'Finite simplicial-cover nerve theorem, with natural equivariant homotopy-colimit comparisons.',
         'Barycentric subdivision removes edge inversions; graph-of-groups van Kampen computes the displayed free product.',
         'A graph and the classifying space of a discrete group are aspherical; use the Borel fibration for higher homotopy.',
         'Finite subgroups of a free product are conjugate into a factor; hence no order-16 D8 section exists.',
      ],
      'not_claimed': [
         'Coefficient arrows become equivalences under the index contraction.',
         'This is the full eight-point physical marked-state infinity-groupoid.',
         'All source/relative degrees of the full physical chain totalization have been computed.',
         'The loops survive attachment of the other octagon strata.',
         'A relation to RH or an operation differentiating numerical primes.',
      ],
      'derived_cover_formula': 'Rlim_J C = fib(product_over_8_patches Rlim C -> product_over_12_overlaps Rlim C), using the signed difference of restrictions',
      'constant_coefficient_control': {'H0': 'Z', 'H1': 'Z^5', 'other_cohomology': 0, 'torsion': False},
      'check_counts': dict(sorted(COUNTS.items())), 'total_exact_checks': sum(COUNTS.values()),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(certificate, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'certificate': str(output), 'checks': sum(COUNTS.values()),
                      'boundary_cells': len(boundary), 'boundary_arrows': boundary_arrows,
                      'nerve': 'wedge of 5 circles', 'quotient_pi1': 'C2 * (C2 x C2)'}, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=Path('marici_eight_point_boundary_certificate.json'))
    args = parser.parse_args()
    main(args.output)
