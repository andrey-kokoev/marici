# The all-soft phase is a flat relative differential character

## Two readout channels

The all-soft supported class should not be inserted into the complex-linear
Gauss--Manin system.  Its natural target is the flat part of relative
differential cohomology.  In Cheeger--Simons grading, a degree-three flat
character on the pair \((\Delta^2,\partial\Delta^2)\) is represented by

\[
\widehat\tau_{\rm soft}
\in
H^2(\Delta^2,\partial\Delta^2;\mathbb R/\mathbb Z)
\subset
\widehat H^3(\Delta^2,\partial\Delta^2).
\]

The cellular relative complex has one oriented two-cell and no higher cell,
so

\[
H^2(\Delta^2,\partial\Delta^2;\mathbb R/\mathbb Z)
\cong\mathbb R/\mathbb Z.
\]

The source-derived order-three class selects

\[
\widehat\tau_{\rm soft}=\frac13\pmod{\mathbb Z}
\]

up to orientation.  Evaluation on the relative fundamental class gives

\[
\operatorname{Hol}_{\widehat\tau_{m soft}}
([\Delta^2,\partial\Delta^2])
=\exp(2\pi i/3).
\]

## Why linear probes cannot see it

This character is flat:

\[
\operatorname{curv}(\widehat\tau_{\rm soft})=0.
\]

Its integral characteristic class also vanishes.  For

\[
0\to\mathbb Z\to\mathbb R\to\mathbb R/\mathbb Z\to0,
\]

the Bockstein lands in

\[
H^3(\Delta^2,\partial\Delta^2;\mathbb Z)=0.
\]

Thus the phase is nontrivial as relative holonomy while contributing neither
curvature nor a characteristic-zero cohomology direction.  The two channels
are complementary:

\[
\begin{array}{c|c|c}
\text{channel}&\text{detects}&\text{all-soft value}\\
\hline
\text{twisted de Rham/Gauss--Manin}&\text{curvature and periods}&0\\
\text{flat differential character}&\text{relative torsion holonomy}&\zeta_3^{\pm1}
\end{array}
\]

This explains, rather than repairs, the rank-seven half-twist no-go.

## Boundary transgression

The connecting isomorphism for the disk pair identifies the relative class
with a flat boundary character:

\[
H^2(\Delta^2,\partial\Delta^2;\mathbb R/\mathbb Z)
\cong
H^1(\partial\Delta^2;\mathbb R/\mathbb Z).
\]

It evaluates to \(1/3\) on the oriented boundary circle.  The three localized
edge representatives differ by coboundaries, exactly matching the previously
proved homotopy-coherent cyclic cocycle.  Hence the surface holonomy and its
boundary transgression are the same source class in two legal presentations.

## Physical gate

Differential cohomology types the readout but does not supply its physical
argument.  A physical observation still requires a source-derived relative
two-cycle, boundary loop with trivialization, or pullback

\[
c_{\rm CM}^*\widehat\tau_{\rm soft}.
\]

The current Cayley--Menger packets do not provide that comparison.  Therefore
the correct status is:

\[
\boxed{
\text{canonical flat character exists; physical evaluation remains
source-underdetermined.}
}
\]

## Evidence

- `research/nima/checkers/check_all_soft_relative_differential_character.py`;
- `research/nima/results/all-soft-relative-differential-character.json`;
- `research/nima/results/all-soft-flat-z3-character.json`;
- `research/nima/results/a2-discriminant-linking-readout.json`.
