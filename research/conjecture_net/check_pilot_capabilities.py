"""Exact finite action/observation/stability audit, not physical capability admission."""
from fractions import Fraction as F
import hashlib
from itertools import product
import json
from pathlib import Path
from check_structural_pilot_transport import zeros, identity, add, scale, mul, transpose, complex_mul
from check_programme_carrier import validate as validate_carrier
from pilot_carrier import Operation, native_permutation

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def rank(rows):
    a = [[F(value) for value in row] for row in rows]
    pivot = 0
    for column in range(len(a[0]) if a else 0):
        found = next((r for r in range(pivot, len(a)) if a[r][column]), None)
        if found is None:
            continue
        a[pivot], a[found] = a[found], a[pivot]
        divisor = a[pivot][column]
        a[pivot] = [value / divisor for value in a[pivot]]
        for r in range(len(a)):
            if r != pivot and a[r][column]:
                factor = a[r][column]
                a[r] = [x - factor * y for x, y in zip(a[r], a[pivot])]
        pivot += 1
        if pivot == len(a):
            break
    return pivot


def flatten(a):
    return [value for row in a for value in row]


def adjoint(m):
    return transpose(m[0]), scale(-1, transpose(m[1]))


def trace_pair(m, n):
    real, imag = complex_mul(m, n)
    require(sum(imag[i][i] for i in range(len(imag))) == 0, 'nonreal Hermitian trace pairing')
    return sum(real[i][i] for i in range(len(real)))


