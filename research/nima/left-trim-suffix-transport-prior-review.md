# Left trim requires a boundary-state choice or a suffix-transported inverse

## Question and disposition

Search narrowed to removing the earliest operation from the retained cavity segment without confusing record restriction, changed preparation and physical uncomputation.

The inspected prior work supplies two decisive clues: the actual segment API carries the prefix-produced boundary state, and the existing cavity round maps do not commute. Together they reduce the search to one particular comparison: a suffix-transported inverse on the complete pre-detection optical packet. That is an algebraic candidate formula, not an admitted laboratory control or an interval encoding.

## 1. The segment implementation already answers the restriction question

Source: `research/nima/checkers/check_physics_instrument_history_binding.py`, functions `segment`, `history`, `join` and the `segment composition` assertion.

The state-map comparison is explicitly

    segment(segment(initial, prefix), suffix, cut)
      == segment(initial, prefix + suffix).

The suffix consumes the **actual prefix-produced branches**, including unnormalized weight, memory and optical state. It does not consume `initial` again. The separate history API stores start/end bins, source, port, outcome, occurrence and memory policy, and joins only matching bins.

Therefore extracting a suffix description with its actual boundary state is a restriction/rebasing of the same run, not erasure of the prefix's physical effect. Running the suffix from the original preparation is a different experiment. The library does not contain an admitted state-changing left-trim constructor implementing that experiment.

## 2. The source already distinguishes based inverse action from unbased cancellation

`research/kitaev/fault-position-calculus-controlled-commutator.md` transports an insertion at a specified location by conjugation with the corresponding prefix. It retains actual operation order and separates an internal insertion from a common final operation. This is the relevant prior mechanism: moving an operation through an executed word changes it by conjugation.

The following is an algebraic deduction for this search, not a theorem quoted as an existing cavity implementation. Write a full optical word as

    V = S A,

where A is its first chronological operation and S is the remaining suffix; rightmost acts first. If removing A means producing S x from S A x **with the same original full input x**, a final correction on all inputs must be

    D = S A^(-1) S^(-1),
    D S A = S.

The bare A inverse works instead only when A and S commute. If removing A means starting the suffix at its actual boundary state A x, then no output correction is needed: S(A x) is already the original result. These two meanings must not be merged.

For density states, the same calculation applies through unitary conjugation; global phase is immaterial unless a coherent-reference interface retains it. Operator equality here is the full amplitude/route convention of the inspected cavity model.

## 3. The existing cavity model makes the difference nonvacuous

Source: `research/nima/checkers/check_physics_geometric_candidate.py`, `round_map` and the `ordered-history hostile`.

The checker explicitly tests W1 W0 != W0 W1. The rounds share returning mode 0 but use different fresh input/output slots. Direct substitution in its rational coefficients gives a simple amplitude witness:

    (W0 W1)[1,4] = (4/5)(48/125) = 192/625,
    (W1 W0)[1,4] = 0.

Mode 4 is the next round's incident input; mode 1 is the first round's reflected output. W1 leaves mode 1 untouched, whereas applying W0 after W1 transfers some of the new returning amplitude there. This arithmetic is derived from the inspected code; no checker was rerun during this search.

Thus the proposed two-round correction is specifically

    D = W1 W0^(-1) W1^(-1),

not W0 inverse alone. A possible operational factorization would undo the suffix, undo the first round, then replay the suffix, provided every one of those operations and all retained ports are admitted. The existence of orthogonal matrices in the model does not supply that control authority.

The scalar compressed recurrence can conceal this issue because its scalar coefficients commute. It is not a substitute for this full-port comparison. Nor does the formula preserve an old execution word as though the correction never occurred: any actual correction adds its own retained execution record.

## 4. Suffix state cannot be reset by dropping its prefix record

