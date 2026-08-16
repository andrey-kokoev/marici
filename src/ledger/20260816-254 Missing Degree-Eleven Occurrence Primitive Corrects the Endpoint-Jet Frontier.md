---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Missing Degree-Eleven Occurrence Primitive Corrects the Endpoint-Jet Frontier

## Record

A frozen-source audit found that entries 246 and 247 had truncated the odd
occurrence primitive at degree nine. The exact source solve has degree eleven:

\[
H_{31}^{\rm odd}
=
\sum_{j=0}^{5}h_{31,2j+1}n^{2j+1},
\qquad
h_{31,11}=-\frac12x^3y^3(x+y),
\]

and occurrence exchange gives

\[
h_{23,11}=+\frac12x^3y^3(x+y).
\]

This is a coefficient-object correction. No carrier cell, support summand,
normalization change, regulator, or fitted projector is introduced.

## Deutsch--Popperian claim tested

The frozen claim was that the degree-nine reconstruction was the complete
odd source primitive. The source solve supplies the finite falsifier:

\[
\boxed{[n^{11}]H_{31}^{\rm odd}\ne0.}
\]

Therefore the degree-nine completeness claim is falsified.

The corrected hard-to-vary claim is

\[
\boxed{
D H_i^{\rm odd}
=
P_i^{\rm even}
-
\frac{L_i}{xy}v^5,
\qquad
D=v\partial_n-9xyn,
}
\]

where

\[
v=xyn^2-2(x+y),
\qquad
P_i^{\rm even}(n)=\frac{P_i(n)+P_i(-n)}2.
\]

The parity projection is forced by type: \(D\) maps odd primitives to even
numerators. Testing an odd primitive against the full numerator mixes in
the separate even primitive sector.

## Independent source certificate

A new Rust verifier reimplements the frozen bivariate source series over
three prime fields:

\[
\mathbb F_{1000000007},\qquad
\mathbb F_{1000000009},\qquad
\mathbb F_{998244353}.
\]

On a side-twelve grid, after excluding soft, diagonal, and \(v=0\) points,
there are 1,582 valid triples per prime. At every valid triple it checks:

1. the corrected \(31\)-occurrence odd primitive identity;
2. the corrected \(23\)-occurrence odd primitive identity;
3. the frozen unsplit checksum.

Thus 9,492 occurrence identities and 4,746 unsplit identities pass. Exact
rational spot checks compare the independent finite-field source residues,
primitive coefficients, and identity components with the original frozen
solver.

This is a finite multi-prime certificate, not by itself a
characteristic-zero polynomial identity theorem.

## Recomputed connection result

The moving-endpoint closure calculation was rerun with the \(n^{11}\) term
included in every jet coefficient.

The main conclusions of entry 247 survive:

\[
24/24
\]

rank-two source-span tests fail, first at \(w^{-7}\);

\[
12/12
\]

sewn rank-one tests fail, first at \(w^{-3}\); and

\[
\rho_{\rm sewn}^{(-3)}
=
\frac{17(y^2-x^2)}{8x^2y^2}
\]

still passes all twelve exact checks. First derivative saturation still has
rank five at all six tested rational fibers.

The sewn formula is unchanged because the missing highest terms cancel
under occurrence sewing:

\[
h_{31,11}+h_{23,11}=0.
\]

Individual closure residuals change, but their occurrence-antisymmetric
typing and their first escaping row do not.

## Classification

- existing carrier: unchanged;
- soft support: \(xy=0\);
- signed-energy/coefficient locus: \(x^2-y^2=0\);
- corrected datum: degree-eleven algebraic endpoint coefficient;
- endpoint extension: full five-level jet tower after first connection
  saturation;
- elliptic quotient: unchanged;
- new carrier datum: none.

The defect and its repair both live inside the sector-specific algebraic
coefficient object. This updates H2 positively: the hostile audit required a
missing coefficient, not a missing incidence stratum.

## Evidence

- research/benincasa/check_occurrence_jet_connection.rs;
- research/benincasa/occurrence-jet-connection.json;
- research/benincasa/marici-gm/src/bin/occurrence_source_identity.rs;
- research/benincasa/occurrence-source-identity.json;
- research/benincasa/marici-gm/src/bin/occurrence_jet_closure.rs;
- research/benincasa/occurrence-jet-closure.json.

## Next finite falsifier

Promote the corrected source identity to a characteristic-zero
coefficientwise certificate, then construct the global rational connection
on the full five-level endpoint-jet saturation. Determine whether that
module embeds canonically into the algebraic \(\mathcal T_7\) kernel and
whether its singular support is exhausted by the frozen energy arrangement
and \(\mathcal Q\).

If the corrected source-derived module requires a pole away from those
loci, locate the first missing source datum. Do not add a carrier stratum
unless that datum is independently an incidence relation.

## Outcome contract

~~~json
{
  "claim": "The degree-nine odd occurrence primitive is complete.",
  "status": "falsified_and_corrected",
  "highest_odd_primitive_degree": 11,
  "h31_n11": "-x^3*y^3*(x+y)/2",
  "h23_n11": "+x^3*y^3*(x+y)/2",
  "finite_field_occurrence_identity_checks": 9492,
  "finite_field_unsplit_checks": 4746,
  "rank_two_closure_failures": 24,
  "sewn_line_failures": 12,
  "sewn_escape_formula_survives": true,
  "first_connection_saturation_rank": 5,
  "geometric_home": "algebraic_endpoint_coefficient_and_extension_over_existing_carrier",
  "new_carrier_incidence": false,
  "next_experiment": "Construct the characteristic-zero source certificate and global rational connection of the corrected endpoint-jet saturation."
}
~~~
