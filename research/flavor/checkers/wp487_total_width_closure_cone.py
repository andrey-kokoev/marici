"""Exact sufficient closure cone for WP486 tree-level total widths."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp484 = load("wp484_gauged_connector_frame_lift.json")
wp486 = load("wp486_pole_current_inverse_instrument.json")

# Exact nonempty witness. It is not a selected benchmark: it proves only that
# the preregistered closure inequalities are mutually consistent.
g2 = sp.Integer(1)
h2 = sp.Rational(1, 68)
f2 = sp.Integer(1)  # adjoint amplitude mu squared
s2 = sp.Integer(32)
tau2 = sp.Integer(1)

a = g2 * f2
d = h2 * (4 * f2 + 2 * s2)
b2 = 4 * g2 * h2 * f2**2
disc = sp.factor((a - d) ** 2 + 4 * b2)
p = sp.simplify((a + d - sp.sqrt(disc)) / 2)
r = sp.simplify((a + d + sp.sqrt(disc)) / 2)
q = 3 * g2 * f2
vector_mass_squares = [p, q, r]

# Requiring every possible daughter mass to exceed half the heaviest parent
# closes fermion-pair, scalar-pair, vector-pair, and vector-scalar two-body
# channels without fitting a coupling selection rule.
vector_pair_margins = {
    f"4m{i + 1}^2_minus_m{j + 1}^2": sp.simplify(4 * left - right)
    for i, left in enumerate(vector_mass_squares)
    for j, right in enumerate(vector_mass_squares)
    if i != j
}
threshold_margins = {
    f"4tau^2_minus_m{i + 1}^2": sp.simplify(4 * tau2 - mass_squared)
    for i, mass_squared in enumerate(vector_mass_squares)
}

Q, m_minus, m_plus, C, D, T = sp.symbols(
    "Q m_minus_squared m_plus_squared C D T", positive=True
)
g_f_squared = sp.factor(-3 * C * D / (Q - 3 * T))
w_minus = sp.factor((m_plus - Q / 3) / (m_plus - m_minus))
w_plus = sp.factor((Q / 3 - m_minus) / (m_plus - m_minus))
total_fractional_widths_on_cone = {
    "mixed_minus": sp.factor(g_f_squared * w_minus / (4 * sp.pi)),
    "mixed_plus": sp.factor(g_f_squared * w_plus / (4 * sp.pi)),
    "quintet": sp.factor(g_f_squared / (4 * sp.pi)),
}

checks = {
    "wp484_dependency_passed": wp484["passed"],
    "wp486_dependency_passed": wp486["passed"],
    "witness_triplet_diagonal_entries_match": a == d,
    "witness_mixed_poles_are_exact": p == 1 - 1 / sp.sqrt(17) and r == 1 + 1 / sp.sqrt(17),
    "all_vector_pair_margins_are_positive": all(value > 0 for value in vector_pair_margins.values()),
    "all_heavy_threshold_margins_are_positive": all(value > 0 for value in threshold_margins.values()),
    "closure_cone_is_strictly_nonempty": min(vector_pair_margins.values()) > 0 and min(threshold_margins.values()) > 0,
    "mixed_fractional_width_sum_rule_survives": sp.simplify(
        total_fractional_widths_on_cone["mixed_minus"]
        + total_fractional_widths_on_cone["mixed_plus"]
        - total_fractional_widths_on_cone["quintet"]
    ) == 0,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP487",
    "domain": "WP486 calibrated pole-current domain at tree level, with six effectively massless quarks and a declared minimum nonquark matter/scalar threshold tau",
    "tree_level_two_body_channel_classes": [
        "quark-antiquark",
        "vector-vector",
        "vector-physical-scalar",
        "physical-scalar pair",
        "vectorlike-messenger pair",
    ],
    "sufficient_closure_cone": {
        "vector_condition": "4 m_i^2 > m_j^2 for every ordered pair of distinct vector poles",
        "nonvector_condition": "4 tau^2 > m_i^2 for every vector pole, where tau is the minimum physical scalar or vectorlike-messenger mass",
        "interpretation": "every nonquark daughter is heavier than half every possible vector parent",
    },
    "exact_nonempty_witness": {
        "g_F_squared": str(g2),
        "g_P_squared": str(h2),
        "mu_squared": str(f2),
        "s_squared": str(s2),
        "tau_squared": str(tau2),
        "mixed_minus_squared": str(p),
        "quintet_squared": str(q),
        "mixed_plus_squared": str(r),
        "vector_pair_margins": {name: str(value) for name, value in vector_pair_margins.items()},
        "threshold_margins": {name: str(value) for name, value in threshold_margins.items()},
    },
    "total_fractional_widths_on_cone": {
        name: str(value) for name, value in total_fractional_widths_on_cone.items()
    },
    "classification": "Exact sufficient tree-level total-width closure theorem with nonempty source domain; no claim that the current source selects or occupies the cone.",
    "selector": False,
    "rigidifier": False,
    "instrument": "threshold-resolved pole/current experiment specified by WP486 plus lower bounds on every nonquark daughter mass",
    "smallest_exact_falsifier": "A measured or source-derived daughter mass at or below half a vector pole falsifies this coupling-independent closure certificate; it then requires a channel-specific coupling audit and does not alone prove a nonzero decay.",
    "remaining_gate": "Derive the connector-scalar and both messenger-stage masses from the same source coefficients and prove the closure inequalities on the selected trajectory; loop-induced and off-shell corrections require a separately declared perturbative order and resolution.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp487_total_width_closure_cone.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
