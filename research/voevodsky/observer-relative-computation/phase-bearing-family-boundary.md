# Fixed finite cyclic families remain incomplete with arbitrary phases

`agda/ObserverPhaseFamily.agda` packages each observer as first-order data: a positive-period code and an actual finite starting state. Duplicate periods may have different phases. No observer callback is stored.

The generic power-action theorem proves transport from ANY starting state equals modular addition of the power residue. Consequently a common multiple of the periods restores every phase, not merely zero. Joint readings are an explicit finite dependent product, preserving each probe's state type.

For every fixed finite list of these probes, its common-period path has the same complete joint readings as zero turns. The integer-cover theorem still proves the actual paths unequal. Thus no decoder of this family's readings faithfully reconstructs all paths, already failing on positive powers.

The calibrated probes used for signed bounded recovery are explicitly embedded in this Probe type, and their readout agrees definitionally with the earlier calibrated interpreter. This closes the phase gap: input-dependent sufficient probes and fixed-family incompleteness concern compatible observer representations. It does not imply a limitation of all possible observer types or assign a physical cost to phase/calibration.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-phase-family.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Test finite adaptive observation rather than just a fixed parallel list. Encode a finite branching protocol using explicit probe data and branch tables, not arbitrary access callbacks. Determine whether a common invisible comparison survives the entire reply-dependent protocol, retaining its transcript or outcome. State precisely whether the proof covers finite trees or more general terminating procedures; do not silently generalize between them.
