# Fixed positive endpoint blocks impose only a whitened contraction

## Question

Can source-fixed positive-definite endpoint Gram blocks force Hall entry signs or interlacing-support zeros?

## Claim boundary

For positive-definite `A,B`, the block matrix `[[A,X],[X^T,B]]` is positive semidefinite exactly when `A^(-1/2) X B^(-1/2)` is a contraction. This norm condition cannot force coordinate signs or support zeros. With `A=diag(2,3)`, `B=diag(5,7)`, and forbidden off-diagonal `X_12=1`, the Schur complement is `diag(5,13/2)` and the whitened squared norm is `1/14`; changing the entry to `-1` leaves the criterion unchanged. More generally, every coordinate of `X` admits both signs at sufficiently small magnitude. Singular endpoint blocks are excluded from this claim.

## Disposition

Reject positive-definite fixed endpoint Grams as a source of Hall signs or support. Their only intrinsic constraint is whitened operator norm. The remaining structural exception is singular endpoint data, whose kernels can force range restrictions and coordinate combinations to vanish. Next test whether those kernel constraints can encode interlacing support without already inserting the support graph.
