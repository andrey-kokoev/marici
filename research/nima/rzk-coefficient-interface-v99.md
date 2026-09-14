# v99: fixed-coefficient physical obstruction

`rzk/127-fixed-coefficient-physical-obstruction.rzk.md` gives a constructive
meaning to obstruction vanishing before a concrete H1 complex is available.
For a selected coefficient class it is precisely a physical lift paired with a
proof that the totalized comparison difference is zero.

Such a lift canonically yields a coherent comparison filling and therefore a
supported-residue amplitude. If the physical/coefficient amplitude bridge is
also supplied, the module proves that this amplitude equals the calibrated
integer expression at the lift's physical coordinates.

This avoids claiming that an abstractly named H1 obstruction vanishes. The
remaining data are explicit: the totalized difference map and one physical
lift/coherence witness for the selected coefficient class.

The transitive closure contains nine files. A fresh combined Rzk check passes
all 159 declarations (171 checker steps including parameter/assumption
commands). The target module adds no `#assume` declarations.
