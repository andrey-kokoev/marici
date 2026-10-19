"""Exact coordinate transport audit; does not admit a programme outcome."""
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
import sys

HOME = Path(__file__).resolve().parent
ROOT = HOME.parents[1]
sys.path.insert(0, str(ROOT / 'research/nima/checkers'))
from export_operational_whole_return import check as check_export, POINTER

CONTRACT = HOME / 'contracts/structural-pilot-transport.v1.json'


def zeros(n):
    return [[F(0) for _ in range(n)] for _ in range(n)]


def identity(n):
    result = zeros(n)
    for i in range(n):
        result[i][i] = F(1)
    return result


def add(a, b):
    return [[x + y for x, y in zip(row, other)] for row, other in zip(a, b)]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def mul(a, b):
    n = len(a)
    result = zeros(n)
    for i in range(n):
        for k in range(n):
            if a[i][k]:
                for j in range(n):
                    if b[k][j]:
                        result[i][j] += a[i][k] * b[k][j]
    return result


def transpose(a):
    return [list(row) for row in zip(*a)]


def realify(a, b):
    n = len(a)
    return [[a[i][j] for j in range(n)] + [-b[i][j] for j in range(n)] for i in range(n)] + \
           [[b[i][j] for j in range(n)] + [a[i][j] for j in range(n)] for i in range(n)]


def complex_mul(m, n):
    a, b = m
    c, d = n
    return add(mul(a, c), scale(-1, mul(b, d))), add(mul(a, d), mul(b, c))


def unit(n, i, j):
    result = zeros(n)
    result[i][j] = F(1)
    return result


def require(condition, message):
    if not condition:
        raise ValueError(message)


def validate_contract(contract):
    require(contract['source_instance'] == 'native-bool-square-pilot', 'different source instance')
    require(set(contract['targets']) == {'unitary-local-return-pilot', 'hamiltonian-symplectic-pilot'}, 'wrong pilot pair')
    witness = contract['common_witness']
    require(witness['labels'] == ['00', '01', '10', '11'], 'source coordinate order changed')
    require(witness['generators_t'] == 'H_j=pi Q_j', 'generator scale changed')
    require(witness['return_convention'] == 'From P_R P_L e_s, execute positive-phase legs in reversed native order on [0,2]; not inverse-phase time reversal', 'return orientation changed')
    maps = {item['id']: item for item in contract['maps']}
    require(maps['scale-transport']['formula'] == 'theta=pi*t; d/dt=pi*d/dtheta', 'scale transport missing')
    require(maps['operator-realification']['formula'] == 'R(A+i B)=[[A,-B],[B,A]]', 'realification sign changed')
    boundary = contract['verification_boundary']
    require(all(boundary[key] is False for key in ('semantic_correspondence_kernel_proved',
            'new_realification_kernel_proved', 'physical_recovery_verified',
            'universal_carrier_embedding_proved', 'programme_target_outcomes_promoted')), 'verification-level overclaim')


