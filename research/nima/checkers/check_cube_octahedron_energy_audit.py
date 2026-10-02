"""Cube/octahedron source eigenlines and architecture-independent trial energy.

No external packages or measured constants. Matrix and polynomial identities are
exact over Q(i*sqrt(3)) and Z; printed decimal gaps have certified rational bounds.
The shared-edge Laplacian and uniform coupling/penalty are declared trial dynamics,
not a derived physical Hamiltonian. No previously generated reports are needed.
"""
from collections import Counter, defaultdict
from fractions import Fraction as F
from itertools import product
from math import isqrt
from pathlib import Path
import json

from check_octahedral_monomial_projectors import (
    closure, QUARTER, C, AXES, I, ONE, ZERO, OMEGA,
    mm, mv, transpose, det, inv, cross, sub, dot, boundary,
    zadd, zmul, zconj, zscale, znorm, zmv, projector,
    operators, sparse_product, sparse_adjoint, sparse_apply,
)

ROOT = Path(__file__).resolve().parents[1]


def add_sparse(*matrices):
    out = {}
    for matrix in matrices:
        for key, value in matrix.items():
            out[key] = zadd(out.get(key, ZERO), value)
    return {k: v for k, v in out.items() if v != ZERO}


def scale_sparse(matrix, weight):
    return {k: zscale(v, weight) for k, v in matrix.items() if weight}


def characteristic(matrix):
    """Faddeev-LeVerrier, integer arithmetic with checked exact divisions."""
    n = len(matrix)
    b = [[int(i == j) for j in range(n)] for i in range(n)]
    rows = [[(k, v) for k, v in enumerate(row) if v] for row in matrix]
    coefficients = [1]
    for order in range(1, n+1):
        ab = [[sum(v*b[k][j] for k, v in rows[i]) for j in range(n)] for i in range(n)]
        trace = sum(ab[i][i] for i in range(n))
        assert trace % order == 0
        coefficient = -trace//order
        coefficients.append(coefficient)
        for i in range(n):
            ab[i][i] += coefficient
        b = ab
    assert all(v == 0 for row in b for v in row)  # Cayley-Hamilton recurrence.
    return coefficients


def divide(poly, divisor):
    if len(poly) < len(divisor):
        return None
    remainder = list(poly)
    quotient = []
    for i in range(len(poly)-len(divisor)+1):
        q = remainder[i]
        quotient.append(q)
        for j, v in enumerate(divisor):
            remainder[i+j] -= q*v
    return quotient if not any(remainder) else None


def multiply(a, b):
    out = [0]*(len(a)+len(b)-1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i+j] += x*y
    return out


def factor_spectrum(coefficients):
    # These cubic graph Laplacians have integer/quadratic factors. Failure to
    # factor completely is an explicit failure, not a numerical spectrum guess.
    remaining = coefficients
    factors = []
    candidates = [[1, -root] for root in range(7)]
    candidates += [[1, b, c] for b in range(-12, 1) for c in range(37)
                   if b*b-4*c > 0 and isqrt(b*b-4*c)**2 != b*b-4*c]
    for factor in candidates:
        multiplicity = 0
        while (quotient := divide(remaining, factor)) is not None:
            remaining = quotient
            multiplicity += 1
        if multiplicity:
            factors.append((factor, multiplicity))
    assert remaining == [1], remaining
    recovered = [1]
    roots = []
    precision = 10**12
    for factor, multiplicity in factors:
        for _ in range(multiplicity):
            recovered = multiply(recovered, factor)
        if len(factor) == 2:
            r = -factor[1]
            roots.append((str(r), F(r), F(r), multiplicity))
        else:
            _, b, c = factor
            discriminant = b*b-4*c
            low = F(isqrt(discriminant*precision**2), precision)
            high = low+F(1, precision)
            assert low*low <= discriminant < high*high
            roots.extend(((f'({-b}-sqrt({discriminant}))/2', (-b-high)/2, (-b-low)/2, multiplicity),
                          (f'({-b}+sqrt({discriminant}))/2', (-b+low)/2, (-b+high)/2, multiplicity)))
    assert recovered == coefficients
    assert sum(mult for _, _, _, mult in roots) == 24
    assert sum(mult for _, low, high, mult in roots if low == high == 0) == 1
    positives = [r for r in roots if r[1] > 0]
    gap = min(positives, key=lambda r: r[1])
    assert all(gap[2] < other[1] for other in positives if other is not gap)
    return {'characteristic_polynomial_descending': coefficients,
            'factors': [{'coefficients_descending': f, 'multiplicity': m} for f, m in factors],
            'gap': {'expression': gap[0], 'lower_bound': str(gap[1]), 'upper_bound': str(gap[2]),
                    'decimal_midpoint': float((gap[1]+gap[2])/2), 'multiplicity': gap[3]}}, gap


