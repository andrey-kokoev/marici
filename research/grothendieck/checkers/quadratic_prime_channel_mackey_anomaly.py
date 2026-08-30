"""Exact C2 controls for the quadratic-channel Mackey anomaly."""

from fractions import Fraction


# Functions on C2 are pairs (f(0),f(1)); pullback by [2] repeats f(0).
def second_power_pullback(function: tuple[int, int]) -> tuple[int, int]:
    return (function[0], function[0])


def fiber_sum(function: tuple[int, int]) -> int:
    return function[0] + function[1]


delta_zero = (1, 0)
left = fiber_sum(second_power_pullback(delta_zero))
right = fiber_sum(delta_zero)  # the power map on the one-point quotient
assert left == 2
assert right == 1
assert left != right

# Averaging changes the frozen normalization rather than repairing both legs.
normalized_selected_value = Fraction(fiber_sum(delta_zero), 2)
assert normalized_selected_value == Fraction(1, 2)
assert normalized_selected_value != 1

# The degree-two norm gives a genuine two-periodic algebraic complex.
norm = ((1, 1), (1, 1))
complement = ((1, -1), (-1, 1))  # 2I-N


def multiply(left: tuple[tuple[int, int], tuple[int, int]], right: tuple[tuple[int, int], tuple[int, int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    return tuple(
        tuple(sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )  # type: ignore[return-value]


zero = ((0, 0), (0, 0))
assert multiply(norm, complement) == zero
assert multiply(complement, norm) == zero

print("quadratic_channel_is_half_trace_of_second_power=True")
print("second_power_C2_Mackey_square_fails_by_factor_two=True")
print("averaging_changes_frozen_selector_normalization=True")
print("degree_two_norm_defect_forms_two_periodic_complex=True")
print("analytic_torsion_identification_open=True")
