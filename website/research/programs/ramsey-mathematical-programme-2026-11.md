# Ramsey mathematical programme: selected November notes

**Editorial snapshot: 2026-11-17.** The source-note dates are November 8–10, 2026; the selected heptagon and neighborhood-stability notes are undated in their text. This is an editorial review of the working tree based on `3ace86e33`, not a scientific execution date or an exhaustive inventory of the programme.

These imported notes are **not independently verified** by this publication. A commit is not proof, source admission or publication approval; no priority or novelty claim is made. Their source-reported written arguments, finite computations and conjectures have different verification boundaries. Scientific checkers, SAT/DRAT proofs and formal compilers were **not rerun** here.

## Evidence map

| Kind | Selected source report | Surviving scope |
|---|---|---|
| Source-reported written results | Matrix extension identities; conditional reflected-return calculation; three-bit rigidity; single-root stability bound. | Each uses its own carrier and hypotheses; none is a universal Ramsey generator. |
| Conditional finite certificates | Selected graph successors and the exact-order parity-closed heptagon classification. | Supplied graph families, encoding and finite certificate trust remain explicit. |
| Counterexamples | Nonuniversal attachment family, nonzero reflected residue, two-bit rigidity failure, and a sharp one-root stability example. | Each excludes a named stronger inference, not every alternative construction. |
| Open claims | General source-selected successor/extremality, unrestricted chirp rigidity, and simultaneous neighborhood stability. | Commitment of the notes or absence of a found counterexample does not close these claims. |

## Matrix generation is not an extremality theorem

The [November 8 matrix-generator position](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/ramsey_matrix_generator_current_position_2026-11-08.md) separates symbolic phase transport, binary incidence reconstruction and Ramsey extremality. An adjacency block must still pass triangle-freeness and the independent-set bound. Its exact extension and enumerative recurrence identities test specified blocks; they do not select the old graph, sector size or attachment seed from a symbolic row.

There is **no general Ramsey formula** or universally complete successor law derived here. The exact enumerative recurrence is not a compressed closed form. The quadratic decoder reconstructs already supplied incidence columns rather than deriving those columns from phase labels alone.

The reported 13-to-17 construction is forced only within its supplied parent, four-cycle symmetry and attachment family. The 17-to-22 continuation first selects a minimum-support compatible pair; the later red $K_{2,3}$ shape is conditional on that choice. Ten of fourteen selected decompositions reach 22 and four stop at 21. The source reports that **two of twenty** sampled extremal 22-vertex graphs have no such attachment decomposition. These constructions give **lower-bound witnesses**, not a universal successor classification or an upper-bound proof.

## Reflected simplices: a boundary is not a filler

The [November 9 reflected-simplex consolidation](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/reflected_simplex_coherence_consolidated_2026-11-09.md) keeps three carriers separate: native retained histories, geometric cell completions and independent-operation route-state complexes.

The six-arrow source has cycles, not supplied filled faces; `BA` is a separate occurrence, not an assumed inverse of `AB`. In the specified reflection-equivariant group-effect model, adding red/blue flatness makes the green residue $a^{-2}$; green flatness additionally requires $a^2=1$. Reflection and reversible composition alone do not impose that condition. The supplied quaternion example has a nonzero central residue; centrality is not automatic in other groups.

A sphere obtained by extra face attachments, or a sphere in an independent-operation order complex, is not thereby a native comparison cell. The missing incidence-to-edge-colouring translation prevents these geometric constructions from explaining a Ramsey threshold. This is a different scope from the [completed certified-input WG assembly](/research/results/source-certified-coherent-assembly); it does not reopen that narrower local objective.

## Minimum-dimension phase rigidity: proved cases versus conjecture

The [November 10 rigidity note](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/minimum_dimension_phase_rigidity_2026-11-10.md) asks whether labelled pairwise squared overlaps, together with minimum real realization dimension, determine the quadratic-chirp Gram configuration up to vertex signs and a common orthogonal transformation.

