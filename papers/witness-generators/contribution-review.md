# Contribution review: bounded literature comparison

Date: 2026-10-06. Internal review of `main.md`, not independent peer review or a literature-wide priority finding.

## Verdict

The current evidence supports a **candidate formalization/integration or expository contribution**, not an established new general mathematical construction principle or proof-search method. The strongest candidate contribution is a type-valued witnessed-step refinement API with selected transitions, source retention and explicit canonical coherence. Its value relative to existing libraries still needs demonstration.

The existing draft is appropriately cautious about universality and the Wolfram converse, but must make the direct dependent-sum precedent more explicit. Full-step preservation and proof dependence are not, on their own, distinctions from displayed constructions. No submission-ready novelty claim is supported by this review.

## Search scope

Used `pnpm pdf:search` and refreshed its stale index with `pnpm pdf:reindex`. The rebuilt top-level `references/` corpus contains 45 PDFs and 4,691 pages. Searches covered displayed categories, dependent type theory, proof relevance, Curry–Howard, logical frameworks, proof assistants and constructor theory. Most indexed downloads concern geometry, physics and analysis; a HoTT reference in Gálvez-Carrillo–Kock–Tonks is not a direct source for the WG theorem.

The index does not cover all PDFs elsewhere in the repository. A filesystem inventory located Voevodsky's existing paper at `research/aspect/references/voevodsky-experimental-library-univalent-foundations-arxiv-1401.0053.pdf`. Two missing close primary sources were downloaded for this review: Ahrens–Lumsdaine and Wadler. Their PDFs, UTF-8 text extractions and source hashes are under `papers/witness-generators/references/`. The Voevodsky original was reused rather than downloaded again. Only relevant passages were read; no claim of reading the entire downloaded corpus is made.

## Primary-source findings

### 1. Dependent pairs already retain witnesses

Vladimir Voevodsky, *An experimental library of formalized Mathematics based on the univalent foundations*, arXiv:1401.0053, PDF pp. 3–4, explains `total2` as both a generic dependent record and the total space of a fibration, its dependent second projection, and dependent functions as sections.

The bare WG type

\[
\prod_s\sum_t R(s,t)
\]

is a standard dependent function returning a dependent pair. It is equivalently a selected successor f together with evidence for every R(s,f(s)). Naming this pattern is permissible, but its witness retention is not a newly discovered logical capability. This source is foundational precedent, not a specific prior implementation of the full WG API.

### 2. Displayed dependent sums already retain proof-dependent second layers

Benedikt Ahrens and Peter LeFanu Lumsdaine, *Displayed Categories*, Logical Methods in Computer Science 15(1), article 20 (2019), DOI 10.23638/LMCS-15(1:20)2019; arXiv:1705.04296.

- Definition 3.1, PDF p. 5: displayed objects over objects and displayed morphisms over particular base morphisms, with dependent identities/composition.
- Definition 3.2, PDF p. 6: total objects and morphisms are dependent pairs; composition is inherited componentwise.
- Definition 3.17, PDF p. 9: for D over C and E over the total of D, form the dependent-sum displayed category. Its morphisms are pairs whose second component is indexed by the first displayed morphism. The total categories have an evident equivalence over C.

This is the direct structural precedent for WG admissions (p,q), witness pairs (r,e,f), and flattening/unflattening. The second layer's dependence on the first witness is already present in the cited definition; it must not be advertised as something displayed constructions erase.

The installed Cubical 0.9 file `Cubical/Categories/Displayed/Constructions/TotalCategory.agda` independently corroborates the implementation baseline: `∫Cᴰ` constructs those dependent object/morphism pairs, and `Assocᴰ`/`Assocᴰ⁻` compare the nested totals. This library inspection is not an exhaustive search for every coherence theorem.

There are actual differences in the local WG interface: the base is a type-valued witnessed graph with a chosen outgoing step, not necessarily a category with hom-sets; refinements preserve that selection and carry explicit source records. The local implementation checks canonical pentagon/triangle behavior on its stated structures. Definition 3.17 alone does not assert every one of these WG-specific statements. These differences are a possible formalization contribution, not a proved priority claim. The paper itself notes that a general displayed bicategory is outside its scope; that observation does not establish that no later work covers the local coherence.

### 3. The map synthesis is ordinary propositions-as-types proof construction

Philip Wadler, *Propositions as Types*, author-hosted expanded online version, section 3, PDF p. 3, describes conjunction as product, implication as function space, and natural-deduction introduction/elimination as construction/use of typed values. The inspected version explicitly identifies itself as the online appendix.

