# Numerical bounds now admit arbitrary signed comparison paths

`agda/ObserverSignedBoundAdmission.agda` closes the previous certificate gap. From |integer(p)|≤B it constructs an actual finite interval slot whose interpreted path has the same signed integer as p. Semantic completeness then gives the required path equality and interval certificate.

For nonnegative integers the slot is B+n. For negative integers the natural-order slack supplies the slot. Integer cancellation and the bound inequalities are checked explicitly; no representation witness is assumed and no truncated choice is used to construct it.

Consequences:

- The calibrated period-(2B+1) probe faithfully reconstructs any loop with the supplied numerical bound.
- For arbitrary loops p,q, B=|integer(p)|+|integer(q)| is a sufficient COMMON bound.
- If those loops differ, the corresponding single finite calibrated probe separates them.
- Agreement under every calibrated probe implies equality of the actual loops.

The probe depends on the compared inputs through their signed normalization. This does not produce one fixed finite observer complete for all unbounded comparisons, nor a finite-time algorithm that interrogates infinitely many probes. All results concern the concrete circle-index loop type, not arbitrary observation spaces or physical computation.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-signed-bound-admission.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

The earlier finite-family invisibility theorem observed each cyclic cover from its zero state, while these sufficient probes use calibration. Explicitly close that quantifier boundary: admit arbitrary finite starting phases as first-order observer data and prove a common-period nontrivial path remains invisible to any FIXED finite family of such phase-bearing cyclic observers. Do not silently infer an arbitrary-phase theorem from the existing zero-phase result.
