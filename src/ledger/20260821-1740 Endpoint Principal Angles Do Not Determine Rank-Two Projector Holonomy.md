# 1740 — Endpoint Principal Angles Do Not Determine Rank-Two Projector Holonomy

## Loop falsifier

For \(n\in S^2\), let \(P_n\) project onto the rank-two plane \(n^\perp\).
Transport this plane around the geodesic octant triangle

\[
e_1\longrightarrow e_2\longrightarrow e_3\longrightarrow e_1
\]

using the source-defined minimal quarter-turn rotations \(R_{12},R_{23},R_{31}\).

## Exact ordered transport

The ordered product

\[
H=R_{31}R_{23}R_{12}
\]

fixes the normal \(e_1\), hence returns the endpoint projector exactly:

\[
HP_{e_1}H^T=P_{e_1}.
\]

Its action on the endpoint fiber \(\langle e_2,e_3\rangle\) is

\[
\boxed{
H_{\rm fib}=
\begin{pmatrix}
0&-1\\1&0
\end{pmatrix}.
}
\]

Thus the fiber rotates by ninety degrees.  Reversing the loop gives
\(H_{\rm fib}^{-1}\).

## Consequence

The initial and final projector pair has identical principal-angle packet
\(\{1,1\}\), but the loop transport is nontrivial.  Therefore Entry 1739's
static characteristic polynomial does not determine higher-rank transport.

The ordered projector path does determine this geometric holonomy through its
connection.  The missing datum is a matrix-valued coefficient connection, not
a new carrier stratum.

This example has \(SO(2)\) holonomy.  It is a rank-two precursor to genuinely
noncommuting Wilczek–Zee holonomy; nonabelianity itself is not yet established.

## Durable artifacts

- `research/benincasa/checkers/rank_two_projector_loop_holonomy.rs`
- `research/benincasa/results/rank-two-projector-loop-holonomy.json`
- `research/benincasa/rank-two-projector-loop-holonomy.md`

## Next falsifier

Construct two loops in a complex rank-two projector family whose holonomies do
not commute.  Test whether a matrix-valued interference reference recovers the
conjugacy class and ordered composition without choosing a fiber frame.
