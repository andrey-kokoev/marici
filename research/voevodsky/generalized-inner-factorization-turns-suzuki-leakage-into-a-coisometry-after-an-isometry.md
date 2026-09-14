# Generalized-inner factorization turns Suzuki leakage into a coisometry after an isometry

## Factorization hypothesis

Assume the boundary-unimodular meromorphic function admits a coprime generalized-inner factorization

\[
\Theta=\frac{S}{B},
\]

where `S` and `B` are inner in the upper half-plane and `B` contains the upper-half-plane pole divisor of `Theta`. On the real boundary,

\[
\bar\Theta=\bar S B.
\]

After linearizing Suzuki's conjugate leakage, the relevant Toeplitz operator is

\[
L\sim T_{\bar\Theta}=T_{\bar S B}.
\]

## Exact operator product

Because `bar S` is coanalytic, the standard Toeplitz product rule gives

\[
\boxed{
T_{\bar\Theta}=T_{\bar S}T_B.
}
\]

Here

\[
T_B:H^2\to H^2
\]

is an isometry, while

\[
T_{\bar S}=T_S^*
\]

is a coisometry. Thus Suzuki leakage is not arbitrary: it is a coisometry applied after an isometric embedding.

This factorization is exact and preserves the order of the two operations. Reversing them would generally introduce a Hankel correction.

## Kernel

Since

\[
\ker T_{\bar S}=K_S:=H^2\ominus SH^2,
\]

we obtain

\[
\begin{aligned}
\ker T_{\bar\Theta}
&=\{f\in H^2:Bf\in K_S\}\\
&=T_B^{-1}(BH^2\cap K_S).
\end{aligned}
\]

Therefore

\[
\boxed{
V\simeq T_B^{-1}(BH^2\cap K_S).
}
\]

The unconditional Suzuki intersection is the part of the positive model space `K_S` divisible by the forbidden Blaschke factor `B`.

When `B=1`, this reduces to

\[
V\simeq K_S,
\]

which is the ordinary inner/model-space case.

## Projection formula without a pseudoinverse

Let `M=BH^2`, and let `P_{K_S}=I-T_ST_{\bar S}`. For `f in H^2`,

\[
T_{\bar\Theta}f=T_{\bar S}(Bf).
\]

The kernel condition says that the isometric image `Bf` lies in `K_S`. Hence the projection onto `V` is unitarily equivalent, through `T_B`, to projection from `M` onto

\[
M\cap K_S.
\]

Thus the geometry involves two explicit closed subspaces:

\[
BH^2
\quad\text{and}\quad
K_S.
\]

Alternating projections between these spaces construct the kernel projection. The former carries the pole divisor; the latter is positive because `S` is inner.

## Closed-range criterion

The range is

\[
\operatorname{ran}T_{\bar\Theta}
=T_{\bar S}(BH^2).
\]

Since `T_barS` is the quotient map with kernel `K_S`, its restriction to `BH^2` has closed range exactly when the pair of subspaces

\[
BH^2
\quad\text{and}
K_S
\]

has closed sum, equivalently a positive Friedrichs angle away from their intersection.

Concretely, closed range is equivalent to a constant `c>0` such that

\[
\|T_{\bar S}g\|
\ge c\|g\|
\qquad
(g\in BH^2\ominus(BH^2\cap K_S)).
\]

This is the correctly typed Toeplitz coercivity condition.

## Coprime divisor meaning

If `B` and `S` are coprime, a nonzero vector in `BH^2 cap K_S` is highly constrained: it is simultaneously divisible by the forbidden pole factor and orthogonal to every `S`-multiple. The intersection can be trivial even though `K_S` is large.

This explains why the unconditional space `V` may collapse. The projection does not simply remove `B`; it asks the `S` model space to contain vectors carrying the full `B` divisibility condition.

## Relation to arithmetic faithfulness

Even if the intersection is nonzero, it may omit the model kernels needed to interpolate all zero coordinates. Proposition 5.8's faithfulness condition becomes a completeness statement for

\[
BH^2\cap K_S
\]

inside the arithmetic evaluation geometry. Thus the two RH-strength gates have distinct factor meanings:

1. arithmetic isometry compares the Weil form with the norm inherited from `K_S`;
2. interpolation requires the `B`-divisible part of `K_S` to detect every required coordinate.

## Source provenance

The factorization `Theta=S/B` can be regarded as a canonical analytic factorization if bounded-type hypotheses are proved, but `B` still encodes the forbidden interior divisor. The operator identity

\[
T_{\bar\Theta}=T_{\bar S}T_B
\]

therefore classifies the obstruction; it does not eliminate it.

A source-derived proof would need to construct `T_B` or the subspace `BH^2` from endpoint--gamma--prime boundary data without first locating its zeros, and then prove the angle and arithmetic-isometry estimates.

## Disposition

The corrected leakage normal form is

\[
\boxed{
L\sim T_{\bar S}T_B,
\qquad
V\simeq T_B^{-1}(BH^2\cap K_S).
}
\]

It consists of an isometric divisor insertion followed by a positive coisometric quotient. The possible collapse occurs at their incidence intersection, and closed-range coercivity is exactly the angle between `BH^2` and `K_S`.
