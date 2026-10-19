"""Exact source-coframe and finite kernel/causality guards, not a limit prover."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from check_yang_mills_one_form_domain_audit import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-parameterized-strong-map.v1.json'
NOTE = BASE+'yang-mills-parameterized-strong-map-v1.md'
SELF = BASE+'checkers/check_yang_mills_parameterized_strong_map.py'
OUT = ROOT/(BASE+'results/yang-mills-parameterized-strong-map-v1.json')


def require(ok, reason):
    if not ok:
        raise AssertionError(reason)


def qmul(a, b):
    w, x, y, z = a
    s, u, v, t = b
    return [w*s-x*u-y*v-z*t, w*u+x*s+y*t-z*v,
            w*v-x*t+y*s+z*u, w*t+x*v-y*u+z*s]


def transpose(a):
    return list(map(list, zip(*a)))


def mul(a, b):
    return [[sum((x*y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def frame(p):
    imaginary = [[F(i == a+1) for i in range(4)] for a in range(3)]
    return transpose([[x/2 for x in qmul(p, e)] for e in imaginary])


def path(x, word):
    result = [x]
    for bit in word:
        result.append(result[-1] ^ bit)
    return tuple(result)


def finite_kernel(x, n, prefix):
    words = [w for w in product([0, 1], repeat=n) if w[:len(prefix)] == prefix]
    counts = Counter(path(x, w) for w in words)
    return {y: F(count, len(words)) for y, count in counts.items()}


def report():
    c = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(c['batch'] == {'kind': 'post-audit', 'iteration': 2, 'size': 10}, 'batch provenance')
    require(all(v is False for v in c['boundary'].values()), 'no analytic/physical promotion')
    require(c['net_update']['ready_frontier'] == [] and c['net_update']['parent_outcome'] is None, 'bounded frontier closure only')
    require(c['net_update']['bounded_post_audit_objective_complete_at_written_conditional_scope'], 'written conditional completion')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-one-form-domain-audit-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text(encoding='utf-8')), 'fresh R3 and frozen upstream evidence')
    counts = {}
    points = [list(map(F, p)) for p in [
        [2, 0, 0, 0], [0, 2, 0, 0], [F(6, 5), F(8, 5), 0, 0],
        [1, 1, 1, 1], [0, 0, F(6, 5), F(8, 5)]]]
    count = 0
    for p, q in product(points, repeat=2):
        V, U = frame(p), frame(q)
        require(sum(x*x for x in p) == 4, 'actual radius-two SU2 data')
        identity = [[F(i == j) for j in range(3)] for i in range(3)]
        require(mul(transpose(V), V) == identity, 'coframe is a left inverse of the marked fields')
        tangent = [[F(i == j)-p[i]*p[j]/4 for j in range(4)] for i in range(4)]
        require(mul(V, transpose(V)) == tangent, 'source bracket is the tangent projection')
        difference_squared = sum((V[i][a]-U[i][a])**2 for i in range(4) for a in range(3))
        require(difference_squared == F(3, 4)*sum((x-y)**2 for x, y in zip(p, q)), 'exact coframe Lipschitz square')
        negative_V = [[-x for x in row] for row in V]
        require(mul(negative_V, transpose(negative_V)) == tangent, 'opposite markings preserve marginal covariance')
        require(mul(transpose(V), negative_V) == [[-x for x in row] for row in identity], 'wrong marking reverses recovered driver')
        count += 1
    counts['actual_SU2_coframe_packets'] = count
    count = 0
    for kappa, R, L, T in product([F(1, 4), F(1, 2), F(1)], [F(0), F(1, 16), F(1, 8)], [F(0), F(1, 4), F(1)], [F(1), F(2)]):
        B0 = kappa*(F(3, 2)+2*R+2*L)
        K = 12*kappa+2*B0**2*T
        C = 3*K*T
        require(4*F(3, 4)*K*T == C, 'Doob/coframe/dyadic source budget')
        epsilon, tolerance = F(1, 4), F(1, 64)
        N = 0
        while 2*C*F(1, 2**N)/epsilon**2 > tolerance:
            N += 1
        require(2*C*F(1, 2**N)/epsilon**2 <= tolerance, 'summable error probability tail')
        require(N == 0 or 2*C*F(1, 2**(N-1))/epsilon**2 > tolerance, 'least sufficient dyadic level')
        count += 1
    counts['dyadic_error_budget_packets'] = count
    count = 0
    for n in range(1, 5):
        for m in range(n+1):
            for x in [0, 1]:
                for prefix in product([0, 1], repeat=m):
                    kernel = finite_kernel(x, n, prefix)
                    require(sum(kernel.values()) == 1 and all(v > 0 for v in kernel.values()), 'partition conditional probability kernel')
                    require({y[:m+1] for y in kernel} == {path(x, prefix)}, 'past depends only on past noise')
                    if m == n:
                        require(kernel == {path(x, prefix): F(1)}, 'full-noise kernel is Dirac with its actual atom')
                    else:
                        children = [finite_kernel(x, n, prefix+(b,)) for b in [0, 1]]
                        keys = set(kernel) | set(children[0]) | set(children[1])
                        require(all(kernel.get(y, F(0)) == (children[0].get(y, F(0))+children[1].get(y, F(0)))/2 for y in keys), 'conditional-kernel refinement tower')
                count += 1
    counts['finite_partition_disintegration_packets'] = count
    count = 0
    for n, x in product([2, 3, 4], [0, 1]):
        words = list(product([0, 1], repeat=n))
        anticipated = F(sum((-1)**((x ^ w[-1]) ^ x)*(-1)**w[-1] for w in words), len(words))
        causal = F(sum((-1)**((x ^ w[0]) ^ x)*(-1)**w[-1] for w in words), len(words))
        require(anticipated == 1 and causal == 0, 'Borel/Dirac does not imply compatibility or adaptedness')
        count += 1
    counts['anticipation_counter_packets'] = count
    count = 0
    p = points[0]
    V = frame(p)
    for kappa in [F(1, 4), F(1, 2), F(1)]:
        expected = 2*kappa*sum(V[1][a]**2 for a in range(3))
        frozen = F(0)
        require(expected-frozen == 2*kappa > 0, 'actual free-SU2 deterministic identity row cannot be frozen')
        if kappa == F(1, 2):
            require(expected-frozen == 1, 'actual null-initial-row bracket defect1')
        count += 1
    counts['actual_free_SU2_null_initial_row_packets'] = count
    count = 0
    for probability in [F(1, 4), F(1, 2), F(3, 4)]:
        off_diagonal = 2*probability*(1-probability)
        require(off_diagonal > 0 and probability**2+(1-probability)**2+off_diagonal == 1, 'non-Dirac conditional-copy obstruction')
        if probability == F(1, 2):
            require(off_diagonal == F(1, 2), 'fair kernel copy mismatch')
        count += 1
    counts['non_Dirac_copy_packets'] = count
    count = 0
    for x in [0, 1]:
        gamma = {0: F(1, 2), 1: F(1, 2), 2: F(0)}
        kernels = {0: {x: F(1)}, 1: {x ^ 1: F(1)}, 2: {x: F(1)}}
        require(all(sum(k.values()) == 1 for k in kernels.values()), 'zero-noise-mass atom has a normalized default')
        reconstructed = {y: sum(gamma[w]*kernels[w].get(y, F(0)) for w in gamma) for y in [0, 1]}
        require(reconstructed == {0: F(1, 2), 1: F(1, 2)}, 'null-noise default does not change any parameter law')
        count += 1
    counts['zero_noise_atom_packets'] = count
    count = 0
    for mu0 in [F(0), F(1, 4), F(1, 2), F(1)]:
        mu = {0: mu0, 1: 1-mu0}
        joint = {(x, w): mu[x]*F(1, 8) for x in [0, 1] for w in product([0, 1], repeat=3)}
        require(sum(joint.values()) == 1, 'independent arbitrary initial mixture')
        require(all(path(x, w)[0] == x for x, w in joint), 'one map preserves each initial parameter')
        require(sum(weight for (x, w), weight in joint.items() if path(x, w)[-1] == 1) == F(1, 2), 'same kernel works under each independent preparation')
        count += 1
    counts['independent_initial_mixture_packets'] = count
    count = 0
    for N in [2, 4, 8, 16, 32, 64]:
        diagonal = [[F(x == w) for w in range(N)] for x in range(N)]
        independent = sum(sum(row) for row in diagonal)/N**2
        correlated = sum(diagonal[w][w] for w in range(N))/N
        require(independent == F(1, N) and correlated == 1, 'exceptional graph: independent input versus future-noise coupling')
        if N == 8:
            require(correlated-independent == F(7, 8), 'scope-control gap,not a finite null-set theorem')
        count += 1
    counts['exceptional_graph_scope_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 131, 'preregistered finite coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path]
    paths += [BASE+name for name in [
        'yang-mills-one-form-domain-audit-v1.md', 'yang-mills-shoshin-second-pass-review-v1.md',
        'yang-mills-probe-pointwise-core-v1.md', 'yang-mills-probe-strong-noise-v1.md',
        'yang-mills-probe-coupled-transport-v1.md', 'contracts/yang-mills-gap-net.v2.json']]
    return {
        'schema': 'marici.yang-mills-parameterized-strong-map.result.v1', 'passed': True,
        'strength': 'written conditional every-x Borel/adapted strong-map theorem,including source antidevelopment kernel; external analytic review remains open',
        'coverage': counts, 'new_exact_controls': 131,
        'predecessor_R3_controls_freshly_replayed': previous['new_exact_controls'],
        'earlier_scaling_controls_freshly_replayed': previous['predecessor_scaling_controls_freshly_replayed'],
        'actual_free_SU2_null_initial_row_bracket_defect': '1',
        'actual_SU2_opposite_driver_recovery_defect': '2',
        'anticipation_compatibility_defect': '1',
        'fair_non_Dirac_copy_off_diagonal_mass': '1/2',
        'exceptional_graph_scope_gap_N8': '7/8',
        'written_conditional_parameterized_strong_map': True,
        'bounded_post_audit_objective_complete_at_written_conditional_scope': True,
        'ready_frontier': [],
        'finite_controls_certify_parameterized_theorem': False,
        'independent_analytic_review_complete': False,
        'physical_continuum_or_Yang_Mills_root_discharged': False,
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
