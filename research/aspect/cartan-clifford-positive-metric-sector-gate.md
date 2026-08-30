# Cartan–Clifford positive-metric sector gate

## Question

The graded identity supplies a finite contraction away from the seam. Can its
two-mode Clifford generator also be the positive-metric self-adjoint carrier
needed for a collocated Weyl and bordered-determinant explanation on both
half-sectors?

## Clifford generator

For the minimal pair, set

\[
C_a=d_a+Q=
\begin{pmatrix}
0&a\\
1&0
\end{pmatrix}.
\]

The Cartan identity is equivalent to

\[
C_a^2=aI.
\]

Let a real symmetric carrier metric be

\[
H=
\begin{pmatrix}
x&y\\
y&z
\end{pmatrix}.
\]

Metric self-adjointness, `HC_a=C_a^T H`, is equivalent to the single equation

\[
z=ax.
\]

The determinant of every such metric is therefore

\[
\det H=ax^2-y^2.
\]

With `x` positive, this determinant can be positive exactly when `a` is
positive. Thus the minimal Cartan–Clifford carrier admits a positive
self-adjoint realization if and only if it lies in the positive-normal
half-sector.

## Three regimes

For positive `a`, choose `H=diag(1,a)`. When `a=4`, the similarity
`S=diag(1,2)` produces the ordinary symmetric carrier

\[
SC_aS^{-1}=
\begin{pmatrix}
0&2\\
2&0
\end{pmatrix}.
\]

For negative `a`, the same formula gives an indefinite metric. The generator
is Krein-self-adjoint but cannot be conjugated to a Hilbert-self-adjoint
carrier. For `a=0`, the metric degenerates. No uniformly positive similarity
continues through the seam.

This is stronger than saying that square roots require different branches.
Positive collocation itself is sector-limited.

## Bordered-Weyl consequence

In the positive example, take the first coordinate as a collocated port. The
symmetric carrier has determinant denominator `z^2-4`, diagonal Weyl
coefficient `-z/(z^2-4)`, and bordered numerator `z`. Kitaev’s finite bridge
therefore works exactly inside that half-sector.

The same positive-Herglotz argument cannot simply be transported to negative
`a`. There the carrier needs an indefinite metric, and at the seam the metric
loses invertibility. Hence the Cartan contraction and the positive-Weyl bridge
do not combine into one global positive carrier.

The architecture must retain two sector realizations plus an independently
typed sewing law. This supports Kitaev’s corrected conclusion: parity balance
is an eligibility condition on each sector complex, not evidence for an
additional sixth cohomology class.

## Optical meaning

A passive reciprocal two-mode coupler has return amplitude conjugate to its
forward amplitude, so their product is a nonnegative square magnitude. It can
realize the positive `a` sector. A signed negative product requires an active,
non-Hermitian, phase-reversed, or indefinite-metric element; that forfeits the
ordinary positive-collocation premise unless a larger source-authorized
dilation restores it.

The decisive experiment is therefore sector-comparative:

1. reconstruct `dQ+Qd` by signed heterodyne tomography;
2. reconstruct the carrier metric from calibrated energy flux;
3. test `HC=C^T H` and the smallest metric eigenvalue;
4. approach the seam from both sides;
5. reject any claimed global positive-Weyl realization if the metric changes
   signature or its lower eigenvalue tends to zero.

## Claim boundary

This is an exact finite metric obstruction and positive-sector bordered-Weyl
control. It neither derives `Q` from theta/Tate sources nor identifies the
bordered numerator with the completed theta section. Infinite completion and
reciprocal sewing remain separate gates.

## Verification

Run:

```text
python research/aspect/checkers/check_cartan_clifford_positive_metric_sector_gate.py
```
