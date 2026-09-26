# Finite adaptive protocols cannot recover every comparison path

`agda/ObserverFiniteAdaptive.agda` adds first-order finite protocols: a terminal numeric label, or a phase-bearing cyclic probe, a literal equality-test value, and two stored successor protocols. Branch choice depends on the actual finite reply. No evaluator/access callback is a constructor field.

Execution returns the complete transcript: every queried probe identity, its typed reply, and the terminal label. The replay theorem proves that agreement on the relevant probe transports preserves the entire adaptive transcript, not just its final label.

Collecting periods from BOTH branches yields a finite family. Its positive common-period path produces exactly the same transcript as zero turns, while integer-cover transport proves those paths unequal. No decoder of the complete transcript can faithfully reconstruct every input comparison path. Phase-bearing/calibrated probes are included.

## Exact scope

This is a finite binary equality-test tree model. Both successors are stored as data, and the proof inventories all branches, including those not visited. It does not cover arbitrary recursive or merely terminating adaptive algorithms, unbounded search, or observers with other primitives. It also does not exclude input-dependent sufficiency when an external winding bound is already supplied.

The transcript theorem is a mathematical property of the fixed interpreter, not a physical causality or running-time result. Paths are accessed through the specified cyclic transports; unrestricted inspection of the supplied path term is outside this protocol language.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-finite-adaptive.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Localize the obstruction to the ACTUAL finite transcript on the zero-loop input. Derive a replay certificate using only periods queried along that branch, rather than a bound collected from the whole tree. Clarify what finite stopping evidence can establish and which extension to more general controllers still requires a separate theorem.
