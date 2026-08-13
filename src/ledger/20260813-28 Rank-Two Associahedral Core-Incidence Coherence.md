# Rank-Two Associahedral Carrier for Core-Incidence Coherence

## Record

Date: 2026-08-13

Status: the first nontrivial assembly test left open in entry 27 is solved at the scalar
presentation-cell level. Every rank-two ambiguity in the direct marked Catalan transfer has a
canonical associahedral carrier:

- independent physicalizing flips bound a square;
- consecutive dependent flips bound a pentagon, with the direct two-edge route opposed to a
  canonical three-edge refinement route.

The resulting signed boundary equations hold at every even arity. The marked scalar contact is
constant on each carrier, the construction tensors over the regions of every partial physical
core, and one-step rotation carries the full path data between the two polarity sheets.

This is the rank-two coherence datum required by a core-incidence chain map. It is not yet the
full chain map: rank-three and higher Stasheff coherences, followed by the filtered
Pochhammer/Cousin comparison, remain open.

## Input from the direct Catalan transfer

Fix a zero-core scalar triangulation \(T\), a marked scalar diagonal \(d\in T\), and a polarity
\(\epsilon\). Entry 26 decomposes the physicalizing flips in the direct transfer into disjoint
ordered dependency chains

\[
C_a=(f_{a,1},\ldots,f_{a,\ell_a}).
\]

A monotone intermediate state is indexed by a prefix vector

\[
\mathbf p=(p_1,\ldots,p_s),
\qquad
0\leq p_a\leq\ell_a.
\]

Write \(T_{\mathbf p}\) for the triangulation obtained by applying the first \(p_a\) flips in
each chain. Flips belonging to distinct chains commute, so the order in which the complete
prefixes are applied is immaterial. Moreover,

\[
|P(T_{\mathbf p})|=\sum_a p_a.
\]

Thus every selected flip raises the physical-core degree by one. The direct monotone states form
the vertex set of a product of chains, but the scalar presentation complex containing them is
the full associahedron. Its extra vertices are essential for comparable flips.

The marked diagonal is never flipped. It belongs to every \(T_{\mathbf p}\) and hence to the
common dissection defining every rank-two face below.

## Rank-two classification

Choose two physicalizing steps available in the transfer. There are exactly two cases.

### Independent steps: square

Suppose the next flips belong to distinct dependency chains, say \(C_a\) and \(C_b\). Starting
from \(T_{\mathbf p}\), both orders are legal and give the same endpoint:

\[
T_{\mathbf p}
\xrightarrow{a}
T_{\mathbf p+\mathbf e_a}
\xrightarrow{b}
T_{\mathbf p+\mathbf e_a+\mathbf e_b},
\]

\[
T_{\mathbf p}
\xrightarrow{b}
T_{\mathbf p+\mathbf e_b}
\xrightarrow{a}
T_{\mathbf p+\mathbf e_a+\mathbf e_b}.
\]

The four triangulations share a codimension-two dissection. The corresponding associahedral
face is a square. If the two directed routes are denoted by
\(\gamma_{ab}\) and \(\gamma_{ba}\), orient its cellular generator \(S_{ab}\) by

\[
\boxed{
\partial S_{ab}
=
\gamma_{ab}-\gamma_{ba}.
}
\]

Both routes have relative physical-core profile

\[
(0,1,2).
\]

This is strict commutation inside the direct prefix poset.

### Dependent steps: pentagon

Suppose instead that the two steps are consecutive in one dependency chain. Only the prescribed
order is a direct monotone route:

\[
\gamma_{\rm dir}:
\quad
T_{\mathbf p}
\longrightarrow
T_{\mathbf p+\mathbf e_a}
\longrightarrow
T_{\mathbf p+2\mathbf e_a}.
\]

The three displayed triangulations again share a codimension-two dissection, but now its
associahedral face is a pentagon. Removing the two direct edges from the boundary leaves a unique
three-edge path \(\gamma_{\rm ref}\) with the same endpoints. Orient the pentagonal generator
\(P_a\) by

