---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Boundary-Value Leray Uniqueness and the Canonical Physical Residue Germ

## Record

Date: 2026-08-15

Status: local uniqueness theorem for the source-defined physical
\(q_{\mathcal G_{12}}\)-residue germ; generic-\(\mathcal Q\) variation not
yet computed.

This entry continues entry 178. It changes no denominator, normalization,
marked section, support summand, resolution, or carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was:

\[
\boxed{
\text{the published negative-imaginary boundary value and the literal
positive Cayley--Menger chain determine at most one admissible local
Leray residue germ.}
}
\]

“Admissible” was frozen before the test to mean analytic continuation of
the source integral germ. It does not permit adding an arbitrary absolute
cycle after inspecting a target monodromy.

The finite falsifier was either:

1. two nonhomotopic continuations inside the published
   negative-imaginary tube with identical endpoints; or
2. an unfixed square-root sheet, residue Jacobian, orientation, or
   multiplicity on a generic transverse \(q_{\mathcal G_{12}}=0\) patch.

## Frozen primary-source data

Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686v2, equations
(4.18)--(4.20), sends every external and internal energy to a value with
negative imaginary part. The prescription follows from positivity and
orientation of the cosmological polytope.

Benincasa--Vazão, arXiv:2402.06558, equations (3.1), (3.4), and
(3.6)--(3.9), defines the loop integral over the oriented Euclidean
Cayley--Menger region. The measure is positive in its interior and the
boundary is the vanishing Cayley--Menger volume together with the required
signed-minor conditions.

Benincasa et al., arXiv:2408.16386v2, equations (57)--(58), fixes the
three-site polar coordinate literally as

\[
q_{\mathcal G_{12}}=E+y_{12}.
\]

Hence

\[
dq_{\mathcal G_{12}}=dy_{12}
\]

and the residue Jacobian is one.

## Uniqueness calculation

The simultaneous conditions

\[
\operatorname{Im}x_s<0,\qquad
\operatorname{Im}y_e<0
\]

define a convex tube \(T_-\). Therefore two paths in \(T_-\) with the same
endpoints are homotopic.

On the real physical chain, positivity of the loop measure fixes

\[
w=+\sqrt K
\]

and the standard loop-edge orientation. These data have unique analytic
continuation inside \(T_-\) away from the already frozen discriminant.

Moreover \(\operatorname{Im}q_{\mathcal G_{12}}<0\). The source boundary
value therefore gives

\[
\frac1{q-i0}
=
\operatorname{PV}\frac1q+i\pi\delta(q),
\qquad
\operatorname{Disc}\frac1{q-i0}
=
2\pi i\,\delta(q).
\]

At

\[
y_{12}=-E,\qquad a=y_{23},\qquad b=y_{31},
\]

the induced residue chain is consequently the continued positive
Cayley--Menger section

\[
\Gamma_E^{\rm res}:
\quad
K_0(a,b)\ge0,\quad
\text{all source-required signed minors}\ge0,\quad
w=+\sqrt{K_0(a,b)},
\]

with orientation \(da\wedge db\) and multiplicity one.

Adding a closed class on the residue surface would change the source period
germ. It is not a second analytic continuation of the frozen chain and is
therefore not admissible.

## Result

Neither falsifier occurs on a generic transverse patch. Thus

\[
\boxed{
\text{the published data uniquely determine the local physical }q_{\mathcal G_{12}}
\text{-residue germ up to ordinary relative homology.}
}
\]

The missing-datum diagnosis in entry 178 was too strong locally. The source
does not print a separate Leray-cycle worksheet, but its boundary-value
prescription and oriented integration chain already determine the local
sheet, orientation, Jacobian, and multiplicity.

## Scope boundary

This theorem does not compute

\[
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys}^{\rm res}).
\]

The convex tube fixes the starting germ. A loop around generic
\(\mathcal Q=0\) must still be transported in a simultaneous resolution of
the frozen marked pair. The previous exact results remain in force:

- \(\mathcal Q\) is absent from the pure elliptic quotient;
- \(\mathcal Q\) is absent from the absolute residue-surface discriminant;
- \(\mathcal Q\) is absent from the generic algebraic Gysin line;
- two transverse exact coefficient connections are regular at
  \(\mathcal Q=0\).

Therefore nonzero physical variation, if present, must be a moving-relative-
chain or extension effect. Zero variation is not inferred here.

## Classification

- existing carrier: unchanged energy/Cut carrier, Cayley--Menger domain,
  residue surface, frozen pole curves, minor boundary, and infinity;
- newly established source datum: canonical local boundary-value residue
  germ;
- coefficient support: unchanged;
- unresolved: generic-\(\mathcal Q\) transport of that germ;
- new carrier datum: none.

The refined H2 architecture survives.

## Exact evidence

- \`research/benincasa/published_boundary_value_leray_uniqueness.md\`

## Next finite falsifier

Construct a simultaneous log resolution of the already frozen
\(q_{\mathcal G_{12}}\)-residue pair over a transverse disk to generic
\(\mathcal Q=0\). Lift the canonical germ just derived and compute its
Picard--Lefschetz variation.

The admissible outcomes are:

\[
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys}^{\rm res})=0
\]

so \(\mathcal Q\) is apparent for this sector, or

\[
\operatorname{Var}_{\mathcal Q}(\Gamma_{\rm phys}^{\rm res})\ne0
\]

with the variation classified inside the frozen relative coefficient
geometry. A new carrier datum is allowed only if the frozen resolved pair
cannot carry the variation.

## Outcome contract

~~~json
{
  "claim": "The published negative-imaginary energy prescription and oriented positive Cayley-Menger chain uniquely determine the local q_G12 Leray residue germ, including sheet, orientation, Jacobian, and multiplicity.",
  "status": "survived",
  "residue_sheet": "positive Cayley-Menger square-root germ",
  "residue_orientation": "da wedge db",
  "residue_multiplicity": 1,
  "local_lift_unique": true,
  "generic_Q_variation_computed": false,
  "classification": "canonical_source_defined_local_relative_germ_on_existing_carrier",
  "new_carrier_datum": "none",
  "next_experiment": "Lift the canonical germ to a simultaneous resolution over a generic transverse Q=0 disk and compute its Picard-Lefschetz variation."
}
~~~
