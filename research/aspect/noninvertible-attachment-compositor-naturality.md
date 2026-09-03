# Noninvertible attachment-compositor naturality

## Question

Does validating compositor coherence on the maximal attachment groupoid suffice when the attachment category also contains one-way refinement, forgetting, or deletion morphisms?

## Claim boundary

This packet isolates a finite one-way naturality obstruction. It does not classify arbitrary noninvertible attachment categories or lax compositors.

## Attachment category with one-way transport

Let \(\mathcal A\) have objects \(0,1\), with

\[
\operatorname{End}(0)=C_2,
\qquad
\operatorname{End}(1)=C_2,
\qquad
\operatorname{Hom}(0,1)=C_2,
\qquad
\operatorname{Hom}(1,0)=\varnothing.
\]

Composition adds labels modulo two. The two arrows \(0\to1\) are noninvertible because no reverse arrow exists. The maximal subgroupoid therefore has two disconnected components, each with isotropy \(C_2\).

Take identity transport functors. A compositor still has invertible components

\[
c_{g,h,x}:x\to x,
\]

and must be natural with respect to every morphism, including noninvertible ones. For \(r:0\to1\), naturality requires

\[
r c_{g,h,0}=c_{g,h,1}r.
\]

In this fixture that equation forces equality of the two component labels.

## DPC cycle

### Governing conjecture

The full attachment category, not its maximal groupoid, is the domain of compositor naturality. Noninvertible morphisms impose one-way compatibility that can connect components invisible to groupoid-core tests. The mechanism is hard to vary because discarding those arrows removes the only equations relating their source and target components.

### Rivals

1. Coherence on the maximal attachment groupoid extends automatically to all attachment morphisms.
2. Noninvertible maps affect lift existence but cannot constrain invertible compositor components.
3. Objectwise cocycles and pentagons already imply naturality along refinement or forgetting maps.

### Risky consequences

A compositor can pass every normalization, local cocycle, pentagon, and maximal-groupoid naturality check while failing every one-way arrow. A component-constant replacement must repair full naturality without changing any objectwise cocycle.

### Falsification attempt

The checker uses \(G=C_2\), sets \(c_{1,1,0}=0\) and \(c_{1,1,1}=1\), and exhaustively tests the finite category. The table passes both local cocycles and every core arrow but fails both noninvertible arrows \(0\to1\). Setting both components to one repairs all naturality equations.

### Residual

The fixture uses identity functors and invertible compositor components. Lax attachment transport may admit noninvertible comparison cells and requires separate lax coherence tests.

### Disposition

All three rivals are rejected. Full-category naturality is provisionally retained as mandatory for pseudofunctorial attachment transport.

## Disposition

Restriction to the maximal groupoid is not conservative for compositor coherence. Noninvertible attachment morphisms carry comparison equations that groupoid-core validation cannot observe.
