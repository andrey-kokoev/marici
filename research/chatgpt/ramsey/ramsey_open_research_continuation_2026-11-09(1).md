# Open research continuation — Ramsey generator, retained composition, and the Golay/2048 mechanism

**Date:** 9 November 2026  
**Status:** open research handoff; executable finite starting point, explicit no-go controls, and unproved mechanism-selection hypotheses.  
**Parent note:** [`ramsey_primitive_golay_2048_consolidated_research_note_2026-11-09.md`](ramsey_primitive_golay_2048_consolidated_research_note_2026-11-09.md)

## 1. Objective and non-objectives

**Objective.** Derive, if possible, a *source-generated* composition/coherence law from the original `R/G/0` rotation–reflection primitive which determines Ramsey red/blue incidence, or a rigorous local-to-global obstruction controlling the extremal size of triangle-free graphs with bounded independence number. A genuine Ramsey generator must predict admissible incidence or its impossibility **without inserting known Ramsey numbers, known extremal graphs, a Golay parity-check matrix, or a tuned adjacency decoder**.

The operative Ramsey condition is a graph \(G\) with

\[
K_3\not\subseteq G,\qquad \alpha(G)<k;
\]

\(R(3,k)\) is the smallest vertex count for which no such \(G\) exists. In particular, \(R(3,7)=23\) means that 23 vertices is the *first impossible* size, while a graph on 22 vertices is feasible. A binary code of length 23 does not prove that threshold.

**Do not pursue as an end in itself:** more low-dimensional symmetry orbits, familiar graph identifications, random/asymptotic Ramsey constructions, arbitrary self-referential promotion records, a 2048-cycle obtained by arbitrary splicing, or further code enumeration already verified. None supplies the missing law.

## Immediate research bet — derive the Ramsey threshold, not the representation

**Target theorem.** Construct a uniform, primitive-generated graph-incidence/obstruction mechanism whose first decisive case proves both halves of the \(R(3,7)=23\) threshold:

1. The mechanism generates an admissible graph on **22 vertices**, with no triangles and independence number at most six, *without importing an existing Ramsey graph*.
2. From the **same law**, derive a **universal** obstruction on 23 vertices: every triangle-free graph on 23 vertices has an independent set of size seven. It is not enough that one 23-vertex Golay-derived graph fails.

**Research conjecture (unproved).** A low-level rotation/reflection/comparison rule creates a retained closure defect whose first unavoidable incidence obstruction is the Ramsey threshold. At \(k=7\), the eleven-doubling-phase, 2047-plus-zero structure may model the defect, but its connection to graph constraints must be *derived*. The 2048-cycle is currently a constructed permutation, not the sought obstruction.

**First concrete calculation:** represent the triangle-free extension problem as an exact matrix condition on a prospective red-neighborhood column \(s\): it must be independent in the existing graph, and the enlarged graph must have independence at most six. Try to express failure of simultaneous admissible columns as a closure relation involving the seven-direction quotient and eleven-phase operator. The goal is an **explicit implication**, not matching the numbers 23, 11 or 2048. If no map from incidence matrices to these phase constraints can be derived, the Golay path is not yet a Ramsey explanation.

**Discriminator:** a construction that proves only the 22-vertex lower bound, or only a special 23-vertex failure, is insufficient. An actual threshold theorem requires an existence witness *and* a universal nonexistence proof. Independent checks at \(k=5\) (13/14) and \(k=8\) (27/28) test generality.

**Priority:** Work backward from the graph constraints to locate a simple closure invariant. Study native XOR typing only if that invariant needs it. Do not make source-typing audits or additional Golay verification the main work programme.

## 2. Verified starting point (the minimum facts to carry forward)

### 2.1 Five positions — important control

`RGR00` under the prior affine rotation/translation action yields ten distinct row states, naturally the two-subsets of five positions. The red-pair disjointness decoder *can* produce Petersen, but the decoder is not selected by the primitive. Source-invariant admissible alternatives exist; the tested induced-extension branches are terminal by eleven vertices. This is a control against conflating orbit generation with Ramsey adjacency.

