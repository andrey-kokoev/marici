# Reciprocal half-planes cannot share one outward-contractive norm

## Proposed anisotropic repair

Write the spectral coordinate relative to the seam as

\[
z=a+it.
\]

The previous no-go suggests treating tangential `t` motion as reversible phase
transport and normal `a` motion as a directed semigroup. A tempting next claim
is that transport is contractive outward from the seam in both half-planes.

That claim is impossible in one common norm when reciprocal transport gives
the inverse normal evolution.

## Two-sided contraction theorem

Let `T(a)` be an invertible one-parameter group on a normed state space. If,
for every nonnegative `a`,

\[
\lVert T(a)\rVert\leq1
\qquad\text{and}\qquad
\lVert T(-a)\rVert\leq1,
\]

then `T(a)` is an isometry.

Indeed, for every state `x`,

\[
\lVert x\rVert
=\lVert T(-a)T(a)x\rVert
\leq\lVert T(a)x\rVert
\leq\lVert x\rVert.
\]

Hence equality holds throughout.

If the holomorphic normal flow is

\[
T(a)=e^{aB}
\]

with self-adjoint `B`, isometry for real `a` forces `B=0`. Thus nontrivial
normal orientation cannot be contractive in both reciprocal directions under
one fixed positive norm.

## Exact scalar hostile

Take

\[
T(a)=e^{-a}.
\]

For positive `a`, the right outward evolution is strictly contractive. Its
reciprocal inverse is

\[
T(-a)=e^a,
\]

which is strictly expansive in the same norm. Requiring both to be contractive
would eliminate every nonzero `a`.

The obstruction is algebraic, not numerical: an invertible map and its inverse
cannot both strictly decrease the same norm.

## Consequence

The two half-planes cannot be two copies of one dissipative sector sharing one
positive geometry. A nontrivial reciprocal construction needs at least one of:

- two sector-dependent norms or polarizations;
- contraction on one sector paired with expansion on the reciprocal sector;
- a Krein or symplectic conservation law replacing positive contraction;
- a relative boundary energy whose sum, rather than each sector separately,
  has a sign;
- a noninvertible source semigroup whose reciprocal is not an internal inverse.

The first option reintroduces the observer-comparison problem. The second does
not itself prevent a fixed overlap zero. The third and fourth return to the
coupled endpoint–gamma–prime current. The fifth requires explicit typing of
the information discarded by normal evolution.

## Categorical meaning

Reciprocity is an equivalence between the two sectors. Dissipation is a
directed, generally noninvertible structure. Transporting dissipation through
an equivalence reverses its order. It cannot produce the same order on both
sides without collapsing the strictly ordered part.

Thus the fifth tower cannot merely attach one global order to the reciprocal
Ubersector. It needs a relative order: each sector has its own outward cone,
and the seam coherencer explains how their opposite orientations combine.

## DPC

For any proposed normal semigroup law, require:

1. the norm, cone, or order used in each sector;
2. whether reciprocal sewing transports the law, reverses it, or dualizes it;
3. whether normal transport is invertible;
4. the exact seam comparison between the two sector geometries;
5. the fixed-observer incidence after this comparison;
6. completion-stable bounds.

Reject:

- strict outward contraction on both reciprocal sides in one norm;
- treating an inverse group element as a second forward contraction;
- silently changing norms across the seam;
- inferring fixed-overlap nonvanishing from state-norm contraction;
- calling a noninvertible completion map reciprocal without typing its lost
  state component.

## Verdict

The common-norm contraction hypothesis is falsified. The surviving fifth-tower
geometry must be genuinely relative: two oppositely oriented sector laws plus
a source-derived seam comparison. This strengthens, rather than removes, the
need for a two-sector Ubersector.

