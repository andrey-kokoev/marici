# The six theta rows have distinct sharp Hilbert thresholds

## Setup

Let the prime-power carrier have atoms \((p,k)\) with arithmetic size

\[
n(p,k)=p^k.
\]

For \(\alpha\ge0\), define the weighted Hilbert rung

\[
H_\alpha
=
\ell^2\!\left(\{(p,k)\},p^{2\alpha k}\right).
\]

A scalar row \(b=(b_{p,k})\) is continuous on \(H_\alpha\) exactly when

\[
\sum_{p,k}|b_{p,k}|^2p^{-2\alpha k}<\infty.
\]

This separates the counting density of a channel from the decay already present in its physical coefficient.

## Constant rows

On a fixed grade \(k\), the constant row \(b_{p,k}=1\) is continuous exactly when

\[
\sum_p p^{-2\alpha k}<\infty.
\]

The prime Dirichlet series has abscissa \(1\), so the sharp threshold is

\[
\alpha>\frac1{2k}.
\]

Consequently:

- primitive-support constant row: \(\alpha>1/2\);
- square-support constant row: \(\alpha>1/4\);
- connected support \(k\ge3\): \(\alpha>1/6\), governed by \(k=3\).

If the seam or endpoint row ranges over every prime-power grade, the primitive support dominates and forces \(\alpha>1/2\).

At the boundary value, the corresponding partial dual norm diverges. For the all-integer augmentation this is harmonic divergence; for prime support it is prime-harmonic divergence.

## Physical Euler rows

The logarithmic Euler current at grade \(k\) has coefficient of the form

\[
b_{p,k}=\frac{\log p}{k}p^{-k/2}.
\]

Its squared dual norm on \(H_\alpha\) is controlled by

\[
\sum_p
\frac{(\log p)^2}{k^2}
p^{-k(1+2\alpha)}.
\]

This yields a different hierarchy.

### Primitive grade

For \(k=1\),

\[
\sum_p(\log p)^2p^{-1-2\alpha}
\]

converges for every \(\alpha>0\) and fails at \(\alpha=0\). The primitive physical row therefore needs arbitrarily small positive exponential regularity, not the stronger \(\alpha>1/2\) required by a constant endpoint row.

### Square grade

For \(k=2\),

\[
\sum_p(\log p)^2p^{-2-4\alpha}
\]

already converges at \(\alpha=0\). The square row is a Hilbert covector on the unweighted coefficient module, although its associated operator need not be trace class.

### Connected grades

For \(k\ge3\), the coefficient family is absolutely summable before squaring and belongs to the smooth uniform-Bohr algebra. It is stronger than merely Hilbert-continuous.

## Exact hierarchy

The topology gate is therefore not simply ordered by the verbal labels “primitive,” “square,” and “connected.” It depends on both support density and coefficient decay:

| Row | Sharp requirement |
|---|---|
| Constant seam/endpoint over all prime powers | \(\alpha>1/2\) |
| Physical primitive Euler row | \(\alpha>0\) |
| Physical square Euler row | \(\alpha\ge0\) |
| Connected \(k\ge3\) Euler tail | smooth uniform-Bohr |

The endpoint/seam evaluation is the strictest weighted-Hilbert row among these arithmetic channels.

## Adams motion

Adams transport sends \((p,k)\) to \((p,rk)\). On weighted Hilbert rungs it has the scale typing

\[
\psi^r:H_{r\alpha}\longrightarrow H_\alpha.
\]

No single positive \(\alpha\) is an internal Hilbert rung for every Adams operation. The projective source core retains all positive \(\alpha\) and makes this scale motion continuous.

## Consequence for the Green domain

Any common graph domain supporting the aggregate seam or endpoint must control a rung above \(\alpha=1/2\), or supply an equivalent estimate. Once that is done, the physical primitive and square rows are automatically continuous as covectors.

This does not prove the Green operator is continuous. Its cross-terms, derivatives, and archimedean coefficients may require stronger regularity. But it locates the first common threshold exactly and prevents the primitive current from being blamed for a stricter requirement actually imposed by endpoint aggregation.

## Finite falsifiers

1. At \(\alpha=1/2\), truncate the constant primitive-support row. Its dual norm diverges.
2. At \(\alpha=0\), truncate the physical primitive row. Its squared norm diverges.
3. At \(\alpha=0\), the physical square row remains bounded; a compiler rejecting it solely because it is grade two confuses arity with growth.
4. Any cancellation between rows must first transport them to a common \(H_\alpha'\) fiber.

## Verdict

The first common arithmetic graph threshold is \(\alpha>1/2\), selected by seam/endpoint aggregation rather than by the physical primitive Euler coefficient. The remaining Green audit should begin above this threshold and then measure only the additional regularity demanded by mixed and archimedean terms.
