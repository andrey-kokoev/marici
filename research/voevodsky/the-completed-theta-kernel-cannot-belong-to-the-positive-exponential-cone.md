# The completed theta kernel cannot belong to the positive exponential cone

## Proposed bridge

The ordered face factorization is proved for positive exponential packets. A direct bridge would require the completed theta kernel on the positive half-line to have a representation

\[
\Phi(u)
=
\int_{[0,\infty)}
e^{-\alpha u}
\,d\mu(\alpha),
\qquad
\mu\ge0.
\]

Such a representation makes \(\Phi\) completely monotone.

## Seam derivative obstruction

The completed theta kernel extends to a smooth even function on the whole real line. Therefore

\[
\Phi'(0)=0.
\]

Differentiating a positive exponential representation from the right gives

\[
-\Phi'(0+)
=
\int_{[0,\infty)}
\alpha
\,d\mu(\alpha).
\]

The left side is zero. Since the integrand and measure are nonnegative,

\[
\int
\alpha
\,d\mu(
\alpha)=0.
\]

Thus \(\mu\) must be supported at \(\alpha=0\). The represented function would then be constant on the half-line.

But the completed theta kernel is strictly positive at the seam and decays to zero at infinity. It is not constant.

Hence no such positive exponential representation exists.

## Consequence

The differentiated completed theta source does not belong directly to the positive exponential cone used by the rank-two ordered-face Gram factorization.

This agrees with the earlier local result that the actual theta source enters the two-point Krein-negative corridor near the modular seam. The obstruction is structural and already visible in the first derivative at the seam.

## Grouping limitation

No source-fixed grouping that preserves smooth modular evenness and positivity can repair this obstruction while remaining a positive mixture of decaying exponentials on the half-line. Every such grouped completed kernel still has zero seam derivative and nonconstant decay.

A representation with signed weights, negative rates, or cancellation between reciprocal charts leaves the positive exponential cone and cannot invoke the existing Gram theorem unchanged.

## Revised role of the positive-mode theorem

The positive-mode factorization remains a valid comparison theorem and a diagnostic model. It cannot be transferred to the completed theta source by direct cone membership.

A viable common-state intertwiner would need a type-changing operation, such as:

1. a boundary quotient that removes the even seam constraint;
2. a derivative or tail transform that converts the theta kernel into a completely monotone object while preserving the Xi zero-state;
3. a larger positive dilation whose compressed source is theta but whose ambient modes are exponential;
4. a signed Krein representation with an independently proved contraction of its negative channel.

The transform must preserve the ordered flux and zero-state relation. Applying an arbitrary Laplace or Bernstein transform would not suffice.

## Disposition

Direct positive-exponential cone membership is rejected:

\[
\Phi'(0)=0,
\qquad
\Phi(0)>0,
\qquad
\lim_{u\to\infty}
\Phi(u)=0.
\]

These three properties are incompatible with a positive mixture of decaying exponentials.

The ordered-face route now requires a dilation or quotient, not a direct source identification.
