# Direct Catalan Bijection and QTDS Contact Theorem

## Record

Date: 2026-08-13

Status: the minimum-distance pattern of entry 25 has been replaced by a direct all-arity
construction with an explicit inverse. For every even multiplicity and either alternating
polarity, marked zero-core scalar triangulations are canonically bijective with marked
unique-sink quadrangulations. The scalar flip distance is exactly \((n-4)/2\), the shortest paths
are linear extensions of a disjoint union of chains, and their average gives the canonical
deck-odd contact homotopy.

A separate vertex-local argument proves at all arity that these unique-sink slots are exactly the
polynomial contact sector of the complete QTDS period, with coefficient \(-1\) in the convention
used by the audits.

This settles the contact layer of the Jordan/QTDS strictification. It does not yet construct the
complete transfer over every partial physical core, nor the filtered worldsheet comparison.

## Setup

Let \(n=2m\geq6\). Color the vertices of the cyclic polygon alternately. Call a diagonal

- scalar if its endpoints have the same color;
- physical if its endpoints have opposite colors.

Let \(Z_{2m}\) be the scalar triangulations with empty physical core. Let
\(U_{2m}^{\epsilon}\) be the quadrangulations whose dual tree, directed by alternating
coorientation \(\nu_\epsilon\), has a unique sink. Each \(Q\in U_{2m}^{\epsilon}\) has two
marked scalar slots, the two diagonals of its sink quadrilateral.

The theorem concerns

\[
\widetilde Z_{2m}
=
\{(T,d):T\in Z_{2m},\ d\in T\}
\]

and

\[
\widetilde U_{2m}^{\epsilon}
=
\{(Q,d):Q\in U_{2m}^{\epsilon},\
d\in\operatorname{Slot}_{\epsilon}(Q)\}.
\]

## Lemma 1: zero-core triangulations are parity-polygon triangulations

In a zero-core triangulation every non-boundary edge joins equal colors. A triangle is therefore
of exactly one of two types:

1. all three vertices have the same color, so all three sides are scalar diagonals;
2. two vertices have one color and the third has the other, in which case the two opposite-color
   sides must be original polygon edges and the triangle is an ear.

The non-ear triangles form a connected subtree of the triangle dual tree. Adjacent non-ear
triangles share a scalar edge and hence have the same color. Thus every non-ear triangle lies on
one parity sheet. Every vertex of the opposite color is an ear between its two neighbors on that
sheet.

Consequently \(T\) consists of:

1. all \(m\) boundary edges of one parity \(m\)-gon, viewed as short diagonals of the original
   \(2m\)-gon;
2. an arbitrary triangulation of that parity \(m\)-gon.

Conversely every such parity-polygon triangulation is a zero-core scalar triangulation. Hence

\[
\boxed{|Z_{2m}|=2C_{m-2}.}
\]

The factor two is the alternating sheet choice.

## Direct construction

Fix \((T,d)\in\widetilde Z_{2m}\), a polarity \(\epsilon\), and the parity sheet of \(T\).
Regard \(T\) as a triangulated parity \(m\)-gon.

Insert an abstract root at the marked edge \(d\). If \(d\) is an internal parity-polygon
diagonal, this gives two rooted triangle-dual components; if \(d\) is a parity-polygon boundary
edge, it gives one. Every triangle now has a unique parent edge.

For a triangle with vertices \(a<b<c\), cyclically order its edges as

\[
(ab,\ bc,\ ca).
\]

Relative to the parent edge, select

- the predecessor for \((\epsilon=+,\text{ even sheet})\) or
  \((\epsilon=-,\text{ odd sheet})\);
- the successor for the two opposite combinations.

The marked edge is never selected. A selected internal edge is the parent edge of exactly one
child triangle, and that child cannot select it again. Therefore the selected edges are distinct
and their triangle incidence is a disjoint union of directed chains.

Reverse every chain and flip its scalar edges leaf-first. Different chains may be interleaved
arbitrarily.

### Why every flip becomes physical

The leaf edge of a chain is a parity-polygon boundary edge. Its opposite vertices consist of one
parity-sheet vertex and the intervening original-polygon vertex, so its flip is physical.

After that flip, the next edge in the reversed chain sees the newly exposed opposite-color
vertex. It therefore also flips to a physical edge. Induction up the chain proves the statement
for every selected edge. Edges in distinct chains are separated by unselected scalar edges, so
their legal flips commute.

