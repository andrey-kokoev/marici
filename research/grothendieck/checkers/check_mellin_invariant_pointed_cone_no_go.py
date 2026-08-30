"""Dependency-free exact witness against a fixed Mellin-invariant pointed cone."""


def main():
    # Work in the realification of one complex label line.  At q=1 and
    # t=pi, Mellin transport is the exact half-turn -I.
    label = (1, 0)
    half_turn = ((-1, 0), (0, -1))

    transported = (
        half_turn[0][0] * label[0] + half_turn[0][1] * label[1],
        half_turn[1][0] * label[0] + half_turn[1][1] * label[1],
    )

    checks = [
        ("label_nonzero", label != (0, 0)),
        ("half_turn_is_negative_label", transported == (-1, 0)),
        ("half_turn_squares_to_identity", (-transported[0], -transported[1]) == label),
        ("opposite_rays_are_distinct", transported != label),
        ("cone_lineality_witness_nonzero", label != (0, 0) and transported == (-label[0], -label[1])),
    ]

    for name, passed in checks:
        print(f"{'PASS' if passed else 'FAIL'} {name}")
    passed = sum(ok for _, ok in checks)
    print(f"SUMMARY {passed}/{len(checks)}")
    raise SystemExit(0 if passed == len(checks) else 1)


if __name__ == "__main__":
    main()

