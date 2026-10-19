"""Exact clustering mechanism controls; not a spatial SU2 propagation computation."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_multi_time_state import report as predecessor_report
from check_yang_mills_thermodynamic_form import matmul, matvec, dot, det, transpose
from check_yang_mills_thermodynamic_vacuum import invert

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-source-clustering.v1.json'
NOTE = BASE+'yang-mills-source-clustering-v1.md'
SELF = BASE+'checkers/check_yang_mills_source_clustering.py'
OUT = ROOT/(BASE+'results/yang-mills-source-clustering-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def psd(a):
    count = 0
    for n in range(1, len(a)+1):
        for ix in combinations(range(len(a)), n):
            require(det([[a[i][j] for j in ix] for i in ix]) >= 0, 'PSD principal minor')
            count += 1
    return count


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 4 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'root promotion')
    require(c['subnet']['ready_frontier'] == ['nonzero-gauge-connected-correlator'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum root')
    prior = predecessor_report()
    require(prior['passed'] and prior == json.loads((ROOT/(BASE+'results/yang-mills-multi-time-state-v1.json')).read_text()), 'predecessor stale')
    a = F(4, 3)
    states = list(product([-1, 1], repeat=2))
    law = {s: F(9 if s[0] == s[1] else 8, 34) for s in states}
    covariance = sum(s[0]*s[1]*w for s, w in law.items())
    require(covariance == F(1, 17), 'weak Gibbs covariance')
    influence = F(1, 17)
    alpha = a*influence
    require(alpha < F(1, 8), 'spatial influence regime')
    D = invert([[F(1), -influence], [-influence, F(1)]])
    require(covariance <= D[0][1], 'oscillation covariance comparison')
    require(covariance <= alpha/(1-alpha)/a, 'disjoint weighted covariance bound')
    for q in [F(9, 17), F(8, 17)]:
        require(2*q*(1-q) <= F(1, 2), 'conditional tilt derivative bound')
    for i in range(2):
        require(sum(a**abs(i-j)*D[i][j] for j in range(2)) <= 1/(1-alpha), 'weighted D')
        require(sum(a**abs(i-j)*(D[i][j]-F(i == j)) for j in range(2)) <= alpha/(1-alpha), 'weighted D-I')

    # Damped-gradient resolvent analogue with connected finite geometry.
    n = 5
    R = F(9, 128)
    curvature = F(1, 2)-3*R
    h = [[F(1, 128) if abs(i-j) <= 1 else F(0) for j in range(n)] for i in range(n)]
    for i in range(n):
        require(sum(a**abs(i-j)*h[i][j] for j in range(n)) <= 3*R, 'weighted Hessian')
    L = [[F(1, 2)*(i == j)-h[i][j] for j in range(n)] for i in range(n)]
    killed_resolvent = invert(L)
    step = invert([[F(i == j)+L[i][j] for j in range(n)] for i in range(n)])
    ratio = 1/(1+curvature)
    gradient_orders = 0
    for order in range(9):
        require(all(x >= 0 for row in killed_resolvent for x in row), 'positive gradient kernel')
        for i in range(n):
            require(sum(a**abs(i-j)*killed_resolvent[i][j] for j in range(n)) <= ratio**order/curvature, 'damped spatial row')
        require(killed_resolvent[0][4] <= a**(-4)*ratio**order/curvature, 'mixed spatial/resolvent bound')
        killed_resolvent = matmul(killed_resolvent, step)
        gradient_orders += 1
    require(F(1, 2)-3*F(9, 64) == F(5, 64), 'source curvature endpoint')

    p = [F(1, 6), F(4, 6), F(1, 6)]
    A = [[F(2), F(-2), F(0)], [F(-1, 2), F(1), F(-1, 2)], [F(0), F(-2), F(2)]]
    Q = invert([[A[i][j]+F(i == j) for j in range(3)] for i in range(3)])
    variance = [[p[i]*(i == j)-p[i]*p[j] for j in range(3)] for i in range(3)]
    power = [[F(i == j) for j in range(3)] for i in range(3)]
    rho = F(1, 3)
    f, g, h0, k = [list(map(F, x)) for x in [[-1, 0, 2], [2, -1, 1], [1, 3, -1], [-2, 1, 0]]]
    u = [x*y for x, y in zip(g, matvec(Q, f))]
    v = [x*y for x, y in zip(h0, matvec(Q, k))]
    var_F = dot(p, [x*x*y for x, y in zip(g, matvec(Q, [z*z for z in f]))])-dot(p, u)**2
    var_G = dot(p, [x*x*y for x, y in zip(h0, matvec(Q, [z*z for z in k]))])-dot(p, v)**2
    require(var_F > 0 and var_G > 0, 'nonlinear block norms')
    contraction_minors = 0
    for order in range(9):
        pulled = matmul(matmul(transpose(power), variance), power)
        residual = [[rho**(2*order)*variance[i][j]-pulled[i][j] for j in range(3)] for i in range(3)]
        contraction_minors += psd(residual)
        cov_blocks = dot(p, [x*y for x, y in zip(u, matvec(power, v))])-dot(p, u)*dot(p, v)
        require(cov_blocks**2 <= rho**(2*order)*var_F*var_G, 'separated nonlinear blocks')
        power = matmul(power, Q)

    # Fixed spectral gap with arbitrarily nonlocal static correlation.
    reset_p = [F(9 if x == y else 1, 20) for x, y in states]
    projection = [reset_p[:] for _ in states]
    reset_A = [[F(i == j)-projection[i][j] for j in range(4)] for i in range(4)]
    require([[reset_p[i]*reset_A[i][j] for j in range(4)] for i in range(4)] ==
            transpose([[reset_p[i]*reset_A[i][j] for j in range(4)] for i in range(4)]), 'weighted reset self-adjointness')
    require(matmul(reset_A, reset_A) == reset_A, 'reset spectrum 0/1')
    require(sum(reset_A[i][i] for i in range(4)) == 3, 'unique reset vacuum')
    remote_cov = sum(x*y*w for (x, y), w in zip(states, reset_p))
    require(remote_cov == F(4, 5), 'remote correlation fixed')
    for distance in [4, 8, 16, 32, 64]:
        require(remote_cov > a**(-distance), 'gap alone does not force spatial decay')

    # One fast reader misses a slow source sector.
    blind = []
    for N in [4, 8, 16, 64]:
        slow = 1-F(1, N)
        fast_Q = [[(1+rho)/2, (1-rho)/2], [(1-rho)/2, (1+rho)/2]]
        slow_Q = [[(1+slow)/2, (1-slow)/2], [(1-slow)/2, (1+slow)/2]]
        tensor = [[fast_Q[i//2][j//2]*slow_Q[i%2][j%2] for j in range(4)] for i in range(4)]
        fast_reader = list(map(F, [-1, -1, 1, 1]))
        slow_reader = list(map(F, [-1, 1, -1, 1]))
        require(matvec(tensor, fast_reader) == [rho*x for x in fast_reader], 'fast reader fixed')
        require(matvec(tensor, slow_reader) == [slow*x for x in slow_reader], 'hidden slow reader')
        require(slow > rho, 'whole contraction inferred from fast reader fails')
        blind.append({'N': N, 'fast_ratio': str(rho), 'hidden_ratio': str(slow)})
    inputs = [CONTRACT, NOTE, SELF, BASE+'contracts/yang-mills-gap-net.v1.json']
    for name in ['multi-time-state', 'propagator-comparison', 'thermodynamic-vacuum']:
        inputs += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                   BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                   BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-source-clustering.result.v1', 'passed': True,
            'strength': 'written source clustering bounds with exact finite Gibbs/matrix/chain controls',
            'binary_covariance': str(covariance), 'gradient_resolvent_orders': gradient_orders,
            'whole_contraction_PSD_minors': contraction_minors, 'nonlinear_block_separations': 9,
            'nonlocal_reset_covariance': str(remote_cov), 'blind_reader_hostile': blind,
            'upstream_receipt_fresh': True, 'independent_analytic_review': False,
            'nonzero_SU2_connected_correlator_constructed': False, 'continuum_Yang_Mills': False,
            'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'binary_covariance', 'gradient_resolvent_orders',
                     'whole_contraction_PSD_minors', 'nonlinear_block_separations', 'nonlocal_reset_covariance']}, indent=2))
