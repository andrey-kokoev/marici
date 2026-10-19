"""Live-pinned exact exchange bridge audit; no native preparation/control admission."""
from fractions import Fraction as F
from itertools import combinations
import hashlib
import json
from pathlib import Path
from exchange_source_bridge import (ROOT, SOURCE, BINDING, source_model, identity, zeros, decode,
    add, scale, transpose, mul, block_diagonal, invert, ldl, spectral, complex_mul, adjoint,
    realification, word_matrix, execute, validate_word, ExecutionLedger)
from check_pilot_capabilities import rank
from check_programme_controls import validate as validate_previous

HOME = Path(__file__).resolve().parent


def require(condition, message):
    if not condition:
        raise ValueError(message)


def live_source_pins():
    queue = [SOURCE, BINDING, 'research/nima/results/exchange-contact-gate-comparison.json']
    pins = {}
    while queue:
        relative = queue.pop()
        if relative in pins:
            continue
        path = (ROOT / relative).resolve()
        require(path.is_relative_to(ROOT), 'source path escapes repository')
        pins[relative] = hashlib.sha256(path.read_bytes()).hexdigest()
        if path.suffix != '.json':
            continue
        document = json.loads(path.read_text())
        for name, expected in document.get('input_sha256', {}).items():
            name = name.replace(chr(92), '/')
            if name.startswith('research/'):
                dependency = ROOT / name
            else:
                owner = path.parent.parent
                candidates = [owner / 'checkers' / name, owner / 'results' / name]
                present = [candidate for candidate in candidates if candidate.is_file()]
                require(len(present) == 1, 'missing/ambiguous source dependency: ' + name)
                dependency = present[0]
            dependency = dependency.resolve()
            require(dependency.is_relative_to(ROOT) and not Path(name).is_absolute(), 'dependency escapes repository')
            require(hashlib.sha256(dependency.read_bytes()).hexdigest() == expected, 'stale exchange dependency: ' + name)
            queue.append(dependency.relative_to(ROOT).as_posix())
    for relative in ('research/nima/checkers/check_seed_typed_execution.py',
                     'research/nima/checkers/check_natural_tower_return.py'):
        pins[relative] = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
    return pins


def validate_contract(contract):
    require(contract['source'] == SOURCE and contract['source_binding'] == BINDING, 'wrong exchange source')
    require(all(value is False for value in contract['boundary'].values()), 'exchange bridge boundary promotion')
    require(contract['target']['carrier'] == 'C16 anchor direct_sum C6 mismatch with the transported positive source metric',
            'faithful source domain compressed')
    require(contract['typed_path_policy']['global_switching'] ==
            'Free simultaneous or arbitrary switching among all six Hamiltonians is not inferred from their existence as typed port maps.',
            'typed port controls silently unlocked')


