# Cancelling the relative return by its own determinant recovers only the bare Euler line

The exact Schur factorization is

\[
D_{\rm coupled}=D_{\rm Euler}^{\rm gr}\,D_{\rm ret},
\qquad
D_{\rm ret}=\det_F(I-K).
\]

One can form the ratio

\[
\frac{D_{\rm coupled}}{D_{\rm ret}}
=D_{\rm Euler}^{\rm gr}
\]

as an identity of local determinant-line sections, with numerator/denominator
frames used across zeros.  This is source-typed but tautological: it is exactly
Schur elimination of the boundary-return factor.

The ratio cannot be an independent conservative Xi criterion.  Every zero or
pole contributed by the coupled Green return is cancelled with its full local
multiplicity.  The surviving divisor is precisely the already known bare
graded Euler/scalar target divisor.

Therefore a legitimate compensating factor must be independently constructed
from another source face and compared with `D_ret`; using `D_ret` itself only
forgets the Green spectrum.  Conversely, retaining `D_ret` gives a genuinely
coupled determinant but no current theorem identifies its extra divisor with
Xi or proves it is a nowhere-zero unit.

This creates a strict dichotomy:

1. cancel the return factor and recover the known scalar determinant line, with
   no new spectral information;
2. retain the return factor and prove a new source comparison/unit theorem.

No algebraic normalization simultaneously cancels the factor and preserves its
kernel information.
