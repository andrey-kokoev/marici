# A retained higher comparison for repeated interchange

## Result

A concrete three-constructor diagram now has a kernel-checked higher comparison
between its two resulting COMPLETE interchange fillers, not merely agreement of
the final source vertex.

The diagram starts with the nonidentity A->B source comparison and source
attachments AB and BC. Their transported attachments are BA and AD. Both routes
have active final boundary D, but the interpreted final outgoing carrier still
has two values: this is not a singleton endpoint test.

The theorem compares:

- a staged route, moving the comparison through the second attachment and then
  lifting the first interchange through the remaining attachment;
- a direct route, using a graph comparison and a pointed loop bridge to compare
  the same source and target interfaces in one map.

The certificate retains both full fillers, all intermediate Body records, the
native comparison-leg derivations, and the higher witness.

## The parallel boundaries are explicit

`RepeatedInterchangeCoherence.agda` names three Body objects:

- source: comparison of the two twice-attached operands;
- middle: attachment of their once-attached comparison;
- target: two attachments after the original comparison.

The sequential map composes the existing second interchange with the lifted
first interchange. The direct map factors through the comparison graph and
transports the actual pointed loop witness into the final attachment carrier.
Both have precisely the same source and target interpreted types.

The original route packages are not identified by endpoint coincidence. Rather,
two maps BETWEEN fixed retained route packages are compared. All original
comparison and attachment provenance remains available in the certificate.

## What makes this higher witness constructible

The proof first establishes relevant local truncation facts:

1. Vertex is a set, as previously checked.
2. Out(v) is a set: in this simple six-arrow source, its target projection has
   a checked retraction onto the actual outgoing incidence witnesses.
3. The old comparison graph is equivalent to its source carrier and is a set.
4. The relevant attachment carriers are sets, so their loop-witness types are
   propositions.

Both route maps compute the SAME final outgoing-edge component. Their loop
components agree by these proved local facts. Function extensionality and
comparison of equivalence records then give equality of the two equivalences.

The actual comparison filler includes more than its equivalence:

    Sigma(e:source~=target)
      [(e(selected_source)=selected_target)
       x (all source-port readings commute with e)].

The target carrier's sethood makes the selected-value proof fiber propositional.
Vertex sethood makes the whole-carrier port-law fiber propositional. The map
comparison therefore lifts to equality of COMPLETE fillers, including these
witnesses.

Selected-value witnesses are normalized through their proved uniqueness rather
than expanding very large composed Cubical transport terms. The original leg
witnesses are still stored in the raw diagram; this is not a claim that arbitrary
proofs or native derivations are irrelevant.

## Retained comparison and native-history compatibility

Applying the internal compare constructor to the two complete fillers gives a
path between their retained comparison Bodies. Applying the native interpreter
along that path gives a dependent path between their actual Resolve derivations,
with the varying complete output package as its index.

The final certificate stores:

- the raw source, middle and target Bodies;
- the actual lower interchange and lifted-comparison Bodies;
- their compiled native endpoint/history records;
- the sequential and direct complete fillers;
- both final native comparison derivations;
- the path between the complete fillers.

The whole certificate is reified in the next universe with exact recovery.
A Complete path package containing the higher witness is also FORMED using the
existing whole-package path constructor.

Important admission distinction: no `Resolve Seeds` derivation of that newly
formed higher-path package is claimed. Native derivations of the two comparison
outputs and their dependent compatibility are proved; automatic admission of
the new higher package through a native higher-rule is a separate obligation.

## Hostile: identical ports and selected points do not force coherence

The companion obstruction module changes the contract by adding two independent
Boolean witness fields to Out(A). Identity and coordinate-swap equivalences:

- preserve every port reading;
- fix the selected (AD,false,false) value;
- nevertheless differ on (AB,false,true).

Agda proves that NO equality between these equivalences exists. A negative
module asserting their equality by reflexivity is rejected. The finite control
finds four differing values among the eight retained states.

This is not a counterexample to the exact outgoing-edge contract used by the
positive diagram. It shows why the positive proof must establish agreement of
the full maps and inspect their witness fibers: endpoint and port agreement
alone are insufficient when extra retained distinctions are admitted.

## Scope of the coherent-interface conjecture

The local test is positive: one repeated interchange diagram has a retained
higher comparison preserving both routes and their native histories.

It does not establish:

- coherence for arbitrary non-set-valued carriers;
- all interchange pentagons, cubes, or all-dimensional coherence;
- a unique source/target continuation convention;
- an automatically admitted native higher operation from every formed path;
- a universal theorem that all competing constructions have a filler.

The source contract and target-side continuation policy remain those of the
previous internalization test. No physical time or event interpretation is
assigned to the attachment positions.

## Verification

    python research/strominger/checkers/check_repeated_interchange_coherence.py
    python research/strominger/checkers/check_internal_comparison_interchange.py

Both fresh headless closure checks pass under Agda 2.8.0.1 / Cubical 0.9 with
ignored interfaces. The new safe Cubical/guardedness modules have no postulates,
holes or unsupported indexed-match warnings. The intended new negative control
exits 42; both prior internal-comparison negative controls still exit 42.

Two previously checked point-law definitions in InternalComparisonInterchange
were made `abstract` to avoid expanding nested proof normal forms during repeated
interchange checking. Their implementations and types are unchanged and freshly
rechecked; this is proof opacity, not an added axiom.

Artifacts:

- `agda/RepeatedInterchangeCoherence.agda`
- `agda/InterchangeHiddenFiberObstruction.agda`
- `agda/negative/InterchangeBadEndpointOnlyCoherence.agda`
- `checkers/check_repeated_interchange_coherence.py`
- `results/repeated-interchange-coherence.json`
- `results/repeated-interchange-coherence-positive.log`
- `results/repeated-interchange-coherence-negative.log`

Source hashes remain stable across verification. Temporary diagnostic probes
were removed. Only Strominger-owned sources, checkers and reports were edited;
dependency interfaces may be refreshed. No physical claim, graph publication,
commit or push.
