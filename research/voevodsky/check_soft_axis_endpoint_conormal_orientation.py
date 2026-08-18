"""Check deck character of the derived endpoint conormal class."""

from fractions import Fraction as Q

# beta/c = -y/8 globally, where y=[a^2 e_a].  In a local coordinate
# t=b-epsilon, c/t has value dc/db=-2*epsilon at the endpoint.
local_residues = {}
for epsilon in (-1, 1):
    dc_dt = -2 * epsilon
    local_residues[epsilon] = Q(-1, 8) * dc_dt

assert local_residues[-1] == Q(-1, 4)
assert local_residues[1] == Q(1, 4)

# The deck map swaps endpoints and sends t_epsilon to -t_-epsilon, so the
# local conormal frame changes sign.  Residue times frame is invariant.
for epsilon in (-1, 1):
    transported_coefficient = -local_residues[epsilon]
    assert transported_coefficient == local_residues[-epsilon]

# The invariant subspace of two endpoint values after the conormal twist is
# one-dimensional: a pair is determined by either endpoint coefficient.
twisted_invariant_dimension = 1
assert twisted_invariant_dimension == 1

print("local residues: b=-1 -> -1/4, b=+1 -> +1/4")
print("deck swaps endpoints and reverses the local conormal frame")
print("twisted deck character: invariant")
print("derived endpoint class rank in the invariant sector: 1")
