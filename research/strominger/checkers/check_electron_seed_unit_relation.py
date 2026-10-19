"""Trace the existing electron seed and its unit scalar relation exactly.

Read the retained 144-arrow store and replay its producer in isolated output.
No shared writes, mass term, momentum assignment, physical constants or
additional occupied input.
"""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
import contextlib
import hashlib
import io
import json
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
SOURCE_CHECKERS = ROOT / 'research/voevodsky/checkers'
sys.path.insert(0, str(SOURCE_CHECKERS))
import check_electron_tetrahedral_spinor as producer
from check_electron_tetrahedral_spinor import (
    D, G0, G1, GI, ga, gs, gm, gc, gt, gmm, ident, adj, sm, ma, act,
    spin, trace, encode,
)


def subtract(a, b):
    return ga(a, gs(-1, b))


def read_scalar(z):
    return tuple(D(F(x[0]), F(x[1])) for x in z)


def encode_matrix(a):
    return [[encode(z) for z in row] for row in a]


def inner(a, b):
    return gt(gm(gc(x), y) for x, y in zip(a, b))


def outer(a):
    return tuple(tuple(gm(x, gc(y)) for y in a) for x in a)


def spin_conjugate(z):
    # C=-epsilon K; C^2=-I. A relation on the same logical seed, NOT an
    # independently occupied second electron or a proposed executable gate.
    return (gs(-1, gc(z[1])), gc(z[0]))


def pairing(z, w):
    return subtract(gm(z[0], w[1]), gm(z[1], w[0]))


def exterior(a):
    pairs = tuple(combinations(range(len(a)), 2))
    return tuple(tuple(subtract(gm(a[i][k], a[j][l]), gm(a[i][l], a[j][k]))
                       for k, l in pairs) for i, j in pairs)


def real_text(z):
    assert z[1] == 0
    x = z[0]
    if isinstance(x, D):
        assert x.b == 0
        return str(x.a)
    return str(x)


