# The Adams-to-endpoint comparison is finite only on the source-generated wall--jump plane

## Typing and bounded direction

The analytic window carrier and doubled theta endpoint carrier have different
completion scales. The raw Stieltjes disagreement

\[
d_p=W_{2\log p}-W_{\log p}
\]

becomes super-polynomially soft, while the theta odd Wronskian vector

\[
j_\theta
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}
\]

has fixed nonzero norm.

Therefore a uniformly bounded comparison cannot point from the raw window
carrier to the fixed theta odd port. The completion-stable direction is

\[
\text{theta wall--jump plane}
\longrightarrow
\text{Stieltjes wall--jump plane}.
\]

This corrects the tempting but false requirement of a prime-uniform lower
bound for a window-to-theta coefficient.

## The two finite planes

Let

\[
E_p^\theta
=
\operatorname{span}\{w_\theta,j_\theta\}
\]

be the source-generated theta endpoint plane, and let

\[
E_p^{\mathrm{win}}
=
\operatorname{span}\{w_p,d_p\}
\]

be the corresponding Stieltjes wall--disagreement plane.

Reciprocal reflection acts evenly on the wall generators and oddly on the
jump generators. Hence every reflection-equivariant comparison

\[
K_p:E_p^\theta\to E_p^{\mathrm{win}}
\]

is diagonal:

\[
K_pw_\theta
=
k_{\mathrm{wall},p}w_p,
\qquad
K_pj_\theta
=
k_{\mathrm{jump},p}d_p.
\]

The source normalization used by the established reverse comparison is

\[
K_pj_\theta=d_p.
\]

In the normalized reciprocal basis

\[
e_{\mathrm{jump}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
-1
\end{pmatrix},
\qquad
j_\theta=\frac1{2\sqrt2}e_{\mathrm{jump}},
\]

this is equivalently

\[
K_pe_{\mathrm{jump}}=2\sqrt2\,d_p.
\]

## Why decay is admissible

The operator norm of the odd branch satisfies

\[
\|K_p|_{\mathrm{odd}}\|
=
2\sqrt2\,\|d_p\|_{\mathrm{win}},
\]

which tends to zero super-polynomially in the raw Stieltjes norm. This is not a
completion defect. It is precisely why the theta-to-window map is bounded and
even trace class after prime assembly.

The inverse direction would have norm proportional to
\(\|d_p\|_{\mathrm{win}}^{-1}\) and therefore cannot act continuously in the
declared finite exponential-order topology.

Thus the endpoint matrix lower bound \(1/4\) belongs to the retained theta
signal port. It must not be transported backward through \(K_p\) as a lower
bound on the soft window carrier.

## Closed relation rather than isomorphism

The correct comparison object is the graph

\[
\Gamma(K_p)
=
\{(y,K_py):y\in E_p^\theta\}
\subset
E_p^\theta\oplus E_p^{\mathrm{win}}.
\]

Projection to the theta coordinate is a left inverse, so

\[
\|(y,K_py)\|\ge\|y\|.
\]

Therefore the graph is closed with lower bound one even though the window
component collapses. The faithful theta coordinate remains retained; the
Stieltjes component is a compact or trace-class shadow.

This is the same paired-port mechanism that repaired scalar theta synthesis.
One does not demand that every shadow be invertible when the source coordinate
is still present.

## Endpoint composition

The source endpoint observer acts first:

\[
V_p:E_p^\theta\to E_p^\theta,
\]

with

\[
\sigma_{\min}(V_p)\ge\frac14.
\]

The Stieltjes shadow then has the typed direction

\[
K_pV_p:E_p^\theta\to E_p^{\mathrm{win}}.
\]

On the odd vector,

\[
K_pV_pe_{\mathrm{jump}}
=
2\sqrt2\,
\lambda_{\mathrm{jump},p}
d_p,
\]

where

\[
\lambda_{\mathrm{jump},p}
=
\frac12(1-p^{-1}).
\]

This formula fixes the endpoint coefficient once the reverse comparison
\(K_pj_\theta=d_p\) is source-authorized.

## What remains to prove

The numerical normalization is no longer the main uncertainty. The required
constructor theorem is the trace identity showing that the independently
constructed causal/anti-causal theta history maps to the independently
constructed four-front Stieltjes disagreement by \(K_p\), with

\[
K_pj_\theta=d_p,
\]

rather than this equality being adopted as a definition.

That theorem must preserve:

- reciprocal sign;
- prime label;
- ordered primitive;
- wall routing;
- cutoff restriction;
- and the declared theta-to-window bounded direction.

## Hostile

Reverse the arrow and demand a uniformly bounded inverse. Every finite prime
plane is algebraically isomorphic, but the inverse norms grow faster than any
fixed power of \(p\). The completed constructor fails although all finite
rank tests pass.

A second hostile discards the theta coordinate after forming \(K_p\). Then the
trace-class window shadow is no longer faithful, and the earlier closed-range
margin disappears.

## Verdict

The Adams-to-endpoint comparison is a closed graph of a bounded
theta-to-window compression, not a uniformly invertible identification.

The endpoint odd port remains uniformly faithful in the theta coordinate.
Its Stieltjes image is allowed to become soft. The live source identity is now

\[
K_pj_\theta=d_p
\]

with the arrow direction, sign, and provenance proved from the causal-history
Green/Stokes constructor.