### 2.2 Seven positions — exact binary quotient, conditional reading

Project `RGRGR00` to its **red-support indicator** \(x=(1,0,1,0,1,0,0)\) over \(\mathbb F_2\); this explicitly conflates `G` and `0`. The seven cyclic shifts of \(x\) have rank seven and sum to \(\mathbf1\). With \(q=\mathbf1\), their images in

\[
V=\mathbb F_2^7/\langle q\rangle,\qquad\dim V=6,
\]

form seven distinct columns \(h_i\) with the sole relation \(\sum_i h_i=0\). All sums of at most three distinct columns are different, giving \(\sum_{j=0}^3\binom7j=64=2^6\). This result is exact **after selecting the binary projection and vector-space quotient**.

### 2.3 Golay completion — exact construction, not yet selected

With an explicitly chosen symmetric quadratic comparison structure on \(V\), identify \(V\cong\Lambda^2\mathbb F_2^4\) and append columns

\[
 g_z=(\nu_2(z),1,z),\qquad z\in\mathbb F_2^4,
\]

where \(\nu_2\) consists of the six distinct pairwise products of the four coordinates. The seven old columns \((h_i,0,0)\) and sixteen new ones form a rank-eleven 23-column parity check. Exhaustive checks give all \(2048=\sum_{j=0}^3\binom{23}{j}\) different syndromes; its kernel is the perfect \([23,12,7]\) Golay code. Weight-seven supports give \(S(4,7,23)\), and parity extension gives \(S(5,8,24)\).

**Critical qualification:** neither the \(S_7\)-invariant quadratic comparison refinement nor the complete sixteen-point phase extension has been derived from source-native retained composition.

### 2.4 Eleven phases and a 2047/2048 distinction

The doubling map on nonzero residues modulo 23 has two reflected 11-cycles, giving \(23=1+11+11\). Choose an irreducible degree-eleven factor \(f\) of \(X^{23}+1\) over \(\mathbb F_2\). On \(K=\mathbb F_{2^{11}}\), let \(T(v)=\zeta v\), where \(\zeta\) has order 23, and set

\[
 U(v)=(I+T)v=(1+\zeta)v.
\]

For the checked factor, \(g=1+\zeta\) has multiplicative order \(2047\). Thus \(U\) cycles through every *nonzero* syndrome state and fixes zero. A two-transition nonlinear successor swap,

\[
F(0)=1,\qquad F(g^{-1})=0,\qquad F(v)=gv\quad\text{otherwise},
\]

produces a single 2048-state cycle. **The splice is supplied, is nonunique, and has no demonstrated native retained-history authorization.** Eleven Frobenius-doubling phases are not 2048 time steps. Also distinguish the Golay syndrome space from the complement-quotient of the 24-bit Golay code: both have 2048 elements but are not canonically identified here.

### 2.5 The decisive negative controls

- *Incomplete extension exists.* Appending \((0,1)\) to the seven original syndrome columns inside \(V\oplus\mathbb F_2\) gives an eight-position system with **93 different** at-most-three-mark syndromes among 128 available states. It preserves source retention, unique decoding and full permutation symmetry of the seven old columns. Therefore these properties **do not force perfect saturation or a 16-point jump**.
- *Naive two-copy gluing fails.* Two independent six-dimensional seven-position systems have 470 distinct at-most-three-mark sums. Quotienting their twelve-dimensional direct sum by **any** nonzero one-dimensional subspace creates a collision.
- *Finite symmetry is not a Ramsey decoder.* In the 10-state `RGR00` system, the additional three overlap-class records give 13 objects, but none of the 1024 source-invariant red-edge assignments satisfies both triangle-freeness and independence \(\le4\).
- *Quadratic rigidity is not yet proved.* Thirty restricted higher-degree perturbations of the \(\nu_2\) decoder fail, but those trials do not classify all admissible functions.

## 3. Principal open claim (mechanism first)

> **Source-selection conjecture.** There exists a precise, source-native retained rotation/reflection/comparison constructor \(\mathcal C\), independent of target Ramsey values, such that its admissibility and closure requirements explain a nontrivial jump from the seven-position comparison field. In its binary reading, \(\mathcal C\) must either (a) force a complete three-mark quotient and select the 16-phase quadratic extension, or (b) identify a different mathematically necessary obstruction with a Ramsey readout.

