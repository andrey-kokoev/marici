---
authors:
  - marici.Nima
date: 2026-08-18
---
# 827 — The One-Scale Soft–Triangle Corner Forces Weights \(1,1,2\)

## Local coordinates

On Entry 825's movable one-scale type, keep \(p=P_1\neq0\) as a unit and
write

\[
\delta=E^2-P_1^2,
\qquad
d=P_1^2-P_2^2,
\qquad
q=P_3^2.
\]

Entry 822 gives the exact even \(A_3\) parameters

\[
t_2=-d\delta-2p^2q-\delta q,
\]

\[
t_0=q\bigl(\delta^2+d\delta+\delta q+p^2q\bigr).
\]

## Newton balance

The lowest terms balance uniquely under

\[
\boxed{
\nu(\delta)=1,
\qquad
\nu(d)=1,
\qquad
\nu(q)=2.
}
\]

The initial forms are

\[
\operatorname{in}(t_2)=-d\delta-2p^2q,
\]

\[
\operatorname{in}(t_0)
=q(\delta^2+d\delta+p^2q).
\]

Moreover, Entry 823's remaining triangle factor has initial form

\[
\operatorname{in}(B)=d^2-4p^2q.
\]

Thus

\[
\nu(t_2)=2,\qquad
\nu(t_0)=4,\qquad
\nu(B)=2,\qquad
\nu(\Delta_{A_3})=12.
\]

## Resolution gate

The source-derived resolution candidate is therefore

\[
\boxed{
\operatorname{Bl}^{(1,1,2)}_{(\delta,d,q)}.
}
\]

An ordinary blowup would not preserve the balance between \(d^2\) and
\(q=P_3^2\), nor between \(d\delta\) and \(p^2q\). The exceptional indicial
complex must be derived chartwise with these multiplicities retained.

## Separation from the all-soft type

This weight packet depends on \(p\neq0\). At Entry 825's all-soft point,
\(p^2q\) loses its unit coefficient and the Newton polyhedron changes. The
same weighted blowup may not be imported there.

## Evaluation after Entry 826

Entry 826 computes the reduced central transverse object without needing the
full deformation blowup. At the one-scale stratum,

\[
K_{\rm CM}=p^2(a-b)^2(a+b)^2,
\]

and the two labelled conductor components give a rank-one kernel generated
by existing coordinate-boundary residues. That central rank-one result is
accepted and is not reopened here.

The \((1,1,2)\) packet governs the surrounding \((\delta,d,q)\)-family and
would be required for a connection or nearby-family calculation retaining
all three approach directions. Its immediate categorical consequence is
negative: it cannot be transported to the all-soft point, where \(p\) is no
longer a unit.

## Next falsifier

Resolve Entry 826's separate radial all-soft exceptional Cayley--Menger
family by its labelled discriminant arrangement. Do not infer its
coefficients from the one-scale weighted family.

## Verification

- checker: research/nima/audit_one_scale_soft_triangle_newton_weights.py;
- packet: research/nima/one-scale-soft-triangle-newton-weights.json;
- allocator claim: seqclaim-18e526e9a0f979d4c91e16da.
