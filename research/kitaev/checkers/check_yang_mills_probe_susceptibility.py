"""Exact amplitude jets and positive off-diagonal gain controls, not SU2 evaluations."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_probe_clustering import report as predecessor_report, mm, mv, eye, diagonal
from check_yang_mills_mesh_word import inverse

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-susceptibility.v1.json'
NOTE = BASE+'yang-mills-probe-susceptibility-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_susceptibility.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-susceptibility-v1.json')
DEGREE = 8


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def scale(a, q):
    return [[q*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return add(a, scale(b, -1))


def mean(law, vector):
    return sum(x*y for x, y in zip(law, vector))


def gains(R, kappa):
    R, kappa = F(R), F(kappa)
    if not 0 <= R < F(9, 64) or kappa <= 0:
        raise ValueError('admitted source coupling and positive kappa required')
    c = F(1, 2)-3*R
    return (1/c-2, 2*(1/c**2-4)/kappa, 2*(1/c**3-8)/kappa**2)


def plan_susceptibility(R, kappa, T, gradient_product, epsilon):
    kappa, T, gradient_product, epsilon = map(F, [kappa, T, gradient_product, epsilon])
    if kappa <= 0 or T < 0 or gradient_product < 0 or epsilon <= 0:
        raise ValueError('positive kappa/tolerance; nonnegative horizon/gradient product')
    short, density = ((F(54, 5), F(7992, 25)/kappa) if R is None else gains(R, kappa)[:2])
    coefficient = min(T*T*short, T*density)
    distance, error = 1, coefficient*gradient_product*F(3, 4)
    while error > epsilon:
        distance += 1
        error *= F(3, 4)
    return {'separation': distance, 'error_bound': error, 'coefficient': coefficient}


def heatbath(a, b):
    weights = [[F(a), F(b)], [F(b), F(a)]]
    states = list(product(range(2), repeat=2))
    law = [weights[x][y]/(2*(a+b)) for x, y in states]
    g = []
    for i, (x, y) in enumerate(states):
        row = []
        for j, (xx, yy) in enumerate(states):
            value = F(0)
            if yy == y:
                value += weights[xx][y]/sum(weights[k][y] for k in range(2))
            if xx == x:
                value += weights[x][yy]/sum(weights[x])
            row.append(value-2*F(i == j))
        g.append(row)
    return law, g, [F(x) for x, y in states], [F(y) for x, y in states]


def amplitude_jet(law, g, v, w):
    keys = list(product(range(2), repeat=2))
    zero = scale(g, 0)
    powers = {key: (eye(4) if key == (0, 0) else zero) for key in keys}
    zv = {key: [] for key in keys}
    bv, bw = scale(diagonal(v), -1), scale(diagonal(w), -1)
    for degree in range(DEGREE+1):
        for key in keys:
            zv[key].append(mean(law, mv(powers[key], [F(1)]*4))/factorial(degree))
        if degree < DEGREE:
            new = {}
            for i, j in keys:
                cell = mm(powers[(i, j)], g)
                if i:
                    cell = add(cell, mm(powers[(i-1, j)], bv))
                if j:
                    cell = add(cell, mm(powers[(i, j-1)], bw))
                new[(i, j)] = cell
            powers = new
    require(zv[(0, 0)] == [F(1)]+[F(0)]*DEGREE, 'unperturbed normalized state')
    require(zv[(1, 0)] == [F(0), -mean(law, v)]+[F(0)]*(DEGREE-1), 'first ordered derivative')
    require(zv[(0, 1)] == [F(0), -mean(law, w)]+[F(0)]*(DEGREE-1), 'second ordered derivative')
    connected = [zv[(1, 1)][n]-sum(zv[(1, 0)][k]*zv[(0, 1)][n-k] for k in range(n+1)) for n in range(DEGREE+1)]
    vc, wc = [x-mean(law, v) for x in v], [x-mean(law, w) for x in w]
    expected = [F(0), F(0)]
    image = wc
    for n in range(2, DEGREE+1):
        expected.append(2*mean(law, [x*y for x, y in zip(vc, image)])/factorial(n))
        image = mv(g, image)
    require(connected == expected, 'both orderings and connected covariance coefficient')
    return connected, zv[(1, 1)]


def weighted_norm(a):
    return max(sum(F(4, 3)**abs(i-j)*abs(x) for j, x in enumerate(row)) for i, row in enumerate(a))


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 4 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-spectral-pressure'], 'next constructor')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-clustering-v1.json')).read_text()), 'fresh predecessor receipt')
    jet_cases = density_cases = 0
    weak_density = missing_order = None
    for a, b in [(1, 1), (9, 8), (5, 4), (3, 2)]:
        law, g, v, w = heatbath(a, b)
        require(all(sum(row) == 0 for row in g), 'conservative heat-bath generator')
        require(all(law[i]*g[i][j] == law[j]*g[j][i] for i in range(4) for j in range(4)), 'actual reversible base state')
        eta = F(a-b, a+b)
        jets = []
        for vv, ww in [(v, w), ([x+1 for x in v], [x+2 for x in w]), ([F(1)]*4, w), (v, [F(2)]*4)]:
            chi, raw = amplitude_jet(law, g, vv, ww)
            jets.append(chi)
            jet_cases += 1
        require(jets[0] == jets[1] and jets[2] == jets[3] == [0]*(DEGREE+1), 'constant shifts and constant probes')
        for n in range(2, DEGREE+1):
            closed = ((1+eta)*(-(1-eta))**(n-2)-(1-eta)*(-(1+eta))**(n-2))/(4*factorial(n))
            require(jets[0][n] == closed, 'two exact heat-bath spectral modes')
        AplusJ = [[-g[i][j]+law[j] for j in range(4)] for i in range(4)]
        vc, wc = [x-mean(law, v) for x in v], [x-mean(law, w) for x in w]
        image = mv(inverse(AplusJ), wc)
        density = 2*mean(law, [x*y for x, y in zip(vc, image)])
        require(density == eta/(1-eta**2), 'centered inverse response density')
        density_cases += 1
        if eta == 0:
            require(jets[0] == [0]*(DEGREE+1) and density == 0, 'independent-coordinate zero-coupling response')
        if eta == F(1, 17):
            weak_density = density
            missing_order = jets[0][2]/2
            require(weak_density == F(17, 288) and jets[0][2] == F(1, 68) and missing_order == F(1, 136), 'missing-order hostile')
    _, raw_constant = amplitude_jet(law, g, [F(1)]*4, [F(2)]*4)
    require(raw_constant[2] == 2, 'uncentered constant-probe hostile')
    for n in [2, 4, 16, 64]:
        require(F(1, n)*(n*n)**2 == n**3, 'real absolute bound does not control mixed derivative')
    require(F(1, 16)*16**4 == 4096, 'real-bound hostile example')

    matrix_cases = 0
    for R in [F(0), F(1, 128), F(9, 128), F(575, 4096)]:
        h = [[R/2 if i == j else (R/4 if abs(i-j) == 1 else F(0)) for j in range(3)] for i in range(3)]
        require(weighted_norm(h) <= 3*R, 'inherited weighted Hessian budget')
        power = eye(3)
        for degree in range(13):
            require(weighted_norm(power) <= (3*R)**degree, 'positive matrix power moment')
            power = mm(power, h)
        U = inverse(sub(eye(3), scale(h, 2)))
        U2, U3 = mm(U, U), mm(mm(U, U), U)
        for kappa in [F(1, 2), F(1), F(2)]:
            packets = [scale(sub(U, eye(3)), 2), scale(sub(U2, eye(3)), 8/kappa), scale(sub(U3, eye(3)), 16/kappa**2)]
            for packet, gain in zip(packets, gains(R, kappa)):
                require(all(x >= 0 for row in packet for x in row) and weighted_norm(packet) <= gain, 'identity removed before positive resolvent majorant')
            matrix_cases += 1
    planner_cases = 0
    for R, kappa, T, gradient in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(2)], [F(0), F(1), F(10)], [F(0), F(1)]):
        plan = plan_susceptibility(R, kappa, T, gradient, F(1, 1000))
        require(plan['error_bound'] <= F(1, 1000) and plan['separation'] >= 1, 'bilinear susceptibility budget')
        if plan['separation'] > 1:
            require(plan['error_bound']*F(4, 3) > F(1, 1000), 'least sufficient separation')
        if R*T*gradient == 0:
            require(plan['error_bound'] == 0, 'zero coupling/horizon/gradient')
        planner_cases += 1
    examples = [plan_susceptibility(R, 1, 1, 1, F(1, 1000))['separation'] for R in [None, F(9, 128)]]
    require((jet_cases, density_cases, matrix_cases, planner_cases) == (16, 4, 12, 48), 'frozen control counts')
    require(examples == [33, 26] == list(contract['bounds']['separation_kappa1_T1_gradient_product1_epsilon_1_1000'].values()), 'worked susceptibility separations')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-clustering', 'source-clustering', 'probe-limit', 'mesh-word']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-susceptibility.result.v1', 'passed': True,
            'strength': 'written actual-source analytic mixed-response, off-diagonal spatial comparison and centered response-density completion; independently unreviewed',
            'bivariate_jet_cases': jet_cases, 'formal_parameter_degree': DEGREE, 'centered_density_cases': density_cases,
            'weighted_matrix_packets': matrix_cases, 'susceptibility_plans': planner_cases,
            'weak_pair_density': str(weak_density), 'missing_order_hostile_residual': str(missing_order),
            'uncentered_hostile_residual': '2', 'real_bound_hostile': {'real_error_bound': '1/16', 'mixed_log_derivative': '4096'},
            'separations_kappa1_T1_gradient_product1_epsilon_1_1000': examples,
            'finite_amplitude_pressure_proved': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'bivariate_jet_cases', 'formal_parameter_degree',
                     'centered_density_cases', 'weighted_matrix_packets', 'susceptibility_plans',
                     'weak_pair_density', 'missing_order_hostile_residual', 'uncentered_hostile_residual']}, indent=2))
