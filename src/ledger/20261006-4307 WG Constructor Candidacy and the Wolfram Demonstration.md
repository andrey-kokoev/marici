---
author: marici.Voevodsky
---

# 4307 — WG Constructor Candidacy and the Wolfram Demonstration

## Publication objective

Introduce Witness Generator (WG) as a universal-constructor candidate, supported by a structural account of generator construction and a recognizable demonstration: a materially simpler derivation or explanation of Wolfram's single Boolean axiom's sufficiency. The demonstration is intended to communicate WG's capability to an audience already aware of the problem, not to prove universality by one example.

Deutsch's *Constructor Theory*, [arXiv:1210.7439](https://arxiv.org/abs/1210.7439), sections 3.7–3.8, defines universality through the repertoire of programmable constructors, including construction of specialized constructors. Section 3.15 considers messages enabling another intelligent system to carry out tasks repeatedly. “Candidate” is our research qualification; no formal Deutsch/Marletto UCC predicate has been established here.

## Generator audit

The existing Agda work supports several distinct statements:

- `DomainWitnessCompiler` constructs a witnessed request/response machine from a supplied dependent computation.
- `MetaWitnessGenerator` constructs a specialized generator from a supplied base generator, domain, agreement, closure and law evidence.
- `WholePackageUniversalProperty` proves least rule-closed interpretation, evaluator uniqueness and fusion for the declared rule signature. It does not synthesize every external generator.
- Entry 4303 establishes that compatible specialization preserves full finite histories and infinite witnessed execution, not merely readouts.
- The native bridge uses a separately added application rule; retaining a function family alone does not derive all its outputs in the original rule system.

The bounded audit did not locate a theorem covering a defined class of “all known generators.” The next breadth obligation is to name that class and construct its members without supplying the requested generator as a seed. The generator-work owner has been asked whether a stronger intended theorem was missed.

## Why Wolfram, and what would count

Wolfram's [2018 explanation article](https://writings.stephenwolfram.com/2018/11/logic-explainability-and-the-future-of-understanding/) distinguishes checking a computer-generated proof from understanding why the result holds. [NKS p. 810](https://www.wolframscience.com/nks/p810--implications-for-mathematics-and-its-foundations/) identifies the target as recovering the Sheffer axioms from the single identity. This is the relevant comparison, not evaluating an expression already interpreted as Boolean NAND.

The present converse replays published McCune–Veroff–Fitelson–Harris–Feist–Wos certificates: 92 and 67 positive equations, including starting equations, with an explicit bridge. It is checked prior-proof reuse. The existing synthesis-completion packet reports minimum formula cost six and a kernel inhabitant of `Goal.Result`, but reuses adequacy; independent adequacy search remains open. Formula size and derivation size are different objectives.

A winning demonstration must fix the same premises and target as its comparator, generate a derivation through WG without importing that derivation, and expose all theorem-specific helper dependencies. Before claiming improvement, normalize comparable certificates and freeze a primary proof-size measure; report intermediate term size, search resources, supplied guidance and explanatory structure separately. A second construction through the same mechanism should test whether the method transfers beyond this example.

## Scope

This entry records an audit and prospective success criteria, not a simpler proof, autonomous discovery, a literature-wide shortest-proof result, universal physical construction, or guaranteed audience uptake. The belief that many unsuccessful simplification attempts exist has not been verified. The six-call compositional executor is correctness infrastructure, not the advertised proof-of-concept achievement.

## Durable verification

- Audit packet: `research/voevodsky/wg-ucc-wolfram-publication-audit.md`.
- Fresh safe Cubical Agda checks with `--ignore-interfaces` exited 0 for `MetaWitnessGenerator`, `WholePackageUniversalProperty`, `CompositionalWitnessCompiler` and `BooleanNandEquivalence`; logs and retrieved public sources are in `research/voevodsky/results/wg-ucc-audit/`.
- Existing `isPropIsContr` import warnings remain. The minimum-certificate and infinite-trace roots were source-audited, not freshly rechecked in this audit.
- SCC classification: forward realization and route/coherencer compatibility; existing `nima-wolfram-converse` model inspected, no new coherence theorem claimed.
- Sequence claim: `seqclaim-4fec04120fb23a4148572df0`, allocating 4307.
- Graph report to `marici.Nima`: `ev-000000015796-bca8dc1e-989c-4d0f-b544-6758dc48b8f9`; proposal `ep_6d51a87b-200b-4a4f-86d4-b5dc74a3eb41`. Admission records communication, not scientific truth.
- `pnpm run build` exited 0; VitePress and Pagefind completed. Log: `research/voevodsky/results/wg-ucc-audit/website-build.log`. No deployment or Git checkpoint claimed.
