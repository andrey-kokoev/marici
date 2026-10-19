"""Exact fixed-mode/one-direction trial on the retained shared-edge photon seed.
Read-only with respect to other owners: native replay runs in a temporary tree.
Scalars are a+b*j with j^2=-3; no physical helicity or mass is inferred.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from tempfile import TemporaryDirectory
import json
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
SEED = ROOT / 'research/strominger/results/photon_shared_edge_seed.json'
OUT = ROOT / 'research/voevodsky/results/photon-one-direction-trial-v1.json'
Z = (F(0), F(0))
ONE = (F(1), F(0))
J = (F(0), F(1))
OMEGA = (F(-1, 2), F(1, 2))


def add(a, b):
    return a[0] + b[0], a[1] + b[1]


def scale(s, a):
    return s * a[0], s * a[1]


def mul(a, b):
    return a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0]


def conj(a):
    return a[0], -a[1]


def inverse(a):
    return scale(1 / (a[0] ** 2 + 3 * a[1] ** 2), conj(a))


def total(values):
    result = Z
    for value in values:
        result = add(result, value)
    return result


def eye(n):
    return tuple(tuple(ONE if i == k else Z for k in range(n)) for i in range(n))


def mm(a, b):
    return tuple(tuple(total(mul(x, y) for x, y in zip(row, col)) for col in zip(*b)) for row in a)


def ma(a, b):
    return tuple(tuple(add(x, y) for x, y in zip(row, other)) for row, other in zip(a, b))


def ms(s, a):
    return tuple(tuple(mul(s, x) for x in row) for row in a)


def act(a, v):
    return tuple(total(mul(x, y) for x, y in zip(row, v)) for row in a)


def vs(s, v):
    return tuple(mul(s, x) for x in v)


def va(a, b):
    return tuple(add(x, y) for x, y in zip(a, b))


def gram(v):
    # The source's averaged logical metric diag(3,1), not counting norm.
    return add(scale(3, mul(conj(v[0]), v[0])), mul(conj(v[1]), v[1]))


def phase(t, negative=False):
    result = ((1 - 3 * t * t) / (1 + 3 * t * t), 2 * t / (1 + 3 * t * t))
    return scale(-1 if negative else 1, result)


def rank(a):
    a = [list(map(F, row)) for row in a]
    r = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        divisor = a[r][col]
        a[r] = [x / divisor for x in a[r]]
        for i in range(len(a)):
            if i != r:
                factor = a[i][col]
                a[i] = [x - factor * y for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def main():
    source = json.loads(SEED.read_text(encoding='utf-8'))
    assert source['status'] == 'passed' and all(source['checks'].values())
    pins = dict(source['source_hashes'])
    assert all(digest(ROOT / file) == expected for file, expected in pins.items())
    pins[SEED.relative_to(ROOT).as_posix()] = digest(SEED)
    pins[Path(__file__).relative_to(ROOT).as_posix()] = digest(Path(__file__))
    # Copy the native producer and all its declared dependencies. It computes
    # only in this isolated tree, including its own fixed result path.
    producer = 'research/strominger/checkers/check_photon_shared_edge_seed.py'
    with TemporaryDirectory(prefix='photon-one-direction-') as directory:
        isolated = Path(directory)
        for file in source['source_hashes']:
            target = isolated / file
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((ROOT / file).read_bytes())
        (isolated / 'research/strominger/results').mkdir(parents=True, exist_ok=True)
        run = subprocess.run([sys.executable, str(isolated / producer)], cwd=isolated,
                             capture_output=True, text=True, timeout=90)
        assert run.returncode == 0, run.stderr
        replay = json.loads((isolated / SEED.relative_to(ROOT)).read_text(encoding='utf-8'))
        assert replay == source

    arrows = source['arrows']
    K = tuple(tuple((F(a[1] == b[0]), F(0)) for a in arrows) for b in arrows)
    assert K == tuple(tuple((F(x), F(0)) for x in row) for row in source['continuation']['matrix'])
    plus, minus = tuple(tuple((F(c['real']), F(c['imaginary_sqrt3_coefficient'])) for c in source['modes'][key]['coefficients']) for key in ('plus', 'minus'))
    assert minus == tuple(conj(x) for x in plus)
    assert act(K, plus) == vs(OMEGA, plus)
    assert act(K, minus) == vs(conj(OMEGA), minus)
    assert mul(mul(OMEGA, OMEGA), OMEGA) == ONE

    # Recover the actual full-registry spectral projector as a polynomial in K.
    # Verify idempotence, rank-one factorization, and both commuting actions.
    # The other nonzero eigenvalues solve x^2-x-1=0, not x=2,-1.
    # Keep that real quadratic intact rather than introducing sqrt(5).
    real_factor = ma(ma(mm(K, K), ms((F(-1), F(0)), K)), ms((F(-1), F(0)), eye(6)))
    other_factor = ma(K, ms(scale(-1, conj(OMEGA)), eye(6)))
    at_omega = add(add(mul(OMEGA, OMEGA), scale(-1, OMEGA)), scale(-1, ONE))
    denominator = mul(mul(OMEGA, at_omega), add(OMEGA, scale(-1, conj(OMEGA))))
    project = ms(inverse(denominator), mm(mm(K, real_factor), other_factor))
    decoder = (project[0],)  # plus has AB coefficient one
    encoder = tuple((x,) for x in plus)
    assert mm(decoder, encoder) == eye(1)
    assert mm(encoder, decoder) == project and mm(project, project) == project
    assert mm(K, project) == mm(project, K) == ms(OMEGA, project)
    assert act(project, plus) == plus and act(project, minus) == (Z,) * 6

    # Logical coordinates (a,b) in v=a*u+b*w, where plus=u+j*w.
    B = tuple(((x[0], F(0)), (x[1], F(0))) for x in plus)
    D = tuple(tuple((F((i == 0) if row == 0 else (2 * (i == 2) - (i == 0))), F(0)) for i in range(6)) for row in range(2))
    assert mm(D, B) == eye(2)
    T = mm(D, mm(K, B))
    assert mm(K, B) == mm(B, T)
    expected_T = (((F(-1, 2), F(0)), (F(1, 2), F(0))), ((F(-3, 2), F(0)), (F(-1, 2), F(0))))
    assert T == expected_T
    G = (((F(3), F(0)), Z), (Z, ONE))
    adjT = tuple(tuple(conj(T[k][i]) for k in range(2)) for i in range(2))
    assert mm(adjT, mm(G, T)) == G
    assert all(gram(act(T, v)) == gram(v) for v in ((ONE, J), (ONE, scale(-1, J)), (ONE, ONE)))

    samples = []
    for t in (F(-2), F(-1), F(-1, 3), F(0), F(1, 3), F(1, 2), F(1), F(2)):
        p = phase(t)
        assert mul(conj(p), p) == ONE
        raw = vs(p, plus)
        assert act(decoder, raw) == (p,)
        assert act(K, raw) == vs(mul(OMEGA, p), plus)
        assert act(mm(K, mm(K, K)), raw) == raw
        ingress = ms(p, encoder)
        egress = ms(conj(p), decoder)
        assert mm(egress, ingress) == eye(1)
        assert mm(ingress, egress) == project
        assert mm(mm(ingress, egress), mm(ingress, egress)) == project
        assert gram(act(D, raw)) == (F(6), F(0))
        if t:
            assert phase(-1 / (3 * t), True) == p
        real_state = tuple((x[0], F(0)) for x in raw)
        real_coordinates = ((p[0], F(0)), (-3 * p[1], F(0)))
        assert act(B, real_coordinates) == real_state
        assert gram(real_coordinates) == (F(3), F(0))
        assert act(D, act(K, real_state)) == act(T, real_coordinates)
        samples.append({'chart_parameter': t, 'phase': p, 'fixed_plus_mode': raw,
                        'real_plane_coordinates': real_coordinates})
    assert phase(F(1)) == OMEGA and phase(F(0), True) == scale(-1, ONE)
    # Conic normalization identity for all t: (1-3t^2)^2+3(2t)^2=(1+3t^2)^2.
    assert [a + b for a, b in zip([1, -6, 9], [0, 12, 0])] == [1, 6, 9]
    fixed_tangent = vs(scale(2, J), plus)
    assert fixed_tangent != (Z,) * 6

    shared = [i for i, arrow in enumerate(arrows) if set(arrow) == {'A', 'B'}]
    assert len(shared) == 2
    restrict = lambda v: tuple(v[i] for i in shared)
    assert restrict(plus) == restrict(minus) and plus != minus
    assert restrict(act(K, plus)) != restrict(act(K, minus))
    real_a = tuple((x[0], F(0)) for x in vs(phase(F(1, 3)), plus))
    real_b = tuple((x[0], F(0)) for x in vs(phase(F(-1, 3)), plus))
    assert gram(act(D, real_a)) == gram(act(D, real_b)) == (F(3), F(0))
    assert restrict(real_a) == restrict(real_b)
    assert restrict(act(K, real_a)) != restrict(act(K, real_b))

    # Full complexified two-mode carrier: three independent normalized tangents.
    qplus, qminus = (ONE, J), (ONE, scale(-1, J))
    tangent_columns = [tuple(c for x in v for c in x) for v in
                       (vs(scale(2, J), qplus), vs((F(2), F(0)), qminus), vs(scale(2, J), qminus))]
    assert rank(list(zip(*tangent_columns))) == 3
    for t in (F(-1), F(0), F(1, 3), F(1)):
        c = (1 - t * t) / (1 + t * t)
        s = 2 * t / (1 + t * t)
        curves = (vs(phase(t), qplus), va(vs((c, F(0)), qplus), vs((s, F(0)), qminus)),
                  va(vs((phase(t)[0], F(0)), qplus), vs((F(0), phase(t)[1]), qminus)))
        assert all(gram(v) == (F(6), F(0)) for v in curves)
    # The source explicitly warns that counting norm is not its invariant metric.
    superposition = va(plus, minus)
    counting_norm = lambda v: total(mul(conj(x), x) for x in v)
    assert counting_norm(superposition) == (F(18), F(0))
    assert counting_norm(act(K, superposition)) == (F(12), F(0))
    assert all(digest(ROOT / file) == expected for file, expected in pins.items())

    checks = {
        'source_receipt_passed_and_all_declared_pins_fresh': True,
        'isolated_native_replay_reproduces_complete_retained_receipt': True,
        'continuation_reconstructed_from_actual_six_arrow_registry': True,
        'actual_conjugate_modes_have_native_period_three': True,
        'plus_mode_spectral_projector_recovered_on_full_six_slot_registry': True,
        'fixed_mode_encoder_decoder_and_fourfold_identities_hold': True,
        'fixed_mode_unit_phase_conic_has_one_nonzero_real_tangent': True,
        'two_phase_charts_retain_the_missing_antipode_and_overlap': True,
        'all_sample_phase_states_preserve_native_continuation_and_recovery': True,
        'native_step_is_the_actual_chart_endpoint_t_one': True,
        'actual_real_plane_decoder_recovers_both_coordinates': True,
        'averaged_source_metric_is_preserved_by_real_plane_transport': True,
        'normalized_real_plane_is_a_one_direction_conjugate_locked_family': True,
        'shared_edge_erasure_merges_modes_with_distinct_next_edge_outputs': True,
        'shared_edge_erasure_also_fails_on_normalized_real_plane': True,
        'full_complexified_normalized_mode_pair_has_three_independent_real_tangents': True,
        'counting_norm_hostile_reproduces_source_eighteen_to_twelve': True,
        'all_bound_source_inputs_unchanged': True,
    }
    report = {
        'schema': 'marici.photon-one-direction-trial.v1',
        'verification_passed': all(checks.values()), 'checks': checks,
        'native_replay_check_count': len(source['checks']),
        'source_boundary': 'Existing shared-edge two-face seed and declared cyclic modes. No physical photon identification, helicity, masslessness or metric derivation inferred.',
        'interpretation_of_n': 'Local smooth real configuration directions within an explicitly selected retained interface, not number of endpoints, raw slots or simplices.',
        'fixed_mode': {'candidate': '[marked cyclic mode; one phase direction]', 'complex_dimension': 1,
                       'fixed_metric_norm_squared': 6, 'normalized_real_dimension': 1,
                       'phase_chart': 'lambda(t)=(1-3t^2+2t*j)/(1+3t^2), j^2=-3; opposite chart -lambda(t), overlap t -> -1/(3t).',
                       'native_phase_subgroup': ['1', 'omega', 'conjugate(omega)'],
                       'scope': 'The native step preserves the selected spectral line. Continuous phase preparation/transports are supplied beyond the finite C3 steps; plus/minus are cyclic labels, not seed-derived physical helicities.'},
        'real_plane': {'candidate': 'Re(lambda g_plus), with squared norm 3 in the source averaged metric',
                       'normalized_real_dimension': 1, 'constraint': 'Conjugate modal coefficients are tied; they are not independent polarization amplitudes.'},
        'full_mode_pair': {'complex_dimension': 2, 'normalized_real_dimension': 3,
                           'tangent_columns_in_real_logical_coordinates': tangent_columns,
                           'boundary': 'Allowing independent complex coefficients restores three normalized real directions. One selected line is not a presentation of this full family.'},
        'edge_hostile': {'shared_occurrence_indices': shared,
                         'mode_edge_inputs': restrict(plus), 'plus_next_edge': restrict(act(K, plus)), 'minus_next_edge': restrict(act(K, minus)),
                         'real_plane_edge_inputs': restrict(real_a), 'real_plane_next_a': restrict(act(K, real_a)), 'real_plane_next_b': restrict(act(K, real_b)),
                         'conclusion': 'No deterministic shared-edge-only continuation reproduces both examples. The retained supporting complex must not be discarded.'},
        'encoder': plus, 'decoder': decoder[0], 'spectral_projector': project,
        'samples': samples,
        'simplex_boundary': 'A local interval from g_plus to omega*g_plus may be drawn as a 1-simplex. Three native steps give a cyclic return. The entire retained two-triangle disk or phase circle is not a single interval; an edge alone is not the full packet certificate.',
        'comparison_boundary': 'A fixed normalized electron mode also has a one-phase family, but the electron full native binary tetrahedral action does not preserve a logical line. Compare required operation sets, not just differently restricted state families.',
        'candidate_accounting': {'n': 1, 'dependency_sectors': 1, 'three_products': [1, 1, 1], 'sum': 3,
                                 'boundary': 'Not native arrow cost, photon energy or mass. Positive candidate score does not establish or refute physical masslessness.'},
        'verification_level': 'Exact finite-source replay, full-input linear identities, rational conic identity and declared normalized curve samples. Not proof-assistant formalization or universal one-direction photon theorem.',
        'source_sha256': pins,
    }
    OUT.write_text(json.dumps(serial(report), indent=2) + '\n', encoding='utf-8')
    print(json.dumps({'verification_passed': report['verification_passed'], 'checks': checks,
                      'receipt': str(OUT.relative_to(ROOT))}, indent=2))


if __name__ == '__main__':
    main()
