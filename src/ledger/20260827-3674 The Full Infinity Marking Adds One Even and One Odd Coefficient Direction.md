---
author: marici.Benincasa
date: 2026-08-27
---

# 3674 — The Full Infinity Marking Adds One Even and One Odd Coefficient Direction

## Frozen marked geometry

After the source residue (q_{\mathcal G_{12}}=0\), the five remaining
denominators restrict on the elliptic infinity boundary to three labelled
projective positions:

\[
\begin{array}{c|c}
t=0&q_{g_2},q_{\mathcal G_{23}}\\
t=-1&q_{g_3}\\
t=\infty&q_{g_1},q_{\mathcal G_{31}}.
\end{array}
\]

Deck completion therefore marks six points

\[
D_6=
\{p_0^\pm,p_{-1}^\pm,p_\infty^\pm\}.
\]

This uses the source-derived marked sections of Entry 796. No additional
point or divisor is introduced.

## Relative rank and character

For a genus-one curve,

\[
\dim H^1(E,D_6)
=2+(6-1)=7.
\]

The endpoint quotient (H^0(D_6)/H^0(E)) has deck character

\[
2\mathbb Q_+\oplus3\mathbb Q_-.
\]

Compact elliptic (H^1(E)) contributes two further odd directions. Hence

\[
H^1(E,D_6)
\cong
2\mathbb Q_+\oplus5\mathbb Q_-.
\]

Relative to Entry 3618's endpoint-only object, adjoining the deck pair over
(t=-1) adds exactly

\[
\mathbb Q_+\oplus\mathbb Q_-.
\]

## Physical incidence

The source projective ray is

\[
t\in[0,\infty]
\]

with boundary only at (t=0,\infty). Its literal chain has no incidence with
the additional mark at (t=-1). Moreover, the elliptic branch collides with
that mark only when

\[
P_3=0,
\]

which is existing site-soft support.

Thus the full marked relative object is larger than the endpoint object, but
the extra pair is not directly activated by the literal infinity path at
generic nonsoft kinematics.

## Scope and next falsifier

This is an incidence and deck-character theorem. It does not prove that the
rank-two new-mark quotient is preserved by the full marked-relative
Gauss–Manin connection.

The next finite test is connection-level: compute the covariant derivative of
the (t=-1) evaluation pair in the source-normalized frame and determine
whether it mixes with the four-dimensional odd endpoint–elliptic object. A
nonzero mixing block would make the new finite mark visible through transport
despite empty literal incidence. A zero block would prove that the physical
infinity covector factors through the endpoint-only object on the generic
nonsoft base.

## Evidence

- `research/benincasa/marici-gm/src/bin/generic_marked_infinity_collisions.rs`;
- `research/benincasa/checkers/check_infinity_full_mark_relative_object.py`;
- `research/benincasa/results/infinity-full-mark-relative-object.json`;
- Entries 796 and 3618.

The exact checker passes six of six gates.

Epistemic graph event:
`ev-000000007888-477cb610-7111-4dc8-8aad-43ffab1dde46`.

Allocator claim: `seqclaim-9ee8e550ac607c6df4dea35a`.