- **Source-reported proof for n = 3:** the 64-vector, eight-dimensional case uses an exact cycle/triangle-rank certificate and the minimum-rank Gram equation, not a floating-point signing search.
- **Counterexample for n = 2:** the same labelled squared overlaps and dimension can have different cycle holonomy, not removable by vertex-sign gauge.
- **Separate translation-invariant theorem:** the note gives a proof for all $n \ge 2$ under translation invariance, or invariance after sign gauge. Arbitrary feasible realizations need not have that symmetry.
- **The unrestricted n = 4 remains open.** The full 1,024-vector problem requires a positive semidefinite Gram matrix of rank sixteen with all prescribed squared entries. Candidate signs are not arbitrary graph signings. A locally positive changed triangle or a restricted symmetry search does not decide extension to that entire matrix. The conjecture for all $n \ge 3$ needs a further rigidity argument or justified lifting theorem.

These are real Gram/projector statements, not a physical state-preparation or nuclear-geometry identification.

## Heptagon normal form: exact order and all hypotheses matter

The [computer-assisted normal-form note](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/heptagon-normal-form-theorem.md) assumes a simple graph on **exactly 22 vertices** with:

1. no triangle;
2. no independent seven-set;
3. an induced seven-cycle such that every vertex has an even number of neighbours on that cycle.

Under those hypotheses, the source reports that the graph is **6-regular**, has **binary adjacency rank 16**, and belongs to **two isomorphism classes**. The fixed canonical profile has four labelled completions. Its eight-qubit minimum is an algebraic Pauli commutation/anticommutation realization cost, not an experimentally demonstrated quantum register.

The proof pipeline is a mathematical reduction to CNF, source-reported independently checked DRAT refutations, explicit graph/isomorphism witnesses and exact binary-algebra certificates. The final core does not require the 191-graph catalogue or earlier Ramsey-value cuts. This is **not a proof-assistant formalization**: the semantic encoding and symmetry reduction still require mathematical review. Budget exhaustion is UNKNOWN, not UNSAT. Regenerated solver outputs require renewed independent checking.

The exact order and parity-closed heptagon cannot be dropped: the 21-vertex circulant counterexample survives. This is **not the unrestricted Ramsey upper bound**; the heptagon hypothesis is an extra condition, not a consequence established for every Ramsey-admissible graph.

## Neighborhood stability: one root is not every root

The [twenty-three-vertex stability note](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/neighborhood_stability_at_twenty_three.md) concerns finite simple triangle-free six-regular graphs. A root is three-stable when its neighborhood has no improving independent-set exchange supported on at most three of its labels, including rank zero.

The source gives a written proof that **one three-stable root** implies **at most 23** vertices. Its explicit sharp 23-vertex graph has independence number seven: the distinguished root first improves by a rank-four exchange, while another root has a rank-one improvement. It is **not a counterexample to the classical Ramsey value**, because it contains independent seven-sets.

The proposed exclusion of order 23 when **every root** is three-stable is not proved by that example or the single-root bound. The **simultaneous-stability step remains missing** in this particular enumeration-free argument. The note does not claim the known classical Ramsey value itself is unknown.

## Reproduction and publication limits

Follow each linked packet's hypotheses and declared environment, not a generic “all notes verified” command. Existing matrix and heptagon scripts include [the selected 17-to-22 certificate](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/ramsey_17_to_22_successor_certificate.py) and [the heptagon proof verifier](https://github.com/andrey-kokoev/marici/blob/main/research/chatgpt/ramsey/verify_heptagon_proof.py). The heptagon note specifies pinned python-sat, Rust/Cargo and independent-checker invocations. Large generated CNF/DRAT payloads are local replay artifacts, not public downloads promised by this guide.

Some source reproduction references are incomplete in this checkout. The named helpers `check_pairwise_rigidity_base.py`, `check_circulant_reduction.py` and `verify_neighborhood_stability.py` were **not found in the reviewed tree**. The reflected-simplex note also names sibling stage-package paths not present here. These are unresolved reproduction inputs, not evidence that their checks pass or fail; no replacement checker or missing receipt has been invented.

This guide is **not pinned by the historical ten-family v1 snapshot**. [Reviewed successor v2](/research/provenance/current-results) identifies the selected sources, available checker/receipt identities and missing reproduction inputs; source-note presence, historical receipt metadata and independently replayed science must stay distinct.

[Results and verification levels](/research/results/) · [Native Ramsey revision-32 scope](/research/results/ramsey-retained-assembly-coherence) · [Theory](/research/theory/)
