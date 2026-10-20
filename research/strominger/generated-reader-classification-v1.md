# Generated reader images and complete compatible fillers

Owner: `marici.Strominger`. Net node: **`generated-reader-image-classification`**.

- [Net](contracts/wg-source-determination-conjecture-net.v1.json)
- [General theorem](agda/GeneratedReaderClassification.agda)
- [Exact predecessor regression](agda/GeneratedReaderClassificationRegression.agda)
- [Fresh verification](results/generated-reader-classification/verification.json)
- [Dependency manifest](results/generated-reader-classification/dependency-manifest.json)

## Result

For the explicitly generated source-pointed/attachment/comparison fragment:

1. Every interpreted carrier has a reader-preserving equivalence to one of five explicit normal forms.
2. Its reader is an embedding into `Vertex`; its exact image fibers are propositions.
3. For fixed operands and mode, the **complete compatible filler type is equivalent to agreement of their reader images under that mode**.
4. This filler type is a proposition and is contractible when inhabited.
5. Actual native comparison derivations and their dependent compatibility are constructed using the retained operand derivations.

This is an inductive theorem over the fragment, not an inference from a finite list of successful diagrams. It classifies interpreted values and compatible operations. It does not identify all native histories or certify the origin of every constructor parameter.

## Exact fragment and source boundary

`Fragment` has only three constructors:

- `start v d`, where `d : Resolve Seeds (pointQ v)` is an actual supplied derivation and the reader is the identity on Vertex;
- `attachF`, using the existing outgoing-witness attachment;
- `compareF`, using the existing equivalence, selected-point proof and whole-carrier mode/port law.

`body` erases this syntax into the **unchanged** `Body` constructors. `native` uses their unchanged native interpreter. No native seed or rule is added. The source proof is not replaced by `root v` during recursion.

This is a declared sublanguage. It excludes arbitrary `prepared` carriers/readers, generic E-index families, Pi operations outside this interface, and arbitrary next-universe reifications. In particular, it is not a theorem about every `Body` or every native WG derivation.

The fragment still accepts comparison parameters as inputs. Their compatible interpreted action is constrained by the theorem, but their program provenance is not thereby certified. That distinction motivates the next synthesis task.

## Reader-labelled normal forms

| Normal form | Reader image |
|---|---|
| `whole` / Vertex | A, B, C, D |
| `outgoing A` / Out(A) | B, D |
| `outgoing B` / Out(B) | A, C |
| `outgoing C` / Out(C) | A |
| `outgoing D` / Out(D) | B |

These are **five reader-labelled forms**, not five physical states, five unlabelled homotopy types, or a bound on the number of histories.

`normal` computes the form from the constructor tree:

- A source-pointed package normalizes to Vertex.
- An attachment at v normalizes to Out(v): its additional selected-point loop fiber is contractible because the preceding interpreted carrier is a set.
- A comparison graph is equivalent to its target carrier. Its normalization therefore uses the target operand's normal form, with the original graph witness providing the reader square.

The proof reuses the existing graph equivalence and the actual six-arrow outgoing-family retraction/sethood results. It does not assume proof irrelevance of Code, Complete or Resolve.

`image-classification` identifies the actual reader fiber at each vertex with the corresponding normal-form image fiber. This is constructive: the normal forms come from syntax, not from classical selection of an arbitrary subset of a finite set.

## Complete-filler classification

For `a : Fragment v`, `b : Fragment (act m v)`, define a filler as

```text
(e : Carrier(a) ≃ Carrier(b))
× (e(selected(a)) = selected(b))
× ((x : Carrier(a)) -> act(m, reader(a,x)) = reader(b,e(x))).
```

`ImageAgreement` gives both directions of membership transport between the actual reader images at w and `act m w`.

The checked equivalence is:

```text
Comparisons.classification : Filler ≃ ImageAgreement.
```

`images-from-filler` obtains image agreement from the complete map and its port law. Conversely, `filler-from-images` constructs forward/backward maps from the image witnesses. Reader injectivity proves their inverse laws and selected-point compatibility.

