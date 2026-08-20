# 1111 — The Cyclic Partner Tangency Independently Closes on L2

## Question

Does the exceptional center

\[
(u,v)=(-1,0)
\]

have the same local closure mechanism as Entry 1110, when derived directly
from the frozen source rather than transported by cyclic symmetry?

## Independent critical-point derivation

At fixed \((u,v)=(-1,0)\), direct substitution into the complete
Cayley--Menger polynomial gives

\[
\boxed{
K=
\left(a^2-\frac32b^2-\frac14\right)^2.
}
\]

The labelled plane

\[
L_2=a-\frac12
\]

is tangent to the doubled conic at

\[
\boxed{(a,b)=\left(\frac12,0\right),}
\]

while \(L_1=2\) is a unit.

## Joint Newton data

Set

\[
p=u+1,\qquad q=v,\qquad A=a-\frac12,\qquad B=b.
\]

The exact Symbolica calculation gives

\[
\operatorname{in}K=\frac14(p+q-2A)^2,
\qquad
\operatorname{in}K_1=-(p+q-2A).
\]

Writing \(T=p+q-2A\), restriction to the doubled plane gives

\[
\boxed{
K_3|_{T=0}=6q(p-B)(p+B).
}
\]

On that plane,

\[
L_2=q,
\qquad
L_1=2.
\]

Thus this center selects the existing labelled \(L_2\) occurrence, in contrast
with the \(L_1\) occurrence selected at \((u,v)=(2/3,0)\).

## Support-cube test

The factors

\[
(\rho,q,V_-,V_+),
\qquad
V_-=p-B,\quad V_+=p+B,
\]

have Jacobian determinant

\[
\boxed{2\neq0}
\]

in coordinates \((\rho,q,p,B)\). They are therefore étale local coordinates.

Their augmented signed Koszul cube has dimensions

\[
(1,4,6,4,1),
\]

differential ranks

\[
(1,3,3,1),
\]

and zero homology.

## Narrow conclusion

The cyclic partner center independently closes:

\[
\boxed{
\text{existing }L_2\text{ occurrence}
\quad+\quad
\text{normal-crossing coefficient branches}
\quad+\quad
\text{no excess Tor}.
}
\]

No new carrier datum is required. Cyclic symmetry was not used to derive this
local result; it is now legitimate to compare Entries 1110 and 1111 through
the source occurrence action.

This remains an algebraic associated-grade result and does not establish a
physical relative-chain activation.

## Verification

Newton checker:

research/benincasa/marici-gm/src/bin/rank12_u2over3v0_newton.rs, invoked with
argument partner.

Support checker:

research/benincasa/marici-gm/src/bin/rank12_u2over3v0_support_cube.rs, invoked
with argument partner.

Packet:

research/benincasa/rank12-um1-v0-partner-tangency.json.

Ledger claim: seqclaim-eb093c7f1c7a3f76c82bf5b3.

Epistemic event:

ev-000000000810-e7d01b37-863a-4887-91c3-2c084b897e2e.

## Next finite falsifier

Construct the source-labelled cyclic occurrence map between the two rational
tangency packets. Verify its orientation, deck character, and transport of
the ordered support cubes. A mismatch would be a coherence defect in the
shared calculus even though both local complexes are separately exact.
