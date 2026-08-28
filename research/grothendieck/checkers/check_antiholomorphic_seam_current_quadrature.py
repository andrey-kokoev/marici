from fractions import Fraction as F


def add(z, w):
    return z[0] + w[0], z[1] + w[1]


def neg(z):
    return -z[0], -z[1]


def sub(z, w):
    return add(z, neg(w))


def conj(z):
    return z[0], -z[1]


def inv(z):
    norm = z[0] * z[0] + z[1] * z[1]
    return z[0] / norm, -z[1] / norm


def anti_reciprocal(z):
    return inv(conj(z))


def current(z):
    return sub(z, inv(z))


def main() -> None:
    checks = {}
    seam_points = [(F(1), F(0)), (F(-1), F(0)), (F(3, 5), F(4, 5)), (F(5, 13), F(12, 13))]
    for index, w in enumerate(seam_points):
        j = current(w)
        checks[f"anti_reciprocal_fixed_{index}"] = anti_reciprocal(w) == w
        checks[f"current_pure_imaginary_{index}"] = j[0] == 0
        checks[f"anti_linear_sign_law_{index}"] = current(anti_reciprocal(w)) == neg(conj(j))

    checks["generic_seam_current_nonzero"] = current((F(3, 5), F(4, 5))) == (F(0), F(8, 5))

    off_points = [(F(2), F(1)), (F(3, 2), F(-2, 3)), (F(-2), F(1, 2))]
    for index, w in enumerate(off_points):
        checks[f"off_seam_not_fixed_{index}"] = anti_reciprocal(w) != w
        checks[f"off_seam_sign_law_{index}"] = current(anti_reciprocal(w)) == neg(conj(current(w)))

    checks["holomorphic_fixed_plus"] = inv((F(1), F(0))) == (F(1), F(0))
    checks["holomorphic_fixed_minus"] = inv((F(-1), F(0))) == (F(-1), F(0))
    checks["generic_unit_point_not_holomorphic_fixed"] = inv((F(3, 5), F(4, 5))) != (F(3, 5), F(4, 5))

    assert all(checks.values()), [name for name, ok in checks.items() if not ok]
    print(f"{len(checks)}/{len(checks)} exact gates passed")


if __name__ == "__main__":
    main()