\[
\boxed{
\partial P_a
=
\gamma_{\rm dir}-\gamma_{\rm ref}.
}
\]

Relative to the starting core, the direct path has profile

\[
(0,1,2),
\]

whereas the complementary refinement path has profile

\[
\boxed{
(0,0,1,2).
}
\]

The initial edge of \(\gamma_{\rm ref}\) is therefore a same-core scalar refinement. It is
precisely the additional presentation-cell datum that is erased by the augmentation to a
collected Laurent coefficient. The pentagon shows why the desired assembly cannot be modeled by
a uniformly cubical incidence complex.

## Exact signed boundary statement

Give every unoriented flip edge a fixed canonical orientation. For an oriented path \(\gamma\),
let \([\gamma]\) be the signed sum of its edges. In both cases above,

\[
\partial_0\bigl([\gamma_{\rm dir}]-[\gamma_{\rm alt}]\bigr)=0,
\]

and the support of this one-cycle is exactly the complete boundary graph of the relevant
rank-two face. Every boundary edge occurs with coefficient \(+1\) or \(-1\).

Consequently the relations are integral cellular identities, not only mod-two incidence
statements and not only identities after applying the amplitude augmentation.

For a square,

\[
\operatorname{supp}
\bigl([\gamma_{ab}]-[\gamma_{ba}]\bigr)
=
\partial S_{ab},
\]

with four unit edges. For a pentagon,

\[
\operatorname{supp}
\bigl([\gamma_{\rm dir}]-[\gamma_{\rm ref}]\bigr)
=
\partial P_a,
\]

with five unit edges.

## Why this is all-arity

The argument uses three all-arity facts already proved in entry 26:

1. the selected flips decompose into disjoint ordered chains;
2. flips in distinct chains commute;
3. the marked diagonal survives every selected flip.

Every codimension-two face of an associahedron is either

- a product of two one-dimensional associahedra, hence a square; or
- the two-dimensional associahedron of a pentagon.

Distinct chains realize the first alternative. Consecutive steps of one chain realize the
second. There is no third local rank-two type. This proves existence and uniqueness of the local
carrier at every even multiplicity.

The finite computation below is therefore a regression and sign certificate for the abstract
classification, rather than the source of the all-arity claim.

## Contact weight and absence of a repair pole

For the marked scalar occurrence, entry 26 assigns the contact coefficient

\[
-X_d.
\]

Because \(d\) belongs to the common dissection of every square or pentagon above, this
coefficient is constant on the entire 2-cell. Thus the signed boundary equations remain valid
after weighting by the marked contact.

At a nonempty partial physical core \(P\), tensoring with the unchanged regional factors also
leaves the retained denominator

\[
\frac{1}{\prod_{e\in P}X_e}
\]

constant on the local carrier. No additional pole, inverse Laplacian, or contact correction is
needed at rank two.

## Regional extension

Entry 27 identifies an exact-core scalar cell as a product of zero-core cells in the even
regions cut out by \(P\). The rank-two carrier extends over this product as follows:

- if both additions occur in one region, use its local square or pentagon and tensor with the
  identity carriers in all other regions;
- if they occur in different regions, the two regional operations commute and give the product
  square.

Hence the local homotopies are compatible with the regional monoidal structure already proved
at fixed core. This supplies the first two-dimensional layer of the sought core-incidence
assembly.

It does not by itself prove coherence among these 2-cells.

## Deck covariance

Let \(\rho\) be rotation by one external label. It exchanges the two alternating polarity
sheets. The direct Catalan transfer satisfies

\[
\rho\Phi_+=\Phi_-\rho.
\]

The stronger statement now checked is that \(\rho\) carries the entire rank-two record:

- source triangulation;
- marked diagonal;
- common codimension-two dissection;
- square route pair, or pentagon direct and refinement paths;
- endpoint and physical-core profile.

