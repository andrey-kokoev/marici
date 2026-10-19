"""Exact regressions for a written equal-time convergence theorem, not a YM solver."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_anchored_casimir import report as anchored_report

ROOT = Path(__file__).resolve().parents[3]
STEM = 'research/kitaev/'
CONTRACT = STEM + 'contracts/yang-mills-thermodynamic-vacuum.v1.json'
NOTE = STEM + 'yang-mills-thermodynamic-vacuum-v1.md'
SELF = STEM + 'checkers/check_yang_mills_thermodynamic_vacuum.py'
OUT = ROOT / (STEM + 'results/yang-mills-thermodynamic-vacuum-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def subsets(s):
    s = sorted(s)
    return [frozenset(c) for n in range(len(s)+1) for c in combinations(s, n)]


def B(x, y):
    """Intrinsic centered inverse for Walsh modes, with UNION labels retained.

    This finite analogue is not the SU(2) derivative/Casimir calculation.
    A basis element is (retained label, actual nonconstant mode).
    """
    a, m = x
    b, n = y
    mode = m ^ n
    if not mode or not (m & n):
        return None
    return (a | b, mode), F(len(m & n), len(mode))


def project(term, box):
    return term if term and term[0][0] <= box else None


def invert(a):
    n = len(a)
    aug = [list(row)+[F(i == j) for j in range(n)] for i, row in enumerate(a)]
    for j in range(n):
        pivot = next(i for i in range(j, n) if aug[i][j])
        aug[j], aug[pivot] = aug[pivot], aug[j]
        t = aug[j][j]
        aug[j] = [v/t for v in aug[j]]
        for i in range(n):
            if i != j:
                t = aug[i][j]
                aug[i] = [x-t*y for x, y in zip(aug[i], aug[j])]
    return [row[n:] for row in aug]


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(all(v is False for v in contract['boundary'].values()), 'scope promotion')
    prior = anchored_report()
    require(prior['passed'], 'anchored dependency regression')
    require(prior == json.loads((ROOT/(STEM+'results/yang-mills-anchored-casimir-v1.json')).read_text()),
            'anchored receipt stale: explicit dependency review required')
    sites = frozenset(range(3))
    basis = [(a, m) for a in subsets(sites) if a for m in subsets(a) if m]
    squares = 0
    for x, y, box in product(basis, basis, subsets(sites)):
        left = project(B(x, y), box)
        right = B(x, y) if x[0] <= box and y[0] <= box else None
        require(left == right, 'retained-label restriction square')
        squares += 1
    # Trivial ambient Fourier factors add spin zero: dimension/Casimir unchanged.
    fourier_extensions = 0
    for spins in product(range(5), repeat=3):
        c = sum(F(n*(n+2), 4) for n in spins)
        dim = 1
        for n in spins:
            dim *= n+1
        for extra in range(4):
            extended = spins+(0,)*extra
            require(c == sum(F(n*(n+2), 4) for n in extended), 'ambient Casimir')
            new_dim = 1
            for n in extended:
                new_dim *= n+1
            require(dim == new_dim, 'ambient Fourier dimension')
            fourier_extensions += 1
    y = (frozenset({1}), frozenset({1}))
    xy = (frozenset({0, 1}), frozenset({0, 1}))
    term = B(y, xy)
    require(term == ((frozenset({0, 1}), frozenset({0})), F(1)), 'support-loss hostile source')
    inner = frozenset({0})
    require(project(term, inner) is None, 'retained outside attachment deleted')
    compressed = (term[0][1], term[0][1]), term[1]
    require(project(compressed, inner)[1] == 1, 'premature compression defect must be 1')
    require(not (y[0] <= inner) and not (xy[0] <= inner), 'restricted input vanishes')

    threshold = F(27, 262144)
    require(F(4096, 3)*threshold == F(9, 64), 'R endpoint')
    require(F(8, 9)*F(9, 64) == F(1, 8), 'weighted contraction endpoint')
    require(1/(1-F(1, 8)) == F(8, 7), 'boundary prefactor')
    a = F(4, 3)
    for n in range(1, 65):
        m = n-1
        require(F(m, 2**n) <= F(1, 4), 'unweighted support moment')
        require(2*m*a**m/F(2**n) <= F(8, 9), 'weighted support moment')
        if m >= 3:
            require(F(m+1, m)*F(2, 3) <= F(8, 9), 'all-later recurrence ratio')
    require(2*2*a**2/F(2**3) == F(8, 9), 'weighted maximum attained')

    # Connected interval fixture: exact positive influence resolvent and boundary bound.
    n = 5
    interactions = [(frozenset(range(i, j+1)), F(1, 4096))
                    for i in range(n) for j in range(i+1, n)]
    R = max(sum(2**len(s)*w for s, w in interactions if i in s) for i in range(n))
    C = [[sum(2*w for s, w in interactions if i in s and j in s) if i != j else F(0)
          for j in range(n)] for i in range(n)]
    alpha = F(8, 9)*R
    require(alpha < 1, 'fixture contraction')
    for i in range(n):
        require(sum(C[i]) <= R/2, 'fixture unweighted row')
        require(sum(a**abs(i-j)*C[i][j] for j in range(n)) <= alpha, 'fixture weighted row')
    D = invert([[F(i == j)-C[i][j] for j in range(n)] for i in range(n)])
    box = frozenset({1, 2, 3})
    h = [min(abs(i-j) for j in range(n) if j not in box) for i in range(n)]
    b = [sum(w for s, w in interactions if i in s and not s <= box) if i in box else F(1)
         for i in range(n)]
    for i in range(n):
        require(all(x >= 0 for x in D[i]), 'positive resolvent')
        require(sum(a**abs(i-j)*D[i][j] for j in range(n)) <= 1/(1-alpha), 'weighted resolvent')
        require(b[i] <= a**(-h[i]), 'crossing tail bound')
        require(sum(D[i][j]*b[j] for j in range(n)) <= a**(-h[i])/(1-alpha), 'boundary comparison algebra')

    weights = [[F(3), F(1)], [F(1), F(1)]]
    marginal = sum(weights[0])/sum(map(sum, weights))
    marginal_defect = marginal-F(1, 2)
    require(marginal_defect == F(1, 6), 'free-boundary marginal hostile')
    conditional_row = abs(weights[0][0]/sum(weights[0])-weights[1][0]/sum(weights[1]))
    require(conditional_row == F(1, 4) < 1, 'marginal mismatch despite contraction')
    # Disconnected labels can have small ordinary row but no asserted spatial rate.
    w = F(1, 10000)
    long_row = 2*w*a**10
    wrong_connected_bound = F(8, 9)*4*w
    require(2*w < 1 and long_row > wrong_connected_bound, 'connectedness hostile')
    rho_plus = [[F(1, 2), F(1, 2)], [F(1, 2), F(1, 2)]]
    rho_minus = [[F(1, 2), F(-1, 2)], [F(-1, 2), F(1, 2)]]
    require([rho_plus[i][i] for i in range(2)] == [rho_minus[i][i] for i in range(2)], 'same diagonal state')
    quantum_defect = sum(rho_plus[i][1-i]-rho_minus[i][1-i] for i in range(2))
    require(quantum_defect == 2, 'off-diagonal nonidentification hostile')
    inputs = [CONTRACT, NOTE, SELF, STEM+'contracts/yang-mills-anchored-casimir.v1.json',
              STEM+'yang-mills-anchored-casimir-v1.md', STEM+'checkers/check_yang_mills_anchored_casimir.py',
              STEM+'results/yang-mills-anchored-casimir-v1.json']
    return {'schema': 'marici.yang-mills-thermodynamic-vacuum.result.v1', 'passed': True,
            'scope': 'exact finite regressions accompanying a written equal-time thermodynamic convergence theorem',
            'restriction_squares': squares, 'trivial_fourier_extensions': fourier_extensions,
            'support_moment_cases': 64, 'influence_resolvent_size': n,
            'deliberate_failure_residuals': {'premature_support_compression': '1',
                'free_boundary_marginal': str(marginal_defect),
                'disconnected_weighted_row_excess': str(long_row-wrong_connected_bound),
                'off_diagonal_quantum_expectation': str(quantum_defect)},
            'analytic_inputs_mechanically_proved': False,
            'independent_analytic_review': False, 'quantum_gap_transport': False,
            'multi_time_correlations': False, 'continuum_Yang_Mills': False,
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result, indent=2))
