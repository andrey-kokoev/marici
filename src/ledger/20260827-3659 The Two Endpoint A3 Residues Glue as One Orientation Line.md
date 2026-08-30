---
author: marici.Benincasa
date: 2026-08-27
---

# 3659 — The Two Endpoint A3 Residues Glue as One Orientation Line

## Reciprocal rows

Entry 3652 gives the infinity-corner logarithmic row

\[
\rho_\infty=
\begin{pmatrix}
0&1/y&0
\end{pmatrix}
\]

in the source coordinate \(s=1/t\). The reciprocal finite corner has

\[
\rho_0=
\begin{pmatrix}
0&1/x&0
\end{pmatrix}.
\]

Under reciprocal exchange \(x\leftrightarrow y\), one has

\[
\frac{ds}{s}=-\frac{dt}{t}.
\]

Therefore

\[
\rho_\infty\longmapsto-\rho_0.
\]

The sign is forced by orientation reversal of the projective interval. It is
not a normalization choice.

## Deck and scaling characters

Sheet exchange sends \(W\mapsto-W\), so the residue form also acquires sign
\(-1\). Consequently the two characters are

\[
\chi_{\rm reciprocal}=-1,
\qquad
\chi_{\rm deck}=-1,
\qquad
\chi_{\rm combined}=+1.
\]

Each involution squares to the identity. Under common energy scaling, the
residue line has weight \(-1\), matching the source elliptic forms and the
tangential finite-part covector.

## Result

The finite and infinity endpoint residues are not two independent physical
ports. They are reciprocal charts of one rank-one orientation/Kummer line.

Together with Entries 3648 and 3652, the soft-signed endpoint coefficient
packet is therefore:

- a rank-two even deformation grade;
- one complementary logarithmic readout line;
- reciprocal and deck gluing fixed by sign;
- no additional carrier or coherence generator.

The all-soft cone vertex \(x=y=z=0\) is excluded from this projective chart
and remains a separate radial specialization question.

## Evidence

- `research/benincasa/checkers/check_endpoint_a3_reciprocal_gluing.py`;
- `research/benincasa/results/endpoint-a3-reciprocal-gluing.json`.

The exact checker passes seven of seven gates.

Epistemic graph event:
`ev-000000007855-e4d41a02-d651-40a5-9d08-0a2f6cbc657e`.

Allocator claim: `seqclaim-97a8530a8ca719df604abde0`.
