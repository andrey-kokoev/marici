# Connes semilocal Theorem 4 realizes finite-place Weil terms as the finite part of a product-cutoff trace, not a positive trace

## Source

Alain Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Mathematica 5 (1999), arXiv:math/9811068, Section VII, Theorem 4.

This is reference [7] cited by Connes--Consani--Moscovici, arXiv:2310.18423.

## Semilocal Hilbert carrier

Let `S` be a finite set of places containing all archimedean places. Connes defines

\[
A_S=
\prod_{v\in S}k_v,
\qquad
X_S=A_S/O_S^*,
\]

and the Hilbert space

\[
\mathcal H_S=L^2(X_S).
\]

The semilocal idele class group

\[
C_S=J_S/O_S^*
\]

acts unitarily by scaling:

\[
(U(g)\xi)(x)=\xi(g^{-1}x).
\]

For a smooth compactly supported function `h` on `C_S`, define

\[
U(h)=
\int_{C_S}h(g)U(g)dg.
\]

All active places therefore act on one common semilocal Hilbert carrier. Prime translations are inside the same scaling representation `U`, not separate scalar endpoint coordinates.

## The two cutoffs

Let

\[
P_\Lambda
=
1_{\{|x|\le\Lambda\}}
\]

be the infrared multiplication projection. Let `F` be the semilocal Fourier transform and define

\[
\widehat P_\Lambda
=F P_\Lambda F^{-1}.
\]

The trace cutoff is

\[
\boxed{
R_\Lambda
=P_\Lambda\widehat P_\Lambda.
}
\]

Crucially, this is the product of two orthogonal projections. Unless they commute,

\[
R_\Lambda^*
=
\widehat P_\Lambda P_\Lambda
\ne
R_\Lambda.
\]

Thus `R_Lambda` is generally neither an orthogonal projection nor a positive operator.

## Exact semilocal trace theorem

Theorem 4 states that, as `Lambda -> infinity`,

\[
\boxed{
\operatorname{Tr}
\left(R_\Lambda U(h)
ight)
=
2h(1)\log\Lambda
+
\sum_{v\in S}
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u
+
o(1).
}
\]

The prime denotes the uniquely normalized principal-value distribution whose Fourier transform, relative to the chosen basic additive character, vanishes at `1`.

The finite sum of local principal-value terms is exactly the contribution of the places in `S` to the Weil explicit formula.

## Exact finite-part identity

Define

\[
W_S(h)
=
\sum_{v\in S}
\int_{k_v^*}^{\prime}
\frac{h(u^{-1})}{|1-u|_v}d^*u.
\]

Then Theorem 4 is equivalently

\[
\boxed{
W_S(h)
=
\lim_{\Lambda\to\infty}
\left[
\operatorname{Tr}(R_\Lambda U(h))
-
2h(1)\log\Lambda
\right].
}
\]

The remainder is `o(1)` after this subtraction. It is not a fixed finite-rank endpoint operator.

## Convolution-square insertion

If

\[
h=g*g^*,
\]

then the unitary group representation gives

\[
U(h)=U(g)U(g)^*
\succeq0.
\]

However,

\[
\operatorname{Tr}
\left(
R_\Lambda U(g)U(g)^*
\right)
\]

is not automatically nonnegative because `R_Lambda` is not positive or self-adjoint.

Cyclicity does not repair this:

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda AA^*)
=
\operatorname{Tr}
(\widehat P_\Lambda AA^*P_\Lambda),
\]

which is not of the form `Tr(B*B)` unless additional commutation or sewing identities are proved.

Therefore Theorem 4 is a genuine operator trace formula but not a positive trace formula.

## Divergent evaluation term

For a convolution square,

\[
h(1)
=
\|g\|_{L^2(C_S)}^2
\]

under the standard group-convolution normalization. Hence the divergent term is positive:

\[
2h(1)\log\Lambda
=
2\log\Lambda\|g\|^2.
\]

But the Weil local functional is obtained only after subtracting this positive divergence. Positivity of the unrenormalized leading trace therefore says nothing about positivity of the finite part.

