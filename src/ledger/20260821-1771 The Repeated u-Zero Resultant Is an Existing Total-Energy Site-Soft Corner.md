# 1771 — The Repeated \(u=0\) Resultant Is an Existing Total-Energy/Site-Soft Corner

## Question

Entry 1770 closes the generic transverse \(P_6\)-wall intersections. The exact
resultants retain repeated factors \(u^4\) for \((P_6,D)\) and \(u^3\) for
\((P_6,H)\). Do these factors identify a new carrier incidence?

## Source chart

In the homogeneous chart

\[
X_1=1,\qquad u=E_T,\qquad
X_2=\frac{u+v}{2}-1,\qquad X_3=\frac{u-v}{2},
\]

the common point over \(u=0\) is \((u,v)=(0,2)\), hence

\[
E_T=0,\qquad X_2=0.
\]

This is an already frozen total-energy/site-soft incidence.

## Completed local equations

Set \(z=v-2\). Exact translation gives

\[
4P_6=z^2+2u(1+2u-2u^2)z+u^2(1-2u)^2,
\]

\[
D=-z^2+(-6u+4u^2)z-u^2,
\]

\[
H=(1+2u-u^2)z+u(1-u)^2.
\]

Their ordinary initial forms are

\[
\operatorname{in}(4P_6)=(z+u)^2,
\]

\[
\operatorname{in}(D)=-(z^2+6uz+u^2),
\]

\[
\operatorname{in}(H)=z+u.
\]

Thus \(P_6\) and \(H\) share the tangent \(z+u=0\), with the \(P_6\)
branch doubled. The \(D\) tangent cone has two distinct directions because
its binary-quadratic discriminant is \(32\). These tangencies account for the
enhanced resultant multiplicities.

## Narrow conclusion

\[
\boxed{
u=0\text{ contributes no new carrier divisor; it is a nontransverse
coefficient collision over }E_T=X_2=0.
}
\]

This is a carrier classification, not a vanishing theorem for the iterated
nearby-cycle coefficient object. The remaining typed calculation at this
corner is the existing total-energy/site-soft iterated specialization with
the displayed tangent multiplicities retained.

## Durable evidence

- `research/benincasa/checkers/p6_wall_soft_corner.py`
- `research/benincasa/results/p6-wall-soft-corner.json`
- `research/benincasa/p6-wall-soft-corner.md`
- allocator claim: `seqclaim-5446857e5c3c7259702d9983`