This is **a research conjecture, not a theorem**. Do not assume the first branch is true. The eight-position counterexample requires any proposed saturation rule to provide a *specific* reason for rejecting incomplete extensions. If the rule cannot distinguish them, the forced-Golay hypothesis fails.

There are **three separable selection gaps**, each of which can invalidate the desired chain:

1. **Representation/operation gap:** why does the original ternary `R/G/0` retained-comparison law admit a faithful or justified binary red-support image with **XOR** as the descended composition? What becomes of the distinction between `G` and `0`?
2. **Completion/uniqueness gap:** why should the next admitted record system be *perfectly saturated*, and why should its 16-point decoder be quadratic, rather than one of the permitted incomplete extensions or a different saturated representation?
3. **Ramsey readout gap:** what functor/decoder maps the retained code/comparison incidence into red/blue graph edges or a graph-independent impossibility certificate while preserving triangle/independence conditions?

The 2048-cycle adds a **fourth independent gap**: derive the zero-state splice from source admissibility, if such a splice is relevant at all. Do not treat it as a consequence of Golay perfect packing.

## 4. Supporting work package — binary-composition bridge

This is a supporting test, not the primary goal. Run it when an explicit graph-incidence or closure invariant requires a binary source interpretation.

**Source material to inspect (Marici `andrey-kokoev/marici`):**

- `research/nima/triangle-comparison-feedback-cycles.md`: a supplied comparison feedback law; repeated re-promotion adds history, not independent degrees of freedom.
- `research/nima/recursive-independent-family-comparison.md`: explicit independent Cartesian pairing, with source/target endpoint typing.
- `research/nima/promotion-factor-independence.md`: independent-factor obstruction for mere grouping/copying.
- `research/nima/spectral-record-successor-constructor-search.md`: no inspected constructor directly composes two spectral identity records without an endpoint/operand adapter.
- `research/nima/comparison-successor-operation-contract.md`: retained reference and witnessed/admitted composition require an explicit rule and type.
- `research/nima/record4-spectral-promotion.md`: spectral mode identities retain source history; labeling alone creates no new independent operand.

**Test contract.** Take the *actual* source-typed operations, not a newly invented rule. Define, or prove that one cannot define, a reading \(\Phi\) from retained histories/records into \(V\) satisfying all applicable constraints:

\[
\Phi(\mathcal C(a,b))=\Phi(a)+\Phi(b),\qquad
\Phi(\rho a)=\rho\Phi(a),
\]

with the domain of \(\mathcal C\), reflection \(\rho\), source/target endpoints, and history windows explicitly specified. Check that the operation is well-defined on quotient classes, preserves the actual source admission relation, and does not identify distinguishable `G` and `0` histories except where source equivalence authorizes it. If \(\mathcal C\) is only partially defined, state the quantified law **only on its typed domain**; do not silently extend it to all pairs.

**Minimal counterexample test.** Exhibit two source records with the same binary \(\Phi\)-value but different admissible continuations. If they exist, \(\Phi\) cannot be a sufficient state for the proposed generator. Alternatively, prove the required congruence/admissibility property. This is more informative than matching 64 and 2048 counts.

**Success criterion:** a checked homomorphism or correctly typed partial homomorphism plus a proof that its kernel is stable under every authorized continuation, *or* a concrete source-native counterexample that terminates the XOR hypothesis.

**Stop condition:** if no source-supported \(\mathcal C\) acts on the original `R/G/0` rows in the required way, report that no derivation is presently available. Do not design an XOR operator and later relabel it "source-generated."

## 5. Second work package — make saturation an admission theorem or reject it

Run this only if the first work package establishes a meaningful binary interface.

Formalize the proposed next-state admission predicate \(P(X)\) using only actual source-observable history, ports, endpoints and continuation rules. Evaluate it on **both**:

- the explicitly valid **8-position / 93-of-128** extension, and
- the **23-position / 2048-of-2048** quadratic extension.

