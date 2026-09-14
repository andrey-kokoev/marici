# v137: supported-residue W nonvanishing

The W-survival statement is now expressed directly in the physical amplitude's
actual readout shape, `residue (gysin physical)`.

Module 165 proves that if the supported residue of transported W equals its
endpoint detector value, then endpoint detector nonvanishing implies physical
supported-residue nonvanishing. The proof composes the inverse comparison path
with any hypothetical physical-zero path and contradicts endpoint nonzero.

This removes ambiguity about which physical functional must retain W. The exact
remaining input is the comparison equality
`residue(gysin(transport W)) = endpointDetector(W)` on the W-sector. Together
with cyclicity, that equality makes the odd reflection result both physical and
nonvacuous.

`rzk/165-supported-residue-W-nonvanishing.rzk.md` passes all six declarations
without assumptions.
