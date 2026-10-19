"""Exact local Fourier/cap/budget controls, not an infinite source-tail prover."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_relativistic_scalar_witness import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-electric-magnetic-reader.v1.json'
NOTE = BASE+'yang-mills-electric-magnetic-reader-v1.md'
SELF = BASE+'checkers/check_yang_mills_electric_magnetic_reader.py'
OUT = ROOT/(BASE+'results/yang-mills-electric-magnetic-reader-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def casimir(twice_spin):
    return F(twice_spin*(twice_spin+2), 4)


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def transpose(a):
    return list(map(list, zip(*a)))


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def kron(a, b):
    return [[a[i//len(b)][j//len(b[0])]*b[i % len(b)][j % len(b[0])]
             for j in range(len(a[0])*len(b[0]))] for i in range(len(a)*len(b))]


def partial_trace(a):
    return [[sum(a[2*i+k][2*j+k] for k in range(2)) for j in range(2)] for i in range(2)]


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 4, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'scope')
    require(c['net_update']['ready_frontier'] == ['native-free-magnetic-fluctuation-scaling'] and c['net_update']['parent_outcome'] is None, 'native next source test')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-relativistic-scalar-witness-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh scalar bridge and unchanged frozen predecessors')
    counts = {}
    count = 0
    for a, b in product([0, 1, 2, 3, 4, 6], repeat=2):
        outputs = list(range(abs(a-b), a+b+1, 2))
        require(sum(l+1 for l in outputs) == (a+1)*(b+1), 'SU2 Clebsch-Gordan dimensions')
        require(all(casimir(l) <= 2*(casimir(a)+casimir(b)) for l in outputs), 'Casimir product weight')
        require(all(1+casimir(l) <= 2*(1+casimir(a))*(1+casimir(b)) for l in outputs), 'weighted Fourier algebra factor2')
        count += 1
    counts['weighted_fusion_packets'] = count
    I = [[F(1), F(0)], [F(0), F(1)]]
    X = [[F(0), F(1)], [F(1), F(0)]]
    Z = [[F(1), F(0)], [F(0), F(-1)]]
    arrays = [
        [[F(i == j == 0) for j in range(4)] for i in range(4)],
        [[F(i == 0 and j == 3) for j in range(4)] for i in range(4)],
        [[F(i == 1 and j == 2)-F(i == 2 and j == 1) for j in range(4)] for i in range(4)],
        [[F(i-2*j, 6) for j in range(4)] for i in range(4)]]
    count = 0
    for A, B, U in product(arrays, [I, X, [[F(1), F(2)], [F(0), F(-1)]]], [I, X, Z]):
        require(mul(transpose(U), U) == I, 'rest-variable unitary')
        evaluated = partial_trace(mul(kron(I, U), A))
        require(tr(mul(B, evaluated)) == tr(mul(kron(B, U), A)), 'partial-trace dual identity underlying norm contraction')
        count += 1
    counts['partial_trace_duality_packets'] = count
    count = 0
    for cutoff, base, amplitude in product([0, 1, 2, 4, 8], [1, 2, 4, 8], [F(1, 4), F(1), F(2)]):
        spins = [base+i for i in range(4)]
        weights = [amplitude/F(2**(i+1)) for i in range(4)]
        hard_squared = sum(w*w*casimir(j)**2/((j+1)*(1+casimir(j))**2)
                           for j, w in zip(spins, weights) if j > cutoff)
        soft_squared = sum(w*w*max(F(0), casimir(j)-casimir(cutoff))**2/((j+1)*(1+casimir(j))**2)
                           for j, w in zip(spins, weights))
        tail_weight = sum(w for j, w in zip(spins, weights) if j > cutoff)
        require(soft_squared <= hard_squared <= tail_weight**2/(cutoff+2), 'Plancherel tail pays the SU2 dimension,not a moment-only guess')
        count += 1
    counts['weighted_Plancherel_tail_packets'] = count
    count = 0
    wrong_gain_defect = None
    for j, amplitude in product([2, 4, 8, 16], [F(1, 4), F(1), F(2)]):
        d, C = j+1, casimir(j)
        actual_squared = amplitude**2*C*C/(d*(1+C)**2)
        wrong_squared = amplitude**2/d**2
        require(actual_squared > wrong_squared, 'rank-one Fourier block rejects a d^-1 norm rate')
        if j == 2 and amplitude == 1:
            wrong_gain_defect = actual_squared-wrong_squared
            require(wrong_gain_defect == F(1, 27), 'exact squared-rate counterreader')
        count += 1
    counts['incorrect_dimension_gain_packets'] = count
    count = 0
    for R, cutoff in product([F(0), F(1, 64), F(1, 16), F(1, 8), F(9, 64)], [0, 1, 2, 4, 8]):
        Kbar = R/((1-R)*(1-2*R))
        require(0 <= Kbar <= F(288, 1265) < F(1, 4), 'rational uniform tail coefficient')
        require(Kbar**2/(cutoff+2) <= F(1, 16)/(cutoff+2), 'rational squared vacuum-tail envelope')
        if R == 0:
            require(Kbar == 0, 'actual free electric vacuum tail vanishes')
        count += 1
    counts['rational_tail_constant_packets'] = count
    count = 0
    for power, N in product([0, 2, 4, 8], [1, 2, 3, 4, 8, 16]):
        D, S = N**power, N**(4*power+2)
        root_S = N**(2*power+1)
        require(root_S**2 == S and S == N*N*D**4, 'one common cap schedule')
        delta = F(D, 4*root_S)
        require(delta == F(1, 4*N*D) and 2*D*delta == F(1, 2*N), 'two-point error pays both growing vectors')
        require(D*(S*(S+1)+1) <= 3*D*S*S == 3*N**(9*power+4), 'polynomial operator-norm budget')
        count += 1
    counts['common_cap_schedule_packets'] = count
    count = 0
    for N in [1, 2, 3, 4, 8, 16]:
        electric, magnetic, S = 12*N**4, 6*N**4, N**18
        V, delta = 9*N**4, F(3, N**5)
        require(electric*F(1, 4)+magnetic <= V, 'unit-box primitive vacuum norm bound')
        require(electric*F(1, 4*N**9) == delta and 2*V*delta == F(54, N), 'unit-box tail and two-point rate')
        require(electric*S*(S+1)+magnetic <= 30*N**40, 'native bounded reader norm')
        require(F(12*N**3, 2)*(60*N**40)**2 == 21600*N**83, 'centered locality pair budget')
        count += 1
    counts['unit_box_reader_packets'] = count
    count = 0
    for N in [1, 2, 4, 8, 16, 32]:
        original, perturbed = F(N*N), F(N*N)+F(1, N)
        difference = (perturbed**2-original**2)/2  # positive time exp(-H*t)=1/2 on this mode
        require(perturbed-original == F(1, N) and difference >= N, 'vector convergence alone does not control normalized two-point functions')
        count += 1
    counts['vector_vs_two_point_scope_packets'] = count
    count = 0
    for twice_spin in [2, 4, 8, 16, 32, 64]:
        C, d = casimir(twice_spin), twice_spin+1
        high_mass = 1/C**2
        require(0 < high_mass < 1 and high_mass*C*C == 1, 'bounded Casimir second moment can retain tail norm1')
        weighted_fourier_high_squared = d*(1+C)**2/C**2
        require(weighted_fourier_high_squared >= d, 'counterfamily violates the actual uniform weighted Fourier premise')
        count += 1
    counts['second_moment_tail_scope_packets'] = count
    count = 0
    offsets = [(F(0),)*3, (F(1, 2), F(0), F(0)), (F(1, 2), F(1, 2), F(0)), (F(1, 2),)*3]
    for spacing, N, offset in product([F(1), F(1, 2), F(1, 4)], [1, 2, 4], offsets):
        weight_sum = sum(spacing**3/(1+max(abs(spacing*(n+theta)) for n, theta in zip(point, offset)))**4
                         for point in product(range(-N, N+1), repeat=3))
        require(weight_sum <= 128, 'finite prefixes respect the analytic shifted-grid bound')
        count += 1
    counts['weighted_lattice_count_packets'] = count
    require(4*384**2*2*F(1, 4) == 294912, 'joint tempered cap-removal coefficient')
    count = 0
    for cutoff in [0, 1, 2, 4, 8]:
        vacuum_spin = 0
        require(casimir(vacuum_spin) == min(casimir(vacuum_spin), casimir(cutoff)) == 0, 'actual free vacuum is unchanged and annihilated by electric cap')
        require(casimir(cutoff) >= 0, 'cap is an observer,not deletion of high-spin source states')
        count += 1
    counts['actual_free_vacuum_cap_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 252, 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path]
    paths += [BASE+name for name in [
        'yang-mills-anchored-casimir-v1.md', 'yang-mills-weighted-fourier-v1.md',
        'yang-mills-ground-state-transfer-v1.md', 'yang-mills-relativistic-scalar-witness-v1.md',
        'yang-mills-arbitrary-clock-locality-v1.md']]
    return {
        'schema': 'marici.yang-mills-electric-magnetic-reader.result.v1', 'passed': True,
        'strength': 'written source-conditional Casimir vacuum tail and bounded reader/S-prime cap-removal theorem; no actual Lorentz scalar limit',
        'coverage': counts, 'new_exact_controls': 252,
        'predecessor_scalar_controls_replayed': previous['new_exact_controls'],
        'uniform_rational_K_bound': '288/1265',
        'incorrect_dimension_rate_squared_defect': str(wrong_gain_defect),
        'second_moment_tail_norm_defect': '1',
        'unit_box_spin_cap_power': 18, 'unit_box_two_point_error_coefficient': '54',
        'joint_tempered_cap_removal_coefficient': 294912,
        'actual_source_Hamiltonian_or_vacuum_truncated': False,
        'individual_tempered_limit_or_Lorentz_scalar_constructed': False,
        'finite_controls_certify_analytic_theorem': False,
        'independent_analytic_review_complete': False,
        'physical_continuum_or_Yang_Mills_root_discharged': False,
        'next_executable': 'native-free-magnetic-fluctuation-scaling',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
