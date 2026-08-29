# Pfaffian rung: pairwise relations generate an emergent four-volume

## Question

What does the four-system Pfaffian mean structurally, beyond being a criterion for invertibility of a skew matrix?

## Claim boundary

Let \(V\) be the real four-dimensional defect space with basis \(e_1,e_2,e_3,e_4\). Encode pairwise skew interactions as the 2-form

\[
\omega
=
\sum_{i<j}a_{ij}e_i^*\wedge e_j^*.
\]

Then

\[
\frac12\omega\wedge\omega
=
\operatorname{Pf}(D)
\,e_1^*\wedge e_2^*\wedge e_3^*\wedge e_4^*,
\]

where

\[
\operatorname{Pf}(D)
=
a_{12}a_{34}-a_{13}a_{24}+a_{14}a_{23}.
\]

The Pfaffian is therefore the oriented four-volume created by composing pairwise relations.

### Why four is the first closing rung

In odd dimension a skew form is necessarily degenerate. Three pairwise-related real modes always leave one null direction. A fourth mode permits

\[
\omega\wedge\omega\ne0,
\]

which is equivalent to nondegeneracy of \(\omega\).

Thus the fourth system does not merely supply another repair coordinate. It allows the relation field itself to become volume-filling.

This is an exact sense in which the higher rung exposes composition capability rather than closing a residue by hand.

### Three perfect matchings are three factorizations of volume

The three monomials

\[
a_{12}a_{34},\qquad
a_{13}a_{24},\qquad
a_{14}a_{23}
\]

are the three perfect matchings of four labels. Each is a complete pairwise factorization of the four-system volume. Their signed superposition is the Pfaffian.

All six edges may be nonzero while the Pfaffian vanishes. Relationship density is therefore insufficient. What matters is coherent orientation among alternative complete matchings.

This answers the earlier relationship-density question sharply:

\[
\text{many relations}
\neq
\text{nondegenerate relational geometry}.
\]

### Decomposability shadow

In four dimensions,

\[
\operatorname{Pf}(D)=0
\]

is equivalent to \(\omega\wedge\omega=0\), hence to rank at most two for the skew form. The relation field then occupies only one effective interaction plane even if every coordinate edge is populated.

The shadow of failed four-way coherence is therefore dimensional collapse of the relation field, not absence of pairwise data.

### Orientation and the three coefficient lenses

The scalar lens sees

\[
\det D=\operatorname{Pf}(D)^2.
\]

It detects degeneracy but identifies opposite orientations.

The determinant-line lens retains \(\operatorname{Pf}(D)\) as an oriented volume element. Its sign or phase changes only by the declared frame law.

The ordered lens retains the actual matching products before addition. In a noncommutative coefficient algebra, the three products require specified order and may not collapse to one central Pfaffian.

Thus the lenses do supply different order-of-operation machinery:

- scalarization forgets factorization and orientation;
- determinant transport remembers oriented global volume;
- ordered holonomy remembers the construction history of that volume.

### Gauge transformation and invariant content

Under independent rescaling of defect frames \(e_i\mapsto g_ie_i\),

\[
\operatorname{Pf}(D)
\longmapsto
(g_1g_2g_3g_4)^{-1}\operatorname{Pf}(D)
\]

with the precise covariance determined by whether coefficients are written covariantly or contravariantly.

Therefore zero versus nonzero is frame-independent. A numerical sign is meaningful only after an orientation or determinant-line frame is source-fixed.

This repeats the tensor-unit lesson: the algebra may possess an oriented line without providing a physical constructor that preserves its chosen frame.

### Topological stability

For a continuous family \(D(t)\), the Pfaffian orientation cannot change sign without passing through

\[
\operatorname{Pf}(D(t_*))=0.
\]

At that point the interaction gap closes. Hence the sign labels connected components of the nondegenerate real skew-pairing space once an orientation frame is fixed.

This is the finite precursor of spectral-flow and determinant-line phenomena in completed Fredholm families.

### Interaction with deletion tomography

Deleting any vertex pulls \(\omega\) back to a three-dimensional space, where its top wedge vanishes automatically. Deleting one edge removes one matching contribution but may leave the other two to close the volume. Deleting an entire perfect matching removes two disjoint edges and can force the Pfaffian to depend on the remaining competing factorizations.

Therefore vertex deletion tests minimal collective dimension, while edge deletion tests redundancy among factorizations.

The highest-information deletion order is:

1. remove one vertex and verify the forced odd zero mode;
2. restore it and remove each edge separately;
3. remove each perfect matching;
4. track which deletion first forces \(\omega\wedge\omega=0\).

This reconstructs the matroid-like support of the symplectic volume.

### Completion analogue

For a family of completed skew-Fredholm operators, the determinant or Pfaffian line replaces the finite scalar Pfaffian. A nonvanishing section requires:

- Fredholmness, excluding essential zero modes;
- finite defect pairing with zero total index;
- a continuous source-authorized orientation of the Pfaffian line;
- a uniform spectral gap if quantitative stability is claimed.

A pointwise nonzero Pfaffian section can still approach zero under cutoff, reproducing finite faithfulness without completion stability.

### Falsifiers

The emergent-volume interpretation fails for a proposed four-system packet if:

- its interaction is not skew under the declared lens;
- the six edge coefficients do not transform as one 2-form;
- the Pfaffian depends on an unauthorized frame choice even at the zero/nonzero level;
- nonzero determinant is claimed while \(\omega\wedge\omega=0\);
- completion loses Fredholmness or the Pfaffian gap.

## Disposition

The four-system rung is the first point where pairwise relations can generate an oriented top-dimensional object. The Pfaffian measures that emergent relational volume. Its vanishing explains how a dense network of nonzero edges can still be effectively two-dimensional; its sign records a global orientation that scalar determinants erase.

This supplies a concrete structural candidate for the next tower: not another state variable, but the determinant-line object generated by coherent pairings. The subsequent tetrahedral rung then asks whether that emergent orientation is transported consistently across overlapping four-system packets.