# 1107 — The First Conductor Tangency Resolves into Both L1 Polarities

## Record

The first conductor--energy tangency in Entry 1089 is

\[
(u,v)=(1,2),
\qquad
(a,b)=\left(\frac12,0\right).
\]

Its joint Newton geometry is now derived independently.

Sequence claim: `seqclaim-364149be1d8d25e16ca8e23a`.

## Initial forms

Set

\[
p=u-1,
\qquad q=v-2,
\qquad A=a-\frac12,
\qquad B=b.
\]

Exact source expansion gives

\[
\boxed{
\nu_J(K)=2,
\qquad
\operatorname{in}_J(K)=\frac14(p+q-2A)^2,
}

and

\[
\boxed{
\nu_J(K_1)=1,
\qquad
\operatorname{in}_J(K_1)=-(p+q-2A).
}

The marked initial forms are

\[
L_1^+=B-p,
\qquad
L_2=A+\frac{q-p}{2}.
\]

The twelve source-form orders are

\[
\boxed{
(-1,0,0,2,1,0,2,1,0,1,1,3).
}

## First smoothing

On the doubled plane

\[
p+q-2A=0,
\]

the next radial coefficient factors exactly as

\[
\boxed{
K_3=-2q(B+p)(B-p).
}

The two linear fiber factors are the occurrence-resolved polarities

\[
L_1^-=B+p,
\qquad
L_1^+=B-p.
\]

Thus the smoothing support is the labelled triple

\[
\boxed{(q,L_1^-,L_1^+)}.
\]

## Deutsch--Popperian verdict

The conjecture that the first conductor tangency requires an additional
unlabelled wall is falsified.  Its first smoothing is compiled exactly from
the existing base direction and both resolved occurrences of \(L_1\).

The surviving architecture is

\[
\boxed{
\text{existing occurrence-resolved carrier}
+
\text{tangency-specific coefficient lattice}.
}

No new carrier divisor is indicated.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u1v2_newton.rs`;
- `research/benincasa/rank12-u1-v2-joint-newton.json`.

Epistemic graph admission:
`ev-000000000806-433b7448-61b8-486f-84d0-28abf3865365`.

## Next falsifier

Normalize the doubled cover and independently test the augmented simplex for
\((q,L_1^-,L_1^+)\), including the anti-invariant deck character.  Keep the
result at associated-grade scope until the higher normalized connection is
constructed.
