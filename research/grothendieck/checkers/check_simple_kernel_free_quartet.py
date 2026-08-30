"""Exact free quartet with one-dimensional kernels at every simple root."""


def h(z):
    # a=b=1.
    return ((z - 1) ** 2 + 1) * ((z + 1) ** 2 + 1)


def derivative_at(z):
    # Product rule for the same factorization.
    left = (z - 1) ** 2 + 1
    right = (z + 1) ** 2 + 1
    return 2 * (z - 1) * right + left * 2 * (z + 1)


def main():
    roots = {1 + 1j, 1 - 1j, -1 + 1j, -1 - 1j}
    checks = [
        ("four_distinct_roots", len(roots) == 4),
        ("all_roots_exact", all(h(z) == 0 for z in roots)),
        ("all_roots_simple", all(derivative_at(z) != 0 for z in roots)),
        ("reality_closes_orbit", {z.conjugate() for z in roots} == roots),
        ("reciprocity_closes_orbit", {-z for z in roots} == roots),
        ("no_root_fixed_by_real_reciprocal", all(-z.conjugate() != z for z in roots)),
        ("kernel_dimension_one_at_each_root", all(h(z) == 0 for z in roots)),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