def graph_and_geometry(group, reference, expected):
    triangles = [tuple(mv(r, p) for p in reference) for r in group]
    points = set(p for t in triangles for p in t)
    assert len(set(triangles)) == 24 and len(points) == 14
    assert boundary(triangles) == {}
    owners = defaultdict(list)
    point_neighbors = defaultdict(set)
    volumes = []
    for i, tri in enumerate(triangles):
        normal = cross(sub(tri[1], tri[0]), sub(tri[2], tri[0]))
        assert dot(normal, tri[0]) > 0
        assert all(dot(normal, sub(p, tri[0])) <= 0 for p in points)
        volumes.append(det(transpose(tri))/6)
        for a, b in zip(tri, tri[1:]+tri[:1]):
            owners[tuple(sorted((a, b)))].append(i)
            point_neighbors[a].add(b)
            point_neighbors[b].add(a)
    assert len(owners) == 36 and all(len(v) == 2 for v in owners.values())
    assert set(volumes) == {expected['cone_volume']}
    assert sum(volumes) == expected['volume']
    assert Counter(len(v) for v in point_neighbors.values()) == expected['vertex_degrees']
    neighbors = [set() for _ in triangles]
    for a, b in owners.values():
        neighbors[a].add(b)
        neighbors[b].add(a)
    assert all(len(row) == 3 for row in neighbors)
    seen = {0}
    frontier = [0]
    while frontier:
        x = frontier.pop()
        for y in neighbors[x]-seen:
            seen.add(y)
            frontier.append(y)
    assert len(seen) == 24
    # The source incidence is equivariant, not an independently chosen graph.
    positions = {r: i for i, r in enumerate(group)}
    for a in group:
        perm = [positions[mm(a, r)] for r in group]
        assert all({perm[j] for j in neighbors[i]} == neighbors[perm[i]] for i in range(24))
    laplacian = [[3*int(i == j)-int(j in neighbors[i]) for j in range(24)] for i in range(24)]
    spectrum, gap = factor_spectrum(characteristic(laplacian))
    return {'vertices': 14, 'edges': 36, 'triangles': 24,
            'vertex_degree_histogram': dict(sorted(expected['vertex_degrees'].items())),
            'centroid_count': len({t[0] for t in triangles}),
            'volume': str(sum(volumes)), 'cone_volume': str(volumes[0]),
            'dual_graph_connected': True, 'dual_graph_degree': 3,
            'dual_graph_edges': [list(v) for _, v in sorted(owners.items())],
            'laplacian_spectrum': spectrum}, laplacian, gap


