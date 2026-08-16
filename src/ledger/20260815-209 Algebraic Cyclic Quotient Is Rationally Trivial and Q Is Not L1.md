---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Algebraic Cyclic Quotient Is Rationally Trivial and \(\mathcal Q\) Is Not \(L_1\)

## Record

Date: 2026-08-15

Status: exact generic finite-field de Rham certificate for the algebraic
Gysin plane and its cyclic rank-one quotient. The off-diagonal extension,
discriminant extension, integral normalization, and physical relative chain
remain open.

This entry continues entries 150, 169, 183, 199, and 207. It adds no
denominator, support component, fitted projector, splitting, or carrier cell.

## Deutsch--Popperian conjecture tested

Entry 207 proves that the explicit Gysin kernel
\[
\mathcal A_{--}=\langle e_6,v_{\rm alg}\rangle
\]
is connection-stable. The hard-to-vary claim was that the cyclic
last-three-master quotient selects the source algebraic line
\[
L_1\stackrel?\sim_{\rm rat}
\partial-\frac12d\log(-\mathcal Q).
\]

Freeze
\[
u=E_T,\qquad y=X_2=\frac{u+v}{2}-1
\]
on the projective chart \(X_1=1\), together with the source quartic
\(\mathcal Q\) and the explicit vector \(v_{\rm alg}\). No gauge factor
was chosen after seeing the connection.

The finite falsifier was either:

1. failure of \(\mathcal A_{--}\) to close under both bivariate
   derivatives; or
2. a unique nonzero \(d\log\mathcal Q\) coefficient in the induced cyclic
   quotient.

## Exact algebraic-plane connection

In the ordered basis \((e_6,v_{\rm alg})\), write
\[
d
\begin{pmatrix}e_6\\v_{\rm alg}\end{pmatrix}
=
\begin{pmatrix}
g_{00}&g_{01}\\
g_{10}&g_{11}
\end{pmatrix}
\begin{pmatrix}e_6\\v_{\rm alg}\end{pmatrix}.
\]

At 1,024 generic points and in both independent directions:

\[
\text{closure residual}=0,
\qquad
g_{01}=0,
\qquad
g_{10}\ne0
\]
at every tested direction.

Thus \(\langle e_6\rangle\) is a flat subline, while
\(v_{\rm alg}\) defines the cyclic rank-one quotient modulo that subline.
The static vector \(v_{\rm alg}\) is not itself horizontal, exactly as
allowed in entry 150.

## Unique dlog decomposition

The predeclared divisor basis was
\[
u, v, y, 1-y, 1+y, v-u, y-u^2, y+u^2, \mathcal Q.
\]
Its sampled logarithmic-derivative matrix has full rank nine. Therefore the
coefficient vector is unique over the test field.

The induced quotient connection is
\[
\boxed{
g_{11}
=d\log(v-u)+d\log(y-u^2)+d\log(y+u^2)
}
\]
or
\[
\boxed{
g_{11}=d\log\!left((v-u)(y^2-u^4)\right).
}
\]

The unique weight of \(d\log\mathcal Q\) is
\[
\boxed{0}.
\]

The identity passes all 2,048 directional validations with zero mismatch over
\[
\mathbf F_{2^{61}-1}.
\]

Since
\[
v-u=-2X_3,
\]
the gauge factor is composed entirely from existing site-energy and
algebraic-kernel divisors:
\[
(v-u)(y^2-u^4)
=-2X_3(X_2^2-E_T^4).
\]
Rescaling the quotient generator by its inverse trivializes the generic
connection rationally.

## Falsification

The conjecture
\[
L_1\sim_{\rm rat}\partial-\frac12d\log(-\mathcal Q)
\]
is falsified on the generic bivariate de Rham locus.

More strongly, the cyclic algebraic quotient carries no \(\mathcal Q\)
weight in a full-rank source-divisor dlog census. The published scalar
factor \(L_1\), when interpreted as this cyclic quotient, is rationally
gauge-trivial and supported only on the already present factors above.

This does not remove \(\mathcal Q\) from the full coefficient system.
It localizes its remaining possible provenance to the off-diagonal extension
one-form \(g_{10}\), to another algebraic block outside this quotient, or to
extension across the discriminant.

## Classification

\[
\boxed{
\text{existing energy/algebraic coefficient divisors}
+
\text{rationally trivial rank-one quotient}.
}
\]

No new carrier datum is required. The result strengthens H2 and rejects the
specific \(\mathcal Q=L_1\) identification.

## Scope boundary

Not proved:

- rational exactness or nontriviality of the off-diagonal extension
  \(g_{10}\);
- whether \(\mathcal Q\) controls that extension;
- extension through the discriminant locus;
- integral lattice normalization;
- compatibility with the physical relative integration chain;
- analogous closure in the remaining five masters or the full 34-master
  system.

Generic rational triviality of the quotient is not a splitting theorem for
the algebraic plane or the nine-master sequence.

## Exact evidence

- `research/benincasa/marici-gm/src/main.rs`;
- `research/benincasa/marici-gm/algebraic-line-certificate.json`;
- ignored raw run `algebraic-dlog-1024.json`, SHA-256
  `d2cfbfde5c42d25c9fe7716a4f3d3a052d8bbe92665bf09cc5f70ea27468983b`;
- factor-matrix rank: \(9\);
- 1,024 generic points and 2,048 directional validations;
- validation mismatches: \(0\).

## Next hostile falsifier

Rationally trivialize both diagonal lines of \(\mathcal A_{--}\), transport
\(g_{10}\) into the resulting extension one-form \(\eta\), and compute
its class in
\[
H^1_{\rm dR}
\left(
U,
\operatorname{Hom}(\mathcal L_{\rm quot},\mathcal L_{e_6})
\right).
\]

Predeclare the frozen source divisor arrangement, including \(\mathcal Q\).
Test whether \(\eta\):

1. is rationally exact, in which case the algebraic plane splits generically;
2. has a nonzero residue on \(\mathcal Q=0\), placing \(\mathcal Q\) in
   the extension class;
3. has support only on existing energy/Cayley--Menger divisors; or
4. requires a genuinely absent divisor.

Only the last outcome permits a new carrier proposal.

## Outcome contract

~~~json
{
  "claim": "The cyclic algebraic quotient is the Q Kummer line with connection one-half dlog(-Q).",
  "status": "falsified_generic_bivariate_de_rham",
  "prime": "2305843009213693951",
  "sample_points": 1024,
  "directions": 2048,
  "algebraic_plane_closure_residual": 0,
  "e6_subline_stable": true,
  "v_alg_to_e6_mixing": true,
  "factor_matrix_rank": 9,
  "quotient_connection": "dlog((v-u)(y-u^2)(y+u^2))",
  "Q_weight": 0,
  "validation_mismatches": 0,
  "generic_quotient_rationally_trivial": true,
  "new_carrier_datum": false,
  "next_experiment": "Gauge-normalize the algebraic plane and compute the de Rham class and divisor support of its off-diagonal extension one-form."
}
~~~
