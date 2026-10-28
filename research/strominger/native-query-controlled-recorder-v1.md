# Native controlled recording exists; its physical isometry is not derived

## Correction to the frontier

The previous search identified controlled reflection as an apparatus route to coherent recording. Before importing another physical model, we tested whether the existing native constructors can already admit the reversible recorder.

They can. `agda/NativeQueryControlledRecorder.agda` constructs the controlled operation from the actual native transition query and binds it to the actual native-table filler interface.

This narrows the unresolved claim. It would be incorrect to say the source language cannot express a carrier-pointer interaction. What remains absent is a source-authorized physical interpretation preserving one fixed joint pairing.

## Constructed operation

The carrier is a supplied equivalence of the actual Vertex type, together with a Boolean record:

    Carrier = (Vertex ≃ Vertex) × Bool.

For queried endpoints x,y the operation is

    (e,b) -> (e, b xor [e(x)=y]).

The module proves for all supplied vertex equivalences and all record values:

- the source equivalence is unchanged;
- a false blank receives the exact native transition answer;
- executing twice recovers the complete initial pair;
- the operation is an equivalence of Carrier;
- it defines an actual filler between the corresponding pointed complete packages;
- translation through `Native.actual-filler-equivalence` executes the same recorder;
- retaining the filler recovers that exact recorder witness;
- identity and the actual ABC transport give different AB record outcomes.

The marked packages change with the recorded bit. The construction does not falsely call the operation a pointed automorphism of a package whose marked record must stay fixed.

The carrier ranges over supplied vertex equivalences, not only the generated A4 subgroup. Restricting its semantics to that subgroup gives the controlled-xor table used in the preceding finite model. No formal equivalence between an Agda enumeration of A4 and the Python enumeration is asserted here.

## What was supplied, and what was derived

The native compare/filler architecture accepts a supplied equivalence with its marked-value witness. We construct that equivalence using Boolean control, then pass it through the actual native interface. We do not add an axiom or alter the owner source.

The choice to use this recorder, the query endpoints, the source transport, and the blank are supplied task data. The source does not autonomously select or prepare them. An admitted native construction is not thereby an executable laboratory coupling.

This is native definability and native-table agreement, not synthesis from a fixed finite set of microscopic physical pulses. Thus it does not evade Kitaev's no-controlization theorem, which has a different gate-access contract.

## The norm obstruction survives

The existing exact pairing checker was rerun. With the same classical controlled-xor semantics, the positive non-diagonal carrier pairing and pointer overlap 1/2 still give

    squared norm 11/18 -> 7/12.

Thus the newly proved native equivalence cannot, by itself, establish joint isometry. Boolean storage and exact uncomputation are now native-checked, but their amplitude realization still needs a pairing and composition law.

The earlier conditional theorem remains available: if these recorders are isometric nondemolition interactions for a product pairing with distinct unit pointer states, their query sectors are orthogonal. If the triangle actions also preserve that carrier pairing, the finite carrier pairing is scalar counting. Those physical/numerical hypotheses were not added to the Agda theorem.

## Verification

    python research/strominger/checkers/check_native_query_controlled_recorder.py

Fresh headless Agda closure passed with `--ignore-interfaces --safe --cubical --guardedness` and a stable conservative manifest of 2,409 Agda files in the declared include roots. Inherited Cubical UnsupportedIndexedMatch warnings are retained in the log. This manifest is specific to this checker, not the earlier runners' larger include-root inventories.

The negative control claiming that ABC leaves the AB blank false fails with the intended UnequalTerms diagnostic (exit 42). The positive compilation exits zero. The 1,098 exact recording/norm checks also pass, retaining the counterexample rather than interpreting compilation as unitarity.

Receipt and logs: `results/native-query-controlled-recorder/`.

## Next question

Can the physical interpretation be required, independently, to preserve the source's constructed controlled recorders and triangle actions under one compositional tensor pairing? That would activate the conditional uniqueness theorem. It must be justified as an interpretation principle or apparatus law, not smuggled into the word “equivalence.”
