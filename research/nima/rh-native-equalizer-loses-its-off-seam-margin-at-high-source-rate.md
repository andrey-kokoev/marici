# The native equalizer loses its off-seam margin at high source rate

Scope correction: the checker works on the real normal slice.  The corresponding
full-plane reciprocal parameter is \(1-\overline{s}\), not \(1-s\).

## Finite exactness is not uniform exactness

For one labelled mode of rate \(\lambda\) and incidence \(b\), the native
off-seam equalizer block is

\[
E_{z,\lambda,b}=
\begin{pmatrix}
z-\lambda&b\\
1-z-\lambda&b
\end{pmatrix}.
\]

Its determinant is \(b(2z-1)\), so it is invertible for every finite
\(\lambda\) when \(b\ne0\) and \(z\ne1/2\).

Choose a state \((A,c)\) satisfying

\[
bc=(\lambda-1/2)A.
\]

Then

\[
E_{z,\lambda,b}
\binom{A}{c}
=
\binom{(z-1/2)A}{-(z-1/2)A}.
\]

Its squared residual-to-state ratio is

\[
\frac{2|z-1/2|^2|A|^2}
{|A|^2+|c|^2}
=
\frac{2|z-1/2|^2}
{1+|\lambda-1/2|^2/|b|^2}.
\]

For fixed nonzero \(b\) and fixed off-seam \(z\), this tends to zero as
\(\lambda\to\infty\).

## Consequence

Every finite equalizer is trivial, but the family has no cutoff-independent
lower bound in the unweighted tail-plus-reservoir norm.  High-rate states become
approximate common solutions off the seam.  Thus finite naturality does not
make completion preserve the equalizer.

This is an explicit realization of the earlier completion-at-infinity warning:
the partner does not disappear because of a mysterious global limit.  It
escapes into the large reservoir coordinate needed to cancel the common
\(-\lambda A\) contribution in both sector equations.

## What repairs the margin

The endpoint kernel observer sees the escaping coordinate directly:

\[
J_0(A,c)=c.
\]

Adding \(|c|^2\) to the observation energy prevents this particular sequence
from becoming invisible.  Therefore the seam law cannot be only the equalizer
of sector residuals.  It must include a source-derived boundary observation or
graph norm controlling the labelled reservoir coordinate.

This makes the previous distinction operational:

1. sector equalization exposes the normal factor;
2. boundary-kernel resolution supplies the missing uniform completion margin;
3. tangential spectral incidence must remain separate so legitimate seam zeros
   are not erased.

## DPC verdict

The unweighted native equalizer fails the completion gate.  A viable completed
law must prove a bound of the form

\[
\|x\|_{\mathrm{src}}^2
\le C_K
\left(
\|D_+(z)x\|^2+
\|D_-(z)x\|^2+
\|Jx\|^2
\right)
\]

uniformly for \(z\) in each compact set \(K\) disjoint from the seam and
uniformly in the arithmetic cutoff.

The exact finite falsifier is the normalized state above along any sequence of
rates tending to infinity.  If the proposed source norm or seam incidence does
not prevent its residual ratio from tending to zero, completion exactness
fails.

## Verification

`check_rh_equalizer_high_rate_escape.py` evaluates the exact rational residual
ratios for increasing rates, proves strict decrease in the chosen family, and
checks that adjoining the endpoint reservoir observation gives a uniform lower
bound for the same escape states.
