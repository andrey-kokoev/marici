"""Mesh-uniform finite-word controls; not an infinite-product constructor."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_buffered_memory import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-mesh-word.v1.json'
NOTE = BASE+'yang-mills-mesh-word-v1.md'
SELF = BASE+'checkers/check_yang_mills_mesh_word.py'
OUT = ROOT/(BASE+'results/yang-mills-mesh-word-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def word_prefactor(R):
    R = F(R)
    if not 0 <= R < F(9, 64):
        raise ValueError('outside admitted source window')
    alpha, c = 8*R/9, F(1, 2)-3*R
    eta = R/2+alpha/(1-alpha)
    return max(2*R/c, F(44, 7)*eta)


def plan_word_buffer(R, B, epsilon):
    B, epsilon = F(B), F(epsilon)
    if B < 0 or epsilon <= 0:
        raise ValueError('nonnegative total gradient budget and positive tolerance required')
    coefficient = F(18, 5) if R is None else word_prefactor(R)
    amplitude, b = coefficient*B, 0
    while amplitude > epsilon:
        b += 1
        amplitude *= F(3, 4)
    return {'buffer': b, 'coefficient': coefficient, 'error_bound': amplitude}


def discounts(M, q):
    G = [F(0)]*len(M)
    G[-1] = M[-1]
    for j in range(len(M)-2, -1, -1):
        G[j] = M[j]+q[j]*G[j+1]
    propagation = sum((1-q[j])*G[j+1] for j in range(len(q)))
    return G, propagation


def inverse(a):
    n = len(a)
    aug = [list(row)+[F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        scale = aug[j][j]
        aug[j] = [x/scale for x in aug[j]]
        for i in range(n):
            if i != j:
                scale = aug[i][j]
                aug[i] = [x-scale*y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def expectation(law, f):
    return sum(w*x for w, x in zip(law, f))


def reset(q, law, f):
    mean = expectation(law, f)
    return [q*x+(1-q)*mean for x in f]


def nested(fs, qs, law):
    u = fs[-1]
    for j in range(len(fs)-2, -1, -1):
        u = [f*x for f, x in zip(fs[j], reset(qs[j], law, u))]
    return u


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 1 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'strength')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['bounded-probe-product-limit'], 'frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-buffered-memory-v1.json')).read_text()), 'predecessor stale')
    gradient_cases = 0
    for n, base, pattern in product([1, 2, 3, 8, 31, 128], [F(1), F(3, 4), F(1, 2)], range(3)):
        M = [F(j+1, n*(n+1)//2) for j in range(n)]
        q = [base**(1 if pattern == 0 else (j % 3 if pattern == 1 else (0 if j % 2 == 0 else 5))) for j in range(n-1)]
        G, propagation = discounts(M, q)
        weight, direct = F(1), F(0)
        for j in range(n):
            direct += weight*M[j]
            if j < n-1:
                weight *= q[j]
        require(sum(M) == 1 and G[0] == direct and propagation+G[0] == 1, 'gradient-source telescope, including repeated parameters')
        for dyn, state in [(F(0), F(0)), (F(2, 5), F(1, 7)), (F(1, 4), F(3, 4))]:
            require(dyn*propagation+state*G[0] <= max(dyn, state), 'convex rather than count-dependent error budget')
        gradient_cases += 1
    require(gradient_cases == 54, 'frozen gradient grids')
    a = F(4, 3)
    for coupling in [F(0), F(1, 256), F(1, 128), F(1, 64)]:
        C = [[F(0), coupling, F(0)], [coupling, F(0), coupling], [F(0), coupling, F(0)]]
        R, alpha = 3*coupling, F(8, 3)*coupling
        require(alpha == 8*R/9 and max(sum(a**abs(i-j)*C[i][j] for j in range(3)) for i in range(3)) == alpha, 'weighted influence majorant')
        D = inverse([[F(i == j)-C[i][j] for j in range(3)] for i in range(3)])
        h, xi = [2, 1, 0], [R/8, R/4, F(1)]
        y = [sum(D[i][j]*xi[j] for j in range(3)) for i in range(3)]
        eta = R/2+alpha/(1-alpha)
        for i in range(3):
            require(a**h[i]*y[i] <= 1/(1-alpha), 'global resolvent comparison')
            if i < 2:
                require(a**h[i]*y[i] <= eta, 'R-sensitive interior state comparison')
    require(F(9, 128)+F(1, 7) == F(191, 896), 'eta endpoint')
    require(F(44, 7)*F(191, 896) == F(2101, 1568) < F(18, 5), 'universal state coefficient')
    planner_cases = 0
    for R, B, epsilon in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(0), F(1), F(5)], [F(1, 10), F(1, 1000)]):
        plan = plan_word_buffer(R, B, epsilon)
        require(plan['error_bound'] <= epsilon and word_prefactor(R) < F(18, 5), 'word tolerance')
        if plan['buffer']:
            require(plan['error_bound']*F(4, 3) > epsilon, 'minimal rational sufficient buffer')
        planner_cases += 1
    require(planner_cases == 24, 'frozen word planners')
    universal = plan_word_buffer(None, 1, F(1, 1000))
    interior = plan_word_buffer(F(9, 128), 1, F(1, 1000))
    require([universal['buffer'], interior['buffer']] == list(contract['certificate']['buffer_examples_B1_epsilon_1_1000'].values()) == [29, 23], 'buffer examples')
    require(interior['coefficient'] == F(4301, 6720), 'interior rational coefficient')

    pi, rho = [F(1, 3)]*3, [F(1, 6), F(4, 6), F(1, 6)]
    tv = sum(abs(x-y) for x, y in zip(pi, rho))/2
    require(tv == F(1, 3), 'finite-law comparison coefficient')
    word_cases = 0
    for n, base, kind in product([1, 2, 3, 8, 16, 32], [F(1), F(3, 4), F(1, 2)], range(2)):
        amplitude = F(1, n+1)
        fs = [[1-amplitude*(int(i == j % 3) if kind == 0 else int(i != j % 3)) for i in range(3)] for j in range(n)]
        M = [max(f)-min(f) for f in fs]
        q = [base**(j % 3) for j in range(n-1)]
        G, propagation = discounts(M, q)
        up, uq = nested(fs, q, pi), nested(fs, q, rho)
        require(max(abs(x-y) for x, y in zip(up, uq)) <= tv*propagation, 'actual nested propagation error')
        require(abs(expectation(pi, uq)-expectation(rho, uq)) <= tv*G[0], 'distinct-state error retained')
        require(abs(expectation(pi, up)-expectation(rho, uq)) <= tv*sum(M) <= tv, 'mesh-uniform finite-law word error')
        word_cases += 1
    require(word_cases == 36, 'frozen word fixtures')
    one = [F(1), F(0), F(1)]
    state_hostile = abs(expectation(pi, one)-expectation(rho, one))
    require(state_hostile == F(1, 3), 'zero intervals do not imply zero state discrepancy')
    for n in [1, 2, 7, 32, 129]:
        require(abs((-1)**n-(-1)**(n+1)) == 2, 'zero-gradient finite-word comparison does not create infinite product')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['buffered-memory', 'thermodynamic-vacuum', 'source-clustering', 'multi-time-state']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-mesh-word.result.v1', 'passed': True,
            'strength': 'written actual finite-word comparison uniform in count/mesh/horizon at fixed total gradient budget; independently unreviewed',
            'discounted_gradient_grids': gradient_cases, 'state_resolvent_fixtures': 4,
            'rational_word_plans': planner_cases, 'finite_law_word_cases': word_cases,
            'universal_coefficient': '18/5', 'buffer_B1_epsilon_1_1000': [universal['buffer'], interior['buffer']],
            'state_identification_hostile_residual': str(state_hostile), 'infinite_word_hostile_residual': '2',
            'iterated_projected_words_proved': False, 'infinite_product_constructed': False,
            'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'discounted_gradient_grids', 'state_resolvent_fixtures',
                     'rational_word_plans', 'finite_law_word_cases', 'universal_coefficient',
                     'state_identification_hostile_residual', 'infinite_word_hostile_residual']}, indent=2))
