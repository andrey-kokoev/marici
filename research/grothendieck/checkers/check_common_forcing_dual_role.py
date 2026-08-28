"""Exact checks for the boundary/bulk dual role of common forcing."""

from fractions import Fraction


checks = 0
for z in (Fraction(-2), Fraction(-1, 3), Fraction(0), Fraction(5, 2)):
    for u in (Fraction(-3), Fraction(0), Fraction(7, 4)):
        for f in (Fraction(1, 5), Fraction(1), Fraction(9, 2)):
            v = -u

            # Endpoint scalar cancellation retains strict affine energy.
            energy = (u + f) ** 2 + (v + f) ** 2
            assert energy == 2 * u * u + 2 * f * f
            assert energy > 0

            # The endpoint anti-diagonal is not flow-invariant generically.
            u_prime = -z * u - f
            v_prime = z * v - f
            p_prime = u_prime + v_prime
            q = u - v
            assert p_prime == -z * q - 2 * f
            checks += 3

print(f"PASS {checks}/{checks}: common forcing preserves endpoint meaning but obstructs pathwise sewing")

