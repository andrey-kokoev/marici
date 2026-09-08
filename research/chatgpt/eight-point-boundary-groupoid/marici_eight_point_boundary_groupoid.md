# Eight-point boundary assembly for the arithmetic transport proposal

Date: 2026-09-06

## Result and scope

This extends the source lookup beyond the six-point cyclic packet. It constructs the actual finite indexing diagram for the union of the eight physical six-by-four Cut facets in Marici's loaded octagon model, including their common strata and coefficient-localization maps. It proves an exact derived-section gluing formula over this diagram and computes its indexing homotopy type with dihedral transport.

The selected boundary has 7,100 loaded cells and 24,160 generating incidence arrows. Its cover has eight patches, twelve nonempty pairwise intersections, and no nonempty triple intersections. Each patch has 1,075 loaded cells; each pairwise intersection has 125.

The nerve of the boundary indexing category is homotopy equivalent to a wedge of five circles. With the source's order-sixteen octagon dihedral action, its homotopy quotient has fundamental group C2 * (C2 x C2), and all higher homotopy groups vanish. This is an indexing-space calculation, not a computation of the full coefficient-marked physical moduli space.

For any covariant integral derived coefficient diagram on this index, its derived sections are the homotopy fibre of the difference of restrictions from the eight patch section complexes to the twelve overlap section complexes. A proof is given below; it does not assume that coefficient localization maps are equivalences.

No identification of these derived sections with Marici's complete physical relative totalization or its normalized readout is asserted. The previous six-point contraction cannot supply that identification. The other 5,325 loaded octagon cells are not part of the selected boundary union and have not been attached in this computation.

## 1. Pinned source

Repository: `andrey-kokoev/marici`

Commit: `d1947b67a60d3e88ba77f4ca60ea02c2a306ee61`

Source files, read through the GitHub connector:

- `research/voevodsky/check_n8_six_by_four_cut_boundary.py`
- `research/voevodsky/check_n8_loaded_octagon_carrier.py`
- `research/voevodsky/check_n8_multirees_conductor_stalk_kernel.py`
- `research/voevodsky/check_n8_cut_naturality_after_sheet_transform.py`

The new checker independently enumerates the source's combinatorial rules. It does not run their imported geometric, sheet-transform, or amplitude audit pipelines. The source's declarations about physical readouts are therefore not treated as independently re-proved by this indexing audit.

## 2. The indexing category and its coefficient diagram

Label octagon vertices by integers modulo eight. Let D contain its twenty diagonals. Let F be a pairwise noncrossing set of diagonals, and M a subset of F. A loaded cell is the pair (F,M), with degree

\[
\deg(F,M)=5-|F|+|M|.
\]

In words: the source degree decreases when an unmarked diagonal is added or a mark is removed.

The two generating arrows are

\[
(F,M)\longrightarrow(F\cup\{d\},M),\qquad
(F,M)\longrightarrow(F,M\setminus\{d\}).
\]

In words: add a compatible unmarked diagonal, or remove an existing mark. Adding is allowed only when the enlarged face remains noncrossing.

Use the resulting poset category J, in which

\[
(F,M)\leq(F',M')\quad\Longleftrightarrow\quad F\subseteq F',\ M'\subseteq M.
\]

In words: along a composite incidence, the face can only grow and the marked subset can only shrink. Every such comparable pair is connected by the generating moves. Source coefficient maps depend on the endpoints, so the poset relations are supplied by actual commuting localizations rather than arbitrarily imposed new physical relations.

The source localization set is

\[
L(F,M)=F\setminus M.
\]

In words: exactly the unmarked face coordinates are inverted. Every generating arrow adds one coordinate to this set.

A precise formal coefficient realization of the source's exponent rule is

\[
R_L=\mathbb Z[u_d,v_d\ (d\in D),\ v_d^{-1}\ (d\in L)].
\]

In words: all first-family exponents are nonnegative; negative second-family exponents are allowed only on the localization set. These variable names are conventions for the formal source rings, not newly identified physical observables.

The source conductor row is the complex

\[
Q_L=\left[R_L[z_+]\oplus R_L[z_-]
\xrightarrow{\ e\ }R_L\right],\qquad
 e(f_+,f_-)=f_+(0)-f_-(0).
\]

