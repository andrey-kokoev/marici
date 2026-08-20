# 1099 — The Second Exceptional Center Begins as a Doubled Existing Wall

## Record

Entry 1098 closed the first rank-twelve exceptional center across both Rees
charts.  The next frozen center from Entry 1089 is

\[
(u,v)=(2,0).
\]

Its marked intersection occurs at

\[
(a,b)=(2,1).
\]

Sequence claim: `seqclaim-b53e3bf3b646282be5d14821`.

## Source-local coordinates

Set

\[
p=u-2,
\qquad
q=v,
\qquad
A=a-2,
\qquad
B=b-1.
\]

The marked walls remain

\[
L_1=B-p,
\qquad
L_2=A+\frac{q-p}{2}.
\]

Thus the same labelled joint ideal is forced:

\[
J=(p,q,A,B).
\]

## Newton initial forms

Exact characteristic-zero Symbolica expansion gives

\[
\boxed{
\nu_J(K)=2,
\qquad
\operatorname{in}_J(K)=4(3p-q-2A)^2,
}
\]

and

\[
\boxed{
\nu_J(K_1)=1,
\qquad
\operatorname{in}_J(K_1)=-16(3p-q-2A).
}
\]

Also

\[
\nu_J(L_1)=\nu_J(L_2)=1.
\]

Unlike the first center, whose exceptional branch was a genuine quartic,
this center begins as a doubled linear branch.

## Source-form lattice

Using the fixed ordering

\[
(\Omega_{111},\Omega_{101},\Omega_{110},e_1,\ldots,e_9),
\]

the derived joint orders are

\[
\boxed{
(-1,0,0,1,1,0,1,0,0,1,1,1).
}
\]

The generic rank-twelve basis is again not a lattice at the center, but its
required shifts differ from Entry 1090 because the branch order has fallen
from four to two.

## First smoothing coefficient

On the \(p\neq0\) chart write \(s=q/p\).  The doubled branch is

\[
3-s-2A=0.
\]

Restricting the next radial coefficient of \(K\) to that plane gives

\[
\boxed{
K_3\big|_{3-s-2A=0}
=-16s(B-1).
}
\]

Both factors are already frozen support:

- \(s=0\) is the strict transform of \(q=0\);
- \(B-1=0\) is the exceptional \(L_1\) wall.

No undeclared smoothing divisor appears.

## Deutsch--Popperian verdict

The conjecture that the second exceptional center repeats the first center's
quartic exceptional geometry is falsified.  It instead produces a doubled
linear branch whose first smoothing is supported entirely on existing
labelled walls.

The narrow surviving architecture is

\[
\boxed{
\text{existing joint carrier}
+
\text{nonreduced/normalized coefficient degeneration}.
}
\]

The calculation does not justify a new carrier incidence.

## Evidence

- `research/benincasa/marici-gm/src/bin/rank12_u2v0_newton.rs`;
- `research/benincasa/rank12-u2-v0-joint-newton.json`.

Epistemic graph admission:
`ev-000000000798-c21d85bb-61cf-4c71-94b6-a68ea46d9c2d`.

## Next falsifier

Normalize the doubled exceptional cover and derive its conductor over

\[
s(B-1)=0.
\]

Then pull back the twelve source forms with the derived shifts and compute the
conductor-local quotient and connection.  If normalization requires support
beyond these two frozen divisors, H2 fails at this center; if not, the second
raw rank loss is again coefficient degeneration on the shared carrier.
