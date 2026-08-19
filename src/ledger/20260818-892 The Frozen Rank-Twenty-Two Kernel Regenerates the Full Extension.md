---
authors:
  - marici.Nima
date: 2026-08-18
---
# 892 — The Frozen Rank-Twenty-Two Kernel Regenerates the Full Extension

Entry 890 produced the rank-22 common kernel \(K_{22}\) of the three
moving-wall leakage covectors inside the rank-25 simple-pole numerator space.
Its invariance was tested in the source polynomial trivialization at the same
generic fiber.

For each external derivative, reduction modulo \(K_{22}\) has rank

\[
\boxed{3}.
\]

Thus \(K_{22}\) is not preserved by any of the three frozen connection
operators.  Iterating all three derivatives from \(K_{22}\) gives

\[
\boxed{
\dim\langle\nabla^\bullet K_{22}\rangle=26,
}
\]

the entire stable moving-wall extension of Entry 887.

This falsifies a constant source-frame rank-22 connection reduction.  The
result is deliberately narrower than a no-subbundle theorem: a parameter-
dependent kernel would contribute derivatives of its defining frame and must
be constructed over the generic function field before testing horizontality.
Likewise, a relative-support functor could select a smaller object not visible
as an invariant subspace of the absolute fiber.

The surviving conclusion is

\[
\boxed{
\text{the full rank-26 moving-wall extension is the smallest connection-stable
object found in the frozen source presentation.}
}
\]

The next admissible reduction test is therefore generic and functorial:
construct the second fundamental form over the kinematic function field and
solve its differential kernel equations, rather than choosing another
constant finite-fiber subspace.

## Durable verification

- checker: `research/nima/check_rank21_stable_horizontal_closure.py`;
- packet: `research/nima/rank21-stable-horizontal-closure.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-671cd6a8938000555198403f`.
