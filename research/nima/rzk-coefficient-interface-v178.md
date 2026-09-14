# v178: road correction supplies the Cech-zero witness

The selected log road cell is now attached to the candidate physical point.
The corrected physical type retains both the original point and its road cell.
Its Cech discrepancy is defined as

`rawCech(coefficient,physical) - roadBoundary(cell)`.

If the actual raw residual and the road boundary are both identified with the
same selected target `Cech(v)`, path composition identifies the two terms and
the Cech cancellation law proves that the corrected discrepancy is zero.
Thus the selected road comparison produces exactly the Cech witness required
by candidate completion; it is not merely a nonzero residual detector.

No physical comparison was assumed in the theorem. The remaining geometric
inputs are precisely the two equalities:

1. the actual physical Cech residual equals `Cech(v)`;
2. the primitive log road boundary equals `Cech(v)`.

`rzk/206-road-corrected-cech-physical-point.rzk.md` passes all ten declarations
without assumptions.
