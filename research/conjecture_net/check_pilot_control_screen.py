"""Exact conditional Lie-control screen; never authorize the added actuators."""
import hashlib
from fractions import Fraction
from itertools import combinations
import json
from pathlib import Path
from pilot_controls import (candidate_families, lie_closure, RealSpan, commutator,
                            is_skew_hermitian, fixes_uniform, exchange_matrix)
from pilot_observers import factor_generators
from check_pilot_capabilities import tensor, flatten
from check_structural_pilot_transport import identity, zeros, add, scale, mul, transpose
from check_programme_observers import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]
EXPECTED = {'native-local': 2, 'native-plus-exchange': 5, 'all-label-transpositions': 9,
            'native-plus-local-phase': 7, 'local-phase-plus-exchange': 16}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(contract['source_instance'] == 'native-bool-square-pilot', 'wrong control source')
    require({family['id'] for family in contract['families']} == set(EXPECTED), 'control family inventory changed')
    require(all(value is False for value in contract['boundary'].values()), 'control boundary promotion')
    require(contract['control_assumptions'] == [
        'Independent signed piecewise-constant coefficients for every listed Hamiltonian',
        'A common phase-framed representative before channel quotient',
        'Ideal finite-dimensional closed-system dynamics',
        'The common nonzero pi normalization; no physical energy/time units'] and contract['source_reviews'],
        'missing control/source premises')
    expected_hamiltonians = {
        'native-local': ['Q_L', 'Q_R'],
        'native-plus-exchange': ['Q_L', 'Q_R', 'Q_swap=(I-S)/2'],
        'all-label-transpositions': ['Q_ab=(I-P_ab)/2 for all six label transpositions'],
        'native-plus-local-phase': ['Q_L', 'Q_R', 'Q_ZL=(I-Z tensor I)/2', 'Q_ZR=(I-I tensor Z)/2'],
        'local-phase-plus-exchange': ['Q_L', 'Q_R', 'Q_ZL', 'Q_ZR', 'Q_swap']}
    require(all(family['hamiltonians'] == expected_hamiltonians[family['id']] for family in contract['families']),
            'control formula/implementation mismatch')
    require(all(family['extra_premises'] for family in contract['families'] if family['id'] != 'native-local'),
            'added controls lack explicit premises')


def audit():
    families = candidate_families()
    axes = factor_generators()
    i4, z4 = identity(4), zeros(4)
    pauli_sum = z4
    for axis in ('X', 'Y', 'Z'):
        pauli_sum = add(pauli_sum, tensor(axes[axis], axes[axis])[0])
    require(exchange_matrix() == scale(Fraction(1, 2), add(i4, pauli_sum)),
            'exchange/Pauli identity failed')
    reports = {}
    for name, hs in families.items():
        for h in hs:
            require(transpose(h) == h and mul(h, h) == h, 'candidate not a Hermitian projector generator')
        basis, rounds = lie_closure(hs)
        require(len(basis) == EXPECTED[name] and all(is_skew_hermitian(matrix) for matrix in basis), 'Lie dimension/type changed')
        span = RealSpan()
        for matrix in basis:
            require(span.add(flatten(matrix[0]) + flatten(matrix[1])), 'dependent final Lie basis')
        closure_pairs = 0
        for a, b in combinations(basis, 2):
            bracket = commutator(a, b)
            require(not span.add(flatten(bracket[0]) + flatten(bracket[1])), 'final Lie span not bracket closed')
            closure_pairs += 1
        uniform = all(fixes_uniform(matrix) for matrix in basis)
        require(uniform == (name in ('native-local', 'native-plus-exchange', 'all-label-transpositions')),
                'uniform-vector invariant changed')
        phase_span = RealSpan()
        for matrix in basis:
            phase_span.add(flatten(matrix[0]) + flatten(matrix[1]))
        has_global_phase = not phase_span.add(flatten(z4) + flatten(i4))
        reports[name] = {'declared_generator_count': len(hs), 'real_lie_dimension': len(basis),
                         'closure_rounds': rounds, 'final_bracket_pairs_checked': closure_pairs,
                         'fixes_uniform_vector': uniform, 'contains_global_phase_generator': has_global_phase,
                         'full_u4_algebra': len(basis) == 16,
                         'physical_actuator_authorization': False}
    return {'families': reports,
            'permutation_projector_upper_bound': 9,
            'uniform_invariant_argument': 'All canonical involutive-permutation Q=(I-P)/2 kill w; linear combinations/brackets still kill w, restricting action to u(3).',
            'successful_conditional_family': 'local-phase-plus-exchange',
            'scope': 'Finite continuously adjustable phase-framed controls under declared extra premises; no physical source selection or arbitrary discrete-gate controllability claim.'}


def main():
    contract_path = HOME / 'contracts/pilot-control-screen.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    previous = validate_previous(json.loads((HOME / 'contracts/programme-hierarchy.v9.json').read_text()),
                                 json.loads((HOME / 'results/pilot-observer-extension-audit.json').read_text()))
    controls = audit()
    paths = [contract_path, HOME / 'pilot_controls.py', Path(__file__), HOME / 'PILOT-CONTROL-SCREEN.md',
             HOME / 'results/pilot-observer-extension-audit.json'] + [ROOT / path for path in contract['source_reviews']]
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    result = {'schema': 'marici.conjecture-net.pilot-control-screen-result.v1', 'status': 'pass',
              'validation_only': True, 'outcome': None, 'root_outcome': None,
              'source_sha256': pins, 'previous_observer_validation': previous, 'controls': controls,
              'added_controls_physically_authorized': False, 'added_controls_derived_from_native_flips': False,
              'phase_framing_physically_supplied': False, 'new_kernel_control_theorem': False,
              'programme_outcomes_promoted': False}
    destination = HOME / 'results/pilot-control-screen.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'conditional_lie_dimensions': EXPECTED,
                      'added_controls_physically_authorized': False}, indent=2))


if __name__ == '__main__':
    main()
