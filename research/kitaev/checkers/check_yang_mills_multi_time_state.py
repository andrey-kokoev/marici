"""Rational joint-state/RP tests, not an SU2 semigroup or continuum solver."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_propagator_comparison import report as predecessor_report
from check_yang_mills_thermodynamic_form import matmul, matvec, dot, det
from check_yang_mills_thermodynamic_vacuum import invert

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-multi-time-state.v1.json'
NOTE = BASE+'yang-mills-multi-time-state-v1.md'
SELF = BASE+'checkers/check_yang_mills_multi_time_state.py'
OUT = ROOT/(BASE+'results/yang-mills-multi-time-state-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 3 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['spatial-and-semigroup-clustering'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum root')
    prior = predecessor_report()
    require(prior['passed'] and prior == json.loads((ROOT/(BASE+'results/yang-mills-propagator-comparison-v1.json')).read_text()), 'predecessor stale')
    p = [F(1, 6), F(4, 6), F(1, 6)]
    A = [[F(2), F(-2), F(0)], [F(-1, 2), F(1), F(-1, 2)], [F(0), F(-2), F(2)]]
    Q = invert([[A[i][j]+F(i == j) for j in range(3)] for i in range(3)])
    require(all(x > 0 for row in Q for x in row), 'positive transition')
    require(all(sum(row) == 1 for row in Q), 'stochastic rows')
    for i, j in product(range(3), repeat=2):
        require(p[i]*Q[i][j] == p[j]*Q[j][i], 'detailed balance')
    PQ = [[p[i]*Q[i][j] for j in range(3)] for i in range(3)]
    for n in range(1, 4):
        for ix in combinations(range(3), n):
            require(det([[PQ[i][j] for j in ix] for i in ix]) >= 0, 'positive operator, not just entries')
    powers = [[[F(i == j) for j in range(3)] for i in range(3)]]
    for n in range(12):
        powers.append(matmul(powers[-1], Q))

    def law(times, states):
        ans = p[states[0]]
        for k in range(len(times)-1):
            ans *= powers[times[k+1]-times[k]][states[k]][states[k+1]]
        return ans

    times = [-2, -1, 0, 1, 2]
    total = F(0)
    atom_count = 0
    for states in product(range(3), repeat=5):
        prob = law(times, states)
        require(prob > 0, 'joint positivity')
        require(prob == law(times, states[::-1]), 'joint reversal')
        total += prob
        atom_count += 1
    require(total == 1, 'joint normalization')
    deletion_count = 0
    for removed in range(5):
        kept_times = times[:removed]+times[removed+1:]
        for kept in product(range(3), repeat=4):
            marginal = sum(law(times, kept[:removed]+(x,)+kept[removed:]) for x in range(3))
            require(marginal == law(kept_times, kept), 'all coordinate deletion marginals')
            deletion_count += 1

    def normalized(word):
        merged = {}
        for t, f in word:
            merged[t] = [x*y for x, y in zip(merged.get(t, [F(1)]*3), f)]
        return sorted(merged.items())

    def moment(word):
        w = normalized(word)
        if not w:
            return F(1)
        x = w[-1][1]
        for k in range(len(w)-2, -1, -1):
            x = [a*b for a, b in zip(w[k][1], matvec(powers[w[k+1][0]-w[k][0]], x))]
        return dot(p, x)

    def J(word):
        w = normalized(word)
        if not w:
            return [F(1)]*3
        require(w[0][0] >= 0, 'positive half')
        x = w[-1][1]
        for k in range(len(w)-2, -1, -1):
            x = [a*b for a, b in zip(w[k][1], matvec(powers[w[k+1][0]-w[k][0]], x))]
        return matvec(powers[w[0][0]], x)

    indicators = [[F(i == j) for i in range(3)] for j in range(3)]
    f, g = list(map(F, [-1, 0, 2])), list(map(F, [2, -1, 1]))
    words = [[(0, v)] for v in indicators]+[[(1, f)], [(0, g), (1, f), (2, g)], [(1, g), (2, f)]]
    gram = []
    for left in words:
        row = []
        for right in words:
            reflected = [(-t, v) for t, v in left]
            value = moment(reflected+right)
            require(value == dot(p, [x*y for x, y in zip(J(left), J(right))]), 'full word-pair reflection factorization')
            row.append(value)
        gram.append(row)
    principal_count = 0
    for n in range(1, 5):
        for ix in combinations(range(4), n):
            require(det([[gram[i][j] for j in ix] for i in ix]) >= 0, 'reflection PSD principal minor')
            principal_count += 1
    for word in words:
        require(moment(word) == moment([(t+7, v) for t, v in word]), 'stationarity')
        require(moment(word) == moment([(-t, v) for t, v in word]), 'reversal of words')
        for shift in range(3):
            require(J([(t+shift, v) for t, v in word]) == matvec(powers[shift], J(word)), 'shift quotient intertwining')
    duplicate = [(0, f), (1, f), (1, g), (3, g)]
    merged = [(0, f), (1, [x*y for x, y in zip(f, g)]), (3, g)]
    require(moment(duplicate) == moment(merged), 'coincident insertion sewing')
    qf = matvec(Q, f)
    null_coeff = [-x for x in qf]+[F(1)]
    require(matvec([row[:4] for row in gram[:4]], null_coeff) == [0]*4, 'exact RP radical')
    path_norm = dot(p, [x*x for x in f])-dot(p, [x*x for x in qf])
    require(path_norm > 0, 'RP-null is not path-null')

    signed = {s: F(1+2*s[0]*s[1]*s[2], 8) for s in product([-1, 1], repeat=3)}
    require(sum(signed.values()) == 1 and sum(w < 0 for w in signed.values()) == 4, 'signed triple hostile')
    for omitted in range(3):
        keep = [i for i in range(3) if i != omitted]
        for vals in product([-1, 1], repeat=2):
            require(sum(w for s, w in signed.items() if tuple(s[i] for i in keep) == vals) == F(1, 4), 'positive pair marginals hide negative triple')
    bad = [[F(1, 4), F(3, 4)], [F(3, 4), F(1, 4)]]
    flip = [F(1), F(-1)]
    link_reflection = dot(flip, matvec(bad, flip))/2
    require(link_reflection == F(-1, 2) and all(x > 0 for row in bad for x in row), 'stochastic link-reflection failure')
    inputs = [CONTRACT, NOTE, SELF, BASE+'contracts/yang-mills-gap-net.v1.json']
    for name in ['propagator-comparison', 'thermodynamic-form']:
        inputs += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                   BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                   BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-multi-time-state.result.v1', 'passed': True,
            'strength': 'written joint source-state/RP quotient construction with rational discrete-chain regressions',
            'joint_atoms': atom_count, 'deletion_marginals': deletion_count,
            'reflection_word_pairs': len(words)**2, 'reflection_principal_minors': principal_count,
            'hostiles': {'negative_triple_atom': str(min(signed.values())),
                         'wrong_link_reflection': str(link_reflection), 'RP_null_path_norm_squared': str(path_norm)},
            'upstream_receipt_fresh': True, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'physical_clock': False,
            'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'joint_atoms', 'deletion_marginals',
                    'reflection_word_pairs', 'reflection_principal_minors', 'hostiles']}, indent=2))
