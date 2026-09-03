from __future__ import annotations

import json

import sympy as sp


def main() -> None:
    t, h = sp.symbols("t h", real=True, positive=True)
    s = 35 * t**4 - 84 * t**5 + 70 * t**6 - 20 * t**7
    derivatives = [sp.factor(sp.diff(s, t, order)) for order in range(1, 4)]
    for derivative in derivatives:
        assert derivative.subs(t, 0) == 0
        assert derivative.subs(t, 1) == 0
    assert s.subs(t, 0) == 0
    assert s.subs(t, 1) == 1

    second = derivatives[1]
    third = derivatives[2]
    critical = [root for root in sp.solve(third, t) if root.is_real and 0 < root < sp.Rational(1, 2)]
    assert len(critical) == 1
    positive_maximum = sp.simplify(second.subs(t, critical[0]))
    assert positive_maximum > 0
    third_l1 = sp.simplify(4 * positive_maximum)

    # Two transitions per window and two complementary windows.
    total_partition_third_l1 = sp.simplify(4 * third_l1 / h**2)
    fourier_leakage_bound = sp.simplify(sp.pi * total_partition_third_l1 / 6)

    result = {
        "schema": "marici.voevodsky.septic-smoothstep-partition.v1",
        "status": "explicit_C3_partition_profile_verified",
        "profile": str(s),
        "endpoint_derivatives_through_order_three_vanish": True,
        "interior_second_derivative_maximizer": str(critical[0]),
        "second_derivative_positive_maximum": str(positive_maximum),
        "single_transition_third_derivative_L1": str(third_l1),
        "scaled_single_transition_L1": str(sp.simplify(third_l1 / h**2)),
        "two_window_two_transition_total_L1": str(total_partition_third_l1),
        "fourier_commutator_leakage_bound": str(fourier_leakage_bound),
        "proper_interval_subordination_possible": True,
        "overlap_width_materialized": False,
        "coordinate_transfer_normalization_materialized": False,
        "next_gate": "choose interval cover and overlap width, then compare partition choices by bounded change",
        "passed": True,
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
