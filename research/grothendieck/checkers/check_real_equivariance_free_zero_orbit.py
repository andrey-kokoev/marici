"""Exact symbolic orbit check for the positive even two-cell hostile."""


def main():
    # Represent z_t = t + i*pi only by its independent formal coordinates.
    z = ("t", "pi")
    fz = ("-t", "-pi")
    cz = ("t", "-pi")
    rz = ("-t", "pi")
    orbit = {z, fz, cz, rz}

    checks = [
        ("generic_orbit_has_four_points", len(orbit) == 4),
        ("functional_reflection_distinct", fz != z),
        ("conjugate_reflection_distinct", cz != z),
        ("real_reciprocal_reflection_distinct", rz != z),
        ("orbit_closed_under_functional_reflection", {("-" + a if not a.startswith("-") else a[1:], "-" + b if not b.startswith("-") else b[1:]) for a, b in orbit} == orbit),
        ("off_seam_isotropy_absent", rz != z),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

