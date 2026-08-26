# Native prime-sheet adjoint matching occurs exactly on the seam

## Bounded question

Does Fourier--Tate doubling pair each prime transport with its Hilbert adjoint
at equal source coefficient before scalar aggregation?

## Native local coefficients

Use the centered coordinate

\[
z=s-\frac12.
\]

For a prime \(p\), the direct Euler sheet carries the coefficient

\[
\alpha_p(z)=p^{-1/2-z},
\]

while reciprocal transport carries

\[
\beta_p(z)=p^{-1/2+z}.
\]

On the integer-label module let \(T_p e_n=e_{pn}\). The native direct and
reciprocal transport terms are therefore

\[
\alpha_p(z)T_p,
\qquad
\beta_p(z)T_p^*.
\]

No scalar readout or zero location enters these coefficients.

## Exact adjoint test

The Hilbert adjoint of the direct term is

\[
\bigl(\alpha_p(z)T_p\bigr)^*
=p^{-1/2-\overline z}T_p^*.
\]

It equals the reciprocal term precisely when

\[
p^{-1/2+z}=p^{-1/2-\overline z}.
\]

Since \(p>1\), this is equivalent to

\[
z=-\overline z,
\]

or

\[
\operatorname{Re}s=\frac12.
\]

Thus the source-native prime pair is star-compatible exactly on the critical
seam.

## The mismatch is not a removable unitary phase

The ratio of reciprocal amplitude to the adjoint direct amplitude is

\[
\frac{|\beta_p(z)|}{|\overline{\alpha_p(z)}|}
=p^{2\operatorname{Re}z}.
\]

Away from the seam this is not one. A unitary change of label frame can rotate
the phase of \(T_p\), but cannot alter this modulus ratio. Hence no
source-authorized unitary parallelization turns the two native terms into
adjoints off seam.

A nonunitary rescaling can absorb the ratio prime by prime, but it changes the
Hilbert metric and reproduces the previously identified gain cocycle. Using it
without a separately derived global metric would insert the desired
adjointness by hand.

## Smallest matrix residual

On \(\operatorname{span}\{e_1,e_p\}\), the unmatched part is the single
off-diagonal coefficient

\[
\delta_p(z)
=p^{-1/2+z}-p^{-1/2-\overline z}.
\]

It vanishes exactly on the seam. This is the smallest finite falsifier for any
claim that native two-sheet doubling is already a self-adjoint energy away
from the seam.

## Result and boundary

Fourier--Tate doubling supplies a perfect local seam detector, not a
zero-confinement mechanism. The coefficient equality needed to cancel the
indefinite logarithmic-degree commutator is itself equivalent to being on the
seam.

Consequently the proposed two-sheet repair cannot prove that a zero lies on
the seam unless an independent source theorem first forces the zero-state to
use the Hilbert-adjoint comparison. The doubled tail domain and staircase
Green identity do not supply that theorem.

## Remaining live question

The only surviving place for new force is a global compatibility law that
connects scalar zero-state boundary data to the native star comparison without
assuming local coefficient equality. It must use a genuinely global
prime--archimedean constructor and must reject the off-seam two-shell hostile
before its zero is inspected.
