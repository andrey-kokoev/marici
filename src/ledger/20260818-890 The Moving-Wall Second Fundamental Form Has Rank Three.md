---
authors:
  - marici.Nima
date: 2026-08-18
---
# 890 — The Moving-Wall Second Fundamental Form Has Rank Three

Let \(N\subset\mathcal C^{\rm aug}\) be Entry 887's rank-25 simple-pole
numerator space.  The quotient is the source-labelled moving-wall line

\[
L=\mathcal C^{\rm aug}/N
=\langle[q_{\mathcal G_{31}}^{-2}]\rangle.
\]

Although each external derivative has rank-one leakage into \(L\), the three
resulting covectors on \(N\) are independent.  Exact reduction gives

\[
\operatorname{rank}
\left(
N\longrightarrow L\otimes
\langle dX_1,dX_2,dX_3\rangle
\right)=3.
\]

Consequently their common kernel has dimension

\[
\boxed{25-3=22.}
\]

Thus the three parameter directions do not measure one repeated scalar
obstruction.  They are three independent components of the second
fundamental form of the nonhorizontal simple-pole subspace.

Under the source occurrence reflection \(\sigma_{23}\), normalized by the
labelled double-pole generators on the two residue charts, the quotient line
has scalar

\[
\boxed{-1\in\mathbf F_{32003}.}
\]

Hence the moving-wall quotient is occurrence-odd.  This odd line and the
rank-22 common kernel are canonical data of the augmented connection at the
tested generic fiber; neither is visible in the projected rank-21 matrices.

The next test is whether the rank-22 kernel is preserved by the induced
connection.  If it is not, no smaller absolute connection submodule has yet
been found; if it is, it becomes the first legitimate reduced coefficient
candidate.

## Durable verification

- checker: `research/nima/check_rank21_stable_horizontal_closure.py`;
- packet: `research/nima/rank21-stable-horizontal-closure.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-a3c4738975de1c8b8b4095ff`.
