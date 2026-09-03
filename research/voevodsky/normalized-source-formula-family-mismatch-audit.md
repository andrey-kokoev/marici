# Audit: existing normalized source formulas do not yet define the interval operator

## Question

Does prior research already contain the normalized explicit-formula identity needed to assemble the compact-support weighted matrix?

## Claim boundary

This audit classifies the materialized source formulas by test family. It does not dispute their formulas within those families.

## Materialized formulas

Two nearby packets carry explicit signs and prefactors:

1. `research/grothendieck/explicit-two-variable-weil-heat-source-formula.md` treats shifted spectral Gaussians
   \[
   h_{t,\xi}(u)=e^{-t(u-\xi)^2}.
   \]
   Its prime term has the declared factor
   \[
   -\frac{1}{2\sqrt{\pi t}}
   \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
   e^{-(\log n)^2/(4t)}\cos(\xi\log n).
   \]

2. `research/grothendieck/source-formula-for-the-gaussian-translation-rectangle.md` treats modulated Gaussian correlations
   \[
   h_{t,a}(u)=e^{-tu^2}\cos(au).
   \]
   That packet explicitly distinguishes modulation by logarithmic displacement from spectral translation.

## Missing comparison map

The fixed-support programme acts on zero-extended functions supported in \((-L,L)\), with Dirichlet compression, endpoint localization, and prime translations. Neither Gaussian packet supplies a proved map from its test family to this interval form carrying all of the following simultaneously:

- Fourier normalization;
- the sign and prefactor of each prime translation and its adjoint;
- archimedean normalization relative to \(A=\log(1+\sqrt{-\Delta_D})\);
- polar/endpoint terms;
- the zero-extension boundary convention;
- the quadratic IMS localization convention.

Equality of the prime coefficient pattern \(\Lambda(n)/\sqrt n\) does not construct this comparison map. Importing the Gaussian prefactor into the interval matrix would therefore be a cross-family coercion.

## Acceptance test

The source gate closes only when a source-linked identity for a general compactly supported logarithmic test is specialized to \((-L,L)\), with its Fourier convention declared, and each resulting term is matched to a bounded component of \(B_L\). The specialization must reproduce the Gaussian formulas when evaluated on their own test families; that is a consistency test, not a substitute for the general identity.

## Disposition

Prior research narrows the blocker but does not remove it. The shifted-Gaussian and modulated-Gaussian formulas are normalization fixtures. They cannot yet authorize unified interval-matrix assembly.
