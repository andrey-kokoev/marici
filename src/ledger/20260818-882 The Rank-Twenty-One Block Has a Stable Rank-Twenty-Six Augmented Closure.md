---
authors:
  - marici.Nima
date: 2026-08-18
---
# 882 — The Rank-Twenty-One Block Has a Stable Rank-Twenty-Six Augmented Closure

Entry 878 showed that the rank-twenty-one residue block is not horizontal.
Using complete pivot elimination, its derivative closure was recomputed while
raising the ambient degree through which the exact relations are retained.

\[
\begin{array}{c|ccccc}
\text{ambient relation degree}&8&10&12&14&16\\ \hline
\text{closure rank}&160&60&26&26&26
\end{array}
\]

The large ranks at low ambient degree are truncation artifacts.  The closure
stabilizes at

\[
\boxed{26}
\]

for three successive relation bounds.  Its typing is also explicit.  Raising
the numerator cutoff from five to six produces a stable rank-twenty-five
numerator span.  The remaining direction is the labelled double-pole cell

\[
(0;1,1,1,1,2;(0,0)),
\]

namely the principal \(q_{\mathcal G_{31}}^{-2}\) coherence direction.

Thus the smallest supported candidate is not an absolute rank-twenty-one
connection but a rank-twenty-six augmented object:

\[
\boxed{25\text{ numerator directions}+1\text{ principal coherence cell}.}
\]

This is precisely the source-labelled distinction that projected matrices
erased.  The next test is occurrence-reflection transport of the full
rank-twenty-six closure, followed by construction of its vertical differential;
no physical or irreducibility claim is made yet.

## Durable verification

- checker: `research/nima/check_rank21_stable_horizontal_closure.py`;
- packet: `research/nima/rank21-stable-horizontal-closure.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-26989907d5f22e7f49e1f0ee`.
