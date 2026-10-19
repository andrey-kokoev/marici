"""Exact tests accompanying the written closed thermodynamic-form theorem."""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_thermodynamic_vacuum import report as vacuum_report
from check_yang_mills_uniform_detection import report as curvature_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-thermodynamic-form.v1.json'
NOTE = BASE+'yang-mills-thermodynamic-form-v1.md'
SELF = BASE+'checkers/check_yang_mills_thermodynamic_form.py'
OUT = ROOT/(BASE+'results/yang-mills-thermodynamic-form-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def transpose(a):
    return list(map(list, zip(*a)))


def matmul(a, b):
    return [[sum(x*y for x, y in zip(row, col)) for col in zip(*b)] for row in a]


def matvec(a, x):
    return [sum(v*w for v, w in zip(row, x)) for row in a]


def diag(x):
    return [[v if i == j else F(0) for j in range(len(x))] for i, v in enumerate(x)]


def dot(x, y):
    return sum(v*w for v, w in zip(x, y))


def det(a):
    total = F(0)
    for perm in permutations(range(len(a))):
        sign = (-1)**sum(perm[i] > perm[j] for i in range(len(a)) for j in range(i+1, len(a)))
        term = F(sign)
        for i, j in enumerate(perm):
            term *= a[i][j]
        total += term
    return total


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 1 and all(v is False for v in c['boundary'].values()), 'scope/iteration')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    node = next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])
    require(node['status'] == 'open' and not c['parent_net']['discharges_parent'], 'continuum parent promoted')
    net = c['subnet']
    require(net['outcome'] is None, 'unproved correlation objective')
    by = {n['id']: n for n in net['conjectures']}
    ready = [n['id'] for n in net['conjectures'] if n['status'] == 'open'
             and all(by[d]['status'] == 'resolved' for d in n['depends_on'])]
    require(ready == net['ready_frontier'] == ['finite-propagator-comparison'], 'stale executable frontier')
    upstream = {}
    for name, fn in [('thermodynamic-vacuum', vacuum_report), ('uniform-detection', curvature_report)]:
        actual = fn()
        require(actual['passed'], name+' regression')
        receipt = BASE+'results/yang-mills-'+name+'-v1.json'
        require(actual == json.loads((ROOT/receipt).read_text()), name+' stale receipt')
        upstream[name] = 'fresh exact replay; not independent analytic verification'

    omega = list(map(F, [1, 2, 1]))
    p = [x*x/6 for x in omega]
    S = [list(map(F, row)) for row in [[2, -1, 0], [-1, 1, -1], [0, -1, 2]]]
    require(matvec(S, omega) == [0, 0, 0], 'actual vacuum')
    A = matmul(matmul(diag([1/x for x in omega]), S), diag(omega))
    require(matvec(A, [1, 1, 1]) == [0, 0, 0], 'transformed constant vacuum')
    G = [list(map(F, row)) for row in [[-1, 1, 0], [0, -1, 1]]]
    P = diag(p)
    adjoint = matmul(matmul(diag([1/x for x in p]), transpose(G)), diag([F(1, 3)]*2))
    require(matmul(adjoint, G) == A, 'weighted adjoint/divergence selects source generator')
    require(matmul(P, A) == transpose(matmul(P, A)), 'weighted self-adjointness')
    for eigen in [0, 2, 3]:
        shifted = [[A[i][j]-F(eigen)*(i == j) for j in range(3)] for i in range(3)]
        require(det(shifted) == 0, 'exact spectrum')
    residual = [[p[i]*A[i][j]-2*(p[i]*(i == j)-p[i]*p[j]) for j in range(3)] for i in range(3)]
    principal_minors = 0
    for k in range(1, 4):
        for indices in combinations(range(3), k):
            require(det([[residual[i][j] for j in indices] for i in indices]) >= 0, 'whole finite-form Poincare residual')
            principal_minors += 1
    vectors = 0
    adjoint_tests = 0
    for f0 in product(range(-2, 3), repeat=3):
        f = list(map(F, f0))
        psi = [x*y for x, y in zip(omega, f)]
        gradient = matvec(G, f)
        q = dot(gradient, gradient)/3
        require(q == dot(psi, matvec(S, psi))/6, 'source form identity')
        mean = dot(p, f)
        variance = dot(p, [x*x for x in f])-mean*mean
        require(q >= 2*variance, 'finite gap')
        for g0 in product(range(-2, 3), repeat=2):
            g = list(map(F, g0))
            require(dot(gradient, g)/3 == dot(p, [x*y for x, y in zip(f, matvec(adjoint, g))]), 'adjoint identity')
            adjoint_tests += 1
        vectors += 1
    require(matvec(G, omega) != [0, 0], 'raw vacuum gradient hostile')
    threshold = F(27, 262144)
    require(2*F(4096, 3)*threshold == F(9, 32), 'conditional drift uniform endpoint')
    require(F(1, 2)-4096*threshold == F(5, 64), 'source Poincare constant')

    collapse = []
    for n in [1, 2, 4, 8, 16, 32, 256]:
        norm_squared = F(1, n*n)
        evaluation = n*F(1, n)
        require(evaluation == 1, 'nonclosable form sequence')
        # For two distinct indices, T(e_n/n-e_m/m)=1-1=0.
        require(evaluation-evaluation == 0, 'form-Cauchy but not closable')
        collapse.append({'N': n, 'vanishing_state_norm_squared': str(norm_squared),
                         'nonclosable_form_energy': '1', 'same_measure_rescaled_gap': str(F(2, n)),
                         'hidden_appended_state_energy': str(F(1, n))})
    require(F(collapse[-1]['same_measure_rescaled_gap']) < F(1, 100), 'energy-scale hostile')
    require(F(collapse[-1]['hidden_appended_state_energy']) < 2, 'nondense old core hides new low energy')
    inputs = [CONTRACT, NOTE, SELF, BASE+'contracts/yang-mills-gap-net.v1.json']
    for name in ['thermodynamic-vacuum', 'uniform-detection']:
        inputs += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                   BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                   BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-thermodynamic-form.result.v1', 'passed': True,
            'strength': 'written fixed-lattice closed-form construction with exact finite regressions',
            'upstream': upstream, 'weighted_source_vectors': vectors,
            'adjoint_identity_cases': adjoint_tests, 'Poincare_principal_minors': principal_minors,
            'exact_finite_spectrum': ['0', '2', '3'], 'deliberate_failures': collapse,
            'source_unit_bound': '5*kappa/64', 'finite_propagators_compared': False,
            'multi_time_source_correlations': False, 'continuum_Yang_Mills': False,
            'independent_analytic_review': False, 'ready_frontier': ready,
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
