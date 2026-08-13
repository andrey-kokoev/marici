# All-Arity Rooted-Spine Base-Change Theorem

## Record

Date: 2026-08-13

Status: the support/source invariance inferred from the ten-, twelve-, and fourteen-point mixed
prism audits is now proved at arbitrary even arity and arbitrary partial physical core.

The proof is local on the rooted triangle tree.  A selected-child spine produces a physical
diagonal by propagating one opposite-sheet boundary vertex toward the root.  Once that diagonal
is created, its child-side quadrilateral is sealed; later flips can change only its root-side
neighbour.  A scalar rotation in an independent associahedral factor therefore cannot change the
cut support, source quadrilateral, or its two scalar slots.  After cutting, the two slot choices
give two regional inverse sections, each of which preserves the remote scalar edge.

Consequently the two-slot physical coaction of entry 34 is a strict cellular chain map on every
mixed product face, not merely in the finite audits.

This theorem closes the scalar-cellular naturality problem.  It does not by itself construct a
loaded Pochhammer/Cousin image or a preferred twisted de Rham representative.

## Regional reduction

Fix a partial physical core \(P\).  Its complement is a product of even polygonal regions,

\[
\operatorname{Cell}(P)
\cong
\prod_{R\in\mathcal R(P)}\operatorname{Cell}_0(R).
\]

The regional Catalan transfer and its inverse are tensor products over these regions.  A mixed
scalar/physical square is therefore either split between two regions, where naturality is
literal product functoriality, or lies in one region.  It suffices to prove the zero-core theorem
in one even region \(R\); all other regions and all pre-existing marks are spectators.

Write \(R^\pi\) for the parity polygon selected by a zero-core scalar triangulation \(T\), and
let \(d\in T\) be its contact mark.  Root the triangle-dual forest of \(T|_{R^\pi}\) at \(d\),
as in entry 26.  The polarity and parity sheet choose, at every triangle \(v\), one of the two
non-parent sides.  Denote it by \(c(v)\).

If \(c(v)\) is internal, it is the parent side of a unique child triangle.  Iterating gives the
selected-child spine

\[
v=v_0\longrightarrow v_1\longrightarrow\cdots\longrightarrow v_k,
\]

whose last selected side \(b(v)=c(v_k)\) is a parity-polygon boundary edge.  Let
\(o(b(v))\) be the unique opposite-colour vertex of the original even polygon lying between the
endpoints of \(b(v)\), and let \(a(v_j)\) be the vertex of \(v_j\) opposite \(c(v_j)\).

## Lemma 1: selected-spine formula

Leaf-first flipping along the spine inserts, at the step belonging to \(v_j\), the physical
diagonal

\[
\boxed{
e(v_j)=\bigl(a(v_j),o(b(v))\bigr).
}
\]

### Proof

For the terminal triangle \(v_k\), the two triangles adjacent to \(b(v)\) in the original even
polygon are the parity triangle and the opposite-colour ear.  Flipping \(b(v)\) therefore joins
\(a(v_k)\) to \(o(b(v))\).

Assume the formula after the descendants of \(v_j\) have been flipped.  On the child side of
\(c(v_j)\), the leaf-first sequence has propagated the same vertex \(o(b(v))\) to the cell
adjacent to \(c(v_j)\).  The root-side triangle is still \(v_j\), whose opposite vertex is
\(a(v_j)\).  Flipping \(c(v_j)\) therefore inserts
\((a(v_j),o(b(v)))\).  Induction proves the formula along the whole spine.

The formula is also a locality statement: a physical edge remembers only its starting triangle
and the terminal boundary leaf of its selected-child spine.

## Lemma 2: the sealed-source lemma

When \(e(v)\) is inserted, let \(S(v)\) be the quadrilateral on its child side.  Then:

1. \(S(v)\) is determined entirely by the suffix of the selected-child spine from \(v\) to
   \(b(v)\);
2. \(S(v)\) is unchanged by every later flip in the Catalan transfer;
3. the alternating coorientation directs \(e(v)\) from \(S(v)\) toward the root-side cell.

Hence \(S(v)\) is exactly the source quadrilateral of the directed physical edge \(e(v)\), and
its two diagonals are exactly the two coaction slots.

### Proof

All descendant flips on the selected spine occur before \(e(v)\), so the child-side cell is
already complete when \(e(v)\) is inserted.  Every unperformed flip is either closer to the root
on the same spine or belongs to a different selected-edge component separated by an unselected
scalar edge.  Such a flip can alter the root-side neighbour of \(e(v)\), but it cannot cross
\(e(v)\) and enter the completed child component.  The child-side quadrilateral is therefore
permanent.

