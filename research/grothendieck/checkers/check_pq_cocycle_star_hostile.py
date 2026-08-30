"""Exact two-atom hostile: scalar nullity and seam composition without star equality."""

from fractions import Fraction


def main():
    # Exact exponential values at z0 = pi + i log 2.
    exp_i_z = Fraction(-1, 2)
    exp_minus_i_z = Fraction(-2)
    exp_minus_i_conj_z = Fraction(-1, 2)

    scalar = 1 + 2 * exp_i_z
    reciprocal_interval = 1 + 2 * exp_minus_i_z
    adjoint_interval = 1 + 2 * exp_minus_i_conj_z
    star_defect = reciprocal_interval - adjoint_interval

    # Universal two-window composition in an abstract split: left + right.
    left = Fraction(1)
    right = 2 * exp_i_z
    composed = left + right

    checks = [
        ("positive_source_weights", 1 > 0 and 2 > 0),
        ("off_seam_scalar_zero", scalar == 0),
        ("two_window_composition_holds", composed == scalar),
        ("reciprocal_interval_value", reciprocal_interval == -3),
        ("adjoint_interval_value", adjoint_interval == 0),
        ("star_defect_nonzero", star_defect == -3),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

