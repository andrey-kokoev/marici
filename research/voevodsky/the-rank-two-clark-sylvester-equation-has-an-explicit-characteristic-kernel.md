# The rank-two Clark Sylvester equation has an explicit characteristic kernel

## Kernel form of the equation

Let

\[
(Kf)(u)
=
\int_0^\infty
k(u,v)f(v)\Phi(v)\,dv.
\]

For

\[
A_+=-\partial_u,
\qquad
A_-^*=-\partial_u-
\frac{\Phi'}{\Phi},
\]

the cross Sylvester equation

\[
A_-^*K+KA_+=Q_{-+}
\]

has interior kernel equation

\[
\left(
\partial_v-
\partial_u+
\frac{\Phi'(v)}{\Phi(v)}-
\frac{\Phi'(u)}{\Phi(u)}
\right)k(u,v)
=
\frac12(u-v).
\]

Here the right side follows from

\[
Q_{-+}
=
\frac12
\left(
|u\rangle\langle1|-
|1\rangle\langle u|
\right),
\]

whose integral kernel relative to \(\Phi(v)dv\) is \((u-v)/2\).

Integration by parts in \(KA_+\) also produces the endpoint term

\[
k(u,0)\Phi(0)f(0).
\]

The no-extra-seam-source prescription is therefore

\[
k(u,0)=0.
\]

## Integrating factor

Set

\[
m(u,v)=
\Phi(u)
\Phi(v).
\]

Since

\[
(\partial_v-
\partial_u)
\log m
=
\frac{\Phi'(v)}{
\Phi(v)}-
\frac{
\Phi'(u)}{
\Phi(u)},
\]

the PDE becomes

\[
(\partial_v-
\partial_u)(mk)
=
\frac12(u-v)m.
\]

The characteristics have constant \(u+v\). Starting at the boundary point \((u+v,0)\) and integrating to \((u,v)\) gives

\[
k_0(u,v)
=
\frac{
1
}{
2\Phi(u)
\Phi(v)
}
\int_0^v
(
 u+v-2t
)
\Phi(u+v-t)
\Phi(t)
\,dt.
\]

This is an explicit theta-source construction of the cross-storage kernel.

Although the displayed integral is oriented toward the `v=0` boundary, its numerator is symmetric in `u,v`. Indeed, the integrand is odd about the midpoint of the full interval `[0,u+v]`, so its full integral vanishes. Consequently the same numerator can always be evaluated over the shorter interval `[0,min(u,v)]`, after swapping `u,v` when necessary. This removes a severe cancellation instability and shows

\[
k_0(u,v)=k_0(v,u).
\]

## Homogeneous ambiguity

The general interior solution differs from \(k_0\) by

\[
k_H(u,v)
=
\frac{
H(u+v)
}{
\Phi(u)
\Phi(v)
},
\]

where \(H\) is arbitrary along characteristics.

The boundary condition \(k(u,0)=0\) forces \(H=0\). Hence \(k_0\) is the unique solution with no additional endpoint source.

## What has been achieved

The oppositely oriented Sylvester equation can be inverted without a stable semigroup integral. Its inverse is characteristic integration from the modular seam.

All terms in \(k_0\) come from:

- the completed theta weight;
- modular-seam incidence;
- the zeroth and first Clark moments.

No Xi zero data or fitted Gram matrices occur.

## Remaining analytic tests

The formula defines a formal integral operator. To be an admissible doubled storage block, it must satisfy:

1. boundedness on \(L^2(\Phi du)\);
2. the adjoint symmetry required by the doubled storage;
3. the contraction bound \(\|K\|\le1\);
4. compatibility of the diagonal KYP blocks with the distributed Green outputs.

A sufficient first test is the Hilbert--Schmidt estimate

\[
\int_0^\infty
\int_0^\infty
|k_0(u,v)|^2
\Phi(u)
\Phi(v)
\,du\,dv
<
\infty.
\]

If this integral diverges, the no-extra-seam prescription fails as a bounded storage. If it converges but the norm exceeds one, an additional positive diagonal storage correction is required.

A Nyström scout using the cancellation-free shorter-interval formula gives stable cutoff values

\[
\|K\|\approx 0.00244914,
\qquad
\|K\|_{HS}\approx0.00246410
\]

for cutoffs from `1` through `5`. This is strong numerical evidence that the characteristic solution is Hilbert--Schmidt and far inside the contraction ball. It is not an interval proof.

Checker:

`research/voevodsky/checkers/scout_clark_characteristic_cross_storage.py`

Result:

`research/voevodsky/results/clark-characteristic-cross-storage-scout.json`

## Disposition

The missing cross-storage is no longer only an abstract Sylvester solution. The canonical no-extra-seam candidate has the explicit kernel

\[
\frac{
1
}{
2\Phi(u)
\Phi(v)
}
\int_0^v
(
 u+v-2t
)
\Phi(u+v-t)
\Phi(t)
\,dt.
\]

Its boundedness and contraction norm are the next executable analytic gates.
