# 1104 — The Existing Three-Face Simplex Generates the Nodal Tate Line

## Record

Entry 1103 identified one anti-invariant Tate vanishing-cycle line for

\[
XY=p\,s\,(B-1).
\]

The labelled residue/Gysin comparison and all overlap coherences are now
derived from the exact smoothing monomial.

Sequence claim: `seqclaim-4bed32f34a1c80cb926fdd8b`.

## Face maps

Since

\[
d\log\bigl(p\,s\,(B-1)\bigr)
=d\log p+d\log s+d\log(B-1),
\]

the three labelled face maps into the universal Tate line are

\[
\boxed{d_0=(1,1,1).}
\]

No coefficient is fitted; each unit coefficient is the valuation of the
source smoothing parameter along its labelled divisor.

## Pairwise and triple coherence

Order the vertices by

\[
(p,s,B-1)
\]

and the oriented edges by

\[
(p,s),\quad(s,B-1),\quad(B-1,p).
\]

The edge boundary is

\[
d_1=
\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix},
\]

and the triple boundary is

\[
d_2=
\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]

Exact integer matrix calculation gives

\[
d_0d_1=0,
\qquad
d_1d_2=0,
\]

with ranks

\[
\boxed{(\operatorname{rank}d_0,operatorname{rank}d_1,operatorname{rank}d_2)
=(1,2,1).}
\]

Therefore the augmented simplex

\[
\mathbb Q
\xrightarrow{d_2}
\mathbb Q^3
\xrightarrow{d_1}
\mathbb Q^3
\xrightarrow{d_0}
\mathbb Q
\]

has zero homology in every degree.  Every term carries the same
anti-invariant deck character, so the comparison is deck equivariant.

## Deutsch--Popperian verdict

The conjecture that the nodal Tate line leaves a residual comparison-cone
class is falsified.  The three existing support faces, together with their
pairwise and triple coherences, generate it exactly.

Hence the second exceptional center closes locally as

\[
\boxed{
\text{existing labelled three-face carrier}
+
\text{one anti-invariant Tate coefficient}
+
\text{exact Gysin simplex}.
}
\]

No new carrier or residual coefficient class survives this local test.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_node_gysin_simplex.rs`;
- `research/benincasa/rank12-u2-v0-joint-newton.json`.

Epistemic graph admission:
`ev-000000000803-e0cb693c-8d1e-4975-8627-d91ba6772f85`.

## Next falsifier

Move to the next frozen exceptional center, \((u,v)=(2,4)\), and derive its
joint parameter--fiber Newton geometry before selecting a blowup.  Compare
its resulting coefficient object with the first two centers only after its
own labelled carrier and transition maps are fixed.
