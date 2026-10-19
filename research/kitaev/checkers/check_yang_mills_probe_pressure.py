"""Exact isolated-spectral/readout controls; not SU2 spectral evaluations."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_probe_susceptibility import report as predecessor_report, heatbath, mean
from check_yang_mills_probe_clustering import mm, mv, eye, diagonal
from check_yang_mills_mesh_word import inverse, word_prefactor

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-pressure.v1.json'
NOTE = BASE+'yang-mills-probe-pressure-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_pressure.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-pressure-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def scale(a, q):
    return [[q*x for x in row] for row in a]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def sub(a, b):
    return add(a, scale(b, -1))


def working_bound(R, kappa):
    kappa = F(kappa)
    if kappa <= 0:
        raise ValueError('positive source kappa required')
    if R is None:
        return kappa*F(5, 512), F(18, 5)
    R = F(R)
    if not 0 <= R < F(9, 64):
        raise ValueError('outside source coupling window')
    return kappa*(F(1, 2)-3*R)/8, word_prefactor(R)


def plan_pressure_buffer(R, kappa, delta, gradient, epsilon):
    delta, gradient, epsilon = map(F, [delta, gradient, epsilon])
    ceiling, coefficient = working_bound(R, kappa)
    if delta < 0 or delta > ceiling or gradient < 0 or epsilon <= 0:
        raise ValueError('working norm ball and nonnegative gradient/positive tolerance required')
    if delta == 0 or coefficient*gradient == 0:
        return {'n': 0, 'buffer': 0, 'parameter': None, 'error_bound': F(0)}
    n = 1
    while delta/n+coefficient*gradient*F(3, 4)**(2*n) > epsilon:
        n += 1
    return {'n': n, 'buffer': 3*n, 'parameter': F(n)/(8*delta),
            'error_bound': delta/n+coefficient*gradient*F(3, 4)**(2*n)}


def spectral_packet(m, q, shift):
    d = 2*q/(1-q*q)
    root = (1+q*q)/(1-q*q)
    require(root*root == 1+d*d, 'rational discriminant')
    U = [m*(shift+d/2), m*(shift-d/2)]
    delta = max(abs(x) for x in U)
    H = add(scale([[F(1), F(-1)], [F(-1), F(1)]], m/2), diagonal(U))
    E, upper = m*(1+2*shift-root)/2, m*(1+2*shift+root)/2
    projection = scale(sub(scale(eye(2), upper), H), 1/(upper-E))
    require(delta <= m/8 and abs(E) <= delta and upper >= m-delta, 'actual small multiplication spectral ball')
    require(mm(projection, projection) == projection and sum(projection[i][i] for i in range(2)) == 1, 'rank-one spectral projection')
    require(mm(H, projection) == scale(projection, E) and all(x >= 0 for row in projection for x in row), 'ground-state eigenvalue and positive packet')
    overlap = sum(mv(projection, [F(1)]*2))/2
    require(overlap == 1/(1+q*q) and overlap >= F(8, 9) and upper-E >= 3*m/4, 'original uniform-state overlap and relative gap')
    for discount in [F(0), F(1, 4), F(1, 2), F(1)]:
        relative_readout = overlap+(1-overlap)*discount
        require(overlap <= relative_readout <= 1, 'positive relative spectral packet')
    require((1-overlap)/overlap <= F(1, 8), 'rational majorant for negative log overlap')
    return E, overlap, projection


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 5 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-eigenstate-transport'], 'next constructor')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-susceptibility-v1.json')).read_text()), 'fresh predecessor receipt')

    contour_cases = 0
    for m, fraction in product([F(1, 2), F(1), F(2)], [F(0), F(1, 32), F(1, 16), F(1, 8)]):
        delta = m*fraction
        rho = 2*delta/(m-2*delta)
        require(2*delta/m <= F(1, 4) and rho <= F(1, 3), 'Neumann contour budget')
        overlap = 1-rho*rho
        require(overlap >= F(8, 9) and (1-overlap)/overlap <= F(1, 8), 'uniform overlap and logarithmic bound')
        require(m-2*delta >= 3*m/4, 'uniform relative spectral gap')
        contour_cases += 1
    spectral_cases = 0
    for m, q, shift in product([F(1, 2), F(1), F(2)], [F(0), F(1, 32), F(1, 16), F(1, 10)], [F(-1, 64), F(0), F(1, 64)]):
        spectral_packet(m, q, shift)
        spectral_cases += 1
    plus = spectral_packet(F(1), F(1, 16), F(0))
    minus = spectral_packet(F(1), F(-1, 16), F(0))
    state_residual = abs(plus[2][0][0]-minus[2][0][0])
    require(plus[:2] == minus[:2] and state_residual == F(32, 257), 'identical energies and weights do not identify local states')

    jet_cases = 0
    weak_mixed = None
    for a, b in [(1, 1), (9, 8), (5, 4), (3, 2)]:
        law, g, v, w = heatbath(a, b)
        A = scale(g, -1)
        K = inverse([[A[i][j]+law[j] for j in range(4)] for i in range(4)])
        for vv, ww in [(v, w), ([x+1 for x in v], [x+2 for x in w]), ([F(1)]*4, w)]:
            ez, ew = mean(law, vv), mean(law, ww)
            vz, wz = [x-ez for x in vv], [x-ew for x in ww]
            psi_z, psi_w = [-x for x in mv(K, vz)], [-x for x in mv(K, wz)]
            e_zw = mean(law, [vv[i]*psi_w[i]+ww[i]*psi_z[i] for i in range(4)])
            rhs = [e_zw+ez*psi_w[i]+ew*psi_z[i]-vv[i]*psi_w[i]-ww[i]*psi_z[i] for i in range(4)]
            require(mean(law, rhs) == 0 and mean(law, psi_z) == mean(law, psi_w) == 0, 'analytic original-state eigenvector normalization')
            psi_zw = mv(K, rhs)
            require(mv(A, psi_zw) == rhs and mean(law, psi_zw) == 0, 'mixed eigenvalue equation at zero')
            density = 2*mean(law, [vz[i]*x for i, x in enumerate(mv(K, wz))])
            require(e_zw == -density, 'spectral pressure curvature equals negative source response density')
            if vv == v and ww == w and (a, b) == (9, 8):
                weak_mixed = e_zw
                require(weak_mixed == F(-17, 288), 'weak-pair pressure curvature')
            jet_cases += 1

    for n in range(1, 7):
        weight = F(1, 4)**n
        require(0 < weight < F(8, 9), 'vanishing overlap violates source small-probe gate')
        for discount in [F(0), F(1, 4), F(1, 2), F(1)]:
            actual = weight+(1-weight)*discount
            require(abs(actual-discount) == weight*(1-discount) <= weight, 'uniform absolute readout convergence without rate convergence')
    planner_cases = 0
    for R, kappa, ratio, gradient, epsilon in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(1, 16), F(1, 8)], [F(0), F(1)], [F(1, 100), F(1, 1000)]):
        delta = kappa*(F(1, 2)-3*R)*ratio
        plan = plan_pressure_buffer(R, kappa, delta, gradient, epsilon)
        require(plan['error_bound'] <= epsilon, 'spatial pressure tolerance')
        if plan['n']:
            n = plan['n']
            require(plan['buffer'] == 3*n and 2*delta*plan['parameter'] == F(n, 4), 'typed diagonal source/spatial budget')
            if n > 1:
                require(delta/(n-1)+word_prefactor(R)*gradient*F(3, 4)**(2*(n-1)) > epsilon, 'least sufficient diagonal n')
        else:
            require(R*gradient == 0 and plan['error_bound'] == 0, 'exact zero cross-source term')
        planner_cases += 1
    examples = [plan_pressure_buffer(R, 1, F(1, 128), 1, F(1, 1000))['buffer'] for R in [None, F(9, 128)]]
    require((contour_cases, spectral_cases, jet_cases, planner_cases) == (12, 36, 12, 96), 'frozen control counts')
    require(examples == [48, 39] == list(contract['transport']['buffer_kappa1_delta_1_128_M1_epsilon_1_1000'].values()), 'worked pressure buffers')
    require(plan_pressure_buffer(F(1, 128), 1, 0, 1, F(1, 1000))['error_bound'] == 0, 'zero probe')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-susceptibility', 'probe-limit', 'mesh-word', 'source-clustering']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-pressure.result.v1', 'passed': True,
            'strength': 'written small-probe spectral/readout completion and changing-state pressure transport; independently unreviewed source analysis',
            'contour_budget_cases': contour_cases, 'exact_spectral_cases': spectral_cases,
            'mixed_eigenvalue_jets': jet_cases, 'pressure_budget_cases': planner_cases,
            'projection_distance_bound': '1/3', 'original_state_overlap_lower': '8/9',
            'weak_pair_mixed_pressure_curvature': str(weak_mixed),
            'vanishing_overlap_rate_hostile_residual': '1', 'equal_scalar_eigenstate_hostile_residual': str(state_residual),
            'buffers_kappa1_delta_1_128_M1_epsilon_1_1000': examples,
            'tilted_state_transport_proved': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'contour_budget_cases', 'exact_spectral_cases',
                     'mixed_eigenvalue_jets', 'pressure_budget_cases', 'weak_pair_mixed_pressure_curvature',
                     'vanishing_overlap_rate_hostile_residual', 'equal_scalar_eigenstate_hostile_residual']}, indent=2))
