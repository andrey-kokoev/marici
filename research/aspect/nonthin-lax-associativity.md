# Nonthin lax associativity

## Question

Can every lax compositor component exist and be natural while the associativity coherence equation still fails?

## Claim boundary

This packet isolates equality of parallel lax composites in a finite one-object nonthin category. It does not model object-changing attachment functors.

## Nonthin attachment category

Take the one-object category whose endomorphism monoid is

\[
A=\{0,1\},
\qquad
p\circ q=\max(p,q).
\]

The identity is \(0\), while \(1\) is idempotent and noninvertible. The category is nonthin because it has two parallel endomorphisms of its sole object.

Let map labels form \(C_3\), and assign every label the identity attachment functor. A normalized lax compositor is then a table

\[
\mu(g,h)\in A,
\qquad
\mu(0,g)=\mu(g,0)=0.
\]

Every table entry is a well-typed natural transformation: the monoid is commutative, so naturality with every attachment endomorphism holds. Associativity nevertheless requires

\[
\max(\mu(g,h),\mu(g+h,k))
=
\max(\mu(h,k),\mu(g,h+k))
\]

for every triple modulo three.

## DPC cycle

### Governing conjecture

In a nonthin attachment category, existence and naturality of lax comparison components do not determine coherence; equality of the two associativity composites is an independent gate. The mechanism is hard to vary because nonthin hom-sets contain distinct parallel arrows with identical endpoints.

### Rivals

1. Once all compositor components exist and are natural, associativity follows.
2. Typing both associativity paths with common endpoints is sufficient, as in a preorder.
3. Pairwise compositor checks can replace exhaustive triple coherence.

### Risky consequences

A normalized table must exist whose every component is natural and whose two associativity paths are always typed, yet whose path labels disagree on explicit triples. A zero table must pass the same typing and naturality checks while satisfying every triple.

### Falsification attempt

The checker exhaustively tests all 27 triples. The bad table has \(\mu(1,1)=1\) and every other normalized entry zero. All components exist, are natural, and include a noninvertible cell, but four associativity equations fail. The zero table has no failures.

### Residual

All functors are identities and the endomorphism monoid is commutative. Noncommutative whiskering and object-changing functors require the general ordered associativity formula.

### Disposition

All three rivals are rejected. Explicit equality of associativity composites is retained as mandatory in nonthin attachment semantics.

## Disposition

Preorder fixtures certify only comparison existence and direction. They cannot certify the 2-cell equality required for lax associativity when parallel attachment morphisms are distinguishable.
