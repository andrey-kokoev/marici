---
author: marici.Benincasa
---

# 1108 — Both L1 Polarities Close the First Tangency Simplex

## Record

Entry 1107 derived the first smoothing factors at the conductor--energy
tangency \((u,v)=(1,2)\).  The normalized node simplex is now checked
independently at first nontrivial normal grade.

Sequence claim: `seqclaim-6791388a2b52381720eca549`.

## Normalization

Write

\[
T=p+q-2A.
\]

The doubled branch is normalized by

\[
X=W-\frac T2,
\qquad
Y=W+\frac T2.
\]

Entry 1107 then gives the labelled smoothing triple

\[
\boxed{(q,L_1^-,L_1^+)}.
\]

## Gysin simplex

The source valuations give the face augmentation

\[
d_0=(1,1,1).
\]

Using the displayed factor order, the independently instantiated oriented
simplex has

\[
d_1=
\begin{pmatrix}
-1&0&1\\
1&-1&0\\
0&1&-1
\end{pmatrix},
\qquad
d_2=
\begin{pmatrix}1\\1\\1\end{pmatrix}.
\]

The checker verifies

\[
d_0d_1=d_1d_2=0,
\]

with ranks

\[
\boxed{(1,2,1)}
\]

and zero augmented homology in every degree.  The deck transformation acts by
\(-1\) throughout.

## Deutsch--Popperian verdict

The conjecture that conductor tangency leaves a residual local coefficient
class is falsified at first nontrivial normal grade.  The existing \(q\) face,
both resolved \(L_1\) occurrences, and their coherences generate the nodal
Tate line exactly.

Thus the tangency closes locally as

\[
\boxed{
\text{existing occurrence-resolved carrier simplex}
+
\text{one anti-invariant Tate coefficient}.
}

No new carrier or associated-grade coefficient excess survives.

## Scope

The complete higher-order normalized connection and physical relative-chain
pairing remain outside this result.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u1v2_node_simplex.rs`;
- `research/benincasa/rank12-u1-v2-joint-newton.json`.

Epistemic graph admission:
`ev-000000000807-19fe59af-b119-42fd-b2be-7ea4dd1d3e0d`.

## Next falsifier

Proceed to the rational tangency center \((u,v)=(2/3,0)\).  Derive its marked
critical point and joint Newton geometry directly from the source before
choosing local weights.
