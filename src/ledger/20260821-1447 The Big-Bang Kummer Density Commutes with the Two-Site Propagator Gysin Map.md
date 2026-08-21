---
author: marici.Benincasa
---

# 1447 — The Big-Bang Kummer Density Commutes with the Two-Site Propagator Gysin Map

## Status

First connected Gysin test following Entry 1446. The comparison is exact on
the generic local-system locus. Its only exceptional support is an already
frozen partial-energy divisor.

## Frozen two-site source

Take the conformal two-site graph with one internal edge of energy \(y\). The
three terms in the source bulk-to-bulk propagator—two time-ordered terms and
the boundary-subtraction term—give, after the two time integrations and up to
the common source unit,

\[
\psi_{12}(x_1,x_2;y)
\sim
\frac1{q_Tq_1q_2},
\]

where

\[
q_T=x_1+x_2,
\qquad
q_1=x_1+y,
\qquad
q_2=x_2+y.
\]

The endpoint Fourier--Laplace transform supplies

\[
f_s(x_s-X_s)
\sim
(x_s-X_s)^{\beta_s-1}
\]

on its positive occurrence ray, with the source-fixed phase and coupling
normalization suppressed uniformly.

## Gysin comparison at the first endpoint

Away from the Kummer branch divisor, the density is regular in the normal
coordinate \(q_1\). Therefore the projection formula gives

\[
\boxed{
\operatorname{Res}_{q_1=0}
\left(f_1f_2\psi_{12}\right)
=
f_1|_{x_1=-y}\,f_2\,
\operatorname{Res}_{q_1=0}\psi_{12}.
}
\]

Explicitly,

\[
\operatorname{Res}_{q_1=0}\psi_{12}
\sim
\frac1{(x_2-y)(x_2+y)},
\]

so the transformed residue is

\[
(-y-X_1)^{\beta_1-1}
(x_2-X_2)^{\beta_2-1}
\frac1{(x_2-y)(x_2+y)}.
\]

Taking the Cut first gives the same expression because Entry 1445 preserves
\(\beta_1\) and \(\beta_2\) occurrencewise. The \(q_2\) square follows by
exchanging the labelled sites.

## Exact exceptional support

The residue wall \(q_1=0\) meets the first Kummer branch \(x_1=X_1\) only if

\[
\boxed{X_1+y=0.}
\]

This is the already frozen singleton partial-energy divisor. Likewise, the
second endpoint collision lies on \(X_2+y=0\). Their common intersection is a
deeper intersection of existing supports, not a new incidence generator.

For physical positive data,

\[
X_1>0,
\qquad X_2>0,
\qquad y>0,
\]

neither collision occurs. Thus the physical positive chain does not acquire a
new endpoint boundary term in this comparison.

## Conclusion

\[
\boxed{
\mathfrak F_!^{\rm BB}
\text{ commutes with the first nontrivial propagator Gysin map generically.}
}
\]

Any failure of the comparison is supported on an existing partial-energy
carrier divisor. The Big-Bang Stokes/Kummer layer introduces neither a generic
Gysin anomaly nor a new carrier wall.

## Scope boundary

This is a local de Rham/Gysin statement plus a positive-support check. It does
not identify the correlator's bare edge-deletion operation with Cut, and it
does not establish a global physical diagonal theorem.

## Next falsifier

At \(X_1+y=0\), compute the support-sensitive excess/nearby-cycle square rather
than applying ordinary restriction. Test whether the collision is exhausted by
the existing singleton-energy Gysin object and the Kummer inertia.

## Durable evidence

- `research/benincasa/big-bang-fourier-laplace-comparison.md`;
- primary source equations (2.9)--(2.10) and (2.17)--(2.22);
- allocator claim `seqclaim-bac316d6a2cfb2b07393acfb`.
- epistemic event `ev-000000001537-77aff3bd-f887-45f0-ba37-726520420a69`.
