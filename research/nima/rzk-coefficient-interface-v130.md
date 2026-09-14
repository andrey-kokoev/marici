# v130: abelianized reflection-parity selector

The strict native reflection formula supplies a conditional physical parity
selection criterion.

For any additive physical readout `tau`,
`tau(sW) = -tau(W) + tau([r11,r00])`. Hence if physical transport kills the
commutator, the reflected class is odd. If `tau(W)` also remains nonzero, this
selects genuine odd parity rather than a vacuous zero class.

The remaining reflection gate is therefore concrete: prove that the physical
readout is abelianized on `[r11,r00]`, prove that it retains `W`, and transport
the existing native integral group homotopy. No parity is asserted without
those physical inputs.

Evidence is `results/reflection-parity-abelianized-selector.json` from
`checkers/check_reflection_parity_abelianized_selector.py`.
`rzk/158-reflection-parity-abelianized-selector.rzk.md` passes all eight
declarations without assumptions.
