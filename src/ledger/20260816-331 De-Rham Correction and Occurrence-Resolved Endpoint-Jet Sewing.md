---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# De-Rham Correction and Occurrence-Resolved Endpoint-Jet Sewing

## Record

Status: the individual Kummer coefficients of entry 242 have been corrected
by an exact de Rham cokernel computation. The corresponding individual
weight-\(0\) primitives exist, are odd in the wall coordinate \(n\), and
sum exactly to entry 240's unsplit primitive. Hence each occurrence has
opposite finite-endpoint jets and the two jet vectors sew additively.

No physical current is assigned to either occurrence separately. The
regulator-hierarchy qualification of entries 231--232 remains in force.
No carrier datum or fitted support summand is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the raw }n^2\text{ coefficient of }R_i=P_i/v^4
\text{ is the individual Kummer residue.}
}
\]

The finite falsifier was failure of the exact derivative equation with that
coefficient. At \(x=1,y=2\), the raw value \(13/4\) left a nonzero cokernel
residual, while the exact de Rham value is \(-41/4\).

## Frozen individual form

For

\[
a=xy,\qquad s=x+y,\qquad v=an^2-2s,\qquad w^2=v,
\]

the occurrence-resolved wall form is represented as

\[
\eta_i
=
\frac{P_i(n)}{8a^{3/2}w^{11}}\,dn.
\]

The polynomial \(P_i\) is obtained from the exact bivariate source
expansion through weight \(0\). No interpolation is used to choose the
cohomology projector.

## Exact de Rham projector

Seek

\[
\eta_i
=
c_i\frac{dn}{w}
+
d\left(\frac{H_i(n)}{8a^{3/2}w^9}\right).
\]

After clearing the common factor, this is equivalent to

\[
\boxed{
H_i'v-9anH_i
=
P_i-\frac{L_i}{a}v^5,
\qquad
c_i=\frac{L_i}{8a^{5/2}}.
}
\]

The derivative operator has a one-dimensional cokernel at the degree-nine
resonance. Requiring exact solvability selects

\[
\boxed{
L_{31}^{\rm dR}
=
-\frac{3x^2+7xy+6y^2}{2xy},
\qquad
L_{23}^{\rm dR}
=
\frac{6x^2+7xy+3y^2}{2xy}.
}
\]

Their sum is unchanged:

\[
L_{31}^{\rm dR}+L_{23}^{\rm dR}
=
\frac{3(x-y)(x+y)}{2xy}.
\]

Thus entry 240's unsplit Kummer class survives exactly, while entry 242's
individual allocation required correction.

## Why the raw infinity extraction failed

The raw coefficients

\[
\frac{3x+5y}{2y},
\qquad
-\frac{5x+3y}{2x}
\]

are the \(n^2\)-coefficients of \(R_i=P_i/v^4\). Each split form also has
higher powers at projective infinity. When

\[
\eta_i=\frac{R_i}{8a^{3/2}w^3}\,dn
\]

is expanded in the actual local coordinate, those higher powers combine
with subleading terms of \(w^{-3}\) and contribute to the logarithmic
residue. The de Rham cokernel includes all such contributions.

The unsplit form has the higher powers cancelled already, which is why the
shortcut was valid for entry 240 but invalid occurrence by occurrence.

## Primitive and endpoint sewing

For each of six exact nonsoft pairs, the rational linear system produces a
polynomial \(H_i(n)\). Every even coefficient vanishes:

\[
\boxed{
H_{31}(-n)=-H_{31}(n),
\qquad
H_{23}(-n)=-H_{23}(n).
}
\]

At the two finite endpoints

\[
n=\pm N,\qquad N^2=\frac{2s}{a},\qquad w=0,
\]

the Laurent expansion of \(H_i(n)/w^9\) therefore has opposite principal
parts. Each occurrence has a canonical algebraic endpoint-jet vector of
the form

\[
(J_i,-J_i).
\]

The exact polynomial identity

\[
\boxed{
H_{31}+H_{23}
=
\frac{3(x-y)s}{2a}\,
nP_0(n^2)v^2,
}
\]

where

\[
P_0(u)
=
\frac{-4a^2u^2+23asu-24s^2}{6a},
\]

is precisely the entry-240 primitive rewritten over \(w^9\). Therefore

\[
\boxed{
J_{31}+J_{23}=J_{\rm unsplit}.
}
\]

The endpoint relative data sew before any physical boundary-value choice.

## Verdict

The raw-projective-coefficient conjecture is falsified and repaired:

\[
\boxed{
\text{individual Kummer projection}
=
\text{cokernel of the exact derivative operator},
}
\]

not coefficient extraction from \(R_i\) alone.

The repaired occurrence-resolved system still supports H2:

\[
\text{unchanged carrier}
+
\text{two unequal Kummer coefficient objects}
+
\text{additively sewn endpoint jets}.
\]

No new cosmological carrier incidence appears.

## Classification

- existing carrier: unchanged occurrence divisors, exceptional wall,
  projective wall infinity, and finite endpoint flags;
- corrected coefficient support: two unequal Kummer classes;
- individual primitives: exact and odd in \(n\);
- endpoint jets: opposite occurrence by occurrence;
- occurrence forgetting: additive at both cohomology and endpoint-jet
  levels;
- physical individual currents: still regulator-hierarchy dependent;
- direct anticanonical infinity-Gysin image: zero;
- genuinely new carrier datum: none.

## Exact evidence

- research/benincasa/check_split_occurrence_weight_zero.rs;
- research/benincasa/split-occurrence-weight-zero.json;
- research/benincasa/split-occurrence-endpoint-jets.json;
- six exact derivative-cokernel solves;
- six exact primitive-sum identities;
- thirty exact even-component cancellations in the summed primitive;
- zero even coefficients in either individual primitive on the tested
  pairs;
- warnings-denied optimized Rust compilation and exact artifact
  regeneration.

## Next finite falsifier

Derive closed symbolic formulas for \(H_{31}(n)\) and \(H_{23}(n)\), rather
than pointwise exact solves, and expand each at \(w=0\) through

\[
w^{-9},w^{-7},w^{-5},w^{-3},w^{-1}.
\]

Require:

1. coefficientwise addition to entry 240's displayed endpoint jet;
2. cyclic transport in both occurrence orbits of entry 242;
3. no regulator hierarchy in the algebraic jet map;
4. no new support or carrier component.

A failure of the closed symbolic sewing formula falsifies the present
finite-model extrapolation narrowly.

## Outcome contract

~~~json
{
  "claim": "The raw n^2 coefficient of R_i=P_i/v^4 is the individual Kummer residue.",
  "status": "falsified_and_corrected",
  "L31_de_rham": "-(3*x^2+7*x*y+6*y^2)/(2*x*y)",
  "L23_de_rham": "(6*x^2+7*x*y+3*y^2)/(2*x*y)",
  "sum_L": "3*(x-y)*(x+y)/(2*x*y)",
  "individual_primitive_parity": "odd",
  "endpoint_jets": "opposite_occurrence_by_occurrence",
  "primitive_sum": "exactly_entry_240",
  "physical_individual_currents": "regulator_hierarchy_dependent",
  "new_carrier_incidence": false,
  "next_experiment": "Derive closed H31 and H23 and their five endpoint polar coefficients."
}
~~~
