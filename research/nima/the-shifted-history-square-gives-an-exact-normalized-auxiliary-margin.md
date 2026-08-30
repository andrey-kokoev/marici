# The shifted-history square gives an exact normalized auxiliary margin

## Source square

Suppose the source two-ray identity supplies the shifted-history factors

\[
D_\pm
=
\frac12
\left(
\sqrt\lambda I
\pm i\alpha H
\right)^*
\left(
\sqrt\lambda I
\pm i\alpha H
\right),
\]

where \(H\) is the declared causal history operator. Expanding gives an even
form

\[
E[f]
=
\frac12
\left(
\lambda\|f\|^2
+
|\alpha|^2\|Hf\|^2
\right)
\]

and an oriented cross form whose diagonal magnitude is bounded by

\[
|O[f]|
\le
|\alpha|\sqrt\lambda
\|f\|\,\|Hf\|.
\]

This identifies the abstract two graph weights rather than choosing them:

\[
a=\frac\lambda2,
\qquad
b=\frac{|\alpha|^2}{2}.
\]

## Why the unrestricted graph estimate saturates

With no bound on \(H\), the universal two-weight criterion gives

\[
\frac{|\alpha|\sqrt\lambda}
{2\sqrt{ab}}
=
1.
\]

This is not a failure of the square. It says only that a perfect square can
have arbitrarily small values if its two summands can cancel.

Strictness comes from excluding the cancellation ratio

\[
\frac{\|Hf\|}{\|f\|}
=
rac{\sqrt\lambda}{|\alpha|}.
\]

## History-mass improvement

Assume

\[
\|H\|\le M
\]

and define the dimensionless loading

\[
q
=
\frac{|\alpha|M}{\sqrt\lambda}.
\]

If \(q<1\), then for
\(r=|\alpha|\|Hf\|/(\sqrt\lambda\|f\|)\le q\),

\[
\frac{|O[f]|}{E[f]}
\le
\frac{2r}{1+r^2}
\le
\frac{2q}{1+q^2}.
\]

Therefore the exact normalized contraction margin derived from the norm bound
is

\[
\delta_{\mathrm{aux}}
=
1-
\frac{2q}{1+q^2}
=
\frac{(1-q)^2}{1+q^2}.
\]

This converts the earlier shifted-resolvent estimate into the same normalized
margin language used by the nested Schur audit.

## Absolute coercivity

The reverse triangle inequality gives

\[
D_\pm[f]
\ge
\frac12
\left(
\sqrt\lambda-|\alpha|M
\right)^2
\|f\|^2.
\]

Thus the absolute auxiliary scale is

\[
s_0
=
\frac\lambda2(1-q)^2.
\]

Both quantities are required:

- \(\delta_{\mathrm{aux}}\) controls normalized even--odd saturation;
- \(s_0\) controls the inverse and triangular realization in the source
  frame.

## Theta-mass specialization

For a positive half-line theta kernel,

\[
M
=
M_\Phi
=
\int_0^\infty\Phi(r)\,dr
\]

under the frozen normalization. The whole auxiliary theorem then reduces to

\[
q_p
=
\frac{|\alpha_p|M_\Phi}{\sqrt{\lambda_p}}
<1.
\]

Uniform completion requires

\[
\sup_p q_p<1
\]

and a uniform positive lower bound for \(\lambda_p\) in the declared
source frame.

## Relation to the differential connection carrier

The operator \(H\) in the shifted-history square and the transported
derivative \(T_n\) need not be identical. The differential curvature
constructs the reciprocal-odd carrier; the causal integral history may
provide the bounded propagation on that carrier.

The missing comparison theorem must establish the factorization connecting
them. Substituting \(T_n\) directly for \(H\) is invalid because \(T_n\)
is not bounded on the full Sobolev topology.

## Hostile

Use the square identity but omit the bound \(q<1\). Every finite block is
nonnegative, yet approximate vectors can make
\(\sqrt\lambda f\pm i\alpha Hf\) tend to zero. Positivity without the
history-mass exclusion gives no completion margin.

## Frontier

Conditional on the exact shifted-history square and its normalization, the
auxiliary operator theory is finished:

\[
q<1
\Longrightarrow
\delta_{\mathrm{aux}}
=
\frac{(1-q)^2}{1+q^2}>0,
\qquad
s_0
=
\frac\lambda2(1-q)^2>0.
\]

The unresolved source arrow is now the identification of the bounded causal
history in this square with the reciprocal-odd curvature carrier produced by
the window-to-theta connection defect.