def algebra_audit():
    n = 4
    zero, ident = zeros(n), identity(n)
    j = realify(zero, scale(-1, ident))
    basis = [(unit(n, i, k), zero) for i in range(n) for k in range(n)] + \
            [(zero, unit(n, i, k)) for i in range(n) for k in range(n)]
    # Multiplication and action are bilinear over R. Checking a full real
    # matrix-unit basis determines the general coefficient identities.
    for m in basis:
        a, b = m
        r = realify(a, b)
        require(realify(transpose(a), scale(-1, transpose(b))) == transpose(r), 'adjoint/transpose mismatch')
        require(mul(r, j) == mul(j, r), 'complex structure mismatch')
        for v in range(2 * n):
            q = [F(int(v == k)) for k in range(n)]
            p = [F(int(v == n + k)) for k in range(n)]
            expected = [sum(a[i][k] * q[k] - b[i][k] * p[k] for k in range(n)) for i in range(n)] + \
                       [sum(b[i][k] * q[k] + a[i][k] * p[k] for k in range(n)) for i in range(n)]
            require([r[i][v] for i in range(2 * n)] == expected, 'state/operator square mismatch')
        for other in basis:
            require(realify(*complex_mul(m, other)) == mul(r, realify(*other)), 'composition mismatch')
    permutations = []
    projectors = []
    for mask in (2, 1):
        p = zeros(n)
        for label in range(n):
            p[label ^ mask][label] = F(1)
        q = scale(F(1, 2), add(ident, scale(-1, p)))
        require(mul(q, q) == q and transpose(q) == q, 'native projector law failed')
        require(mul(p, p) == ident, 'native flip failed')
        # H=pi Q is represented coefficientwise: pi multiplies this exact
        # normalized Q. Every asserted identity is homogeneous in that scale.
        a_h = realify(zero, scale(-1, q))
        hessian = realify(q, zero)
        require(a_h == mul(j, hessian), 'Hamiltonian-gradient correspondence failed')
        require(add(mul(transpose(a_h), j), mul(j, a_h)) == zeros(2 * n), 'infinitesimal symplectic law failed')
        for zr, zi in ((F(1), F(0)), (F(-1), F(0)), (F(0), F(-1)), (F(3, 5), F(4, 5))):
            # Finite phase controls only; all-time law is from projectors,
            # written algebra, and the live imported operational certificate.
            u = realify(add(ident, scale(zr - 1, q)), scale(zi, q))
            require(mul(transpose(u), u) == identity(2 * n), 'phase control orthogonality failed')
            require(mul(mul(transpose(u), j), u) == j, 'phase control symplectic law failed')
        permutations.append(p)
        projectors.append(q)
    left, right = permutations
    require(mul(left, right) == mul(right, left), 'native factor composition failed')
    require(mul(projectors[0], projectors[1]) == mul(projectors[1], projectors[0]), 'generator commutation failed')
    for source in range(n):
        for first, second in ((2, 1), (1, 2)):
            native_target = source ^ 2 ^ 1
            seam = native_target ^ first
            finish = seam ^ second
            require(finish == source, 'return attachment failed')
            require(seam != (native_target ^ second), 'schedule seam separation failed')
    return {'real_matrix_basis_size': len(basis), 'composition_basis_pairs': len(basis) ** 2,
            'state_action_basis_pairs': len(basis) * 2 * n, 'native_generators': 2,
            'finite_unit_phase_controls_per_generator': 4,
            'scale_handling': 'pi retained as a symbolic common scalar; homogeneous normalized generator identities checked exactly',
            'all_time_analytic_evidence': 'existing live operational export plus written interpretation/realification argument; not inferred from phase controls'}


def main():
    sources = [CONTRACT, HOME / 'STRUCTURAL-PILOT-TRANSPORT.md', Path(__file__),
               ROOT / 'research/nima/agda/ObserverCoherenceCube.agda',
               ROOT / 'research/nima/agda/TickOperationalWholeReturnKernel.agda',
               ROOT / 'research/nima/standard-spectral-correspondence.md',
               ROOT / 'research/nima/native-square-controlled-hamiltonian.md',
               HOME / 'contracts/programme-source-interface.v1.json',
               HOME / 'contracts/programme-targets.v1.json']
    pins = {p.relative_to(ROOT).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    validate_contract(contract)
    imported = check_export(json.loads((ROOT / POINTER).read_text(encoding='utf-8')))
    controls = algebra_audit()
    require(all(hashlib.sha256((ROOT / path).read_bytes()).hexdigest() == digest for path, digest in pins.items()), 'sources changed during audit')
    result = {'schema': 'marici.conjecture-net.structural-pilot-transport-audit.v1',
              'status': 'pass', 'validation_only': True, 'claim': contract['id'],
              'outcome': None, 'root_outcome': None, 'target_outcomes_promoted': False,
              'imported_operational_evidence': imported, 'exact_coordinate_controls': controls,
              'source_sha256': pins, 'new_transport_kernel_proved': False,
              'physical_recovery_verified': False, 'universal_carrier_embedding_proved': False,
              'proof_kind': 'written_general_coordinate_transport_with_exact_rational_basis_controls_and_live_mixed_operational_import',
              'remaining_admission': 'Programme-level scope/transport admission and any stronger kernel or physical requirements remain open.'}
    destination = HOME / 'results/structural-pilot-transport-audit.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(result, indent=2, sort_keys=True) + '\n', encoding='utf-8')
    print(json.dumps({key: result[key] for key in ('status', 'outcome', 'new_transport_kernel_proved', 'physical_recovery_verified')}, indent=2))


if __name__ == '__main__':
    main()
