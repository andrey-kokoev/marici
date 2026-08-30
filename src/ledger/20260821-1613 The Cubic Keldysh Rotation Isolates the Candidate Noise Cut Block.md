# Entry 1613 — The Cubic Keldysh Rotation Isolates the Candidate Noise Cut Block

## Claim

The cubic self-energy has a canonical Keldysh-noise block before endpoint
assembly.  This block, rather than the full indefinite endpoint response, is
the correctly typed candidate for Gaussian second-Rees positivity.

## Exact contour algebra

Write each internal Wightman pair as

\[
G^>=F+\frac{\rho}{2},
\qquad
G^<=F-\frac{\rho}{2}.
\]

For labelled internal occurrences \(q,k\), the symmetric and antisymmetric
cubic products are

\[
G_q^>G_k^>+G_q^<G_k^<
=2F_qF_k+\frac12\rho_q\rho_k,
\]

\[
G_q^>G_k^>-G_q^<G_k^<
=F_q\rho_k+\rho_qF_k.
\]

The first is the Keldysh-noise block; the second is the spectral/retarded
block.  On the convolution-collapsed diagonal,

\[
\Sigma^K_{\rm diag}
=2F^2+\frac12\rho^2,
\]

which is nonnegative for real physical data.

## Consequence

The contour metric must be removed by the Keldysh rotation before applying a
positivity test.  Entry 1612's indefinite endpoint form mixes the two blocks
and therefore cannot serve as the uncertainty completion.

## Remaining gate

For independent \(q,k\), algebraic bilinearity alone does not prove
positivity.  The physical Cut measure and conjugation/orientation must turn
the symmetric Wightman product into a norm pairing.  Endpoint incidence must
then be transported separately within this block.

## Next falsifier

Construct the source endpoint assembly directly for
\(G_q^>G_k^>+G_q^<G_k^<\), retaining both occurrence labels.  Test whether
its physical Cut pairing is positive and whether its second phase-space jet
equals the statistical completion predicted in Entry 1608.

## Artifacts

- `research/benincasa/marici-gm/src/bin/cubic_self_energy_keldysh_noise.rs`
- `research/benincasa/results/cubic-self-energy-keldysh-noise.json`

Allocator claim: `seqclaim-e37ad97c03365358bc9430bc`.
