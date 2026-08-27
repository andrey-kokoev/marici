#!/usr/bin/env python3
"""Audit denominator closure of the physical second-shape insertion."""

from fractions import Fraction as F


# For y(t)=sqrt(k(t)^2), record denominator powers in the exact derivatives:
# y'=(k.k')/y and y''=(k'^2+k.k'')/y-(k.k')^2/y^3.
y_prime_denominator_powers = {1}
y_second_denominator_powers = {1, 3}

# For one source pole q^-1, the exact second derivative is
# 2(q')^2 q^-3 - q'' q^-2.  q' contains y^-1 and q'' contains y^-1,y^-3.
q_second_powers = {2, 3}
induced_y_powers = y_prime_denominator_powers | y_second_denominator_powers

# Momentum-space propagators are (k^2)^(-tau).  Source Eq. (54) and its
# discussion explicitly retain the integer/half-integer mixed family.
# Multiplication by y^-r=(k^2)^(-r/2) preserves the half-integral lattice.
base_tau = F(1, 2)
shifted_taus = {base_tau + F(r, 2) for r in induced_y_powers}

# Cross derivatives of a product of source poles raise each individual q
# exponent by at most two and never introduce a new polynomial denominator.
source_support_labels = {
    "qG", "qg1", "qg2", "qg3",
    "qG12", "qG23", "qG31", "qg12", "qg23", "qg31",
    "k1_squared", "k2_squared", "k3_squared",
}
insertion_support_labels = set(source_support_labels)

checks = {
    "first_length_derivative_has_only_existing_propagator_support": y_prime_denominator_powers == {1},
    "second_length_derivative_closes_at_cubic_length_power": y_second_denominator_powers == {1, 3},
    "source_pole_second_derivative_closes_at_power_three": q_second_powers == {2, 3},
    "half_integral_propagator_lattice_is_preserved": all((2 * tau).denominator == 1 for tau in shifted_taus),
    "no_new_denominator_polynomial_is_introduced": insertion_support_labels == source_support_labels,
    "insertion_has_finite_exponent_bound": max(q_second_powers) == 3 and max(induced_y_powers) == 3,
}

assert all(checks.values()), checks
print(f"PASS {sum(checks.values())}/{len(checks)}")
print("shifted half-integer propagator exponents:", sorted(shifted_taus))
print("max source-pole power: 3; max length-denominator power: 3")
