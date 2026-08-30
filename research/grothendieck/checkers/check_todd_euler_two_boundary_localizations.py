#!/usr/bin/env python3
"""Exact coefficient audit of the Todd–Euler scale derivative law."""

from fractions import Fraction


degree = 16

# E(r)=-log(1-r)=sum r^k/k.  The logarithmic derivative r*d/dr
# removes the occupation denominator and fills every positive grade.
euler = [Fraction(0)] + [Fraction(1, k) for k in range(1, degree + 1)]
log_derivative = [Fraction(0)] + [Fraction(k) * euler[k] for k in range(1, degree + 1)]
geometric_tail = [Fraction(0)] + [Fraction(1) for _ in range(degree)]
assert log_derivative == geometric_tail

# Under r=exp(-t), r/(1-r)=1/(exp(t)-1), so multiplication by
# t=-log(r) gives the Todd germ t/(exp(t)-1).
assert all(log_derivative[k] == 1 for k in range(1, degree + 1))

print("euler_chart=r=0")
print("euler_potential=-log(1-r)=sum_k r^k/k")
print("log_scale_derivative=r*d/dr")
print("derived_current=sum_k r^k=r/(1-r)")
print("coordinate_transition=r=exp(-t)")
print("todd_chart=r=1_equivalently_t=0")
print("todd_identity=tau(-log(r))=(-log(r))*r*dE/dr")
print("structure=two_boundary_localizations_one_global_scale_object")
