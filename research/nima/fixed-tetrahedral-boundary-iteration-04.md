# Iteration 4: fixed tetrahedral boundaries and path-indexed extension

## Frozen question and test

SCC obligations: route/coherencer compatibility and attachment transport.

- Problem: iteration 3 completes a missing face, but does not classify fillers when every face is already fixed.
- Conjecture: an inhabited fixed-boundary filler space retains loop-space freedom; comparing two fillers means nullhomotopy of a residual loop. The useful universal property is unique dependent extension with the comparison path retained as an argument.
- Rivals: horn contractibility implies fixed-boundary uniqueness; extension can ignore its path argument; higher comparison changes the supplied face witnesses.
- Risky consequences: construct an equivalence with the actual loop space, an equivalence between comparison witnesses and residual nullhomotopies, and four lifted face-chart equivalences, all over fixed faces. A dependent interpretation must detect two loops with the same endpoint.
- Test: fresh safe Cubical Agda check of `FixedTetrahedralBoundary.agda` and an expected false/true rejection in `FixedBoundaryBadErasure.agda`.
- Disposition: the generic loop classification, grade-four comparison, four lifted charts, and path-indexed extension theorem pass fresh safe Cubical Agda. Endpoint-only extension is refuted. A concrete pair of inequivalent tetrahedral fillers at one fixed four-face boundary remains unconstructed.

## Fixed-boundary comparison

`FixedTetrahedralBoundary.OnEdges.OnFaces` fixes the four vertices, six edges, and all four triangle witnesses. Let L and R be the two composed face routes from iteration 3 and let F=(L=R) be their tetrahedral filler type.

Given a reference filler b:F, concatenation with its inverse gives

\[
F\simeq(L=L),\qquad t\longmapsto t\cdot b^{-1}.
\]

The reference filler maps to the identity loop up to the retained cancellation witness. `fixed-boundary-uniqueness` proves

\[
\operatorname{isContr}(F)\simeq\operatorname{isContr}(L=L).
\]

This is conditional on a supplied filler b; it constructs neither a filler for an empty F nor a contraction of the remaining loop space. `change-base` and `change-base-correct` construct the equivalence between two reference-filler descriptions and its commuting witness.

For two supplied fillers s,t:F, `residual-test` proves

\[
(s=t)\simeq(s\cdot t^{-1}=\operatorname{refl}).
\]

A grade-four comparison is thus a nullhomotopy of the actual residual loop, not an equality of diagonals or a numerical test. `grade-four-equivalence` identifies it definitionally with the earlier globular grade-four filler while all original face data remain parameters.

The four `compare012`, `compare123`, `compare013`, and `compare023` equivalences transport comparison witnesses through the corresponding face descriptions. `reverse-comparison` reverses the two face routes. These operations do not establish a cyclic vertex-rotation law or a four-simplex boundary theorem.

## A more explanatory universal property

`PathIndexedExtension.PathYoneda` proves the dependent path-Yoneda form of identity elimination. For any type A, point x:A, and family Y:A -> Type,

\[
\left(\prod_{y:A}((x=y)\to Y(y))\right)\simeq Y(x).
\]

Evaluation is at (x,refl); its inverse is transport along the supplied path. For any prescribed value at x, the space of extensions together with their agreement witness is contractible. The left inverse is proved by path induction, not by assuming path irrelevance.

This says: a value extends uniquely along retained identifications. It does not say that different identifications have the same action.

`FiberYoneda` derives the same property for the fiber of an equivalence e:X equiv Y at a target r:Y. Put c=e inverse(r). For any D:X -> Type,

\[
\left(\prod_{z:X}((e(z)=r)\to D(z))\right)\simeq D(c).
\]

The explicit witness equivalence (e(z)=r) equiv (c=z) connects this statement to path Yoneda. The interpretation family may depend on the missing value itself, not only on the supplied horn. `MissingFaceInterpretation` instantiates it at the tetrahedral 023 horn using the previously proved face-to-route equivalence.

At a fixed tetrahedral boundary and reference filler b, the same path-Yoneda module supplies interpretations indexed by comparisons b=t. Its total comparison package is contractible:

\[
\operatorname{isContr}\left(\sum_{t:F}(b=t)\right).
\]

Only the second filler varies during this contraction. It gives no automatic inhabitant of b=t for a separately fixed t.

## Retention controls and exact residual

Take A to be the universe of types, x=Bool, Y(X)=X, and starting value false. The unique transported section evaluates to false on refl and true on the univalent Boolean-negation loop. Both loops have the same source and target Bool.

`no-loop-erasure` proves there is no single Boolean value agreeing with this section on every Bool loop. The negative module tries to equate those two evaluations by reflexivity and is rejected with false/true unequal terms.

A separate checked control proves `isContr (Bool = Bool)` impossible even though the based comparison package at refl is contractible. Therefore contractibility of the total comparison package cannot by itself imply contractibility of its ambient fixed-endpoint path space.

These are concrete universe-level tests. They do not supply a pair of distinct grade-three tetrahedral fillers with one fixed boundary; that requires a higher-dimensional example. The tetrahedral theorem currently gives the exact loop-space criterion rather than such an example.

## Outward test against the original retained-change structure

After constructing the path universal property, the outward test was to replace identity paths by the original E-arrows. Freshly reading `RetainedComparisonStructure.agda` exposes a decisive distinction: its explicit model has P=Bool and an inhabited E(false,true), while false=true is empty.

`no-native-path-realization` formally excludes a map taking every E(p,q) to p=q on this P. More directly, take the family Y(q)=(false=q). It has the starting value refl at false. `no-naive-retained-extension` proves that no function assigning Y(q) to every E(false,q) exists: applying it to `change0` would produce false=true.

Thus the identity-path universal property cannot be transferred to this structure for arbitrary families over P. The next candidate must equip the family with an E-action and retain the equivariance witnesses of its extension. This is an additional interface requirement, not a reason to discard the original E-arrows or identify their object labels.

## Verification and continuation

Sources: `agda/PathIndexedExtension.agda`, `agda/FixedTetrahedralBoundary.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module FixedTetrahedralBoundary -ReceiptStem fixed-tetrahedral-boundary -NegativeModules FixedBoundaryBadErasure
```

Fresh safe compilation and the intended rejection pass. The existing runner uses `-NoNewWindow`, fresh interfaces, and stable compiler/source/library hashes. Receipt: `results/fixed-tetrahedral-boundary-formal-audit.json`. Source-bound audit: `checkers/check_fixed_tetrahedral_boundary.py`.

Next executable test: construct the universal property of equivariant extensions for the original retained E-structure, beginning with set-valued actions. Test the regular action E(p,-) against the realized comparison action K(p,-), so hidden changes remain distinguishable without forcing j to be faithful. Do not identify these arrows with native P-paths.

The fixed-boundary higher-dimensional counterexample remains a separate open test; a sphere/HIT model is available as a construction route. The full five-vertex four-simplex and repeated forward-rotation coherence are also open. No fourth-grade terminality or global retained-graph universal property is asserted.
