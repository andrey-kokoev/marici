"""Module audit for the even incidence principal parts at t=b+1."""

from fractions import Fraction as Q

# A_+=Q[x]/(x^2), x=a^2.  In H^1_(t), eta=[1/t] and x*eta=[x/t].
# Represent the cyclic submodule A_+ eta in the basis (eta,x eta).
eta = (Q(1), Q(0))
x_eta = (Q(0), Q(1))


def multiply_x(vector):
    constant, x_coefficient = vector
    return (Q(0), constant)  # x^2=0


assert multiply_x(eta) == x_eta
assert multiply_x(x_eta) == (Q(0), Q(0))

# The two lift residues from Entry 501 are scalar multiples of this pair.
residue_0 = tuple(-Q(1, 6) * v for v in eta)
residue_2 = tuple(-Q(1, 6) * v for v in x_eta)
assert multiply_x(residue_0) == residue_2

print("incidence module = A_+ * eta, A_+=Q[x]/(x^2)")
print("eta=[1/(b+1)], x eta=[a^2/(b+1)]")
print("Q-dimension=2, Cartier-module generator count=1")
print("verdict: the two even poles form one cyclic incidence obstruction")
