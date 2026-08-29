# Conditioned constructors form an enriched reachability-requirement bifibration

Owner: marici.Kitaev

## Question

What categorical structure is shared by conditioned constructor pullback,
controllability and observability, Fisher geometry, weakest preconditions,
descent, renormalization, error correction, Schur elimination, and viability?

## Claim boundary

The common object is best modeled as a resource-enriched indexed category with
two variances.

Let \(\mathcal K\) be the authorized constructor category. Over each object
\(X\), place a fibre whose objects retain:

- a reachable or admissible subobject \(S\hookrightarrow X\);
- a quantitative requirement on \(S\);
- its metric, resource, fault, and completion data.

A constructor \(f:X\to Y\) acts covariantly on reachable subobjects,

\[
f_!:\operatorname{Reach}(X)\to\operatorname{Reach}(Y),
\qquad
S\mapsto f(S),
\]

and contravariantly on requirements,

\[
f^*: \operatorname{Req}(Y)\to\operatorname{Req}(X).
\]

Where images and inverse images are available, these form the familiar
existential/substitution pattern

\[
f_!\dashv f^*.
\]

The bidirectional constructor is therefore not an inverse pair. It is a
push-forward/pullback pair with opposite variance. With source refinements as
vertical arrows, constructors as horizontal arrows, and typed comparison
certificates as squares, the same data can be presented as a double category
or equipment.

Conditioning is an order-enriched comparison inside a fibre. If \(g_X\) and
\(g_Y\) are source and target quadratic forms, then

\[
c(f\mid S)^2
=
\sup\{\lambda:
\lambda g_X|_S
\le
(f|_S)^*g_Y\}.
\]

Thus conditioning is not an extra scalar decoration. It measures how strongly
the backward metric dominates the native source metric on the forward
reachable image.

## Exact correspondences

| Existing area | Categorical component |
|---|---|
| controllability | forward image \(f_!S\) |
| observability Gramian | pulled-back output quadratic form |
| Fisher information | pullback metric on an admissible statistical model |
| weakest precondition | contravariant requirement transformer \(f^*\) |
| reverse differentiation | cotangent pullback, a first-order shadow of \(f^*\) |
| sheaf descent | compatibility of restriction and gluing across base change |
| renormalization | coarse-graining or Kan extension plus its comparison cell |
| error correction | restriction or localization to an admissible code or error subobject |
| Schur complement | infimal push-forward after eliminating hidden coordinates |
| viability kernel | greatest fixed point of a backward admissibility transformer |
| categorical optic | two-variance interface, with predicates rather than a fabricated state update |

These correspondences are structural, but they do not identify the physical
authority or topology across sectors.

## New relationship 1: the missing law is Beck--Chevalley coherence

Given a square relating a finite presentation to a completed or changed
context, there are two forward routes and dually two backward routes. A
Beck--Chevalley-style mate compares them.

The equality of these routes is exactly the naturality demanded by
Grothendieck's final Green/Ward mate and by the source--behavior distributive
law. In additive coordinates, the difference may be written as a residue. In
general it is a comparison 2-cell, not necessarily a subtractable scalar.

The tiny modular tail is therefore a candidate base-change defect:

\[
\Delta_X:
\operatorname{restrict}_X(W_\infty)
\Longrightarrow
W_X.
\]

Its exponentially small norm does not decide whether this comparison is
invertible, conservative, or kernel-producing.

## New relationship 2: closure failure is failure of left exactness

Let \(C\) denote the chosen completion or closure operation. The earlier
control obstruction compares

\[
C(G\cap\operatorname{Stab}P)
\quad\text{with}\quad
C(G)\cap\operatorname{Stab}P.
\]

Their possible inequality says that closure does not preserve the relevant
pullback. Categorically, \(C\) is not left exact on the admitted constructor
category.

The RH analogue compares finite invertibility with invertibility after
completion. Again, completion need not preserve the kernel pullback or a
strict lower-gain inequality.

Thus the control and RH failures are instances of the same categorical
question: which finite limits and enriched lower bounds does the completion
functor preserve?

## New relationship 3: robustness is quantitative conservativity

Ordinary Beck--Chevalley coherence asks whether a comparison cell is an
isomorphism. The conditioned version asks for more: its inverse cost must
remain uniformly bounded.

For cutoff comparisons \(\beta_N\), the robust gate is not merely that every
\(\beta_N\) is invertible, but that

\[
\inf_N c(\beta_N\mid S_N)>0.
\]

This is quantitative conservativity of base change. It is the categorical
home of completion-stable observability, robust control compilation, and the
relative importance of a tiny coherence tail.

## New relationship 4: task semantics is localization before conditioning

Different tasks identify different output directions. Projective D(S3)
control quotients central phases; dephasing retains only sector separation;
full coherent control retains the entire center.

Therefore conditioning must be computed after applying the task
localization, not on the ambient output space. This explains why the same
physical controls can be complete for conjugation and incomplete for coherent
relative phases without contradiction.

## Disposition

The next compiler object should be a conditioned square, not a bare
constructor. It should retain:

- source object and reachable subobject;
- constructor and target task localization;
- forward image and backward requirement;
- comparison cell and restricted lower gain;
- resource and fault modulus;
- cutoff base change and uniformity status.

Three finite laws should be audited:

1. functoriality of forward reachable images;
2. contravariant composition of quantitative requirements;
3. Beck--Chevalley compatibility for every authorized context or cutoff
   square.

This synthesis adds a precise missing relationship to the existing
enriched-Yoneda and distributive-law packets. Yoneda says complete contexts
identify constructors. The distributive law says source syntax composes with
behavior. The bifibration says which states move forward and which
requirements move backward. Conditioned Beck--Chevalley coherence says these
operations remain compatible and uniformly faithful when context changes.

The first falsifier is a square that commutes on scalar outputs but whose
comparison cell has a reachable kernel or a lower gain tending to zero.
