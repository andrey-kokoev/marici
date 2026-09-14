# v197: supported odd reflection group cell

The normalized ramified branch-difference line supplies the previously missing
nonannihilating physical readout of the native group primitive W: its selected
readout is one. The supported scalar readout is commutative and multiplicative,
so it kills the `[r11,r00]` commutator.

Transporting the existing native integral homotopy

`sW=-W+[r11,r00]`

therefore gives readout `sW=-1`. This constructs a supported odd reflection
group cell retaining the native coherence homotopy; it also closes the two
premises that were left open in modules 158--162 (commutator killing and W
nonannihilation) on the selected supported line.

As with rawCech before v196, `rawGroup` is still only an interface parameter.
The remaining group gate is to define its concrete physical reflection defect
formula and compare that formula with this cell's boundary.

Evidence is `results/supported-reflection-cell-readout.json`.
`rzk/225-supported-reflection-group-cell.rzk.md` passes all eight declarations
without assumptions.
