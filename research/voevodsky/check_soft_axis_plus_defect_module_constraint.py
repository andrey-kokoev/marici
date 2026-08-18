"""Classify one-dimensional modules over A_+=Q[x]/(x^2)."""

from fractions import Fraction as Q

# On a one-dimensional Q-space, x acts by a scalar lambda.  The relation
# x^2=0 forces lambda^2=0, hence lambda=0 over Q.
tested = [Q(n, d) for d in range(1, 8) for n in range(-8, 9)]
nilpotent_scalars = [value for value in tested if value * value == 0]
assert nilpotent_scalars == [Q(0)] * 7  # zero occurs once for each denominator

print("one-dimensional A_+ module: x must act by 0")
print("unique type: A_+/(x)")
print("full incidence module A_+ eta has Q-dimension 2 and cannot equal defect one")
print("falsifier: the total differential must kill x eta while retaining eta")
