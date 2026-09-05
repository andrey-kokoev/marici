# Six-point cross-order chain lift: novelty gate

## Question

Can the order-labelled NMHV simplex carrier map to the worldsheet twisted complex by a residue-intertwining chain map in a way that makes BCJ descent intrinsic before canonical-form evaluation?

## Source object presently available

For each DDM ordering `alpha`, the existing construction assigns a signed top chain

\[
T(\alpha)\in C_4^{\mathrm{simp}},
\]

with three oriented five-label simplex generators. The exact checker `check_six_point_nmhv_bcj_chain_relation.py` evaluates all 24 fundamental BCJ generators `b` and proves

\[
\Omega(T(b))=0,
\qquad
T(b)\ne 0,
\]

both for raw Mandelstam weighting and for the tested Parke–Taylor dressing. Here `Omega` is canonical-form evaluation.

## Strict descent obstruction

Let `q:V_6 -> V_6/B_6` be the BCJ quotient. A strict factorization

\[
T=\bar T\circ q
\]

exists if and only if `T(B_6)=0`. The checker supplies 24 counterexamples, so no strict factorization into the current simplex chain module exists.

More generally, suppose an enriched source complex `C`:

1. contains `C_4^{simp}` injectively in degree four;
2. has no degree-five chains whose boundaries can kill the displayed BCJ chains;
3. retains the tested simplex assignment.

Then the nonzero `T(b)` survive as nonzero degree-four chains, and strict BCJ descent remains impossible. Any successful lift must therefore do at least one of the following: identify top cells across orderings, add degree-five homotopies, or quotient by a relation module containing `T(B_6)`.

## Why this is not yet publishable

The proposition is formal once `T(B_6) != 0` is known. Publication requires a source-derived classification theorem showing that a natural class of residue-local Grassmannian or amplituhedron enrichments is forced to satisfy conditions 1–3. Without that theorem, adding higher cells or quotient relations evades the obstruction by definition.

## First missing typed object

There is currently no canonical cross-order source complex. The checker identifies equal sorted five-label generators across orderings, but it does not derive that identification from a common positive geometry, gluing functor, or oriented-matroid map. Consequently its nonzero chains cannot yet be promoted to invariant homology classes.

## Acceptance test

Construct a common complex `C_cross` with:

- an independently defined generator and orientation set;
- embeddings of every ordered simplex triangulation;
- a boundary map with `d^2=0`;
- residue maps for all physical divisors;
- a declared policy on higher cells and cross-order identifications.

Then compute whether every `T(b)` is zero, a boundary, or a nonzero homology class. A nonzero class invariant under all admissible refinements would yield a genuine obstruction theorem. An explicit null-homotopy compatible with residues would yield the desired comparison construction. Until `C_cross` is source-derived, neither conclusion is available.

## Minimal common complex test

The label set canonically defines the oriented simplicial chain complex of the abstract five-simplex,

\[
C_{\mathrm{cross}}=C_*(\Delta^5;K).
\]

Its six degree-four generators are the five-label facets. Every cyclic ordering modulo reflection gives a signed three-facet chain, so all 60 ordered triangulations embed in one `C_4`. The residue map is the signed simplicial boundary `d_4:C_4 -> C_3`; each codimension-one residue is a coordinate projection of this boundary. Exact matrices verify `d^2=0`. The unique degree-five simplex has the standard alternating six-facet boundary, and `H_4(Delta^5;K)=0`.

All 24 fundamental raw BCJ-weighted chains have now been classified:

- zero: 0;
- boundaries: 0;
- nonzero homology classes: 0;
- non-cycles: 24.

Thus every tested BCJ chain has a nonzero residue boundary. None defines a homology class in the minimal common complex, so adding the single available degree-five simplex cannot kill it. This is stronger than the earlier nonzero-chain result: the obstruction already occurs at residue compatibility.

Evidence:

- `research/nima/checkers/check_six_point_common_cross_order_complex.py`
- `research/nima/results/six-point-common-cross-order-complex.json`

## Minimal free repair

Let `D` be the `15 x 24` matrix of residue boundaries of the fundamental BCJ chains. Exact linear algebra gives

\[
\operatorname{rank}T(B_6)=4,
\qquad
\operatorname{rank}D=4.
\]

Therefore four new degree-four defect lifts are necessary and sufficient to cancel every BCJ residue. After adjoining them, the 24 corrected chains are cycles spanning a four-dimensional space. Four degree-five null-homotopies are then necessary and sufficient to make every corrected BCJ cycle exact. The resulting mapping-cone extension satisfies `d^2=0` and has vanishing fourth homology.

The pivot relations are indexed by permutations `(2345)`, `(2354)`, `(2435)`, and `(3245)`; every other repair is recorded in exact coordinates relative to these four.

Evidence:

- `research/nima/checkers/check_six_point_minimal_bcj_chain_repair.py`
- `research/nima/results/six-point-minimal-bcj-chain-repair.json`

## Worldsheet comparison test

The minimal repair is not the full scattering-equation relation module. Its repair space has rank four, whereas the generic BCJ relation module has rank eighteen. It captures only the image `T(B_6)`, equivalently `B_6/ker(T|_{B_6})`. No canonical map identifies the four freely adjoined defect lifts or null-homotopies with scattering-equation exact forms. Dimension and exactness alone do not supply such a map.

## Disposition

The minimal free repair is completely classified as `(4 degree-four lifts, 4 degree-five homotopies)`. It repairs the fixed simplex assignment but does not establish a worldsheet identification and is not independently publishable: it is the mapping cone of a rank-four defect map. A publishable result would require deriving these eight generators from source geometry or proving that every residue-local repair contains this mapping cone canonically.
