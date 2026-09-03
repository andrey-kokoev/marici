# Finite natural isomorphism preserves all matching fibers

## Question

Do naturality and componentwise invertibility suffice, in the finite two-probe model, to conjugate matching maps and preserve every matching fiber?

## Claim boundary

This packet proves a finite instance by exhaustive enumeration. It does not prove the general categorical theorem, global rewrite confluence, normalization, or physical equivalence.

## Presheaves

Use the full two-probe face system. The empty-face constraint is a singleton; each singleton-face constraint is \(\{0,1\}\). Let the source joint set be \(\{a,b,c\}\), with matching map

\[
a\mapsto(0,0),
\qquad b\mapsto(1,1),
\qquad c\mapsto(0,1).
\]

Let the target joint set be \(\{A,B,C\}\), with

\[
A\mapsto(0,0),
\qquad B\mapsto(1,1),
\qquad C\mapsto(1,0).
\]

Both presheaves are lawful because every further restriction to the empty face is unique.

## Natural isomorphism

On both singleton constraints use bit complementation. On joint constraints use

\[
a\mapsto B,
\qquad b\mapsto A,
\qquad c\mapsto C.
\]

Every component is bijective. The induced matching-object map is coordinatewise complementation:

\[
(x,y)\mapsto(1-x,1-y).
\]

Direct evaluation on all three joint sections proves

\[
\mu_G\alpha_{pq}=\alpha_M\mu_F.
\]

## Fiber census

Enumerate all four matching data. For each \(m\), the joint-component bijection restricts to a bijection

\[
\mu_F^{-1}(m)
\longrightarrow
\mu_G^{-1}(\alpha_M(m)).
\]

This includes the empty source fiber over \((1,0)\), which corresponds to the empty target fiber over \((0,1)\). Thus the statement preserves absence as well as nonzero multiplicity.

## Independent hostile mutations

1. Keep every comparison component bijective but alter one target restriction. A naturality square fails, and matching-map conjugacy fails.
2. Use a natural quotient between presheaves with singleton proper faces and collapse two joint sections to one. Naturality survives, but the joint component and induced fiber map are not invertible.

These mutations independently test the two hypotheses rather than treating “natural isomorphism” as an indivisible label.

## Disposition

In the finite model, naturality plus componentwise invertibility suffices for matching-map conjugacy and bijections on every fiber. Together with the two prior countermodels, this closes the finite local necessity-and-sufficiency audit. The general theorem remains a formalization target.