def audit(name, group, reference, expected):
    geometry, laplacian, gap = graph_and_geometry(group, reference, expected)
    x0 = transpose(reference)
    coeff = (ONE, OMEGA, zmul(OMEGA, OMEGA))
    v0 = zmv(x0, coeff)
    a0 = mm(mm(x0, C), inv(x0))
    assert zmv(a0, v0) == tuple(zmul(OMEGA, z) for z in v0)
    vectors, u, norm, local, alignment, collective = operators(group, v0)
    assert [len(a) for a in (local, alignment, collective)] == expected['supports']
    assert sum(z != ZERO for z in u) == expected['visible_coordinates']
    assert sparse_product(local, alignment) == sparse_product(alignment, local) == collective
    assert sparse_apply(collective, u) == u
    # Full support was also what made every original arrow belong to a closed
    # selected-mode traversal. The cube has unused normal-direction R arrows.
    covered = [set(), set(), set()]
    total_cycle_weight = ZERO
    for (i, k), closing in collective.items():
        middle = [b for b in range(72) if (b, i) in local and (k, b) in alignment]
        assert len(middle) == 1
        b = middle[0]
        weight = zmul(zmul(local[b, i], alignment[k, b]), closing)
        assert weight == (znorm(collective[k, i]), F(0)) and weight[0] > 0
        total_cycle_weight = zadd(total_cycle_weight, weight)
        covered[0].add((b, i))
        covered[1].add((k, b))
        covered[2].add((i, k))
    assert total_cycle_weight == ONE
    covered_counts = list(map(len, covered))
    assert covered_counts == ([96, 1152, 2304] if name == 'cube' else [216, 1728, 5184])
    pruned_alignment = {k: alignment[k] for k in covered[1]}
    assert sparse_product(pruned_alignment, local) == collective
    eye = {(i, i): ONE for i in range(72)}
    returned_dense = sparse_product(collective, sparse_product(alignment, local))
    returned_identity = sparse_product(eye, sparse_product(alignment, local))
    assert returned_dense == returned_identity == collective
    return_penalty = add_sparse(eye, scale_sparse(collective, -1))
    assert sparse_apply(return_penalty, u) == (ZERO,)*72
    assert sparse_product(return_penalty, return_penalty) == return_penalty
    assert sum(return_penalty.get((i, i), ZERO)[0] for i in range(72)) == 71

    # Connection Laplacian K_xz=D_xz rho(x)rho(z)^T. U removes its flat frame
    # transport. This energy uses shared-edge incidence, not coefficient support.
    frame = {(3*x+i, 3*x+j): (r[i][j], F(0)) for x, r in enumerate(group)
             for i, j in product(range(3), repeat=2) if r[i][j]}
    bare = {(3*x+i, 3*z+i): (F(laplacian[x][z]), F(0))
            for x, z in product(range(24), repeat=2) for i in range(3) if laplacian[x][z]}
    connection = sparse_product(sparse_product(frame, bare), sparse_adjoint(frame))
    assert sparse_product(sparse_adjoint(frame), frame) == eye
    assert sparse_product(sparse_product(sparse_adjoint(frame), connection), frame) == bare
    p0 = projector(v0)
    local_reference = {(3*x+i, 3*x+j): p0[i][j] for x in range(24)
                       for i, j in product(range(3), repeat=2) if p0[i][j] != ZERO}
    assert sparse_product(sparse_product(sparse_adjoint(frame), local), frame) == local_reference
    assert sparse_product(connection, local) == sparse_product(local, connection)
    local_penalty = add_sparse(eye, scale_sparse(local, -1))
    hamiltonian = add_sparse(connection, local_penalty)
    assert sparse_adjoint(hamiltonian) == hamiltonian
    assert sparse_apply(hamiltonian, u) == (ZERO,)*72
    assert sparse_product(hamiltonian, collective) == {}
    # Independent quadratic-form evaluation on the selected mode, a coordinate
    # basis probe, and a deterministic complex field; no random or fitted data.
    probes = (u, (ONE,)+(ZERO,)*71,
              tuple((F(i % 5-2, 3), F(i % 7-3, 4)) for i in range(72)))
    for probe in probes:
        pulled = [zmv(transpose(r), probe[3*x:3*x+3]) for x, r in enumerate(group)]
        edge_budget = sum(znorm(zadd(pulled[x][i], zscale(pulled[z][i], -1)))
                          for x in range(24) for z in range(x+1, 24)
                          if laplacian[x][z] == -1 for i in range(3))
        rejected = sparse_apply(local_penalty, probe)
        selection_budget = sum(znorm(z) for z in rejected)
        for a, b in ((F(1), F(1)), (F(1), F(1, 10)), (F(2), F(3))):
            trial = add_sparse(scale_sparse(connection, a), scale_sparse(local_penalty, b))
            image = sparse_apply(trial, probe)
            value = ZERO
            for v, w in zip(probe, image):
                value = zadd(value, zmul(zconj(v), w))
            assert value == (a*edge_budget+b*selection_budget, F(0))
            assert value[0] >= 0
    # The exact gauge reduction gives spectrum a*lambda (once) and
    # a*lambda+b (twice) for each scalar graph eigenvalue lambda, at a,b>0.
    assert 0 < gap[1] <= gap[2] < 1
    assert F(1, 10) < gap[1]  # Choosing b=1/10 erases the gap distinction.
    hs_squared = lambda a: sum(znorm(z) for z in a.values())
    assert [hs_squared(a) for a in (local, alignment, collective)] == [24, 3, 1]
    assert hs_squared(eye) == 72

    if name == 'cube':
        assert v0 == (ZERO, (F(0), F(1)), (F(-1), F(0)))
        # Adding a normal component repairs support but loses the geometric
        # omega eigenline. This is an explicit new choice, not a basis repair.
        supplied = (ONE, v0[1], v0[2])
        assert zmv(a0, supplied) != tuple(zmul(OMEGA, z) for z in supplied)
        _, _, _, full_l, full_r, full_n = operators(group, supplied)
        assert [len(a) for a in (full_l, full_r, full_n)] == [216, 1728, 5184]
        assert sparse_product(full_r, full_l) == full_n

    report = {'geometry': geometry,
              'reference_triangle_columns': [[str(a) for a in p] for p in reference],
              'selected_vector_Q_i_sqrt3': [[str(a), str(b)] for a, b in v0],
              'local_squared_norm': str(sum(znorm(z) for z in v0)),
              'assembled_squared_norm': str(norm),
              'selected_nonzero_coordinates': expected['visible_coordinates'],
              'stage_supports': expected['supports'],
              'dense_feedback_arrows': sum(expected['supports']),
              'closed_traversal_covered_supports': covered_counts,
              'closed_traversal_union': sum(covered_counts),
              'closed_traversal_weight_sum': '1',
              'pruning_uncovered_alignment_preserves_return': True,
              'identity_feedback_arrows': len(local)+len(alignment)+72,
              'feedback_return_operators_identical': True,
              'return_penalty_spectrum': {'0': 1, '1': 71},
              'squared_Hilbert_Schmidt_stage_costs': {'dense_feedback': 28, 'identity_feedback': 99},
              'trial_local_hamiltonian': {
                  'formula': 'H(a,b)=a*K+b*(I-L), a>0,b>0',
                  'source': 'uniform shared-edge triangle graph with flat spatial frame transport',
                  'frame_reduction_exact': True, 'kernel_dimension': 1,
                  'quadratic_form_identity_probes': 3, 'positive_coupling_pairs_tested': 3,
                  'collective_energy': '0',
                  'spectrum_rule': 'a*lambda once and a*lambda+b twice per scalar Laplacian eigenvalue lambda',
                  'gap_rule': 'min(a*lambda_1,b)',
                  'unit_coupling_gap': geometry['laplacian_spectrum']['gap'],
                  'gap_at_a_1_b_one_tenth': '1/10',
                  'not_selected': ['coupling ratio a/b', 'energy units', 'absolute energy offset', 'physical dynamics', 'particle sector']}}
    return report


