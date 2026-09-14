# v122: primitive free-cokernel detector

The integral Smith checker now computes a primitive left-nullvector of the
L2-completed matrix at every cutoff D12--D28.

The same closed formula occurs throughout: restrict to monomials with `u=0`
and `a=0`, then take the alternating coefficient sum
`sum_b (-1)^b c_(0,0,b)`. This functional is primitive and spans the rank-one
free cokernel at all five cutoffs.

Therefore L2 completion cannot remove the remaining free boundary class. Any
global soft extension that closes the road-Cech map must pair with this detector
by a unit (or alter the target in a separately justified derived construction).
Unlike a bare rank count, the explicit alternating formula is a viable target
for a direct all-degree proof.

`rzk/150-soft-d1-primitive-free-cokernel-detector.rzk.md` passes all eight
declarations without assumptions.
