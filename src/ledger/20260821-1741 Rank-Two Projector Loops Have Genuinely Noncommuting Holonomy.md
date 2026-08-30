# 1741 — Rank-Two Projector Loops Have Genuinely Noncommuting Holonomy

## Nonabelian loop construction

Work in \(\mathbb C^4\) with initial rank-two subspace

\[
E=\langle e_1,e_2\rangle.
\]

Construct closed projector loops using quarter-turns that move one occupied
direction at a time through a vacant auxiliary direction.  Each segment is a
horizontal lift: it has no internal rotation inside the instantaneous occupied
subspace.

The first loop sends \(e_1\) through \(e_3\) and back to \(-e_1\), leaving
\(e_2\) fixed.  Its fiber holonomy is

\[
H_A=
\begin{pmatrix}-1&0\\0&1\end{pmatrix}.
\]

The second loop transports both basis vectors through \(e_3,e_4\) and returns
them exchanged:

\[
H_B=
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

## Noncommutativity

Exact multiplication gives

\[
\boxed{
H_AH_B=
\begin{pmatrix}0&-1\\1&0\end{pmatrix}
\ne
\begin{pmatrix}0&1\\-1&0\end{pmatrix}
=H_BH_A.
}
\]

Both loops return the endpoint projector exactly.  Therefore endpoint
principal angles and static density data cannot detect their order.

## Readout typing

A source-labelled matrix interference reference can recover the ordered
holonomy matrices.  Without such a fiber frame, only conjugacy-invariant
quantities such as Wilson traces are canonical; those need not distinguish
the two orderings.

## Narrow result

The higher-rank amplitude coefficient object genuinely carries nonabelian
Wilczek–Zee-type transport.  It is encoded by the ordered projector path and
its matrix connection, not by a new carrier stratum.

## Durable artifacts

- `research/benincasa/checkers/noncommuting_rank_two_holonomy.rs`
- `research/benincasa/results/noncommuting-rank-two-holonomy.json`
- `research/benincasa/noncommuting-rank-two-holonomy.md`

## Next falsifier

Remove the labelled fiber frame and compute the complete gauge-invariant
Wilson packet for the two-loop groupoid.  Determine which ordered information
survives conjugation and what additional physical reference is required to
recover the full matrices.