`filler-prop` compares **full equivalences and both witness fields**, not just displayed ports. It uses proved reader injectivity and sethood at this boundary. Thus an inhabited filler fiber is contractible. It is not unconditionally inhabited.

`admitted` compiles each filler through the existing comparison rule with both actual native operand derivations. `native-coherence` is a dependent path between these constructed comparison histories. It does not make all proofs inhabiting an arbitrary Resolve index equal.

## Exact reuse of an existing diagram

The regression reconstructs the actual source and target Bodies of `RepeatedInterchangeCoherence` by the fragment constructors, with definitional recovery. The general `filler-prop` then compares its old sequential/direct fillers.

`old-witness-recovered` proves equality with the **previously constructed higher witness itself**, not merely existence of another comparison. Rebuilding a filler through image agreement also recovers the complete original filler.

This concrete regression concerns the existing **one-comparison/two-attachment** diagram. The structural theorem is general, but this run does not claim a new forward/forward binding of the separate two-comparison Body diagram. An attempted additional concrete specialization encountered expensive elaboration and was not retained as a verified regression; this is not a mathematical obstruction.

The earlier framed-presentation and normalization notes motivated the compatible-fiber interface. Their broader theorems are not imported wholesale: the actual source frames and classification above are independently checked against this fragment. No new normalization-rule schemas are introduced.

## Two proved boundaries

### Selected-point agreement does not imply existence

A source-pointed package at A has image `{A,B,C,D}`. An attachment along `CA` also selects A but has image `{A}`. `same-point-no-filler` proves that no stay-mode complete compatible filler exists between them.

Uniqueness of possible fillers does not manufacture one when the image condition fails.

### Arbitrary prepared readers are outside the theorem

Using the very same admitted package `pointQ A` and its native seed derivation, `prepared` can attach a constant reader returning A for every value. `hidden-not-injective` proves that this reader is not injective.

Thus the unrestricted-Body claim is false even without new native seeds or hidden Boolean indices. The identity-reader base restriction is substantive supplied interface policy, not a consequence of native admission alone. The earlier hidden-Boolean-fiber obstruction remains another boundary example.

## What this does not settle

- Contractibility of compatible filler fibers does not contract their represented carrier, raw syntax, or arbitrary native histories.
- It does not fill `TripleExchangeOverlap`, which concerns chosen paths on retained histories rather than this fixed compatible-map fiber.
- It does not admit a literal atomic higher-path Code or provide universal native higher-rule completeness.
- It does not impose the fragment's parameter discipline on unrestricted native rules.
- Finite-set interpreted carriers do not imply trivial topology of families, classifying spaces, universes, or retained history types.
- It is not a global limitation theorem for WG or a physical state/dimension count.

## Verification

```sh
python research/strominger/checkers/check_generated_reader_classification.py
```

Fresh safe headless closure passes with `--ignore-interfaces` and explicit include roots. Three negative controls fail with `UnequalTerms`: applying the source-reader certificate to the unrestricted constant reader, supplying an identity filler merely from selected-point agreement, and treating normalization as literal raw-package equality.

The receipt records all commands/exits, compiler identity, source hashes and an unchanged conservative **1,828-file** include-root/primitive source inventory. It records dependency indexed-match warnings normally suppressed by Cubical's library configuration; repository sources have none. The inventory is not an exact import graph or a claim that every inventoried file was compiled.

A separate finite control checks all 50 shape/mode pairs and enumerates their port-compatible bijections. This supports the finite image table; the unbounded result is the Agda induction and classification theorem.

## Next highest-leverage task

**`canonical-comparison-synthesis`: produce or reject a comparison from generated operands and a mode, without accepting an arbitrary equivalence or ImageAgreement function as an input.**

Use the computed five normal forms and their finite incidence/action table to construct the image agreement or its obstruction, then invoke `filler-from-images` and `admitted`. Keep the source proofs and raw histories as declared retained inputs.

This is narrower than certifying every native parameter program, but it would remove the caller-supplied comparison parameters from this classified adapter. Do not claim that generating a canonical comparison reconstructs every original raw producer program.
