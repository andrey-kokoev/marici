# Fourier reciprocity exchanges two rigged Clifford charts; it need not preserve one

## 1. Rigged sequence space

Let

\[
  E\subset H\subset E'
\]

be a nuclear or Hilbert-scale rigging of the place-current space. A model is

\[
  s\subset\ell^2\subset s',
\]

where \(s\) denotes rapidly decreasing sequences and \(s'\) slowly growing
distributional sequences.

The all-place charge and all-ones current exist naturally in \(E'\), not in
\(E\) or generally in \(H\).

## 2. Two hyperbolic charts

Instead of demanding one Fourier-stable hyperbolic space, define

\[
  \mathcal C_+=E\oplus E',
\]

and

\[
  \mathcal C_-=E'\oplus E.
\]

The first chart pairs a test current with a distributional charge; the second
pairs a distributional current with a test charge. Their split forms are
well typed because every contraction is an \(E'\)-against-\(E\) pairing.

The quarter-turn is a correspondence

\[
  J:\mathcal C_+\longrightarrow\mathcal C_-,
  \qquad
  J(x,\alpha)=(\alpha,-x).
\]

It need not be an automorphism of either chart separately.

\[
\boxed{
\text{Fourier reciprocity exchanges two valid riggings
rather than preserving one impossible rigging}.}
\]

## 3. Charge spinors in the two charts

In \(\mathcal C_+\), the product-formula covector

\[
  \varepsilon\in E'
\]

defines the pure-spinor relation

\[
  L_+
  =
  \ker\varepsilon
  \oplus
  \mathbb C\varepsilon.
\]

Its quarter-turned partner lies in the other chart:

\[
  L_-=JL_+.
\]

The distributional all-ones current is therefore not an illegal vector in
the first chart. It is a legitimate distributional current in the second
chart.

This resolves the algebraic Fourier-escape defect without forcing a
distribution into the positive Fisher Hilbert space.

## 4. Why a smoothing bridge is necessary

Elements of \(E'\) cannot generally be paired with other elements of \(E'\).
Therefore the two distributional spinors do not possess an automatic scalar
overlap.

A comparison requires a continuous smoothing map

\[
  K_\Phi:E'\longrightarrow E
\]

or a nuclear bilinear kernel derived from the completed theta source. Then a
cross-chart pairing such as

\[
  \langle\varepsilon,K_\Phi J\varepsilon\rangle
\]

is well typed.

This places theta completion in a precise role:

\[
\boxed{
\text{theta is the smoothing comparison between two distributional
Clifford localizations}.}
\]

It is not merely an extra factor attached to a pre-existing scalar product.

## 5. Relation to earlier heat compression

The source diffusion heat operator is a candidate smoothing bridge:

\[
  e^{-tA_\Phi}:E'\longrightarrow E
\]

for \(t>0\) under appropriate nuclearity estimates. But a fixed arbitrary
heat time remains regulator data, and the long-time limit collapses to the
rank-one vacuum channel.

The correct bridge must therefore be selected by modular covariance or be a
regulator-independent relative kernel. The two-chart formulation explains
why smoothing is structurally necessary while preserving the earlier
regulator warning.

## 6. Scalar half-planes as shadows

Character transport acts with opposite analytic variance on the two charts.
Their domains of bounded or continuous action project to opposite
half-planes. Thus:

\[
\boxed{
\text{the two half-planes are scalar domains of two different rigged
Clifford localizations}.}
\]

The critical line is their common unitary boundary, where the unitary
vacuum-defect theorem identifies scalar zeros with full coupled defects.

## 7. Sharp next theorem

Construct \(E\), \(E'\), and \(K_\Phi(z)\) directly from the completed adelic
theta source and prove:

1. \(J\) exchanges the two rigged Clifford charts;
2. \(K_\Phi(z):E'\to E\) is nuclear in the required domain;
3. its pure-spinor cross-pairing is \(X(z)\) up to a source unit;
4. modular sewing fixes the smoothing normalization;
5. the induced de Branges kernel is positive; and
6. a hostile self-Fourier source fails the construction before zero data.

## 8. Scope

The paired-rigging construction resolves the type mismatch between the
global charge distribution and its Fourier image. It identifies the
necessity and type of a smoothing comparison. No canonical theta smoothing
kernel, spinor pairing identity, Hermite--Biehler positivity, or RH theorem
is constructed.
