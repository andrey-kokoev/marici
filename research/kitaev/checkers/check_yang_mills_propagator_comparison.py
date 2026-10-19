"""Exact majorants/hostiles for the written actual-propagator comparison theorem."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_thermodynamic_form import report as form_report, matmul, matvec, dot, det
from check_yang_mills_thermodynamic_vacuum import invert

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-propagator-comparison.v1.json'
NOTE = BASE+'yang-mills-propagator-comparison-v1.md'
SELF = BASE+'checkers/check_yang_mills_propagator_comparison.py'
OUT = ROOT/(BASE+'results/yang-mills-propagator-comparison-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 2 and all(v is False for v in c['boundary'].values()), 'scope')
    require(c['subnet']['outcome'] is None and c['subnet']['ready_frontier'] == ['source-compatible-multi-time-correlations'], 'frontier/root')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(not c['parent_net']['discharges_parent'], 'parent promotion')
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent closed')
    upstream = form_report()
    require(upstream['passed'], 'predecessor regression')
    require(upstream == json.loads((ROOT/(BASE+'results/yang-mills-thermodynamic-form-v1.json')).read_text()), 'stale form receipt')
    a = F(4, 3)
    support_cases = 0
    for n in range(1, 65):
        require(F(n+1, 2**n)*a**(n-1) <= 1, 'weighted Hessian support factor')
        require(F(n+2, n+1)*F(2, 3) <= 1, 'all-later support recurrence')
        support_cases += 1
    spin_cases = 0
    for n in range(1, 6):
        for labels in product(range(4), repeat=n):
            spins = [F(x, 2) for x in labels]
            J = sum(spins)
            C = sum(x*(x+1) for x in spins)
            for j in spins:
                require(j*J <= F(n+1, 2)*C, 'anchored Casimir derivative activity')
                spin_cases += 1

    # Connected finite scalar-spin fixture; it is not a finite SU2 source solver.
    n = 5
    terms = []
    for i in range(n):
        for j in range(i, n):
            s = frozenset(range(i, j+1))
            w = F(1, 8192)
            W = (1+F(3, 4)*len(s))*w
            terms.append((s, w, W))
    R = max(sum(2**len(s)*W for s, w, W in terms if i in s) for i in range(n))
    require(R < F(9, 64), 'fixture source window')
    box = frozenset({1, 2, 3})
    K = 2
    hK = 2
    h = [[sum(6*F(1, 4)*w for s, w, W in terms if s <= box and i in s and j in s)
          for j in range(n)] for i in range(n)]
    for i in range(n):
        require(sum(a**abs(i-j)*h[i][j] for j in range(n)) <= 3*R, 'Hessian weighted row')
        require(sum(a**abs(i-j)*h[j][i] for j in range(n)) <= 3*R, 'Hessian weighted column')
    b = [4*sum(W for s, w, W in terms if i in s and not s <= box) if i in box else F(0)
         for i in range(n)]
    for i in box:
        hi = min(abs(i-j) for j in range(n) if j not in box)
        require(b[i] <= 2*R*F(1, 2)**hi <= 2*R*a**(-hi), 'crossing drift')
    alpha = F(1)
    require(alpha > 3*R, 'resolvent parameter')
    resolvent = invert([[alpha*(i == j)-h[i][j] for j in range(n)] for i in range(n)])
    require(all(x >= 0 for row in resolvent for x in row), 'positive gradient resolvent')
    for i in range(n):
        require(sum(a**abs(i-j)*resolvent[i][j] for j in range(n)) <= 1/(alpha-3*R), 'weighted resolvent row')
    require(sum(b[i]*resolvent[i][K] for i in range(n)) <= 2*R/(alpha-3*R)*a**(-hK), 'graph-range boundary majorant')
    power = [[F(i == j) for j in range(n)] for i in range(n)]
    for order in range(9):
        for i in range(n):
            require(sum(a**abs(i-j)*power[i][j] for j in range(n)) <= (3*R)**order, 'exponential coefficient majorant')
        require(sum(b[i]*power[i][K] for i in range(n)) <= 2*R*(3*R)**order*a**(-hK), 'Duhamel coefficient majorant')
        power = matmul(power, h)

    schur = []
    for N in [1, 2, 4, 8, 16, 64, 256]:
        matrix = [[F(1), F(-N)], [F(-N), F(2*N*N)]]
        require(det(matrix) == N*N and matrix[0][0] > 0, 'positive hidden-mode source')
        core = [F(1), F(0)]
        recovery = [F(1), F(1, 2*N)]
        require(dot(core, matvec(matrix, core)) == 1, 'same core energy')
        require(dot(recovery, matvec(matrix, recovery)) == F(1, 2), 'hidden relaxation energy')
        observed = invert([[matrix[i][j]+F(i == j) for j in range(2)] for i in range(2)])[0][0]
        require(F(2, 3)-observed == F(1, 3*(2+3*N*N)), 'actual Schur resolvent limit')
        require(observed-F(1, 2) == F(N*N, 2*(2+3*N*N)), 'wrong candidate resolvent defect')
        schur.append({'N': N, 'core_energy': '1', 'recovery_energy': '1/2',
                      'observed_resolvent': str(observed), 'core_graph_residual_squared': str(N*N)})
    require(F(2, 3)-F(1, 2) == F(1, 6), 'limiting resolvent hostile')
    norm_defect = F(4, 6)-F(1, 3)
    require(norm_defect == F(1, 3), 'vacuum coordinate nonisometry hostile')
    require(3*F(9, 64) < 1, 'alpha=kappa admissible throughout source window')
    inputs = [CONTRACT, NOTE, SELF, BASE+'contracts/yang-mills-gap-net.v1.json']
    for name in ['thermodynamic-form', 'thermodynamic-vacuum', 'uniform-detection']:
        inputs += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                   BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                   BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-propagator-comparison.result.v1', 'passed': True,
            'strength': 'written source-propagator and operator-core comparison with exact finite regressions',
            'weighted_support_cases': support_cases, 'spin_activity_cases': spin_cases,
            'gradient_matrix_size': n, 'positive_power_orders': 9,
            'exact_fixture_R': str(R), 'Schur_hostile': schur,
            'limiting_wrong_resolvent_defect': '1/6', 'vacuum_norm_defect': str(norm_defect),
            'upstream_receipt_fresh': True, 'independent_analytic_review': False,
            'multi_time_source_packets': False, 'continuum_Yang_Mills': False,
            'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'passed': result['passed'], 'weighted_support_cases': result['weighted_support_cases'],
                      'spin_activity_cases': result['spin_activity_cases'],
                      'positive_power_orders': result['positive_power_orders'],
                      'hostile_residuals': ['1/6', '1/3'], 'receipt': str(OUT.relative_to(ROOT))}, indent=2))
