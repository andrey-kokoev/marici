---
author: marici.Benincasa
---

# 1125 — The Three Physical Soft Tate Lines Form the Regular Cyclic Module

## Question from Entry 1124

Entry 1124 proved that the fixed-base \(X_2\)-soft normal activates the
second-center anti-invariant Tate line with unit Gysin coefficient.  The
remaining descent test is whether its three labelled site occurrences glue
under cyclic relabelling with the source orientations.

## Occurrence basis

Let

\[
(\tau_1,\tau_2,\tau_3)
\]

denote the physically activated Tate generators for the fixed-base limits

\[
X_i=\eta\to0^+,
\]

with the other two site energies held fixed and equal on the corresponding
cyclic chart.  Each chart has

\[
p=q=\eta,
\qquad
s=1,
\]

so every local Gysin coefficient is one and every coefficient line carries
the same square-root deck character \(-1\).

## Cyclic transport

The cyclic relabelling \(1\to2\to3\to1\) acts by

\[
\boxed{
\sigma=
\begin{pmatrix}
0&0&1\\
1&0&0\\
0&1&0
\end{pmatrix}.
}
\]

Both orientation contributions are positive:

- the cyclic permutation of the three external soft normals is even;
- the cyclic permutation
  \((y_{12},y_{23},y_{31})\mapsto(y_{23},y_{31},y_{12})\)
  preserves the loop residue three-form.

Therefore no additional sign or transition unit occurs.  Exact calculation
gives

\[
\sigma^3=I,
\qquad
\det\sigma=1,
\]

and character

\[
\boxed{\chi=(3,0,0).}
\]

## Hard-to-vary conclusion

\[
\boxed{
\langle\tau_1,\tau_2,\tau_3\rangle
\simeq\mathbb Q[C_3]
}
\]

as an occurrence module, with a common anti-invariant coefficient deck
character.  Over \(\mathbb Q\),

\[
\mathbb Q[C_3]
\simeq
\mathbb Q_{\rm triv}\oplus\mathbb Q(\zeta_3).
\]

Thus the physical soft Tate class descends through the cyclic atlas without
a residual cocycle.  The three labels must nevertheless be retained: cyclic
equivariance does not authorize collapsing the occurrence module to its
invariant line.

## Architectural consequence

This is a complete local example of

\[
\text{labelled shared carrier}
+\text{ source Gysin calculus}
+\text{ sector-specific physical coefficients}
\]

with both local activation and global occurrence descent.  It supports H2
and supplies no new carrier datum.

## Durable verification

Checker:

`research/benincasa/checkers/rank12_soft_tate_cyclic_occurrences.py`.

Packet:

`research/benincasa/results/rank12-soft-tate-cyclic-occurrences.json`.

Ledger claim: `seqclaim-8c0572e08fd92d74b8b2918d`.

Epistemic event:

`ev-000000000833-76e5aad9-c2f7-4b9d-93b5-5a5e8ca147fd`.

## Next falsifier

Compare the invariant sum

\[
\tau_1+\tau_2+\tau_3
\]

with the total-energy nearby-cycle Tate line, while retaining the two-
dimensional nontrivial cyclic summand.  A source-derived map may identify the
invariant line; no rank comparison may erase the remaining occurrence data.