In words: take the difference of the two branch values at the conductor. Put the left term in cohomological degree zero and the right term in degree one as a declared grading convention.

Coefficient localization gives chain maps between these complexes. Evaluation at zero commutes with every such localization because both operations act coefficientwise. This is a polynomial identity in every degree, not a conclusion drawn from testing finitely many monomials. Thus the rule defines a strict diagram Q on J, and hence a homotopy-coherent diagram in the derived infinity-category of integral complexes.

This row alone is not being equated with the entire physical coefficient system; source variance, support, relative-chain, and readout data may require additional diagrams.

## 3. Eight patches and their actual intersections

The source physical Cuts form the set

\[
\mathcal P=\{\{i,i+3\}:i\in\mathbb Z/8\}.
\]

In words: these are the eight diagonals splitting the octagon into a hexagon and a quadrilateral.

For a Cut d, take the full subcategory

\[
J_d=\{(F,M):d\in F\setminus M\}.
\]

In words: the Cut is present as an unmarked divisor. This is the source's closed-facet indexing embedding, not its separate degree-shifted marked-normal copy.

Write J_U for the union of these eight subcategories. Every J_d is forward closed: once d is unmarked, every subsequent source incidence retains it. Consequently every chain in J_U lies entirely in at least one J_d. This is important: the patch nerves cover the entire nerve, not merely its vertices.

The checker obtains:

| Index | Loaded cells | Degree counts, starting at zero |
|---|---:|---|
| Full octagon J | 12,425 | 132, 990, 2,940, 4,320, 3,140, 903 |
| One physical facet J_d | 1,075 | 28, 168, 375, 369, 135 |
| One nonempty intersection J_d intersect J_e | 125 | 8, 36, 54, 27 |
| Selected boundary J_U | 7,100 | 128, 912, 2,352, 2,628, 1,080 |

Two patches intersect exactly when their Cut diagonals are noncrossing. There are twelve such pairs. No three physical Cut diagonals are mutually compatible, and the checker verifies all 56 candidate triple intersections are empty. Therefore

\[
|\operatorname{Ob}J_U|=8\cdot1075-12\cdot125=7100.
\]

In words: subtract the twelve double-counted overlaps from the eight facet totals; there are no higher intersection corrections.

For every nonempty compatible set S of physical Cuts, the overlap is exactly the inherited full subcategory with S contained in the localization set. Inclusions of overlaps into facets and into J_U give literal comparison functors. Restricting Q along these functors gives the coefficient comparisons; no arbitrary isomorphism between different facets is inserted.

## 4. Exact derived-section assembly

Let C be any specified covariant diagram on J_U with values in the derived infinity-category of integral complexes. It can be Q above or a larger supplied source diagram.

Define

\[
T_d=\operatorname*{lim}_{J_d}C,\qquad
T_{de}=\operatorname*{lim}_{J_d\cap J_e}C,\qquad
T_U=\operatorname*{lim}_{J_U}C.
\]

In words: take homotopy limits, retaining all coefficient and comparison degrees, over a facet, an overlap, and the selected union respectively. These are derived sections of the specified diagram.

Orient each compatible pair by the displayed vertex ordering. Then

\[
T_U\simeq\operatorname{fib}\left(
\bigoplus_{d\in\mathcal P}T_d
\xrightarrow{\ \Delta\ }
\bigoplus_{\{d,e\}\in E}T_{de}\right),
\]

\[
\Delta((a_d)_d)_{de}=\operatorname{res}_{e,de}(a_e)-\operatorname{res}_{d,de}(a_d).
\]

In words: compare both restrictions on every overlap and retain a homotopy witnessing their agreement. All sums are finite, so they are also products. The homotopy fibre retains higher comparisons inside the input complexes; this formula is not an ordinary kernel or a truncation to two physical chain degrees.

### Proof

For a forward-closed subcategory V of J_U, let Z_V be the constant integral diagram on V extended by zero to J_U. It is also the derived left Kan extension of the constant integral diagram: the relevant comma category is empty outside V and has a terminal object inside V.

There is a pointwise exact sequence of diagrams

\[
0\longrightarrow\bigoplus_{\{d,e\}\in E}\mathbb Z_{J_d\cap J_e}
\longrightarrow\bigoplus_{d\in\mathcal P}\mathbb Z_{J_d}
\longrightarrow\underline{\mathbb Z}_{J_U}\longrightarrow0.
\]