If both are admitted, the source does **not** force Golay. If the smaller extension is excluded, identify the exact local-to-global incompatibility that excludes it; prove the rejection without using the target condition \(|\mathrm{Syndromes}|=2^r\). A requirement of perfect saturation is allowed as a separately declared new axiom, but it is then not an explanation derived from the primitive.

**Conditional mathematical rewards only after this gate:** The binary radius-three perfect-packing equation

\[
\sum_{j=0}^3\binom{n}{j}=2^r
\]

has, for \(n\ge7\), the only solutions \((n,r)=(7,6),(23,11)\). Under the additional assumption of *old six-dimensional quotient retention*, the sixteen new columns must project onto an affine hyperplane \(\{(1,z):z\in\mathbb F_2^4\}\) of the five-dimensional new quotient. These are **conditional theorems**; they do not supply the admission predicate.

## 6. Third work package — quadratic selector and obstruction class

If the affine 16-point phase projection is source-forced, classify admissible maps

\[
 f:\mathbb F_2^4\to V,
 \qquad g_z=(f(z),1,z),
\]

with the original seven columns retained, modulo precisely declared affine/gauge equivalences. In the checked quadratic solution, \(f(z)=\nu_2(z)\), and its second derivative is

\[
 D_aD_b f(z)=a\wedge b
\]

independent of \(z\). For general admissible maps the second derivatives on the 140 affine 2-planes must obey the source's nonzero-singular constraint; that condition by itself is weaker than being exactly a fixed exterior product. Establish full rigidity, give an inequivalent admissible counterexample, or describe the moduli without asserting uniqueness.

A useful split: (i) prove the invariant form \(B,Q\) from a *justified* enlarged symmetry group (do not infer \(S_7\) from cyclic/reflection generators); (ii) prove the quadratic law independently of having chosen an isometry \(V\cong\Lambda^2\mathbb F_2^4\); (iii) test whether reflection failure in the heptad stabilizer \(2^4\!:\!A_7\) forces a meaningful cocycle/obstruction rather than merely an orientation relabelling. Failure at (i) or (iii) does not invalidate the valid constructed code.

## 7. Fourth work package — is the zero state a source-defined obstruction?

The known linear map \(U=I+T\) fixes zero and permutes nonzero states in a 2047-cycle. Ask for a **typed source rule** that acts on the empty/zero configuration to change this, with the transition's parent history, endpoint typing, reference, and admissibility witness retained. Does the native retained-comparison system authorize \(0\to1\) and the compensating \(g^{-1}\to0\), or does it require a different operation?

**Control:** an arbitrary nonzero splice point creates a full cycle. A mechanism is explanatory only if the source specifies the splice by an invariant criterion or produces a nontrivial obstruction class that must be resolved, not if it merely allows the resulting permutation. Also test the degree-three seven-position constituent: it has a seven-state nonzero cycle and one fixed zero, so the zero obstruction itself is not unique to eleven dimensions.

**Reject a false inference:** a 2048-cycle on syndrome labels is not a 2048-element orbit under the additive syndrome group, not a Golay-code automorphism, and not a Ramsey threshold.

## 8. Fifth work package — the actual Ramsey bridge (mandatory for success)

Require a uniform rule \(D_k\) that produces a red adjacency matrix or an obstruction certificate **from the primitive construction alone**, without reading a known witness or threshold. For a produced graph \(A\), verify

\[
A=A^\top,\quad A_{ii}=0,\quad
\operatorname{tr}(A^3)=0,\quad \alpha(A)<k.
\]

For an impossibility certificate, prove that no graph of the claimed size can satisfy the two forbidden-subgraph constraints. The test must distinguish **admissible 22** from **impossible 23** at \(k=7\). Independently test \(k=5\) (13 feasible, 14 impossible) and \(k=8\) (27 feasible, 28 impossible). A decoder tuned separately to each known answer is not predictive.

A single match of Golay's 23 coordinates with \(R(3,7)=23\) is inadequate. The code coordinates, 2048 syndrome states, 253 heptads, 759 octads and 2048-cycle positions have **different types**. Every proposed bridge must specify which become graph vertices, edges, constraints or certificates and prove the relevant preservation laws.

