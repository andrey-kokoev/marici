# Endpoint separation forces a direct summand

## Question

Can an interior positive localizer compensate the exterior endpoint rank-one subtraction at every rank, or must the background factor contain the endpoint vector itself?

## Claim boundary

A separated-support obstruction is proved. It forces an exact endpoint-vector summand in any all-rank compensation factor. Such a summand has not yet been derived from the completed gamma--prime source.

## Setup

In the sharp normalized chart, the desired interior spectral coordinate satisfies

\[
0\leq y\leq q<1.
\]

Let the endpoint vector at rank \(N\) be

\[
v_N=(1,1,\ldots,1)^T.
\]

Suppose the background localizer decomposes as

\[
L_N=A_N+m v_Nv_N^*,
\]

where \(A_N\) is represented by a finite positive measure \(\mu\) on \([0,q]\). The endpoint subtraction is

\[
c v_Nv_N^*.
\]

Then

\[
L_N-cv_Nv_N^*
=A_N+(m-c)v_Nv_N^*.
\]

## Separating monomial

Test the quadratic form with the monomial

\[
p_n(y)=y^n.
\]

It satisfies

\[
p_n(1)=1,
\qquad
\sup_{0\leq y\leq q}|p_n(y)|\leq q^n.
\]

For an interior localizer with weight bounded above by \(q\),

\[
\langle p_n,A p_n\rangle
\leq q^{2n+1}\mu([0,q]).
\]

Therefore

\[
\langle p_n,(L-cvv^*)p_n\rangle
\leq
q^{2n+1}\mu([0,q])-(c-m).
\]

If \(m<c\), this is negative for all sufficiently large \(n\).

## Theorem

A positive factor supported strictly below the endpoint cannot diffusely compensate an exterior endpoint subtraction at all ranks.

For a background of the displayed form, all-rank positivity requires

\[
m\geq c.
\]

Conversely, if \(A_N\geq0\) coherently at every rank and \(m\geq c\), then

\[
A_N+(m-c)v_Nv_N^*\geq0.
\]

Thus the condition is exact in this decomposition.

## Stronger meaning of the Schur gate

The finite-rank range and pseudoinverse conditions can hold approximately because low-degree polynomials do not yet separate \([0,q]\) from \(1\) sharply. But as rank grows, the monomials force separation exponentially.

Hence collapsing Schur margins have a structural interpretation: absent an exact endpoint feature, they must eventually fail. An all-rank Douglas contraction cannot be assembled from unrelated finite-rank compensations.

The required source constructor is stronger than

\[
L_{\Gamma+P}=R^*R.
\]

It must exhibit a compatible splitting

\[
R^*R=A+c vv^*+B,
\qquad A\geq0,
\qquad B\geq0,
\]

where the endpoint feature is exact and coherent under rank restriction, translation in \(t\), and mesh refinement in \(h\).

After subtraction, the endpoint pair cancels and leaves the interior factor.

## Categorical interpretation

The endpoint is not merely an object in the closure of the interior feature span at each finite rank. It must occur as a retract compatible with the inverse system of truncations.

Finite-rank range inclusion supplies lifts

\[
q_N:\mathbb C\to\mathcal H_N.
\]

All-rank positivity requires these lifts to form a bounded compatible cone. Separated support prevents such a cone unless an endpoint direct summand is already present.

Thus packetwise pseudoinverses are insufficient: the proof needs a natural endpoint splitting.

## Exact fixture

For \(q=1/2\), positive atoms at \(0\) and \(1/3\), and endpoint coefficient \(c=3/2\), the checker verifies:

- no endpoint feature produces a negative diagonal by degree three;
- an insufficient feature \(m=1\) produces one by degree four;
- exact mass \(m=c\) leaves the interior Gram localizer;
- excess positive feature leaves a positive rank-one residual.

## Disposition

The endpoint Schur gate has sharpened into a direct-summand problem. If the completed gamma--prime background contains only interior support, the all-rank programme is impossible. To survive, the source formula must expose an exact positive endpoint feature of coefficient at least \(c\), preferably exactly \(c\), before the residual interior positivity problem is attacked.

## Verification

- `research/voevodsky/endpoint-separation-direct-summand-obstruction-v1.json`
- `research/voevodsky/checkers/check_endpoint_separation_direct_summand.py`
- `research/voevodsky/results/endpoint_separation_direct_summand.json`
