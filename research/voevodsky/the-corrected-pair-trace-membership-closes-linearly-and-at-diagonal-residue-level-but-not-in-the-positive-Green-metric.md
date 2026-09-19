# The corrected pair trace membership closes linearly and at diagonal-residue level, but not in the positive Green metric

The corrected pair lane has a more precise status than pointwise
source-membership alone suggests.

Prior all-jet work constructs the linear chain

\[
P_{\rm pair}\longrightarrow B_{\rm jet}
\longrightarrow E_{\rm aug,p},
\]

with

\[
D_{\rm jet}(h_k,H_k)=(h_{k+1},zH_k-h_k(0))
\]

and an exact boundary-augmented Euler intertwiner.  It retains the full pair
density, every endpoint jet, shell labels, cutoff naturality, and orientation.
Thus linear corrected-trace membership is not missing.

A domain qualification remains for the Xi homotopy.  The formal coefficient
`exp(zq)` is not in the rapid pair-to-border domain.  With Evans parameter `z`
and Laplace parameter `zeta`, its shell response is

\[
\frac{\tau(z)A_{[a,b]}(z)}{\zeta-z},
\qquad
A_{[a,b]}(z)=\int_a^b\Phi(x)e^{zx}\,dx.
\]

It has a pole on the physical diagonal.  Therefore the earlier algebraic
multiplicity statement cannot be promoted directly to a holomorphic rapid
bordered family.

The two-variable residue extension repairs this exactly:

\[
\operatorname{Res}_{\zeta=z}
\frac{\tau(z)A_{[a,b]}(z)}{\zeta-z}
=\tau(z)A_{[a,b]}(z).
\]

Since `A_[a,b]` is entire, this residue is null-homotopic through the Xi wall
differential and preserves all local divisor jets.  Shell concatenation and
finite cutoffs commute with the residue construction.

Accordingly, corrected trace membership has three levels:

1. linear all-jet boundary/Euler square: constructed;
2. Xi-divisible diagonal-residue comparison: constructed;
3. positive conservative Green realization of the pole--residue extension:
   open.

The missing `CG` datum is now metric: construct a hyperbolic or chirality-
selected pole--residue block whose boundary pairing is the diagonal residue,
and compare its positive form with the independent conservative Green form.
A direct positive norm on the residue itself would be wrong because the
Xi-exact residue must vanish in the derived quotient.
