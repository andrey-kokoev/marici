# Flexible block-Gram embeddability is vacuous for Hall admissibility

## Question

Does positive-semidefinite block-Gram embeddability restrict a finite Hall coupling when endpoint blocks may be scaled?

## Claim boundary

No. For every finite real `m×n` matrix `X`, the symmetric block matrix `[[lambda I_m,X],[X^T,lambda I_n]]` is positive semidefinite whenever `lambda` is at least the spectral norm of `X`. The exact choice `lambda=sum_ij |X_ij|` always suffices because it dominates the Frobenius and spectral norms. Thus every coupling, and every matrix violating nonnegativity, margins, or interlacing support, has such a Gram embedding. The checker verifies an exact witness and a deliberate small-`lambda` obstruction. This does not address endpoint Gram blocks fixed independently by source geometry.

## Disposition

Reject freely scalable Gram positivity as a Hall mechanism: it contributes no sign, margin, or support restriction. Any surviving Gram rival must derive fixed endpoint blocks from the source and prove that their Schur-contraction constraint forces the required Hall conditions. Next test that fixed-block criterion after whitening and determine whether contraction alone can ever force entry signs or support zeros.
