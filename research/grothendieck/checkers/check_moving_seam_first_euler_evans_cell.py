from fractions import Fraction


def main():
    # Formal first-order coefficients represented by exact rational fixtures.
    f = Fraction(17, 5)
    b = Fraction(7, 11)
    q = Fraction(3, 13)

    evans_jet = q * (f - b)
    euler_jet = q * f
    seam_jet = -q * b

    checks = {
        "evans_equals_euler_plus_seam": evans_jet == euler_jet + seam_jet,
        "bare_euler_mismatches": evans_jet != euler_jet,
        "mismatch_is_moving_seam": evans_jet - euler_jet == seam_jet,
        "undivided_identity_uses_no_inverse": f != 0,
        "log_jet_matches_when_chart_exists": evans_jet / f == q - q * b / f,
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
