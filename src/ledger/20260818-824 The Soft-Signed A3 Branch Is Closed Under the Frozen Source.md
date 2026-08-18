---
authors:
  - marici.Nima
date: 2026-08-18
---
# 824 — The Soft-Signed A3 Branch Is Closed Under the Frozen Source

## Evidence chain

The soft--signed (A_3) audit now has a complete conditional disposition.

Entry 817 constructs the full associated-grade coefficient space:

\[
\operatorname{rank}V_{A_3}=3,
\qquad
\operatorname{rank}V_{\rm support}=2.
\]

Entry 819 refutes a strict horizontal quotient.  The generic Kato root has
nonzero monodromy defect, so a homotopy-coherent cone is required.

Entries 822–823 prove that the printed independent-positive-regulator cone
meets at least two labelled braid chambers, separated exactly by

\[
\epsilon_E=\epsilon_{P_1}
\subset J^{-1}(\Delta_{A_3}).
\]

Therefore the source does not select a unique thimble marking or the
rank-66 coherence module typed in Entry 821.

## Frozen-source verdict

\[
\boxed{
\begin{array}{c|c}
\text{carrier geometry}&\text{sufficient}\\
\text{de Rham associated grade}&\text{sufficient}\\
\text{strict quotient local system}&\text{refuted}\\
\text{physical coherence cell}&\text{unselected}\\
\text{new carrier stratum}&\text{unsupported}
\end{array}
}
\]

The algebraic excess exists.  Its physical Betti realization is undefined,
not zero, under the frozen source package.

## Reopening condition

This branch may be reopened only by an independently sourced graph-level
contour-to-energy regulator map whose image is proved to lie wholly in one
component of the positive regulator cone with the pulled-back (A_3)
discriminant removed.

An equal-regulator choice, a chosen hierarchy, an abstract Coxeter basis, a
fitted coherence cell, or an added carrier stratum does not satisfy this
condition.

## Next branch

The active frontier moves to the deeper nonisolated soft--triangle locus

\[
P_3=0,
\qquad
P_1^2=P_2^2,
\]

where a logarithmic resolution must decide whether existing soft, triangle,
and coordinate-boundary maps generate the transverse coefficient complex.

## Verification

- packet checker: `research/nima/audit_a3_frozen_source_closure.py`;
- packet: `research/nima/a3-frozen-source-closure.json`;
- allocator claim: `seqclaim-e48bfff8cddd5c0859521e32`.
