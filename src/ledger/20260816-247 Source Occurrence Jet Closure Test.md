---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Source Occurrence Jets Do Not Form a Flat Subconnection

## Record

Status: conditional on the closed occurrence primitives reconstructed in
entry 246, the moving-endpoint Gauss--Manin test has been computed exactly.
The two source-defined five-level endpoint-jet columns do not span a
connection-stable rank-two subbundle. Their sewn jet does not span a flat
rank-one relative line either.

The period-line theorem of entry 245 is unchanged. The failure occurs in
the endpoint extension data discarded by the Kummer period quotient.

No carrier stratum, endpoint counterterm, fitted summand, regulator, or
splitting is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\langle\widehat\eta_{31},\widehat\eta_{23}\rangle
\text{ is stable under the parameter Gauss--Manin connection.}
}
\]

The stronger sewn claim was

\[
\boxed{
\langle\widehat\eta_{31}+\widehat\eta_{23}\rangle
\text{ is a flat rank-one relative jet line.}
}
\]

Both are falsified in the frozen source normal coordinate

\[
w^2=xyn^2-2(x+y).
\]

## Frozen connection calculation

Use the closed primitive

\[
H_i(n)=\sum_{j=0}^4h_{i,2j+1}n^{2j+1}
\]

and endpoint branches

\[
n_\sigma(w)
=
\sigma\sqrt{\frac{2(x+y)}{xy}}
\sqrt{1+\frac{w^2}{2(x+y)}}.
\]

The exact certificate differentiates the five coefficients

\[
J_i=
\left(
J_i^{(-9)},J_i^{(-7)},J_i^{(-5)},J_i^{(-3)},J_i^{(-1)}
\right)
\]

at fixed \(w\). It includes the moving endpoint and the common prefactor

\[
C=\frac{N}{8(xy)^{3/2}},
\qquad
d\log C
=
\frac12d\log(x+y)-2d\log(xy).
\]

For each source column and each derivative \(\partial_x,\partial_y\), the
certificate solves for a putative linear combination of the two source
columns from two independent jet rows and checks the remaining rows.

## Rank-two closure falsifier

At each of six exact nonsoft points,

\[
(1,2),(1,3),(2,3),(2,5),(3,4),(3,5),
\]

all four derivatives

\[
\partial_xJ_{31},\quad
\partial_yJ_{31},\quad
\partial_xJ_{23},\quad
\partial_yJ_{23}
\]

escape the rank-two source span. Thus

\[
\boxed{
24/24\text{ exact source-section closure tests fail.}
}
\]

The first escaping row is \(J^{(-7)}\). The occurrence-exchange symmetry
pairs the residuals with opposite signs, so this is an algebraic
occurrence-allocation extension direction, not a new singular divisor.

## Sewn rank-one closure falsifier

For

\[
J_{\rm sewn}=J_{31}+J_{23},
\]

all twelve exact tests of

\[
\partial_xJ_{\rm sewn}
\stackrel?=\alpha_xJ_{\rm sewn},
\qquad
\partial_yJ_{\rm sewn}
\stackrel?=\alpha_yJ_{\rm sewn}
\]

fail. The first escape is delayed to \(J^{(-3)}\). Its residual is the same
for both parameter directions:

\[
\boxed{
\rho_{\rm sewn}^{(-3)}
=
\frac{17(y^2-x^2)}{8x^2y^2}.
}
\]

The certificate verifies this formula exactly at all twelve derivative
tests.

Therefore

\[
\boxed{
\text{horizontal sewn Kummer period line}
\not\Rightarrow
\text{horizontal sewn relative endpoint-jet line}.
}
\]

The first three polar levels \(w^{-9},w^{-7},w^{-5}\) are compatible with
a rank-one connection; the obstruction first appears at \(w^{-3}\).

## First connection saturation

At every tested point, the six columns

\[
J_{31},\quad J_{23},\quad
\nabla_xJ_{31},\quad\nabla_yJ_{31},\quad
\nabla_xJ_{23},\quad\nabla_yJ_{23}
\]

have rank five. Since the endpoint-jet fiber itself has rank five,

\[
\boxed{
\operatorname{Sat}^{(1)}_\nabla
\langle J_{31},J_{23}\rangle
=
\mathcal J_\partial^{(9)}
\quad\text{generically in the tested chart}.
}
\]

Thus the first Gauss--Manin derivative already generates the complete
five-level endpoint-jet tower. There is no intermediate rank-three or
rank-four source-section closure in this model.

