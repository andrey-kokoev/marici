# The graph-energy reciprocal blocks are exact shifted-history squares

## Exact factorization

Let \(H=H_+\) be a closed densely defined history operator. Define

\[
S_{\mathrm{gr}}
=
\frac12(I+H^{*}H)
\]

as a closed quadratic form and

\[
T_{\mathrm{hist}}
=
\frac{H-H^{*}}{2}.
\]

Then the reciprocal auxiliary forms are

\[
D_\pm
=
S_{\mathrm{gr}}\pm iT_{\mathrm{hist}}.
\]

They factor exactly:

\[
D_+
=
\frac12(I+iH)^{*}(I+iH),
\]

\[
D_-
=
\frac12(I-iH)^{*}(I-iH).
\]

Indeed,

\[
(I-iH^{*})(I+iH)
=
I+H^{*}H+i(H-H^{*}),
\]

and the opposite sign gives the second identity.

Thus positivity is not merely an inequality consequence. Each reciprocal auxiliary block is a shifted-history Gram.

## Exact kernels

The factorization gives

\[
\ker D_+
=
\ker(I+iH),
\qquad
\ker D_-
=
\ker(I-iH).
\]

Therefore

\[
\ker D_+
=
\{x:Hx=ix\},
\]

\[
\ker D_-
=
\{x:Hx=-ix\}.
\]

The two forbidden auxiliary modes are exactly the reciprocal imaginary unit eigenmodes of history synthesis.

At completion, uniform lower bounds are equivalent to the shifted histories being uniformly bounded below:

\[
\|(I\pm iH)x\|
\ge
c_\pm\|x\|.
\]

Then

\[
D_\pm\ge\frac{c_\pm^2}{2}I.
\]

This is stronger and cleaner than estimating the normalized odd contraction indirectly.

## Approximate-spectrum criterion

Loss of the auxiliary margin occurs precisely when there exist unit vectors \(x_n\) such that

\[
(I+iH)x_n\to0
\]

or

\[
(I-iH)x_n\to0.
\]

Equivalently,

\[
+i\in\sigma_{\mathrm{ap}}(H)
\quad\text{or}\quad
-i\in\sigma_{\mathrm{ap}}(H),
\]

with the sign assigned to the corresponding sheet.

For a normal multiplier \(m(\xi)\), this reduces to the essential range of \(m\) approaching \(+i\) or \(-i\).

## Closed-range qualification

Point-spectrum exclusion is insufficient. Even if

\[
\ker(I\pm iH)=\{0\},
\]

the range may fail to be closed, and the reciprocal Gram may have no positive lower bound. The exact finite-to-completion gate is

\[
\operatorname{dist}
\left(
0,
\sigma\bigl(|I\pm iH|\bigr)
\right)>0.
\]

In non-normal geometry, spectral exclusion alone may still be insufficient for stable inversion; the singular-value or bounded-below statement is authoritative.

## Radical descent becomes transparent

If a reciprocal block is semidefinite, its radical is no longer abstract:

\[
\operatorname{rad}D_\pm
=
\ker(I\pm iH).
\]

Endpoint incidence \(C\) descends precisely when

\[
C\,\ker(I\pm iH)=0
\]

in the convention where \(C\) maps the auxiliary carrier to endpoints.

A common reciprocal quotient requires incidence to annihilate both shifted-history radicals. If the two radicals differ, one must retain sheet-indexed reduced supports rather than silently identify them.

## Resolvent representation

When \(I\pm iH\) is boundedly invertible,

\[
D_\pm^{-1}
=
2(I\pm iH)^{-1}(I\pm iH)^{-*}.
\]

Thus the endpoint Schur return is

\[
CD_\pm^{-1}C^{*}
=
2C(I\pm iH)^{-1}(I\pm iH)^{-*}C^{*}.
\]

The return is the Gram of resolved endpoint incidence through the shifted causal history. This gives a direct route to loading and shear estimates without separately constructing a square root of \(D_\pm\).

## Source-authority gate

The algebra is exact if the source Green energy really is

\[
S_{\mathrm{gr}}
=
\frac12(I_{\mathrm{wall}}+H^{*}H).
\]

The identity carrier must still be proven to be the represented coefficient wall with the correct normalization. Without that, the shifted-history squares are a canonical analytic completion but not yet the authorized Adams auxiliary block.

## Next source calculation

Prove the wall–history identity and then test the two shifted operators

\[
I_{\mathrm{wall}}\pm iH_+
\]

for uniform bounded-below estimates on the prime-labeled reduced rigging. This replaces the abstract auxiliary contraction problem by two explicit singular-value problems.
