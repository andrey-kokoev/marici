# New research directions: generating coherence between reflected simplex trees

**Date:** 2026-11-09  
**Status:** Research programme; no new generator theorem asserted.  
**Companion:** `2026-11-09_reflected_simplex_coherence_research_note.md`.

## 1. Problem to solve

**Input.** A finite, typed tree of composable simplices `R`, an involutive reversal/reflection `ρ`, and a source signature `Σ` specifying admissible local extensions, endpoint/boundary occurrences, and comparison operations. Set `B=ρR`.

**Wanted.** An operation that **generates**, instead of choosing afterward, the coherent mixed cells `G` joining `R` and `B`:

\[
\Gamma_\Sigma(R,\rho R)\;\leadsto\;(G,\text{attachment histories},\text{coherence witnesses}).
\]

At a chain level, any candidate must solve `∂G=−∂(R+B)`. This admits many solutions and need not yield a manifold. A more faithful formulation retains a typed boundary witness and its fiber:

\[
\operatorname{Fill}_\Sigma(\beta)
  := \operatorname{hofib}_{\beta}(\partial_\Sigma),
\qquad \beta= -\partial(R+\rho R).
\]

Here `∂_Σ` is a **to-be-defined typed boundary operator** in the source's chosen category; `hofib` is a candidate homotopy-theoretic formulation, not a derived Marici identity. The research question is whether the native local rules construct an inhabitant, a contractible space of inhabitants, a nontrivial family, or an obstruction.

**Crucial typing decision:** distinguish endpoints of a directed operation from vertices of a geometric simplex, and distinguish source-history equality from equality of evaluated geometric positions.

## 2. Candidate frameworks to investigate

| Literature | Mechanism actually supplied | Specific role | Limitation for our question |
|---|---|---|---|
| Dendroidal sets / ∞-operads | Tree-indexed operations; grafting; inner horn fillers | Local branch composition of R, B and candidate G | Existence up to homotopy need not select one filler or a manifold |
| 2-Segal sets/spaces | Compatibility among polygon triangulations and decompositions | Compare different orders of local attachments | May permit nonunique or partial composition; not a geometric reflection law |
| 2-Segal sets from cuts of rooted trees | Canonical simplicial data built from admissible tree cuts | Encode branch exposure and compositional bookkeeping | Does not itself equip a tree with point-reflected endpoint geometry |
| Algebraic Kan complexes | Explicitly designated horn fillers | Track the *choice* and provenance of local completion | Chosen fillers are extra algebraic structure; they are not generally forced |
| Simplicial necklaces | Chains of simplices connecting two marked vertices | Typed two-endpoint paths and mapping spaces | More natural for serial passage than simultaneous branching |
| Directed acyclic fillers in bar constructions | Fillers for some directed acyclic simplex configurations | Test whether weaker-than-Kan local closure suffices | Existence under additional algebraic hypotheses, not universal |

**Primary references (verified):**

