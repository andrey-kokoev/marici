# Internal boundary groupoids versus external occurrence actions

## Question

How do matching limits change when occurrence exchange is a morphism inside the boundary index rather than an external automorphism of a discrete occurrence presentation?

## Claim boundary

This packet computes finite `Set`-valued limits for three index types. It does not treat homotopy limits, stacks, gauge reduction, or physical indistinguishability.

## Discrete repeated occurrences

Let \(X=\{0,1\}\). For a discrete boundary index with two occurrences, both carrying \(X\), the matching object is

\[
M_{\rm disc}=X\times X,
\]

with four elements. An external swap of the two occurrences acts on this product. It does not impose an equation in the limit.

The external fixed-point subset is the diagonal

\[
M_{\rm disc}^{S_2}=\{(0,0),(1,1)\},
\]

while the orbit quotient has three elements.

## Walking internal isomorphism

Now put an isomorphism \(u:p_1\to p_2\) and its inverse inside the boundary index. Let the diagram map carried by \(u\) be bit complementation

\[
f(0)=1,
\qquad f(1)=0.
\]

A limiting family must satisfy

\[
x_2=f(x_1).
\]

Hence the matching object is the anti-diagonal

\[
M_{\rm iso}=\{(0,1),(1,0)\}.
\]

It has the same cardinality as the external fixed-point subset but is a different subobject of \(X^2\). Equal cardinality therefore cannot identify the two constructions.

If the internal isomorphism is carried by the identity map instead, the internal limit is the diagonal. Even then, its equality with the external fixed subset follows from the chosen diagram map; it is not a general identification of internal and external symmetry.

## Internal loop group

For a one-object index groupoid \(BS_2\), a diagram is an \(S_2\)-set. Its ordinary limit is the fixed-point set of the internal action. With the nontrivial flip action on \(X\), the limit is empty. With the trivial action, it is all of \(X\).

Thus internal morphisms contribute compatibility equations to the limit. External automorphisms act on an already constructed limit. Orbit quotienting is a third operation performed after an action is present.

## Required discriminator

A boundary certificate must declare its index kind and maps:

1. `discrete_occurrences_with_external_action`;
2. `internal_groupoid_diagram`;
3. `authorized_orbit_quotient`.

The first yields an action on matching data, the second changes the matching limit through coherence equations, and the third discards distinctions through a separately authorized quotient. No cardinality test can recover which constructor was used.

## Hostile identification

The anti-diagonal internal limit and diagonal external fixed subset both have cardinality two. A classifier using only cardinality reports them equal, but their intersection is empty. This is a source-identity failure, not a harmless coordinate convention.

## Disposition

Internal boundary groupoids, external occurrence actions, fixed points, and orbit quotients are distinct typed constructions. SCC certificates must record the boundary index and diagram maps before computing matching data or applying symmetry operations.
