"""Audit a uniform enlarged mathematical probe family; no physical instrument claim."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from pilot_observers import factor_generators, product_probes
from pilot_carrier import Operation, native_permutation
from check_pilot_capabilities import tensor, rank, flatten, trace_pair, adjoint, audit as old_audit
from check_structural_pilot_transport import identity, zeros, add, scale, complex_mul
from check_programme_capabilities import validate as validate_previous

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(contract['source_instance'] == 'native-bool-square-pilot', 'wrong observer source')
    require(contract['branch'] == 'authorize-richer-observers', 'wrong synthesis branch')
    require(all(value is False for value in contract['boundary'].values()), 'observer boundary promotion')
    require(len(contract['ingredient_provenance']) == 6 and all(item['role'] and item['origin'] and item['boundary']
                for item in contract['ingredient_provenance']), 'missing probe provenance')


def audit():
    generators = factor_generators()
    probes = product_probes()
    i2, z2, i4, z4 = identity(2), zeros(2), identity(4), zeros(4)
    for axis in ('X', 'Y', 'Z'):
        m = generators[axis]
        require(adjoint(m) == m and complex_mul(m, m) == (i2, z2), 'generated axis is not a Hermitian involution')
    # Existing half-phase flow rotates the coordinate Z to -Y. X probes are
    # from the native involution, not obtainable by this Z-propagation alone.
    q = scale(F(1, 2), add(i2, scale(-1, generators['X'][0])))
    quarter = add(i2, scale(-1, q)), scale(-1, q)
    rotated_z = complex_mul(adjoint(quarter), complex_mul(generators['Z'], quarter))
    require(rotated_z == (scale(-1, generators['Y'][0]), scale(-1, generators['Y'][1])), 'quarter-phase/source-generator mismatch')
    labels = [a + b for a in generators for b in generators]
    basis = [tensor(generators[label[0]], generators[label[1]]) for label in labels]
    rows = []
    yz_rows = []
    for setting, effects in probes.items():
        total_real, total_imag = z4, z4
        for signs, effect in effects.items():
            require(adjoint(effect) == effect and complex_mul(effect, effect) == effect, 'effect not an orthogonal projector')
            require(trace_pair(effect, (i4, z4)) == 1, 'effect not rank one')
            total_real = add(total_real, effect[0])
            total_imag = add(total_imag, effect[1])
            row = [trace_pair(effect, p) / 4 for p in basis]
            rows.append(row)
            if all(axis in ('Y', 'Z') for axis in setting):
                yz_rows.append(row)
        require((total_real, total_imag) == (i4, z4), 'complete setting normalization failed')
    require(len(rows) == 36 and rank(rows) == 16, 'enlarged mathematical observation not complete')
    require(rank(yz_rows) == 9, 'old restricted family changed')
    gram = [[sum(row[a] * row[b] for row in rows) for b in range(16)] for a in range(16)]
    require(all(gram[a][b] == 0 for a in range(16) for b in range(16) if a != b), 'Pauli Gram not diagonal')
    diagonal = [gram[a][a] for a in range(16)]
    expected = [F(9, 4) if label == 'II' else F(3, 4) if 'I' in label else F(1, 4) for label in labels]
    require(diagonal == expected, 'finite tomography bound changed')
    # Diagonal Gram gives a uniform rational left inverse, tested on the
    # entire coordinate basis: d = G^-1 S^T records.
    for coordinate in range(16):
        records = [row[coordinate] for row in rows]
        reconstructed = [sum(row[a] * value for row, value in zip(rows, records)) / diagonal[a] for a in range(16)]
        require(reconstructed == [int(a == coordinate) for a in range(16)], 'reconstruction failed')
    xi = basis[labels.index('XI')]
    rho_plus = add(scale(F(1, 4), i4), scale(F(1, 8), xi[0])), z4
    rho_minus = add(scale(F(1, 4), i4), scale(F(-1, 8), xi[0])), z4
    plus_record = trace_pair(probes[('X', 'Z')][(1, 1)], rho_plus)
    minus_record = trace_pair(probes[('X', 'Z')][(1, 1)], rho_minus)
    require(plus_record == F(3, 8) and minus_record == F(1, 8), 'old hostile not separated')
    covariance_cells = 0
    for operation, factor in ((Operation.LEFT, 0), (Operation.RIGHT, 1)):
        matrix = [list(row) for row in native_permutation(operation)]
        u = matrix, z4
        for (a, b), effects in probes.items():
            axes = (a, b)
            for (s, t), effect in effects.items():
                signs = [s, t]
                if axes[factor] != 'X':
                    signs[factor] *= -1
                transformed = complex_mul(adjoint(u), complex_mul(effect, u))
                require(transformed == probes[(a, b)][tuple(signs)], 'Bool relabel covariance failed')
                covariance_cells += 1
    exchange = zeros(4)
    for j in range(4):
        exchange[2 * (j % 2) + j // 2][j] = F(1)
    u = exchange, z4
    for (a, b), effects in probes.items():
        for (s, t), effect in effects.items():
            require(complex_mul(adjoint(u), complex_mul(effect, u)) == probes[(b, a)][(t, s)], 'factor exchange covariance failed')
            covariance_cells += 1
    require(old_audit()['action']['continuous_control_lie_dimension'] == 2, 'observer extension altered dynamics')
    return {'settings': 9, 'complete_effects': 36, 'hermitian_observation_rank': 16,
            'trace_one_visible_tangent_dimension': 15, 'old_restricted_observer_rank': 9,
            'finite_pauli_coordinate_gram_diagonal': [str(value) for value in diagonal],
            'full_finite_lower_bound': '1/4', 'full_finite_upper_bound': '9/4',
            'basis_reconstruction_cases': 16, 'covariance_cells': covariance_cells,
            'old_hostile_separation': {'rho_plus_record': '3/8', 'rho_minus_record': '1/8', 'setting': 'X,Z with +,+ outcomes'},
            'continuous_control_dimension_unchanged': 2,
            'boundary': 'Mathematical source-polynomial probes under declared markings/complex background. No physical detector, Born-law derivation or infinite stability.'}


def main():
    contract_path = HOME / 'contracts/pilot-observer-extension.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    previous = validate_previous(json.loads((HOME / 'contracts/programme-hierarchy.v8.json').read_text()),
                                 json.loads((HOME / 'results/pilot-capability-audit.json').read_text()))
    controls = audit()
    paths = [contract_path, HOME / 'pilot_observers.py', Path(__file__), HOME / 'PILOT-OBSERVER-EXTENSION.md',
             HOME / 'results/pilot-capability-audit.json',
             ROOT / 'research/nima/agda/TickSpectralFactorOperators.agda']
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    result = {'schema': 'marici.conjecture-net.pilot-observer-extension-audit.v1', 'status': 'pass',
              'validation_only': True, 'outcome': None, 'root_outcome': None,
              'controls': controls, 'previous_capability_validation': previous, 'source_sha256': pins,
              'physical_observers_authorized': False, 'new_controls_supplied': False,
              'new_kernel_observer_theorem': False, 'infinite_completion_stability_proved': False,
              'programme_outcomes_promoted': False}
    destination = HOME / 'results/pilot-observer-extension-audit.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'mathematical_observation_rank': 16, 'physical_observer_authorization': False,
                      'continuous_controls_unchanged': 2}, indent=2))


if __name__ == '__main__':
    main()
