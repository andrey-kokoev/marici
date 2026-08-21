"""Exact one-mode Unruh--DeWitt instrument pilot.

The full UDW source supplies detector + field interaction.  This bounded pilot
takes the resonant single-excitation sector, where the resulting unitary is an
excitation swap with exact rational cosine/sine 3/5 and 4/5.
"""
import json
from pathlib import Path
import sympy as sp

I = sp.I
c, s = sp.Rational(3, 5), sp.Rational(4, 5)
K0 = sp.Matrix([[1, 0], [0, c]])
K1 = sp.Matrix([[0, -I*s], [0, 0]])
eye = sp.eye(2)
dag = lambda a: a.conjugate().T

rho00, rho01, rho10, rho11 = sp.symbols("rho00 rho01 rho10 rho11")
rho = sp.Matrix([[rho00, rho01], [rho10, rho11]])
branches = [sp.simplify(K*rho*dag(K)) for K in (K0, K1)]
effects = [sp.simplify(dag(K)*K) for K in (K0, K1)]
channel = sp.simplify(sum(branches, sp.zeros(2)))

# Formal Lüders completion of the click effect has the same record probability
# but a different successor state.
L1 = sp.Matrix([[0, 0], [0, s]])
luders_click = sp.simplify(L1*rho*dag(L1))
physical_click = branches[1]

# Phase-rephasing covariance: the instrument map is unchanged because the
# only changed Kraus operator acquires a scalar phase.
z = sp.symbols("z", nonzero=True)
R = sp.diag(1, z)
Rinv = sp.diag(1, 1/z)
K0p = sp.simplify(R*K0*Rinv)
K1p = sp.simplify(R*K1*Rinv)
phase_covariance = sp.simplify(K0p-K0) == sp.zeros(2) and sp.simplify(K1p-z**-1*K1) == sp.zeros(2)

# Two sequential uses. Outcome words are ordered second-after-first.
seq = {(j, i): sp.simplify(Kj*Ki) for i, Ki in enumerate((K0, K1))
                                      for j, Kj in enumerate((K0, K1))}
seq_complete = sp.simplify(sum((dag(K)*K for K in seq.values()), sp.zeros(2)))

checks = {
    "kraus_completeness": sp.simplify(sum(effects, sp.zeros(2))-eye) == sp.zeros(2),
    "branch_sum_trace_preserving": sp.simplify(sp.trace(channel)-sp.trace(rho)) == 0,
    "click_probability": sp.simplify(sp.trace(physical_click)-s**2*rho11) == 0,
    "same_effect_as_luders": sp.simplify(dag(L1)*L1-effects[1]) == sp.zeros(2),
    "source_update_differs_from_luders": sp.simplify(physical_click-luders_click) != sp.zeros(2),
    "phase_rephasing_descent": phase_covariance,
    "sequential_completeness": sp.simplify(seq_complete-eye) == sp.zeros(2),
    "double_click_forbidden_single_excitation": seq[(1, 1)] == sp.zeros(2),
    "coarse_forget_equals_branch_sum": channel == sp.simplify(branches[0]+branches[1]),
}
assert all(checks.values())

def mat(m):
    return [[str(sp.simplify(x)) for x in m.row(i)] for i in range(m.rows)]

result = {
    "schema": "marici.udw-one-mode-source-instrument.v1",
    "source": {
        "paper": "Suryaatmadja, Cong, Mann, arXiv:2205.14739",
        "interaction_equation": "H_D=lambda chi mu_D tensor phi[x_D]",
        "unitary_equation": "U=T exp(-i integral H_I dt)",
        "preparation": "detector ground state",
        "pointer": "detector energy basis",
    },
    "bounded_specialization": {
        "scope": "resonant one-field-mode, single-excitation sector",
        "c": str(c), "s": str(s),
        "status": "declared finite specialization; not a full-field equivalence theorem",
    },
    "kraus": {"no_click": mat(K0), "click": mat(K1)},
    "effects": {"no_click": mat(effects[0]), "click": mat(effects[1])},
    "nonselective_channel": mat(channel),
    "physical_click_successor": mat(physical_click),
    "formal_luders_click_successor": mat(luders_click),
    "checks": checks,
    "verdict": (
        "The declared UDW interaction supplies the first source-selected "
        "Marici instrument in a bounded physical specialization. Its click "
        "probability agrees with the effect algebra, but its successor state "
        "is amplitude damping to the field vacuum, not the formal Luders "
        "successor. Records do not determine updates."
    ),
}
out=Path(__file__).parents[1]/"results"/"udw_one_mode_source_instrument.json"
out.write_text(json.dumps(result, indent=2)+"\n", encoding="utf-8")
print(json.dumps(result, indent=2))
