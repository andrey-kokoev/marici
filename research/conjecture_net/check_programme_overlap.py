"""Audit structural readout descent; never infer physical probabilities or energy."""
import hashlib
import json
from pathlib import Path
from check_structural_pilot_transport import zeros, identity, unit, realify, scale
from check_programme_transport import validate as validate_transport

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(contract['status'] == 'proposed_candidate', 'overlap prematurely admitted')
    require(len(contract['overlaps']) == 1, 'unsupported cross-sector overlap')
    overlap = contract['overlaps'][0]
    require(overlap['targets'] == ['unitary-local-return-pilot', 'hamiltonian-symplectic-pilot'] and
            overlap['common_source_instance'] == 'native-bool-square-pilot', 'wrong overlap source/targets')
    require(overlap['parameter_map'] == 'theta=pi*t', 'overlap scale mismatch')
    require(overlap['kernel_observable_transport_proved'] is False and
            overlap['admission_status'] == 'not_admitted_as_programme_proof_link', 'kernel/admission overclaim')
    laws = {readout['id']: readout for readout in overlap['readouts']}
    require(set(laws) == {'squared-norm', 'hermitian-quadratic', 'canonical-energy', 'coordinate-intensity'}, 'readout inventory changed')
    require(laws['canonical-energy']['law'] == 'z* H z=2 E_H(x)', 'energy normalization mismatch')
    require(all(readout['role'] == 'mathematical_readout' and readout['physical_authorization'] is False
                for readout in laws.values()), 'mathematical record promoted to physical readout')
    require(all(contract['physical_readout_gate'][key] is False for key in
                ('normalization_is_born_rule', 'canonical_energy_is_physical_energy',
                 'retained_schedule_is_physical_clock', 'scalar_readout_is_full_record')), 'physical promotion policy changed')
    require(contract['unconnected_interfaces'][0]['target'] == 'compton-complete-record-calibration' and
            contract['unconnected_interfaces'][0]['status'] == 'source_bridge_missing', 'unproved Compton bridge')


def validate_attachment(hierarchy, terms, contract):
    previous = json.loads((HOME / 'contracts/programme-hierarchy.v4.json').read_text())
    require(hierarchy['phase'] == 'defined_finite_structural_overlap', 'wrong overlap phase')
    for key in ('root', 'obligations', 'existing_net_links', 'promotion_policy', 'structural_pilot_transports'):
        require(hierarchy[key] == previous[key], 'programme status changed: ' + key)
    status = hierarchy['overlap_status']
    require(status['physical_sector_overlap'] == 'not_defined' and status['compton_source_bridge'] == 'missing'
            and status['proof_bearing'] is False, 'physical overlap overclaim')
    shared = next(term for term in terms['terms'] if term['id'] == 'shared_regimes')
    require(shared['status'] == 'reviewed_candidate' and shared['residuals'], 'candidate overlap residuals missing')
    evidence = shared['evidence'][0]
    expected = hashlib.sha256((HOME / 'contracts/programme-overlaps.v1.json').read_bytes()).hexdigest()
    require(evidence['source_sha256'] == expected and evidence['role'] == 'finite_structural_overlap_specification_not_physical_proof',
            'overlap definition evidence mismatch')
    require(contract['overlaps'][0]['admission_status'] == 'not_admitted_as_programme_proof_link', 'overlap admission overclaim')


def quadratic(matrix, x):
    return sum(x[i] * matrix[i][j] * x[j] for i in range(len(x)) for j in range(len(x)))


def complex_expectation(a, b, x):
    n = len(a)
    q, p = x[:n], x[n:]
    real = [sum(a[i][k] * q[k] - b[i][k] * p[k] for k in range(n)) for i in range(n)]
    imag = [sum(b[i][k] * q[k] + a[i][k] * p[k] for k in range(n)) for i in range(n)]
    return sum(q[i] * real[i] + p[i] * imag[i] for i in range(n)), \
           sum(q[i] * imag[i] - p[i] * real[i] for i in range(n))