Our search uses exactly this mechanism: pair, project, abstract and apply. The generated Wolfram maps therefore demonstrate type-directed construction in this fragment, not a new kind of proof synthesis. Producing proof terms and checking them separately is not, without further comparison, a WG-specific benefit. Wadler is explanatory precedent for the mechanism, not a performance baseline or a citation for our exact formula.

### 4. Existing combinatorial downloads are contextual, not novelty evidence

`references/1512.07573v4.pdf`, Gálvez-Carrillo, Kock and Tonks, *Decomposition Spaces, Incidence Algebras and Möbius Inversion I*, indexed PDF pp. 1–3 and 10, discusses decomposition structures, simplicial groupoids and HoTT background. It does not establish either priority or novelty of our selected-step/refinement interface. Matching words such as composition, retained structure or coherence is not a theorem-level comparison. The geometric/associahedral downloads likewise do not replace the closer displayed-category comparison.

## Claim-by-claim disposition

| Proposed contribution | Review disposition |
| --- | --- |
| WG signature returning value and witness | Standard dependent programming pattern; definition/terminology, not novelty by itself |
| Compilation of a supplied computation | Adapter implementation; cannot be described as independent synthesis |
| Proof-sensitive dependent refinement | Standard displayed-data principle with selected-step/type-valued specialization |
| Closed indexed composite and full-step flattening | Direct dependent-sum precedent; document local executable and source-retention details |
| Canonical units, associator, pentagon and triangle | Concrete checked artifact; comparative novelty not yet established |
| Explicit retained sources and per-rule traces | Potential API contribution; an ordinary proof AST also retains derivations, so a matched baseline is required |
| Constructive Wolfram double-negation equivalence | Useful exposition and fixture; no priority finding on the exact lemma |
| Automatic generation of the two maps | Standard fragment inhabitation; proof-producing demonstration, not a new algorithm |
| Fewer proof nodes than the published converse | Inadmissible comparison: different premises, target and size metric |
| Universal-constructor candidate | Motivation only; no qualifying repertoire theorem established |

## Honest contribution statement to use now

“We formalize a selected-step, proof-relevant refinement interface and its canonical composition/coherence in Cubical Agda, making its displayed-totalization interpretation explicit. A constructive Boolean example illustrates independently searched certificates assembled and retained through that interface.”

Follow this immediately with the fact that the Boolean example currently exercises the basic rule compiler, not the stronger refinement composer. Do not let “through that interface” imply an application of every theorem in the framework.

## What would strengthen the paper without changing its mathematical scope?

The cheapest discriminating comparison is **a matched implementation using ordinary typed proof trees and the installed displayed-total machinery**. Hold fixed the inputs, semantic obligations and provenance fields. Compare which adaptation code, preservation lemmas and proof-dependent checks the WG API removes or centralizes. Use the existing proof-dependent erasure fixture to verify the contract, but do not pretend a baseline retaining the same evidence would necessarily fail it.

A demonstrated reduction in repeated proof obligations or a reusable API across distinct examples could support an engineering/formalization contribution. If the baseline is equally clear and small, frame the work as an expository artifact rather than claim an abstraction breakthrough. No runtime speedup or lower proof complexity is predicted by this review.

## Remaining literature gaps

This is not a comprehensive review of refinement calculi, logical relations, proof-carrying code, certifying algorithms, indexed containers, ornaments, displayed bicategories, or later displayed-category formalizations. These topics may contain closer API precedents. Their absence from the local PDF corpus is not evidence of novelty. Exact priority of the short Wolfram constructive lemma is also unreviewed.

Follow-up: `matched-comparison.md` now implements the proof-dependent fixture both with independent ordinary dependent pairs and with the WG composer. Fresh checking establishes definitionally equal data/maps and identical invalid-witness rejection. WG reuses generic structural proofs; the baseline's corresponding laws are reflexivity proofs. The subsequent reuse-against-reuse comparison factors the baseline through Cubical's dependent-sum associator/congruence and a 14-line generic helper. All unchanged tests still pass by reflexivity; no hand-written inverse proofs remain. WG's residual benefit is refinement assembly and preservation-certificate packaging, not a demonstrated nontrivial proof advantage. The bounded disposition is expository formalization.

The contribution-review gate is therefore **partially completed: closest structural precedents and one matched fixture verified, originality unresolved**. Bibliography verification for the rest of the manuscript, independent theorem review and clean artifact evaluation remain open. No mathematical code was changed or recompiled during this review.
