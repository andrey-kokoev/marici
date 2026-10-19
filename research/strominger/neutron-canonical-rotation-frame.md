# Neutron pulse binding, iteration 2: retain the actual rotation frame

## Fresh result

The previous 52-complex-coordinate retained-bank binding now has an exact rotation-covariant **moving-address** version. No metric, source feature, Hamiltonian or neutron mode was changed. A three-valued frame record is retained explicitly.

The fixed-address alternative was tested first and fails for every bijection between the six original source labels and the six native rim modes. This is a restriction on fixed port covariance, not a failure of the previous pulse intertwiner.

## Native rotation reconstructed from live sources

Read the current `inputs/mode-neutron.json`, geometry, native coefficient store and iteration-1 receipt. Apply the supplied source generator to the actual vertices and face centers. Verify the induced rotation of all 18 ordered triangle modes in the existing Cartesian coefficient frame, then the permutation of all 36 intrinsic coordinates.

For the previous address policy the six rim modes rotate as

    (AB CA AD)(BC BA DB).

These names are addresses attached to actual neutron modes. The source AB arrow still has its original endpoints A and B; its typed history is not rewritten as a neutron vertex path.

## Why a static six-port assignment cannot be equivariant

The source feature Gram is D_ij=f_i* H f_j. Its exact permutation automorphism group has eight elements:

- one of order 1;
- five of order 2;
- two of order 4;
- none of order 3.

A static assignment to the two rotating neutron rims would require an order-three permutation of these six source features preserving D. All 720 bijections were checked and fail. Unequal overlap magnitudes also rule out repairs by multiplying the individual features by phases.

For example the source AB/AD pair has overlap 1/11. The native rotation sends their addresses to CA/AB, whose source overlap is 1/121. No metric-unitary action on the record bank can implement that feature permutation.

This excludes static bijective port covariance with a unitary bank action preserving individual features. It does not classify more general operation mixing or enlarged source-port families.

## Moving-address construction

Let Rhat=R_neutron direct-sum I_bank. Keep the original source features and record coordinates stationary, and retain t in {0,1,2}. Define

    J_t(y,r)=(R_neutron^t sum_i v_i r_i, y),
    d_i,t=(R_neutron^t v_i,-f_i),
    P_i,t=d_i,t d_i,t* M/2,
    U_i,t(theta)=I+(exp(-i theta)-1)P_i,t.

The port label i and its source occurrence remain unchanged; its actual neutron mode address follows t. Exact identities give

    U_i,t+1(theta) Rhat = Rhat U_i,t(theta),
    <d_i,t,d_j,t>=K_ij,
    h_i,t+1(Rhat state)=h_i,t(state).

Projector covariance proves the first identity for all pulse angles, not merely the exchange endpoint. It was checked on all 52 complex target coordinate vectors, for all six ports and all three frames. Non-endpoint pulses were also evaluated exactly.

The state still has all 36 native neutron coordinates and all 16 dynamical source-bank coordinates. The discrete frame record is additional control information, not a new amplitude or a physical clock.

## Retained execution and energy

Replay AB,BA,AB,BA,AB,BA, with an actual neutron rotation after each pulse. Retain each source occurrence, frame, actual neutron triangle and full pre/post states. The result agrees at every step with rotating the reference-frame source execution. Reverse all six rotations and pulses and recover the exact initial state.

After the three-valued frame recurs, the source state generally has not returned. No source history is erased by frame recurrence.

For the unit coherent neutron and empty source bank, the existing pulse value remains

    h_i,t=2099/53820

for every initial port/frame choice. No energy rescaling was needed. These values refer to that preparation; they are not asserted constant under an arbitrary sequence of differently addressed pulses.

The schedule used in this replay is supplied. The construction does not derive a physical clock, an autonomous controller or the initial address policy.

## Verification and output

```sh
python research/strominger/checkers/check_neutron_canonical_rotation_frame.py
```

Ten checks passed. Exact native permutations, static-obstruction certificate, moving-frame identities, six full occurrence records and source hashes:

`research/strominger/results/neutron-canonical-rotation-frame.json`.

Shared source and native stores were not changed.

## Next executable obligation

Determine the invariant closure generated from the occupied coherent neutron by the bound pulses **and** native rotations. Retain every emitted neutron direction and bank amplitude; do not apply the lossy native return projector to force it back into a one-dimensional occupied mode. This tests whether the bound interaction can support an occupied-sector calculation rather than only one-pulse readouts.
