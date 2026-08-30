# 1772 — The Repeated \(u=1\) Resultant Is the Existing Double-Site-Soft Corner

## Question

After Entries 1770–1771, the only unclassified component of

\[
\operatorname{Res}_v(P_6,D)
=u^4(u-1)^2(1-8u+12u^2-4u^3)
\]

is the repeated rational factor \((u-1)^2\).

## Carrier support

The associated intersection is \((u,v)=(1,1)\). In the frozen homogeneous
chart

\[
X_1=1,\qquad
X_2=\frac{u+v}{2}-1,\qquad
X_3=\frac{u-v}{2},
\]

this is exactly

\[
X_2=X_3=0.
\]

It is therefore an existing labelled double-site-soft incidence.

## Exact local form

Set \(x=u-1\) and \(z=v-1\). Then

\[
4P_6=z^2+8x-2xz+21x^2-8x^2z+16x^3-4x^3z+4x^4,
\]

\[
D=-z^2-4x+2xz-5x^2+4x^2z.
\]

Their initial forms are

\[
\operatorname{in}(4P_6)=8x,
\qquad
\operatorname{in}(D)=-4x.
\]

Both coefficient branches are smooth and share the tangent \(x=0\). Their
ordinary tangency accounts for the repeated resultant factor.

## Narrow conclusion

\[
\boxed{
(u-1)^2\text{ records tangency over }X_2=X_3=0,
\text{ not a new carrier incidence.}
}
\]

Together with Entries 1770 and 1771, this classifies every irreducible
component of the two exact \(P_6\)-wall resultants at carrier level. Generic
cubic branches have no descending relative-sign extension, while both repeated
rational components lie on pre-existing soft strata.

This does not replace the iterated nearby-cycle coefficient calculations on
the soft corners.

## Durable evidence

- `research/benincasa/checkers/p6_d_double_soft_corner.py`
- `research/benincasa/results/p6-d-double-soft-corner.json`
- `research/benincasa/p6-d-double-soft-corner.md`
- allocator claim: `seqclaim-4ca221843894144f0cc4effc`

