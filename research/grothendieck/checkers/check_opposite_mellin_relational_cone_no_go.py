"""Exact real-coordinate witness for opposite-Mellin relational sign reversal."""


def real_pairing(a, b):
    # Complex numbers as (real, imaginary); Re(a * conjugate(b)).
    return a[0] * b[0] + a[1] * b[1]


def quarter_turn(v):
    return (-v[1], v[0])


def inverse_quarter_turn(v):
    return (v[1], -v[0])


def main():
    a = (1, 0)
    b = (1, 0)
    before = real_pairing(a, b)

    # q=1 and t=pi/2: direct rotates by +pi/2, dual by -pi/2.
    at = quarter_turn(a)
    bt = inverse_quarter_turn(b)
    after = real_pairing(at, bt)

    checks = [
        ("initial_relation_acute", before == 1),
        ("direct_quarter_turn", at == (0, 1)),
        ("dual_inverse_quarter_turn", bt == (0, -1)),
        ("relative_phase_is_half_turn", after == -1),
        ("acute_sign_reverses", after == -before),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

