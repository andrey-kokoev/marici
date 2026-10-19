# Exact context orbit versus averaging

## Frozen domain and equivalence

Use the existing marked-contact descriptor and all mathematical field pairs
(p,n) in V_P x V_N admitted by the anchored packet API. No equation n=S p is
imposed on this product domain, and no claim of independent physical input
preparations is added. The context action is fixed before testing:

    g.(p,n)=(U_P^g p,U_N^g n), g in Z/3.

It acts on both fields and their retained anchor/patch data through the actual
prepare API. The only allowed equivalence is belonging to the same orbit of
this specified action. Common or relative complex phase is not silently added
to the equivalence.

The quotient encoding is the unordered complete set of distinct full anchored
packets in the orbit. Orbit sizes are1 or3. Sorting serialized records is only
a deterministic storage convention, not an equivariant choice of one field or
a physical preferred context. Recovery returns the unordered orbit of fields,
not one supposedly canonical representative.

## Exact comparison and controls

Validate every packet with the source recover API, reconstruct its field pair,
recompute the complete orbit and require exact set equality. This rejects
missing orbit members, foreign members, missing anchors and malformed packets;
record ordering must not matter. Since prepare/recover is injective on its
fixed domain and the action is a finite group, equality of these complete
packet sets is equivalent to equality of field orbits. Fixture checks are
regressions of that argument, not its only evidence.

Test dense, zero, source-derived contrast and phase variants. Freeze a
counterexample: p is a unit source return vector fixed by U_P; n is a unit
target local-relative vector killed by the U_N average. Compare (p,n) and
(p,i n), retaining the same nonzero P anchor. Their field means agree and
their averaged quadratic comparison blocks agree: self blocks are unchanged
by phase and averaged cross blocks vanish. Their anchored packet orbits differ.
They cannot be context equivalent: U_N^g n=i n would imply n=i^3 n after
cubing, contradicting n!=0. This is loss beyond the declared C3 quotient.

The averaged block collection is not automatically a coherent rank-one packet.
With the unchanged P anchor, recovery would infer zero N from the averaged
cross blocks, contradicting the nonzero averaged N self blocks; verify source
recover rejects it. It may be given a different statistical type in future,
but that is not part of this coherent-packet contract.

## Interpretation

A full finite packet orbit can forget the context label without merging distinct
orbits; amplitude and quadratic-block averaging can merge more. This is a
mathematical quotient/readout result, not restoration of a fixed geometric PN
intertwiner, physical sewing, phase calibration or a privileged context.

Replay: `python research/strominger/checkers/check_context_orbit_readout.py`.
Receipt: `results/context-orbit-readout/verification.json`.