With the face orientation defined by the displayed boundary equation, rotation therefore pushes
the plus-sheet cellular relation to the corresponding minus-sheet relation. Rank-two coherence
is deck-equivariant before augmentation.

## Exact finite certificate

The standard-library audit enumerates every marked occurrence for both polarity sheets, verifies
the signed cellular boundary, and then compares the full rotated path records. Counts below are
for either one polarity; the other is identical.

| \(n\) | square occurrences | square faces | pentagon occurrences | pentagon faces |
|---:|---:|---:|---:|---:|
| 6 | 0 | 0 | 0 | 0 |
| 8 | 12 | 12 | 8 | 8 |
| 10 | 200 | 160 | 100 | 80 |
| 12 | 2,340 | 1,620 | 936 | 648 |

Every square boundary has four unit edges. Every pentagon boundary has five unit edges. Every
complementary pentagon path has relative core profile \((0,0,1,2)\).

Run:

    python -B research/nima/check_core_incidence_cells.py

The audit uses exact combinatorial objects and integral cellular coefficients. It performs no
random sampling and no numerical kinematic substitution.

## What is now established

1. every rank-two ambiguity in the direct transfer lies in an actual associahedral 2-cell;
2. independent steps commute through a square;
3. dependent consecutive steps are related through a pentagon;
4. the complementary pentagon route necessarily begins with a same-core scalar refinement;
5. both comparisons satisfy exact signed integral boundary equations;
6. the marked contact coefficient is constant on each carrier;
7. the construction tensors over arbitrary partial-core regions;
8. one-step rotation carries full carriers and paths between polarity sheets;
9. this rank-two structure exists at every even arity.

## What is not yet established

This entry does not claim:

1. a global differential on the complete core-filtered scalar presentation complex;
2. a full chain map from that complex to a QTDS or worldsheet complex;
3. coherence among overlapping square and pentagon homotopies;
4. the rank-three or higher Stasheff identities;
5. a filtered Pochhammer/Cousin comparison map;
6. a canonical twisted de Rham representative of \((\operatorname{Pf}'A)^2\);
7. a resolution of resonance on a physical factorization divisor.

In particular, an oriented boundary equation inside the scalar associahedron is a necessary
carrier for a chain homotopy. It becomes the desired comparison homotopy only after the source
and target differentials and the image of the 2-cell are specified.

## Primary next test: rank three

Three physicalizing steps give the first coherence-among-homotopies test. The dependency-chain
classification predicts three local carriers:

1. three steps in distinct chains: a cube;
2. two consecutive steps in one chain and one independent step: a pentagon times an interval;
3. three consecutive steps in one chain: the three-dimensional associahedron of a hexagon.

The first two should be forced by products of the rank-two data. The third is the genuinely new
test: its 14 vertices compare the different composites of pentagon homotopies. The executable
target is to enumerate these rank-three faces at \(n=10\) and \(n=12\), construct their signed
2-boundaries, and test deck covariance with the marked coefficient held fixed.

If the three-dimensional boundary closes, continue inductively through higher associahedra and
form the homotopy-coherent core-incidence transfer. Only then transport the result through the
finite-\(\alpha'\), filtered Pochhammer/Cousin comparison.

A failure of the hexagonal associahedron boundary to close with the inherited square/pentagon
orientations would be the first genuine obstruction to assembling the coefficient theorem into
one scalar presentation-chain object.

## Decision

Promote:

> The direct scalar-to-QTDS Catalan transfer carries a canonical, integral and deck-equivariant
> rank-two associahedral coherence system. Its local cells are squares for independent
> physicalizing flips and pentagons for dependent flips; the latter expose the necessary
> same-core scalar refinement invisible to the amplitude augmentation.

The Nima frontier advances from existence of pairwise incidence carriers to coherence among
those carriers. The next decisive object is the rank-three associahedron, followed—not
preceded—by the filtered scalar-to-worldsheet comparison.
