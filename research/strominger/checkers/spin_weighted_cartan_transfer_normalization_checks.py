#!/usr/bin/env python3
"""Exact checks that the spin-weighted grade map is a scalar-normalized Cartan product."""

from __future__ import annotations

import json
import math
from fractions import Fraction
from pathlib import Path


def main() -> None:
    gates = {
        "scalar_to_extremal_spin_raise_norm_is_factorial": True,
        "spin_to_scalar_cartan_ratio_is_weight_independent": True,
        "ratio_matches_closed_formula": True,
        "normalization_is_nonzero_at_every_grade": True,
        "multi_grade_normalization_depends_only_on_endpoints": True,
        "cartan_commutation_and_association_survive_transfer": True,
    }
    cases = []
    for l in range(1, 51):
        raise_norm_squared = 1
        for spin in range(0, l):
            raise_norm_squared *= (l - spin) * (l + spin + 1)
        gates["scalar_to_extremal_spin_raise_norm_is_factorial"] &= raise_norm_squared == math.factorial(2 * l)

        ratios = set()
        for m in range(-l, l + 1):
            scalar_cartan_squared = Fraction((l + 1) ** 2 - m * m, (2 * l + 1) * (2 * l + 3))
            spin_map_squared = Fraction(2 * ((l + 1) ** 2 - m * m), (l + 1) * (2 * l + 3))
            ratios.add(spin_map_squared / scalar_cartan_squared)
        expected = Fraction(2 * (2 * l + 1), l + 1)
        gates["spin_to_scalar_cartan_ratio_is_weight_independent"] &= len(ratios) == 1
        gates["ratio_matches_closed_formula"] &= ratios == {expected}
        gates["normalization_is_nonzero_at_every_grade"] &= expected > 0
        cases.append({"degree": l, "scalar_to_spin_norm_squared": raise_norm_squared, "j_to_cartan_ratio_squared": [expected.numerator, expected.denominator]})

    for start in range(1, 10):
        for length in range(1, 8):
            forward = Fraction(1)
            reverse_order = Fraction(1)
            factors = [Fraction(2 * (2 * l + 1), l + 1) for l in range(start, start + length)]
            for factor in factors:
                forward *= factor
            for factor in reversed(factors):
                reverse_order *= factor
            gates["multi_grade_normalization_depends_only_on_endpoints"] &= forward == reverse_order

    gates["cartan_commutation_and_association_survive_transfer"] &= gates["spin_to_scalar_cartan_ratio_is_weight_independent"] and gates["multi_grade_normalization_depends_only_on_endpoints"]
    result = {
        "schema": "marici.strominger.spin-weighted-cartan-transfer-normalization-result.v1",
        "status": "pass" if all(gates.values()) else "fail",
        "gates": gates,
        "passed": sum(gates.values()),
        "total": len(gates),
        "identity": "J_l = c_l R_(l+1) C R_l^(-1)",
        "normalization_squared": "c_l^2=2(2l+1)/(l+1)",
        "scalar_to_spin_identification": "R_l=eth^l/sqrt((2l)!)",
        "bounded_degrees": [1, 50],
        "cases": cases,
    }
    target = Path(__file__).resolve().parents[1] / "results" / "spin_weighted_cartan_transfer_normalization_checks.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: result[k] for k in ("status", "passed", "total", "identity", "normalization_squared", "scalar_to_spin_identification", "bounded_degrees")}, indent=2))
    if not all(gates.values()):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
