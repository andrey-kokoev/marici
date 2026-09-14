# v179: group correction supplies the group-zero witness

The physical point can now retain a supported reflection/group coherence cell
in the same way that module 206 retains the logarithmic road cell. Define the
corrected group discrepancy as

`rawGroup(coefficient,physical) - groupBoundary(cell)`.

When the raw physical group defect and the boundary of the reflection cell are
both identified with one target, path composition identifies them and the
group cancellation law proves that the corrected discrepancy is zero. This is
the exact witness required by the group component of candidate completion.

The trace results remain useful but correctly weaker: cyclicity kills the
commutator in supported readout and hence proves odd reflection parity. It does
not by itself identify the underlying group defect with zero. The retained
group cell supplies the needed homotopy-level correction, while trace cyclicity
controls its physical scalar image.

The remaining physical group input is one equality: the boundary of the
constructed supported reflection cell must equal the actual raw group defect at
the candidate point.

`rzk/207-group-corrected-physical-point.rzk.md` passes all nine declarations
without assumptions.
