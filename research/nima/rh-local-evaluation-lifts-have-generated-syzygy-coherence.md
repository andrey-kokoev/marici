# RH local evaluation lifts have generated syzygy coherence

## Result

Regular evaluation-wall factorizations on different spectral charts do not require independently declared comparison cells.

Suppose

\[
R=L_iM
\]

on each chart \(U_i\). On an overlap,

\[
(L_j-L_i)M=0.
\]

Thus the difference \(L_j-L_i\) lies in the left syzygy module of the bordered operator \(M\).

For three charts, the overlap differences telescope:

\[
(L_V-L_U)+(L_W-L_V)+(L_U-L_W)=0.
\]

Triangle coherence is generated automatically from the local factors.

## Exact fixture

The checker uses

\[
M=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
R=(1,0),
\]

with three distinct local factors

\[
L_U=(1,0),
\qquad
L_V=(1,1),
\qquad
L_W=(1,3).
\]

All factor \(R\) through \(M\). Their differences are nonzero syzygies, and the triangle residual is exactly zero.

## Finite analytic consequence

For finite holomorphic matrices on an open half-plane, the relevant kernel and syzygy sheaves are coherent. The half-plane is Stein, so the standard coherent-sheaf vanishing theorem removes the ordinary first gluing obstruction once genuine local membership has been established on a suitable cover.

This does not manufacture local factors. It says that no extra finite coherence certificate should be fitted after they exist.

## Where obstruction can return

The completed theta carrier is pro-valued and infinite-dimensional. Coherence of each finite syzygy sheaf does not imply that the inverse limit preserves:

- bounded factorization norms;
- compatible domains;
- closed ranges;
- exactness of inverse limits.

The obstruction can therefore reappear as a completion defect even though every finite overlap triangle telescopes.

## DPC verdict

Candidate: declare pairwise and triple comparison cells between local evaluation lifts.

Verdict: redundant and vulnerable to fitting.

Candidate: generate comparisons as differences of source-derived local factors.

Verdict: exact at finite level.

Surviving completion gate: construct a compatible inverse system of regular factors and syzygies with uniform graph bounds. A finite chart cocycle residual rejects local typing; unbounded compatible factors reject completion.

## Immediate audit

If Grothendieck's bordered lift requires multiple spectral charts, record the local factors themselves. Generate every overlap cell by subtraction and verify the syzygy equation. Do not accept separately supplied coherence matrices. Then inspect whether the factors and syzygies remain bounded and domain-compatible across moment cutoffs.
