# The joint graph energy gives an exact two-weight history-loading criterion

## Abstract graph form

Let \(T\) be the closed transported ray derivative on its graph domain.
For positive constants \(a,b\), define the even graph energy

\[
E_{a,b}[f]
=
a\|f\|^2+b\|Tf\|^2.
\]

The causal-minus-anticausal diagonal form is

\[
h_T[f]
=
\operatorname{Im}\langle f,Tf\rangle.
\]

It is the diagonal of the Hermitian polarization of the skew part of \(T\).
Cauchy--Schwarz gives

\[
|h_T[f]|
\le
\|f\|\,\|Tf\|.
\]

For \(r=\|Tf\|/\|f\|\),

\[
\frac{|h_T[f]|}{E_{a,b}[f]}
\le
\frac{r}{a+br^2}.
\]

The scalar function on the right is maximized at
\(r=\sqrt{a/b}\), with value

\[
\frac{1}{2\sqrt{ab}}.
\]

Therefore

\[
|h_T[f]|
\le
\frac{1}{2\sqrt{ab}}E_{a,b}[f].
\]

## Strict positivity criterion

For an oriented loading coefficient \(\alpha\), consider

\[
D_\pm[f]
=
E_{a,b}[f]\pm\alpha h_T[f].
\]

A sufficient uniform margin is

\[
\kappa_{a,b}
=
\frac{|\alpha|}{2\sqrt{ab}}
<1.
\]

Then

\[
D_\pm[f]
\ge
(1-\kappa_{a,b})E_{a,b}[f].
\]

This is the infinite-dimensional graph version of the earlier two-coordinate
determinant inequality. The quantities \(a\) and \(b\) are the absolute
source weights of the state and derivative energies; \(\alpha\) is the
oriented history loading.

## Quarter-gap normalization

The bare theta energy supplies

\[
a=\frac14.
\]

If the two-ray Green identity supplies exactly one unit of derivative graph
energy, \(b=1\), then

\[
2\sqrt{ab}=1
\]

and the criterion becomes

\[
|\alpha|<1.
\]

Thus the same saturation threshold found for the constant translation
benchmark reappears without translation invariance. It follows from the
weighted square law alone.

## Theta-label suppression

For

\[
T_n=n^{-1}T,
\]

the odd form obeys

\[
|h_{T_n}[f]|
=
n^{-1}|h_T[f]|.
\]

If the common even topology retains the unscaled derivative energy
\(b\|Tf\|^2\), then

\[
\kappa_{a,b,n}
=
\frac{|\alpha_n|}{2n\sqrt{ab}}.
\]

Hence all large labels are automatically safer. The worst finite gate is at
the smallest admitted label, unless \(\alpha_n\) itself grows with \(n\).

If instead the even energy is weakened labelwise to
\(b\|T_nf\|^2\), this suppression disappears. That is another reason the
common completion must use the unscaled source graph.

## Sharpness qualification

The constant \(1/(2\sqrt{ab})\) is universally optimal using only the two
norm coordinates. Equality in a particular source cyclic carrier additionally
requires approximate vectors satisfying both:

\[
\|Tf\|/\|f\|\to\sqrt{a/b},
\]

and phase alignment of \(Tf\) with \(if\).

If the source excludes such vectors, a better strict bound may hold. That
improvement must be proved from the carrier, not inferred from finite
truncations.

## Missing authority

The joint graph topology is analytically legitimate, but the coefficients
\(a,b\) cannot be chosen freely. The source two-ray Green/Stokes identity
must show which combination of

\[
\|f\|^2,
\qquad
\|Tf\|^2
\]

actually constitutes the even auxiliary energy.

Only then is \(\kappa_{a,b,n}\) an authorized Adams-cell margin.

## Frontier

The remaining positivity problem has contracted to three source scalars or
forms:

\[
a,
\qquad
b,
\qquad
\alpha_n.
\]

Once the two-ray Green identity fixes them, the auxiliary contraction follows
from

\[
|\alpha_n|<2n\sqrt{ab},
\]

uniformly in the declared prime and off-seam family. The endpoint incidence
and Schur-return identity remain downstream.
