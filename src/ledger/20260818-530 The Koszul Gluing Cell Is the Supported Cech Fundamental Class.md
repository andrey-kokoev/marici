---
authors:
  - marici.Nima
date: 2026-08-18
---
# The Koszul Gluing Cell Is the Supported Cech Fundamental Class

## Correction

The target-side reciprocal promotion is not missing.  The global
Koszul--Čech checker proves that the 215-generator Entry-143 packet has a
canonical extended Čech realization, that the endpoint/(Q) filtration
remains strict, and that each (u_a^{-1}) occurs only in its legal
(S\setminus H) summand.

The remaining problem is the source-to-target supported comparison.

## Canonical two-variable comparison

Let

\[
A=R[x,u].
\]

Use the cohomological Koszul complex

\[
K(x,u):qquad
A\xrightarrow{d_0}A^2\xrightarrow{d_1}A,
\]

with

\[
d_0(a)=(xa,ua),
\qquad
d_1(b,c)=ub-xc.
\]

Use the Čech complex

\[
C(x,u):qquad
A\xrightarrow{\delta_0}A_x\oplus A_u
\xrightarrow{\delta_1}A_{xu},
\]

with

\[
\delta_0(a)=(a,a),
\qquad
\delta_1(B,C)=B-C.
\]

There is a canonical chain map

\[
\Phi:K(x,u)\longrightarrow C(x,u)
\]

given by

\[
\Phi_0(a)=a,
\qquad
\Phi_1(b,c)=\left(\frac b x,\frac c u\right),
\qquad
\Phi_2(a)=\frac a{xu}.
\]

Indeed,

\[
\Phi_1d_0(a)=(a,a)=\delta_0\Phi_0(a),
\]

and

\[
\Phi_2d_1(b,c)
=\frac{ub-xc}{xu}
=\frac b x-\frac c u
=\delta_1\Phi_1(b,c).
\]

## Interpretation of the former gluing cell

Entry 163's formal generator satisfied

\[
d\lambda=ug-xh.
\]

Under the comparison above, its geometric replacement is the supported
Čech top

\[
\boxed{
\lambda_{\rm geom}=\left[\frac1{xu}\right].
}
\]

Its two chart faces are (1/x) and (1/u), and its boundary is exactly the
mixed Koszul syzygy.  Thus the missing cell is neither a new global free
generator nor an existing absolute (Q)-cell.  It is the fundamental class
of the mixed support, visible only in the supported Čech category.

This also matches the mixed-ideal blowup of Entry 529: the overlap
(A_{xu}) records the tautological transition between its two affine
charts.

## What is proved

The coefficient-level source comparison is now canonical:

\[
K(x_3,u_3)
\longrightarrow
R\Gamma_{(x_3,u_3)}(A).
\]

It retains the overlap term, uses only chartwise inversions, and realizes
the primitive mixed syzygy without changing the absolute target.

## Remaining physical gate

The global Entry-143 Čech promotion has many labelled summands.  To obtain a
physical (D03) Beck--Chevalley cell one must still prove that

\[
\frac1{x_3},\qquad \frac1{u_3},\qquad \frac1{x_3u_3}
\]

land respectively in the prescribed occurrence, normal, and mixed-overlap
summands of the literal (D03) corridor, with its endpoint
corestrictions and reflection signs.  The displayed chain map proves the
local algebra, not that label-sensitive realization.

## Consequence

Forgetting support sends the Čech fundamental class into the contractible
absolute packet, explaining simultaneously:

- the absolute nullhomotopy of Entry 163;
- the nonzero associated supported grade;
- why adjoining a free scalar (lambda) was mistyped;
- why a physical class, if it exists, must be established before forgetting
  support.

## Evidence

- Entry 163: formal mixed syzygy and blowup provenance boundary;
- Entry 529: exceptional-support pushforward and the two-chart Čech source;
- `research/voevodsky/check_global_k6_koszul_cech_promotion.rs`: canonical
  target-side extended Čech realization.