This is the trace-level analogue of the Poisson decomposition into a positive bulk and a diverging Plancherel baseline.

## Where prime translations act

The finite-place terms arise from fixed-point/orbit contributions in the trace of the common scaling representation `U(h)` on `L2(X_S)`. For `k=Q`, the local integral at `p` expands into the complete prime-power tower. Thus prime shifts occur inside `U(h)` before the trace is taken.

They are not a finite-rank correction to the archimedean trace. The cutoff product `P_Lambda F P_Lambda F^-1` couples physical support and Fourier support and is infinite-rank.

This answers the first open gate affirmatively:

\[
\boxed{
\text{prime channels lie inside one semilocal operator trace bulk.}
}
\]

## Sign and positivity audit

The theorem supplies:

1. one common semilocal Hilbert space;
2. one scaling representation containing all active places;
3. an exact asymptotic trace formula;
4. the finite-place Weil functional as its renormalized finite part.

It does **not** supply:

1. positivity of `R_Lambda`;
2. positivity of `Tr(R_Lambda U(g)U(g)*)`;
3. positivity after subtracting `2 log Lambda ||g||^2`;
4. a finite-rank remainder;
5. a comparison identifying the negative cutoff sector with Suzuki's cokernel.

## Product-of-projections structure

Although `R_Lambda=P_Lambda hat P_Lambda` is not positive, the related compression

\[
P_\Lambda\widehat P_\Lambda P_\Lambda
=
(P_\Lambda\widehat P_\Lambda)
(P_\Lambda\widehat P_\Lambda)^*
\succeq0
\]

is positive. The difference between the theorem's trace and a trace using this positive compression is

\[
\operatorname{Tr}
\left[
P_\Lambda\widehat P_\Lambda
(I-P_\Lambda)
U(h)
\right]
\]

up to cyclic rearrangement and domain conventions.

This is an infinite-rank boundary/sewing term. Determining its finite part is the concrete positivity problem suggested by the theorem.

## Transition under adding places

When `S` is enlarged, both the space `X_S` and scaling group `C_S` change, and Theorem 4 adds the corresponding local principal-value distribution to the finite part. The source theorem does not state a transition intertwiner identifying

\[
R_{\Lambda,S}
\]

with

\[
R_{\Lambda,S\cup\{p\}}.
\]

The later Sonin isomorphism supplies Hilbert-space stability, but compatibility of the product-cutoff trace under that isomorphism remains to be derived.

## Exact remaining comparison

Let

\[
A_g=U(g).
\]

A positive candidate is

\[
\operatorname{Tr}
\left(
P_\Lambda\widehat P_\Lambda P_\Lambda
A_gA_g^*
\right)
=
\|
\widehat P_\Lambda P_\Lambda A_g
\|_{HS}^2
\]

when Hilbert--Schmidt conditions hold.

The theorem instead controls

\[
\operatorname{Tr}
\left(
P_\Lambda\widehat P_\Lambda
A_gA_g^*
\right).
\]

Thus the exact next remainder is

\[
\boxed{
\mathcal E_{\Lambda,S}(g)
=
\operatorname{Tr}
\left(
P_\Lambda\widehat P_\Lambda
(I-P_\Lambda)
A_gA_g^*
\right).
}
\]

One must compute its finite part, sign, and transition compatibility. It cannot be assumed finite-rank.

## Disposition

The precise semilocal trace theorem has now been extracted:

\[
\boxed{
W_S(h)
=
\operatorname*{FP}_{\Lambda\to\infty}
\operatorname{Tr}
\left(
P_\Lambda\widehat P_\Lambda U(h)
\right).
}
\]

Prime translations do occur inside a single common operator trace bulk. But the cutoff is a non-self-adjoint product of projections, and the Weil functional is a renormalized finite part after subtracting a positive divergence. The theorem does not prove positivity on convolution squares.

The next viable calculation is the finite part of the sewing remainder `E_Lambda,S(g)` comparing the product cutoff with the positive triple compression.
