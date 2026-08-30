"""Exact scalar-channel audit of the observer-difference seam cocycle."""

from fractions import Fraction


def main():
    q = Fraction(1, 3)
    before_seam = Fraction(1)
    after_seam = Fraction(-1)
    f = before_seam + after_seam
    boundary_window = before_seam

    moving_observer = q * f
    fixed_observer = q * (f - boundary_window)
    observer_difference = fixed_observer - moving_observer

    checks = [
        ("hostile_scalar_zero", f == 0),
        ("boundary_window_nonzero", boundary_window == 1),
        ("moving_observer_zero", moving_observer == 0),
        ("fixed_observer_detects_hidden_state", fixed_observer == -q),
        ("difference_equals_seam_cocycle", observer_difference == -q * boundary_window),
        ("hostile_satisfies_universal_identity", fixed_observer == moving_observer - q * boundary_window),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

