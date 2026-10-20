# Canonical comparison synthesis from actual generated operands

## Closed question

Can the classified fragment construct a compatible native comparison without accepting a new equivalence or image-agreement function as input?

**Yes.** `CanonicalComparisonSynthesis.Compile mode left right` takes only the mode and actual generated operands at the required source/target vertices. Its `run` returns:

- **Success:** a derived full comparison certificate, a computed `compareF` term retaining both exact operand terms, and its actual native admission; or
- **Refusal:** a separating vertex, a witness in one actual reader fiber, and a proof that the other transported reader fiber is empty.

The refusal refutes every compatible complete filler for those operands and that mode. Completeness proves that any existing compatible filler implies acceptance. This is a total constructive procedure on arbitrary finite `Fragment` syntax, not a lookup table limited to the displayed examples.

## What was previously missing

`GeneratedReaderClassification.Comparisons.filler-from-images` already constructed a filler from supplied `ImageAgreement`. That was the correct constructor, not a missing native rule. The new program computes the agreement or its obstruction from the existing normalizer and the actual six-arrow incidence, then calls that constructor.

No historical theorem or native schema is modified.

## Algorithm and parameter origin

1. Compute each operand's reader-preserving normal form: `whole` or `outgoing v`. The normalizer consumes the actual syntax and retains its existing dependencies.
2. Decide image membership. `whole` contains every vertex; `outgoing v` membership is decided from the actual indexed `Edge v w` constructors. Negative cases are typed empty eliminations.
3. For each vertex w, compare membership in the left image with membership of `act mode w` in the right image. Search order is A,B,C,D.
4. If all memberships agree, construct both directions of normal-form image agreement and transport them through the normalizer's equivalences to the actual reader fibers.
5. Invoke `filler-from-images` to derive the equivalence, selected-point equality and whole-carrier port law. Construct `compareF mode left right` with those parameters and use the unchanged native comparison rule with the actual operand derivations.
6. On mismatch, transport the membership witness and emptiness proof to the actual operands. `refutes` turns any alleged filler into a contradiction using its reader action.

`Success.term` and `Success.admission` are computed definitions, not independently replaceable fields. A fresh seed cannot be substituted into the emitted comparison while keeping its certificate.

The vertex enumeration selects the first diagnostic witness, not a physical preference. Complete successful fillers are proposition-valued under the existing fragment theorem; the emitted native proofs are compared along that exact filler path. This does not contract arbitrary native histories.

## Actual regressions

- Whole source at A versus whole source at B, in exchange mode: **accepted**. Native output is constructed.
- That output is compared with the actual earlier `nonidentity A` implementation, with both Body equality and a dependent path between native derivations. The old comparison is used only as a post-synthesis regression target, not an input to the compiler.
- Attachment out of A via AB versus attachment out of B via BA, in exchange mode: **accepted**, with native output.
- Whole source at A versus the CA attachment selecting A, in stay mode: **refused at B**, despite the same selected vertex.
- A synthesized comparison can itself be supplied to another synthesis call; that repeated call is accepted and natively admitted.

`CanonicalComparisonSynthesisRegression.agda` additionally proves all **50** mode/normal-form cases by reduction: **10 accept, 40 refuse**. The checker independently recomputes these outcomes from the original typed incidence. Some shape pairs cannot simultaneously realize the required selected vertices; this table does not assert otherwise. The general theorem is about actual well-typed operands, not the finite table alone.

## Exact scope

- Only the declared `Fragment`, not arbitrary `prepared` Body readers or all native WG programs.
- Initial native proofs are arbitrary actual inputs and are retained, not reset to root seed proofs.
- **New comparison parameters are derived.** Existing `compareF` nodes inside operand histories may already contain supplied equivalences or witnesses. Their entire parameter provenance is not retroactively certified.
- The existing target-side continuation convention is retained. No policy selection theorem is added.
- Coherence of emitted comparisons with existing fillers is scoped to this complete filler fiber. Forward/forward diagram binding, chosen higher overlaps, non-set witnesses and global coherent actions remain separate obligations.

## Verification

    python research/strominger/checkers/check_canonical_comparison_synthesis.py

Fresh safe Cubical/guarded Agda closure, with ignored interfaces and implicit libraries disabled, passed. The regression root imports the full implementation. Three negative controls reject accepting the same-point mismatch, resetting the output to a fresh seed, and supplying an arbitrary prepared Body instead of a Fragment.

The checker locks a conservative 2,299-file include-root/primitive inventory and verifies stable sources. Existing Cubical indexed-match warnings are recorded; no repository-source warnings were reported for this closure.

- Source: `agda/CanonicalComparisonSynthesis.agda`
- Regression: `agda/CanonicalComparisonSynthesisRegression.agda`
- Contract and origin ledger: `contracts/canonical-comparison-synthesis.v1.json`
- Receipt: `results/canonical-comparison-synthesis/verification.json`
- Dependency lock: `results/canonical-comparison-synthesis/dependency-manifest.json`
- Connected net: `wg-source-determination-conjecture-net-v1.md`

## Next bounded use

The canonical-comparison-synthesis node is closed at its stated scope. Its completion unblocks broader parameter-origin work, without claiming that work finished. The next recommended existing gate is **forward/forward Body binding**: use the actual forward-lifted operand histories and this compiler where applicable, rather than inventing a fresh comparison or resetting the inputs. The typed interface between that diagram and this Fragment must still be constructed and checked; the compiler alone does not close the diagram.