Entry 26 proved that alternating coorientation points across every inserted edge toward the
root.  Thus the permanent child-side quadrilateral is the source, while the root-side target may
slide.  This proves all three statements.

## Lemma 3: rooted grafting locality

Let \(T_0,T_1\) be marked zero-core scalar triangulations with the same mark and differing by one
scalar rotation inside a polygonal factor \(A\) of a common associahedral face.  Let \(B\) be a
different factor of that face.

The rooted parent relation, selected-child choice, and selected-spine suffixes inside \(B\) are
the same for \(T_0\) and \(T_1\).  A spine may leave \(B\) through its unique attachment toward a
descendant factor, but it cannot leave and later re-enter \(B\).  Therefore:

- a physical diagonal whose starting triangle and terminal opposite-sheet boundary vertex lie
  in \(B\) is present for \(T_0\) if and only if it is present for \(T_1\);
- when present, its source quadrilateral is the same at both endpoints;
- only its root-side target quadrilateral can differ.

### Proof

Delete the unresolved factor \(A\) from the common triangle tree.  Every remaining component is
attached to \(A\), if at all, through one fixed tree edge.  If the mark lies outside a component,
that attachment is its root edge at both endpoints.  If the mark lies inside, the rooted paths
inside the component are determined entirely by the common restricted triangulation.  Thus all
parent sides and selected-child choices in \(B\) agree.

A selected-child spine is a directed path in a tree, so after crossing the attachment of \(B\)
it cannot return.  By Lemma 1, a physical edge local to \(B\) can only be produced by a spine
whose relevant suffix remains in \(B\).  That suffix is identical at the two endpoints, proving
support invariance.  Lemma 2 then proves source-cell and slot invariance.  A change in \(A\) can
meet the edge only on its root side, which is precisely the allowed target slide.

This is the required local rooted-dual-tree argument; no enumeration of ambient triangulations
or induction in the multiplicity is involved.

## Lemma 4: the two inverse cut sections

Let \(Q=\Phi_{\epsilon,P}(T;\mathbf d)\) contain a directed physical edge

\[
e:S\longrightarrow T_{\rm root}
\]

with source slots \(s^0,s^1\).  Delete \(e\).  For each \(\sigma\in\{0,1\}\), mark the new
source component by \(s^\sigma\) and apply the regional inverse Catalan map.  This defines a
section

\[
\lambda_{e,\sigma}
=
\Psi_{\epsilon,P\cup\{e\}}
\bigl(Q;\mathbf d\cup s^\sigma\bigr).
\]

If \(T_0\leftrightarrow T_1\) is a scalar edge in an independent factor and the hypotheses of
Lemma 3 hold, then

\[
\lambda_{e,\sigma}(T_0)
\longleftrightarrow
\lambda_{e,\sigma}(T_1)
\]

is a scalar edge at core \(P\cup\{e\}\), for each \(\sigma\).

### Proof

Cutting \(e\) separates the permanent source-side subtree of Lemma 2 from the root-side subtree.
The regional inverse is the tensor product of the inverse selected-spine algorithms on those two
trees.  Choosing \(s^\sigma\) changes only the parity refinement of the new source component.
The remote scalar rotation is a rooted subtree substitution in a different product factor.
Inverse spine operations in the two factors commute, so the same single rotation relates the two
inverse images for either slot.

If the original scalar edge and the physical edge are the two factors of a mixed product square,
one of these sections is its visible upper scalar edge.  The other is a parallel upper scalar
edge.  There is exactly one of each: the two slots cross inside the same source quadrilateral, so
no scalar triangulation can contain both, while the one-edge restriction of the forward/inverse
bijection guarantees that one slot reconstructs the visible upper endpoints.

## All-arity rooted-spine base-change theorem

Let

\[
h:x_0\longrightarrow x_1
\]

be a scalar-refinement one-cell in the marked associahedral envelope at partial physical core
\(P\).  Let \(e\notin P\) be the physical factor of an independent mixed product square.  Decorate
the lower endpoints by arbitrary common component marks and apply the regional marked Catalan
transfer.

Then, at every even arity:

1. **Support dichotomy**
   \[
   e\in\Phi(x_0)
   \quad\Longleftrightarrow\quad
   e\in\Phi(x_1).
   \]

2. **Common-zero case.** If \(e\) is absent, both cut routes vanish.