def kron(a, b):
    return [[a[i // len(b)][j // len(b)] * b[i % len(b)][j % len(b)]
             for j in range(len(a) * len(b))] for i in range(len(a) * len(b))]


def tensor(m, n):
    a, b = m
    c, d = n
    return add(kron(a, c), scale(-1, kron(b, d))), add(kron(a, d), kron(b, c))


def audit():
    i4, z4 = identity(4), zeros(4)
    left = [list(row) for row in native_permutation(Operation.LEFT)]
    right = [list(row) for row in native_permutation(Operation.RIGHT)]
    ql = scale(F(1, 2), add(i4, scale(-1, left)))
    qr = scale(F(1, 2), add(i4, scale(-1, right)))
    action_basis = [i4, left, right, mul(left, right)]
    action_rank = rank([flatten(matrix) for matrix in action_basis])
    require(action_rank == 4, 'native action algebra rank changed')
    require(all(len({tuple(matrix[row][source] for row in range(4)) for matrix in action_basis}) == 4
                for source in range(4)), 'native label orbit is not transitive')
    require(mul(ql, qr) == mul(qr, ql), 'native generators no longer commute')
    lie_rank = rank([flatten(ql), flatten(qr)])
    require(lie_rank == 2, 'continuous generator rank changed')
    sectors = [scale(F(1, 4), mul(add(i4, scale(sign_l, left)), add(i4, scale(sign_r, right))))
               for sign_l, sign_r in product((-1, 1), repeat=2)]
    for index, sector in enumerate(sectors):
        require(mul(sector, sector) == sector and transpose(sector) == sector
                and sum(sector[i][i] for i in range(4)) == 1, 'joint sector projection failed')
        for other in sectors[index + 1:]:
            require(mul(sector, other) == z4, 'sector orthogonality failed')
    total = z4
    for sector in sectors:
        total = add(total, sector)
    require(total == i4, 'carrier sector splitting incomplete')
    pauli = {
        'I': (identity(2), zeros(2)),
        'X': ([[F(0), F(1)], [F(1), F(0)]], zeros(2)),
        'Y': (zeros(2), [[F(0), F(-1)], [F(1), F(0)]]),
        'Z': ([[F(1), F(0)], [F(0), F(-1)]], zeros(2))}
    labels = [a + b for a, b in product(pauli, repeat=2)]
    operators = [tensor(pauli[label[0]], pauli[label[1]]) for label in labels]
    require(all(trace_pair(a, b) == (4 if ia == ib else 0)
                for ia, a in enumerate(operators) for ib, b in enumerate(operators)), 'Pauli basis pairing failed')
    coordinate = []
    for j in range(4):
        matrix = zeros(4)
        matrix[j][j] = F(1)
        coordinate.append((matrix, z4))
    native_rows = [[trace_pair(effect, p) / 4 for p in operators] for effect in coordinate]
    require(rank(native_rows) == 4, 'native mathematical observation rank changed')
    settings = []
    rows = []
    effects = []
    for a, b in product((0, 1), repeat=2):
        # Index 1 means t=1/2, where the accepted phase is -i.
        ul = (i4, z4) if a == 0 else (add(i4, scale(-1, ql)), scale(-1, ql))
        ur = (i4, z4) if b == 0 else (add(i4, scale(-1, qr)), scale(-1, qr))
        u = complex_mul(ur, ul)
        settings.append((a, b))
        for effect in coordinate:
            propagated = complex_mul(adjoint(u), complex_mul(effect, u))
            effects.append(propagated)
            rows.append([trace_pair(propagated, p) / 4 for p in operators])
    observation_rank = rank(rows)
    require(observation_rank == 9, 'propagated observation rank changed')
    invisible = [label for column, label in enumerate(labels) if all(row[column] == 0 for row in rows)]
    require(set(invisible) == {label for label in labels if 'X' in label} and len(invisible) == 7,
            'invisible directions changed')
    visible_columns = [column for column, label in enumerate(labels) if label not in invisible]
    gram = [[sum(row[a] * row[b] for row in rows) for b in visible_columns] for a in visible_columns]
    require(all(gram[a][b] == 0 for a in range(9) for b in range(9) if a != b), 'visible Gram not diagonal')
    diagonal = [gram[i][i] for i in range(9)]
    require(min(diagonal) == F(1, 4) and max(diagonal) == 1, 'finite stability bounds changed')
    xi = operators[labels.index('XI')][0]
    rho_plus = (add(scale(F(1, 4), i4), scale(F(1, 8), xi)), z4)
    rho_minus = (add(scale(F(1, 4), i4), scale(F(-1, 8), xi)), z4)
    projector_plus = scale(F(1, 2), add(i4, xi))
    projector_minus = scale(F(1, 2), add(i4, scale(-1, xi)))
    require(mul(projector_plus, projector_plus) == projector_plus and mul(projector_minus, projector_minus) == projector_minus
            and mul(projector_plus, projector_minus) == z4, 'hostile positivity decomposition failed')
    require(rho_plus[0] == add(scale(F(3, 8), projector_plus), scale(F(1, 8), projector_minus)) and
            rho_minus[0] == add(scale(F(1, 8), projector_plus), scale(F(3, 8), projector_minus)), 'hostile positive weights failed')
    require(rho_plus != rho_minus and trace_pair(rho_plus, (i4, z4)) == trace_pair(rho_minus, (i4, z4)) == 1,
            'hostile state normalization failed')
    require(all(trace_pair(effect, rho_plus) == trace_pair(effect, rho_minus) for effect in effects), 'hostile record equality failed')
    return {
        'carrier_splitting': {'orthogonal_joint_sectors': 4, 'rank_each': 1, 'background': 'declared free complex linearization'},
        'action': {'native_label_orbit_size': 4, 'linear_action_algebra_dimension': action_rank,
                   'full_complex_matrix_algebra_dimension': 16, 'continuous_control_lie_dimension': lie_rank,
                   'full_unitary_control_dimension': 16, 'full_unitary_control_supplied': False,
                   'joint_sector_relative_phase_control_dimension': 2,
                   'arbitrary_joint_sector_relative_phases_dimension': 3},
        'observation': {'native_coordinate_readout_rank': 4, 'native_label_separation': True,
                        'hermitian_domain_dimension': 16, 'trace_one_tangent_dimension': 15,
                        'propagated_readout_rank': observation_rank, 'trace_one_visible_tangent_dimension': 8,
                        'invisible_pauli_directions': invisible, 'full_hermitian_observation_supplied': False,
                        'all_time_upper_bound': 'Written local-X rotation argument confines every propagated coordinate effect to span{I,Y,Z} tensor span{I,Y,Z}; four exact settings attain rank nine.'},
        'finite_stability': {'visible_pauli_coordinate_gram_diagonal': [str(value) for value in diagonal],
                             'visible_lower_bound': '1/4', 'visible_upper_bound': '1',
                             'full_hermitian_domain_lower_bound': '0', 'infinite_completion_claimed': False},
        'hostile': {'states': '(I4 +/- (1/2) X tensor I)/4', 'trace_each': '1',
                    'positive_eigenvalues': ['3/8', '1/8'], 'multiplicity_each': 2,
                    'same_propagated_coordinate_records': True,
                    'boundary': 'Declared mathematical density/trace model, not an authorized physical preparation or derived Born rule.'}}


def validate_contract(contract):
    require(contract['source_instance'] == 'native-bool-square-pilot', 'wrong capability source')
    require(all(value is False for value in contract['boundary'].values()), 'capability boundary upgrade')
    require(contract['predeclared_basis']['operators'] == 'All sixteen tensor Pauli matrices from I,X,Y,Z on each factor.',
            'state/operator domain changed')


def main():
    contract_path = HOME / 'contracts/pilot-capability-audit.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    carrier = validate_carrier(json.loads((HOME / 'contracts/programme-hierarchy.v7.json').read_text()),
                               json.loads((HOME / 'results/pilot-carrier-interface-audit.json').read_text()))
    gates = audit()
    paths = [contract_path, Path(__file__), HOME / 'PILOT-CAPABILITY-AUDIT.md',
             HOME / 'pilot_carrier.py', HOME / 'results/pilot-carrier-interface-audit.json']
    pins = {path.relative_to(ROOT).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest() for path in paths}
    result = {'schema': 'marici.conjecture-net.pilot-capability-audit-result.v1',
              'status': 'pass', 'validation_only': True, 'outcome': None, 'root_outcome': None,
              'source_sha256': pins, 'live_finite_fragment_validation': carrier, 'gates': gates,
              'physical_capabilities_authorized': False, 'new_kernel_proof': False,
              'programme_target_outcomes_promoted': False}
    destination = HOME / 'results/pilot-capability-audit.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({'status': 'pass', 'action_algebra_dimension': 4, 'propagated_observation_rank': 9,
                      'invisible_hermitian_directions': 7, 'physical_authorization': False}, indent=2))


if __name__ == '__main__':
    main()
