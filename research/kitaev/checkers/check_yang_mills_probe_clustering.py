"""Full tensor/cut controls for the written completed-probe clustering bound."""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_probe_limit import report as predecessor_report
from check_yang_mills_mesh_word import word_prefactor

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-clustering.v1.json'
NOTE = BASE+'yang-mills-probe-clustering-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_clustering.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-clustering-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, x):
    return [sum(w*y for w, y in zip(row, x)) for row in a]


def kron(a, b):
    return [[x*y for x in rowa for y in rowb] for rowa in a for rowb in b]


def diagonal(values):
    return [[x if i == j else F(0) for j in range(len(values))] for i, x in enumerate(values)]


def reset(law, q):
    return [[q*F(i == j)+(1-q)*law[j] for j in range(len(law))] for i in range(len(law))]


def plan_separation(R, T, gradient_sum, epsilon):
    T, gradient_sum, epsilon = F(T), F(gradient_sum), F(epsilon)
    if T < 0 or gradient_sum < 0 or epsilon <= 0:
        raise ValueError('nonnegative source horizon/gradient budgets and positive tolerance required')
    coefficient = F(36, 5) if R is None else 2*word_prefactor(R)
    b = 1
    error = coefficient*T*gradient_sum*F(3, 4)
    while error > epsilon:
        b += 1
        error *= F(3, 4)
    return {'buffer': b, 'separation': 2*b, 'error_bound': error}


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 3 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'strength guard')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['mixed-probe-susceptibility'], 'next constructor')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-limit-v1.json')).read_text()), 'fresh predecessor receipt')

    subsets = [frozenset(i for i in range(4) if mask & (1 << i)) for mask in range(16)]
    restriction_cases = 0
    for S, A, B in product(subsets, repeat=3):
        require(((A | B) <= S) == (A <= S and B <= S), 'retained-label deletion on arbitrary cuts')
        restriction_cases += 1
    require(restriction_cases == 4096, 'frozen restriction predicates')
    geometry_cases = 0
    for distance in range(2, 17):
        b = distance//2
        S1 = set(range(-b+1, b))
        S2 = set(range(distance-b+1, distance+b))
        S = S1 | S2
        require(S1.isdisjoint(S2) and min(abs(x-y) for x in S1 for y in S2) >= 2, 'disconnected buffered geometry')
        universe = range(-b-1, distance+b+2)
        require(min(abs(x) for x in universe if x not in S1) == b, 'first support buffer')
        require(min(abs(x-distance) for x in universe if x not in S2) == b, 'second support buffer')
        require(min(min(abs(x), abs(x-distance)) for x in universe if x not in S) >= b, 'joint support buffer')
        for left in universe:
            for right in range(left, distance+b+2):
                A = set(range(left, right+1))
                if A <= S:
                    require(A <= S1 or A <= S2, 'contained connected labels cannot span components')
        geometry_cases += 1
    require(geometry_cases == 15, 'frozen buffered geometry')

    p, q = [F(1, 3), F(2, 3)], [F(3, 5), F(2, 5)]
    joint_law = [x*y for x in p for y in q]
    a, b = [F(1), F(1, 2)], [F(2, 3), F(1)]
    tensor_cases = 0
    for n, rate1, rate2, pattern in product([1, 2, 4, 8, 16], [F(1, 2), F(2, 3), F(3, 4)], [F(1, 2), F(2, 3), F(3, 4)], range(2)):
        full, first, second = eye(4), eye(2), eye(2)
        for j in range(n):
            width = 1 if pattern == 0 else j % 3+1
            K1, K2 = reset(p, rate1**width), reset(q, rate2**width)
            require([sum(p[i]*K1[i][j] for i in range(2)) for j in range(2)] == p, 'first original state stationary for unprobed kernel')
            require([sum(q[i]*K2[i][j] for i in range(2)) for j in range(2)] == q, 'second original state stationary for unprobed kernel')
            E1, E2 = diagonal([x**width for x in a]), diagonal([x**width for x in b])
            full = mm(full, mm(kron(K1, K2), kron(E1, E2)))
            first, second = mm(first, mm(K1, E1)), mm(second, mm(K2, E2))
        require(full == kron(first, second), 'full tensor operator identity, not just one reader')
        require(all(x >= 0 for row in full for x in row) and all(sum(row) <= 1 for row in full), 'positive contractive probe packet')
        joint = sum(x*y for x, y in zip(joint_law, mv(full, [F(1)]*4)))
        singles = sum(x*y for x, y in zip(p, mv(first, [F(1)]*2)))*sum(x*y for x, y in zip(q, mv(second, [F(1)]*2)))
        require(joint == singles > 0, 'actual product-state scalarization and noncollapse')
        tensor_cases += 1
    require(tensor_cases == 90, 'frozen tensor families')

    coupled = [[F(9, 34), F(8, 34)], [F(8, 34), F(9, 34)]]
    require([sum(row) for row in coupled] == [F(1, 2)]*2 and [sum(coupled[i][j] for i in range(2)) for j in range(2)] == [F(1, 2)]*2, 'matching fair marginals hostile')
    influence = abs(F(9, 17)-F(8, 17))
    fa, fb = [F(1), F(1, 2)], [F(1), F(1, 3)]
    actual = sum(coupled[i][j]*fa[i]*fb[j] for i in range(2) for j in range(2))
    independent = sum(fa)/2*sum(fb)/2
    require(influence == F(1, 17) < F(9, 128), 'small unweighted influence survives')
    require(actual == F(103, 204) and independent == F(1, 2) and actual-independent == F(1, 204), 'matching marginals do not imply independence')
    for assigned_distance in [4, 16, 64]:
        require(F(4, 3)**assigned_distance*influence > F(16, 153), 'disconnected-label hostile violates required weighted bound')

    flip, I2, I4 = [[F(0), F(1)], [F(1), F(0)]], eye(2), eye(4)
    local = [[(I2[i][j]+flip[i][j])/2 for j in range(2)] for i in range(2)]
    both = kron(flip, flip)
    shared = [[(I4[i][j]+both[i][j])/2 for j in range(4)] for i in range(4)]
    separate = kron(local, local)
    require(mm(shared, shared) == shared and mm(separate, separate) == separate, 'invariant projectors')
    ranks = [sum(P[i][i] for i in range(4)) for P in [shared, separate]]
    witness = [F(1), F(-1), F(-1), F(1)]
    require(ranks == [2, 1] and mv(shared, witness) == witness and mv(separate, witness) == [0]*4, 'shared gauge quotient does not tensor-factor')

    planner_cases = 0
    for R, T, gradient in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(0), F(1), F(3)], [F(0), F(2)]):
        plan = plan_separation(R, T, gradient, F(1, 1000))
        require(plan['separation'] >= 2 and plan['error_bound'] <= F(1, 1000), 'typed separation budget')
        if plan['buffer'] > 1:
            require(plan['error_bound']*F(4, 3) > F(1, 1000), 'least sufficient disconnected buffer')
        if R*T*gradient == 0:
            require(plan['error_bound'] == 0, 'product-source and constant budget boundary')
        planner_cases += 1
    examples = [plan_separation(R, 1, 2, F(1, 1000))['separation'] for R in [None, F(9, 128)]]
    require(planner_cases == 24 and examples == [68, 56] == list(contract['comparison']['separation_T1_gradient_sum2_epsilon_1_1000'].values()), 'worked separation budgets')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-limit', 'thermodynamic-vacuum', 'mesh-word']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-clustering.result.v1', 'passed': True,
            'strength': 'written arbitrary-free-cut tensor realization and completed-probe spatial upper bound; independently unreviewed source analysis',
            'restriction_predicates': restriction_cases, 'buffered_geometry_cases': geometry_cases,
            'full_tensor_operator_cases': tensor_cases, 'separation_plans': planner_cases,
            'separations_T1_gradient_sum2_epsilon_1_1000': examples,
            'matching_marginal_hostile_residual': '1/204', 'hostile_unweighted_influence': '1/17',
            'shared_symmetry_projector_ranks': [int(x) for x in ranks], 'shared_symmetry_witness_residual': '1',
            'universal_prefactor': '36/5', 'bilinear_susceptibility_proved': False,
            'full_gauge_invariant_spaces_factor': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'restriction_predicates', 'buffered_geometry_cases',
                     'full_tensor_operator_cases', 'separation_plans', 'matching_marginal_hostile_residual',
                     'shared_symmetry_projector_ranks', 'shared_symmetry_witness_residual']}, indent=2))
