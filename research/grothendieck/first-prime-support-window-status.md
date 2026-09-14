# First-prime support-window status after numerical supersessions

## Question

What survives from the sequence of projector, quadrature, and Schur-complement messages after following their later corrections?

## Claim boundary

The empirical order-refinement and rank-25 projector scouts are not the final evidence. The current branch is `research/voevodsky/regularization-at-the-proved-tail-floor-produces-a-finite-polynomial-certificate.md`.

Two projection regimes must not be conflated. For the exact concentration spectral projection with complement norm at most
\(\eta_*=\delta/[2(\delta+C_-)]\), the bound
\(A\geq\delta I-(\delta+C_-)T\) genuinely gives \(QAQ\geq1/40\,Q\). Thus the event-13507 strict-tail argument and its inverse factor `40` are valid for that exact spectral subspace.

The later certificate instead uses an arbitrary exactly specified 25-dimensional polynomial space. Its captured-trace residual `rho` controls \(\|QTQ\|\), but does not identify that space with the exact spectral projection. After the deliberately weakened localization bound used there, its certified tail coercivity is

\[
\alpha=\frac{1-130\rho}{40}.
\]

At the certified residual, `alpha` is approximately `0.00486945765658`, so its inverse is approximately `205.36`. Using inverse factor `40` for this arbitrary polynomial space would be invalid; the spectral-projection theorem itself is not thereby refuted.

The later directed 192-bit Arb calculation reports:

- interval enclosure of every cutoff-form entry;
- certified trace residual and corrected inverse floor;
- exact-span projected residual propagation;
- all 25 final interval LDL pivots positive, with minimum lower bound about `0.2428851171`;
- nonnegativity of the omitted multiplier outside cutoff 250.

This proves positivity of the corresponding uncut first-prime form on the single support window used by that packet, conditional on the source identity whose external classical normalization remains unaudited in `research/grothendieck/compact-weil-instance-audit.md`.

## Disposition

The old continuum-enclosure and spectral-projector blockers are closed for this support window. No finite-to-global promotion follows: positivity for other windows, one cutoff uniform over all tests, the full prime/Euler product, and an RH implication remain unproved. In particular, the older combined-symbol scout at \(L=\log 2\) estimated a still-unusable concentration dimension near \(2.487\times10^8\); the one-prime \(L=7/20\) certificate does not resolve that obstruction. This numerical branch therefore supplies a finite-window analytic test object for a future zeta formalization, not the zeta construction itself.