`research/sontag/detector-memory-comparative-reconstruction.md` gives an independent operational witness. After a click the detector is dead, so an immediate photon has click probability zero; from a newly ready preparation the same photon has probability 9/25. A suffix supplied with the wrong boundary memory therefore changes its law.

`research/aspect/higher-history-memory-falsifier.md` strengthens the warning: a reset passing one-predecessor marginal checks can retain two-back dependence, detected by predictive Hankel rank three. Neither deletion of labels nor a weak reset test authorizes independence from the prefix.

`research/kitaev/coherent-memory-combs-and-tester-kernels.md`, Coherent continuation criterion and Same scalar, different comb, supplies the corresponding quantum-process boundary: endpoint agreement for one closed sequence does not determine responses to alternative intermediate interventions. A proposed inverse needs an admitted continuation, not only equal final scalar records.

## Resulting focus and stopping condition

Use the existing W0,W1, complete port labels and retained histories to distinguish:

1. suffix restriction with inherited boundary state;
2. suffix execution from the original preparation;
3. physical implementation of the suffix-transported correction.

The first is already supported as segment semantics. The second is a distinct preparation policy. The third has the explicit candidate operator above but no inspected apparatus authorization. An independently justified interval-to-segment encoding is still absent. No source-law, clock or AdS/dS conclusion follows.

Stop searching broadly for a generic reversible device. The remaining source search is specifically for admitted inverse/replay control of the actual cavity suffix and accessible retained ports, with a policy for recording the correction. Do not manufacture that authority from the conjugation identity.

## Follow-up search: was inverse/replay authority already answered?

The answer splits by scope; the search found no completed physical cavity inverse/replay binding in the inspected sources.

- **Inverse-word synthesis already exists in another declared model.** `research/strominger/encoder-bidirectional-meeting-v1.md` explicitly joins a forward word to the reversed backward list with inverted phases. Splitting its existing certified 468-gate word tests the convention; omitting order reversal produces a large residual. The packet calls this a reversible software-control model and explicitly disclaims hardware admission. It is not the retained optical cavity's control package.
- **Optical inverse-readout compilation already exists.** `research/aspect/comparison-loop-minimal-analyzer-mesh.md` and its actual checker compile a 19-rotation analyzer ladder and reverse it. The contract preserves one analyzer/readout, not the earlier full Householder action on its orthogonal complement. Its emitted status is `compiled_not_programmed`, with `physical_status: not_run`. It cannot be substituted for full-port state recovery.
- **Complete logs do not supply coherent port access.** `research/aspect/coherent-port-versus-classical-log.md` gives orthogonal input states whose full computational-basis environment logs coincide, while coherent access permits inverse dilation. Thus retaining every event is insufficient for the proposed full-state undo/replay.
- **The physical binding remains explicitly unfilled.** `research/aspect/comparison-loop-hardware-binding.md` leaves device/control/calibration fields null. `research/aspect/apparatus-capability-receipt-gate.md` uses fixture-only authentication and reports no live hardware execution. The cavity plant and Sontag's completed audit likewise withhold controller authority; sampled controllability is not a full-joint inverse-control certificate.
- **Logical reversal is not a physical reverse protocol.** `research/voevodsky/opposite-analytical-pullback-and-causal-admission-have-distinct-boundaries.md` constructs a coordinate reversal while rejecting reversal of the original issue/receive schedule. This is a separate source, not an optical result, but confirms that the missing admission cannot be filled by an opposite diagram alone.

Consequently the generic inverse-order mathematics is not a new open research problem. A cavity-specific full-port compiler comparison could still be carried out at conditional model scope. Physical execution is blocked by coherent-port access and calibrated inverse/replay controls, not by an unknown conjugation identity. Further searches over the same packets will not supply those authorities. The interval-to-segment identification remains a separate missing map.

Verification boundary: bounded source/code inspection plus the displayed elementary algebra and rational entry calculation; no fresh checker execution, foreign mutations, apparatus trial or programme-status changes.
