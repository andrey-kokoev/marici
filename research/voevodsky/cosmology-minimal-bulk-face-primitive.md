# Minimal bulk--face primitive for the triple-incidence p-normal gate

## Question

Can one controlled source-derived enlargement of the closed logarithmic carrier supply a non-tautological primitive \(H_p\) with

\[
dH_p=p\Xi_p
\]

for the triple-incidence circuit?

## Claim boundary

This packet works in the cleared local numerator carrier with fiber de Rham differential in coordinates

\[
u=q_1,\qquad v=q_2,\qquad q_3=u+v+p,
\]

holding \(p\) as a base parameter. It does not construct the full logarithmic denominator complex, the full Cayley--Menger face census, a resolved/Rees ordered-wall blow-up, a global contour, or a physical period.

## Disposition

The minimal enlargement adds one degree-one bulk generator

\[
H_p=pq_1\,dq_2.
\]

With the fiber differential, \(d_{\rm fib}p=0\), hence

\[
d_{\rm fib}H_p=p\,dq_1\wedge dq_2.
\]

The cleared logarithmic source identity identifies the target with the oriented circuit numerator:

\[
q_1\,dq_2\wedge dq_3-q_2\,dq_1\wedge dq_3+q_3\,dq_1\wedge dq_2
=p\,dq_1\wedge dq_2.
\]

Thus in the cleared carrier

\[
dH_p=p\Xi_p,
\qquad
\Xi_p=\omega_{12}-\omega_{13}+\omega_{23}.
\]

The higher differential is zero, so \(d^2=0\). The generic cited incidence point is away from \(K_{\rm CM}=0\), so the local \(E_{\rm CM}\) remains empty and stable. No circuit quotient is imposed.

Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), the vector \((1,-1,1)\) has rank \(1\). The boundary \(p\Xi_p\) lies in the proved \(p\)-supported submodule. Treating \(\Xi_p\) itself as a boundary would require division by \(p\), which is not used.

This revives the coefficient-level relative Bockstein candidate in the cleared numerator carrier, but it does not yet pass the denominator, full face, or physical-readout gates. The remaining tests are to promote the carrier to source-approved logarithmic denominators, complete the Cayley--Menger face census if the carrier is extended to \(K_{\rm CM}\) faces, and compare with the resolved/Rees ordered-wall blow-up and sewn chain transport.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_minimal_bulk_face_primitive.py`

Result:

- `research/voevodsky/results/cosmology_minimal_bulk_face_primitive.json`
