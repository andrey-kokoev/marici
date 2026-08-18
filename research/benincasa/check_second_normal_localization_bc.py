"""Labelled second-normal Beck--Chevalley audit for q_G12 localization."""

import json
from pathlib import Path

import sympy as sp


nu1, nu2, nu3 = sp.symbols("nu1 nu2 nu3")
x1, x2, x3, c = sp.symbols("X1 X2 X3 y12")
q_g12 = x1 + x2 + x3 + c
labels = {
    "nu1*nu2": nu1 * nu2,
    "nu1*nu3": nu1 * nu3,
    "nu2*nu3": nu2 * nu3,
}


def labelled_grade(expr, left, right):
    """Coefficient in I^2/I^3 of one square-free labelled monomial."""
    return sp.diff(sp.diff(expr, left), right).subs({nu1: 0, nu2: 0, nu3: 0})


normal_pairs = [(nu1, nu2), (nu1, nu3), (nu2, nu3)]
assert all(sp.diff(q_g12, nu) == 0 for nu in (nu1, nu2, nu3))

commutators = {}
for (name, monomial), (left, right) in zip(labels.items(), normal_pairs):
    route_localize_then_grade = labelled_grade(monomial / q_g12, left, right)
    route_grade_then_localize = labelled_grade(monomial, left, right) / q_g12
    commutator = sp.cancel(route_localize_then_grade - route_grade_then_localize)
    assert commutator == 0
    commutators[name] = {
        "localize_then_grade": str(route_localize_then_grade),
        "grade_then_localize": str(route_grade_then_localize),
        "commutator": str(commutator),
    }

result = {
    "schema": "marici.second-normal-localization-bc.v1",
    "q_G12": str(q_g12),
    "normal_derivatives_of_q_G12": {
        str(nu): str(sp.diff(q_g12, nu)) for nu in (nu1, nu2, nu3)
    },
    "labelled_generators": list(labels),
    "commutators": commutators,
    "beck_chevalley_commutator_rank": 0,
    "Q_valuation_test_admissible": False,
    "reason_Q_test_inadmissible": "the typed commutator is identically zero",
    "scope": "twisted de Rham chain-level localization and I^2/I^3 associated grade",
}

out = Path(__file__).with_name("second-normal-localization-bc.json")
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
