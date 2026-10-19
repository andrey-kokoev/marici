# Native feedback endpoints: rejection and retained-payload refinement

## Iteration result

Freshly inspecting the actual native constructor and table contract identifies another nontrivial binding constraint, beyond the matrix fixture's32-versus1 policy ambiguity.

`TriangleComparisonFeedbackRegression.Feedback.run` maps every input comparison to the SAME outer source presentation A and target presentation C. It is injective on retained input comparisons. Consequently its outer presentation endpoints cannot constitute an endpoint-unique row table with multiple distinct inputs.

This is now formally proved using the existing native input and its exchanged counterpart, whose inherited questions are(1,2) and(2,1). No fabricated137-row native fixture is inserted.

The rejection is conditional on `TableFibrationCycle.UniqueEndpoints`. Tables without this requirement may legitimately contain parallel records; feedback itself is not rejected.

## Exact formal gate

Define the proposed table fields directly from the actual constructor:

    from(c)=source(run c),
    to(c)=target(run c).

Existing `run-source` and `run-target` show equality of both fields for every pair c,d. Under endpoint uniqueness, those equalities would imply c=d. The attached inherited question disproves this for c=exchange(input), d=input.

Distinct native outputs remain distinct: promotion retention does not repair their outer endpoint collision.

Module: `agda/NativeFeedbackEndpointBindingGate.agda`.

## Constructive endpoint refinement

The constructor already retains a decoder. Expose that actual retained payload in the port fields:

    refined-from(c)=(source(run c), decode(run c)),
    refined-to(c)=(target(run c), decode(run c)).

The formal module proves endpoint uniqueness for these fields using `decode-run`: equality of refined source ports already recovers equality of inputs. No fresh identifier, extra face equation or changed feedback operation is required.

However this refinement changes the context relation. Different FULL payloads now have different ports, even where their underlying record target keys might agree. Therefore this is a genuine candidate endpoint table, not automatically the intended table and not an operation-preserving identification with the incoming-family matrix promotions.

## Test the actual matrix candidates against the same requirement

The executable audit freshly rebuilds the full geometric record binding and checks label and endpoint-pair uniqueness at the input and both promotion rounds.

The137 original rows have unique endpoint pairs. Both matrix policies have unique promoted endpoint pairs because every family receives a fresh assembly source key. Thus endpoint uniqueness alone does not choose between:

- inherited-key:32 final rows;
- common-target:1 final row.

The native outer presentation table, the native payload-refined table and these matrix promotion tables therefore have DIFFERENT endpoint signatures. None can be identified solely from retention or the word "promotion".

## Precise next obligation

An intended-T9 adapter must match the admitted common-target context relation, not just injectively label records or reproduce their scalar values.

The available interfaces now make that test executable:

1. native outer presentation ports: all inputs share the same endpoints;
2. native decoded-payload ports: distinct full inputs have distinct target ports;
3. matrix inherited ports: inputs are related by original target-key fibres;
4. matrix common port: all retained inputs share a next target.

The next binding test should compare these relations and the induced record composition domains. Any intermediate endpoint relation must be explicitly selected; the refined-port theorem itself does not authorize a physical successor.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeFeedbackEndpointBindingGate -Fresh
    uv run research/nima/checkers/check_native_feedback_endpoint_binding_gate.py

Fresh safe Cubical/guardedness closure passes with ignored interfaces and stable source inputs.17 executable audits pass, including current proof/source hashes and both actual promotion table signatures. Dependencies freshly rerun the3495-check decorated record binding and its original numerical/flat-attachment chain.

Artifacts:

- `agda/NativeFeedbackEndpointBindingGate.agda`
- `results/agda-NativeFeedbackEndpointBindingGate.json`
- `checkers/check_native_feedback_endpoint_binding_gate.py`
- `results/native-feedback-endpoint-binding-gate.json`

No postulates or intended-T9 completion claim were introduced.
