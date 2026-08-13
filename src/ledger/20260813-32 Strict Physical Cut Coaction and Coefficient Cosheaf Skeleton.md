# Strict Physical Cut Coaction and the Coefficient Cosheaf Skeleton

## Record

Date: 2026-08-13

Status: the physical-core incidence maps of the scalar/QTDS occurrence system are canonical,
strictly order independent, and deck-equivariant at all even arity.

For a directed unique-sink QTDS tree, cutting an edge creates a new component whose sink is the
source quadrilateral of that edge. The new sink contributes either of its two scalar diagonal
slots. This defines an explicit two-term Gysin/coaction map with coefficient

\[
-\frac{X_{\rm slot}}{X_e}.
\]

Iterated cuts satisfy a closed product formula. Hence the physical directions of the coefficient
cosheaf are constructed. What remains is extension across the scalar associahedral directions
of entry 31 and the filtered twisted-chain realization.

## Directed unique-sink trees

Let \(Q\) be a full quadrangulation and \(\Gamma_Q^\epsilon\) its dual tree, directed by the
alternating coorientation on polarity sheet \(\epsilon\).

Suppose \(\Gamma_Q^\epsilon\) has a unique sink \(s\). Since the underlying graph is a tree,
every other vertex has exactly one outgoing edge and every directed path ends at \(s\). Thus
\(\Gamma_Q^\epsilon\) is an arborescence toward \(s\).

A sink quadrilateral

\[
v=(a,b,c,d)
\]

has two scalar slots

\[
d_v^0=(a,c),
\qquad
d_v^1=(b,d).
\]

A zero-core QTDS occurrence is the data

\[
(Q,s,d_s^\sigma),
\qquad
\sigma\in\{0,1\},
\]

with weight

\[
-X_{d_s^\sigma}.
\]

Entry 26 identifies these occurrences bijectively with marked zero-core scalar triangulations.

## Cutting one physical edge

Let

\[
e:u\longrightarrow v
\]

be an oriented edge of \(\Gamma_Q^\epsilon\). Delete \(e\).

The component containing \(v\) retains its old sink. In the component containing \(u\), every
remaining directed path that formerly exited through \(e\) now terminates at \(u\). Therefore
\(u\) is the unique new sink.

If \(P\subset Q\) is the set of already cut or retained physical edges, define the elementary
coaction

\[
G_e:
\mathcal L(P)
\longrightarrow
\mathcal L(P\cup\{e\})
\]

on an occurrence by

\[
\boxed{
G_e[Q,P;\mathbf d]
=
-\frac{1}{X_e}
\sum_{\sigma=0}^{1}
X_{d_u^\sigma}
[Q,P\cup\{e\};\mathbf d\cup d_u^\sigma].
}
\]

All old component marks are preserved. The only new datum is the slot choice at the source
quadrilateral \(u\).

This is the physical facet map anticipated after entry 31.

## Arbitrary cut set

Let \(P\subset Q\). For every \(e\in P\), write

\[
e:u_e\longrightarrow v_e.
\]

Distinct cut edges have distinct sources because every nonsink vertex of the arborescence has
only one outgoing edge.

After deleting all of \(P\), the component sinks are exactly

\[
\boxed{
\{s\}\cup\{u_e:e\in P\}.
}
\]

Starting with a fixed global sink slot \(d_s^\tau\), the complete occurrence expansion is

\[
\boxed{
G_P[Q,s,d_s^\tau]
=
\frac{(-1)^{|P|}}{\prod_{e\in P}X_e}
\sum_{\sigma:P\to\{0,1\}}
\left(
\prod_{e\in P}X_{d_{u_e}^{\sigma(e)}}
\right)
[Q,P;d_s^\tau,(d_{u_e}^{\sigma(e)})_{e\in P}].
}
\]

Including the initial coefficient \(-X_{d_s^\tau}\), each term has weight

\[
\boxed{
(-1)^{|P|+1}
\frac{
X_{d_s^\tau}
\prod_{e\in P}X_{d_{u_e}^{\sigma(e)}}
}{
\prod_{e\in P}X_e
}.
}
\]

This is exactly the occurrence-level coefficient of entry 27:

- one denominator for every retained physical edge;
- one marked scalar numerator for every forest component;
- sign \((-1)^{|P|+1}\).

## Strict order independence

The closed formula is a product over cut edges. Slot choices and Laurent multipliers belonging
to distinct edges are independent. Therefore for any two available cuts,

\[
\boxed{
G_eG_f=G_fG_e.
}
\]

More generally, for every ordering \(\pi\) of \(P\),

\[
G_{\pi(|P|)}\cdots G_{\pi(1)}
=
G_P.
\]

This is strict equality of occurrence-valued Laurent expressions, not equality only after
summing diagrams or collecting monomials.

The physical-core Boolean lattice is therefore represented by a strict cubical cosheaf.

## The physical coefficient cosheaf

For a partial core \(P\), define

\[
\mathcal L_{\rm phys}(P)
=
\bigoplus_{Q\supseteq P}
\bigotimes_{C\in\pi_0(\Gamma_Q\setminus P)}
\operatorname{span}
\{d_C^0,d_C^1\},
\]

restricted to directed forests with one sink in every component.

The maps \(G_e\) above make

\[
P\longmapsto\mathcal L_{\rm phys}(P)
\]

a strict functor on physical-core inclusions. Its Laurent augmentation is

\[
\operatorname{wt}
[Q,P;(d_C)]
=
(-1)^{|P|+1}
\frac{\prod_C X_{d_C}}{\prod_{e\in P}X_e}.
\]

