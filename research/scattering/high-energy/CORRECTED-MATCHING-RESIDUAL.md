# H7 — corrected central matching residual

This audit advances from non-invariance diagnostics to the actual source matching equations. It uses the completed H6 corrected state at radial K=3.30, reconstructs the raw entrance interaction/contact forcing q, and evaluates the source radial Green matrices in the original 420-mode spectral sector. It independently evaluates the full downstream matching row, including outgoing boundary terms and the hinge trace reconstructed from the stored downstream field.

The original spectral-sector residual is `u_low - G_low q_low - Fin_low`. Its small numerical size is expected but newly checked from raw forcing rather than merely copying the projected solver's reported residual. The original floating eigenframe has nonzero Gram and native eigen residuals; the receipt exposes both. These are not silently treated as exact spectral-projector certificates.

For the complementary raw coordinates, the audit computes the actual corrected-state norm ||Q420 u|| and forcing norm ||Q420 q||. Applying the [conditional closed radial envelope](RADIAL-RESOLVENT-ENVELOPE.md) gives

    ||Q420 r|| <= ||Q420 u|| + ||Q420 q||/Delta.

It evaluates this expression using the reported band-gap candidate, with the common pose shift included. The receipt calls the resulting number a **conditional central residual envelope**, not a certified actual error bound. It requires a certified invariant projector/gap and outward-rounded evaluation to become such a residual bound. It does not assume cancellation, replace the full residual by native leakage, or apply an inverse that has not been bounded.

All reported matrix norms are Frobenius norms over the four prepared columns. They therefore also upper-bound the operator norm on normalized combinations of these columns, conditional on the same exact arithmetic/projector assumptions. Only the central energy is evaluated: no interval coverage or full-band residual is inferred.

## Disposition and next step

H7 remains open. The next useful step is to certify spectral separation and the floating spectral-frame reconstruction, then obtain a uniform coupled inverse bound for the declared matching system. A tighter omitted-sector functional-calculus action may be useful if the triangle envelope is too loose; repeating the already completed low-sector/downstream central checks is not progress. H6's separate finite-response observable-error and peak-certification gates remain unchanged.