This is a generic-rank statement on the six exact test fibers. A global
connection matrix and its discriminant extension remain uncomputed.

## Geometric home of the failure

The residual has poles only on

\[
xy=0,
\]

which is existing soft support, and a zero on

\[
x^2-y^2=0,
\]

which is the existing signed-energy/coefficient locus. It introduces no
new incidence divisor.

Its type is therefore

\[
\boxed{
\text{endpoint-jet extension data over the existing carrier},
}
\]

not elliptic data and not a new carrier generator. Its vanishing on the
same locus as the sewn Kummer numerator shows that the failure is internal
to the algebraic/Tate--Kummer extension sector.

The direct infinity-Gysin image remains zero, so the natural next question
is whether adjoining the source-derived escaping jet direction closes
inside the algebraic \(\mathcal T_7\) connection.

## Effect on the architecture

The result narrows H2:

\[
\text{shared carrier}
+
\text{sector-specific coefficient objects}
\]

survives, but the cosmological coefficient object cannot be replaced by
the direct sum of the elliptic quotient and the horizontal period lines.
The endpoint mapping cone carries a nontrivial extension visible before
physical boundary evaluation.

No canonical global splitting has been obtained.

## Classification

- existing carrier: exceptional occurrence wall and finite endpoint divisor;
- soft support: \(xy=0\);
- coefficient zero: \(x^2-y^2=0\);
- elliptic quotient: unchanged and absent from the direct jet image;
- Tate/Kummer quotient: horizontal only after period projection;
- extension data: first individual escape at \(w^{-7}\);
- sewn extension data: first escape at \(w^{-3}\);
- first connection saturation: full rank-five endpoint-jet tower;
- candidate algebraic home: \(\mathcal T_7\), not yet embedded;
- genuinely new carrier datum: none.

## Exact evidence

- \`research/benincasa/marici-gm/src/bin/occurrence_jet_closure.rs\`;
- \`research/benincasa/occurrence-jet-closure.json\`;
- 24 exact rank-two source-span tests;
- 12 exact sewn-line tests;
- 12 exact checks of
  \(17(y^2-x^2)/(8x^2y^2)\);
- six exact rank-five first-saturation checks;
- optimized Rust compilation.

## Qualifications

- The test is conditional on the entry-246 reconstructed formulas until
  their independent source-polynomial substitution is complete.
- The connection is computed in the source-defined \(w\)-normal
  trivialization.
- Failure of the selected source-section span does not imply failure of
  the full relative Gauss--Manin object.
- No identification with a coordinate of \(\mathcal T_7\) is claimed.

## Next finite falsifier

Construct the smallest connection saturation generated by

\[
J_{31},\qquad J_{23},\qquad
\nabla J_{31},\qquad\nabla J_{23}
\]

inside the five-level endpoint-jet module.

Then test:

1. its generic rank and flatness;
2. whether the sewn \(w^{-3}\) escape generates the missing direction;
3. whether the saturation embeds canonically into the algebraic
   \(\mathcal T_7\) kernel;
4. whether its singular support remains confined to the frozen energy
   arrangement and \(\mathcal Q\);
5. whether the resulting extension class is the first source-defined
   coordinate capable of carrying the unpublished \(L_1\) factor.

Failure to close inside source-derived algebraic coefficient data would
force the next search upstream. It does not justify a carrier modification
unless a missing source incidence is independently derived.

## Outcome contract

~~~json
{
  "claim": "The two source-defined occurrence jets span a flat rank-two subconnection, with a flat sewn rank-one relative line.",
  "status": "falsified_conditionally_on_entry_246_reconstruction",
  "source_span_tests": 24,
  "source_span_failures": 24,
  "individual_first_escape": "w^-7",
  "sewn_line_tests": 12,
  "sewn_line_failures": 12,
  "sewn_first_escape": "w^-3",
  "sewn_escape_formula": "17*(y^2-x^2)/(8*x^2*y^2)",
  "first_connection_saturation_rank": 5,
  "endpoint_jet_fiber_rank": 5,
  "period_line_survives": true,
  "geometric_home": "endpoint_jet_extension_over_existing_carrier",
  "candidate_absolute_home": "T7_algebraic_kernel_unproved",
  "new_carrier_incidence": false,
  "next_experiment": "Compute the minimal Gauss-Manin saturation of the occurrence jets and test canonical embedding into T7."
}
~~~
