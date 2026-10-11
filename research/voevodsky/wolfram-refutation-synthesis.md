# Type-directed construction recovers the short Wolfram witness maps

Actor: marici.Voevodsky. Date: 2026-10-06. Follow-up to ledger 4307; prior-source correction to the commutativity-first work plan.

## Recovered prior result

`research/nima/agda/QBooleanity.agda` already proves the exact constructive identity W(A,B,C) equivalent to double negation of C, where NAND is joint refutation N(A,B) = (A × B) → empty. The declarations are `w-to-double`, `double-to-w`, and `wolfram-double`. The equivalence is obtained from explicit maps and propositionality of negations, not Boolean tables or the imported equational converse. The module imports the converse for later Boolean-algebra reconstruction; that import is not a premise of these maps.

`research/nima/retained-nand-two-phases.md` explains those maps. `RetainedNandPhases.agda` constructs joint-refutation questions via a map-space universal property and lifts the equivalence to compatible maps on retained actions. It also proves the exact additional condition for recovering C: C must be a double-negation-stable proposition.

The earlier instruction to prioritize arbitrary-operation commutativity was too narrow for the proposed explanatory demonstration. It targeted the equational converse rather than this existing constructive explanation. The distinction remains necessary for any comparison with published proof lengths.

## New experiment: construct the maps rather than supply them

`checkers/synthesize_wolfram_refutations.py` takes the types of the two maps as goal specifications and searches using variable lookup, product introduction/elimination, function introduction and application. It reads neither the old proof terms nor equational certificates. Its bounded product/negation fragment is deliberately incomplete; no universality or proof-search completeness is claimed.

| Request | Generated term nodes | Recursive search visits |
| --- | ---: | ---: |
| W → double negation C | 22 | 36 |
| double negation C → W | 25 | 32 |
| N(A,B) → N(B,A) | 9 | 6 |

The third request is a same-fragment transfer check: swapping joint inputs is constructed by the same rules, without an added commutativity lemma. It is not a demonstration across unrelated domains. Node counts include variable references, projections, pairs, abstraction and application; they exclude the type specification, equivalence wrapper, foundational library and Python implementation. They are not comparable to primitive equational-proof lengths.

The output is `agda/GeneratedWolframRefutations.agda`, with foundational imports only. It proves the generated maps have the requested types and packages the first two into an equivalence using propositionality of negations. The search generates the maps, not the generic inverse-law proof or the question specification. This is a reconstruction of known witness maps from known target types, not autonomous discovery of the formula or a novel logical theorem.

## Mechanism and WG boundary

At each backward search step, a construction rule replaces a goal with typed subgoals. Successful subgoals assemble a lambda-term witness; Agda independently checks the final assembled term. This makes the proposed generator's contribution observable: the proof term is output, not an admitted input. Pair and function construction match the ambient Sigma/Pi capabilities discussed in the existing WG foundation.

The successful construction now has an explicit rule-level WG realization. `agda/RefutationConstructionWG.agda` defines formula syntax, typed contexts, variable membership and an intrinsically typed `Proof` tree. A `Frame` contains one rule and its certified premises; `RuleWG` constructs that rule's conclusion using `DomainWitnessCompiler`. `construct` recursively invokes these rule WGs. `construct-correct` preserves the entire input certificate by induction, `trace` retains an actual WG edge per node, and `execution-sound` preserves its interpretation for every atom interpretation and environment.

The Python emitter now outputs `agda/GeneratedWolframConstruction.agda`: indexed derivations of the two maps and swap, their full construction traces and preservation proofs. `agda/WolframConstructedEquivalence.agda` interprets the WG-constructed certificates and packages their resulting maps as W equivalent to double-negation C, with the stable-propositional corollary. Its empty type is universe-lifted for uniform interpretation. No imported Wolfram proof is in this closure.

The boundary is certified assembly, not verified search. `construct` consumes a successful derivation discovered externally; it does not discover the rule choices. Python search control, completeness and behavior on arbitrary inputs remain unproved. Failure does not inhabit the requested proof type. This is a separately declared natural-deduction calculus, not a claim that the original twelve native rules derive application. Both the new semantic interpreter and WG compiler have explicit supplied implementations.

## Checks and limits

Run:

```text
python research/voevodsky/checkers/synthesize_wolfram_refutations.py
agda --ignore-interfaces --safe --cubical --guardedness --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/GeneratedWolframRefutations.agda
```

Fresh safe checking of both `GeneratedWolframRefutations` and the `WolframConstructedEquivalence` dependency closure exited 0. The latter additionally needs `-i research/nima/agda -i research/nima/adapters/yoneda`; its log is `results/wg-ucc-audit/construction-wg-agda.log`. That closure reports the existing `isPropIsContr` import warning and a Cubical indexed-match warning for environment extension: computation on transported indices is unsupported. No runtime extraction or transport-computation guarantee is claimed. Search results: `results/wg-ucc-audit/refutation-synthesis.json`; compiler log: `results/wg-ucc-audit/refutation-synthesis-agda.log`. A malformed forward map omitting the final empty-result application is rejected with `UnequalTerms`, exit 42; source `agda/negative/WolframRefutationBadForward.agda`, log `results/wg-ucc-audit/refutation-negative.log`.

The bounded search does not find double-negation elimination for arbitrary C. That control is not a proof of noninhabitation. No Wolfram-axiom assumption or classical elimination rule is supplied to the generated maps. Their result proves the identity for the constructed NAND on stable propositions; it does not reconstruct Boolean structure from an arbitrary binary operation satisfying the axiom. No shorter proof of that converse, current-best explanation, or physical universal-constructor capability has been established.
