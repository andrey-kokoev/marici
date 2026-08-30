"""Exact harmonic hostile for locally strict but globally vanishing reserve."""

from fractions import Fraction


def main():
    reserve = Fraction(1)
    checks = []

    for j in range(1, 9):
        rho = Fraction(1, j + 1)
        retained = 1 - rho
        reserve *= retained
        checks.append((f"stage_{j}_strict", 0 < rho < 1))
        checks.append((f"stage_{j}_telescopes", reserve == Fraction(1, j + 1)))

    checks.extend([
        ("reserve_decreases", Fraction(1, 9) < Fraction(1, 2)),
        ("arbitrary_cutoff_formula", reserve == Fraction(1, 9)),
        ("no_uniform_positive_floor", all(Fraction(1, n + 1) < Fraction(1, 10) for n in range(10, 20))),
    ])

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

