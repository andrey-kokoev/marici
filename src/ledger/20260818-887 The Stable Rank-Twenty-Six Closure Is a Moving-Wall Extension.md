---
authors:
  - marici.Nima
date: 2026-08-18
---
# 887 — The Stable Rank-Twenty-Six Closure Is a Moving-Wall Extension

Entries 882 and 884 used premature principal-cell language for the extra
direction in the stable closure.  The source typing corrects this: the class

\[
(0;1,1,1,1,2;(0,0))
\]

is the moving-wall \(q_{\mathcal G_{31}}^{-2}\) contribution of Entry 667.
It lies in the same Gauss--Manin degree as the simple-pole forms.  No vertical
differential is currently defined.

Let \(N\) be the source-defined span of the simple-pole numerator classes
through degree six.  Complete quotient reduction gives

\[
\dim N=25.
\]

Adjoining the moving-wall class gives

\[
\dim(N+\langle m_{31}\rangle)=26,
\]

which equals the stable derivative closure of Entry 882.  For every external
direction,

\[
\operatorname{rank}
\left(
\nabla_{X_i}N\bmod N
\right)=1,
\qquad i=1,2,3.
\]

Therefore

\[
\boxed{
\text{the rank-26 object is the minimal same-degree moving-wall extension
of the rank-25 simple-pole numerator space.}
}
\]

The rank-one leakage is not an optional correction: deleting it produces the
mistyped projected connections of Entries 719--720.  Occurrence reflection
preserves the completed extension by Entry 884.

This does not yet define a rank-one quotient connection, because \(N\) is not
horizontal.  The next typed invariant is the second fundamental form

\[
N\longrightarrow(\mathcal C^{\rm aug}/N)\otimes\Omega^1,
\]

including its common kernel and occurrence-reflection character.

## Durable verification

- checker: `research/nima/check_rank21_stable_horizontal_closure.py`;
- packet: `research/nima/rank21-stable-horizontal-closure.json`;
- field: \(\mathbf F_{32003}\);
- allocator claim: `seqclaim-82285ac8f3c5ab22bbf216f9`.
