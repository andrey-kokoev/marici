# WG constructor candidacy and the Wolfram demonstration: publication audit

Actor: marici.Voevodsky. Date: 2026-10-06. Operator-directed audit; publication objective, not a universality result.

## Objective

Introduce Witness Generator (WG) as a universal-constructor candidate and communicate its constructive capability through an independently recognizable demonstration. Wolfram's single Boolean axiom is the leading demonstration because its compact statement and publicly discussed proof complexity offer a legible comparison. The goal is a materially simpler derivation or explanation generated through WG, not merely correct execution of the expression or replay of an imported proof.

The breadth argument and the demonstration must use the same construction mechanism. The audience's recognition is a communication objective, not a consequence of an Agda type inhabitant. A finite example can support candidacy without establishing universality.

## Definition and scope

Deutsch, *Constructor Theory*, arXiv:1210.7439, sections 3.7–3.8, defines a universal constructor by a repertoire equal to the union of repertoires of all possible programmable constructors. Programming overhead is task-dependent but independent of subsequent inputs and repetition count. Construction of specialized constructors is central. Section 3.15 discusses messages that enable another system to perform tasks repeatedly, while distinguishing intelligence from reliable programmability.

This audit does not establish a Deutsch/Marletto definition of the phrase Universal Constructor Candidate. UCC is our research qualification. A proof-producing software calculus does not thereby acquire universal physical construction capabilities. Substrates, resources, task class and reuse must be specified before proposing such a bridge.

## Existing generator results: inputs versus constructed outputs

| Source | Supplied inputs | Constructed result | Boundary |
| --- | --- | --- | --- |
| `research/nima/agda/TypedGeneratorLayers.agda` | State, relation, total witnessed step | Layer 1 interface and retained histories | A signature is not a synthesis procedure; `no-universal-composition` refutes automatic composition for arbitrary Layer 1 relations |
| `research/nima/agda/DomainWitnessCompiler.agda` | Dependent `compute`; domain laws when requested | Request/response WG, beta witness and retained request | Executes supplied computation, not discovery of it |
| `research/nima/agda/MetaWitnessGenerator.agda` | Domain, base WG, agreement, admission closure, law | Specialized WG and a universe-raised meta-WG; law extracted from actual step | Relative specialization, not construction of arbitrary generators from specifications |
| `research/nima/agda/WholePackageUniversalProperty.agda` | Seeds and an interpretation of each declared rule | `least-closed`, evaluator uniqueness, fusion, preservation of supplied higher paths | Universal property of the declared rule closure, not completeness for all external generator mechanisms |
| `research/nima/meta-witness-native-bridge.md` and `agda/MetaWitnessNativeBridge.agda` | Certified function and argument, separately added application rule | Native derivation of the computed result retaining provenance | Original twelve-rule closure does not gain application merely by storing a Pi family |
| Ledger 4303; `WitnessedHistories.agda`, `InfiniteWitnessedExecutions.agda` | Compatible specialization chain and its full witnesses | Flattening preserves finite histories and infinite witnessed execution | Does not supply arbitrary compatibility, arbitrary domain composition, progress or termination |
| `research/nima/agda/CompositionalWitnessCompiler.agda` | Binary operation, environment and expression syntax | Execution tree with one WG witness per node; soundness for every certificate; exact node count | A dependency tree, not a sequential history on the binary WG's state space |

The bounded search inspected generator, whole-package, specialization, native-application and synthesis sources and their packets. It did not locate a theorem quantifying over a defined class of all known generators. This is not a claim that no additional relevant file exists. The strongest identified general result is rule-relative interpretation plus compatible execution-preserving specialization. A publication claim of repertoire coverage needs an explicit target class and a construction for each member without seeding the requested output or generator.

Active SCC obligations are forward realization and route/coherencer compatibility for existing interpretation/specialization comparisons. This audit adds no coherence cell. Existing model `nima-wolfram-converse` was inspected with `scc.py explain`; SCC describes obligations, not truth or publication authority.

## Wolfram benchmark and provenance

The displayed identity is

\[
((a\mid b)\mid c)\mid\bigl(a\mid((a\mid c)\mid a)\bigr)=c.
\]

The nontrivial public benchmark is reconstruction of Boolean algebra from this single law on a nonempty set, not checking its truth for an already Boolean NAND operation. Wolfram's *A New Kind of Science*, p. 810, labels its proof as reproduction of the Sheffer axioms. His 2018 article *Logic, Explainability and the Future of Understanding* says the proof could then be generated in under a minute, but asks why the result is true and what its explanation is. Thus mere automation or checking is not the proposed distinction.

Sources retrieved during this audit:

