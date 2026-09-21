"""Exact ordered-Volterra receiver fixtures; not a completed Clark metric test."""
import importlib.util
import json
from pathlib import Path
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
spec = importlib.util.spec_from_file_location("history", ROOT / "research/grothendieck/universal_history.py")
history = importlib.util.module_from_spec(spec)
spec.loader.exec_module(history)
Jet = history.Jet
N = 8
one = Jet.unit(N)
u, v, w = [Jet(N, {(i,): 1}) for i in range(3)]


def ordered(a):
    # Exact relation T_i T_j=0 for i>j on disjoint increasing shells.
    return Jet(N, {word: c for word, c in a.terms.items()
                   if all(i <= j for i, j in zip(word, word[1:]))})


def mul(a, b):
    return ordered(a * b)


left = mul(one + u, one + v + w)
right = mul(one + u + v, one + w)
r = mul(ordered(left.inverse()), right)
d = r + one.scale(-1)
A = mul(u, (one + u).inverse())
B = mul(v, (one + v).inverse())
formula = mul(B, w) + mul(mul(A, v), one + w).scale(-1)
assert d.terms == formula.terms
square = mul(d, d)
assert square.terms == mul(mul(mul(A, v), B), w).scale(-1).terms
assert square.terms
assert not mul(square, d).terms
assert mul(left, r).terms == right.terms

# Exact piecewise functions on three consecutive unit shells, with f_i=1.
# Independent direct Volterra evaluation verifies the closed-form columns.
x, t = s.symbols("x t", real=True)
zero = s.Integer(0)
vacuum = [s.Integer(1)] * 3


def op(i, pieces, resolvent_increment=False):
    out = []
    for j in range(3):
        if j > i:
            out.append(zero)
            continue
        lower = x if j == i else s.Integer(i)
        kernel = s.exp(-(t - lower)) if resolvent_increment else 1
        out.append(s.simplify(s.integrate(kernel * pieces[i].subs(x, t), (t, lower, i + 1))))
    return out


def add(a, b, scale=1):
    return [s.simplify(p + scale * q) for p, q in zip(a, b)]


def D(pieces):
    first = op(1, op(2, pieces), True)
    second = op(0, op(1, add(pieces, op(2, pieces))), True)
    return add(first, second, -1)


col1 = D(vacuum)
col2 = D(col1)
col3 = D(col2)
expected1 = [-1 - s.exp(-1) + 2*s.exp(x-1), 1-s.exp(x-2), zero]
expected2 = [-s.exp(-1)*(1-s.exp(x-1)), zero, zero]
assert all(s.simplify(a-b) == 0 for a, b in zip(col1, expected1))
assert all(s.simplify(a-b) == 0 for a, b in zip(col2, expected2))
assert col3 == [zero]*3
columns = [vacuum, col1, col2]
Q = s.Matrix(3, 3, lambda i, j: s.simplify(sum(
    s.integrate(columns[i][k]*columns[j][k], (x, k, k+1)) for k in range(3))))
U = s.Matrix([[1, 0, 0], [1, 1, 0], [0, 1, 1]])
residual = s.simplify(U.T * Q * U - Q)
assert s.simplify(residual[1, 2] - Q[2, 2]) == 0
expected_norm = (-s.exp(2)+4*s.E-1)/(2*s.exp(4))
assert s.simplify(Q[2, 2] - expected_norm) == 0
assert Q[2, 2] != 0

result = {
    "schema": "marici.voevodsky.ordered-volterra-history-receiver.v1",
    "passed": True,
    "checks": {
        "ordered_quotient_comparison_formula_through_degree_eight": True,
        "ordered_quotient_nonzero_comparison_square": True,
        "ordered_quotient_comparison_cube_zero": True,
        "direct_piecewise_volterra_columns": True,
        "exact_positive_metric_invariance_residual": True,
    },
    "fixture_Q": [[str(Q[i,j]) for j in range(3)] for i in range(3)],
    "fixture_residual_12_equals_norm_d_squared_vacuum_squared": str(expected_norm),
    "scope": "Exact quotient jets and constant-forcing Volterra fixture. All-order boundedness and source-faithfulness statements are arguments in the note; this is not the prescribed completed Clark form or a positivity test for its kernel.",
}
p = ROOT / "research/voevodsky/results/ordered-volterra-history-receiver.json"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