There are \(m-2\) parity triangles and hence \(m-2\) selected edges. After all flips, the endpoint
\(E^\epsilon_{T,d}\) contains \(m-2\) pairwise noncrossing physical diagonals. They form a full
quadrangulation

\[
Q^\epsilon_{T,d}
=
\rho(E^\epsilon_{T,d}).
\]

The mark \(d\) remains scalar.

## Unique-sink property

Each physical replacement separates the quadrilateral created by its child-side flip from the
part of the chain closer to the abstract root. The alternating coorientation points across that
edge toward the root.

Thus every non-root quadrilateral has exactly one outgoing dual edge, while the quadrilateral
containing \(d\) has none. The directed dual tree has a unique sink, and \(d\) is one of its two
scalar diagonals:

\[
(Q^\epsilon_{T,d},d)
\in
\widetilde U_{2m}^{\epsilon}.
\]

This defines the direct map

\[
\Phi_\epsilon:
\widetilde Z_{2m}
\longrightarrow
\widetilde U_{2m}^{\epsilon}.
\]

## Explicit inverse

Start with a marked sink slot

\[
(Q,d)\in\widetilde U_{2m}^{\epsilon}.
\]

The mark determines one parity sheet. Every quadrilateral cell of \(Q\) has exactly one scalar
diagonal whose endpoints lie on that sheet. Add that diagonal in every cell. This gives a unique
marked scalar refinement

\[
E_\sigma(Q).
\]

Because an oriented tree with a unique sink has one outgoing edge at every non-sink vertex, each
non-sink quadrilateral has a unique parent edge pointing toward the sink. Cyclically order the
four boundary sides of that cell. Relative to its parent edge, choose the same predecessor or
successor prescribed in the direct construction.

If the chosen side is another physical edge of \(Q\), connect the parent edge to that child edge.
These connections form disjoint chains covering every physical edge of \(Q\). Flip each chain
from the sink outward, with arbitrary interleaving between chains. Each flip replaces a physical
edge by a scalar edge on the marked parity sheet.

The result is a zero-core triangulation \(T\) containing \(d\). The local predecessor/successor
rules are inverse at each triangle/quadrilateral pair, so the two constructions undo one another:

\[
\Psi_\epsilon\Phi_\epsilon=\operatorname{id},
\qquad
\Phi_\epsilon\Psi_\epsilon=\operatorname{id}.
\]

Therefore:

\[
\boxed{
\widetilde Z_{2m}
\simeq
\widetilde U_{2m}^{\epsilon}.
}
\]

## Counts

Every zero-core triangulation has \(2m-3\) marked diagonals, and every unique-sink
quadrangulation has two sink slots. The bijection gives

\[
|\widetilde Z_{2m}|
=
2(2m-3)C_{m-2},
\]

\[
|\widetilde U_{2m}^{\epsilon}|
=
2(2m-3)C_{m-2},
\]

and hence

\[
\boxed{
|U_{2m}^{\epsilon}|
=
(2m-3)C_{m-2}.
}
\]

For comparison, the total number of quadrangulations is the Fuss--Catalan number

\[
\frac{1}{2m-1}
\binom{3m-3}{m-1}.
\]

A full quadrangulation has \(m-1\) quadrilateral cells, each independently refined by one of its
two scalar diagonals, so every full physical core has

\[
\boxed{2^{m-1}}
\]

scalar triangulation refinements.

## Exact distance and unique closest endpoint

The direct path removes \(m-2\) scalar edges and inserts all \(m-2\) physical edges of \(Q\).
Thus its length is \(m-2\).

Any path from a zero-core source to a full-core triangulation must introduce \(m-2\) physical
diagonals, one per flip at best. Therefore

\[
\operatorname{dist}_d(T,Q)\geq m-2.
\]

The direct construction attains the bound:

\[
\boxed{
\operatorname{dist}_d(T,Q^\epsilon_{T,d})
=
m-2
=
\frac{n-4}{2}.
}
\]

Now fix a target slot \((Q,d)\). Any marked full-core refinement at this distance retains
\(m-1\) scalar edges from a zero-core source. Lemma 1 says those retained edges all lie on one
parity sheet, and \(d\) fixes which sheet. Hence every quadrilateral must be refined by the
same-color diagonal selected in \(E_\sigma(Q)\). The closest marked endpoint is unique.

