# The completed xi section is entirely an integrality-defect readout

## Integer source and Haar replacement

Let

\[
\Psi(t)=\sum_{n\geq1}e^{-\pi n^2t}.
\]

Its additive Haar-continuum replacement is

\[
\Psi_{\mathrm H}(t)
=\int_0^\infty e^{-\pi x^2t}\,dx
=\frac1{2\sqrt t}.
\]

Define the lattice discrepancy

\[
\Delta(t)=\Psi(t)-\Psi_{\mathrm H}(t).
\]

In the open critical strip, the completed Mellin representation is

\[
\Lambda(s)
=\frac1{s(s-1)}
+\int_1^\infty
\Psi(t)\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
\]

The two Haar half-integrals are elementary:

\[
\int_1^\infty\frac1{2\sqrt t}t^{s/2}\frac{dt}{t}
=\frac1{1-s},
\]

\[
\int_1^\infty\frac1{2\sqrt t}t^{(1-s)/2}\frac{dt}{t}
=\frac1s.
\]

Their sum is

\[
\frac1{1-s}+\frac1s
=-\frac1{s(s-1)}.
\]

It cancels the completion carrier exactly. Therefore

\[
\Lambda(s)
=\int_1^\infty
\Delta(t)\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
\]

Equivalently, with (P(s)=s(s-1)/2),

\[
\xi(s)
=P(s)\int_1^\infty
\Delta(t)\left(t^{s/2}+t^{(1-s)/2}\right)\frac{dt}{t}.
\]

## Meaning of the cancellation

If the integer labels are replaced by the Haar continuum while the completed
carrier is retained, the completed scalar section is identically zero. Thus
the nonzero xi section is not the continuum carrier with a small arithmetic
perturbation. It is entirely the readout of the integer-lattice minus
Haar-continuum discrepancy.

This gives a precise version of the operator's loss-of-integrality intuition.
Removing integrality does not create a few exceptional zeros. It destroys the
distinction everywhere: the completed scalar readout becomes null for every
spectral parameter.

Conversely, an individual Riemann zero should not be described as integrality
itself failing. Integrality is present and supplies the entire section. A zero
is a cancellation inside the transform of its discrepancy from the continuum
reference.

## The hidden control channel

The earlier decomposition

\[
\xi=C+U+V
\]

treated the carrier \(C=1/2\) as an independent channel. The present identity
shows that, relative to the Haar source, this carrier is the exact
counterchannel to the continuous part of \(U+V\). After forming that pullback,
only the lattice discrepancy survives.

So the faithful architecture starts with the integer source, separates its
Haar-continuum component from its lattice discrepancy, cancels the continuum
component against the carrier, and only then produces \(\xi\).

The continuum component and completion carrier form a null pair. The
discrepancy is the physical scalar channel.

## Consequence for the RH programme

The remaining zero-confinement theorem should be sought directly on the
signed discrepancy \(\Delta\), not on the positive theta sum alone. This also
explains why positivity of the original source repeatedly failed to orient
the oscillatory transform: completion projects away its continuum-positive
mode before producing \(\xi\).

The new hard target is:

> Prove that the reciprocal transform of the exact lattice discrepancy can
> vanish only when the two reciprocal spectral sectors are related by the
> unitary seam involution.

This is narrower than the preceding positive-source problem, but also more
honest: \(\Delta\) is signed. Any successful orientation must come from the
integer/Haar comparison and Poisson sewing, not pointwise positivity.

## Hostile tests

Three counterfactuals now have distinct meanings.

1. Replace the lattice by Haar continuum. The completed section vanishes
   identically.
2. Preserve the Haar term but alter the discrepancy. This changes the entire
   scalar section and is the natural location for hostile off-seam divisors.
3. Alter the completion carrier without altering the Haar reference. This
   breaks the exact null-pair identity before zeros are examined.

The strongest next falsifier is a noninteger self-dual sampling measure whose
Haar discrepancy obeys the same Poisson sewing law but has an off-seam zero.
It would determine whether integer support itself, rather than merely
self-duality of the discrepancy, supplies the missing force.

## Operator stimulus

The operator proposed that zeros arise where a completed relation loses
meaning because integrality has failed after the two half-plane sectors become
distinct. The calculation corrects and sharpens that intuition: loss of
integrality makes the readout meaningless everywhere, while actual zeros are
isolated cancellations of the surviving integrality-defect transform.