def audit():
    model = source_model()
    e, d, g = model['encoder'], model['decoder'], model['mismatch_metric']
    require(mul(e, d) == mul(d, e) == identity(22), 'source decomposition not invertible')
    lower, pivots = ldl(g)
    diag = zeros(6)
    for i, value in enumerate(pivots):
        diag[i][i] = value
    require(mul(mul(lower, diag), transpose(lower)) == g, 'metric positivity certificate failed')
    ldl(model['raw_metric'])
    transported_metric = mul(mul(transpose(d), model['raw_metric']), d)
    require([row[16:] for row in transported_metric[16:]] == g and
            all(transported_metric[i][j] == transported_metric[j][i] == 0 for i in range(16) for j in range(16, 22)),
            'anchor/mismatch metric splitting failed')
    g_inverse = invert(g)
    poisson = realification((zeros(6), scale(-1, g_inverse)))
    omega = realification((zeros(6), g))
    require(mul(poisson, omega) == identity(12), 'metric symplectic/Poisson convention mismatch')
    phase_controls = ((F(1), F(0)), (F(-1), F(0)), (F(0), F(-1)), (F(3, 5), F(4, 5)))
    for label, t in model['reduced'].items():
        raw = model['raw'][label]
        require(mul(t, t) == identity(6) and mul(raw, raw) == identity(22), 'source port not an involution')
        require(mul(mul(transpose(t), g), t) == g, 'source mismatch metric not preserved')
        require(mul(mul(transpose(raw), model['raw_metric']), raw) == model['raw_metric'], 'raw source budget changed')
        require(mul(mul(e, raw), d) == block_diagonal(identity(16), t), 'full source operation square failed')
        q = scale(F(1, 2), add(identity(6), scale(-1, t)))
        require(mul(q, q) == q and mul(transpose(q), g) == mul(g, q), 'metric projector law failed')
        gq = mul(g, q)
        field = realification((zeros(6), scale(-1, q)))
        require(mul(poisson, block_diagonal(gq, gq)) == field, 'weighted Hamiltonian realification failed')
        require(add(mul(transpose(field), omega), mul(omega, field)) == zeros(12), 'weighted symplectic law failed')
        for zr, zi in phase_controls:
            u = spectral(t, zr, zi)
            require(complex_mul(adjoint(u), complex_mul((g, zeros(6)), u)) == (g, zeros(6)), 'metric-unitary phase control failed')
        require(spectral(t, F(1), F(0)) == (identity(6), zeros(6)) and
                spectral(t, F(-1), F(0)) == (t, zeros(6)), 'spectral endpoint binding failed')
        half = spectral(t, F(0), F(-1))
        require(complex_mul(half, half) == (t, zeros(6)), 'spectral composition control failed')
    commutators = [add(mul(a, b), scale(-1, mul(b, a))) for a, b in combinations(model['reduced'].values(), 2)]
    columns = [sum((matrix[row] for matrix in commutators), []) for row in range(6)]
    require(rank(columns) == 6, 'active noncommuting mismatch response erased')
    source_collision = model['source_receipt']['collision']
    first, second = tuple(source_collision['first_word']), tuple(source_collision['second_word'])
    require(validate_word(first, model['ports']) == validate_word(second, model['ports']) == ('A', 'A'), 'source collision endpoints changed')
    full_first = word_matrix(first, model['raw'], model['ports'])
    full_second = word_matrix(second, model['raw'], model['ports'])
    residual = add(full_second, scale(-1, full_first))
    require(rank(residual) == source_collision['exchange_residual_rank'] == 2, 'source collision response changed')
    anchor = e[:16]
    require(mul(anchor, residual) == zeros(16, 22), 'source anchor response changed')
    reduced_first = word_matrix(first, model['reduced'], model['ports'])
    reduced_second = word_matrix(second, model['reduced'], model['ports'])
    require(mul(mul(e, full_first), d) == block_diagonal(identity(16), reduced_first) and
            mul(mul(e, full_second), d) == block_diagonal(identity(16), reduced_second), 'whole-word transport failed')
    preparation = [F(0)] * 22
    preparation[16 + model['labels'].index('AB')] = F(1)
    ledger = ExecutionLedger()
    output1, history1 = ledger.execute(first, preparation, model['raw'], model['ports'], 'first', 'A')
    output2, history2 = ledger.execute(second, preparation, model['raw'], model['ports'], 'second', 'A')
    require(output1 != output2 and len(history1) == 6 and len(history2) == 12, 'retained collision witness lost')
    replay, replay_history = ledger.execute(first, preparation, model['raw'], model['ports'], 'replay', 'A')
    require(replay == output1 and replay_history != history1, 'execution identity collapsed')
    for output, history in ((output1, history1), (output2, history2)):
        restored = [[value] for value in output]
        for record in reversed(history):
            restored = mul(model['raw'][record['port']], restored)
            require(tuple(row[0] for row in restored) == record['before'], 'inverse occurrence reconstruction failed')
        require(tuple(row[0] for row in restored) == tuple(preparation), 'whole source reconstruction failed')
    return {'raw_source_dimension': 22, 'anchor_dimension': 16, 'mismatch_dimension': 6,
            'source_ports': list(model['labels']), 'metric_ldl_positive_pivots': [str(value) for value in pivots],
            'metric_unitary_port_count': 6, 'finite_phase_controls_per_port': 4,
            'weighted_hamiltonian_realification_count': 6, 'mismatch_commutator_image_rank': 6,
            'retained_collision_residual_rank': 2, 'retained_collision_word_lengths': [6, 12],
            'same_source_geometric_quotient_collision': 'Imported historical source fact; this audit recomputes typed endpoints and full numerical collision, not the historical geometric/spin producer.',
            'continuous_spectral_verification': 'Exact projector/metric identities plus written all-time exponential argument, not sampling or a new completion kernel theorem',
            'free_switching_of_all_ports_supplied': False, 'physical_preparation_derived': False}


def main():
    contract_path = HOME / 'contracts/exchange-source-bridge.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    pins = live_source_pins()
    previous = validate_previous(json.loads((HOME / 'contracts/programme-hierarchy.v10.json').read_text()),
                                 json.loads((HOME / 'results/pilot-control-screen.json').read_text()))
    controls = audit()
    for path in (contract_path, HOME / 'exchange_source_bridge.py', Path(__file__), HOME / 'EXCHANGE-SOURCE-BRIDGE.md'):
        pins[path.relative_to(ROOT).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    require(all(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == value for path, value in pins.items()), 'sources changed during bridge audit')
    result = {'schema': 'marici.conjecture-net.exchange-source-bridge-audit.v1', 'status': 'pass',
              'validation_only': True, 'outcome': None, 'root_outcome': None,
              'source_sha256': pins, 'controls': controls, 'previous_control_validation': previous,
              'new_kernel_spectral_bridge_proved': False, 'physical_source_instrument_bridge_proved': False,
              'freely_switchable_six_port_controls_authorized': False,
              'same_physical_witness_as_bool_source_proved': False, 'programme_outcomes_promoted': False}
    destination = HOME / 'results/exchange-source-bridge-audit.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'faithful_source_dimension': 22, 'active_metric_unitary_dimension': 6,
                      'source_ports': 6, 'physical_source_control_bridge': False}, indent=2))


if __name__ == '__main__':
    main()