Entry 27 proves a regional marked Catalan bijection

\[
\Phi_{\epsilon,P}
\]

between this basis and the product of marked zero-core scalar bases in the regions cut out by
\(P\). Transporting the \(G_e\) maps through \(\Phi_{\epsilon,P}\) gives the physical incidence
maps on the scalar occurrence modules.

Thus the physical-core part of the desired coefficient cosheaf is no longer conjectural.

## Relation to factorization

Deleting \(P\) splits the directed tree into \(|P|+1\) components. The coaction makes those
components explicit before coefficient augmentation.

On the scalar side, the same map creates one new regional marked contact whenever a physical
edge splits a region. On the QTDS side, the new contact is the two-slot sum at the newly created
sink.

The formula therefore refines fixed-core monoidality to a map between neighboring cores:

\[
\mathcal L_{\rm phys}(P)
\xrightarrow{G_e}
\mathcal L_{\rm phys}(P\cup\{e\}).
\]

This is the occurrence-level factorization map that entry 27 did not yet possess.

## Deck covariance

One-step rotation \(\rho\) exchanges the two alternating coorientations. It rotates:

- the quadrangulation;
- every directed edge source and target;
- every cut core;
- every sink quadrilateral;
- both scalar slots;
- every Laurent variable.

The exact relation is

\[
\boxed{
\rho G_e^+
=
G_{\rho e}^-\rho.
}
\]

Consequently

\[
\rho G_P^+
=
G_{\rho P}^-\rho.
\]

No absolute choice of polarity is required.

## Exact finite certificate

The number of initial marked unique-sink occurrences is

\[
2,\ 6,\ 20,\ 70,\ 252
\]

at \(n=4,6,8,10,12\), respectively. These equal both:

\[
\binom{n-2}{n/2-1}
\]

and the number of marked zero-core scalar triangulations.

At twelve points, where a full quadrangulation has four edges, the audit finds:

| cut rank \(p\) | marked starting records | terms per expansion |
|---:|---:|---:|
| 0 | 252 | 1 |
| 1 | 1,008 | 2 |
| 2 | 1,512 | 4 |
| 3 | 1,008 | 8 |
| 4 | 252 | 16 |

The record count is

\[
252\binom{4}{p},
\]

and each expansion has \(2^p\) distinct marked occurrences.

For every record the script compares every cut permutation with the closed product formula and
then rotates the complete Laurent-decorated occurrence expansion to the opposite sheet.

Run:

    python -B research/nima/check_qtds_cut_coaction.py

The proof is the arborescence argument; the computation exhaustively checks all examples through
twelve points.

## What this solves

1. every physical cut has a canonical occurrence-level map;
2. the new component sink is intrinsic;
3. the two new scalar slots are intrinsic;
4. the Laurent multiplier is \(-X_{\rm slot}/X_e\);
5. arbitrary cuts have a closed product formula;
6. all physical-cut orders commute strictly;
7. the weights reproduce the complete core-filtered theorem;
8. the maps transport to scalar regional occurrence modules;
9. the construction is deck-equivariant;
10. physical-core factorization naturality holds at occurrence level.

## What it does not solve

The full envelope of entry 31 has both physical and scalar facets. This entry constructs only the
physical-core direction.

It does not yet provide:

1. coefficient transport along scalar-refinement facets;
2. compatibility between scalar and physical facet maps;
3. a cellular map on a pentagon or higher associahedron;
4. loaded Pochhammer/current representatives;
5. the filtered Cousin comparison;
6. acyclicity of the comparison kernel;
7. a chain representative of \((\operatorname{Pf}'A)^2\).

The strict physical cubes are necessary but not sufficient for the full half-object.

## The universal mixed prism

The smallest unresolved compatibility is

\[
K_2\times I.
\]

Its \(I\)-direction is now governed by \(G_e\). Its \(K_2\)-direction is the scalar pentagon
homotopy carried by the marked associahedral envelope.

The missing square asks whether the physical coaction is natural with respect to scalar
refinement. Schematically, the required Beck--Chevalley relation is

\[
\boxed{
G_e\,h_{\rm scalar}
-
h_{\rm split}\,G_e
=
\partial H_e+H_e\partial,
}
\]

where:

- \(h_{\rm scalar}\) is the parent-region pentagon transport;
- \(h_{\rm split}\) is the product transport on the two cut regions;
- \(H_e\) is the mixed square cell.

At the scalar presentation level \(H_e\) is already an actual face by entry 31. The remaining
task is to define its coefficient/current image.

## Primary next test

Construct the scalar-refinement action on the occurrence modules, first on the universal
pentagon. Then evaluate the two routes around the forced mixed square using the explicit
\(G_e\) above.

There are two possible outcomes:

1. the route difference is the boundary of a canonical loaded square current, extending
   \(\mathcal L_{\rm phys}\) to the full associahedral envelope;
2. the route difference gives a nonzero residue-free class, the first genuine obstruction to
   \(\mathsf J\) as an intrinsic chain-level half-object.

This is now a bounded local test. Global factorization combinatorics and physical cut ordering
are no longer part of the uncertainty.

## Decision

Promote:

> The core-filtered scalar/QTDS occurrence system carries a strict,
> deck-equivariant physical cut coaction. Cutting \(e:u\to v\) creates the source
> quadrilateral \(u\) as a new sink and multiplies by the two-term factor
> \(-\bigl(X_{d_u^0}+X_{d_u^1}\bigr)/X_e\).

The remaining coefficient problem is precisely the mixed naturality of this coaction with the
scalar associahedral refinement, beginning with the universal pentagonal prism.
