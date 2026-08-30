from fractions import Fraction


def main():
    # Exact fixtures for F, the two initial windows, and the transported
    # second windows.  Both decompositions represent one B_pq.
    f = Fraction(19, 7)
    bp = Fraction(2, 5)
    bq = Fraction(3, 8)
    bq_after_p = Fraction(11, 30)
    bpq = bp + bq_after_p
    bp_after_q = bpq - bq
    rp = Fraction(2, 11)
    rq = Fraction(3, 13)
    a = Fraction(5, 17)
    b = Fraction(7, 19)

    direct_corner = rp * rq * (f - bpq)
    p_then_q = rq * (rp * (f - bp) - rp * bq_after_p)
    q_then_p = rp * (rq * (f - bq) - rq * bp_after_q)

    endpoint = (
        f
        + a * rp * (f - bp)
        + b * rq * (f - bq)
        + a * b * direct_corner
    )
    bare_euler = (1 + a * rp) * (1 + b * rq) * f
    boundary = -a * rp * bp - b * rq * bq - a * b * rp * rq * bpq

    checks = {
        "p_then_q_equals_direct": p_then_q == direct_corner,
        "q_then_p_equals_direct": q_then_p == direct_corner,
        "transported_windows_concatenate": bp + bq_after_p == bq + bp_after_q == bpq,
        "endpoint_equals_euler_plus_boundary": endpoint == bare_euler + boundary,
        "shared_corner_is_nonzero": a * b * rp * rq * bpq != 0,
    }

    for name, passed in checks.items():
        print(f"{name}: {'PASS' if passed else 'FAIL'}")
    print(f"summary: {sum(checks.values())}/{len(checks)} checks passed")
    raise SystemExit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
