---
id: 543
date: 2026-08-18
title: Raw DNC Comparison Is Localization Not a Physical Realization
---

# Raw DNC Comparison Is Localization Not a Physical Realization

Entry 542 leaves comparison with raw algebraic DNC geometry as the apparent
foundational frontier.  Entries 425--429 already determine the nature of that
comparison locally.  Propagating their invariant through the even-arity
induction shows that a raw-scheme equivalence preserving the physical class is
impossible.

At every physical radial chart, the logarithmically saturated PC stalk is

\[
C=mathbb Z[X,u^{\pm1}].
\]

The raw DNC relation (u=Xt) implies that inverting (u) also inverts (X)
and (t).  Hence the raw radial stalk is

\[
C[X^{-1}]=mathbb Z[X^{\pm1},u^{\pm1}],
\]

and the canonical comparison is localization at (X).

The retained boundary module

\[
C/(X)\congmathbb Z[u^{\pm1}]
\]

is nonzero, but

\[
C/(X)\otimes_C C[X^{-1}]=0.
\]

This module is not incidental: it is the occurrence/Cartier support carrying
the closed residue of the framed connector.  Therefore the raw comparison is
flat but nonconservative and cannot be a derived equivalence.  A failure on
one chart cannot be repaired by global descent.

Every even-arity physical Cut chart contains this same radial local model.
The checker verifies the witness on all physical charts through (n=14), with
counts

\[
3, 8, 15, 24, 35.
\]

The general count at (n=2m) is (m(m-2)), so the obstruction propagates to
every nontrivial even arity.

Consequently

\[
\boxed{\text{there is no raw ordinary-DNC scheme equivalence that preserves
the framed physical connector}.}
\]

The correct algebraic home is the fs/Kato logarithmic model of Entry 426 or
the trivial-inertia sector of its Artin-cone presentation from Entries
427--428.  The raw DNC remains available only as the generic nonconservative
localization obtained after forgetting occurrence support.  Its annihilation
of the physical class is the required ordinary-forgetting behavior, not a
defect awaiting repair.

Thus the phrase "raw algebraic realization" must be narrowed.  What can still
be sought is a global logarithmic algebraic stack realizing the Kato diagram
and its mixed-variance transform.  What cannot be sought is an equivalence to
the ordinary raw DNC structure sheaf while retaining the connector.

The executable audit is
`research/voevodsky/check_general_raw_dnc_comparison_no_go.py`.
