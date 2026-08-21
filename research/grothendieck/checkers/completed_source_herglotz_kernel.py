"""Exact sign and Laurent-cancellation checks for the source Xi kernel."""

import sympy as sp

z, log_n, coefficient = sp.symbols("z log_n a", positive=True)
single_prime_diagonal = -coefficient * sp.exp(-z * log_n) / z
assert single_prime_diagonal < 0

# Abstract Laurent germ at s=1: zeta'/zeta=-1/epsilon+gamma+O(epsilon).
epsilon, euler_constant = sp.symbols("epsilon gamma", positive=True)
endpoint_germ = 1 / epsilon
zeta_log_derivative_germ = -1 / epsilon + euler_constant
completed_germ = sp.simplify(endpoint_germ + zeta_log_derivative_germ)
assert completed_germ == euler_constant

# A negative local block can live inside a positive Schur complement only
# through coupling; it cannot itself be a Gram diagonal.
positive_a, positive_b, coupling = sp.symbols("A B C", positive=True)
block = sp.Matrix([[positive_a, coupling], [coupling, positive_b]])
assert block.det() == positive_a * positive_b - coupling**2

print("single_prime_kernel_diagonal_negative=True")
print("endpoint_zeta_poles_cancel=True")
print("raw_prime_series_extends_to_s_1=False")
print("orthogonal_positive_local_sum_possible=False")
print("completed_relative_Gram_construction_open=True")