- Heuts & Moerdijk, [*Dendroidal Spaces and ∞-Operads*](https://link.springer.com/chapter/10.1007/978-3-031-10447-3_12), 2022; see also Cisinski & Moerdijk, [*Dendroidal sets as models for homotopy operads*](https://doi.org/10.1112/jtopol/jtq039), 2011.
- Dyckerhoff & Kapranov, [*Higher Segal spaces I*](https://arxiv.org/abs/1212.3563), 2012 / subsequent publication.
- Bergner, Borghi, Dey, Gálvez-Carrillo & Hoekstra-Mendoza, [*2-Segal sets from cuts of rooted trees*](https://www.sciencedirect.com/science/article/pii/S0166864125002457), 2025.
- Nikolaus, [*Algebraic models for higher categories*](https://arxiv.org/abs/1003.1342), 2010 / 2011.
- Dugger & Spivak, [*Rigidification of quasi-categories*](https://arxiv.org/abs/0910.0814), 2009 / 2011; necklaces as simplices strung into endpoint-to-endpoint strings.
- Constantin, Perrone, Fritz & Shapiro, [*Partial Evaluations and the Compositional Structure of the Bar Construction*](https://arxiv.org/abs/2009.07302), 2020 preprint / later publication: fillers for directed acyclic configurations for BC monads, not all inner horns.

The best combination to study is **dendroidal branch composition + comparison coherence of 2-Segal decompositions**, with a source-level selection/admission operation that neither theory supplies automatically.

## 3. Proposed generator contract

A constructive rule `Γ_Σ` should declare its *local inputs and outputs*, before checking any global geometry.

**Inputs at one extension:** retained source occurrence, its oriented boundary/ports, neighboring admitted cells and already retained witnesses, reversal metadata, and the local partial history. No global genus, vertex degree, preferred polytope, or desired Ramsey count is supplied.

**Outputs:** one of (i) a specific admissible new mixed simplex with complete witness, (ii) several compatible candidates recorded without silently selecting one, or (iii) a certified obstruction.

**Obligations:**

1. **Admission and provenance.** Every new cell is justified by a permitted `Σ`-operation. Reversibility of its displayed geometry does not automatically confer an inverse source operation. Keep distinct histories distinct unless a comparison witness exists.
2. **Reflection equivariance.** Swapping the two inputs by `ρ` transports the generated output and its witnesses coherently; `ρ` need not fix every green cell individually.
3. **Locality.** The same rule operates at an edge, branch, and critical overlap. No topology-specific parameter may be inserted after seeing the desired answer.
4. **Critical-pair confluence.** Extending independent branches in the orders `ab` and `ba` gives outputs related by a *generated comparison*; where three comparisons overlap, generate the next compatibility witness. Strict equality should not be assumed.
5. **Global closure and links.** Test whether admitted fillers yield `∂K=0` and, separately, whether each simplex link is of the correct spherical/ball type for the claimed dimension. Allow failure and report its local obstruction.
6. **Selection strength.** State whether the theorem is existence, unique strict completion, unique completion up to isomorphism, contractible filler space, or a classified family. These are different assertions.

## 4. First discriminating computation: branch critical pairs

Use the already enumerated four-triangle star `R` and its point-reflected `B` as a fixed **control fixture**, but **do not** allow the known degree-five rule to participate in `Γ_Σ`.

1. Define the smallest typed local filling/transport operations from one pair of adjacent red/blue boundary ports.
2. Generate candidates in two different branch orders. Record all endpoint maps, cell occurrences, and comparison histories.
3. At the first overlap of the two propagated regions, compute the obstruction to identifying them. Try to construct the comparison from the same rules.
4. Enumerate all completed candidates. Check reflection, manifold links, boundary, and whether geometry is selected or remains ambiguous.
5. Run the same generator unchanged on the linear four-triangle disk, and then on the smallest asymmetric branching tree.
6. Extend to 3-dimensional simplex trees only after the 2-dimensional critical-pair type and failure behavior are understood. The intended theorem must **not** presuppose a 2-dimensional ambient domain.

**Strong discriminator:** Does the locally sourced comparison rule force the icosahedral member of the eight combinatorial completions, reject the other seven with explicit local reasons, select a different completion, or certify nonuniqueness? A post hoc degree condition does not count as success.

**Immediate falsifiers:** incompatible completions surviving the same local source rule with no generated comparison; a branch-order-dependent obstruction where confluence was asserted; a non-manifold link in a claimed universal manifold completion; or a required cell that the source rule cannot generate.

## 5. Higher-coherence tests

The first critical square is the comparison of two local orders. The next test is three overlapping extension orders: the comparisons form a higher coherence diagram. If the relevant substitution structure is associative up to a witness, compare its five bracketings and pentagon boundary. Determine whether its filler is constructed or independently stipulated.

This relates directly to existing Marici work, which must be used as *prior source material*, not relabeled as a newly found mechanism:

- [Witnessed reference return and pentagon coherence](https://github.com/andrey-kokoev/marici/blob/main/research/nima/witnessed-reference-return-and-pentagon.md): retained associator and pentagon history, with possible unit-history obstruction.
- [Reversible local generation](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/marici_reversible_local_generation_note.md): distinction between algebraically generated residue and source-admitted next operation.
- [Reflection experiment](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/reflection_experiment_note.md): explicit seams, retained occurrence copies, and dependence on the full simplex lift.

At each dimension, keep the distinction between (a) a geometric equality of evaluated endpoints, (b) a witnessed comparison between retained histories, and (c) an admissible new cell. A quotient of histories may erase the obstruction being sought.

## 6. Separate downstream tests: topology and Ramsey

**Topology:** If `Γ_Σ` yields a closed oriented 2- or 3-manifold, compute cell incidence, links, homology, and a presentation of its fundamental group. To recognize the Poincaré sphere one needs three-dimensional manifold data and the correct nontrivial binary-icosahedral fundamental group, not merely an icosahedral 2-sphere. To recognize `Σ(2,3,7)`, the Seifert invariants likewise must be produced rather than matched numerically.

**Ramsey:** Build an explicit translation `Φ` from the generated R/B/G incidence record to a complete pair-color relation (or prove why such a translation cannot be natural). Show that its admissibility equations encode precisely the absence of an R triangle and a B 7-set under the agreed edge-color convention. Only after that is it meaningful to ask whether `Γ_Σ` determines the `22→23` obstruction of `R(3,7)` or predicts `R(3,k)`.

A generator that reproduces known Ramsey values only after inserting the values, the number 7, a regularity condition, or the topology as inputs is not predictive.

## 7. Theorem ladder and evidence criterion

| Target | Precise success condition | Initial falsifier |
|---|---|---|
| T0: well-typed boundary | Ports, reversal, cell attachments and history records are defined | Ambiguous endpoint type; inadmissible inverse |
| T1: local generator | One source rule constructs or rejects the next G cell | Unexplained choices at the first two cells |
| T2: reflected branching confluence | Different branch orders admit generated coherent comparison | Surviving incompatible critical pair |
| T3: global structure | Admitted completed cases pass `∂=0` and link tests | Non-manifold link or unresolved boundary |
| T4: selection | In a stated input class, classify the admissible G space without fitted balance | Multiple inequivalent survivors to a claimed uniqueness theorem |
| T5: Ramsey bridge | Source-level `Φ` enforces the exact forbidden pair patterns and explains 22 vs 23 | An output violating the Ramsey condition; need for hardcoded threshold |

**Priority:** T0–T2. They decide whether the proposed source is genuinely generative. T3–T5 are consequences to test after local operations are defined, not premises.

## 8. Output of the next research pass

Produce (i) a short typed signature `Σ` with one concrete local generator, (ii) an exhaustive table of branch critical pairs and their source histories, (iii) exact code for link/boundary tests, (iv) either a construction of the comparison witness or an explicit minimal obstruction, and (v) a written statement of which of T0–T5 actually passed.

This should first be attempted on the four-triangle star, but success must not depend on supplying its known icosahedral answer.
