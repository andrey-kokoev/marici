# v142: Smith augmentation provenance correction

A source-level audit found that the integral Smith checker does not contain the
labelled `s11` Bockstein matrix or an explicit L2-transition column. It computes
the Smith form of the plus exact image augmented by `a^2` times eligible image
columns.

Therefore the exact D12--D28 Smith tables and their `{2,3,7}` prime support
apply to the Cartier `a^2`-product augmentation. Earlier checkpoints calling
this matrix the L2 completion overstate the established identification. No
proof currently equates the `a^2` product augmentation with the labelled L2
Bockstein transition.

The modular orbit result for L2 remains valid, and the s11 provenance remains
`3a^3+3a^3b`; but an integral Smith presentation of that labelled transition is
still open. The free alternating detector and unit-cone route belong to the
Cartier augmentation unless a later comparison theorem connects the matrices.

Evidence is `results/smith-augmentation-provenance.json` from
`checkers/check_smith_augmentation_provenance.py`.
`rzk/170-smith-augmentation-provenance-correction.rzk.md` passes all six
declarations without assumptions.
