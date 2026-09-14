# v94: physical/coefficient amplitude bridge

`rzk/122-physical-coefficient-amplitude-bridge.rzk.md` defines the exact
pointwise comparison needed to identify a physical supported-residue amplitude
with the integer calibration.

A bridge consists of three coefficient coordinates for every physical class and
a proof that its supported Gysin residue equals
`- beta (a + (b + c))`. Given such a bridge, every coherent comparison filling
inherits a calibrated integer amplitude, and its physical residue is proved
equal to that calibration.

The bridge is deliberately an inhabitance problem: no coefficient pairing is
silently promoted to a physical trace. The missing construction is now a term
of `nima-physical-coefficient-amplitude-bridge` for the actual physical Gysin
and residue maps.

The transitive closure contains eight files. A fresh combined Rzk check passes
all 149 declarations (161 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.
