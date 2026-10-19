# H7 — residual-controlled triangular inverse reconstruction

The covariance-error screen grew to an unusable bound because it repeatedly amplified a Frobenius error by multiplier norms. This attempt instead reconstructs the inverse of the actual stored unit block-bidiagonal factor L, one block row at a time. It keeps only the previous row, not a full dense 12,250-square inverse.

For blocks of W, use W_jj=I and W_jk=-L_j W_(j-1,k). Independently evaluate LW-I and include a matrix-product arithmetic error allowance; cancellation of repeated rounded products cannot count as an exact zero residual. Assemble Frobenius bounds on W and LW-I directly across the rows.

## Exact sufficient criterion

For any approximate inverse W with eta=||LW-I||<1, LW is invertible by the Neumann series. In finite dimension L and W are then invertible and

    L^-1=W (LW)^-1,
    ||L^-1|| <= ||W||/(1-eta).

This avoids propagating covariance errors through every block. Frobenius norms can upper-bound the operator norms in the formula. It is a certificate only when W and the residual have actually been enclosed.

## Scope

This checker uses the same explicitly conditional binary64/gamma arithmetic model as the previous screen; it does not introduce verified interval arithmetic. It imports the unchanged D-block separation and factor-product residual model from that receipt to show whether fixing the inverse-factor bound suffices. The source matrix/pose reference and floating spectral frame are also still uncertified.

The measured inverse reconstruction and factor margin are distinct gates. A residual below one in the model resolves only the inverse-factor propagation obstacle. It is not by itself inertia certification, a gap certificate or the coupled H7 inverse.

## Measured result

The residual model is 2.44239e-8, below one; the reconstructed W norm is 4453.806036 and the resulting inverse-factor upper model is 4453.806145. This avoids the previous 1e106 squared bound and restores separation near 5.55647e-8. The unchanged factor-product roundoff bound, 2.66102e-5, still exceeds that separation. Thus the inverse reconstruction is a viable conditional bound, while the full factor-margin test still fails. Both runtime enclosures and the factor residual remain gates.

This spends one H7 cycle. One of the original eight-cycle budget remains. The final bounded attempt should address the remaining factor-product enclosure rather than replay the threshold search or covariance screen.