def coefficient_audit():
    n = 4
    basis = [(unit(n, i, i), zeros(n)) for i in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            symmetric, skew = zeros(n), zeros(n)
            symmetric[i][j] = symmetric[j][i] = 1
            skew[i][j], skew[j][i] = 1, -1
            basis.extend(((symmetric, zeros(n)), (zeros(n), skew)))
    # Unit vectors and pair sums determine every coefficient of a real
    # homogeneous quadratic form. Hermitian matrix units determine M linearly.
    vectors = [[int(i == j) for i in range(2 * n)] for j in range(2 * n)]
    vectors += [[int(k == i or k == j) for k in range(2 * n)]
                for i in range(2 * n) for j in range(i + 1, 2 * n)]
    for a, b in basis:
        for x in vectors:
            real, imag = complex_expectation(a, b, x)
            require(imag == 0 and real == quadratic(realify(a, b), x), 'Hermitian readout descent failed')
    for x in vectors:
        expected = sum(v * v for v in x)
        require(complex_expectation(identity(n), zeros(n), x) == (expected, 0), 'norm descent failed')
        for j in range(n):
            require(complex_expectation(unit(n, j, j), zeros(n), x) == (x[j] ** 2 + x[n+j] ** 2, 0),
                    'coordinate intensity mismatch')
    # Equal scalar readouts cannot establish full-state/record identity.
    first = vectors[0]
    opposite = [-v for v in first]
    require(first != opposite and all(quadratic(realify(a, b), first) == quadratic(realify(a, b), opposite)
                                     for a, b in basis), 'quotient hostile missing')
    return {'hermitian_basis_size': len(basis), 'quadratic_coefficient_controls': len(vectors),
            'readout_coefficient_identities': len(basis) * len(vectors),
            'scalar_quotient_hostile': 'x and -x have equal Hermitian quadratic records; full state identity is not inferred',
            'energy_convention': 'Hermitian expectation is twice canonical quadratic Hamiltonian; pi is retained as a shared symbolic scale',
            'evidence_boundary': 'Complete polynomial-coefficient controls and written identities, not measured data or a kernel theorem'}


def main():
    hierarchy = json.loads((HOME / 'contracts/programme-hierarchy.v4.json').read_text())
    transport_audit = json.loads((HOME / 'results/structural-pilot-transport-audit.json').read_text())
    transport = validate_transport(hierarchy, transport_audit)
    contract_path = HOME / 'contracts/programme-overlaps.v1.json'
    contract = json.loads(contract_path.read_text())
    validate_contract(contract)
    current = json.loads((HOME / 'contracts/programme-hierarchy.v5.json').read_text())
    terms = json.loads((HOME / 'contracts/programme-terms.v4.json').read_text())
    validate_attachment(current, terms, contract)
    controls = coefficient_audit()
    paths = [contract_path, Path(__file__), HOME / 'contracts/programme-hierarchy.v5.json',
             HOME / 'contracts/programme-terms.v4.json', HOME / 'STRUCTURAL-PILOT-TRANSPORT.md',
             HOME / 'contracts/structural-pilot-transport.v1.json',
             HOME / 'results/structural-pilot-transport-audit.json']
    pins = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    result = {'schema': 'marici.conjecture-net.programme-overlap-audit.v1', 'status': 'pass',
              'validation_only': True, 'outcome': None, 'root_outcome': None,
              'source_sha256': pins, 'live_transport_validation': transport, 'coordinate_controls': controls,
              'kernel_observable_transport_proved': False, 'physical_readout_authorized': False,
              'empirical_confirmation': False, 'programme_proof_links_admitted': 0}
    destination = HOME / 'results/programme-overlap-audit.json'
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'outcome', 'physical_readout_authorized', 'empirical_confirmation')}, indent=2))


if __name__ == '__main__':
    main()
