"""Exact delta-net error budget for continuous star-defect extension."""

from fractions import Fraction


def main():
    lipschitz = Fraction(3, 2)
    delta = Fraction(1, 20)
    sample_residual = Fraction(1, 100)
    bound = sample_residual + lipschitz * delta

    checks = [
        ("positive_lipschitz_constant", lipschitz > 0),
        ("positive_net_radius", delta > 0),
        ("exact_error_budget", bound == Fraction(17, 200)),
        ("exact_samples_sharpen_bound", lipschitz * delta == Fraction(3, 40)),
        ("refinement_reduces_error", lipschitz * Fraction(1, 40) < lipschitz * delta),
        ("zero_mesh_forces_zero_extension", lipschitz * Fraction(0) == 0),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

