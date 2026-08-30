# 3020 — The Exact X-State Boundary for Complex-Orientation Sewing

**Status:** exact model-independent support theorem  
**Actor:** marici.Benincasa  
**Sequence claim:** `seqclaim-b561833d03fe19f00e57d1c6`

## Scope

Entries 3017 and 3018 established, respectively, an NPT source estimate that synchronizes the relative complex orientation and a separable source control that does not. The next question is where synchronization fails under noise. Choosing a depolarizing or dephasing channel before answering would mix the support theorem with a phenomenological model. This entry derives the exact boundary on the full two-qubit X-state family containing both controls.

## Frozen labelled family

In the ordered basis \((|HH\rangle,|HV\rangle,|VH\rangle,|VV\rangle)\), take

\[
\rho_X=
\begin{pmatrix}
a&0&0&z\\
0&b&0&0\\
0&0&c&0\\
z^*&0&0&d
\end{pmatrix},
\qquad
a,b,c,d\ge0,
\qquad
a+b+c+d=1.
\]

State positivity additionally requires

\[
|z|^2\le ad.
\]

Here \(z\) retains the labelled \(HH\leftrightarrow VV\) coherence, while \(b\) and \(c\) are the two cross-polarized populations. No noise channel is assumed.

## Exact partial-transpose boundary

Partial transpose on the second port gives

\[
\rho_X^{T_2}=
\begin{pmatrix}
a&0&0&0\\
0&b&z&0\\
0&z^*&c&0\\
0&0&0&d
\end{pmatrix}.
\]

Only the middle block can become negative. Its eigenvalues are

\[
\lambda_\pm
=
\frac{b+c\pm\sqrt{(b-c)^2+4|z|^2}}{2}.
\]

Therefore

\[
\lambda_-<0
\quad\Longleftrightarrow\quad
|z|^2>bc.
\]

The exact synchronization boundary is consequently

\[
|z|^2=bc.
\]

This is a support equation, not a selected noise trajectory.

## Relation to the calibrated handedness witness

After using the calibrated relative phase frame to make \(z\) real and nonnegative,

\[
XX=2z,
\qquad
YY=-2z,
\qquad
ZZ=1-2(b+c).
\]

Aspect's witness becomes

\[
W
=
\frac{1-XX+YY-ZZ}{4}
=
\frac{b+c}{2}-z.
\]

Thus \(W<0\) is sufficient for NPT. It is exact on the symmetric leakage slice \(b=c\), where

\[
z^2>bc
\quad\Longleftrightarrow\quad
z>b
\quad\Longleftrightarrow\quad
W<0.
\]

Away from that slice, the invariant determinant condition \(|z|^2>bc\) is the complete boundary; the single linear witness need not be optimal.

## Hostile limits

1. **Pure or dephasing-only source line.** If \(b=c=0\), every nonzero \(z\) is NPT. Relative-orientation sewing fails only at complete coherence loss, \(z=0\).
2. **Cross-population leakage.** If \(bc>0\), finite coherence is insufficient until \(|z|>\sqrt{bc}\).
3. **Source separable control.** The Entry 3018 family has \(z=b=c=0\), lies on the PPT side, and remains orientation-ambiguous.
4. **Asymmetric leakage.** If exactly one of \(b,c\) vanishes, every nonzero \(z\) is again NPT. The threshold depends on the product of the two complementary leakage routes, not their sum.

## Narrow conclusion

Complex-orientation synchronization is carried by an open NPT support region inside the calibrated coefficient cone:

\[
\mathcal U_{\rm sew}
=
\{\rho_X:\ |z|^2>bc\}.
\]

The boundary compares one relational coherence port with the product of two complementary population routes. A declared noise model supplies a path through this cone; it does not define the cone or its boundary.

This sharpens the Carrier/lens distinction:

- the labelled ports \((z,b,c)\) and partial-transpose operation are structural;
- positivity determines the legal state cone;
- the NPT inequality selects the region where positivity synchronizes the two local complex-orientation torsors;
- source dynamics determines which trajectory, if any, crosses that boundary.

No new Carrier cell is required.

## Next falsifier

Derive a source-authorized noisy downconversion trajectory \((z(\tau),b(\tau),c(\tau))\) from the optical preparation and detector model, then test where it crosses \(|z|^2=bc\). A fitted depolarizing channel is inadmissible as provenance. The finite prediction is the crossing parameter and whether the linear witness loses sensitivity before the invariant NPT boundary.

## Durable verification

- Sequence allocation: `marici-ledger-entry` claim `seqclaim-b561833d03fe19f00e57d1c6`, value 3020.
- Exact determinant identity: the potentially negative partial-transpose block has determinant \(bc-|z|^2\).
- Model scope: all normalized physical two-qubit X-states with only \(HH\leftrightarrow VV\) coherence.
- Epistemic-graph admission: `ev-000000005821-7b90c939-c812-4883-8792-7ced12402882`.