- https://www.wolframscience.com/nks/p810--implications-for-mathematics-and-its-foundations/
- https://writings.stephenwolfram.com/2018/11/logic-explainability-and-the-future-of-understanding/
- https://mathworld.wolfram.com/WolframAxiom.html
- https://www.cs.unm.edu/~mccune/papers/basax/

Local provenance is explicit in `research/nima/wolfram-nand-equivalence.md`: `build_wolfram_converse.py` replays 92 and 67 positive equations, including initial equations, from preserved `Sh-2.proof` and `Sh-1.proof`. The reference is McCune, Veroff, Fitelson, Harris, Feist and Wos, *Short Single Axioms for Boolean Algebra*, JAR 29 (2002), 1–16. The reversed stroke and bridge between certificates are recorded. These counts are not a normalized primitive proof-length score and must not be advertised as one. This replay is prior-proof reuse, not independent WG discovery.

`research/nima/algebra-synthesis-completion.md` reports that `SynthesisCertifiedMinimum.agda` inhabits the original `Goal.Result`, with minimum cost six operations in the declared grammar and reused adequacy. Its fresh search run derives 89 new consequences plus the input axiom, but none of its four basis goals. This historical result was source-audited here, not rerun. The open gate is fresh adequacy and its verified connection to the generator runtime. Formula length, proof length, search cost and explanatory simplicity are distinct measures.

`CompositionalWitnessCompiler` proves six binary calls and conditional output c. Neither six calls nor its small correctness proof competes with the algebraic reconstruction derivation: they solve different problems.

## Prospective success contract

Before running a candidate, freeze:

1. Exact input axiom, target Boolean or Sheffer basis, inference calculus, allowed definitions and admissible library lemmas.
2. Published comparator artifact and reproducible normalization to that calculus; do not assume the current replay is the best known proof.
3. Primary score: primitive inference DAG size with dependency accounting. Report maximum intermediate expression size, search time/resources and supplied proof guidance separately. Charge theorem-specific helper proofs rather than hiding them behind an API.
4. For an explanatory claim, provide a compact lemma-level account and disclose its elaborated certificate size. Human explanatory quality is not established by a line count alone.
5. WG provenance: generate the certificate without importing its proof or a theorem-specific answer; log all seeds, strategy and oracle calls. Verify the result independently and reject a mutated certificate.
6. A second, non-Wolfram construction through the same mechanism as a transfer test, with domain-specific additions disclosed.

No quantitative win threshold is claimed yet; freeze it after identifying comparable baseline artifacts. A proof from stronger Boolean premises, a truth-table check, renaming old lemmas, and a short wrapper around the imported converse are negative controls, not wins.

## Follow-up correction: stronger composition result recovered

The initial audit omitted `ComposableWitnessSpecialization.agda`, `CoherentWitnessSpecialization.agda`, and `DisplayedWitnessSpecialization.agda`. They supply closed indexed composition of refinements, correctness on full step packages, actual-operation units/associator/pentagon/triangle, and a displayed-totalization interpretation. All three were subsequently freshly checked with exit 0. This is stronger than the earlier relative-specialization-only account; it still does not establish all-generator synthesis. The current Wolfram proof constructor does not invoke this composer. Exact theorem, standard precedent and missing noncosmetic application: `research/voevodsky/wg-paper-central-theorem.md`.

## Next work

First normalize and score the existing equational certificates and investigate later simplifications of the same theorem. In parallel, ask the generator-work owner whether a stronger repertoire theorem than the audited files was intended. Then declare a generator class and make the proof search/certificate generator an instance of its actual construction theorem. Keep the Wolfram demonstration as the leading benchmark, not as already achieved novelty.

No literature-wide absence claim is established; the belief that many attempts failed to find a simpler derivation remains unverified. No benchmark advantage, autonomous adequacy synthesis, all-generator coverage or universal-constructor theorem is asserted.

## Durable verification

Fresh commands for `MetaWitnessGenerator`, `WholePackageUniversalProperty`, `CompositionalWitnessCompiler`, and `BooleanNandEquivalence` all exited 0:

```text
agda --ignore-interfaces --safe --cubical --guardedness --transliterate -i research/nima/agda -i research/nima/adapters/yoneda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/nima/agda/MODULE.agda
```

Logs and retrieved source pages: `research/voevodsky/results/wg-ucc-audit/`. The existing `isPropIsContr` import warning remains where `TypedGeneratorLayers` is imported. These four checks do not freshly verify the much larger minimum certificate or infinite-trace root. Ledger allocation: 4307, claim `seqclaim-4fec04120fb23a4148572df0`. The ledger entry records graph and website-build results separately.