3. **Source-germ invariance.** If \(e\) is present, its source quadrilateral and its two slots
   \(d_e^0,d_e^1\) agree at the two endpoints.  The target quadrilateral may slide.

4. **Two upper edges.** For each slot, regional inverse descent at core
   \(P\cup\{e\}\) reconstructs a genuine scalar one-cell \(h_e^\sigma\).  Exactly one is the
   visible upper edge of the mixed carrier; the other is its parallel slot edge.

5. **Strict coefficient base change**
   \[
   \boxed{
   G_e(h)
   =
   -\frac{X_{d_e^0}}{X_e}h_e^0
   -\frac{X_{d_e^1}}{X_e}h_e^1,
   \qquad
   \partial G_e(h)=G_e(\partial h).
   }
   \]

### Proof

Use the regional reduction.  The scalar and physical factors are distinct unresolved regions of
the product face supplied by the all-rank block-face theorem.  Lemma 3 gives support and source
invariance.  Lemma 4 gives the two upper scalar edges.  Their Laurent multipliers depend only on
the common source slots and \(e\), so they agree endpointwise.  Taking the signed cellular
boundary proves the final identity term by term.

## Extension over the transverse mixed-cell system

Every cell of the marked envelope is a product

\[
F_{\mathbf r}\cong\prod_a K_{r_a}.
\]

A physical cut in an independent factor is natural on each one-dimensional scalar edge by the
theorem.  Naturality on every product cell generated by such transverse factors follows because:

1. the cellular differential of a product is generated by its oriented facets;
2. the physical cut operators commute strictly with one another by entry 32;
3. the two-slot lift is compatible with rooted subtree substitution;
4. every higher face is an associahedron or product of associahedra, whose relations are generated
   by these facet incidences.

Thus for every cut set \(E\) transverse to the selected scalar block factors,

\[
\boxed{
G_E:
C_*^{\rm cell}(\operatorname{AssEnv};\mathcal L_J)
\longrightarrow
C_*^{\rm cell}(\operatorname{AssEnv}_{P\cup E};\mathcal L_J)
}
\]

is a well-defined, deck-equivariant cellular chain map on the corresponding mixed product
subcomplex, and

\[
G_EG_F=G_FG_E
\]

for disjoint available cut sets.

This promotes the universal mixed-prism coefficient skeleton of entries 32--35 to an all-arity
cellular coaction on all of its product-associahedral propagations.  It does not yet assert a
Gysin map for an arbitrary nontransverse intersection of a physical divisor with an unrelated
scalar cell; that broader extension belongs naturally to the facewise Pochhammer/Cousin target.

## Relation to the finite audits

The theorem explains every previously empirical feature:

- common-zero support is the case in which the selected spine exits the local factor;
- supported edges have an unchanged terminal spine suffix;
- the source is fixed because it is the sealed child-side cell;
- the target slides precisely when the remote rotation changes the root-side neighbour;
- the forced and parallel upper edges are the two inverse cut sections;
- spectator stability is rooted grafting locality;
- deck covariance follows because one-step rotation exchanges predecessor and successor while
  rotating every rooted spine.

The exhaustive Rust counts through fourteen points remain independent regression certificates,
not premises of the proof.

## Epistemic boundary

Established here:

1. all-arity support naturality;
2. all-arity source-cell and slot invariance;
3. both regional inverse upper edges;
4. strict mixed Beck--Chevalley base change;
5. extension of every transverse physical cut over the full family of mixed
   product-associahedral cells;
6. arbitrary spectator cores and marks;
7. deck covariance.

Not established here:

1. a finite-nonresonant-\(\alpha'\) loaded-current realization;
2. a filtered comparison with logarithmic/twisted worldsheet complexes;
3. commutation with resonant physical specialization;
4. a preferred off-shell or de Rham representative;
5. chain-level equality with \((\operatorname{Pf}'A)^2\).

## Decision

Promote:

> The marked Catalan transfer is natural under independent rooted subtree substitution.  A
> physical cut sees only the sealed child-side source germ of its selected spine; hence its
> support, slots, and two inverse scalar lifts are invariant under every remote scalar
> associahedral refinement.  The scalar occurrence system therefore carries an all-arity strict
> cellular cut coaction.

The primary frontier is now genuinely worldsheet-theoretic:

> apply the canonical normal-torus/Pochhammer construction to this cellular cosheaf at finite
> nonresonant \(\alpha'\), keeping the scalar associated-grade extraction prior to the
> worldsheet regularization.
