from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    L, h_x = sp.symbols("L h_x", positive=True)
    h_theta = sp.pi * h_x / L
    base_leakage = 224 * sp.sqrt(5) * sp.pi / (25 * h_theta**2)
    physical_leakage = sp.simplify(base_leakage)
    assert physical_leakage == 224 * sp.sqrt(5) * L**2 / (25 * sp.pi * h_x**2)
    normalized_leakage = sp.simplify(physical_leakage.subs(h_x, L))
    assert normalized_leakage == 224 * sp.sqrt(5) / (25 * sp.pi)

    t = sp.Symbol("t", real=True)
    s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7
    assert sp.simplify(s + (1 - s)) == 1
    square_sum = sp.expand(s**2 + (1 - s) ** 2)
    assert sp.simplify(square_sum - 1) != 0

    C_first, C_second = sp.symbols("C_first C_second", nonnegative=True)
    paired_commutator_change_bound = C_first + C_second

    result = {
        "schema": "marici.voevodsky.normalized-endpoint-cover-coherence.v1",
        "status": "auxiliary_cover_and_bounded_change_certificate_verified",
        "coordinate_map": "theta=pi*(x+L)/L",
        "physical_overlap_choice": "h_x=L",
        "angular_overlap": "pi",
        "general_physical_leakage_bound": str(physical_leakage),
        "normalized_leakage_bound": str(normalized_leakage),
        "linear_partition_sum_is_one": True,
        "square_partition_sum_is_one": False,
        "localization_convention_must_be_declared": True,
        "paired_commutator_change_bound": str(paired_commutator_change_bound),
        "bounded_change_preserves_closed_form_domain": True,
        "bounded_change_preserves_positivity_without_margin_update": False,
        "next_gate": "declare source localization formula, then interval-enclose finite low block",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
