"""Exact polynomial audit: do the proposed requirements select an action?
No optimizer, float arithmetic, or physical identification of graph data.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

BASE = Path(__file__).resolve().parents[1]
N = 4  # three fields plus a symbolic translation/dilation parameter
ZERO = (0,)*N

def clean(p):
    return {e: F(c) for e, c in p.items() if c}

def const(c):
    return clean({ZERO: F(c)})

def variable(i):
    e = [0]*N
    e[i] = 1
    return {tuple(e): F(1)}

def add(*ps):
    out = {}
    for p in ps:
        for e, c in p.items():
            out[e] = out.get(e, F(0)) + c
    return clean(out)

def scale(c, p):
    return clean({e: F(c)*v for e, v in p.items()})

def multiply(p, q):
    out = {}
    for a, x in p.items():
        for b, y in q.items():
            e = tuple(i+j for i, j in zip(a, b))
            out[e] = out.get(e, F(0)) + x*y
    return clean(out)

def power(p, n):
    out = const(1)
    for _ in range(n):
        out = multiply(out, p)
    return out

def derivative(p, i):
    out = {}
    for e, c in p.items():
        if e[i]:
            key = list(e)
            key[i] -= 1
            out[tuple(key)] = c*e[i]
    return clean(out)

def evaluate(p, values):
    out = F(0)
    for e, c in p.items():
        for x, n in zip(values, e):
            c *= F(x)**n
        out += c
    return out

EDGES = [(0, 1, F(1)), (1, 2, F(3))]
SOURCE = (F(0), F(2), F(0))
PHI = [variable(i) for i in range(3)]
PARAM = variable(3)

def action(fields, edges=EDGES, source=SOURCE, mu2=F(0), quartic=F(0)):
    pieces = []
    for i, j, w in edges:
        d = add(fields[i], scale(-1, fields[j]))
        pieces.append(add(scale(w/2, power(d, 2)), scale(quartic/4, power(d, 4))))
    for i, f in enumerate(fields):
        pieces.append(add(scale(-source[i], f), scale(mu2/2, power(f, 2))))
    return add(*pieces), pieces

models = {'quadratic': {}, 'screened': {'mu2': F(2)}, 'quartic': {'quartic': F(1)}}
results = {}
for name, options in models.items():
    s, pieces = action(PHI, **options)
    assert s == add(*reversed(pieces))  # exact additive composition/order independence
    reversed_edges = [(j, i, w) for i, j, w in reversed(EDGES)]
    assert s == action(PHI, reversed_edges, **options)[0]
    shifted = action([add(f, PARAM) for f in PHI], **options)[0]
    shift_residual = add(shifted, scale(-1, s), scale(sum(SOURCE), PARAM))
    source_free = action(PHI, source=(F(0),)*3, **options)[0]
    dilated = action([multiply(PARAM, f) for f in PHI], source=(F(0),)*3, **options)[0]
    degree_two_residual = add(dilated, scale(-1, multiply(power(PARAM, 2), source_free)))
    gradient = [derivative(s, i) for i in range(3)]
    results[name] = {
        'local_vertex_edge_sum': True,
        'additive_composition': True,
        'edge_reversal_invariant': True,
        'bulk_shift_covariance': not shift_residual,
        'degree_two_homogeneity': not degree_two_residual,
        'free_vertex_residual_at_poisson_solution': str(evaluate(gradient[1], [0, F(1, 2), 0, 0])),
    }
assert results['quadratic']['bulk_shift_covariance']
assert results['quartic']['bulk_shift_covariance']
assert not results['screened']['bulk_shift_covariance']
assert results['screened']['degree_two_homogeneity']
assert not results['quartic']['degree_two_homogeneity']

# Derive the full gradient by polynomial differentiation; compare to incidence.
s = action(PHI)[0]
laplacian = [[F(0) for _ in range(3)] for _ in range(3)]
for i, j, w in EDGES:
    laplacian[i][i] += w
    laplacian[j][j] += w
    laplacian[i][j] -= w
    laplacian[j][i] -= w
for i in range(3):
    residual = add(*(scale(laplacian[i][j], PHI[j]) for j in range(3)), const(-SOURCE[i]))
    assert derivative(s, i) == residual
    assert sum(laplacian[i]) == 0
    for j in range(3):
        assert derivative(derivative(s, i), j) == const(laplacian[i][j])

# Dirichlet boundaries phi_0=phi_2=0: only vertex 1 is varied.
assert evaluate(derivative(s, 1), [0, F(1, 2), 0, 0]) == 0
screened = action(PHI, mu2=F(2))[0]
assert evaluate(derivative(screened, 1), [0, F(1, 3), 0, 0]) == 0
assert evaluate(derivative(screened, 1), [0, F(1, 2), 0, 0]) != 0
quartic = action(PHI, quartic=F(1))[0]
assert evaluate(derivative(quartic, 1), [0, F(1, 2), 0, 0]) == F(1, 4)

# Two edges with the same total weight are not identified as the same history.
duplicated = action(PHI, EDGES + [EDGES[0]])[0]
assert duplicated != s
# Dropping a mixed term in the square must not satisfy the action identity.
wrong = add(s, multiply(PHI[0], PHI[1]))
assert derivative(wrong, 0) != derivative(s, 0)
# A closed graph with nonzero total source has NO stationary point: summing
# its three residual polynomials yields the nonzero constant -sum(source).
assert add(*(derivative(s, i) for i in range(3))) == const(-2)

# Coefficient classification for an arbitrary quadratic edge polynomial:
# joint shift => b=-2a,c=a,e=-d; swap symmetry => d=e, hence d=e=0;
# zero at equal fields => f=0. Verify the resulting family symbolically.
u, v, a = variable(0), variable(1), variable(2)
selected = multiply(a, power(add(u, scale(-1, v)), 2))
expanded = add(multiply(a, power(u, 2)), scale(-2, multiply(a, multiply(u, v))), multiply(a, power(v, 2)))
assert selected == expanded

files = [Path(__file__), BASE/'agda/GraphAction.agda']
packet = {
    'status': 'selection-not-unique-without-quadraticity',
    'models': results,
    'laplacian': [[str(v) for v in row] for row in laplacian],
    'dirichlet_solutions': {'quadratic': '1/2', 'screened_mu2_2': '1/3'},
    'closed_nonzero_source_obstruction': True,
    'classification': 'Pair-local, swap-symmetric, shift-invariant, normalized polynomials of degree <=2 are a*(u-v)^2; degree bound is an EXTRA assumption. Weights remain free.',
    'hostiles': {'double_counted_edge': True, 'missing_mixed_term': True, 'screened_at_poisson_solution': True},
    'scope': 'Exact graph-polynomial identities, not gravity or a continuum limit; stationarity is supplied as the selection rule',
    'sha256': {str(p.relative_to(BASE)): hashlib.sha256(p.read_bytes()).hexdigest() for p in files if p.exists()},
}
(BASE/'results/graph-action-selection.json').write_text(json.dumps(packet, indent=2)+'\n', encoding='utf-8')
print('Action audit passed: quadratic and quartic survive composition/shift tests; quadraticity remains an extra input.')
