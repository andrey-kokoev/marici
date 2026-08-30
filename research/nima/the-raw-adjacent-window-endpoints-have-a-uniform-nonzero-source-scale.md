# The raw adjacent-window endpoints have a uniform nonzero source scale

## Result

The analytic adjacent-window traces are not only contractions. Under the source assumption that the front profile is strictly decreasing, both primitive and square endpoint windows have a prime-uniform positive operator-norm lower scale.

This supplies the absolute endpoint scale needed by the Pauli lift estimate, conditional on the missing arithmetic comparison maps realizing these exact windows.

It does not construct those comparison maps.

## Window profile

Let

\[
W_t(q)=H(q+t)-H(q-t),
\]

where

\[
0\le H\le1
\]

is continuous and strictly decreasing.

For every \(t>0\),

\[
W_t(q)<0.
\]

As established previously,

\[
\|M_{W_t}\|_{L^2\to L^2}
=
\|W_t\|_\infty
\le1.
\]

## Lower bound at a marked point

Evaluate at \(q=0\):

\[
W_t(0)=H(t)-H(-t).
\]

Define

\[
m(t)=H(-t)-H(t)>0.
\]

Then

\[
\|W_t\|_\infty
\ge
|W_t(0)|
=
m(t).
\]

Because \(H\) is decreasing, \(H(-t)\) increases and \(H(t)\) decreases as \(t\) grows. Hence \(m(t)\) is increasing.

For every prime,

\[
L=\log p\ge\log2.
\]

Therefore

\[
\|M_{W_L}\|
\ge
m(\log2)
\]

and

\[
\|M_{W_{2L}}\|
\ge
m(2\log2)
\ge
m(\log2).
\]

Set

\[
m_W=H(-\log2)-H(\log2)>0.
\]

Then both endpoint traces obey

\[
m_W
\le
\|M_{W_L}\|,
\|M_{W_{2L}}\|
\le
1
\]

uniformly over all primes.

## Consequence for the Pauli lift

Suppose the source comparison maps \(J_{P,p},J_{Q,p}\) realize the normalized endpoint basis as the actual multiplication windows in a target norm whose endpoint energy agrees with operator norm squared:

\[
a_p=\|M_{W_L}\|^2,
\qquad
b_p=\|M_{W_{2L}}\|^2.
\]

Then

\[
a_p,b_p\ge m_W^2.
\]

The Pauli twirl identity gives

\[
\|J_pXv\|^2+\|J_pYv\|^2
\ge
2m_W^2\|v\|^2.
\]

Thus the lifted arithmetic frame has lower bound

\[
\sqrt2\,m_W.
\]

No endpoint correlation estimate is required.

## Norm qualification

The multiplication-operator norm is not automatically the Green endpoint energy.

If the target Green form uses:

- an \(L^2\) norm of the window;
- a trace norm;
- a quotient energy;
- a rigged dual norm;
- or a source-weighted graph norm,

then a comparison theorem is still required.

The correct statement is

\[
c_-\|M_{W_t}\|_{\mathrm{op}}^2
\le
G_{\partial}(W_t,W_t)
\le
c_+\|M_{W_t}\|_{\mathrm{op}}^2
\]

or its source-derived replacement. Without such a theorem, the raw lower scale cannot be transported into the Green metric.

## Radical qualification

The pointwise nonzero window can still become zero after quotienting by a Green radical. Hence one must prove

\[
[W_L]\ne0,
\qquad
[W_{2L}]\ne0
\]

in the reduced endpoint space.

For the Jacobi heat energy, only constants are radical and these windows are nonconstant, so they survive. The complete adjacent-window relative Green radical may be larger and remains to be audited.

## Strictness assumption

If \(H\) is merely nonincreasing, then

\[
m_W
\]

may vanish because \(H\) could be constant on \([-\log2,\log2]\).

Therefore the positive lower bound uses strict source front separation, not only the earlier monotonicity needed for contraction.

For Gaussian, logistic, error-function, or theta-derived strict fronts, this condition holds.

## Constructor consequence

The raw geometric endpoint packet now has absolute scales

\[
m_W\le\|W_L\|_\infty,\|W_{2L}\|_\infty\le1.
\]

Combined with the exact Pauli twirl, this removes raw endpoint collapse as a candidate obstruction.

The earliest unresolved arrow remains:

> Prove that the arithmetic endpoint incidences map to these exact analytic windows in the declared reduced Green metric, with a uniform norm comparison and the correct reciprocal orientation.

Analytic endpoint traces alone still do not supply that arithmetic incidence authority.
