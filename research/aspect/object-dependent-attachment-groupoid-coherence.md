# Object-dependent attachment-groupoid coherence

## Question

What data are lost when attachment coherence is reduced to the automorphism group of one representing object?

## Claim boundary

This packet treats invertible attachment morphisms. It does not reduce general attachment categories with noninvertible refinement or deletion maps to groupoids.

## Weak action on an attachment groupoid

Let \(\mathcal A\) be the attachment groupoid and \(G\) a group of system-map labels. Coherent transport is a pseudofunctor

\[
BG\longrightarrow\mathbf{Grpd}.
\]

It consists of equivalences

\[
F_g:\mathcal A\to\mathcal A
\]

and natural isomorphisms

\[
c_{g,h}:F_gF_h\Rightarrow F_{gh}.
\]

For each attachment \(x\), the component is typed

\[
c_{g,h,x}:F_g(F_h(x))\longrightarrow F_{gh}(x).
\]

Naturality requires, for every attachment isomorphism \(u:x\to y\),

\[
F_{gh}(u)c_{g,h,x}
=
c_{g,h,y}F_gF_h(u).
\]

The pentagon is an equality of component arrows with the same typed source and target. These object maps and naturality squares are absent from a one-object crossed system.

## Structural decomposition

A groupoid is equivalent to a disjoint union of isotropy groups, one per connected component. A weak action can permute components. After representatives and connecting arrows are chosen, isotropy crossed systems describe within-component automorphisms, but they must be supplemented by:

- the induced action on connected components;
- transport between chosen component representatives;
- conjugacy compatibility with connecting arrows;
- compositor naturality and pentagon cells.

Thus isotropy data are a local projection, not a faithful coordinate for the full groupoid action.

## DPC cycle

### Governing conjecture

A weak attachment-groupoid action is determined only by the combined component permutation, object transport, isotropy action, and natural compositor cells. The mechanism is hard to vary because compositor components cannot even be typed until the object images under both composite functors are known.

### Rivals

1. Crossed systems on object isotropy groups determine the complete weak action.
2. Object permutations are presentation artifacts removable without changing transport.
3. Checking the pentagon on isotropy automorphisms suffices; component typing and naturality add no independent gate.

### Risky consequences

Two actions with identical trivial isotropy data can differ by a nontrivial component swap. On a discrete attachment groupoid, a compositor component exists only when the two object maps agree exactly. A deliberately malformed object map can pass all vacuous isotropy checks while failing equivalence and compositor typing.

### Falsification attempt

The checker uses the discrete two-object groupoid and \(G=C_2\). The trivial action and swap action have identical trivial isotropy groups, but different component permutations. The swap squares to identity and satisfies all strict unit and pentagon equations. A collapse map sending both objects to one object retains vacuous isotropy tables but is not an equivalence and fails the required object-map composition equation.

### Residual

The discrete fixture has no inter-object arrows, so its naturality equations are vacuous. The packet states the general naturality gate, but a connected nonthin fixture is needed to test conjugacy transport mechanically.

### Disposition

All three rivals are rejected at the object/component gate. The combined groupoid pseudofunctor datum is provisionally retained; connected-arrow naturality remains a separately stated residual.

## Disposition

One-object nonabelian cohomology is sound only after choosing and preserving a component. General attachment transport requires the entire groupoid pseudofunctor. Isotropy-only analysis can erase nontrivial motion among inequivalent attachment components and can accept untypable compositor claims.
