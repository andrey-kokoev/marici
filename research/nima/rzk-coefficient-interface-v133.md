# v133: multiplicative route to physical cyclicity

A second actual Rzk theorem now supplies the cyclicity premise of module 160.
Any multiplicative readout into commutative scalars is cyclic: the proof expands
`readout(xy)` as `readout(x)readout(y)`, commutes the scalar factors, and uses
the inverse multiplicativity path for `readout(yx)`.

Consequently the physical reflection route now has two admissible inputs:
either prove supported-trace cyclicity directly on `r11,r00`, or prove that the
relevant physical readout is multiplicative into its commutative scalar target.
Either route feeds module 160 (commutator vanishing) and then module 159 (odd
reflection parity).

This is a conditional theorem, not evidence that the current supported residue
functional is multiplicative; residues are often only linear, so direct
cyclicity may remain the more appropriate geometric proof.

`rzk/161-commutative-multiplicative-readout-is-cyclic.rzk.md` passes all five
declarations without assumptions.
