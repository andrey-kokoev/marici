# Actual finite transcripts suffice for the adaptive obstruction

`agda/ObserverTraceLocal.agda` extracts only periods queried along the executed branch. A checked equality identifies this list with the periods extracted from the complete transcript; unvisited branches contribute nothing.

The trace-local replay theorem needs agreement only for these queried periods (at all phases). After the current reply is identified, its proof follows only the selected successor. Applied to the zero-loop run, the product of actually queried periods gives a semantically nontrivial alternative loop with the SAME complete transcript, including probe identities, typed replies and terminal label.

Two consequences are checked:

- No transcript decoder faithfully reconstructs every loop.
- No predicate of this finite transcript can both accept the zero-loop transcript and soundly certify that its input was the zero loop over the unrestricted loop domain.

The second theorem concerns logical certificates based on the transcript; the predicate is not a new observer primitive. A supplied domain bound can invalidate the alternative-input argument, consistently with the earlier bounded-recovery theorems.

## Scope

The protocol model is still the existing finite first-order binary tree language. The argument is trace-local but has NOT been transferred to arbitrary recursive, merely terminating, randomized, or physical controllers. Equality of transcripts is mathematical equality; no resource-cost or causal theory is asserted. Exhaustion of a dispatch does not terminate the programme.

## Verification

Fresh safe Cubical Agda --ignore-interfaces -Werror passes: results/agda-trace-local.log. Aggregate imports include the module. Fresh check_transport_gate.py passes local/whole ordinary/whole strict checks with inventoried source bytes unchanged: results/transport-gate.json.

## Next

Refresh the canonical aggregate observer checkpoint rather than continuing to cite its old historical receipt. Audit exact entry coverage, source integrity, strict compilation and negative controls, and consolidate the now-checked internal observer, signed-bound and adaptive-transcript boundaries. Keep broader-controller extension and conditional bounded stopping certificates as explicit research directions, not claims already established.