## 9. Decision table and stop rules

| Observation | Consequence | Next action |
|---|---|---|
| Typed source comparison does not descend to XOR | Source \(\to\) Golay derivation unsupported | Stop this bridge; retain Golay as a separate algebraic model |
| Source continuation distinguishes `G` from `0`, but red-support quotient erases that distinction | Binary state not sufficient | Refine the state/quotient or reject it; do not force a match |
| Eight-position incomplete extension is admitted | Perfect packing not source-forced | Reject forced-23 conjecture in its current form |
| Incomplete extension is rejected by a source-derived witness | Real progress on the missing rule | Prove the general rejection theorem and test for circularity |
| All admissible 16-phase decoders equivalent to \(\nu_2\) | Conditional quadratic rigidity | Seek source proof of the admission predicate and symmetry |
| Several inequivalent 16-phase decoders exist | Quadratic uniqueness false | Classify the family; look for missing observable selecting one |
| Zero splice not native or not unique | 2048-cycle is an optional permutation | Do not interpret it as an inherent coherence cycle |
| A uniform decoder proves 22/23 and an independent threshold | Genuine Ramsey relevance | State exact theorem and attempt general \(k\) |

## 10. Reproduction / starting artifacts

Run the following in the directory containing the files (all were rerun successfully for this handoff on 9 November 2026):

```sh
python check_ramsey_golay_2048_cycle.py
python ramsey_five_symbol_primitive_test.py
python ramsey_rgr00_source_promotion_audit.py
python ramsey_heptad_quadratic_golay_constructor.py
python check_golay_from_cyclic_squaring.py
python check_seven_frame_completion_necessity.py
```

Companion source notes:

- `ramsey_primitive_golay_2048_consolidated_research_note_2026-11-09.md` — definitions, proofs, precise caveats and full evidence inventory.
- `ramsey_five_symbol_source_orbit_and_missing_vertex_operation_2026-11-09.md` — ten-state source orbit and Petersen control.
- `ramsey_golay_cyclic_squaring_test_2026-11-09.md` — Golay cyclic polynomial and perfect syndrome enumeration.
- `ramsey_seven_frame_quadratic_golay_completion_2026-11-09.md` — conditional 7+16 completion and Witt systems.
- `ramsey_golay_completion_necessity_2026-11-09.md` — conditional necessity and incomplete-extension counterexample.

## 11. Recommended immediate continuation: attack \(R(3,7)\) directly

**Central mathematical question:** Can the retained phase/zero-state obstruction be converted into a *graph-independent* certificate that a triangle-free graph on 23 vertices must contain an independent seven-set, while the same primitive supplies an admissible 22-vertex construction?

Start from the necessary and sufficient Ramsey predicates, **not** from a supplied Golay code or a preselected field:

\[
 A=A^\top,\quad A_{ii}=0,\quad \operatorname{tr}(A^3)=0,\quad \alpha(A)\le 6.
\]

A feasible \(22\times22\) matrix establishes the lower bound; a proof that no \(23\times23\) matrix satisfies all four conditions establishes the upper bound. Seek a primitive-generated invariant on *all* such matrices that turns the second assertion into a local-to-global closure obstruction.

The distinctive proposed route is to exploit the observed seven-direction comparison quotient and eleven-phase \(2047+1\) structure **only after exhibiting a precise map** from red-neighborhood incidence constraints to retained phase records. Without that map, the observed code/cycle remains an analogy.

**Immediate falsifier:** If identical phase records can be assigned to graph states with incompatible triangle/independence continuations, the proposed phase state is too coarse to certify Ramsey behavior. If the phase action imposes no constraints on arbitrary triangle-free matrices, there is no Ramsey bridge. Report either result directly rather than continuing the Golay programme.

**Success criterion:** a proof of the 22/23 threshold from the same operation, with a separately checkable \(k=5\) or \(k=8\) prediction. A partial theorem identifying a *necessary* local-to-global obstruction on arbitrary triangle-free graphs is more valuable than another reconstruction of the Golay code.
