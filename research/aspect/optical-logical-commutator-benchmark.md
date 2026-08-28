# Dual-rail optical benchmark for balanced-word hardware

The toric logical X and Z pair supplies a reversible source theorem that the
monotone interaction-net pilot lacks.

Encode one logical qubit in two optical rails. A calibrated rail swap realizes
X. A pi relative phase realizes Z. Use a path qubit as coherent control. The
reference branch applies a matched identity delay; the signal branch applies
the echo word Z X Z inverse X inverse.

For odd intersection the word is minus identity, so every target state returns
control record X equals minus one and Y equals zero. A commuting even control
returns X equals plus one. Rephasing the primitive gates cancels when inverse
gates are their actual calibrated inverses.

This is a practical benchmark for the balanced-word optical layer. It tests
coherent branch control, inverse calibration, phase preservation, leakage, and
target-state independence. The checker includes four target states and a
wrong-inverse hostile.

Passing this benchmark would not instantiate the interaction-net O or K
generators. It would certify that the apparatus can measure an ordered central
residue once a valid reversible source pair is supplied.
