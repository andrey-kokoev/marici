"""Bounded n=1/n=2 packet trial against the retained electron spinor.
Reads the existing fixture and replays its producer in isolation; no shared
producer outputs are overwritten.
Configuration dimension is tested as local smooth real state dimension.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from itertools import product
from contextlib import redirect_stdout
from tempfile import TemporaryDirectory
from io import StringIO
import json
import sys

import check_electron_tetrahedral_spinor as native
from check_electron_tetrahedral_spinor import D, adj, act, ident, sm
from check_electron_charge_spin_frontier import ga, gs, gm, gc, gt, gmm, spin, G0, G1, GI
from check_electron_pairing_coupling import pair, rank, gdiv

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT / 'research/voevodsky'
STORE = BASE / 'results/electron_tetrahedral_spinor_store.json'
RECEIPT = BASE / 'results/electron_tetrahedral_spinor.json'
PRIOR = BASE / 'results/electron_charge_spin_frontier.json'
OUT = BASE / 'results/electron-configuration-dimension-trial-v1.json'


def digest(path):
    return sha256(path.read_bytes()).hexdigest()


def decode(z):
    return tuple(D(F(a), F(b)) for a, b in z)


def density(z):
    return tuple(tuple(gm(x, gc(y)) for y in z) for x in z)


def norm(z):
    return gt(gm(gc(x), x) for x in z)[0]


def bloch(z):
    p = density(z)
    return 2 * p[0][1][0], -2 * p[0][1][1], p[0][0][0] - p[1][1][0]


def chart_density(w, north=True):
    absolute2 = gm(w, gc(w))[0]
    rows = ((G1, gc(w)), (w, (absolute2, F(0)))) if north else (((absolute2, F(0)), w), (gc(w), G1))
    return sm(1 / (1 + absolute2), rows)


@dataclass(frozen=True)
class Jet:
    """Exact value and first derivative, only for the local coordinate test."""
    value: F
    derivative: F = F(0)

    def __add__(self, other):
        q = jet(other)
        return Jet(self.value + q.value, self.derivative + q.derivative)
    __radd__ = __add__

    def __neg__(self):
        return Jet(-self.value, -self.derivative)

    def __sub__(self, other):
        return self + -jet(other)

    def __rsub__(self, other):
        return jet(other) + -self

    def __mul__(self, other):
        q = jet(other)
        return Jet(self.value * q.value, self.derivative * q.value + self.value * q.derivative)
    __rmul__ = __mul__

    def __truediv__(self, other):
        q = jet(other)
        return Jet(self.value / q.value, (self.derivative * q.value - self.value * q.derivative) / (q.value * q.value))

    def __rtruediv__(self, other):
        return jet(other) / self


def jet(x):
    return x if isinstance(x, Jet) else Jet(F(x))


def circle(t):
    return (1 - t * t) / (1 + t * t), 2 * t / (1 + t * t)


def families(t):
    c, s = circle(t)
    return (((c, s), G0), ((c, F(0)), (s, F(0))), ((c, F(0)), (F(0), s)))


def real_rank(rows):
    return rank([[(F(x), F(0)) for x in row] for row in rows])


def serial(value):
    if isinstance(value, D):
        return {'rational': str(value.a), 'sqrt3': str(value.b)}
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    # All imported Python modules in the owner checker directory, plus actual inputs.
    inputs = {STORE, RECEIPT, PRIOR, Path(__file__).resolve()}
    for module in tuple(sys.modules.values()):
        file = getattr(module, '__file__', None)
        if file:
            path = Path(file).resolve()
            if path.suffix == '.py' and path.parent == Path(__file__).resolve().parent:
                inputs.add(path)
    before = {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(inputs)}
    source = json.loads(RECEIPT.read_text(encoding='utf-8'))
    store = json.loads(STORE.read_text(encoding='utf-8'))
    assert source['verification_passed']
    prior_pin_matches = source['checker_sha256'] == digest(BASE / 'checkers/check_electron_tetrahedral_spinor.py')
    assert source['source_sha256'] == digest(PRIOR)
    # The historical producer pin may predate documentation edits. Recompute
    # its actual fixture with the current code, without changing shared outputs.
    with TemporaryDirectory(prefix='electron-dimension-trial-') as directory:
        isolated = Path(directory)
        (isolated / 'results').mkdir()
        (isolated / 'results/electron_charge_spin_frontier.json').write_bytes(PRIOR.read_bytes())
        original_base = native.BASE
        try:
            native.BASE = isolated
            with redirect_stdout(StringIO()):
                native.main()
        finally:
            native.BASE = original_base
        replay = json.loads((isolated / 'results/electron_tetrahedral_spinor.json').read_text(encoding='utf-8'))
        replay_store = json.loads((isolated / 'results/electron_tetrahedral_spinor_store.json').read_text(encoding='utf-8'))
        assert replay['verification_passed'] and all(replay['checks'].values())
        assert replay_store == store
        assert replay['checker_sha256'] == digest(BASE / 'checkers/check_electron_tetrahedral_spinor.py')
    projectors = tuple(tuple(tuple(decode(z) for z in row) for row in p) for p in store['face_projectors'])
    I = ident(2)
    assert len(projectors) == 4
    assert tuple(tuple(gt(p[i][j] for p in projectors) for j in range(2)) for i in range(2)) == sm(2, I)
    assert all(gmm(p, p) == p and adj(p) == p for p in projectors)
    roundtrip = sm(F(1, 2), tuple(tuple(gt(gmm(p, p)[i][j] for p in projectors) for j in range(2)) for i in range(2)))
    assert roundtrip == I

    matrices = {stage: [[G0 for _ in range(8)] for _ in range(8)] for stage in ('L', 'G', 'N')}
    seen = set()
    for arrow in store['arrows']:
        key = arrow['stage'], arrow['target'], arrow['source']
        assert key not in seen
        seen.add(key)
        matrices[key[0]][key[1]][key[2]] = decode(arrow['weight'])
    matrices = {s: tuple(map(tuple, m)) for s, m in matrices.items()}
    expected = tuple(tuple(gs(F(1, 2), gmm(projectors[i // 2], projectors[j // 2])[i % 2][j % 2]) for j in range(8)) for i in range(8))
    assert matrices['N'] == matrices['G'] == expected
    assert gmm(matrices['N'], matrices['N']) == matrices['N']
    assert gmm(matrices['N'], gmm(matrices['G'], matrices['L'])) == matrices['N']
    assert len(seen) == 144

    # K=sqrt(2)J stores unscaled face blocks in the existing exact coefficient field.
    # The decoder is K*/2, so its composed projector is exactly the stored N.
    def encode(z):
        return tuple(x for p in projectors for x in act(p, z))

    def recover(raw):
        return tuple(gs(F(1, 2), gt(act(projectors[j], raw[2 * j:2 * j + 2])[i] for j in range(4))) for i in range(2))

    samples = ((G1, G0), (G0, G1), ((F(3, 5), F(0)), (F(4, 5), F(0))),
               ((F(3, 5), F(0)), (F(0), F(4, 5))), ((F(6, 7), F(0)), (F(3, 7), F(2, 7))))
    chart_uses = [0, 0]
    for z in samples:
        assert norm(z) == 1 and recover(encode(z)) == z
        p = density(z)
        assert gmm(p, p) == p
        r = bloch(z)
        assert sum(x * x for x in r) == 1
        if z[0] != G0:
            w = gdiv(z[1], z[0]); assert chart_density(w) == p; chart_uses[0] += 1
        if z[1] != G0:
            v = gdiv(z[0], z[1]); assert chart_density(v, False) == p; chart_uses[1] += 1
        if z[0] != G0 and z[1] != G0:
            assert gm(w, v) == G1  # explicit overlap relation, no single global chart
        for phase in (G1, GI, gs(-1, G1), gs(-1, GI)):
            changed = tuple(gm(phase, x) for x in z)
            assert density(changed) == p
            assert encode(changed) == tuple(gm(phase, x) for x in encode(z))
            assert recover(encode(changed)) == changed

    quaternions = {tuple(F(s if k == j else 0) for k in range(4)) for j in range(4) for s in (-1, 1)}
    quaternions.update(tuple(F(s, 2) for s in signs) for signs in product((-1, 1), repeat=4))
    for q in quaternions:
        U = spin(q)
        assert gmm(adj(U), U) == I
        for p in projectors:
            image = gmm(gmm(U, p), adj(U))
            index = projectors.index(image)
            assert gmm(projectors[index], U) == gmm(U, p)
        for z in samples:
            transformed = act(U, z)
            assert density(transformed) == gmm(gmm(U, density(z)), adj(U))

    U = spin((F(0), F(1), F(0), F(0)))
    V = spin((F(0), F(0), F(1), F(0)))
    commutator = gmm(gmm(gmm(U, V), adj(U)), adj(V))
    assert commutator == sm(-1, I)
    e = (G0, G1); changed = act(commutator, e)
    assert changed == tuple(gs(-1, x) for x in e)
    assert density(changed) == density(e) and encode(changed) != encode(e)
    assert recover(encode(changed)) == changed
    assert pair((G1, G0), e) == G1
    assert pair((G1, G0), changed) == gs(-1, G1)

    # A chosen 1-real-parameter meridian is usable for a restricted operation family.
    # A retained binary tetrahedral action leaves that meridian.
    for t in (F(-2), F(-1), F(0), F(1, 2), F(1), F(2)):
        for z in families(t):
            assert norm(z) == 1
        meridian = families(t)[1]
        assert bloch(meridian)[1] == 0
        assert bloch(act(V, meridian))[1] == 0
    half_turn = spin((F(1, 2),) * 4)
    assert bloch(act(half_turn, (G1, G0)))[1] != 0

    # Exact first derivatives of three normalized rational curves through (1,0).
    tangent_columns, bloch_columns = [], []
    for curve in families(Jet(F(0), F(1))):
        normalization = jet(norm(curve))
        assert normalization.value == 1 and normalization.derivative == 0
        tangent_columns.append([jet(x).derivative for component in curve for x in component])
        bloch_columns.append([jet(x).derivative for x in bloch(curve)])
    tangent_rows = list(zip(*tangent_columns)); bloch_rows = list(zip(*bloch_columns))
    assert real_rank(tangent_rows) == 3 and real_rank(bloch_rows) == 2
    assert bloch_columns[0] == [0, 0, 0]
    assert all(bloch_columns[j] != [0, 0, 0] for j in (1, 2))

    initial = ((F(3, 5), F(0)), (F(0), F(4, 5)))
    current = initial
    display_steps = []
    for label, operation in (('U', U), ('V', V), ('U inverse', adj(U)), ('V inverse', adj(V))):
        current = act(operation, current)
        assert norm(current) == 1
        display_steps.append({'label': label, 'matrix': operation, 'spinor': current, 'bloch': bloch(current)})
    assert current == tuple(gs(-1, x) for x in initial)
    assert density(current) == density(initial)

    after = {p.relative_to(ROOT).as_posix(): digest(p) for p in sorted(inputs)}
    assert before == after
    checks = {
        'existing_prerequisite_pin_matches_actual_source': True,
        'current_native_producer_replayed_in_isolation_with_identical_store': True,
        'actual_face_projectors_form_the_existing_tight_frame': True,
        'actual_144_arrows_reconstruct_the_existing_return': True,
        'source_face_decoder_recovers_all_logical_inputs_by_matrix_identity': roundtrip == I,
        'all_sample_spinors_recover_through_the_source_face_blocks': True,
        'two_ray_charts_cover_samples_including_both_poles_with_overlap_wv_one': all(chart_uses),
        'all_24_retained_binary_rotations_descend_to_ray_transports': True,
        'retained_complex_phase_is_preserved_by_the_source_encoder': True,
        'actual_rotation_commutator_is_minus_identity': True,
        'phase_erasure_merges_distinct_retained_amplitudes_and_pairing_outputs': True,
        'one_parameter_meridian_works_for_a_restricted_family_but_not_all_source_rotations': True,
        'normalized_spinor_has_three_independent_local_real_tangents': real_rank(tangent_rows) == 3,
        'ray_readout_has_two_independent_local_tangents_and_erases_phase_tangent': real_rank(bloch_rows) == 2,
        'display_fixture_four_rotation_prefixes_bound_to_source': True,
        'all_source_inputs_unchanged': before == after,
    }
    report = {
        'schema': 'marici.electron-configuration-dimension-trial.v1',
        'verification_passed': all(checks.values()), 'checks': checks,
        'verification_level': 'Isolated current-producer replay, exact finite source reconstruction, rational chart identities on declared samples, all 24 binary rotations, and exact local derivative ranks; not proof-assistant formalization.',
        'native_replay': {'historical_checker_pin_matches_current': prior_pin_matches,
                          'isolated_replay_passed': replay['verification_passed'],
                          'isolated_replay_check_count': len(replay['checks']),
                          'current_store_equals_retained_store': replay_store == store,
                          'note': 'Historical receipt left unchanged; the trial uses a fresh isolated replay of the current producer.'},
        'interpretation_of_n': 'Number of independent smooth real configuration directions. Complex rank, embedding dimension, control-generator count and coherence-sector count remain distinct.',
        'source_carrier': {'logical_complex_dimension': 2, 'raw_complex_coordinates': 8, 'native_transfers': 144,
                           'scaled_storage': 'K=sqrt(2)J; decoder K*/2. This exact-field storage retains the same subspace and the same N, without rewriting the native fixture.'},
        'trial': {
            'n1': 'A restricted one-real-parameter orbit is viable. One local smooth real coordinate cannot faithfully cover the two-dimensional ray family. A one-complex-dimensional invariant carrier is separately obstructed by the central commutator.',
            'n2': 'Viable as the projective spin-state base, with two charts and actual unitary-induced transports. The phase-erased base alone fails the retained amplitude/phase-sensitive continuation interface.',
            'n2_with_retained_phase': 'Candidate base-plus-fiber packet: keep the phase/transport information in the retained label complex. This trial does not yet construct its 2-times-2 dependency sectors, two output capabilities, recoveries and higher coherence.',
            'full_normalized_spinor': 'Three independent local real directions: two change the ray and one changes phase. This dimension statement does not by itself determine the proposed packet arity.'},
        'hostile': {'route': 'U V U* V* = -I', 'same_ray': True, 'different_source_amplitudes': True,
                    'fixed_reference_pairing': ['+1', '-1'],
                    'scope': 'A phase-sensitive amplitude continuation with its reference retained; not a distinct isolated-state projector measurement.'},
        'display_fixture': {'initial_spinor': initial, 'initial_bloch': bloch(initial), 'steps': display_steps,
                            'application_order': 'Apply U, then V, then U inverse, then V inverse; the right-to-left composite V* U* V U is -I.',
                            'interpolation_boundary': 'Only these discrete source endpoints are certified here. Any browser interpolation between them is separately supplied illustrative data.'},
        'local_tangent_columns_real_spinor': tangent_columns,
        'local_tangent_columns_bloch_readout': bloch_columns,
        'candidate_accounting': {str(n): {'dependency_sectors': n * 2 ** (n - 1), 'directions': n,
            'three_products': [n ** 3 * 2 ** (n - 1), n ** 3 * 2 ** (2 * n - 2), n ** 4 * 2 ** (2 * n - 2)]}
            for n in (1, 2, 3)},
        'count_boundary': 'For n=2 the candidate sum is 112, whereas the native supplied spinor protocol has 144 transfers. These are different accounting interfaces; no electron mass or packet dimension is selected by matching counts.',
        'source_sha256': after,
        'scope': 'No native source files or receipts changed; no physical electron identification, mass, charge, statistics, or universal packet realization claimed.',
    }
    OUT.write_text(json.dumps(serial(report), indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verification_passed': report['verification_passed'], 'checks': checks, 'trial': report['trial'], 'receipt': str(OUT.relative_to(ROOT))}, indent=2))
    if not report['verification_passed']:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
