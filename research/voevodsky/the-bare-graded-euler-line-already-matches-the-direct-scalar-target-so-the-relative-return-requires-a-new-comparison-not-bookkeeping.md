# The bare graded Euler line already matches the direct scalar target, so the relative return requires a new comparison

On the Euler half-plane, the graded bare loop compiles exactly to

\[
D_{\rm Euler}^{\rm gr}(s)
=A_\infty(s)\prod_p(1-p^{-s})
=A_\infty(s)\zeta(s)^{-1}
\]

in the direct Sonin orientation.  This is already the canonical scalar
meromorphic target `M_comp=E Z^(-1)` after the declared elementary
endpoint/archimedean normalization is matched.

The coupled boundary determinant instead factors as

\[
D_{\rm coupled}(s)
=D_{\rm Euler}^{\rm gr}(s)\det_F(I-K(s)).
\]

Therefore equality of the coupled compiler with the same scalar target would
require

\[
\det_F(I-K(s))=1
\]

(up to a separately declared nowhere-zero normalization unit) on an open Euler
chart.  This is not a bookkeeping identity.  The boundary-mediated return is
generically nontrivial, and its logarithmic derivative is

\[
\partial_s\log\det_F(I-K)
=-\operatorname{Tr}\bigl((I-K)^{-1}K'\bigr).
\]

No existing source theorem makes this vanish or identifies it with an omitted
scalar factor.  Absorbing it into `A_infty` after construction would violate
the realization-provenance gate unless an independent endpoint/archimedean
source formula supplies exactly that factor.

Thus there are two distinct objects:

1. the bare graded Euler determinant line, already compared with the direct
   scalar completed target on `Re s>1`;
2. the coupled Green/Schur determinant line, carrying the additional relative
   return determinant.

The next gate is an explicit theorem identifying `det_F(I-K)` with a named
source factor, proving it is a holomorphic unit, or showing that the intended
Xi characteristic is a ratio in which it cancels.  It cannot be removed by
relabeling the total compiler.
