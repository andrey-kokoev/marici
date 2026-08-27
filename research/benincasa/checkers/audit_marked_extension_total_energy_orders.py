"""Audit exact total-energy orders of the rank-12 candidate final block."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "research" / "benincasa" / ".tmp_sympy"))

import sympy as sp


u, v = sp.symbols("u v")
CANDIDATE = ROOT / "research" / "benincasa" / "marked-extension-charzero-candidate.json"
RESULT = ROOT / "research" / "benincasa" / "results" / "marked_extension_total_energy_orders.json"


def monomials(degree: int):
    for total in range(degree + 1):
        for u_degree in range(total + 1):
            yield u**u_degree * v ** (total - u_degree)


def expression(coefficients: list[str], degree: int):
    return sum(
        sp.Rational(coefficient) * term
        for coefficient, term in zip(coefficients, monomials(degree))
    )


def u_order(polynomial) -> int:
    terms = sp.Poly(polynomial, u, v).terms()
    return min(monomial[0] for monomial, coefficient in terms if coefficient != 0)


def main() -> None:
    packet = json.loads(CANDIDATE.read_text(encoding="utf-8"))
    records = []
    for entry in packet["entries"]:
        value = sp.cancel(
            expression(entry["numerator"], entry["numerator_degree"])
            / expression(entry["denominator"], entry["denominator_degree"])
        )
        numerator, denominator = sp.fraction(value)
        order = u_order(numerator) - u_order(denominator)
        leading = sp.factor(sp.limit(value / u**order, u, 0))
        records.append(
            {
                "axis": entry["axis"],
                "row": entry["row"],
                "column": entry["column"],
                "u_order": order,
                "leading_coefficient": str(leading),
            }
        )

    order_matrices = {}
    for axis in ("u", "v"):
        order_matrices[axis] = [
            [
                next(
                    record["u_order"]
                    for record in records
                    if record["axis"] == axis
                    and record["row"] == row
                    and record["column"] == column
                )
                for column in range(3)
            ]
            for row in range(4)
        ]

    double = [record for record in records if record["u_order"] == -2]
    assert len(double) == 1
    assert (double[0]["axis"], double[0]["row"], double[0]["column"]) == ("u", 0, 0)
    assert all(record["u_order"] >= -1 for record in records if record is not double[0])

    output = {
        "schema": "marici.benincasa.marked_extension_total_energy_orders.v1",
        "status": "pass",
        "coordinate_convention": "u=E/X1, v=(X1+X2-X3)/X1, X1=1",
        "order_matrices": order_matrices,
        "unique_double_pole": double[0],
        "records": records,
        "scope": "exact theorem about the reconstructed final-block candidate; source comparison is separate",
    }
    RESULT.write_text(json.dumps(output, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: output[key] for key in ("status", "order_matrices", "unique_double_pole")}, indent=2))


if __name__ == "__main__":
    main()
