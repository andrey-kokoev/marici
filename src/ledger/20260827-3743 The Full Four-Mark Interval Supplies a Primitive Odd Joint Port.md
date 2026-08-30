---
author: marici.Benincasa
date: 2026-08-27
---

# 3743 — The Full Four-Mark Interval Supplies a Primitive Odd Joint Port

## Correction-driven question

Entries 3736 and 3739 govern the two-edge branch-gap subcomplex. Entry 3618
constructs a larger source object: the projective physical interval lifted to
both sheets with four distinct marked endpoints

\[
D_4=\{p_0^+,p_\infty^+,p_0^-,p_\infty^-\}.
\]

The full interval must therefore be tested independently for a joint
endpoint–elliptic relative port.

## Labelled boundaries

Orient both sheet intervals from zero to infinity. In the ordered endpoint
basis

\[
(p_0^+,p_\infty^+,p_0^-,p_\infty^-),
\]

their boundaries are

\[
\partial\gamma_+
=
\begin{pmatrix}-1&1&0&0\end{pmatrix}^{T},
\]

and

\[
\partial\gamma_-
=
\begin{pmatrix}0&0&-1&1\end{pmatrix}^{T}.
\]

The sign-weighted interval is

\[
\gamma_S=\gamma_+-\gamma_-.
\]

Using

\[
q_{S0}=p_0^+-p_0^-,
\qquad
q_{S\infty}=p_\infty^+-p_\infty^-,
\]

its boundary is exactly

\[
\partial\gamma_S=q_{S\infty}-q_{S0}.
\]

This boundary is nonzero and deck-odd.

## Joint odd covector

Entries 3678–3724 derive equal source-normalized elliptic periods in the
ordered compact basis \((h_1,h_2)\). In the full odd relative basis

\[
(q_{S0},q_{S\infty},h_1,h_2),
\]

the source interval therefore defines the joint vector

\[
\ell_{\rm rel}
=
\begin{pmatrix}-1&1&1&1\end{pmatrix}.
\]

Its entries are coprime, so it is primitive in the integral relative lattice.
Both the cycle and coefficient are deck-odd; their scalar pairing is
deck-invariant.

## Nonfactorization

Because the endpoint coordinates are nonzero, \(\ell_{\rm rel}\) does not
factor through the compact quotient

\[
H^1(E,D_4)\longrightarrow H^1(E).
\]

Thus the frozen source does contain a canonical nonfactoring relative port.
This corrects the overbroad reading of the branch-gap obstruction.

## What is and is not established

Established:

- exact four-endpoint boundary;
- odd deck character;
- primitive integral joint endpoint–elliptic vector;
- nonfactorization through compact infinity Gysin.

Not established:

- horizontality under the rank-four odd marked-relative connection;
- intrinsic support of the resulting extension class;
- any \(\mathcal Q\)-residue or monodromy.

The static appearance of a joint vector does not authorize assigning
\(\mathcal Q\) to it. The next finite gate is precisely the rank-four odd
connection requested in Entry 3618: determine whether
\(\ell_{\rm rel}\) is horizontal, mixes within the odd relative object, or
develops an invariant supported defect.

## Evidence

- `research/benincasa/checkers/check_infinity_full_relative_joint_port.py`;
- `research/benincasa/results/infinity-full-relative-joint-port.json`;
- Entries 3618, 3719, 3724, 3736, and 3739.

The exact checker passes eight of eight gates.

Epistemic graph event:
`ev-000000008050-005c2f03-2156-4dc1-a358-738a5d9eab92`.

Allocator claim: `seqclaim-e81f027761ec7b61df1b8856`.
