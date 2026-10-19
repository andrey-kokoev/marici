"""Exact rational buffer planner and norm-safe compressed-memory controls."""
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_box_boundary_leakage import report as predecessor_report
from check_yang_mills_reader_dynamics import mm, sub, mv, transpose

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-buffered-memory.v1.json'
NOTE = BASE+'yang-mills-buffered-memory-v1.md'
SELF = BASE+'checkers/check_yang_mills_buffered_memory.py'
OUT = ROOT/(BASE+'results/yang-mills-buffered-memory-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def budget_buffer(prefactor, epsilon, delta):
    prefactor, epsilon, delta = map(F, [prefactor, epsilon, delta])
    if prefactor < 0 or epsilon <= 0 or delta <= 0:
        raise ValueError('nonnegative prefactor and positive amplitude/quadratic tolerances required')
    b, amplitude = 0, prefactor
    while amplitude > epsilon or amplitude*amplitude > delta:
        b += 1
        amplitude *= F(3, 4)
    return {'buffer': b, 'prefactor': prefactor, 'amplitude_bound': amplitude, 'quadratic_bound': amplitude*amplitude}


def plan_buffer(R, kappa, T, M, epsilon, delta):
    """T is a STEP horizon; None means all parameters. Budget is sufficient."""
    R, kappa, M = map(F, [R, kappa, M])
    if not (0 <= R < F(9, 64)) or kappa <= 0 or M < 0:
        raise ValueError('outside admitted source/gradient parameter stratum')
    c = F(1, 2)-3*R
    factor = F(1)
    if T is not None:
        T = F(T)
        if T < 0:
            raise ValueError('negative step horizon')
        factor = min(kappa*c*T, F(1))
    return budget_buffer(2*R*M*factor/c, epsilon, delta)


def matpower(a, n):
    out = [[F(i == j) for j in range(3)] for i in range(3)]
    for _ in range(n):
        out = mm(out, a)
    return out


def inner(a, b):
    return sum(x*y for x, y in zip(a, b))/3


def explain(plan):
    return {k: str(v) if isinstance(v, F) else v for k, v in plan.items()}


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 10 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['mesh-uniform-insertion-error'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-box-boundary-leakage-v1.json')).read_text()), 'predecessor stale')
    planner_cases, max_buffer = 0, 0
    for R, kappa, T, M, epsilon, delta in product(
            [F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 4), F(1, 2), F(1), F(2)],
            [F(0), F(1, 3), F(4), None], [F(0), F(1), F(4)],
            [F(1, 10), F(1, 100)], [F(1, 200), F(1, 10000)]):
        plan = plan_buffer(R, kappa, T, M, epsilon, delta)
        b, amplitude = plan['buffer'], plan['amplitude_bound']
        require(amplitude == plan['prefactor']*F(3, 4)**b and amplitude <= epsilon and amplitude*amplitude <= delta, 'both exact tolerances')
        if b:
            before = amplitude*F(4, 3)
            require(before > epsilon or before*before > delta, 'minimal integer for rational sufficient budget')
        cc = F(1, 2)-3*R
        require(cc+3*R == F(1, 2) and 2*R/cc < F(18, 5), 'saturating prefactor and uniform coupling-window bound')
        require(2*kappa*R/(kappa*cc) == 2*R/cc, 'integrated damped Duhamel coefficient')
        require(plan['prefactor'] <= 2*R*M/cc, 'finite horizon below saturation')
        if T is not None:
            require(plan['prefactor'] <= 2*kappa*R*T*M, 'short-step linear budget')
        if R == 0 or M == 0 or T == 0:
            require(b == 0 and amplitude == 0, 'zero cases')
        planner_cases += 1
        max_buffer = max(max_buffer, b)
    require(planner_cases == 768, 'frozen planner coverage')
    epsilon, delta = F(1, 100), F(1, 10000)
    finite = plan_buffer(F(9, 128), F(1), F(1), F(4), epsilon, delta)
    all_times = plan_buffer(F(9, 128), F(1), None, F(4), epsilon, delta)
    universal = budget_buffer(F(18, 5)*4, epsilon, delta)
    require([finite['buffer'], all_times['buffer'], universal['buffer']] == list(c['certificate']['fixtures'].values()) == [15, 19, 26], 'declared minimal-buffer witnesses')

    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    projection = [[F(1, 2), F(1, 2), F(0)], [F(1, 2), F(1, 2), F(0)], [F(0), F(0), F(1)]]
    complement = sub(identity, projection)
    kernel = [[F(1, 2), F(1, 4), F(1, 4)], [F(1, 4), F(3, 4), F(0)], [F(1, 4), F(0), F(3, 4)]]
    inputs = [[F(1), F(1), F(1)], [F(1), F(1), F(0)], [F(0), F(0), F(1)], [F(-1), F(-1), F(2)]]
    mixed_cases = 0
    for n, m in product(range(1, 5), repeat=2):
        pn, pm = matpower(kernel, n), matpower(kernel, m)
        kn, km = mm(mm(projection, pn), projection), mm(mm(projection, pm), projection)
        defect = sub(mm(mm(projection, matpower(kernel, n+m)), projection), mm(kn, km))
        rn, rm = mm(mm(complement, pn), projection), mm(mm(complement, pm), projection)
        require(defect == mm(transpose(rn), rm), 'mixed compression factorization')
        for g, f in product(inputs, repeat=2):
            pairing = inner(g, mv(defect, f))
            left, right = mv(rn, g), mv(rm, f)
            require(pairing == inner(left, right) and pairing*pairing <= inner(left, left)*inner(right, right), 'mixed memory Cauchy-Schwarz')
            if n == m and g == f:
                require(pairing == inner(right, right) >= 0, 'equal-step quadratic norm identity')
            mixed_cases += 1
    leakage = mv(mm(complement, kernel), inputs[1])
    require(inner(leakage, leakage) == F(1, 96) > 0, 'zero full-carrier comparison error does not transfer to incomplete reader')
    require(mm(sub(identity, identity), kernel) == [[F(0)]*3 for _ in range(3)], 'full-carrier reader has no toy leakage')
    defect1 = sub(mm(mm(projection, matpower(kernel, 2)), projection), mm(mm(mm(projection, kernel), projection), mm(mm(projection, kernel), projection)))
    require(mv(defect1, inputs[0]) == [0, 0, 0] and inner(inputs[1], mv(defect1, inputs[1])) > 0, 'one constant probe does not bound whole defect operator')
    J = [[F(1, 3)]*3 for _ in range(3)]
    qj = sub(identity, J)
    v = [F(1), F(-1), F(-1)]
    qv = mv(qj, v)
    require(max(map(abs, qv)) == F(4, 3) > max(map(abs, v)) and inner(qv, qv) <= inner(v, v), 'Q is L2 but not L-infinity contractive')
    own_kernel = [[identity[i][j]/4+3*J[i][j]/4 for j in range(3)] for i in range(3)]
    v = [F(1), F(0), F(1)]
    output = mv(own_kernel, v)
    rho = [F(1, 6), F(4, 6), F(1, 6)]
    norm_before = sum(w*x*x for w, x in zip(rho, v))
    norm_after = sum(w*x*x for w, x in zip(rho, output))
    require(norm_before == F(1, 3) < norm_after == F(17, 48), 'own-measure contraction fails under copied target measure')
    require(inner(output, output) <= inner(v, v), 'same kernel contracts in its own uniform measure')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path'], BASE+'yang-mills-multi-time-state-v1.md', BASE+'scc-failures/yang-mills-buffered-memory.coverage384.py.txt']
    for name in ['box-boundary-leakage', 'propagator-comparison', 'source-clustering', 'reader-dynamics']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                  BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-buffered-memory.result.v1', 'passed': True,
            'strength': 'written actual-state buffered memory bounds, including all-source-parameter saturation; independently unreviewed',
            'planner_cases': planner_cases, 'largest_planned_buffer': max_buffer,
            'mixed_memory_cases': mixed_cases, 'finite_step_horizon_example': explain(finite),
            'all_parameter_example': explain(all_times), 'whole_coupling_window_all_parameter_example': explain(universal),
            'Q_Linfinity_hostile_norm': '4/3', 'wrong_measure_expansion': ['1/3', '17/48'],
            'incomplete_reader_zero_comparison_leakage': '1/96', 'actual_free_measure_identified': False,
            'whole_reader_operator_norm_claim': False, 'arbitrary_insertion_error_control': False,
            'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'planner_cases', 'mixed_memory_cases',
                     'finite_step_horizon_example', 'all_parameter_example',
                     'whole_coupling_window_all_parameter_example']}, indent=2))
