# Connected-groupoid compositor naturality

## Question

Can all objectwise crossed-system equations hold while a compositor fails to define a natural transformation across attachment isomorphisms?

## Claim boundary

This packet isolates naturality in a finite connected groupoid. It does not treat noninvertible attachment morphisms.

## Finite connected attachment groupoid

Let the objects be \(0,1\). For every ordered pair \((x,y)\), let

\[
\operatorname{Hom}(x,y)=C_2.
\]

Write an arrow as \((x,y,a)\) with \(a\in C_2\), and compose labels by addition modulo two. This is connected and nonthin: each object has isotropy group \(C_2\), and each pair of distinct objects has two transport arrows.

Take \(G=C_2\) and let every transport functor \(F_g\) be the identity. A compositor component

\[
c_{g,h,x}:x\to x
\]

is then a bit. At each fixed object, choosing \(c_{1,1,x}\) arbitrarily satisfies the normalized local cocycle equation.

Naturality across \(u=(x,y,a)\) requires

\[
u c_{g,h,x}=c_{g,h,y}u.
\]

Because labels add modulo two, this equation reduces to

\[
c_{g,h,x}=c_{g,h,y}.
\]

Thus connected transport forces the compositor components to agree across objects even though each local crossed system is separately valid.

## DPC cycle

### Governing conjecture

Compositor naturality across inter-object attachment arrows is an independent coherence gate not recoverable from objectwise isotropy crossed systems. The mechanism is hard to vary: local equations never compare components at distinct objects, while naturality does exactly that.

### Rivals

1. Valid crossed systems at every object automatically assemble into a groupoid compositor.
2. Naturality need only be checked on isotropy loops; inter-object arrows add no constraint.
3. Componentwise pentagon equations detect every coherence defect.

### Risky consequences

A component table can satisfy normalization and every pentagon at both objects, and commute with every isotropy loop, yet fail on every inter-object arrow. Replacing it by a component-constant table must repair naturality without changing the local cocycle class.

### Falsification attempt

The checker sets \(c_{1,1,0}=0\) and \(c_{1,1,1}=1\). It exhaustively verifies both local cocycle systems and all componentwise pentagons. Naturality passes on all four isotropy arrows but fails on all four inter-object arrows. A constant nontrivial table \(c_{1,1,x}=1\) passes all local, pentagon, and naturality checks.

### Residual

The fixture has central isotropy and identity transport functors. Noncentral conjugacy under nonidentity functors requires the same naturality square with ordered composition, but is not mechanically tested here.

### Disposition

All three rivals are rejected. Inter-object naturality is retained as an independent mandatory gate for attachment-groupoid compositors.

## Disposition

Objectwise crossed systems are necessary but not sufficient. A lawful compositor must be a natural transformation across the full attachment groupoid; connected arrows enforce compatibility among local isotropy data.
