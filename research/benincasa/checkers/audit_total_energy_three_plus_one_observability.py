"""Audit one-step observability of the total-energy 3+1 marked system."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


u, v = sp.symbols("u v")
QUOTIENT = ROOT / "research" / "benincasa" / "marked-wall-quotient-connection.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "total_energy_three_plus_one_observability.json"


def main() -> None:
    packet = json.loads(QUOTIENT.read_text(encoding="utf-8"))
    D = sp.sympify(packet["D"])
    H = sp.sympify(packet["H"])
    replacements = {sp.Symbol("D"): D, sp.Symbol("H"): H}
    axis = {key: sp.sympify(value).subs(replacements) for key, value in packet["u"].items()}
    connection = sp.Matrix(
        [
            [axis["alpha"], 0, 0],
            [axis["beta1"], axis["gamma1"], 0],
            [axis["beta2"], 0, axis["gamma2"]],
        ]
    )
    residue = connection.applyfunc(lambda value: sp.factor(sp.limit(u * value, u, 0)))

    # The second-Rees check sees q0.  The logarithmic quotient check may be
    # represented by its fixed e8 row; any nonzero rescaling gives the same kernel.
    mu = sp.Matrix([[1, 0, 0]])
    lam = sp.Matrix(
        [[
            -(v - 4) / (v * (v - 2) ** 2),
            2 / (v * (v - 2)),
            -2 / (v * (v - 2)),
        ]]
    )
    hidden = sp.Matrix([0, 1, 1])
    transported_check = mu * residue.T
    observability = mu.col_join(lam).col_join(transported_check)

    assert mu * hidden == sp.zeros(1, 1)
    assert lam * hidden == sp.zeros(1, 1)
    transported_hidden = sp.factor((transported_check * hidden)[0])
    determinant = sp.factor(observability.det())
    assert sp.cancel(transported_hidden - v / (2 * (v - 2))) == 0
    assert sp.cancel(determinant - 1 / (v - 2) ** 2) == 0

    cleared = sp.factor(v * (v - 2) ** 2 * lam)
    cleared_observability = mu.col_join(cleared).col_join(transported_check)
    cleared_determinant = sp.factor(cleared_observability.det())
    assert sp.cancel(cleared_determinant - v) == 0

    integral_logarithmic = sp.factor(v * (v - 2) ** 2) * lam
    integral_transport = sp.factor(2 * (v - 2)) * transported_check
    integral_observability = mu.col_join(integral_logarithmic).col_join(integral_transport)
    integral_determinant = sp.factor(integral_observability.det())
    assert integral_determinant == 2 * v * (v - 2)

    invariant_top = sp.Matrix([1, sp.Rational(-1, 2), sp.Rational(-1, 2)])
    assert invariant_top == sp.Matrix([1, 0, 0]) - sp.Rational(1, 2) * hidden

    output = {
        "schema": "marici.benincasa.total_energy_three_plus_one_observability.v1",
        "status": "pass",
        "basis": ["q0", "q1", "q2"],
        "second_rees_check": ["1", "0", "0"],
        "logarithmic_check": [str(sp.factor(value)) for value in lam.tolist()[0]],
        "principal_kernel_generator": ["0", "1", "1"],
        "quotient_connection_residue": [[str(value) for value in row] for row in residue.tolist()],
        "transported_second_rees_check": [str(sp.factor(value)) for value in transported_check.tolist()[0]],
        "transported_hidden_value": str(transported_hidden),
        "observability_determinant": str(determinant),
        "cleared_observability_determinant": str(cleared_determinant),
        "integral_logarithmic_check": [str(sp.factor(value)) for value in integral_logarithmic.tolist()[0]],
        "integral_transport_check": [str(sp.factor(value)) for value in integral_transport.tolist()[0]],
        "integral_observability_determinant": str(integral_determinant),
        "localized_integral_index": 2,
        "invariant_top_lift": ["1", "-1/2", "-1/2"],
        "half_sum_relation": "q0_inv=q0-(q1+q2)/2",
        "generic_rank": 3,
        "localized_locus": "v*(v-2) != 0",
        "exceptional_support": {
            "v=0": "pre-existing signed-energy divisor; requires supported costalk analysis",
            "v=2": "pre-existing coordinate/soft boundary of the chosen chart",
        },
        "scope": "exact consequence of the source-derived quotient connection and Entry 3281 candidate/source-replicated principal covector",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(output, indent=2))


if __name__ == "__main__":
    main()
