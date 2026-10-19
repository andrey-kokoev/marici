# Asymmetric native endpoints preserve a declared context relation

## Iteration3 result

The previous endpoint refinement put the entire decoded payload at BOTH ports. This achieved uniqueness but made distinct target fibres singletons. That over-refinement is unnecessary.

A freshly proved asymmetric interface uses

    source(c)=(source(run c), decode(run c)),
    target(c)=(target(run c), key(decode(run c))).

Here key is an explicit supplied context map on the actual native input type. The actual feedback constructor and decoder remain unchanged.

The full source payload guarantees endpoint uniqueness. The target exposes exactly the selected context key, not the entire payload.

## Formal operation-domain theorem

`NativeFeedbackKeyedEndpointBinding.Keyed` proves both directions:

    key(c)=key(d)  implies  target(c)=target(d),
    target(c)=target(d)  implies  key(c)=key(d).

Thus common-target composition is admitted exactly on the chosen key fibres. Equality of source ports recovers equality of inputs, so arbitrary target-fibre sizes remain compatible with endpoint uniqueness.

This is an exact endpoint-domain bridge for an actual native constructor. It is conditional on the key and on any encoding of another record source into the native input type; no137-row encoding into native `Compared` is asserted by a finite numeric analogue.

## Compare the actual fixture relations

The finite audit uses the existing full-path decorated records and exact target membership from both actual promotions. It tests three key choices:

| Key | Target fibres | Admitted ordered pairs | Unique asymmetric endpoint pairs |
|---|---:|---:|---:|
| original record target |32|977|137|
| constant |1|18769|137|
| full labelled payload |137|137|137|

The original-target key agrees EXACTLY with the inherited promotion's final leaf-pair relation. The constant key agrees EXACTLY with the common-target promotion's relation. Full payload identity loses840 originally admitted nondiagonal pairs. A constant key adds17792 cross-target pairs relative to the original record relation.

Concrete witnesses of both errors are retained in the result JSON. No new cross-target connector is authorized by this comparison.

Therefore endpoint uniqueness does not require either complete target collapse or complete target separation. An original-target-keyed native interpretation can preserve the existing977-pair composition domain, while a constant-key interpretation can model the common candidate's18769-pair domain. The choice still belongs to the source contract.

## Additional source-column contract must not be assumed

If the ORIGINAL record source column were required unchanged, collapsing all target keys on a137-row pointwise lift would destroy endpoint uniqueness: only32 distinct source/target pairs would remain. Keeping original target keys preserves original endpoint uniqueness.

This gives a conditional way to exclude that collapse under a stronger contract. But the actual matrix promotions deliberately use fresh assembly source keys. Consequently their source columns are not unchanged; the stronger condition cannot be silently imported to select inherited T9.

## Context matching is not constructor identification

Pointwise native `run` preserves one output for each distinguishable input. Applied recordwise, its keyed interface still has137 retained rows. Actual matrix T9 performs family aggregation and produces32 or1 rows.

Thus even perfect agreement of leaf-pair context relations does not identify pointwise feedback with incoming-family promotion. The next binding must be at the FAMILY level: specify the family carrier, membership measure, preserved decoded field, and whether the native constructor consumes a whole family rather than an individual leaf.

The full geometric numerical response and typed flat record attachments remain available for that family adapter. No scalar retuning is needed, and neither the key nor the family assembly is selected by the feedback retention theorem.

## Verification

    pwsh -NoProfile -File research/nima/checkers/check_cubical_agda.ps1 -Module NativeFeedbackKeyedEndpointBinding -Fresh
    uv run research/nima/checkers/check_native_feedback_keyed_endpoint_binding.py

Fresh safe Cubical/guardedness closure passes with ignored interfaces and stable inputs.24 exact interface/context checks pass, freshly rerunning the preceding native endpoint audit and full geometric record binding chain.

Artifacts:

- `agda/NativeFeedbackKeyedEndpointBinding.agda`
- `results/agda-NativeFeedbackKeyedEndpointBinding.json`
- `checkers/check_native_feedback_keyed_endpoint_binding.py`
- `results/native-feedback-keyed-endpoint-binding.json`

No postulates, native137-row encoding, physical endpoint selection or intended-T9 completion claim was added.
