"""Oriented P4 chains and their exact event-signature observations.

Run with: uv run --with sympy python <this file>
The checker certifies finite incidence and signature identities. The analytical
extension uses the separately established bounded theta synthesis maps.
"""
from itertools import combinations, permutations
from pathlib import Path
import json
import sys

import sympy as sp

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/grothendieck'))
from theta_interval_signature import observe_route


def serial(matrix):
    return [[str(v) for v in matrix.row(i)] for i in range(matrix.rows)]


def main():
    routes = list(permutations(range(4)))
    index = {w: i for i, w in enumerate(routes)}
    edges_with_slot = {}
    for i, w in enumerate(routes):
        for j in range(3):
            v = list(w)
            v[j], v[j+1] = v[j+1], v[j]
            edge = tuple(sorted((i, index[tuple(v)])))
            edges_with_slot[edge] = j + 1
    edges = sorted(edges_with_slot)
    edge_index = {e: i for i, e in enumerate(edges)}
    d1 = sp.zeros(24, len(edges))
    for j, (a, b) in enumerate(edges):
        d1[a, j], d1[b, j] = -1, 1
    faces = []
    for size in (1, 2, 3):
        for subset in combinations(range(4), size):
            members = [i for i, w in enumerate(routes) if set(w[:size]) == set(subset)]
            adjacency = {v: [] for v in members}
            for a, b in edges:
                if a in adjacency and b in adjacency:
                    adjacency[a].append(b)
                    adjacency[b].append(a)
            assert all(len(ns) == 2 for ns in adjacency.values())
            start = min(members)
            cycle = [start, min(adjacency[start])]
            while True:
                nxt = next(v for v in adjacency[cycle[-1]] if v != cycle[-2])
                if nxt == start:
                    break
                assert nxt not in cycle
                cycle.append(nxt)
            assert set(cycle) == set(members)
            faces.append({'first_block': list(subset),
                          'second_block': sorted(set(range(4)) - set(subset)),
                          'cycle': cycle,
                          'kind': 'square' if size == 2 else 'hexagon'})
    d2 = sp.zeros(36, 14)
    alternating = sp.zeros(24, 14)
    for j, face in enumerate(faces):
        cycle = face['cycle']
        for k, a in enumerate(cycle):
            b = cycle[(k+1) % len(cycle)]
            edge = tuple(sorted((a, b)))
            d2[edge_index[edge], j] = 1 if a < b else -1
            alternating[a, j] = (-1)**k
        face['generator_cycle'] = [edges_with_slot[tuple(sorted((cycle[k], cycle[(k+1) % len(cycle)])))] for k in range(len(cycle))]
        if face['kind'] == 'square':
            assert face['generator_cycle'] in ([3, 1, 3, 1], [1, 3, 1, 3])
        else:
            word = face['generator_cycle']
            assert len(set(word)) == 2 and abs(word[0]-word[1]) == 1
            assert word == [word[0], word[1]] * 3
    assert d1 * d2 == sp.zeros(24, 14)
    null = d2.nullspace()
    assert len(null) == 1
    d3 = null[0] / null[0][0]
    assert all(abs(x) == 1 for x in d3)
    assert d2 * d3 == sp.zeros(36, 1)
    assert (d1.rank(), d2.rank(), d3.rank()) == (23, 13, 1)

    prior = json.loads((ROOT / 'research/voevodsky/results/theta-hidden-channel-transport.json').read_text())
    assert prior['route_order'] == [list(w) for w in routes]
    parity = sp.Matrix(prior['parity_basis_K']).applyfunc(sp.Rational)
    squares = [j for j, f in enumerate(faces) if f['kind'] == 'square']
    hexagons = [j for j, f in enumerate(faces) if f['kind'] == 'hexagon']
    square_match = []
    for j in squares:
        matches = [(k, sign) for k in range(6) for sign in (-1, 1)
                   if alternating[:, j] == sign * parity[:, k]]
        assert len(matches) == 1
        k, sign = matches[0]
        assert faces[j]['first_block'] == prior['blocks'][k][0]
        square_match.append({'face': j, 'parity_column': k, 'sign': sign})
    # Global route antisymmetry has three exact facet decompositions.
    def permutation_sign(w):
        return (-1) ** sum(w[i] > w[j] for i in range(4) for j in range(i+1, 4))
    sign_vector = sp.Matrix([permutation_sign(w) for w in routes])
    facet_signs = [permutation_sign(routes[f['cycle'][0]]) for f in faces]
    for size in (1, 2, 3):
        total = sp.zeros(24, 1)
        for j, face in enumerate(faces):
            if len(face['first_block']) == size:
                total += facet_signs[j] * alternating[:, j]
        assert total == sign_vector
    # Route reversal is central reflection of P4. It exchanges opposite
    # square faces and reverses the orientation of the three-cell.
    reverse = [index[tuple(reversed(w))] for w in routes]
    reversal0 = sp.zeros(24)
    for i, j in enumerate(reverse):
        reversal0[j, i] = 1
    reversal1 = sp.zeros(36)
    for j, (a, b) in enumerate(edges):
        x, y = reverse[a], reverse[b]
        reversal1[edge_index[tuple(sorted((x, y)))], j] = 1 if x < y else -1
    reversal2 = sp.zeros(14)
    for j, face in enumerate(faces):
        target = next(k for k, other in enumerate(faces)
                      if other['first_block'] == face['second_block'])
        mapped = reversal1 * d2[:, j]
        signs = [sign for sign in (-1, 1) if mapped == sign * d2[:, target]]
        assert len(signs) == 1
        reversal2[target, j] = signs[0]
    assert reversal0 * d1 == d1 * reversal1
    assert reversal1 * d2 == d2 * reversal2
    assert reversal2 * d3 == -d3
    parity_reversal = parity.T * reversal0 * parity / 4
    assert reversal0 * parity == parity * parity_reversal
    assert parity_reversal ** 2 == sp.eye(6)
    assert len((parity_reversal - sp.eye(6)).nullspace()) == 3
    assert len((parity_reversal + sp.eye(6)).nullspace()) == 3
    sigs = [observe_route(w) for w in routes]
    keys = [sorted(set().union(*(set(sig[d]) for sig in sigs))) for d in range(5)]
    matrices = [sp.Matrix([[sig[d].get(k, 0) for sig in sigs] for k in keys[d]]) for d in range(5)]
    observations = []
    for d, M in enumerate(matrices):
        # Edge observations are M*d1; every polygonal loop closes exactly.
        assert M * d1 * d2 == sp.zeros(M.rows, 14)
        sq, hx = M * alternating[:, squares], M * alternating[:, hexagons]
        if d <= 3:
            assert sq == sp.zeros(M.rows, 6)
        observations.append({'degree': d, 'square_vertex_rank': sq.rank(),
                             'hexagon_vertex_rank': hx.rank(),
                             'joint_vertex_rank': (M * alternating).rank()})

    # A canonical continuous filling uses barycentric subdivision: assign each
    # cell's barycenter the uniform probability mixture of its vertices.
    cells = [frozenset([i]) for i in range(24)] + [frozenset(e) for e in edges] + [frozenset(f['cycle']) for f in faces] + [frozenset(range(24))]
    cell_index = {v: i for i, v in enumerate(cells)}
    full = len(cells) - 1
    centroids = sp.zeros(24, len(cells))
    for j, cell in enumerate(cells):
        for v in cell:
            centroids[v, j] = sp.Rational(1, len(cell))
        assert sum(centroids[:, j]) == 1
    flags = []
    for face in faces:
        F = frozenset(face['cycle'])
        for edge in edges:
            E = frozenset(edge)
            if E <= F:
                for v in edge:
                    flags.append([cell_index[frozenset([v])], cell_index[E], cell_index[F], full])
    assert len(flags) == 144 and len(set(map(tuple, flags))) == 144
    # Restrictions agree because every shared barycentric vertex has one
    # global source vector; an affine map is fixed by its vertex values.
    for flag in flags:
        assert all(cells[a] < cells[b] for a, b in zip(flag, flag[1:]))

    result = {
        'schema': 'marici.voevodsky.theta-permutohedral-three-cell.v1',
        'passed': True,
        'route_order': [list(w) for w in routes],
        'edges': [{'vertices': list(e), 'swap_slot': edges_with_slot[e]} for e in edges],
        'faces': faces,
        'boundary_ranks': [23, 13, 1],
        'betti_numbers_boundary_sphere': [1, 0, 1],
        'betti_numbers_filled_ball': [1, 0, 0, 0],
        'd1': serial(d1), 'd2': serial(d2), 'd3': serial(d3),
        'square_parity_matches': square_match,
        'facet_signs_for_global_antisymmetry': facet_signs,
        'global_antisymmetry_identity': 'The signed alternating vertex sums over each facet size 1, 2, or 3 separately equal the global route-sign vector.',
        'parity_reversal': serial(parity_reversal),
        'parity_reversal_eigenspace_dimensions': {'even': 3, 'odd': 3},
        'three_cell_reversal_sign': -1,
        'alternating_vertex_matrix': serial(alternating),
        'alternating_vertex_ranks': {'squares': alternating[:, squares].rank(),
                                    'hexagons': alternating[:, hexagons].rank(),
                                    'all_faces': alternating.rank()},
        'alternating_vertex_relations': [serial(v) for v in alternating.nullspace()],
        'observations': observations,
        'barycentric_cells': [sorted(cell) for cell in cells],
        'barycentric_tetrahedra': flags,
        'scope': 'Exact finite route combinatorics and linear signature observations. PL theta filling follows by bounded synthesis; no independent arithmetic successor, signed-form isometry, or nontrivial homotopy group is certified.',
    }
    out = ROOT / 'research/voevodsky/results/theta-permutohedral-three-cell.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({k: result[k] for k in ('passed', 'boundary_ranks', 'betti_numbers_boundary_sphere', 'betti_numbers_filled_ball', 'square_parity_matches', 'alternating_vertex_ranks', 'observations')}, indent=2))
    print('barycentric tetrahedra:', len(flags))


if __name__ == '__main__':
    main()
