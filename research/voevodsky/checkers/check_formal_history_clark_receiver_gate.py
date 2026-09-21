"""Exact finite probes for the full-formal-history receiver obstruction.

The all-order continuity/positivity theorems are proved in the note;
finite coefficient checks below are not proofs of those theorems.
"""
import importlib.util
import json
from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[3]


def load(name, relative):
    spec = importlib.util.spec_from_file_location(name, ROOT / relative)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


history = load("full_history", "research/grothendieck/universal_history.py")
windows = load("source_windows", "research/grothendieck/theta_interval_signature.py")
Jet = history.Jet


def route_windows(route):
    mask = 0
    result = []
    for j in route:
        assert not mask & (1 << j)
        target = mask | (1 << j)
        result.append({k: 1 for k in range(windows.POSITION[mask], windows.POSITION[target])})
        mask = target
    return result


order = 6
one = Jet.unit(order)
left = history.record(order, route_windows((0, 1)))
right = history.record(order, route_windows((1, 0)))
r = left.inverse() * right
d = r + one.scale(-1)
d2, d3 = d * d, d * d * d
assert min(map(len, d.terms)) == 2
assert min(map(len, d2.terms)) == 4
assert min(map(len, d3.terms)) == 6
assert not d3.project(4).terms
assert len(d3.terms) == 27
assert d3.terms[(0, 1, 0, 1, 0, 1)] == -1
assert (d2 * r + d2.scale(-1)).terms == d3.terms
# Match the previously used arithmetic four-jet, not a surrogate input.
for word, expected in [((0, 1), left), ((1, 0), right)]:
    old = windows.observe_route(word)
    old_terms = {w: coefficient for row in old for w, coefficient in row.items()}
    assert expected.project(4).terms == old_terms

# Relative one-variable degree: this is degree in d, not chamber degree.
N = 8
unit = Jet.unit(N)
x = Jet(N, {(0,): 1})
r_relative = unit + x
x_star = r_relative.inverse() + unit.scale(-1)


def clean(jet):
    return Jet(jet.order, {w: sp.expand(c) for w, c in jet.terms.items()})


def power(jet, n):
    result = Jet.unit(jet.order)
    for _ in range(n):
        result = clean(result * jet)
    return result


def star(jet):
    result = Jet(N, {})
    for word, coefficient in jet.terms.items():
        # One generator, so reversal of each word leaves its spelling fixed.
        result = clean(result + power(x_star, len(word)).scale(sp.conjugate(coefficient)))
    return result


assert star(x_star).terms == x.terms
assert clean(star(r_relative) * r_relative).terms == unit.terms
b = clean(x_star * x)
assert star(b).terms == b.terms
T = sp.Symbol("T", real=True)
square_root = Jet(N, {})
for k in range(N + 1):
    square_root = clean(square_root + power(b, k).scale(sp.binomial(sp.Rational(1, 2), k) * (-T)**k))
assert star(square_root).terms == square_root.terms
assert clean(star(square_root) * square_root).terms == clean(unit + b.scale(-T)).terms

result = {
    "schema": "marici.voevodsky.formal-history-clark-receiver-gate.v1",
    "passed": True,
    "checks": {
        "actual_arithmetic_windows_match_prior_four_jets": True,
        "comparison_leading_degree": 2,
        "d_squared_leading_degree": 4,
        "d_cubed_leading_degree": 6,
        "d_cubed_degree_six_nonzero_terms": len(d3.terms),
        "four_jet_kills_d_cubed": True,
        "span_one_d_d_squared_not_invariant_at_order_six": True,
        "relative_involution_through_degree_eight": True,
        "comparison_unitary_for_relative_formal_involution": True,
        "selfadjoint_square_root_identity_for_symbolic_real_T": True,
    },
    "scope": "Exact finite algebra checks; no construction of a Clark receiver, positivity certificate, or proof by finite testing of the all-order formal no-go theorem.",
}
destination = ROOT / "research/voevodsky/results/formal-history-clark-receiver-gate.json"
destination.parent.mkdir(parents=True, exist_ok=True)
destination.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
