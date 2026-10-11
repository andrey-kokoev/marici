# Candidate central theorem for an introductory WG paper

Actor: marici.Voevodsky. Date: 2026-10-06. This corrects the earlier audit's omission of closed indexed refinement composition. It does not replace the publication scope in ledger 4308 with a universality claim.

## Recovered theorem

Let L be a total witnessed generator. A refinement F of L supplies:

- retained source data;
- an admission type at each state;
- advancement of admissions along L's chosen step;
- an extra witness type over each individual base edge and admitted endpoints;
- a certificate of that extra type for the chosen generated edge.

`ComposableWitnessSpecialization.agda` implements the closed indexed operation

\[
\operatorname{compose}:
\prod_{F:\operatorname{Refinement}(L)}
\operatorname{Refinement}(\operatorname{compile}(F))
\to\operatorname{Refinement}(L).
\]

The composite is computed, not supplied. If the first admission is p and the second q, its admission is the dependent pair (p,q). For base witness r, the composite extra witness is (e,f), where f may depend on r and e. Thus this construction retains proof dependencies, not merely endpoints.

The implementation constructs an isomorphism of states and of every full endpoint-and-witness step package between nested compilation and compilation of the composite. It proves endpoint compatibility and agreement of the selected generated steps. Source data are retained. `Composer.solve` returns the composite and its realization certificate; `Composer.WG` itself is a generator of this composite generator specification.

Behavioral left/right units and an associator are constructed. `CoherentWitnessSpecialization.agda` proves the actual-operation pentagon and triangle on states, full steps, sources and selected steps. The second operand must be a refinement of the compiled first; compatibility of unrelated domains is not inferred. Each leaf's advancement and generated-edge certificate remain supplied.

This is stronger than a request/response wrapper and stronger than rebracketing a single fixed record. It is narrower than constructing all known generators.

## Mathematical precedent and defensible contribution

`DisplayedWitnessSpecialization.agda` identifies compilation with displayed-graph totalization and composition with dependent sums of displayed data. These identifications are definitional. With additional hom-set hypotheses, it connects the history construction to Cubical's displayed-category library. Its counterexample proves that chosen-step lifting alone does not imply arbitrary-edge lifting or a fibration.

Accordingly, dependent-sum composition is not a new mathematical discovery. A defensible formalization contribution is the specific proof-sensitive construction API, retained source records, actual-operation coherence, and checked agreement of generated steps. Whether that package improves existing tools requires comparison; this audit does not establish priority or novelty against the displayed-category literature.

## Does the Wolfram constructor arise from this theorem?

Not yet in the current code.

The actual dependency route is:

1. Python type-directed search selects a natural-deduction proof tree.
2. `GeneratedWolframConstruction` emits that tree as an indexed `Proof`.
3. `RefutationConstructionWG` compiles individual inference frames with `DomainWitnessCompiler` and recursively assembles the tree.
4. `WolframConstructedEquivalence` interprets the assembled proofs and packages their maps into an equivalence.

None of these modules invokes `compose`, `Composer.solve`, the refinement associator or its coherence theorem. Recursive assembly of a proof tree is not the same operation as stacking admission/witness refinements over a common state machine. The former also changes logical contexts under abstraction; that context extension cannot silently be identified with the latter's state admission fibers.

Thus the two current results share a WG interface, but the Wolfram experiment is not evidence exercising the stronger composer theorem. It would be misleading to present it as that theorem's application.

## A noncosmetic connection to test

A meaningful specialization experiment must begin with one proof-construction step machine, then supply two independently motivated refinements, such as semantic validity and source-sensitive dependency retention. The second must use an actual witness of the first; deleting that witness while keeping endpoint values should make a concrete certification obligation fail. Compose the refinements using `Composer.solve` and prove that the resulting generated step agrees with the independently written combined construction on complete step packages.

The test must compare both implementations on the generated Wolfram derivations and at least one other derivation family. Report which code and obligations the generic composer eliminates. Merely attaching an always-true predicate or equality-to-the-supplied-answer seal would not support the claimed benefit. This is a proposed discriminating experiment, not an implemented theorem.

## Publication disposition

Use the precise closed-refinement theorem as the candidate structural centerpiece, explicitly relating it to displayed structures. Keep the constructive Wolfram explanation as the motivating proof-producing example, while marking its current relation to that centerpiece as unestablished. Do not label their coexistence a universal-constructor proof.

The next missing result is a nontrivial instance and comparison, not another general rebracketing theorem. If that instance adds no explanatory or engineering advantage, narrow the draft to the checked construction framework and avoid claiming the Wolfram example validates its distinctive mechanism.

## Verification

Fresh headless checks of `ComposableWitnessSpecialization`, `CoherentWitnessSpecialization`, and `DisplayedWitnessSpecialization` all exited 0 with `--ignore-interfaces --safe --cubical --guardedness --transliterate`, Cubical 0.9, and the Agda/yoneda/native-application/application-extension include directories. Logs: `research/voevodsky/results/wg-ucc-audit/` under the corresponding module names. Existing imported warnings remain. No source changes were made to those modules.

Prior explanations: `research/nima/composable-witness-specialization.md`, `coherent-witness-specialization.md`, and `displayed-witness-specialization.md`. Active obligations are forward realization and route/coherencer compatibility; this audit adds no coherence cell. No all-generator coverage, physical universality, or proof-search completeness was verified.
