# H6 — 33-node result and independent error-margin review

## Completed numerical test

The pinned source was rebuilt in a separate persistent environment and all 33 energies were solved with 128 response directions fixed. The source driver completed its analysis, verification and frozen-Schur controls. The matched 17-node subset recovers the historical 17-node diagnostics: relative differences are about 4.62e-8 for peak transport and below 2e-13 for the other two readouts. This is a numerical replay, not an exact assertion of phase-frame equality.

The initial comparison reports the following relative changes from matched 17 to 33 nodes:

| Diagnostic | Relative change |
|---|---:|
| Peak signed transport | 0.113495% |
| Whole-packet signed transport | 0.143864% |
| Product probability | 0.0678384% |

All are below the declared 1% criterion. Both rules have mean 3.30 and RMS 0.035 on the fixed energy band. No response-space or spatial-grid refinement is mixed into this comparison.

## Independent review

`check_quadrature_review.py` freshly checks all 33 stored downstream stationary equations and prepared-column flux identities, reconstructs the occupation/current kernels from raw complex fields, independently solves the moment-matching conditions, and finds the peak using a tenfold denser initial time grid. It separately sums the complex fields at the peak to verify the kernel-based readouts. The source's peak evaluator is not reused for this audit.

The mathematical peak search interval is kept at [-100,100], regardless of the broader plotting/analysis interval used by the source's generic 33-node analysis. Finite scanning and local optimization still do not constitute an interval-certified global peak proof; that limitation is explicit.

## What error budget would settle the inequalities?

Let x17,x33 be the computed values and epsilon17,epsilon33 independent absolute bounds on their errors, including stationary solve, readout and peak-location error where relevant. The sufficient condition

    |x33-x17| + epsilon33 + epsilon17 <= .01 (|x17|-epsilon17)

is equivalent to

    epsilon33 + 1.01 epsilon17 <= .01 |x17| - |x33-x17|.

The right side is the available acceptance margin. If a common relative bound beta is used, epsilon_n<=beta|x_n|, the sufficient budget is

    beta <= [.01|x17|-|x33-x17|]/[|x33|+1.01|x17|].

The review receipt computes these budgets separately. They are **allowed errors**, not errors already proved. Small linear-equation residuals do not establish them without stability/sensitivity information. H6 needs a bound only for its fixed 548-direction entrance approximation and its three diagnostics; the stronger full-untruncated H7 certificate is not logically required and is not installed as a new prerequisite.

## Disposition

H6 remains **open, numerically supported**. Its own falsifier/acceptance boundary says unresolved solver-error margins are inconclusive. We therefore do not promote it merely because all three computed changes are small. The next bounded H6 attempt is finite-model observable-error and global-peak certification using the completed source cache, not another 33-node solve.

The raw fields, metadata and reconstructed kernels remain in `.ai/tmp/scattering-h6-response33/calculation/runs/h6_response33/`; their hashes are bound by the review receipt. A small durable kernel copy is retained under `results/quadrature33-kernels.v1.npz`. No continuum convergence or physical accuracy follows from this finite refinement test.
