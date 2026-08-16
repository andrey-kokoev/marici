---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Global Endpoint-Jet Frame Has an Apparent Reciprocal-Quartic Divisor

## Record

The corrected occurrence jets of entries 254 and 247 generate the complete
five-level endpoint-jet fiber after one Gauss--Manin derivative. This entry
tests whether a natural source-derived five-column selection gives a
canonical global frame and whether its connection introduces intrinsic
singular support.

Freeze the ordered source frame

\[
\mathcal B=
\left(
J_{31},
J_{23},
\nabla_xJ_{31},
\nabla_yJ_{31},
\nabla_xJ_{23}
\right)
\]

in the wall chart (t=x/y). Its determinant is computed exactly:

\[
\boxed{
\det\mathcal B
=
\frac{525}{4194304}
\frac{(t-1)^3(t+1)^{10}}{t^{10}}
C_{\rm cyc}(t),
}
\]

where

\[
\boxed{
C_{\rm cyc}(t)
=
34363t^4+26308t^3-14526t^2+26308t+34363.
}
\]

The same quartic occurs in the denominators of both connection matrices
obtained from this frame.

It is not an intrinsic singularity of the endpoint-jet coefficient module.
It is the degeneracy divisor of this cyclic frame.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\mathcal B
\text{ is a global source-canonical frame of the endpoint-jet saturation.}
}
\]

The finite falsifier is

\[
\boxed{
\det\mathcal B|_{C_{\rm cyc}=0}=0.
}
\]

Thus the selected first-derivative columns do not define a global frame.

The stronger dangerous inference

\[
C_{\rm cyc}=0
\quad\Longrightarrow\quad
\text{new coefficient or carrier support}
\]

is also falsified by the ambient polar basis.

## Frozen construction

Write the corrected odd primitives as

\[
H_i(n)=\sum_{j=0}^{5}h_{i,2j+1}n^{2j+1},
\]

including

\[
h_{31,11}=-\frac12x^3y^3(x+y),
\qquad
h_{23,11}=+\frac12x^3y^3(x+y).
\]

At fixed square-root normal coordinate (w), use the five polar rows

\[
w^{-9},\quad w^{-7},\quad w^{-5},\quad w^{-3},\quad w^{-1}.
\]

The calculation includes the moving endpoint and common Kummer prefactor

\[
C=\frac{N}{8(xy)^{3/2}},
\qquad
d\log C
=
\frac12d\log(x+y)-2d\log(xy).
\]

Homogeneity converts the two-parameter derivatives to exact rational
operations in (t=x/y). The Rust certificate computes (detmathcal B),
inverts (mathcal B), and constructs

\[
A_x=\mathcal B^{-1}\nabla_x\mathcal B,
\qquad
A_y=\mathcal B^{-1}\nabla_y\mathcal B.
\]

An independent exact rational calculation reproduces the displayed
determinant factorization.

## Why the reciprocal quartic is apparent

Before choosing source-generated columns, the complete endpoint-jet module
has the fixed polar-row basis

\[
e_{-9},e_{-7},e_{-5},e_{-3},e_{-1}.
\]

In that basis the connection is the common Kummer connection induced by
(C). Its support in the (t)-chart is confined to

\[
t(t+1)=0,
\]

together with the complementary (y=0) chart boundary. There is no pole on
(C_{\rm cyc}=0).

The matrices (A_x,A_y) acquire (C_{\rm cyc}^{-1}) only because their
definition uses (mathcal B^{-1}). Returning to the fixed polar basis
removes that pole. Therefore

\[
\boxed{
C_{\rm cyc}=0
\text{ is a cyclic-frame degeneracy, not intrinsic coefficient support.}
}
\]

The linear factors have the expected interpretation:

- (t=0): soft support (x=0);
- (t=-1): the existing (x+y=0) signed-energy boundary;
- (t=1): the occurrence-symmetric locus (x-y=0), where this selected
  source frame degenerates.

The homogeneous reciprocal quartic is

\[
\begin{aligned}
\widetilde C_{\rm cyc}(x,y)
={}&34363(x^4+y^4)
+26308xy(x^2+y^2)\\
&-14526x^2y^2.
\end{aligned}
\]

Its divisor need not be added to the carrier or to the intrinsic singular
support of the coefficient module.

## Relation to the search for \(\mathcal Q\)

This quartic is not identified with the source algebraic quartic
(mathcal Q). It arises after restricting to the finite endpoint wall and
choosing a particular cyclic derivative frame. Its pole disappears under a
known gauge change.

Consequently it cannot be the geometric home of (mathcal Q), whose
provenance remains confined to the algebraic (mathcal T_7) connection or
the extension between (mathcal T_7) and the elliptic quotient.

The result removes one false positive from that search:

\[
\boxed{
\text{Wronskian/frame divisor}
\not\Rightarrow
\text{period-system singular support}.
}
\]

## Classification

- endpoint wall and polar rows: existing carrier/coefficient geometry;
- intrinsic endpoint-jet connection support: soft and signed-energy support;
- (x-y=0): source-frame degeneracy on an existing occurrence-symmetric
  locus;
- (widetilde C_{\rm cyc}=0): apparent cyclic-frame divisor;
- (mathcal Q=0): not generated or explained by this frame;
- new carrier datum: none;
- canonical global source frame from first derivatives: falsified.

## Evidence

- research/benincasa/marici-gm/src/bin/endpoint_jet_global_connection.rs;
- research/benincasa/endpoint-jet-global-connection.json;
- warning-denied optimized Rust execution;
- exact rational determinant factorization;
- identical residual quartic in both frame connection directions;
- explicit regular ambient polar basis.

## Next finite falsifier

Do not try to repair (mathcal B) by replacing columns after seeing its
determinant.

Instead compare the intrinsic endpoint-jet module with the source-defined
algebraic Gysin kernel

\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle
\subset\mathcal T_7.
\]

The next test is to construct a typed morphism from the endpoint mapping
cone, not from the failed cyclic frame, into (mathcal A_{--}). Compute
its induced connection and require every genuine pole to lie on the frozen
energy arrangement or (mathcal Q).

If no such source-defined morphism exists, the endpoint extension remains
relative coefficient data with no canonical absolute (mathcal T_7)
coordinate. That falsifies the proposed embedding narrowly without changing
the carrier.

## Outcome contract

~~~json
{
  "claim": "The first-derivative source columns define a canonical global frame of the five-level endpoint-jet saturation.",
  "status": "falsified_by_reciprocal_quartic_frame_degeneracy",
  "determinant": "525*(t-1)^3*(t+1)^10*C_cyc(t)/(4194304*t^10)",
  "C_cyc": "34363*t^4+26308*t^3-14526*t^2+26308*t+34363",
  "C_cyc_type": "apparent_cyclic_frame_divisor",
  "intrinsic_endpoint_connection_support": "soft_and_signed_energy_only",
  "Q_identified": false,
  "new_carrier_incidence": false,
  "canonical_first_derivative_frame": false,
  "next_experiment": "Construct or finitely falsify a typed endpoint-mapping-cone morphism into the algebraic Gysin kernel <e6,v_alg>."
}
~~~
