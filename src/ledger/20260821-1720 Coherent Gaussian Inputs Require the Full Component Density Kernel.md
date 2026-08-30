# 1720 — Coherent Gaussian Inputs Require the Full Component Density Kernel

## Source-derived extension

Entries 1713–1718 close classical finite Gaussian mixtures.  Replace the
classical mixture by the physically admitted coherent superposition of two
normalized displaced Gaussian packets \(|+d\rangle,|-d\rangle\), each with
position variance \(a\).

Their source overlap and transition moment are

\[
S=\langle+d|-d\rangle
=\exp\!\left(-\frac{d^2}{2a}\right),
\qquad
\langle+d|Q^2|-d\rangle=aS.
\]

## Diagonal-weight falsifier

The normalized even and odd states

\[
|\psi_\pm\rangle
=\frac{|+d\rangle\pm|-d\rangle}{\sqrt{2(1\pm S)}}
\]

have identical diagonal component weights.  Nevertheless,

\[
\langle Q^2\rangle_+
=\frac{a+d^2+aS}{1+S},
\qquad
\langle Q^2\rangle_-
=\frac{a+d^2-aS}{1-S},
\]

and their cross-multiplied difference is

\[
\boxed{-2d^2S\ne0}
\]

up to the common positive normalization denominator.  A classical mixture
table predicts \(a+d^2\) for both and therefore loses physical information.

## Narrow result

The minimal tested coherent completion is the full Hermitian component density
kernel \(\rho_{jk}\), together with the transition generating kernel between
labelled packet occurrences.  The matrix structure is derived from quantum
superposition; it is not the hypothetical matrix-valued probability of Entry
1719.

No new Cut carrier stratum is indicated.  This is a sector-specific
coefficient enlargement over the same labelled occurrence carrier.

## Durable artifacts

- `research/benincasa/checkers/coherent_gaussian_density_kernel.rs`
- `research/benincasa/results/coherent-gaussian-density-kernel.json`
- `research/benincasa/coherent-gaussian-density-kernel.md`

## Next falsifier

Derive the independent-Cut coproduct of two coherent component kernels.  Test
whether the labelled tensor product \(\rho^{XY}=\rho^X\otimes\rho^Y\) and the
transition generating kernels close exactly, including partial trace and
coincident packet displacements, without a coefficient braiding cell.