Reversing its physical edges by the inverse chains then gives the unique zero-core source at
distance \(m-2\). Thus the earlier global minimum assignment is not additional structure:
it is exactly the direct Catalan bijection.

## Geodesics and the dependency poset

Let the direct flip chains have lengths

\[
\ell_1,\ldots,\ell_r,
\qquad
\sum_i\ell_i=m-2.
\]

A geodesic cannot use a temporary diagonal: it has exactly \(m-2\) steps and must replace each
source-only scalar edge by one target-only physical edge. Within a chain, the leaf-first order is
forced. Between different chains, every interleaving is legal.

Therefore the geodesics are exactly the linear extensions of the disjoint union of chains:

\[
\boxed{
|\operatorname{Geo}(T,d)|
=
\frac{(m-2)!}{\prod_i\ell_i!}.
}
\]

Two linear extensions differ by a scalar square move precisely when they exchange adjacent flips
from different chains. The linear-extension graph is connected by such adjacent exchanges.

This proves, at all arity, the coherence pattern observed numerically in entries 24 and 25. The
canonical route is the all-geodesic average

\[
\widehat\gamma^\epsilon_{T,d}
=
\frac{1}{|\operatorname{Geo}^\epsilon(T,d)|}
\sum_{\gamma\in\operatorname{Geo}^\epsilon(T,d)}
\gamma.
\]

One-step rotation exchanges the parity sheets and the two polarities. Consequently

\[
\widehat H_{{\rm ct},2m}
=
\sum_{(T,d)}-X_d
\left(
\widehat\gamma^+_{T,d}
-
\widehat\gamma^-_{T,d}
\right)
\]

has exact marked endpoint boundary and is deck odd:

\[
\partial\widehat H_{{\rm ct},2m}
=
K^+_{2m}-K^-_{2m},
\qquad
r\widehat H_{{\rm ct},2m}
=
-\widehat H_{{\rm ct},2m}.
\]

## Scalar zero-core coefficient

Every diagonal of a zero-core cell has the same shift sign because all its endpoints lie on one
parity sheet. There are \(2m-3\) such factors, an odd number. In the \(t^{2m-2}\) associated
grade, choosing the one extra power on a marked edge \(d\) gives coefficient

\[
-\sigma^{2m-2}=-1.
\]

Thus each marked zero-core source contributes

\[
-X_d.
\]

The scalar zero-core grade is therefore the coefficient-\(-1\) sum over
\(\widetilde Z_{2m}\).

## Vertex-local QTDS identity

Consider a QTDS quartic vertex with four consecutive odd momentum blocks

\[
A=[a,b),\qquad
B=[b,c),\qquad
C=[c,d),\qquad
D=[d,a).
\]

Write

\[
X_{ij}=K_{[i,j)}^2.
\]

When the first block starts on the plus sheet, the QTDS numerator is

\[
V_+
=
-2K_A\cdot K_C
=
X_{ac}+X_{bd}-X_{ad}-X_{bc}.
\]

When it starts on the minus sheet, the numerator is

\[
V_-
=
2K_{A+B+C}\cdot K_B
=
X_{ac}+X_{bd}-X_{ab}-X_{cd}.
\]

Because all four blocks have odd length, \(a,c\) have one color and \(b,d\) the other. Hence

\[
X_{ac},\qquad X_{bd}
\]

are exactly the two scalar diagonals of the quadrilateral.

The two negative terms are alternating physical boundary sides. A direct side-orientation check
shows:

> An internal physical side occurs with coefficient \(-1\) in exactly one endpoint vertex
> numerator, namely the source cell of its cooriented dual edge.

Original polygon sides have \(X=0\), so they do not alter the statement.

## All-arity QTDS contact theorem

A quadrangulation of the \(2m\)-gon has

\[
m-1
\]

quartic vertices and

\[
m-2
\]

physical propagators.

To obtain a polynomial degree-one contact from its QTDS term, every propagator denominator must
be selected once from the numerator product. The vertex-local identity says that a physical edge
can be selected only at the source of its directed dual edge.

Since each vertex factor is linear, all propagators can be selected simultaneously exactly when
no vertex sources more than one edge. For an oriented tree with one fewer edge than vertices,
this is equivalent to having one and only one sink.

If the sink is unique:

1. every non-sink vertex contributes its unique term \(-X_e\), cancelling its outgoing
   propagator;
2. the sink contributes either \(X_{ac}\) or \(X_{bd}\), its two scalar slots.

