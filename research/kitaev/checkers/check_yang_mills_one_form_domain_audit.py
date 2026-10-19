"""R3 exact geometry/operator-algebra guards; not an infinite-domain prover."""
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
from check_yang_mills_gap_net_v2 import report as predecessor_report

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-one-form-domain-audit.v1.json'
NOTE = BASE+'yang-mills-one-form-domain-audit-v1.md'
SELF = BASE+'checkers/check_yang_mills_one_form_domain_audit.py'
OUT = ROOT/(BASE+'results/yang-mills-one-form-domain-audit-v1.json')


def require(ok, reason):
    if not ok:
        raise AssertionError(reason)


def mul(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def mv(a, v):
    return [sum((x*y for x, y in zip(row, v)), F(0)) for row in a]


def eps(a, b, c):
    if len({a, b, c}) < 3:
        return 0
    return 1 if (a, b, c) in [(0, 1, 2), (1, 2, 0), (2, 0, 1)] else -1


def report():
    contract = json.loads((ROOT/CONTRACT).read_text(encoding='utf-8'))
    require(contract['batch'] == {'kind': 'post-audit', 'iteration': 1, 'size': 10}, 'new batch provenance')
    require(all(v is False for v in contract['boundary'].values()), 'scope guards')
    require(contract['net_update']['ready_frontier'] == ['parameterized-strong-map-lemma']
            and contract['net_update']['parent_outcome'] is None, 'R4 remains executable,root not discharged')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-gap-net-v2.json'
    require(previous == json.loads((ROOT/previous_path).read_text(encoding='utf-8')) and previous['passed'], 'fresh v2 controls and frozen source evidence')
    counts = {}
    count = 0
    for kappa, x in product([F(1, 4), F(1), F(2)], [F(1), F(5, 4), F(2), F(4), F(8), F(16)]):
        alpha, b = 64*kappa*(1+x)**2, kappa*x
        q = F(5, 16)/(1+x)+b/alpha
        require(q <= F(81, 256) < F(1, 2), 'rational source Neumann envelope')
        require(8/(kappa*alpha) <= 1/(4*kappa**2*(1+x)**2), 'coarse differentiated inverse envelope')
        count += 1
    counts['neumann_envelopes'] = count
    C = [[[F(eps(a, b, c), 2) for b in range(3)] for c in range(3)] for a in range(3)]
    count = 0
    for c, d in product(range(3), repeat=2):
        connection_square = sum(mul(ca, ca)[c][d] for ca in C)
        curl = sum(F(eps(a, b, c)*eps(a, b, d), 2) for a, b in product(range(3), repeat=2))
        require(connection_square == -F(c == d, 2), 'radius-two connection-square normalization')
        require(curl == F(c == d), 'J(Df)=kappa*Df')
        count += 2
    counts['frame_connection_entries'] = count
    count = 0
    defect = None
    for kappa, ratio in product([F(1, 4), F(1), F(2)], [1, 4, 256]):
        alpha = ratio*kappa
        # Actual invariant subspaces: a constant left-frame field and D(plaquette character).
        scalar_rates = [F(0), 3*kappa]
        curl_rates = [F(0), kappa]
        Z0 = -kappa
        for scalar_rate, curl_rate, expected_rate in zip(scalar_rates, curl_rates, [kappa, 3*kappa]):
            perturbation = curl_rate+Z0
            R = 1/(alpha+scalar_rate)
            factored = R/(1-perturbation*R)
            require(factored == 1/(alpha+expected_rate), 'actual free-SU2 resolvent factorization')
        omitted = 1/(alpha+4*kappa)
        correct = 1/(alpha+3*kappa)
        require(correct-omitted == kappa/((alpha+3*kappa)*(alpha+4*kappa)), 'omitted first-order connection reader')
        if kappa == alpha == 1:
            defect = correct-omitted
            require(defect == F(1, 20), 'actual free-SU2 resolvent defect')
        count += 1
    counts['actual_free_SU2_resolvent_packets'] = count
    count = 0
    for kappa in [F(1, 4), F(1), F(2)]:
        for rate in [kappa, 3*kappa]:
            v = -1/rate  # minus integral of exp(-rate*t) against unit forcing
            require(-rate*v == 1, 'zero-resolvent forcing identity')
            require(abs(-rate*(1/rate)-1) == 2, 'wrong integral sign has residual2')
        count += 1
    counts['actual_free_SU2_zero_resolvent_packets'] = count
    count, graph_count = 0, 0
    wrong_order_defect = None
    for alpha, shear in product(map(F, [1, 2, 4]), [F(1, 4), F(1, 2), F(1)]):
        # A=diag(1,2), K=[[0,shear],[0,0]]. This guard is not a gauge source.
        R = [[1/(alpha+1), F(0)], [F(0), 1/(alpha+2)]]
        inverse_I_minus_B = [[F(1), shear/(alpha+2)], [F(0), F(1)]]
        alpha_minus_G = [[alpha+1, -shear], [F(0), alpha+2]]
        correct = mul(R, inverse_I_minus_B)
        require(mul(alpha_minus_G, correct) == [[1, 0], [0, 1]], 'noncommuting inverse in correct order')
        wrong = mul(inverse_I_minus_B, R)
        if alpha == shear == 1:
            wrong_order_defect = correct[0][1]-wrong[0][1]
            require(wrong_order_defect == F(1, 18), 'inverse order matters')
        q = shear/(alpha+2)
        for u, v in product(map(F, [-1, 0, 1]), repeat=2):
            base = [(alpha+1)*u, (alpha+2)*v]
            perturbed = mv(alpha_minus_G, [u, v])
            base_norm, perturbed_norm = max(map(abs, base)), max(map(abs, perturbed))
            require((1-q)*base_norm <= perturbed_norm <= (1+q)*base_norm, 'equivalent graph norms')
            graph_count += 1
        count += 1
    counts['noncommuting_factorization_packets'], counts['graph_norm_envelopes'] = count, graph_count
    count = 0
    for n in range(1, 9):
        # Moving coordinate projections are strong-null on constant-field ell2,
        # but applying to the uncontrolled input e_n leaves norm1.
        size = n+2
        projection = [[F(i == j == n-1) for j in range(size)] for i in range(size)]
        fixed_head = [F(1, 2**(i+1)) for i in range(size)]
        moving_input = [F(i == n-1) for i in range(size)]
        fixed_output, moving_output = mv(projection, fixed_head), mv(projection, moving_input)
        require(sum(x*x for x in fixed_output) == F(1, 2**(2*n)), 'fixed geometric-tail vector output tends to zero')
        require(sum(x*x for x in moving_output) == 1, 'moving-input projection norm residual1')
        count += 1
    counts['moving_input_packets'] = count
    count = 0
    for n in [1, 2, 4, 8]:
        N, entry = n*n, F(1, n)
        row_bound, column_sum = entry, N*entry
        output_squared = N*entry**2
        require(row_bound <= 1 and column_sum == n and output_squared == 1, 'pointwise entries and bounded operator norm do not supply strong convergence without column tails')
        count += 1
    counts['missing_column_packets'] = count
    count = 0
    for k in range(1, 9):
        N = 2**k
        harmonic = sum(F(1, n) for n in range(1, N+1))
        laplacian_trace = sum(4*F(n*(n+1), n**3) for n in range(1, N+1))
        exact_hessian_squared_at_identity = sum(F(16*(n*(n+1))**2, 3*n**6) for n in range(1, N+1))
        require(harmonic >= 1+F(k, 2) and laplacian_trace >= 4*harmonic, 'actual character trace diverges by dyadic harmonic lower bound')
        require(exact_hessian_squared_at_identity <= F(128, 3), 'HS square stays bounded while trace diverges')
        count += 1
    counts['actual_free_SU2_harmonic_trace_packets'] = count
    require(counts == contract['frozen_coverage'] and sum(counts.values()) == 158, 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path]
    paths += [BASE+name for name in [
        'contracts/yang-mills-gap-net.v2.json', 'yang-mills-shoshin-second-pass-review-v1.md',
        'yang-mills-propagator-comparison-v1.md', 'yang-mills-probe-pointwise-core-v1.md',
        'yang-mills-probe-strong-noise-v1.md']]
    return {
        'schema': 'marici.yang-mills-one-form-domain-audit.result.v1', 'passed': True,
        'strength': 'written conditional extension/domain identification with explicit source ledger; no independent certification of upstream analytic inputs',
        'coverage': counts, 'new_exact_controls': 158,
        'predecessor_scaling_controls_freshly_replayed': previous['conditional_scaling_control_packets_replayed'],
        'actual_free_SU2_omitted_connection_resolvent_defect': str(defect),
        'noncommuting_wrong_inverse_order_defect': str(wrong_order_defect),
        'moving_input_or_missing_column_norm_defect': '1',
        'wrong_zero_resolvent_sign_defect': '2',
        'written_conditional_one_form_domain_identified': True,
        'finite_controls_certify_infinite_domain_theorem': False,
        'independent_analytic_review_complete': False,
        'next_executable': 'parameterized-strong-map-lemma',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'input_sha256'}, indent=2))
