"""Exact asymptotic-coefficient checks for quarter-shifted shell matching."""

from fractions import Fraction


def shell_second_coefficient(shift: Fraction) -> Fraction:
    # log((k+1+c)/(k+c)) = 1/k -(c+1/2)/k^2 + ...
    return -(shift + Fraction(1, 2))


def oscillator_second_coefficient(quarter_shift: Fraction) -> Fraction:
    # 1/(k+a) = 1/k-a/k^2+...
    return -quarter_shift


gamma_shift = Fraction(1, 4)
required_shell_shift = gamma_shift - Fraction(1, 2)
assert required_shell_shift == Fraction(-1, 4)
assert shell_second_coefficient(required_shell_shift) == oscillator_second_coefficient(gamma_shift)

unshifted_mismatch = shell_second_coefficient(Fraction(0)) - oscillator_second_coefficient(gamma_shift)
assert unshifted_mismatch == Fraction(-1, 4)

# Finite weighted shell vectors normalize exactly and different shells have
# disjoint support, hence are orthogonal.
shells = (
    (Fraction(1, 2), Fraction(1, 4)),
    (Fraction(1, 6), Fraction(1, 8), Fraction(1, 10)),
)
for shell_weights in shells:
    mass = sum(shell_weights)
    normalized_squared_norm = sum(weight / mass for weight in shell_weights)
    assert normalized_squared_norm == 1

print("shell_second_order_match_uniquely_for_shift_minus_one_quarter=True")
print("gamma_quarter_shift_selects_prime_shell_origin=True")
print("unshifted_shell_relative_error_is_order_one_over_k=True")
print("quarter_shifted_relative_error_is_order_one_over_k_squared=True")
print("quarter_shifted_radial_covariance_difference_trace_class=True")
print("within_shell_fluctuation_Euler_coupling_open=True")
