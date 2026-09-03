# Finite action-groupoid rewrite equivalence criterion

## Question

Which finite data suffice for a probe rewrite to preserve a symmetry-retaining matching action groupoid, and which orbit or stabilizer checks are consequences rather than independent assumptions?

## Claim boundary

This packet treats finite group actions and their ordinary action groupoids. It does not construct groupoid-valued matching objects, homotopy limits, stacks, gauge equivalence, or physical symmetries.

## Presentation-preserving criterion

Let a finite group \(G\) act on matching set \(M\), and let \(H\) act on \(N\). Suppose there are:

1. a group isomorphism \(\varphi:G\to H\);
2. a bijection \(f:M\to N\);
3. equivariance

\[
f(g\cdot m)=\varphi(g)\cdot f(m).
\]

Then define a functor between action groupoids by

\[
m\mapsto f(m),
\qquad
(g:m\to g\cdot m)\mapsto
(\varphi(g):f(m)\to f(g\cdot m)).
\]

The inverse group and set maps define its inverse functor. This is an isomorphism of the presented action groupoids, stronger than abstract categorical equivalence.

For every pair \(m,m'\), equivariance and bijectivity give a bijection

\[
\{g\in G\mid g\cdot m=m'\}
\longrightarrow
\{h\in H\mid h\cdot f(m)=f(m')\}.
\]

Thus the functor is fully faithful and essentially surjective.

## Redundant checks

Under the three core conditions:

- orbit transport follows: \(f(G\cdot m)=H\cdot f(m)\);
- stabilizer transport follows:

\[
\varphi(\operatorname{Stab}_G(m))
=
\operatorname{Stab}_H(f(m)).
\]

Orbit bijection and stabilizer conjugacy are therefore derived verification checks, not additional premises for a presentation-preserving certificate.

## Abstract-equivalence boundary

For finite action groupoids viewed without their presentations, equivalence is weaker. Each connected component is equivalent to the one-object groupoid of a representative stabilizer. Consequently, a component bijection plus isomorphisms of representative stabilizer groups characterizes abstract equivalence. It need not recover an isomorphism of the ambient acting groups or an equivariant bijection of the original action sets.

SCC should use the stronger criterion when a rewrite claims to transport declared occurrence actions. The weaker criterion must be typed as abstract groupoid equivalence.

## Finite witness

Take coordinate swap by \(S_2\) on \(\{0,1\}^2\). Relabel the target group generator and all four matching points. The induced maps satisfy equivariance, map every action-groupoid hom-set bijectively, transport all three orbits, and reproduce stabilizer orders \([2,2,1]\).

## Hostile same-orbit-count fixture

The trivial \(S_2\)-action on three points also has three orbits, but stabilizer profile \([2,2,2]\). No component matching can preserve all stabilizer groups, so the action groupoids are not abstractly equivalent. Equal orbit count is insufficient even for the weaker criterion.

## Disposition

For presentation-preserving finite rewrites, group isomorphism plus equivariant matching-set bijection is sufficient; orbit and stabilizer transport are consequences. Abstract action-groupoid equivalence is weaker and must not be promoted to preservation of a declared group action.
