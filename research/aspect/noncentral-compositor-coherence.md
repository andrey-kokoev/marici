# Noncentral compositor coherence

## Question

What replaces ordinary second cohomology when attachment automorphisms are nonabelian and compositor twists are noncentral?

## Claim boundary

This packet treats a group of system-map labels and a fixed nonabelian attachment automorphism group. It classifies weak actions up to change of representatives; it does not assert that every attachment category reduces to a one-object groupoid.

## Crossed coherence datum

Let \(G\) be the composition group and \(A\) the automorphism group of a representing attachment. Noncentral coherence is not specified by a two-cochain alone. It requires a pair

\[
\alpha_g\in\operatorname{Aut}(A),
\qquad
c(g,h)\in A.
\]

The action closes only up to the compositor:

\[
\alpha_g\alpha_h
=
\operatorname{Inn}(c(g,h))\alpha_{gh}.
\]

Associativity requires the ordered twisted cocycle equation

\[
c(g,h)c(gh,k)
=
\alpha_g(c(h,k))c(g,hk).
\]

Normalization fixes \(\alpha_e=\operatorname{id}\) and \(c(e,g)=c(g,e)=1\).

A normalized representative change \(b_g\in A\) acts on both fields:

\[
\alpha'_g=
\operatorname{Inn}(b_g)\alpha_g,
\]

\[
c'(g,h)=
b_g\alpha_g(b_h)c(g,h)b_{gh}^{-1}.
\]

Therefore the invariant is the pointed nonabelian cohomology set of crossed systems, not an abelian quotient group formed from compositor values alone.

## DPC cycle

### Governing conjecture

The pair \((\alpha,c)\), subject to both action-compatibility and twisted associativity and quotiented by simultaneous gauge, is the minimal complete coherence datum. The mechanism is hard to vary because noncentral compositors alter the action by inner automorphisms, so an independent fixed action is not preserved under representative changes.

### Rivals

1. The twisted cocycle equation for \(c\) alone suffices.
2. One may fix \(\alpha\) and gauge only \(c\), as in central ordinary \(H^2\).
3. A nonidentity raw compositor is itself an invariant obstruction to strictification.

### Risky consequences

The conjecture predicts a two-cochain that passes every associativity equation but fails action compatibility; a gauge transform of a strict system that produces nonidentity \(c\) while remaining equivalent to the strict system; and sensitivity to multiplication order.

### Falsification attempt

The finite checker uses \(G=C_2\) and \(A=S_3\). With trivial \(\alpha\), setting \(c(1,1)\) to a transposition passes the twisted cocycle equation but fails \(\alpha_1^2=\operatorname{Inn}(c(1,1))\). Separately, gauging the strict system by a three-cycle produces a nonidentity compositor and an inner action; exhaustive equations still pass and inverse gauge returns the strict system.

### Residual

The fixture covers one-object groupoids and finite groups. General attachment categories require object-dependent automorphism groupoids and modifications between pseudofunctors.

### Disposition

All three rivals are rejected. The crossed pair with simultaneous gauge is provisionally retained as the noncentral coherence object.

## Consequence for attachment transport

A noncentral compositor value cannot be interpreted independently of its induced action on attachment automorphisms. Ordinary \(H^2(G,A)\) applies only after centrality or an abelian coefficient structure makes inner-action coupling disappear. Strictification means gauge equivalence to \((\operatorname{id},1)\), not literal equality of a chosen compositor table.

## Disposition

Noncentral attachment coherence is controlled by crossed weak actions. Both equations are mandatory, and gauge acts on the action and compositor together.