def main():
    paths = {
        'store': ROOT / 'research/voevodsky/results/electron_tetrahedral_spinor_store.json',
        'producer': SOURCE_CHECKERS / 'check_electron_tetrahedral_spinor.py',
        'report': ROOT / 'research/voevodsky/results/electron_tetrahedral_spinor.json',
        'prior': ROOT / 'research/voevodsky/results/electron_charge_spin_frontier.json',
        'geometry': ROOT / 'research/voevodsky/inputs/relative-electron.json',
        'pairing_note': ROOT / 'research/voevodsky/electron-pairing-coupling.md',
    }
    source_hashes = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in paths.values()}
    report = json.loads(paths['report'].read_text())
    assert report['verification_passed']
    historical_producer_matches = hashlib.sha256(paths['producer'].read_bytes()).hexdigest() == report['checker_sha256']
    assert hashlib.sha256(paths['prior'].read_bytes()).hexdigest() == report['source_sha256']
    store = json.loads(paths['store'].read_text())
    # Historical receipt pins a different producer revision. Fresh replay in
    # an isolated output directory resolves that drift without rewriting any
    # shared store. The upstream prerequisite itself is reused, not regenerated.
    previous_base = producer.BASE
    try:
        with tempfile.TemporaryDirectory(prefix='electron-seed-replay-') as tmp:
            producer.BASE = Path(tmp)
            target = producer.BASE / 'results'
            target.mkdir()
            (target / 'electron_charge_spin_frontier.json').write_bytes(paths['prior'].read_bytes())
            with contextlib.redirect_stdout(io.StringIO()):
                producer.main()
            replay_store = json.loads((target / 'electron_tetrahedral_spinor_store.json').read_text())
            replay_report = json.loads((target / 'electron_tetrahedral_spinor.json').read_text())
            assert replay_store == store and replay_report['verification_passed']
    finally:
        producer.BASE = previous_base
    P = tuple(tuple(tuple(read_scalar(z) for z in row) for row in p)
              for p in store['face_projectors'])
    checks = {'fresh_isolated_native_producer_replay_and_exact_store_equality': True}
    matrices = {s: [[G0] * 8 for _ in range(8)] for s in ('L', 'G', 'N')}
    for row in store['arrows']:
        s, i, j = row['stage'], row['target'], row['source']
        assert matrices[s][i][j] == G0
        matrices[s][i][j] = read_scalar(row['weight'])
    matrices = {s: tuple(tuple(row) for row in a) for s, a in matrices.items()}
    L, G, N = (matrices[s] for s in ('L', 'G', 'N'))
    L_recovered = tuple(tuple(P[i//2][i % 2][j % 2] if i//2 == j//2 else G0
                              for j in range(8)) for i in range(8))
    N_recovered = tuple(tuple(gs(F(1, 2), gmm(P[i//2], P[j//2])[i % 2][j % 2])
                              for j in range(8)) for i in range(8))
    assert L == L_recovered and G == N == N_recovered
    assert all(gmm(p, p) == p and adj(p) == p and trace(p) == G1 for p in P)
    assert tuple(tuple(gt(p[i][j] for p in P) for j in range(2)) for i in range(2)) == sm(2, ident(2))
    assert gmm(N, gmm(G, L)) == N
    checks['all_144_stored_coefficients_reconstructed_from_existing_face_seed'] = True

    # A=stack(P_i); J=A/sqrt(2). Avoid introducing sqrt(2) into the exact field.
    A = tuple(row for p in P for row in p)
    assert sm(F(1, 2), gmm(adj(A), A)) == ident(2)
    assert all(gmm(m, A) == A for m in matrices.values())
    supports = {s: sum(x != G0 for row in m for x in row) for s, m in matrices.items()}
    weighted_norms = {s: real_text(gt(gm(gc(x), x) for row in m for x in row))
                      for s, m in matrices.items()}
    assert supports == {'L': 16, 'G': 64, 'N': 64}
    assert weighted_norms == {'L': '4', 'G': '2', 'N': '2'}
    checks['logical_seed_is_preserved_isometrically_in_every_stage'] = True
    checks['144_support_entries_are_not_a_norm12_amplification'] = True

    # The antisymmetric relation between the TWO BASIS COMPONENTS of one
    # doublet is a one-dimensional determinant line. Its raw embedding is
    # w_(i,j)=(A_i0 A_j1-A_i1 A_j0)/2 = (J e0 wedge J e1)_(i,j).
    pairs = tuple(combinations(range(8), 2))
    w = tuple(gs(F(1, 2), subtract(gm(A[i][0], A[j][1]), gm(A[i][1], A[j][0])))
              for i, j in pairs)
    assert inner(w, w) == G1
    determinant_projector = exterior(N)
    assert determinant_projector == outer(w)
    assert adj(determinant_projector) == determinant_projector
    assert trace(determinant_projector) == G1
    # Equality to w w* and unit norm proves rank one and idempotence exactly.
    assert act(determinant_projector, w) == w
    for m in matrices.values():
        assert act(exterior(m), w) == w
    checks['raw_determinant_relation_has_exact_rank_one_and_weight_one'] = True
    checks['unit_relation_survives_all_three_existing_stages'] = True

    # Recover uniqueness, not merely invariance under a selected axis. Group
    # averaging of U tensor U projects onto the full invariant tensor space.
    quats = set()
    for k in range(4):
        for sign in (-1, 1):
            quats.add(tuple(F(sign if i == k else 0) for i in range(4)))
    quats.update(tuple(F(s, 2) for s in signs) for signs in product((-1, 1), repeat=4))
    mean_fundamental = tuple(tuple(G0 for _ in range(2)) for _ in range(2))
    mean_tensor = tuple(tuple(G0 for _ in range(4)) for _ in range(4))
    for q in sorted(quats):
        U = spin(q)
        assert subtract(gm(U[0][0], U[1][1]), gm(U[0][1], U[1][0])) == G1
        mean_fundamental = ma(mean_fundamental, sm(F(1, 24), U))
        tensor = tuple(tuple(gm(U[i//2][j//2], U[i % 2][j % 2]) for j in range(4))
                       for i in range(4))
        mean_tensor = ma(mean_tensor, sm(F(1, 24), tensor))
        # The retained rotation lift permutes faces as well as acting on spin.
        sigma = [ma(ident(2), sm(-2, p)) for p in P]
        permutation = [sigma.index(gmm(gmm(U, h), adj(U))) for h in sigma]
        T = tuple(tuple(U[i % 2][j % 2] if i//2 == permutation[j//2] else G0
                        for j in range(8)) for i in range(8))
        assert gmm(T, A) == gmm(A, U)
        assert act(exterior(T), w) == w
    assert mean_fundamental == tuple(tuple(G0 for _ in range(2)) for _ in range(2))
    Ui, Uj = spin((F(0), F(1), F(0), F(0))), spin((F(0), F(0), F(1), F(0)))
    assert gmm(gmm(gmm(Ui, Uj), adj(Ui)), adj(Uj)) == sm(-1, ident(2))
    # Any invariant one-dimensional spinor subspace would make this
    # commutator act as +1 there, contradicting the retained central -I.
    singlet = (G0, G1, gs(-1, G1), G0)
    assert mean_tensor == sm(F(1, 2), outer(singlet))
    checks['no_fixed_spinor_line_but_one_unique_bilinear_scalar_relation'] = True
    checks['unit_relation_is_preserved_by_all_24_actual_rotation_lifts'] = True

    samples = [
        (G1, G0), (G0, G1), ((F(3, 5), F(0)), (F(0), F(4, 5))),
        ((F(0), F(3, 5)), (F(4, 5), F(0))),
    ]
    sample_records = []
    for z in samples:
        assert inner(z, z) == G1
        Cz = spin_conjugate(z)
        assert spin_conjugate(Cz) == tuple(gs(-1, x) for x in z)
        assert pairing(z, Cz) == G1 and inner(z, Cz) == G0
        x, y = act(A, z), act(A, Cz)
        density = sm(F(1, 2), outer(x))
        assert trace(density) == G1 and gmm(density, density) == density
        assert gmm(N, density) == gmm(density, N) == density
        transported = tuple(gs(F(1, 2), subtract(gm(x[i], y[j]), gm(x[j], y[i])))
                            for i, j in pairs)
        assert transported == w
        assert pairing(tuple(gs(2, s) for s in z), spin_conjugate(tuple(gs(2, s) for s in z))) == (F(4), F(0))
        phased = tuple(gm(GI, s) for s in z)
        assert pairing(phased, spin_conjugate(phased)) == G1
        sample_records.append({'seed': [encode(s) for s in z], 'paired_scalar': '1',
                               'encoded_density_trace': '1', 'doubled_seed_scalar': '4'})
    checks['same_seed_supplies_scalar_one_without_a_second_occupied_electron'] = True
    checks['phase_invariant_but_amplitude_scaling_is_not_hidden'] = True

    # Trace the separately retained geometric seed as well, without pretending
    # that this five-cycle is the tetrahedral coefficient compiler.
    geometry = json.loads(paths['geometry'].read_text())
    metric = [list(map(F, r)) for r in geometry['metric']]
    gen = geometry['generators'][0]
    Q = [list(map(F, r)) for r in gen['matrix']]
    translation = list(map(F, gen['translation']))
    initial = list(map(F, geometry['seeds'][0]['point']))
    orbit = [initial]
    for _ in range(5):
        v = orbit[-1]
        orbit.append([sum(a*b for a, b in zip(row, v)) + t for row, t in zip(Q, translation)])
    assert orbit[-1] == initial and len(set(map(tuple, orbit[:-1]))) == 5
    lengths = []
    for a, b in zip(orbit, orbit[1:]):
        d = [x-y for x, y in zip(b, a)]
        lengths.append(sum(d[i]*metric[i][j]*d[j] for i in range(4) for j in range(4)))
    assert lengths == [F(8)]*5
    checks['existing_geometric_seed_traced_without_inventing_norm12'] = True

    result = {
        'status': 'passed', 'checks': checks,
        'producer_replay': {'historical_producer_hash_matches_current': historical_producer_matches,
                            'current_producer_checks_passed': len(replay_report['checks']),
                            'retained_store_exactly_reproduced': True,
                            'prerequisite': 'Existing frontier receipt reused, not regenerated.'},
        'coefficient_seed': 'A two-component spinor z, encoded by J_i=P_i/sqrt(2); no norm-12 seed.',
        'geometric_seed': {'generators': len(geometry['generators']), 'seed_points': len(geometry['seeds']),
                           'orbit': [[str(x) for x in v] for v in orbit],
                           'five_primitive_edge_squared_lengths': list(map(str, lengths)),
                           'scope': 'Separate pentachoron geometric source, not a derived 144-arrow coefficient protocol.'},
        'stage_support_counts': supports,
        'stage_sum_of_squared_coefficient_magnitudes': weighted_norms,
        'persistent_scalar': {'definition': 'B(z,Cz)=z0*conj(z0)+z1*conj(z1)=||z||^2',
                              'C': '(-conj(z1),conj(z0))',
                              'unit_seed_value': '1',
                              'general_seed_value': '||z||^2',
                              'bilinear_invariant_dimension': 1,
                              'invariant_single_spinor_dimension': 0},
        'raw_determinant_line': {'coordinate_order': [list(pair) for pair in pairs],
                                 'components': [encode(x) for x in w],
                                 'projector': encode_matrix(determinant_projector),
                                 'rank': 1, 'squared_norm': '1',
                                 'nonzero_raw_components': sum(x != G0 for x in w),
                                 'interpretation': 'Exterior square of one logical doublet, NOT a new occupied two-electron state or a selected one-dimensional electron spin subspace.'},
        'normalized_seed_examples': sample_records,
        'conjecture_progress': 'An exact persistent one-dimensional unit relation has been found within the existing construction and transported through its actual 144 coefficients. It is a concrete candidate for the proposed electron reference arrow weight.',
        'remaining_question': 'Does the model charge this persistent relation rather than the transfer entries, and what corresponding valuation gives proton/neutron weight 1836? The present audit adds no charging law.',
        'momentum_disposition': '144 is support count, not a computed |p|^2. The existing seed normalization and weighted coefficient norms do not identify it with momentum.',
    }
    for p in paths.values():
        assert hashlib.sha256(p.read_bytes()).hexdigest() == source_hashes[p.relative_to(ROOT).as_posix()]
    checks['all_shared_sources_unchanged'] = True
    # Pin the imported exact arithmetic and source traversal dependencies.
    dependencies = [SOURCE_CHECKERS / p for p in ('check_electron_charge_spin_frontier.py',
        'check_coupled_six_piece_belt.py',
        'check_belt_operator_inputs.py', 'check_geometric_cycle_reversal.py',
        'check_smaller_negative_flux_carrier.py')]
    for p in [Path(__file__).resolve(), *dependencies]:
        source_hashes[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    result['source_hashes'] = source_hashes
    output = ROOT / 'research/strominger/results/electron-seed-unit-relation.json'
    output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'passed', 'checks': len(checks), 'supports': supports,
                      'weighted_coefficient_norms': weighted_norms,
                      'persistent_relation_rank': 1, 'persistent_relation_squared_norm': '1',
                      'momentum_squared_identified_with_144': False}, indent=2))


if __name__ == '__main__':
    main()
