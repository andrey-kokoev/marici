# Corrected record carrier: embedding, normalization, and a unique native filler

## Result

`agda/Su32RecordReaderClassification.agda` proves that the corrected Boolean carrier from `Su32CoherentReferenceCarrier` is equivalent to its complete four-record reader. It derives an actual native comparison between two full context presentations and proves the corresponding pointed, full-record-preserving filler type contractible.

This is a new classification of the specific corrected record fragment. It does not apply the existing four-vertex compiler to unclassified Su-32 operands, and it does not identify those vertices with physical cells.

The compared presentations are:

- preparation first, coherent consumer second;
- coherent consumer first, preparation second.

Both retain the same complete context and native operand derivations. They are **not** the original two five-cell incidence histories, nor the entire JavaScript contextual-exchange state with external path words and antecedent records.

## Why the whole-carrier constraints mattered

The earlier audit found that raw products admit inconsistent copies of records. A producer pair has 64 independently variable Boolean values but only 16 common-preparation values. Raw preparation-times-producer similarly has 128 values rather than 16.

The corrected native carrier stores the overlap equality between its two producer packets and the equality between its consumer records and the retained preparation. These constraints hold at every current value.

The classification now proves, rather than infers from selected examples, that the constraints are sufficient:

1. Each tagged Boolean input record is a set.
2. The dependent channel function carriers are sets.
3. For a retained join of set-valued operands with a set-valued shared reader, its current provenance loop witnesses are propositions. Its compatibility paths are propositions as well.
4. Equality of both operand projections therefore determines a join value.
5. The four record fields determine every channel value in the coherent consumer. The shared-reader paths determine its repeated fields.
6. Equality of the preparation reader determines the full corrected context value.

This proves a reader embedding. An explicit reconstruction from arbitrary four records then proves a full isomorphism

\[
\mathrm{CurrentValues}(\mathrm{Full})\cong
\prod_{r\in\{P+,P-,E+,E-\}}\mathrm{RecordAt}(r).
\]

The normal form thus has sixteen Boolean values. The formal theorem is the isomorphism to the four-record type; the accompanying finite control enumerates its sixteen tuples.

The reconstruction produces **current values of one fixed native package**. It does not seed new histories or identify a family of varying packages with one package carrier.

## Computed native comparison and uniqueness

The existing derived join exchange swaps the preparation/consumer order and the corresponding retained provenance entries. Its equivalence and selected-value path are constructed from the native record structure.

For these fixed endpoints, define a filler to comprise:

- an equivalence of their complete current carriers;
- agreement of the selected values;
- preservation of the whole four-record reader at every current value.

Reader injectivity forces any two candidate equivalences to agree pointwise. Equivalence proof fields are propositions, and the selected-value and reader-law paths lie in sets. The complete filler type is therefore a proposition. The computed filler inhabits it, yielding contractibility.

`Reordered.native` applies the existing indexed native comparison rule to the actual two derived context operands. No arbitrary equivalence input, comparison-output seed, or new native rule is introduced.

The module also derives a native normalization comparison from the full carrier to its preparation-record presentation. This is an information normalization result; it is not an operation moving a packet from the central N back to the incoming N.

## Exact reader scope

The reader names all four references through the previously checked geometry dictionary. `physical-reader-injective` proves that equality of the physically named record readouts determines the full current value.

By contrast, a port-only reader still fails. The module constructs two distinct current values, differing at P-, with the same exact geometric output-port profile. An expected-failure module rejects their identification by reflexivity.

The finite control also exhibits two pointed, port-preserving permutations of the sixteen normalized values: identity and a transposition of two nonselected values. Both fix the selected all-zero point, but only identity preserves every complete record. This is an explicit countercontrol, not an exhaustive enumeration of all permutations and not a universal inference from noninjectivity alone.

The full-record reader law is the policy under which uniqueness is proved. This does not establish that every intended physical comparison must use that policy or respect these same observations.

## What uniqueness does not erase

Sethood and proposition-valued loop witnesses concern the current carriers of this Boolean fragment. They do not make `Resolve` proofs, native producer programs, earlier packages, or external path histories equal.

The native comparison retains both endpoint derivations. Its unique filler is not an equality of those derivations. No proof irrelevance of `Resolve`, cancellation through attachment, or period-return relation is used.

This follows the distinction in `native_filler_result.md`: a classified current-value comparison can be unique while its producer histories remain different and fully retained.

## Remaining physical boundary

This discharges the full-record reader/classification obligation for the corrected Boolean native fragment. It does **not** discharge:

- formation of the original Su-32 path/release operands with their complete physical histories;
- a source-admitted continuation or multiport operation at the charged cell;
- classification for richer, potentially higher payload fibers;
- a global physical assembly, phase action, or period-return identification.

The previously checked absence of two charged-cell internal wire transfers remains unchanged. A unique record-presentation filler cannot supply those edges or justify treating different continuation constructors as interchangeable.

## Fresh verification

```sh
python research/strominger/checkers/check_su32_record_reader_classification.py
```

The checker runs a fresh safe Cubical closure with implicit libraries disabled, checks the expected rejection of port-equality-as-value-equality, refreshes the prerequisite geometry/carrier audit and its negative controls, and executes the finite pointed-permutation control. It verifies source stability and records a conservative include-root inventory, tool hash/version, diagnostics and prerequisite receipt hash.

Report: `results/su32-record-reader-classification-v1/verification.json`.

Scope flags:

- `nativeRecordPresentationFillerDerived: true`;
- `nativeSignalExecuted: false`;
- `originalIncidencePathsCompared: false`.
