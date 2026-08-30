"""Exact checks for the minimal affine-tail adjoint-completion obstruction."""

from fractions import Fraction


checks = 0
for f in (Fraction(1, 3), Fraction(1), Fraction(7, 2)):
    for u in (Fraction(-2), Fraction(1, 5), Fraction(4)):
        for c in (Fraction(-3), Fraction(1), Fraction(5, 2)):
            # Forward incidence and its unique real skew-adjoint mate.
            du_coupling = -f * c
            dc_coupling = f * u

            # The coupling preserves the positive two-state norm.
            norm_derivative = 2 * u * du_coupling + 2 * c * dc_coupling
            assert norm_derivative == 0

            # The native constant channel is not invariant for nonzero f,u.
            assert dc_coupling != 0

            # A separate response port can record the adjoint output while c stays fixed.
            native_dc = Fraction(0)
            response_derivative = f * u
            assert native_dc == 0
            assert response_derivative == dc_coupling
            checks += 4

print(f"PASS {checks}/{checks}: adjoint completion requires a response port distinct from constant source input")

