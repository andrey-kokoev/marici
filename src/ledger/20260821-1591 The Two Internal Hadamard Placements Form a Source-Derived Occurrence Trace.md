# 1591 — The Two Internal Hadamard Placements Form a Source-Derived Occurrence Trace

## Question

May Entry 1590's two internal statistical occurrences

\[
q,qquad k=|p-q|
\]

be combined before the hard-grade audit?

## Exact source involution

The change of variables

\[
\vec q\mapsto\vec p-\vec q
\]

exchanges the two internal labels.  It preserves the source vertex

\[
(p^2+q^2+k^2)^2
\]

and exchanges the two Wightman factors.  Its oriented Jacobian is (-1), but
the source integral uses the Lebesgue density, whose Jacobian is (1).

Therefore, on the full loop domain or with a transported swap-invariant
state profile,

\[
\boxed{
\int d^3q\,(delta G_qG_k+G_q\delta G_k)
=2\int d^3q\,\delta G_qG_k.
}
\]

## Interpretation

The coefficient (2) is the trace of a two-element labelled occurrence
orbit.  It is not a fitted Wick normalization or a new cosmological
coupling.

A regulator imposed only on a fixed (q)-centred ball breaks the source
involution and cannot be used to infer this trace.  The Hadamard profile must
travel with the varied mode label.

## Consequence

The middle-loop Hadamard audit reduces to one occurrence representative plus
a source-derived trace coefficient (2).  Carrier occurrence data remain
necessary to derive that coefficient before diagonal identification.

## Next falsifier

Reduce the endpoint primitive of (delta G_qG_k), apply the trace, and test
every nondecaying hard grade after the declared subtractions and
counterterms.

## Artifacts

- `research/benincasa/internal-qk-occurrence-trace.md`
- `research/benincasa/checkers/internal_qk_occurrence_trace.rs`
- `research/benincasa/results/internal-qk-occurrence-trace.json`

Ledger sequence claim: `seqclaim-e6ac49321cc087725aac166f`.