def main():
    group = closure((QUARTER, C))
    assert len(group) == 24
    cube = (AXES[0], (F(1), F(1), F(1)), (F(1), F(-1), F(1)))
    octahedron = ((F(1, 3),)*3, AXES[0], AXES[1])
    cube_report = audit('cube', group, cube,
                        {'cone_volume': F(1, 3), 'volume': F(8), 'vertex_degrees': Counter({4: 6, 6: 8}),
                         'supports': [96, 1728, 2304], 'visible_coordinates': 48})
    octa_report = audit('octahedron', group, octahedron,
                        {'cone_volume': F(1, 18), 'volume': F(4, 3), 'vertex_degrees': Counter({3: 8, 8: 6}),
                         'supports': [216, 1728, 5184], 'visible_coordinates': 72})
    cs = cube_report['geometry']['laplacian_spectrum']
    os = octa_report['geometry']['laplacian_spectrum']
    assert cs['characteristic_polynomial_descending'] != os['characteristic_polynomial_descending']
    assert F(os['gap']['upper_bound']) < F(cs['gap']['lower_bound'])
    report = {'status': 'passed', 'arithmetic': 'exact rational, quadratic complex and integer polynomial arithmetic',
              'cube': cube_report, 'octahedron': octa_report,
              'conclusions': {
                  'same_symmetry_does_not_force_same_geometric_eigenline_support': True,
                  'native_cube_full_support_hypothesis_fails': True,
                  'cube_full_support_repair_changes_selected_line': True,
                  'source_incidence_distinguishes_graph_spectra': True,
                  'uniform_trial_energy_is_independent_of_feedback_implementation': True,
                  'physical_energy_scale_or_particle_mass_derived': False}}
    out = ROOT/'results'
    out.mkdir(exist_ok=True)
    (out/'cube-octahedron-energy-audit.json').write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
