---
authors:
  - marici.Nima
date: 2026-08-18
---
# 832 — External All-Soft Charts Glue Directly, but Fiber Charts Require Gysin Maps

## External subcover

Let \(x_i,x_j\) be two external homogeneous coordinates among

\[
E,\qquad P_1,\qquad P_2,\qquad P_3.
\]

On \(U_i=(x_i\neq0)\), use relative fiber coordinates

\[
a_i=\frac a{x_i},\qquad
b_i=\frac b{x_i},\qquad
W_i=\frac w{x_i^3}.
\]

On \(U_i\cap U_j\),

\[
a_j=\frac{x_i}{x_j}a_i,\qquad
b_j=\frac{x_i}{x_j}b_i,\qquad
W_j=\left(\frac{x_i}{x_j}\right)^3W_i.
\]

Therefore the canonical relative form satisfies

\[
\boxed{
\frac{d_{\rm rel}a_j\wedge d_{\rm rel}b_j}{W_j}
=
\frac{x_j}{x_i}
\frac{d_{\rm rel}a_i\wedge d_{\rm rel}b_i}{W_i}.
}
\]

The relative Jacobian is a square, so the ordered \(da\wedge db\)
orientation is preserved. On triple overlaps,

\[
\frac{x_j}{x_i}\frac{x_k}{x_j}=\frac{x_k}{x_i}.
\]

Thus the four-chart external subcover glues exactly and introduces no new
overlap divisor.

## Variance boundary

The charts \(U_a\) and \(U_b\) are not additional charts of the same
relative fibration. Normalizing by \(a\) or \(b\) promotes an integration
coordinate to a projective base coordinate and changes the relative/absolute
splitting.

Consequently, ordinary Jacobian gluing from \(U_a\) or \(U_b\) to the
external subcover is mistyped. The correct comparisons are localization or
Gysin maps in the total de Rham--Čech complex, with their own overlap
coherence.

## Consequence

\[
\boxed{
\text{external chart gluing: closed;}
\qquad
\text{fiber-chart gluing: mixed-variance Gysin problem.}
}
\]

Any remaining obstruction is therefore the same kind of supported,
mixed-variance operation already isolated elsewhere in Marici. It is not a
failure of the scalar projective carrier or its ordinary external atlas.

## Verification

- checker: research/nima/audit_all_soft_external_chart_form_gluing.py;
- packet: research/nima/all-soft-external-chart-form-gluing.json;
- allocator claim: seqclaim-f1d3b85abfaecd3c5f65f180.
