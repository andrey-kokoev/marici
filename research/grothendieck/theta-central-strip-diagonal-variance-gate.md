# Central-strip diagonal Loewner variance gate

## Domain correction

For the renormalized precursor

\[
K(u)=\cosh(u/2)-\frac12e^{u/2}\Theta(e^{2u}),
\]

we have \(K(u)\sim e^{-|u|/2}/2\). Therefore

\[
I(x)=\int_0^\infty K(u)\cosh(\sqrt x\,u)\,du
\]

converges as a positive real integral only for

\[
\boxed{0\le x<1/4.}
\]

An initially drafted argument for \(x>1/4\) was invalid because it used this
divergent integral as a probability normalization. No positive-ray theorem is
claimed.

## Positivity of the precursor

For \(u\ge0\), put \(X=e^{2u}\ge1\). Then

\[
K(u)=X^{-1/4}
\left[
\frac12-\sqrt X\sum_{n\ge1}e^{-\pi n^2X}
\right].
\]

The bound \(n^2\ge1+3(n-1)\) gives

\[
\sum_{n\ge1}e^{-\pi n^2X}
\le\frac{e^{-\pi X}}{1-e^{-3\pi X}}.
\]

Moreover

\[
\frac{2\sqrt X e^{-\pi X}}{1-e^{-3\pi X}}<1
\qquad(X\ge1),
\]

because its logarithmic derivative is negative and the inequality is strict
at \(X=1\). Hence

\[
\boxed{K(u)>0\qquad(u\in\mathbb R).}
\]

This analytic positivity theorem survives the domain correction.

## Exact tilted-law identity

For \(0<x<1/4\), define

\[
d\mu_x(u)=
\frac{K(u)\cosh(\sqrt x\,u)}{I(x)}\,du
\]

and

\[
q_x(u)=\partial_x\log\cosh(\sqrt x\,u)
=\frac{u\tanh(\sqrt x\,u)}{2\sqrt x}.
\]

Then

\[
\frac{I'}I=\mathbb E_xq_x,
\qquad
\partial_x\mathbb E_xq_x
=\mathbb E_x(\partial_xq_x)+\operatorname{Var}_x(q_x).
\]

For

\[
H(x)=1+(x-1/4)\frac{I'(x)}{I(x)},
\]

we obtain

\[
\boxed{
H'(x)=
\mathbb E_x\left[q_x+(x-1/4)\partial_xq_x\right]
-(1/4-x)\operatorname{Var}_x(q_x).
}
\]

The pointwise term is strictly positive. Indeed \(\partial_xq_x<0\), so for
\(x<1/4\),

\[
q_x+(x-1/4)\partial_xq_x>q_x>0.
\]

But the variance term has the opposite sign. Therefore diagonal Loewner
positivity in the convergent precursor strip is exactly the nontrivial
inequality

\[
\boxed{
\mathbb E_x\left[q_x+(x-1/4)\partial_xq_x\right]
>(1/4-x)\operatorname{Var}_x(q_x).
}
\]

## Meaning

The source decomposition explains the central difficulty as a competition
between deterministic response and fluctuation. The source-forced center
\(1/4\) is where the variance coefficient changes sign, but the positive
precursor representation ceases to converge at exactly the same boundary.

That coincidence blocks the naive continuation to the outer positive ray. It
also explains why positivity of the real-space precursor is insufficient:
one needs a quantitative variance bound, not merely a positive measure.

The escaping null mode can be subtracted exactly. It contributes the pole
\(1/[4(1/4-w)]\), which completion cancels to the constant \(1/4\), leaving
an entire positive-theta transform. See
`theta-null-mode-critical-renormalization.md`.

The next legitimate scalar theorem is to prove the displayed variance bound
from a concentration or curvature property of \(K\). Higher Loewner minors
would then require corresponding multi-point covariance inequalities.

## Falsifier

A single \(x\in(0,1/4)\) where the variance dominates falsifies this
particular tilted-law mechanism. Passing the diagonal bound does not establish
matrix monotonicity or RH.
