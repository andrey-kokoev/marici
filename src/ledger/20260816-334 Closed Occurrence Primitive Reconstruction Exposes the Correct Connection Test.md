---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Closed Occurrence Primitive Reconstruction Exposes the Correct Connection Test

## Record

Status: corrected exact rational reconstruction produced closed homogeneous
candidates for every coefficient of the two odd primitives \(H_{31}(n)\)
and \(H_{23}(n)\), including the previously omitted degree-eleven term.
The candidates reproduce the frozen pointwise solves and pass 60 held-out
exact evaluations. They obey

\[
\boxed{H_{23}(x,y,n)=-H_{31}(y,x,n).}
\]

An independent frozen-source finite-field certificate subsequently tested
the odd primitive against the even source-numerator projection at 1,582
valid points in each of three prime fields. All 9,492 occurrence identities
passed. This is strong finite validation, not a characteristic-zero symbolic
identity proof.

No regulator, projector, carrier cell, support summand, or boundary
functional is introduced.

## Deutsch--Popperian claim

The hard-to-vary candidate is

\[
H_{31}(x,y,n)=h_1n+h_3n^3+h_5n^5+h_7n^7+h_9n^9+h_{11}n^{11},
\qquad
H_{23}(x,y,n)=-H_{31}(y,x,n),
\]

where

\[
h_1=
\frac{
1727y^6+9026xy^5+19841x^2y^4+23548x^3y^3+
16001x^4y^2+5954x^5y+959x^6
}{32x^2y^2},
\]

\[
h_3=
-\frac{
1667y^5+6901xy^4+11640x^2y^3+10136x^3y^2+
4645x^4y+915x^5
}{16xy},
\]

\[
h_5=
\frac{
661y^4+2113xy^3+2643x^2y^2+1585x^3y+397x^4
}{8},
\]

\[
h_7=
-\frac{xy}{8}
\left(259y^3+613xy^2+535x^2y+181x^3\right),
\]

\[
h_9=
\frac{x^2y^2}{4}
\left(25y^2+41xy+21x^2\right).
\]

and the source audit supplies the missing highest term

\[
\boxed{
h_{11}=-\frac12x^3y^3(x+y).
}
\]

The finite falsifier is exact substitution into

\[
H_i'v-9xynH_i
=
P_i^{\rm even}-\frac{L_i}{xy}v^5.
\]

Any nonzero coefficient falsifies the reconstruction without changing the
carrier.

## Endpoint jets in closed form

Let

\[
N^2=\frac{2(x+y)}{xy},
\qquad
n_\sigma(w)=\sigma N
\sqrt{1+\frac{w^2}{2(x+y)}}.
\]

Writing \(H_i=\sum_{j=0}^5h_{i,2j+1}n^{2j+1}\), the five polar
coefficients of

\[
\Phi_i=\frac{H_i(n)}{8(xy)^{3/2}w^9}
\]

are

\[
\boxed{
J_{i,\sigma}^{(-9+2k)}
=
\frac{\sigma N}{8(xy)^{3/2}}
\sum_{j=0}^5
h_{i,2j+1}N^{2j}
\binom{j+\tfrac12}{k}
\frac1{[2(x+y)]^k},
\quad 0\le k\le4.
}
\]

This makes opposite-endpoint parity and additive sewing manifest.

## Typing correction for the connection frontier

The anti-diagonal kernel of the full addition morphism

\[
S:\mathcal R\oplus\mathcal R\to\mathcal R,
\qquad
S(\alpha,\beta)=\alpha+\beta,
\]

is connection-stable formally whenever both summands carry the same
Gauss--Manin connection: \(S\) is constant and
\(\nabla S=S\nabla\). Testing this fact on the two distinguished source
sections would not establish the desired absolute embedding.

The nontrivial finite question is instead:

\[
\boxed{
\text{Does the rank-two span of the two source-defined relative sections
close under the parameter Gauss--Manin connection?}
}
\]

If it closes, one may ask whether its sewn rank-one quotient maps
canonically into the algebraic \(\mathcal T_7\) kernel. If it does not
close, the period-line result of entry 245 survives but no rank-two
source-section subconnection exists.

## Classification

- existing carrier: unchanged occurrence wall and endpoint divisor;
- coefficient data: two reconstructed odd relative primitives through
  degree eleven;
- involution: occurrence exchange equals \(-(x\leftrightarrow y)\);
- endpoint jets: closed binomial formula through all five polar levels;
- formally stable object: kernel of the full addition morphism;
- uncomputed object: connection closure of the two distinguished source
  sections;
- direct elliptic image: zero;
- new carrier datum: none.

## Exact evidence

- \`research/benincasa/check_occurrence_jet_connection.rs\`;
- \`research/benincasa/occurrence-jet-connection.json\`;
- twelve source-graded homogeneous coefficient reconstructions;
- 60 exact held-out evaluations;
- independent three-prime frozen-source certificate over 4,746 valid
  kinematic points and 9,492 occurrence identities;
- warning-denied optimized Rust compilation.

## Next finite falsifier

1. Promote the finite-field source identity to a characteristic-zero
   coefficientwise proof if needed for global descent.
2. Expand the corrected closed endpoint jets and compute their \(x,y\) derivatives,
   including the moving endpoint \(N(x,y)\).
3. Test whether the two source-jet columns close under a rational
   \(2\times2\) connection matrix.
4. If closure holds, compute curvature and compare the induced sewn
   quotient connection with \(\omega_{\rm sewn}\).
5. If closure fails, record the first escaping jet direction and classify
   its source-derived geometric home before considering \(\mathcal T_7\).

## Outcome contract

~~~json
{
  "claim": "Closed homogeneous occurrence primitives are reconstructed and the correct nontrivial connection test is source-section span closure.",
  "status": "corrected_and_finite_field_source_certified",
  "closed_H31": true,
  "H23_relation": "-H31(y,x,n)",
  "highest_odd_degree": 11,
  "held_out_exact_checks": 60,
  "finite_field_source_identity_checks": 9492,
  "symbolic_source_identity": "uncomputed",
  "closed_five_level_jet_formula": true,
  "full_addition_kernel_stability": "formal_by_naturality",
  "source_section_span_connection_closure": "falsified_in_entry_247",
  "new_carrier_incidence": false,
  "next_experiment": "Promote the source identity to characteristic zero and construct the global corrected endpoint-jet connection."
}
~~~
