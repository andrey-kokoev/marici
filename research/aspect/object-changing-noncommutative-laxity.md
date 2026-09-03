# Object-changing noncommutative laxity

## Question

Can an algebraically correct compositor-label calculation conceal an ill-typed whiskering when attachment functors move objects?

## Claim boundary

This packet treats a finite two-object groupoid with noncommutative labels and one object-swapping functor. Its cells are invertible; genuinely noninvertible object-changing comparisons remain outside the fixture.

## Typed attachment groupoid

Let objects be \(0,1\), with every hom-set labelled by \(S_3\). An arrow is

\[
(x,y,p),
\qquad p\in S_3,
\]

and composition is defined only when endpoints match, multiplying labels in order.

Let \(S\) swap the two objects and act on labels by the inner automorphism

\[
\alpha(p)=rpr^{-1}
\]

for a three-cycle \(r\). For the idempotent map label \(a^2=a\), assign \(F_a=S\). A lax compositor

\[
\mu:F_aF_a=\operatorname{Id}\Longrightarrow F_a=S
\]

has components

\[
\mu_x=(x,Sx,r).
\]

Naturality follows from \(\alpha(p)r=rp\).

## Typed associativity

For the triple \((a,a,a)\), both paths start at \(Sx\) and end at \(Sx\). One uses the left-whiskered component

\[
F_a(\mu_x):Sx\to x,
\]

and the other uses the right-whiskered component

\[
\mu_{F_a x}:Sx\to x.
\]

Their labels agree in this fixture, but their endpoints arise from different typed constructions. Composition is lawful only after those endpoints are checked.

## DPC cycle

### Governing conjecture

Object images and component endpoints are indispensable parts of noncommutative lax coherence; label algebra is only a projection. The mechanism is hard to vary because whiskering changes both the morphism label and its source and target.

### Rivals

1. Equality of noncommutative labels certifies equality of associativity paths.
2. Whiskering acts only on labels, so component endpoints may be copied unchanged.
3. If an untyped one-object reduction passes, the multi-object compositor is coherent.

### Risky consequences

A lawful object-swapping fixture must pass naturality and typed associativity. Replacing a whiskered arrow by one with the same label but copied unwhiskered endpoints must preserve every label-only equation while making a required composition undefined.

### Falsification attempt

The checker exhaustively tests naturality for all 24 attachment arrows and both objects. It constructs both associativity paths and verifies endpoint and label equality. It then injects a fake left-whiskered component with the correct label but endpoints \(x\to Sx\) instead of \(Sx\to x\). Label multiplication still predicts the accepted value, while typed composition rejects the path.

### Residual

The fixture has invertible comparison cells and a groupoid with every cross-object hom-set nonempty. Sparse categories and noninvertible cells can introduce additional existence failures.

### Disposition

All three rivals are rejected. Full arrow typing before label comparison is provisionally retained as mandatory.

## Disposition

The forgetful projection from typed attachment arrows to algebraic labels is not faithful for coherence validation. Every whiskered component must retain its object-level source and target.
