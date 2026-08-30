# Theta Tail-Seam Coherency Is a Two-Sheeted Light Cone

## Transform of the primitive cells

Let

\[
U(x,y)=\int_0^\infty\Phi(u)e^{yu}e^{ixu}\,du,
\qquad
V(x,y)=\int_0^\infty\Phi(u)e^{-yu}e^{ixu}\,du.
\]

The cosine transforms of the two reciprocal tail correlations are proportional to (|U|^2) and (|V|^2). The full complex transform of the straddling-seam convolution is

\[
C=UV.
\]

Therefore the primitive function-valued packet assembles into the Hermitian coherency matrix

\[
H=
\begin{pmatrix}
|U|^2 & UV\\
\overline{UV} & |V|^2
\end{pmatrix}.
\]

It is the outer product of the vector (U,\overline V) with its adjoint, so

\[
H\ge0,
\qquad
\operatorname{rank}H=1,
\qquad
\det H=0.
\]

## Stokes and Clifford coordinates

Define

\[
S_0=|U|^2+|V|^2,
\qquad
S_1=2\operatorname{Re}(UV),
\]

\[
S_2=-2\operatorname{Im}(UV),
\qquad
S_3=|U|^2-|V|^2.
\]

The determinant identity becomes the null-cone equation

\[
S_0^2=S_1^2+S_2^2+S_3^2.
\]

After normalization by (S_0), the spatial comparison vector lies on the unit sphere. This is the exact circle-and-sphere geometry suggested by the reciprocal-plane intuition: it is the sphere of relative two-sector coherence, not a circle of zero locations.

## Continuous fiber collapses to two sheets

Scalar completion and the complex seam retain (S_0,S_1,S_2). The rank-one identity then reconstructs

\[
|S_3|
=\sqrt{S_0^2-S_1^2-S_2^2}.
\]

Only the sign of (S_3) is missing. Reciprocal exchange swaps (U) and (V), fixes (S_0,S_1,S_2), and reverses (S_3). Thus the apparent continuous antisymmetric kernel of the linearized cell observation collapses, on the physical rank-one coherency locus, to a two-sheeted orientation fiber.

The sheets meet where

\[
S_3=0,
\qquad
|U|=|V|.
\]

This is exactly the Hermite–Biehler equality locus. The RH-bearing question is no longer reconstruction of an arbitrary missing amplitude. It is whether source dynamics permits the coherency state to cross from one light-cone sheet to the other inside an open reciprocal sector.

## Relation to the additional comparison channel

The odd tangent and Clark quadrature are needed to orient the sheet. But their role is now smaller and sharper than reconstructing an infinite unconstrained fiber: the seam coherence already fixes the magnitude. The odd port must select and continuously transport one of two signs.

This also corrects the finite-moment hostile's scope. Finite moments cannot reconstruct an arbitrary positive separation measure. On the source-derived rank-one coherency locus, however, the full complex seam imposes a nonlinear determinant constraint unavailable to those hostile packets. The two results are compatible because one concerns unrestricted positive measures and the other concerns the completed source image.

## Initially proposed Deutsch–Popper target

The hard-to-vary conjecture becomes:

> The labelled theta/Tate constructor initializes the coherency state on a definite light-cone sheet in each open reciprocal sector, and every authorized transport preserves that sheet until the unitary seam is reached.

Its local falsifier is a source-admissible parameter path inside one open sector for which (S_3) reaches zero. Its global falsifier is a hostile source satisfying the same rank-one seam coherency and constructor laws while changing sheets off the seam.

## Tested disposition

The local falsifier occurs for the raw theta tails themselves. At (y=0.2), the sign changes between (x=15.7) and (x=15.8), stably across five quadrature refinements. Therefore raw tail sheet preservation is superseded.

The exact coherency and two-sheet fiber theorems survive. The corrected target must construct a completed Clark/boundary coherency or conserved connection before asserting sheet preservation.

## Scope

This is an exact source-factorization and fiber-reduction theorem. Raw tail sheet preservation is false. Any RH-bearing sheet prohibition must belong to a further completed dynamical object.

## Verification

The exact symbolic checker `research/grothendieck/checkers/theta_tail_seam_coherency_light_cone.py` verifies rank one, the Stokes null-cone identity, reconstruction of (|S_3|), and reciprocal parity. It writes `research/grothendieck/results/theta_tail_seam_coherency_light_cone.json`.
