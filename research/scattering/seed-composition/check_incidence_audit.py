"""Exact, finite linearization of the supplied path candidate; no physical admission.

R copies labelled primitive cochain coordinates to retained path-use slots.
B sums those coordinates along each displayed edge. B.T is chain expansion.
Neither carrier is asserted to be the source's physical state space.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse
import hashlib
import json

from check_seed_composition_net import check_paths, load

ROOT = Path(__file__).resolve().parents[3]
BASE = Path(__file__).resolve().parent
DEST = BASE / 'results/incidence-audit.v1.json'


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    assert a and b and len(a[0]) == len(b)
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in transpose(b)] for row in a]


def apply(a, v):
    return [sum((x*y for x, y in zip(row, v)), F(0)) for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def rank(a):
    a = [[F(x) for x in row] for row in a]
    pivot_row = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(pivot_row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[pivot_row], a[pivot] = a[pivot], a[pivot_row]
        divisor = a[pivot_row][col]
        a[pivot_row] = [x/divisor for x in a[pivot_row]]
        for i in range(len(a)):
            if i != pivot_row:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[pivot_row])]
        pivot_row += 1
        if pivot_row == len(a):
            break
    return pivot_row


def audit():
    c = load(BASE / 'three-vertex-candidate.v1.json')
    check_paths(c)
    primitives = [(owner, a, b) for owner, cycle in c['primitive_cycles'].items() for a, b in zip(cycle, cycle[1:])]
    endpoints = [(a, b) for _, a, b in primitives]
    assert len(set(endpoints)) == 10  # Endpoint lookup is unambiguous for this frozen fixture only.
    composites = {tuple(p['edge']): p['path'] for p in c['displayed_composites']}
    displayed, uses = [], []
    for pair_index, pair in enumerate(c['displayed_triangle_pairs']):
        for triangle_index, triangle in enumerate(pair):
            for a, b in zip(triangle, triangle[1:]):
                path = composites.get((a, b), [a, b])
                edge_index = len(displayed)
                displayed.append({'pair': pair_index, 'triangle': triangle_index, 'edge': [a, b], 'path': path})
                for position, edge in enumerate(zip(path, path[1:])):
                    primitive = endpoints.index(edge)
                    uses.append({'displayed_edge': edge_index, 'path_position': position, 'primitive': primitive, 'owner': primitives[primitive][0]})
    R = [[F(use['primitive'] == j) for j in range(10)] for use in uses]
    S = [[F(use['displayed_edge'] == i) for use in uses] for i in range(12)]
    B = mm(S, R)
    multiplicity = [sum(row[j] for row in R) for j in range(10)]
    assert multiplicity == [3, 3, 1, 1, 1, 1, 1, 1, 3, 3]
    decoder = [[R[k][j]/multiplicity[j] for k in range(18)] for j in range(10)]
    assert rank(R) == 10 and mm(decoder, R) == eye(10)
    P = mm(R, decoder)
    assert mm(P, P) == P and transpose(P) == P and rank(P) == 10
    gram = mm(transpose(R), R)
    assert gram == [[multiplicity[i] if i == j else F(0) for j in range(10)] for i in range(10)]
    W = [[F(i == j)/multiplicity[uses[i]['primitive']] for j in range(18)] for i in range(18)]
    assert mm(transpose(R), mm(W, R)) == eye(10)
    R1, R2 = R[:9], R[9:]
    assert rank(R1) == rank(R2) == 7 and rank(mm(R1, transpose(R2))) == 4
    assert rank(R1)+rank(R2)-rank(R) == 4
    assert rank(B) == 8 and rank(B[:6]) == rank(B[6:]) == 5

    # A changed duplicate is not a valid retained encoding of any input.
    hostile = [F(0)]*18
    hostile[0] = 1
    assert apply(P, hostile) != hostile
    # Two independent additive readout losses; retaining these residuals repairs
    # this finite observer, not the missing source geometry or dynamics.
    residuals = [[F(j == 2)-F(j == 3) for j in range(10)],
                 [F(j == 5)-F(j == 6) for j in range(10)]]
    assert all(apply(B, v) == [0]*12 for v in residuals)
    assert rank(residuals) == 2 and rank(B+residuals) == 10
    assert apply(R, residuals[0]) != [0]*18

    # Complete compatibility equations for im(B), in the displayed row order.
    C = [[F(j == 5)-F(j == 0)-F(j == 1) for j in range(12)],
         [F(j == 2)-F(j == 9)-F(j == 10) for j in range(12)],
         [F(j == 8)-F(j == 2) for j in range(12)],
         [F(j == 11)-F(j == 5) for j in range(12)]]
    assert rank(C) == 4 and mm(C, B) == [[0]*10 for _ in range(4)]

    # Cochain readout transpose is the actual directed chain expansion. It
    # preserves endpoints; this does NOT attach any two-cells.
    vertices = sorted({v for e in endpoints for v in e})
    boundary = [[F(v == b)-F(v == a) for a, b in endpoints] for v in vertices]
    display_boundary = [[F(v == e['edge'][1])-F(v == e['edge'][0]) for e in displayed] for v in vertices]
    assert mm(boundary, transpose(B)) == display_boundary
    triangle_columns = [[F(i//3 == t) for t in range(4)] for i in range(12)]
    expanded_triangles = mm(transpose(B), triangle_columns)
    assert mm(boundary, expanded_triangles) == [[0]*4 for _ in vertices]
    assert rank(expanded_triangles) == 3
    assert transpose(expanded_triangles)[0] == transpose(expanded_triangles)[3]

    # Recheck the exact photon reference plane against its endpoint incidence;
    # do not execute source-owner checkers that rewrite their own receipts.
    source = load(ROOT / 'research/nima/results/photon-two-packet-candidate.json')
    assert source['packet_order'] == ['AB', 'BC', 'CA', 'BA', 'AD', 'DB']
    U = [[F(z['real']), F(z['imaginary_sqrt3_coefficient'])] for z in source['candidate_plus']['coefficients']]
    assert U == [[1, 0], [-1, 0], [F(1, 2), F(1, 2)], [-1, 0], [1, 0], [-F(1, 2), -F(1, 2)]]
    reference_edges = [('A','B'), ('B','C'), ('C','A'), ('B','A'), ('A','D'), ('D','B')]
    K = [[F(a == previous_b) for _, previous_b in reference_edges] for a, _ in reference_edges]
    T = [[-F(1, 2), F(1, 2)], [-F(3, 2), -F(1, 2)]]
    assert rank(U) == 2 and mm(K, U) == mm(U, T) and mm(T, mm(T, T)) == eye(2)
    # Shared-edge relabellings: (A,B,C,D)->(C,A,B,E), (C,A,Dp,B).
    orders = [[2, 0, 1, 5, 3, 4], [8, 6, 7, 11, 9, 10]]
    relabellings = [{'A':'C','B':'A','C':'B','D':'E'}, {'A':'C','B':'A','C':'Dp','D':'B'}]
    V = [[F(0)]*4 for _ in range(12)]
    for block, (order, relabel) in enumerate(zip(orders, relabellings)):
        assert [displayed[i]['edge'] for i in order] == [[relabel[a], relabel[b]] for a, b in reference_edges]
        for source_row, displayed_row in enumerate(order):
            V[displayed_row][2*block:2*block+2] = U[source_row]
    T4 = [[T[i%2][j%2] if i//2 == j//2 else F(0) for j in range(4)] for i in range(4)]
    CV = mm(C, V)
    assert rank(V) == 4 and rank(CV) == 3
    line = [F(1), F(-1), F(1), F(-1)]
    assert apply(CV, line) == [0]*4
    assert apply(CV, apply(T4, line)) != [0]*4
    assert rank(CV+mm(CV, T4)) == 4  # No nonzero one-step-stable mode in this image.
    input_witness = [-1, 0, 1, 0, 0, -1, 0, 0, 1, 0]
    assert apply(B, input_witness) == apply(V, line)

    dependencies = ['research/scattering/seed-composition/three-vertex-candidate.v1.json',
                    'research/scattering/seed-composition/check_seed_composition_net.py',
                    'research/scattering/seed-composition/check_incidence_audit.py',
                    'research/strominger/photon-shared-edge-seed.md',
                    'research/strominger/positron-reversed-electron-seed.md',
                    'research/nima/results/photon-two-packet-candidate.json',
                    'research/nima/checkers/check_photon_two_packet_candidate.py',
                    'research/nima/checkers/check_whole_seed_occurrence_spectrum.py']
    return {
        'schema': 'marici.scattering.seed-incidence-audit.v1',
        'status': 'exact_finite_linear_audit_passed_not_source_realization',
        'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in dependencies},
        'carrier': 'free rational primitive cochains; retained-use direct sum; additive displayed-edge observer, not a physical Hilbert or tensor-product identification',
        'primitive_order': [{'owner': owner, 'edge': [a, b]} for owner, a, b in primitives],
        'displayed_order': displayed, 'retained_uses': uses,
        'matrices': {'retained_copy_R': R, 'path_sum_S': S, 'additive_observer_B': B,
                     'retained_decoder': decoder, 'display_compatibility_C': C,
                     'residual_observer': residuals, 'expanded_triangle_chains': expanded_triangles,
                     'reference_mode_frame_U': U, 'reference_mode_step_T': T,
                     'displayed_mode_frame_V': V, 'mode_compatibility_CV': CV},
        'retained': {'dimension': 18, 'rank': 10, 'multiplicities': multiplicity,
                     'image_codimension': 8, 'pair_ranks': [7, 7], 'shared_input_dimension': 4,
                     'raw_counting_isometry': False, 'reciprocal_multiplicity_weighted_isometry': True,
                     'weighted_metric_is_physical': False, 'altered_duplicate_rejected': True},
        'additive': {'dimension': 12, 'rank': 8, 'kernel_dimension': 2,
                     'pair_ranks': [5, 5], 'compatibility_rank': 4,
                     'residual_augmented_rank': 10, 'boundary_square_commutes': True,
                     'expanded_triangle_rank': 3, 'first_and_fourth_triangle_same_chain': True},
        'mode_test': {'scope': 'only additive B with stated shared-edge relabellings and reference continuation',
                      'two_plane_dimension': 4, 'intersection_with_B_image_dimension': 1,
                      'intersection_parameters': ['s', '-s', 's', '-s'],
                      'one_step_stable_subspace_dimension': 0, 'input_witness': input_witness,
                      'first_step_constraint_defect': apply(CV, apply(T4, line))},
        'boundary': {'source_authorized_encoder_constructed': False, 'independent_photons_constructed': False,
                     'triangle_faces_constructed': False, 'physical_metric_identified': False,
                     'all_possible_encoders_rejected': False, 'physical_annihilation_derived': False,
                     'ratio_372_derived': False, 'formal_outcomes_admitted': False},
        'next_gate': 'Find a source-authorized retained-path operation with explicit residuals and a commuting continuation square; do not use additive path sums as photon-mode transport.'
    }


def encode(value):
    if isinstance(value, F):
        return value.numerator if value.denominator == 1 else str(value)
    raise TypeError(type(value).__name__)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check', action='store_true', help='compare against committed receipt without writing')
    args = parser.parse_args()
    report = audit()
    rendered = json.dumps(report, indent=2, default=encode)+'\n'
    if args.check:
        if not DEST.exists() or DEST.read_text(encoding='utf-8') != rendered:
            raise SystemExit('FAIL: incidence receipt missing or stale; rerun checker without --check')
    else:
        DEST.parent.mkdir(parents=True, exist_ok=True)
        DEST.write_text(rendered, encoding='utf-8')
    print('PASS: R rank 10; pair ranks 7+7 with 4 shared coordinates; B rank 8 with 2 residuals.')
    print('PASS: additive photon-plane intersection is one-dimensional and has no nonzero continuation-stable subspace.')
    print('Boundary: finite linear observer obstruction only; no source/physical/proof promotion.')


if __name__ == '__main__':
    main()
