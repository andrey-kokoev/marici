# Frozen toric-code sufficiency prediction

Owner: `marici.Nima`

This prediction is frozen before inspecting the current toric-code instrument
and fault packets.

## Predicted source-closed diagram

For one stabilizer `W` with eigenspaces labelled by `s in {+1,-1}`, the
declared lattice-plus-ancilla gate source should realize:

1. task `p_s`: project the data onto the `s` syndrome sector;
2. interaction: prepare an ancilla, coherently write the parity of `W` into
   it, and measure its pointer;
3. record: emit the classical syndrome bit `s`;
4. return: reset or freshly replace the ancilla;
5. coherence: a second ideal extraction returns the same syndrome, while
   coarse-graining over `s` agrees at both record and data-channel levels.

Prediction:

- the ideal syndrome-extraction packet is a positive source-generated
  repeatable constructor for the **measurement task**;
- this does not automatically prove a constructor for **error correction**,
  because conditional recovery and a fault/degradation theorem are additional
  task data;
- the first likely failure of the stronger fault-tolerant claim is at
  resource return/degradation or recovery coherence, not at readout.

## Sufficiency falsifiers fixed in advance

The source-closed criterion fails if all five declared faces are present and
commute but the ideal measurement task is still not constructible.

The positive prediction fails if any of the following is absent:

- a source gate word implementing the parity interaction;
- an ancilla preparation and a classical pointer record;
- a conditional successor state equal to the syndrome projection;
- repeatability on the selected branch;
- reset/fresh-ancilla authority;
- agreement between forgotten fine outcomes and the nonselective channel.

Fault propagation may falsify only the stronger fault-tolerant constructor,
not the exact ideal measurement constructor, unless the source contract
requires fault tolerance as part of the task.

