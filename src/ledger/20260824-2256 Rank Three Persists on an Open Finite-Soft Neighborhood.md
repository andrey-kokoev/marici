# 2256 — Rank Three Persists on an Open Finite-Soft Neighborhood

## Hard-to-vary claim

Entry 2254's rank-three squeezed tensor readout is not confined to the strict
soft boundary.  For any source transfer matrix continuous at soft momentum,
it persists on an open finite-soft neighborhood.  Immediate rank loss would
therefore require a nonregular source transfer or failure of the nonzero-slope
assumption.

## Normalized leading matrix

After dividing the two tensor columns by their common nonzero source slope,
the leading transfer matrix is

\[
T_0=
\begin{pmatrix}
2&2&0\\
2&-1&-1\\
2&-1&1
\end{pmatrix},
\qquad
\det T_0=-12.
\]

Its adjugate is

\[
\operatorname{adj}(T_0)=
\begin{pmatrix}
-2&-2&-2\\
-4&2&2\\
0&6&-6
\end{pmatrix}.
\]

Hence

\[
\|T_0^{-1}\|_\infty=1.
\]

## Perturbative gate

Let the finite-soft source transfer be

\[
T(q)=T_0+\Delta(q),
\qquad
\Delta(q)\to0
\quad(q\to0).
\]

Whenever

\[
\|\Delta(q)\|_\infty<1,
\]

the Neumann criterion gives

\[
T(q)=T_0\bigl(1+T_0^{-1}\Delta(q)\bigr)
\]

invertible.  Continuity therefore guarantees some \(\epsilon>0\) for which

\[
0<|q|<\epsilon
\quad\Longrightarrow\quad
\operatorname{rank}T(q)=3.
\]

## Classification

\[
\boxed{
\text{leading Ward faithfulness}
+\text{regular finite-soft transport}
\Longrightarrow
\text{open finite-soft faithfulness}.
}
\]

This is stronger than an associated-grade statement but weaker than a global
finite-\(q\) theorem.  It does not derive \(\epsilon\), exclude later rank-loss
divisors, or prove detector accessibility.

The next source-specific calculation is to derive \(\Delta(q)\) and locate its
first rank-loss support.  Such support, if present, belongs to transport or
readout; it is not evidence for a missing occurrence Carrier cell.

## Verification

`research/benincasa/checkers/finite_soft_rank_stability.rs` verifies the
determinant, inverse norm, and sufficient stability bound.
