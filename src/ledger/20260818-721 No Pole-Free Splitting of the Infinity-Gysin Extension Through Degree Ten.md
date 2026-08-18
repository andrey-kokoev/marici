---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 721 — No Pole-Free Splitting of the Infinity-Gysin Extension Through Degree Ten

## Question after Entries 719--720

Entries 719--720 prove that the literal physical source is cyclic for the full
rank-twenty-one relative union and that its two tested connection matrices
generate the full matrix algebra.  Hence no smaller physical block is an
invariant subspace or quotient of that frozen absolute connection.

Independently, the rank-nine residue-surface system carries the
source-derived infinity-Gysin functor

\[
0\longrightarrow \mathcal A_2
\longrightarrow \mathcal M_4
\xrightarrow{R_\infty}
\mathbb V_{\rm ell}(-1)
\longrightarrow0.
\]

Entry 207 proves that this is a horizontal exact sequence.  It does not decide
whether the differential-module extension splits.

This rank-nine functor has not been constructed as a quotient of the
rank-twenty-one physical relative union.  The present test is internal to the
residue-surface system and does not bypass Entry 720's irreducibility theorem.

## Frozen block equation

Use the exact Gysin-adapted frame already constructed in Entry 207.  In row
convention its two connection matrices have block form

\[
A_\xi'=
\begin{pmatrix}
K_\xi&0\\
E_\xi&B_\xi
\end{pmatrix},
\qquad \xi\in\{u,v\}.
\]

Here (K) is the algebraic kernel connection, (B) is the elliptic quotient
connection, and (E) is the extension block.  A change of quotient lift by a
matrix (X) removes the extension exactly when

\[
\partial_\xi X+XK_\xi-B_\xi X+E_\xi=0
\]

for both independent directions.

## Pole-free hostile search

Freeze (X) to be a (2\times2) polynomial matrix in the implemented
homogeneous coordinates ((u,v)).  For every total degree (d\le10), solve
the complete simultaneous linear system over
\(\mathbf F_{2^{61}-1}\), retaining all four entries and both derivatives.

No solution exists:

\[
\boxed{
X\in\operatorname{Mat}_{2\times2}\mathbf F[u,v],
\quad \deg X\le10
\quad\Longrightarrow\quad
\nabla X+E\ne0.
}
\]

The checker validates any candidate at 256 independent points and 512
directions; no candidate reached validation.

## Narrow conclusion

The infinity-Gysin extension has no pole-free splitting through total degree
ten.  This is not a nonsplitting theorem.  It implies only that any rational
splitting within the tested presentation must either have higher polynomial
degree or use a denominator.

The next search must admit only predeclared source divisors, one at a time:

\[
u, v, y, 1-y, 1+y, v-u, y-u^2, y+u^2, P_6, \mathcal Q.
\]

Their pole valuations must be reported separately.  In particular,
\(\mathcal Q\) must not be inserted preferentially or inferred from failure of
the pole-free ansatz.

## Classification

\[
\boxed{
\text{horizontal coefficient extension}
+\text{bounded pole-free splitting no-go};
\quad\text{no new carrier datum}.
}
\]

## Evidence

- Entries 207, 211, 718, 719;
- Entry 720;
- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/gysin-polynomial-split-d10.json`;
- allocator claim `seqclaim-956e9f74e953860660cab6aa`.

## Next falsifier

Run the same simultaneous two-direction equation with a frozen single-factor
denominator census.  A split supported on an ordinary signed-energy or soft
factor classifies the extension inside the existing coefficient geometry.  A
minimal \(\mathcal Q\)-denominator would place \(\mathcal Q\) in extension
transport, while absence through the declared bounds leaves nonsplitting as
the surviving hypothesis.
