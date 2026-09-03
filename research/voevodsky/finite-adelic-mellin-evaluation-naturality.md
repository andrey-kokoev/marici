# Finite adelic Mellin-evaluation naturality

## Question

Does the adelic scale lens lift the labelled cutoff-chain functor to finite Mellin evaluation naturally?

## Claim boundary

The result covers finite sums. It does not establish convergence, graph-topology continuity, or completion.

## Evaluation map

The arithmetic lens supplies

\[
\ell(r)=\log H(r),
\qquad
\chi_w(r)=e^{-w\ell(r)}=H(r)^{-w}.
\]

For a labelled affine chain, define

\[
E_N\left(\sum_r c_r[r]\otimes\sigma\right)
=
\sum_r c_r\chi_w(r)\sigma.
\]

This scale is explicit arithmetic/adelic input; it is not derived from the coefficient-neutral Carrier.

## Naturality

Zero-extension does not change a finite packet, so \(E_N\) commutes with cutoff transitions. Since evaluation acts coefficientwise, it commutes with affine boundary. Finally, \(H(1/r)=H(r)\) preserves character coefficients under label reciprocity, while the affine simplex is spectrally reflected.

The checker verifies all three identities on exact finite rational packets without numerical approximation.

## Remaining completion gate

Finite naturality does not imply convergence of the directed system. Completion requires a source decay or summability estimate uniform along the complete reciprocal affine orbit, together with a declared graph topology in which evaluation and boundary are continuous.

## Disposition

Finite cutoff Mellin evaluation is natural under transitions, boundary, and reciprocal action. The only remaining filler-descent gate is analytic: uniform reciprocal-orbit control in a typed graph topology.

## Verification

- `research/voevodsky/finite-adelic-mellin-evaluation-naturality-v1.json`
- `research/voevodsky/checkers/check_finite_adelic_mellin_evaluation_naturality.py`
- `research/voevodsky/results/finite_adelic_mellin_evaluation_naturality.json`
