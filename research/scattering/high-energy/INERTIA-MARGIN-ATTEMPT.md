# H7 — quantitative inertia robustness attempt

The source's 420-negative-pivot count at the unshifted threshold 16-CPOSE has previously been only a numerical indication. This attempt measures a sufficient perturbation margin rather than treating the smallest pivot alone as a certificate.

## Exact sufficient criterion

Let A=H-(16-CPOSE)I. Suppose computed factors define the exact comparison matrix B=L D L*, where L is unit block-lower-bidiagonal and D is Hermitian block diagonal. If each D block has known inertia and spectrum separated from zero by at least d>0, and ||L^-1||<=ell, then

    ||B^-1|| <= ell²/d,   dist(0,spectrum(B)) >= d/ell².

If an independently bounded residual satisfies ||A-B||<=r<d/ell², the straight Hermitian homotopy from B to A stays invertible. Sylvester's law and continuity therefore give inertia(A)=inertia(D). This is a sufficient test, not a necessary one.

## Triangular inverse bound without a giant dense matrix

For the row blocks of L^-1, let R_j be the sum of their products with their adjoints. The bidiagonal recurrence gives

    R_0=I,  R_j=I+L_j R_(j-1) L_j*.

Thus ||L^-1||_F²=sum_j trace(R_j), which also upper-bounds its squared operator norm. This accounts for amplification through all 49 blocks, unlike the minimum pivot diagnostic alone. The factor residual is assembled from diagonal errors and twice the off-diagonal Frobenius squared errors; raw block-tridiagonal sparsity is checked.

## Scope of this run

The audit reconstructs the actual 12,250-dimensional raw source matrix. All 250-dimensional D eigenframes are checked numerically for Gram and spectral-reconstruction defects. It reports the candidate d/ell²-r, the count and the factor conditioning. These are floating candidates, not outward-rounded bounds. A positive measured margin identifies a viable interval-certification target; a negative margin would only reject this particular loose sufficient test, not refute H7 or prove a source singularity.

Even certifying the count does not certify that the stored floating 420-column frame is an exact invariant projector. Spectral-subspace reconstruction must be bounded separately before using the Q420 radial envelope as a certified residual bound. No full coupled inverse is produced here.

## Measured result

The count is again 420, but the sufficient margin is **negative**. The inverse-factor Frobenius norm is about 70,660, giving d/ell² about 8.70e-12, while the factor reconstruction residual is about 1.42e-7. Thus the current bound/factors miss the needed separation by more than four orders of magnitude. Outward rounding alone cannot rescue this measured margin; one must tighten the inverse norm bound substantially or change the factorization/spectral method. This outcome rejects the proposed certification route in its present form, not the source gap or H7.

One focused H7 cycle is spent on this attempt. Four of the original eight-cycle budget remain. The next step should use the measured conditioning to choose between outward-rounded block factor certification and a sharper spectral-separation method; simply repeating the inertia count is redundant.