In words: an object belongs to one patch or two. At a one-patch object the last map is the identity; at a two-patch object the first map is the primitive vector minus-one, plus-one, and the last map sums coordinates. This proves exactness over the integers without inverting any prime.

Naturality follows because supported Cut labels only increase along arrows. Applying derived Hom from this sequence into C produces the claimed fibre sequence. The Kan-extension adjunction identifies its terms with the appropriate homotopy limits. The checker verifies support exactness and its naturality on the generating incidences. The proof covers arbitrary composites and arbitrary integral coefficient complexes.

Thus the boundary gluing problem is reduced to eight patch complexes, twelve overlap complexes, and their supplied restriction maps. It is not solved merely by knowing each patch's final scalar readout.

### Constant-coefficient control

For the constant diagram Z, each facet and overlap has contractible index nerve, as proved next. The assembly map is then the ordinary 12-by-8 graph incidence matrix. Its integral kernel is Z and its cokernel is free of rank five:

\[
H^0(T_U)=\mathbb Z,\qquad H^1(T_U)=\mathbb Z^5,
\qquad H^q(T_U)=0\quad(q\notin\{0,1\}).
\]

In words: the constant coefficient test has one global constant and five incidence cohomology classes, with no torsion. This is a control calculation, not the homology of the nonconstant physical diagram. In cohomological grading, positive-degree cohomology is not automatically positive homotopy of Map(Z,T_U).

## 5. Contracting the patch indices, not the coefficients

On any nonempty patch intersection J_S, define

\[
q(F,M)=(F,\varnothing),\qquad b_S=(S,\varnothing).
\]

In words: forget the remaining marks, and use the unmarked Cut set as a base object.

There are natural transformations from the identity functor to q and from the constant functor at b_S to q. Both follow directly from the poset order. Hence the nerve of J_S is contractible. These transformations are equivariant under every relabelling stabilizing S.

The finite cover nerve theorem [M1] now gives

\[
|N J_U|\simeq K,\qquad K\simeq\bigvee_{j=1}^{5}S^1.
\]

In words: the index has the homotopy type of its eight-vertex, twelve-edge overlap graph, which is a wedge of five circles. The checker constructs an integral cycle basis and the complete dihedral action on it.

In the vertex order

`03, 05, 14, 16, 25, 27, 36, 47`,

the compatible pairs are

`01, 06, 07, 12, 14, 23, 27, 34, 36, 45, 56, 57`.

Here each pair in the latter list consists of vertex indices, not octagon endpoint labels.

The nerve comparison can be made naturally with respect to the dihedral action by using the cover's homotopy-colimit construction. The contraction of each intersection is natural under its stabilizer. Therefore it induces an equivalence after taking homotopy quotients.

Crucial restriction: q may invert additional coefficient variables. Those ring-localization maps need not be quasi-isomorphisms. Contractibility of an INDEX nerve does not make an arbitrary coefficient diagram constant. The proof of Section 4 deliberately retains that distinction.

## 6. Dihedral transport on the indexing space

Use D8 for the dihedral group of order sixteen, with elements (r,f) acting by

\[
i\longmapsto r+(-1)^f i\pmod8.
\]

In words: rotate by r and optionally reflect. This is the relabelling action used by the source octagon checker. It permutes the actual cells, patches, overlaps, and localization variables. The present calculation does not independently identify this index action with every loaded sheet-orientation action in the full physical theory.

Define the indexing infinity-groupoid

\[
\mathscr I_8=\operatorname{Sing}(|N J_U|)//D_8.
\]

In words: take the homotopy type of the indexing diagram and retain the source's dihedral relabelling symmetry. This is NOT the core of the category of whole physical arithmetic diagrams; the latter has additional coefficient data and restrictions.

To compute its fundamental group, subdivide each graph edge. This is necessary because some symmetries exchange its endpoints. The quotient of the subdivided graph is a path with three vertices:

| Vertex type | Stabilizer |
|---|---|
| Midpoint of a shared-endpoint compatible pair | C2 |
| Physical Cut | C2 |
| Midpoint of a disjoint compatible pair | C2 x C2 |

