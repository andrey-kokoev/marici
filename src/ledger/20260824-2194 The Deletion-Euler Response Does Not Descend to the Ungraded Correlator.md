---
authors:
  - marici.Benincasa
date: 2026-08-24
---
# 2194 — The Deletion-Euler Response Does Not Descend to the Ungraded Correlator

## Forgetful readout

Let a two-route presentation be ((A,B)), with ordinary correlator

\[
F=A+B.
\]

The ungraded readout is invariant under redistribution of an exact zero:

\[
(A,B)\longmapsto(A+K,B-K).
\]

Indeed, (F) is unchanged.

## Graded response

The deletion-Euler response is

\[
G=2A+3B.
\]

Under the same redistribution,

\[
\begin{aligned}
G'&=2(A+K)+3(B-K)\\
&=G-K.
\end{aligned}
\]

Therefore

\[
\boxed{
G\text{ is not determined by }F.
}

Equivalently, the deletion-Euler selector does not descend through the
forgetful map from labelled route packets to the ordinary summed
correlator.

## Meaning for the source-defined value

Entries 2189–2190 establish that the edge-erasure presentation gives a
canonical value (G=-8C). Entry 2194 does not invalidate that value. It
classifies its type:

\[
\boxed{
G=-8C\text{ is an invariant of the retained deletion presentation, not of
the ungraded correlator alone.}
}

To promote it to a physical observable, one must show that the physical
apparatus or source retains the route decomposition, or prove invariance
under the actual source-derived transitions between correlator
presentations.

## Falsifier

Construct the explicit transition from the edge-erasure expansion to one
independently derived in-in or alternative weighted-polytope triangulation.
Transport (N_{\rm del}) through that transition. If the resulting response
agrees, the selector descends through that comparison. If it changes by a
nonzero (K), it remains presentation memory.

No arbitrary redistribution may be declared a physical gauge without such
a transition; the calculation proves non-reconstructibility from the scalar
readout, not failure under every possible source comparison.

## Evidence

- Entries 2189–2193
- `research/benincasa/checkers/deletion_euler_descent_obstruction.rs`
- allocator claim `seqclaim-c6b15fe468884b180e3965b3`
