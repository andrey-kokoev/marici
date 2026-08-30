"""Exact checks that the hidden relative response is the Green defect."""

from fractions import Fraction


checks = 0
for z in (Fraction(-2), Fraction(-1, 3), Fraction(0), Fraction(5, 2)):
    for f in (Fraction(1, 5), Fraction(1), Fraction(9, 2)):
        for u, v in (
            (Fraction(-3), Fraction(2)),
            (Fraction(0), Fraction(4)),
            (Fraction(7, 3), Fraction(-7, 3)),
        ):
            u_prime = -z * u - f
            v_prime = z * v - f
            green_derivative = 2 * u * u_prime - 2 * v * v_prime

            r_plus = -f * u
            r_minus = -f * v
            r_relative = r_plus - r_minus

            lhs = 2 * z * (u * u + v * v)
            rhs = -green_derivative + 2 * r_relative
            assert lhs == rhs
            assert r_relative == -f * (u - v)

            if u + v == 0 and u != 0:
                assert r_plus + r_minus == 0
                assert r_relative != 0
                checks += 2
            checks += 2

print(f"PASS {checks}/{checks}: relative adjoint response equals the doubled Green forcing defect")

