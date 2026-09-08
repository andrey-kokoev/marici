# v38: graded Q-lift naturality obstruction

**Supported-branch update:** [`rzk-coefficient-interface-v39.md`](rzk-coefficient-interface-v39.md)
records the principal occurrence-line correction, Rees scaling of the returned
excess, and the primitive reverse connecting map in the finite graded dual.

`rzk/48-q-lift-naturality-obstruction.rzk.md` separates the secondary
coefficient-naturality obstruction from the primary individual-lift
obstruction.

Its seven annihilator modes represent

    (I_plus, I_minus, tau_plus*tau_minus),

so the six branch generators are bare short occurrences, not the
`tau_plus*I_plus` and `tau_minus*I_minus` generators of the primary connecting
class. The module also records the six labelled common-to-branch relation
defects. In the top packet, where there is no degree-four source, each defect
has integral augmentation one while every top boundary has augmentation zero;
an asserted filler therefore implies `0_Z=1_Z`.

A fresh 71-file headless closure passed in 27.05 seconds. Evidence:
`results/48-q-lift-naturality-obstruction.typecheck.json`.

Scope: Rzk checks the type-level distinction of the two annihilators and the
primitive nonboundary consequence for each labelled defect. The actual
24-term target cycles, 43-generator/174-relation presentation, exact extension
annihilator, and spectator-linear dihedral section remain certified by the
incoming all-polynomial calculation rather than reconstructed natively.

Consequently minimum-degree uniqueness for seven individual lifts is not a
coefficient-linear splitting theorem. The spectator-linear section remains
valid, while a section over the full alternating coefficient ring is excluded
in this fixed target model.
