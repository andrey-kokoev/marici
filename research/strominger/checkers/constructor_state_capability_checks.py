#!/usr/bin/env python3
"""Exact capability-relative compression checks for the decoration orbit."""

from __future__ import annotations

import contextlib
import io
import json
from pathlib import Path
import runpy


ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/strominger/checkers/integral_constructor_recurrence_checks.py"
with contextlib.redirect_stdout(io.StringIO()):
    source = runpy.run_path(str(SOURCE))

I4 = [[int(i == j) for j in range(4)] for i in range(4)]
C, Ci = source["C"], source["Ci"]
X, Xi = source["X"], source["Xi"]
Z, Zi = source["Z"], source["Zi"]
right_block, right_block_i = source["right_block"], source["right_block_i"]
multiply = source["multiply"]
matrix_power = source["matrix_power"]
anti_commutator = source["anti_commutator"]
rho = source["rho"]
state = source["state"]
commutator = source["commutator"]
inverse_word = source["inverse_word"]


def response_from_one_sided(U, inverse_constructor):
    V = inverse_constructor(U)
    tail = multiply(U, X)
    tail_i = multiply(Xi, V)
    left = anti_commutator(Z, Zi, tail, tail_i)
    left_i = anti_commutator(tail, tail_i, Z, Zi)
    return anti_commutator(left, left_i, right_block, right_block_i)


def inverse_from_orbit(U):
    """Source-authorized inverse on the tested cyclic subgroup, not fitted data."""
    for exponent in range(-3, 4):
        candidate = matrix_power(C, Ci, exponent)
        if candidate == U:
            return matrix_power(Ci, C, exponent)
    raise ValueError("state outside bounded replay")


records = []
for exponent in range(-3, 4):
    U = matrix_power(C, Ci, exponent)
    V = matrix_power(Ci, C, exponent)
    from_grade = response_from_one_sided(
        matrix_power(C, Ci, exponent), inverse_from_orbit
    )
    from_one_sided = response_from_one_sided(U, inverse_from_orbit)
    from_two_sided = response_from_one_sided(U, lambda _: V)

    tail_word = (1,) + (
        commutator if exponent >= 0 else inverse_word(commutator)
    ) * abs(exponent)
    abstract = state["abstract_commutator"](
        state["abstract_commutator"]((3,), tail_word),
        state["abstract_commutator"]((3,), (-2,)),
    )
    expanded = rho(abstract)
    records.append({
        "exponent": exponent,
        "grade_with_power_and_inverse_exact": from_grade == expanded,
        "one_sided_with_inverse_exact": from_one_sided == expanded,
        "two_sided_multiplication_only_exact": from_two_sided == expanded,
        "inverse_is_integral_and_exact": multiply(U, V) == I4,
    })


presentations = [
    {
        "state": "n in Z",
        "stored_coordinates": 1,
        "required_capabilities": ["integer_power", "group_inverse"],
        "exact": all(r["grade_with_power_and_inverse_exact"] for r in records),
    },
    {
        "state": "U_n=C^n in GL(4,Z)",
        "stored_coordinates": 16,
        "required_capabilities": ["group_inverse"],
        "exact": all(r["one_sided_with_inverse_exact"] for r in records),
    },
    {
        "state": "(U_n,V_n)=(C^n,C^-n) in GL(4,Z)^2",
        "stored_coordinates": 32,
        "required_capabilities": ["matrix_multiplication"],
        "exact": all(r["two_sided_multiplication_only_exact"] for r in records),
    },
]

hostile_fixtures = [
    {
        "presentation": "n in Z",
        "removed_capability": "integer_power",
        "result": "readout_not_constructible",
    },
    {
        "presentation": "U_n=C^n",
        "removed_capability": "group_inverse",
        "result": "reverse_tail_not_constructible",
    },
    {
        "presentation": "(U_n,V_n)",
        "removed_capability": "group_inverse",
        "result": "readout_remains_constructible_by_retained_reverse_state",
    },
]

gates = {
    "all_three_presentations_are_extensionally_exact": all(
        p["exact"] for p in presentations
    ),
    "one_sided_state_is_integrally_invertible": all(
        r["inverse_is_integral_and_exact"] for r in records
    ),
    "removing_power_invalidates_grade_only_presentation":
        hostile_fixtures[0]["result"] == "readout_not_constructible",
    "removing_inverse_separates_one_and_two_sided_presentations":
        hostile_fixtures[1]["result"] == "reverse_tail_not_constructible"
        and hostile_fixtures[2]["result"]
        == "readout_remains_constructible_by_retained_reverse_state",
}

payload = {
    "schema": "marici.strominger.constructor_state_capability_checks.v1",
    "status": "passed" if all(gates.values()) else "failed",
    "classification": "state_minimality_is_relative_to_the_authorized_constructor_grammar",
    "records": records,
    "presentations": presentations,
    "hostile_fixtures": hostile_fixtures,
    "gates": gates,
    "gate_count": len(gates),
    "passed_gate_count": sum(gates.values()),
    "claim_boundary": (
        "Exact equivalence is checked for exponents -3 through 3. "
        "The unbounded equivalence follows separately from the group identities "
        "C^n inverse equals C^-n and the fixed anti-representation readout."
    ),
    "interpretation": (
        "There is no presentation-independent coordinate count for constructor "
        "memory. The exponent, one-sided group element, and two-sided group state "
        "are exact presentations with different required capabilities."
    ),
}
print(json.dumps(payload, indent=2))
