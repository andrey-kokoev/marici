"""Exact finite controls for the written strong bounded-probe completion."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
from hashlib import sha256
import json
from check_yang_mills_mesh_word import report as predecessor_report, plan_word_buffer

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-limit.v1.json'
NOTE = BASE+'yang-mills-probe-limit-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_limit.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-limit-v1.json')
DEGREE = 6


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def zero():
    return [[F(0) for _ in range(3)] for _ in range(3)]


def identity():
    return [[F(i == j) for j in range(3)] for i in range(3)]


def add(a, b):
    return [[x+y for x, y in zip(r, s)] for r, s in zip(a, b)]


def scale(a, scalar):
    return [[scalar*x for x in row] for row in a]


def sub(a, b):
    return add(a, scale(b, -1))


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def norm(a):
    return max(sum(abs(x) for x in row) for row in a)


def exp_series(a, step=F(1)):
    coefficients = [identity()]
    for k in range(1, DEGREE+1):
        coefficients.append(scale(mm(coefficients[-1], a), step/k))
    return coefficients


def poly_mul(a, b):
    coefficients = []
    for k in range(DEGREE+1):
        cell = zero()
        for j in range(k+1):
            cell = add(cell, mm(a[j], b[k-j]))
        coefficients.append(cell)
    return coefficients


def split_series(g, b, step):
    return poly_mul(exp_series(g, step), exp_series(scale(b, -1), step))


def partition_series(g, b, widths):
    current = [identity()]+[zero() for _ in range(DEGREE)]
    for width in widths:
        current = poly_mul(current, split_series(g, b, width))
    return current


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 2 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'strength guard')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['separated-probe-factorization'], 'successor scope')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent remains open')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-mesh-word-v1.json')).read_text()), 'fresh predecessor receipt')
    g = [[F(1, 3)-F(i == j) for j in range(3)] for i in range(3)]
    b = [[F(i if i == j else 0) for j in range(3)] for i in range(3)]
    require(all(sum(row) == 0 for row in g) and all(g[i][j] >= 0 for i in range(3) for j in range(3) if i != j), 'reset Markov generator')
    require(g == [list(row) for row in zip(*g)] and all(b[i][i] >= 0 for i in range(3)), 'reversibility and nonnegative probe')
    commutator = sub(mm(g, b), mm(b, g))
    require(norm(commutator) == 1, 'noncommuting mixed source cell')
    step = split_series(g, b, F(1))
    doubled = split_series(g, b, F(2))
    require(sub(poly_mul(step, step)[2], doubled[2]) == commutator, 'coarsening degree-two sign')
    target = exp_series(sub(g, b))
    coefficient_majorant = norm(g)+norm(b)
    partition_cases = commuting_cases = riemann_cases = 0
    for n in [1, 2, 4, 8, 16]:
        for ramp in [False, True]:
            widths = ([F(j+1, n*(n+1)//2) for j in range(n)] if ramp else [F(1, n)]*n)
            require(sum(widths) == 1 and min(widths) > 0, 'positive partition of unit source interval')
            mesh, square_budget = max(widths), sum(x*x for x in widths)
            actual = partition_series(g, b, widths)
            require(actual[0] == target[0] and actual[1] == target[1], 'zeroth/first product coefficients')
            require(sub(actual[2], target[2]) == scale(commutator, -square_budget/2), 'partition degree-two telescope')
            require(square_budget <= mesh and norm(sub(actual[2], target[2])) <= mesh/2, 'mesh rather than count budget')
            for k in range(2, DEGREE+1):
                bound = 2*coefficient_majorant**k*mesh*sum(F(1, factorial(ell)*factorial(k-ell)) for ell in range(2, k+1))
                require(norm(sub(actual[k], target[k])) <= bound, 'formal coefficient mesh majorant')
            partition_cases += 1
            for commuting_probe in [zero(), identity()]:
                require(partition_series(g, commuting_probe, widths) == exp_series(sub(g, commuting_probe)), 'zero/constant probe exact sewing')
                commuting_cases += 1
            endpoint = F(0)
            moments = [F(0)]*(DEGREE+1)
            for width in widths:
                endpoint += width
                for k in range(DEGREE+1):
                    moments[k] += width*endpoint**k
            require(moments[0] == 1, 'Riemann constant coefficient')
            for k in range(1, DEGREE+1):
                require(0 <= moments[k]-F(1, k+1) <= k*mesh, 'right-Riemann power coefficients converge to integral')
            riemann_cases += 1
    require((partition_cases, commuting_cases, riemann_cases) == (10, 20, 10), 'frozen partition grids')
    for n in [2, 3, 8, 32, 128]:
        widths = [F(1, 2)]+[F(1, 2*(n-1))]*(n-1)
        squares = sum(x*x for x in widths)
        require(squares == F(1, 4)+F(1, 4*(n-1)) and max(widths) == F(1, 2), 'growing count without shrinking mesh')
        require(norm(scale(commutator, -squares/2)) == F(1, 8)+F(1, 8*(n-1)), 'nonshrinking formal defect')
    require(norm(scale(commutator, -F(1, 8))) == F(1, 8), 'exact limiting germ obstruction')
    exp_lower = sum(F((-1)**k, factorial(k)) for k in range(6))
    exp_upper = sum(F((-1)**k, factorial(k)) for k in range(5))
    require((exp_lower, exp_upper) == (F(11, 30), F(3, 8)), 'Taylor bounds for constant probe exp(-1)')
    require(1-exp_upper == F(5, 8) and 1-exp_lower == F(19, 30), 'normalization hostile interval from signed remainders')
    planner_cases = 0
    for R in [F(0), F(1, 128), F(9, 128), F(575, 4096)]:
        for T in [F(0), F(1), F(3)]:
            for gradient in [F(0), F(2)]:
                plan = plan_word_buffer(R, T*gradient, F(1, 1000))
                require(plan['error_bound'] <= F(1, 1000), 'completed-probe gradient budget')
                if T*gradient == 0:
                    require(plan['buffer'] == 0 and plan['error_bound'] == 0, 'identity/constant spatial comparison')
                if plan['buffer']:
                    require(plan['error_bound']*F(4, 3) > F(1, 1000), 'minimal sufficient buffer')
                planner_cases += 1
    universal = plan_word_buffer(None, 6, F(1, 1000))
    interior = plan_word_buffer(F(9, 128), 6, F(1, 1000))
    examples = [universal['buffer'], interior['buffer']]
    require(planner_cases == 24 and examples == [35, 29] == list(contract['comparison']['buffer_T3_M2_epsilon_1_1000'].values()), 'probe planner examples')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['mesh-word', 'propagator-comparison']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-limit.result.v1', 'passed': True,
            'strength': 'written bounded-perturbation and compact-orbit proof of actual-source strong product completion; finite controls are not analytic verification',
            'partition_families': partition_cases, 'formal_degree': DEGREE,
            'commuting_probe_controls': commuting_cases, 'riemann_families': riemann_cases,
            'probe_buffer_plans': planner_cases, 'buffers_T3_M2_epsilon_1_1000': examples,
            'mixed_commutator_norm': '1', 'nonshrinking_mesh_degree2_limit_norm': '1/8',
            'normalization_hostile_residual_open_interval': ['5/8', '19/30'],
            'strong_product_constructor_written': True, 'original_states_retained': True,
            'operator_norm_product_theorem': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'partition_families', 'formal_degree',
                     'commuting_probe_controls', 'riemann_families', 'probe_buffer_plans',
                     'mixed_commutator_norm', 'nonshrinking_mesh_degree2_limit_norm',
                     'normalization_hostile_residual_open_interval']}, indent=2))
