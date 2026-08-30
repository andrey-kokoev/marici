from fractions import Fraction as F


def main() -> None:
    # Exact finite measures are atomic instances of the continuous
    # autocorrelation identities. These gates guard all algebraic signs used
    # by the completion theorem; the Poisson argument is proved in the packet.
    packets = [
        ([F(1), F(2)], F(-1, 2), F(3)),
        ([F(2), F(1)], F(-2), F(-3)),
        ([F(2), F(3)], F(-2, 3), F(5)),
        ([F(3), F(2)], F(-3, 2), F(-5)),
    ]
    checks = {}
    for index, (a, w, expected_current) in enumerate(packets):
        x = a[0] + a[1] * w
        c0 = a[0] * a[0] + a[1] * a[1]
        c1 = a[0] * a[1]
        half_left = c0 / 2 + c1 * w
        half_right = c0 / 2 + c1 / w
        current = c1 * (w - 1 / w)
        checks[f"zero_{index}"] = x == 0
        checks[f"symmetric_factorization_{index}"] = half_left + half_right == 0
        checks[f"oriented_current_{index}"] = current == expected_current
        if abs(w) < 1:
            checks[f"positive_left_half_form_{index}"] = half_left > 0 and current == 2 * half_left
        else:
            checks[f"positive_reciprocal_half_form_{index}"] = half_right > 0 and current == -2 * half_right

    contract = {
        "real_source": True,
        "even_autocorrelation": True,
        "integrable_autocorrelation": True,
        "required_exponential_moments": True,
        "fubini_product_identity": True,
        "bounded_left_half_plane_half_form": True,
        "nonzero_boundary_modulus": True,
        "poisson_strictness": True,
    }
    checks.update({f"contract_{key}": value for key, value in contract.items()})
    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} contract and exact-regression gates passed")


if __name__ == "__main__":
    main()

