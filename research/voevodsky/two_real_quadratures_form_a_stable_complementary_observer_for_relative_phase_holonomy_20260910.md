# Two Real quadratures form a stable complementary observer for relative-phase holonomy

## Question

What is the smallest explicit complementary observer that reconstructs the oriented relative phase of a two-sewing holonomy?

## Claim boundary

The Real trace quadrature alone identifies a phase with its inverse. Adding the oriented skew quadrature gives an isometric embedding of \(U(1)\) into \(\mathbb R^2\) and reconstructs the phase exactly. This is a stable finite-dimensional complementary-observer example, not an essential observer for an infinite carrier.

## Problem

Let

\[
z=v/u\in U(1)
\]

be the relative phase, and let the two-sewing holonomy be

\[
H(z)=
\begin{pmatrix}
z^{-1}&0\\
0&z
\end{pmatrix}.
\]

Real conjugation sends

\[
H(z)\longmapsto H(z^{-1}).
\]

A Real scalar trace cannot distinguish the two loop orientations.

## Bold conjecture

The trace of the holonomy is a faithful stable observer of oriented relative phase.

## Named rivals

1. The trace retains only the cosine quadrature and has a generic two-point fiber.
2. A second skew quadrature restores exact phase reconstruction.
3. Any two nonconstant Real functions on \(U(1)\) suffice stably.
4. Intensity-only channel measurements can recover the same information.

## Trace quadrature

Define

\[
P(z)=\frac12\operatorname{tr}H(z)
=\frac12(z+z^{-1}).
\]

Writing \(z=e^{i\theta}\),

\[
P(z)=\cos\theta.
\]

Therefore

\[
P(z)=P(z^{-1}).
\]

Except at \(z=\pm1\), the fiber contains the two distinct oriented phases

\[
\{z,z^{-1}\}.
\]

The bold conjecture fails.

## Skew quadrature

Define

\[
Q(z)
=
\frac{H_{22}(z)-H_{11}(z)}{2i}
=
\frac{z-z^{-1}}{2i}.
\]

Then

\[
Q(e^{i\theta})=\sin\theta
\]

and

\[
Q(z^{-1})=-Q(z).
\]

This is the oriented quadrature erased by the Real trace.

## Exact reconstruction theorem

The joint observer

\[
\Psi:U(1)\to\mathbb R^2,
\qquad
\Psi(z)=(P(z),Q(z))
\]

is injective, with inverse

\[
z=P(z)+iQ(z).
\]

Its image is the unit circle

\[
P^2+Q^2=1.
\]

Thus \(Q\) is a genuine complement to the trace observer \(P\).

## Stability

For \(z,w\in U(1)\),

\[
\|\Psi(z)-\Psi(w)\|_{\mathbb R^2}^2
=
|z-w|^2.
\]

Hence \(\Psi\) is an isometry for chordal distance. It has exact global stability constant one.

Infinitesimally, for \(z=e^{i\theta}\),

\[
\frac{d}{d\theta}\Psi(e^{i\theta})
=(-\sin\theta,\cos\theta),
\]

so

\[
\left\|\frac{d}{d\theta}\Psi(e^{i\theta})\right\|=1.
\]

Each scalar quadrature separately has critical points, while the pair has no differential rank loss.

## Minimality among continuous Real scalar readouts

No continuous injective map from the circle to the real line exists: a compact connected one-dimensional manifold cannot embed in \(\mathbb R\). Therefore one continuous Real scalar cannot globally reconstruct oriented phase. Two real coordinates are minimal for this embedding class.

Rival 3 is false: two functions suffice only when their joint map is injective with a quantitative embedding bound. For example, \((P,2P)\) remains twofold ambiguous.

## Intensity no-go

The diagonal entries of \(H(z)\) have unit modulus:

\[
|H_{11}(z)|=|H_{22}(z)|=1.
\]

Any observer depending only on separate channel intensities is constant in \(z\). Relative phase requires coherent cross-channel or quadrature-sensitive readout. Rival 4 fails.

## Real structure

Under loop reversal or Real conjugation,

\[
(P,Q)\longmapsto(P,-Q).
\]

Thus:

- \(P\) is Real-even and orientation-forgetting;
- \(Q\) is Real-odd and orientation-sensitive;
- the pair retains the full oriented phase with a transparent Real action.

Neither quadrature should be called non-Real: both are real-valued. Their difference is parity under the Real involution on the phase moduli.

## Complementary-observer interpretation

This is a nonlinear finite-dimensional analogue of the row-observer theorem. The first channel \(P\) has a twofold global ambiguity and local rank loss at \(z=\pm1\). The complement \(Q\) removes both defects, and the joint map has a uniform metric lower bound.

However, \(\Psi\) observes only one \(U(1)\) holonomy. As an observer on an infinite radial carrier it is finite-rank and cannot supply an essential Calkin margin.

## Sewing-network extension

For a graph with first Betti number \(b_1\), choose a cycle basis with holonomies

\[
z_1,\ldots,z_{b_1}.
\]

Applying \((P,Q)\) to each cycle gives an isometric product embedding

\[
U(1)^{b_1}\hookrightarrow\mathbb R^{2b_1}
\]

for the product chordal metric. A different cycle basis acts by integral monomials on the torus; the coordinate presentation changes while the character remains the same.

## Constructor-role signatures

The roles are:

- `real_trace_observer`: \(P\), Real-even, inverse-orbit quotient readout;
- `oriented_skew_observer`: \(Q\), Real-odd, orientation discriminator;
- `relative_phase_complement`: the pair \((P,Q)\), with isometric reconstruction;
- `intensity_observer`: phase-blind and inadmissible for relative-phase reconstruction;
- `essential_observer`: separate infinite-carrier role.

The promotion from two scalar readouts to `relative_phase_complement` requires the explicit inverse and stability identity, not merely nonconstancy.

## Strongest falsification attempt

At \(z=\pm1\), the skew quadrature vanishes, so it may appear unable to complement the trace. But at those points the derivative of \(Q\) has unit magnitude while the derivative of \(P\) vanishes. At \(z=\pm i\), their roles reverse. The joint differential norm remains one everywhere.

## Disposition

The trace-only conjecture is rejected. The cosine and sine quadratures form a minimal, exact, and globally stable observer of oriented relative phase. This is the programme's first positive complementary-observer construction directly inside the Green/Real sewing example, while its finite-dimensional scope remains explicit.
