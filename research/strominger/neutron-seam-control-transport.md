# Neutron rest energy, iteration 2: transport the actual seam controls

## Fresh result

All **21 actual native seam projectors** now act exactly in the retained neutron/source-bank representation. Their inclusion enlarges the minimal generated space from the previous 11 complex dimensions to **24 complex dimensions**:

- all 18 native selected triangle modes;
- all six independent source-bank feature directions.

This is a generated invariant closure, not an assumed truncation. The other native polarization directions and source-bank complement remain unexcited for this preparation and operator family.

## Exact transport, not a replacement seam graph

Read the current rest-energy preflight, native coefficient store, source binding, rotation receipt and `native_operation_energy_lift_store.json`. For each native selected triangle mode, apply every stored 36-coordinate seam operator directly. Verify that its full output equals the reconstructed selected-mode output, including both intrinsic coordinates.

The same check is performed for the native constraint Hamiltonian and return projector. Thus the new matrices reproduce the actual stored operators, rather than building surrogate projectors from seam labels.

All 21 controls remain metric-self-adjoint rank-one projectors. They annihilate the original coherent neutron and are carried into one another by the actual native rotation. All six source pulses in all three frames are retained in the enlarged space with their original metric.

## Minimal occupied closure

Start from the actual coherent neutron, with the source bank empty. Generate images under native rotation, source pulses, all seam controls and native constraint energy. Exact rational elimination produces 24 independent vectors. A parent/operator witness is retained for every basis vector.

Because every transported operator preserves the full 24-coordinate envelope, this establishes both minimality and invariance. No return projection is applied during generation.

## Why the old 21/4 result does not directly transfer

The previous seam-occupation model assumed a conserved occupied-carrier sector. Extend its native carrier projector c_native by zero on the source bank. For every bound source pulse projector P_i,t,

    rank([c_native,P_i,t])=2.

The pulses therefore do not conserve that sector: an excitation can move from native neutron coordinates into the explicitly retained source bank.

The native constraints and all seam projectors have a seven-dimensional common zero space in the enlarged representation: the coherent neutron plus all six bank directions. This space is not invariant under the source pulses. Adding the pulse constraints leaves one common zero direction.

These facts do not invalidate the old supplied 21-register model on its original domain. They prevent treating its 21/4 increment as the rest energy of the new coupled dynamics without an explicit sector and record Hamiltonian contract.

## Computed response to the first AB pulse

For the unit coherent neutron with empty bank, the first full source pulse produces:

    native constraint expectation = 2099/13455,
    sum of actual seam expectations = 2504107/44293860.

Only two seams contribute, each 2504107/88587720. Their ordered triangle positions and actual native triangle indices are retained in the result packet.

These are actual defect expectations after a pulse, not a new rest-energy assignment. No coupling coefficient, neutral-register Hamiltonian or physical energy normalization was introduced in this iteration.

## Verification

```sh
python research/strominger/checkers/check_neutron_seam_control_transport.py
```

Nine checks passed. Complete transported matrices, generated basis and witnesses, metric, pulse projectors and provenance:

`research/strominger/results/neutron-seam-control-transport.json`.

## Next executable step

Determine the conserved particle-sector assignment across the dynamical source bank, comparing the existing charge-compatible constructions. The old native-only occupation label is demonstrably not conserved. Establish that contract before importing an autonomous charging law or computing a vacuum-subtracted rest-energy gap.