The two half-edge stabilizers are respectively trivial and C2. The second half-edge maps isomorphically to the middle vertex group. The graph-of-groups presentation [M2] therefore reduces to

\[
\pi_1(\mathscr I_8)\cong C_2*(C_2\times C_2)
=\langle a,b,c\mid a^2=b^2=c^2=1,\ bc=cb\rangle.
\]

In words: there are three involutions; the second and third commute; no relation is imposed between the first and the other two beyond those displayed.

Representatives are the Cut 03, the shared-endpoint pair {03,05}, and the disjoint pair {03,47}. Their stabilizers in (r,f) notation are respectively

- {(0,0),(3,1)};
- {(0,0),(0,1)};
- {(0,0),(3,1),(4,0),(7,1)}.

The homomorphism to D8 sends a to (0,1), b to (3,1), and c to (4,0). Its kernel is the free group on five generators:

\[
1\longrightarrow F_5\longrightarrow C_2*(C_2\times C_2)
\longrightarrow D_8\longrightarrow1.
\]

In words: the five graph loops are the kernel after forgetting the route through the overlap graph and retaining only the overall dihedral relabelling.

This extension does not split. A finite subgroup of a free product is conjugate into a factor; here the factors have orders two and four, so there cannot be a subgroup of order sixteen furnishing a section. Thus replacing the answer by a semidirect product F5 semidirect D8 would be incorrect.

Finally, the Borel fibration has fibre K and base BD8, both aspherical. Its long exact homotopy sequence gives

\[
\pi_n(\mathscr I_8)=0\quad(n\ge2).
\]

In words: this enlarged indexing groupoid remains a one-type. Its order-two stabilizers reflect actual index symmetries; they are not a proof of new physical prime residues.

## 7. Relation to the proposed arithmetic infinity-groupoid

The fixed-source objects can now contain this specific J_U diagram and its actual overlap comparisons, instead of an unspecified indexing category. Noninvertible coefficient-localization maps remain INSIDE those objects. Taking the homotopy type of J_U in Section 6 does not license treating a localization as an invertible arithmetic transport.

For the boundary derived-section version of the proposal, the space of coefficient markings is Map(Z,T_U). With a supplied compatible source readout, one can take its homotopy fibre over the required normalization. The missing calculation is the actual patch and overlap complexes after all physical relative operations and their normalized readouts are retained.

A useful conditional check follows immediately: if all normalized patch marking spaces AND all normalized overlap marking spaces are contractible, their homotopy limit is contractible. Five loops in the index do not force five arithmetic residue classes. Conversely, nonconstant restrictions or noncontractible overlap marking spaces can change the gluing problem; the fibre formula specifies where to compute that change.

The other octagon strata may attach relations killing index loops. No survival under those attachments, no global all-arity assembly, and no RH implication are established here.

## 8. Reproduction and certificate

Run with Python's standard library:

```sh
python check_marici_eight_point_boundary_groupoid.py --output marici_eight_point_boundary_certificate.json
```

The run passed 644,169 exact checks. They cover loaded cells and all generating arrows, localization inclusions, cover-resolution exactness and naturality, contractions of every nonempty intersection index, dihedral actions, all group-composition checks on diagonals and integral graph homology, source radial orientation comparisons, stabilizers, and the graph-of-groups quotient data.

The certificate contains the complete eight-vertex graph, its integral cycle basis, all sixteen five-by-five homology action matrices, and the source/scope declarations. Homotopy and derived-section conclusions use the proofs above in addition to the finite checks. This is not proof-assistant verification.

## Mathematical references

[M1] Daniel A. Ramras, *Variations on the Nerve Theorem*, Discrete & Computational Geometry 75 (2026), 871–903. Published online December 3, 2025. Introduction and Sections 2–3, including the cover/realization and homotopy-colimit comparison.
`https://link.springer.com/article/10.1007/s00454-025-00809-3`

[M2] *Boundary actions of Bass–Serre Trees and the applications to C*-algebras*, arXiv:2502.02039v1, Section 2 on graphs of groups and their fundamental groups. The amalgamated-product calculation in Section 6 is written out explicitly above.
`https://arxiv.org/html/2502.02039v1`

[M3] The Stacks Project, *Hom complexes*, for the derived linear-comparison formalism used in the surrounding transport proposal.
`https://stacks.math.columbia.edu/tag/0A8H`
