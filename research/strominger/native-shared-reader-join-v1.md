# Native shared-reader join: construction versus identification

## Result and correction to the search target

A shared-reference join can be derived from the existing native rules **without assuming an equivalence of its two operands**. Its operand derivations are retained and recoverable. An equivalence between the two enriched, ordered joins is then derived, rather than supplied as a premise.

This closes a generic construction obligation. It does **not** establish a native Su-32 history filler, select a physical interaction, or construct the globally coherent Su-32 assembly. The native record-interface instance and the finite geometry checks remain separate, with their binding open.

The earlier `check_su32_layer4_comparison.mjs` already established the eight-versus-four Boolean count and the failure of a left-view-only reconstruction. Those are not new discoveries here. The additions are:

1. a native derivation using the existing indexed-table backend and actual input `Resolve` proofs;
2. exact recovery of those proofs through native premise ports;
3. a native comparison of the enriched joins, with a constructed equivalence;
4. classification of **all** shared-reader-preserving Boolean bijections at every tested source comparison interface;
5. a specific independent-payload reencoding under which every such bijection graph ceases to be a function graph, while the shared-reference relation remains valid.

## The typed construction

Let `a` and `b` be native packages with carriers `A` and `B`, shared readers `rA : A → E`, `rB : B → E`, and actual agreement at their selected values. Define

\[
J=\sum_{x:A}\sum_{y:B}(r_A(x)=r_B(y)).
\]

This is a joint retaining both operands and the compatibility witness. It is not a function `A → B`, and it does not equate independent P records.

The source's `E` rule requires a whole *pointed* family. We therefore do not silently treat formation of an arbitrary dependent type as an admitted resolution. The implemented derivation is:

1. apply native reflexivity to each actual operand derivation;
2. apply native `Pi` to retain both resulting loop packages;
3. use `J` as the index of a native `E` family with that constant retained provenance, selecting `(value a, value b, agreement)`.

The resulting carrier is `J` together with the two retained input loop witnesses. Generic loops are **not** erased or assumed contractible. The selected witnesses are reflexivity. In a set-valued fragment these loops add no distinct value choices, but their construction histories remain.

The derived operation takes both actual input `Resolve` proofs. Following three native premise ports recovers each exact input proof definitionally. No output, compatibility filler, or desired comparison is admitted as a seed.

Swapping `(x,y,p)` to `(y,x,sym p)` and exchanging the two provenance entries gives an actual carrier isomorphism. Its inverse, selected-value law and both reader laws are proved. The native comparison rule is applied **after** deriving that isomorphism, to the enriched joins—not to the original branches.

## Prepared native instance

`agda/NativeSharedReaderJoin.agda` also supplies a family parameterized by a four-record Boolean registry. The only admitted seeds are its four tagged input records. Native `Pi` constructs the preparation; its premise ports supply the two channel derivations sharing the same `E+` record. Their agreement is reflexivity.

The join and enriched exchange have actual native closure derivations. A full package retains the complete preparation, including unused `E-`, alongside the join.

A formal counterexample proves that the left projection of the joint carrier is noninjective: the right P value can change while the left operand stays fixed. This is a theorem about the whole carrier, not an assertion that an arbitrary counterfactual value was executed from the selected preparation.

These tags have **not** been promoted to native geometric occurrences, signal routes, or port addresses. This is an admitted record-interface instance, not the completed Su-32 adapter.

## Source-specific finite discriminator

The independent checker constructs the existing complete atlas and checks its restrictions: 36 charts, four sign bindings, four comparison sites per binding, hence 576 interfaces. It does not generate or certify a global physical object by local extension.

At each interface, the varying reference has two independent Boolean records and the common reference has one:

- each operand carrier has four values;
- the compatible-pair relation has eight values;
- precisely four whole-operand bijections preserve the complete shared record;
- each such bijection has a four-pair graph;
- each compatible pair lies in exactly two of those graphs.

Thus **no one fixed equivalence graph is the whole compatibility relation**. A state-dependent choice of equivalence could cover more preparations, but would be extra structure; the relation does not select it. This is not a proof that no equivalence exists at any particular prepared pair.

The checker also uses the existing `mapReferencePayloads` API to collapse only the plus-record payload of the varying role. Every compatible pair remains compatible. But the image of any of the four equivalence graphs has two left values, each paired with two right values: it is no longer a function graph.

That is a falsifier **if** independent payload-map naturality is required of a proposed law. The existence of the mapping API does not itself impose that naturality axiom on every physical operation. A more structured operation must state which payload transformations it respects.

## Remaining hard boundary

There are two distinct obligations:

- **Native formation:** can both inputs and their shared-reference evidence be jointly retained? The generic native construction above answers yes.
- **Native source binding and identification:** are these readers, input derivations and outgoing-port actions the intended Su-32 operation, and does any further rule compare the original histories? This remains open.

The next adapter must connect actual Su-32 preparations and oriented incidences to the typed native operands, preserve full record identities and histories, and verify the real continuation interface. Merely relabeling the tagged Boolean instance, or choosing a constant location reader, would not discharge that obligation.

No period-return relation, history quotient, phase law or global uniqueness theorem follows. Existing JavaScript `nativeFiller:null` fields remain unchanged.

## Verification

```sh
python research/strominger/checkers/check_native_shared_reader_join.py
```

This runs a fresh `--ignore-interfaces --safe --cubical` Agda closure check, three expected-failure modules (incompatible shared-reader agreement, missing operand derivation, and wrong reference identity despite equal scalar payloads), and the finite source-interface checker. It records a conservative include-root source inventory, tool version/hash, commands and diagnostics. Dependency warnings are confined to the existing Cubical unsupported-indexed-match warnings; repository warnings are rejected.

Receipts:

- `results/native-shared-reader-join-v1/verification.json`
- `results/native-shared-reader-join-v1/dependency-manifest.json`
- `results/su32-join-type-boundary-v1/verification.json`

No existing native schemas, source seed policies, or comparison/attachment implementations were modified.
