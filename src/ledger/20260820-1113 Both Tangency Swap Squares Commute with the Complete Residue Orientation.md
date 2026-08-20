---
author: marici.Benincasa
---

# 1113 — Both Tangency Swap Squares Commute with the Complete Residue Orientation

## Correction to Entry 1112

Entry 1112 used degree-four scaling for the Cayley--Menger square root. The
complete source polynomial is homogeneous of degree six. If the source-label
swap \(1\leftrightarrow2\) uses the old second-site energy \(y\) to restore
the chart \(x'=1\), then

\[
a'=\frac by,\qquad b'=\frac ay,\qquad
w'=\frac{w}{y^3}.
\]

Therefore

\[
\boxed{
\frac{da'\wedge db'}{w'}
=
-y\,\frac{da\wedge db}{w}.
}
\]

The relative fiber-residue sign alone is not the complete orientation line.
The ordered \(G_{12}\) occurrence also reverses under
\(1\leftrightarrow2\), contributing a source-derived cut sign \(-1\).

Entry 1112's conclusion survives, but for this corrected reason.

## Rational tangency pair

For

\[
\left(\frac23,0,0,-\frac13\right)
\longrightarrow
\left(-1,0,\frac12,0\right),
\]

one has \(y=-2/3\). Hence

\[
\operatorname{sign}(-y)=+1.
\]

The ordered support factors transform by units

\[
\left(1,-\frac32,-\frac34,-\frac34\right),
\]

whose product has sign \(-1\). Including the ordered-cut sign gives

\[
\boxed{
\operatorname{or}_{\rm support}=-1
=
(+1)(-1)
=
\operatorname{or}_{\rm rel\,fiber}
\operatorname{or}_{G_{12}}.
}
\]

## Integral tangency pair

The same source involution exchanges

\[
(u,v,a,b)=\left(1,2,\frac12,0\right)
\]

with

\[
(u',v',a',b')=(2,4,0,1).
\]

Its linearization in the source coordinates
\((p,q,A,B)\) and target coordinates \((p',q',A',B')\) is

\[
\begin{pmatrix}
p'\\q'\\A'\\B'
\end{pmatrix}
=
\begin{pmatrix}
0&-2&0&0\\
-4&-2&0&0\\
0&0&0&2\\
-1&-1&2&0
\end{pmatrix}
\begin{pmatrix}
p\\q\\A\\B
\end{pmatrix},
\]

with determinant

\[
\boxed{32.}
\]

For the ordered source factors

\[
(q,L_{1,-},L_{1,+})
\]

and ordered target factors

\[
(p',L_{2,+},L_{2,-}),
\]

the map is

\[
p'=-2q,
\qquad
L_{2,+}=2L_{1,+},
\qquad
L_{2,-}=2L_{1,-}.
\]

The factor matrix has determinant \(+8\), so the support-simplex orientation
is \(+1\).

Here \(y=1/2\), so the relative fiber-residue sign is \(-1\). Multiplying by
the ordered-cut sign \(-1\) gives

\[
\boxed{
\operatorname{or}_{\rm support}=+1
=
(-1)(-1)
=
\operatorname{or}_{\rm rel\,fiber}
\operatorname{or}_{G_{12}}.
}
\]

## Deck character

The transformation \(w'=w/y^3\) commutes with the deck involution
\(w\mapsto-w\). Thus

\[
\boxed{\chi_{\rm deck}=+1}
\]

for both swap squares.

## Narrow conclusion

Both independently derived tangency pairs commute with the complete
source-normalized residue orientation:

\[
\boxed{
\text{support orientation}
=
\text{relative fiber orientation}
\times
\text{ordered occurrence orientation}.
}
\]

No transition homotopy, fitted sign, or new carrier datum is required.

This closes the two source-swap coherence squares at the tested associated
grade. It does not construct a physical relative chain or prove a global
characteristic-zero rank-twelve connection.

## Verification

Checker:

research/benincasa/marici-gm/src/bin/rank12_tangency_swap_coherence.rs.

Packet:

research/benincasa/rank12-tangency-swap-coherence.json.

Ledger claim: seqclaim-c1eed1a46de30c07beed0727.

Epistemic event:

ev-000000000812-0be65578-9c71-409a-b7c9-f9f315e2ca8e.

## Next finite falsifier

Assemble the six-center exceptional atlas from Entries 1098--1113 and audit
completeness against the frozen rank-loss census. Keep the first center's
pending characteristic-zero primitive witness and all absent physical-chain
maps as explicit coefficient-level qualifications.
