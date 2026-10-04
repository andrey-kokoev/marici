# Iteration 2: marked triangle completion and its relative universal property

## Question

Can the graded construction preserve explicitly marked simplex data while completing and rotating a triangle? Iteration 1 recovered total packages, but its homotopy moved an upper endpoint. The present obligation is stronger: keep all supplied vertices and two edges fixed.

SCC obligations: forward realization and route/coherencer compatibility. The source is Cubical identity paths in an arbitrary type A. These paths have inverses; outer-horn completion is not thereby established for arbitrary noninvertible arrows in the earlier K record.

## Test and rivals

- Conjecture: the missing edge and face witness of a marked path triangle form a contractible completion space, whichever edge is missing. The realization has a universal property over the marked horn.
- Rival 1: completion requires moving supplied vertices or edges.
- Rival 2: agreeing on the return edge identifies the full retained triangle.
- Rival 3: a result about a missing edge also fills every fully fixed triangular boundary.
- Tests: prove recovery over the same horn and dependent interpretation-extension uniqueness; exhibit two distinct filled triangles with the same diagonal; exhibit a fully fixed boundary that cannot fill.

## Triangle and three partial boundaries

For marked vertices x,y,z and edges p:x=y, q:y=z, r:x=z, define

\[
\operatorname{Triangle}(p,q,r)=(p\mathbin{\cdot}q=r).
\]

The dot here is Cubical path concatenation, first p then q. A face witness compares the two-edge route with the diagonal. The three completion types are

\[
H_{02}(p,q)=\sum_{r:x=z}(p\mathbin{\cdot}q=r),
\]
\[
H_{12}(p,r)=\sum_{q:y=z}(p\mathbin{\cdot}q=r),
\]
\[
H_{01}(q,r)=\sum_{p:x=y}(p\mathbin{\cdot}q=r).
\]

Agda proves all three contractible. For the missing diagonal the center is (p dot q,refl). For the other two, path concatenation by the supplied invertible edge is an equivalence, so its fiber at the supplied diagonal is contractible. No set-truncation assumption on A is used.

The two supplied edges and all vertices are parameters of each theorem: they are not changed by the contraction.

## Rotate the same face witness

The module constructs equivalences

\[
\operatorname{Triangle}(p,q,r)\simeq(q=p^{-1}\mathbin{\cdot}r),
\qquad
\operatorname{Triangle}(p,q,r)\simeq(p=r\mathbin{\cdot}q^{-1}),
\]

and a cyclic change of viewpoint

\[
\operatorname{Triangle}(p,q,r)
\simeq
\operatorname{Triangle}(q,r^{-1},p^{-1}).
\]

The vertices change order from (x,y,z) to (y,z,x), with the required edge reversals. This transports the actual face witness, and `rotation-recovery` proves that the inverse equivalence recovers it. The code does not replace the witness by a Boolean existence test. Three successive forward rotations and their higher coherence have not yet been compared with identity.

## Universal property over the retained horn

Let H be the type of marked vertices with the two composable edges p,q. Let C(h) be its missing-diagonal completion type, and define

\[
T=\sum_{h:H}C(h),\qquad \pi:T\to H.
\]

Canonical completion s:H -> T is a section of pi. The recovery homotopy from s(pi(t)) to t keeps the whole horn fixed. `horn-fixed` proves its projection is the constant path.

For every dependent interpretation family Y:H -> Type, the formal result is

\[
\left(\prod_{t:T}Y(\pi(t))\right)
\simeq
\left(\prod_{h:H}Y(h)\right).
\]

It restricts a section along s and extends a section along pi. For a specified section f of Y, the space

\[
\sum_g(g\circ s=f)
\]

is contractible. This is a boundary-relative universal property: it keeps the supplied horn's types and data fixed, rather than only recovering the starting answer under an unmarked equivalence.

Constant Y recovers the ordinary mapping-out universal property. No additional primitive is needed for the dependent version.

## Connection to the previous grade-two filler

With p,q,r retained as parameters, the globular boundary has endpoints p dot q and r, both paths from x to z. Its grade-two filler type is definitionally the triangle face type. `globular-filler-equivalence` is the identity equivalence on that fiber.

The intermediate vertex and factorization p,q must still be retained. This fiber equivalence does not identify the complete triangle boundary with just its diagonal or composite route.

## Hostiles that retain the path

At the three fixed vertices Bool,Bool,Bool in the universe of types, let u be the univalent path induced by Boolean negation. Two filled triangles are:

- ordinary: edges (refl,refl,refl), with the path-cancellation face;
- twisted: edges (u,u inverse,refl), with the path-cancellation face.

Both have literally the same diagonal refl. Their first edges are distinct, as proved in iteration 1 by transporting false. `different-factorizations` proves that the marked triangles are distinct, and `no-diagonal-recovery` rules out a decoder from the diagonal recovering every marked triangle.

The fully fixed edges (refl,refl,u) have no face filler. `unfillable-triangle` proves this. Thus contractible horn completion neither fills an arbitrary full boundary nor erases the chosen factorization.

The negative module `MarkedTriangleBadErasure` attempts to identify the effects of the ordinary and twisted first edges on false by reflexivity. It must reject with the false/true unequal-term diagnostic.

## Verification

Formal root: `agda/MarkedTriangleCoherence.agda`.

```powershell
pwsh -NoProfile -File research/nima/checkers/check_graded_boundary_coherence.ps1 -Module MarkedTriangleCoherence -ReceiptStem marked-triangle-coherence -NegativeModules MarkedTriangleBadErasure
```

The existing headless runner now accepts a proof root and named rejection modules; its default invocation still checks iteration 1. All compiler launches retain `-NoNewWindow`. Both iteration 1 and iteration 2 were freshly rechecked after generalization of the runner.

`checkers/agda_receipt_audit.py` verifies compiler hashes, the complete Cubical source inventory, and the local import closure of the proof root and rejection controls. Owner-local inputs are not inferred from a count of tests.

Receipt: `results/marked-triangle-coherence-formal-audit.json`.
Source-bound audit: `checkers/check_marked_triangle_coherence.py`.

## Disposition and next executable test

Triangle horn completion, witness-preserving cyclic rotation, and dependent interpretation-extension uniqueness over the retained horn are proved. Equal diagonals do not identify retained factorizations; fully fixed boundaries need not fill.

Next: assemble a marked tetrahedral boundary from four triangle faces. Compare its two composed face-witness routes, retain their difference, and determine which missing-face completion has a relative universal property. Rotation recovery is already available; any proposed multi-rotation closure needs its own higher witness rather than assuming the permutation of edge labels proves it.