If the tree has more than one sink, some vertex has outdegree at least two and its linear
numerator cannot cancel both propagators. No contact term exists.

The cancellation supplies sign \((-1)^{m-2}\). The fixed diagram convention supplies
\((-1)^{m-1}\). Their product is \(-1\). Therefore

\[
\boxed{
\operatorname{Contact}^{\epsilon}_{2m}
=
-\sum_{Q\in U_{2m}^{\epsilon}}
\sum_{d\in\operatorname{Slot}_{\epsilon}(Q)}
X_d.
}
\]

Combining this with the Catalan bijection and the scalar coefficient gives the all-arity equality

\[
\boxed{
\operatorname{gr}^{\,\rm zero}_{R}A_{\rm scalar}
=
\operatorname{Contact}^{\epsilon}_{\rm QTDS}.
}
\]

This identifies diagram, marked diagonal, and coefficient. It is stronger than equality after
summing amplitudes.

## Exact finite certificates

The direct and inverse constructions have been enumerated through fourteen points:

| \(n\) | zero-core cells | marked sources | all quadrangulations | unique sinks per polarity | distance |
|---:|---:|---:|---:|---:|---:|
| 6 | 2 | 6 | 3 | 3 | 1 |
| 8 | 4 | 20 | 12 | 10 | 2 |
| 10 | 10 | 70 | 55 | 35 | 3 |
| 12 | 28 | 252 | 273 | 126 | 4 |
| 14 | 84 | 924 | 1,428 | 462 | 5 |

At fourteen points, the 924 route families have chain profiles

\[
(5),\ (4,1),\ (3,2),\ (3,1,1),\
(2,2,1),\ (2,1,1,1),\ (1,1,1,1,1),
\]

with the predicted multinomial geodesic counts

\[
1,\ 5,\ 10,\ 20,\ 30,\ 60,\ 120.
\]

An independent formal-planar expansion of every QTDS diagram agrees with every scalar sink
occurrence and coefficient through fourteen points. The vertex-local identity is separately
checked on every quartic presentation.

These computations are certificates and regression tests. The all-arity theorem follows from
the direct/inverse and vertex-cancellation arguments, not from extrapolating the finite table.

## Reproducible audits

Direct map, inverse, distance, and route posets:

    python research/nima/check_scalar_catalan_map.py

Independent full symbolic QTDS contact comparison:

    python research/nima/check_scalar_sink_qtds.py

Vertex-local planar identity and outgoing-edge typing:

    python research/nima/check_qtds_vertex_cancellation.py

The earlier ten- and twelve-point scripts remain useful as independent implementations of the
global assignment and compiled bitset constructions.

## What is now established

1. the all-arity classification and Catalan count of zero-core scalar cells;
2. a direct marked scalar-to-sink map;
3. an explicit inverse;
4. exact flip distance and unique closest endpoints;
5. the disjoint-chain dependency poset for every shortest route;
6. connected square coherence and canonical route averaging;
7. an all-arity deck-odd scalar contact chain;
8. the vertex-local QTDS numerator identity;
9. the all-arity unique-sink criterion for QTDS contacts;
10. occurrence-level and coefficient-level equality of scalar zero-core grade and QTDS contact
    sector.

## What is not established

1. the complete transfer over arbitrary nonempty parity cores;
2. a single chain map intertwining every core stratum and every cut;
3. the filtered scalar-to-Pochhammer/Cousin comparison;
4. the equality of the resulting worldsheet half-class with
   \((\operatorname{Pf}'A)^2\) at chain level;
5. identification of the chain dependency relations with the Jordan identity itself;
6. uniqueness of alternating coorientation among all unrestricted local coorientations at every
   arity.

## Decision

Promote:

> The zero-core associated grade of the scalar master and the contact sector of complete QTDS are
> canonically isomorphic at all even arity. Their isomorphism is a marked Catalan
> discrete-Morse transfer, not an amplitude-level reconstruction.

The next Nima target is forced:

> cut along an arbitrary partial physical core, tensor the direct Catalan transfer over its even
> polygonal regions, and determine whether these regional maps assemble into the complete
> core-filtered scalar-to-QTDS chain equivalence.

Forward update: entry 27 proves that the regional tensor product gives the complete
core-filtered scalar--QTDS equality at occurrence and coefficient level. What remains open is the
stronger assembly into one chain map compatible with the incidence maps between different cores,
followed by the filtered worldsheet comparison.
