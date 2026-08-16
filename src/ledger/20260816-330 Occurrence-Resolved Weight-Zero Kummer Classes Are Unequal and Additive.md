---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Occurrence-Resolved Weight-Zero Kummer Classes Are Unequal and Additive

> Correction (entry 243): the individual formulas originally recorded for
> \(L_{31}\) and \(L_{23}\) were raw \(n^2\)-coefficients of
> \(R_i=P_i/v^4\), not de Rham residues. Higher projective-infinity powers
> contribute through the expansion of \(w^{-3}\). The corrected de Rham
> formulas below are selected by the exact derivative cokernel.

## Record

Status: the two literal lower-denominator terms have been expanded
independently through weight \(0\) before occurrence forgetting. Both have
generic nonzero punctured-wall Kummer classes. They are unequal, and their
sum reproduces entry 240 exactly.

This is an algebraic occurrence-resolved Laurent/cohomology statement. The
individual physical boundary currents remain noncanonical without a
source-fixed regulator hierarchy, as established in entries 231--232.
Individual finite-endpoint polar jets are not computed here.

No carrier cell, support summand, regulator choice, projector, or
normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{occurrence forgetting at weight }0\text{ is either multiplication by
two or cancellation of two equal Kummer classes.}
}
\]

The finite falsifier was the pair of projective-wall residues obtained from
the two source denominators separately.

## Frozen occurrence lift

In the \(q_{\mathcal G_{12}}\)-residue chart retain

\[
E_T=\tau^2,\qquad
a=y+\tau^2r,\qquad
b=x-\tau^2r+\tau^3n,
\]

and

\[
q_{\mathfrak g_{31}}=\tau^2r,\qquad
q_{\mathfrak g_{23}}=\tau^2(-r+\tau n).
\]

The common factors are

\[
q_{\mathfrak g_1}=2x-\tau^2(r+1)+\tau^3n,
\]

\[
q_{\mathfrak g_2}=2y+\tau^2(r-1),
\qquad
q_{\mathfrak g_3}=\tau^2(1+\tau n).
\]

The exact Cayley--Menger polynomial \(K\), source numerator
\(K_1^{\rm src}\), and Jacobian \(da\wedge db=\tau^5dr\wedge dn\) are
unchanged.

Each individual full term begins at weight \(-4\). Its weight-\(0\)
coefficient therefore requires the fourth normal coefficient, one layer
beyond the unsplit computation of entry 240.

## Exact bivariate calculation

The certificate expands the source expressions as an exact rational series
in \((\tau,r)\), with

\[
\tau^4D_{31}
=
\frac{1}{q_{\mathfrak g_1}q_{\mathfrak g_2}(1+\tau n)r},
\]

and

\[
\tau^4D_{23}
=
\frac{1}{
q_{\mathfrak g_1}q_{\mathfrak g_2}(1+\tau n)(-r+\tau n)}.
\]

It multiplies each by the frozen normalized expansion of

\[
-\frac12K_1^{\rm src}K^{-3/2}
\]

and extracts \([\tau^4r^{-1}]\). For every tested nonsingular point,

\[
\boxed{
R_{31}^{(0)}+R_{23}^{(0)}
=
\frac{
3n^2(x-y)(x+y)
\left(n^4x^2y^2-7n^2xy(x+y)+5(x+y)^2\right)}
{2xy\left(n^2xy-2x-2y\right)^2},
}
\]

exactly the normalized unsplit residue of entry 240.

## Projective-wall Kummer projection

Let

\[
a_0=xy,\qquad
v=a_0n^2-2(x+y),\qquad
w^2=v.
\]

The original test attempted to identify the \(n^2\) coefficient of
\(R_i^{(0)}\) with the coefficient of \([dn/w]\). Entry 243 shows that this
shortcut is invalid before higher projective-infinity powers cancel. For
the corrected de Rham invariant \(L_i\), write

\[
c_i=\frac{L_i}{8(xy)^{5/2}}.
\]

Exact interpolation after multiplication by \(v^4\) gives the raw
\(n^2\)-coefficients

\[
\boxed{
\operatorname{raw}_{n^2}R_{31}=\frac{3x+5y}{2y},
\qquad
\operatorname{raw}_{n^2}R_{23}=-\frac{5x+3y}{2x}.
}
\]

These are not the Kummer residues because each split form has higher powers
at projective infinity. Exact reduction modulo
\(d(H/w^9)\) instead gives

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

Therefore the corrected Kummer coefficients are

\[
\boxed{
c_{31}
=
-\frac{3x^2+7xy+6y^2}{16xy(xy)^{5/2}},
\qquad
c_{23}
=
\frac{6x^2+7xy+3y^2}{16xy(xy)^{5/2}}.
}
\]

Both are generically nonzero. They are neither equal nor negatives. Their
sum is

\[
\boxed{
c_{31}+c_{23}
=
\frac{3(x-y)(x+y)}{16(xy)^{7/2}},
}
\]

exactly the Kummer coefficient of entry 240.

## Cyclic occurrence orbits

Literal cyclic relabeling produces two distinct occurrence orbits:

\[
(\mathcal G_{12},\mathfrak g_{31})
\to(\mathcal G_{23},\mathfrak g_{12})
\to(\mathcal G_{31},\mathfrak g_{23}),
\]

and

\[
(\mathcal G_{12},\mathfrak g_{23})
\to(\mathcal G_{23},\mathfrak g_{31})
\to(\mathcal G_{31},\mathfrak g_{12}).
\]

The formulas transport by ordered relabeling. Each orbit carries the
Kummer sign monodromy of entry 241:

\[
T_s=-1,\qquad T_u=1,\qquad N=0.
\]

## Verdict

The equal-copy/cancellation alternatives are falsified:

\[
\boxed{
\text{occurrence forgetting at weight }0
=
\text{addition of two unequal nonzero Kummer classes}.
}
\]

The earlier projected factor \(2\) does not survive as a literal factor
\(2\) in this higher-normal full-integrand grade. The noncommutation found
at leading order in entry 230 persists through the first genuine Kummer
class. This is coefficient geometry over the existing marked collision
carrier; no new incidence is required.

## Classification

- existing carrier: unchanged marked lower divisors, exceptional wall,
  projective wall infinity, and cyclic occurrence labels;
- coefficient support: two unequal rank-one Kummer classes;
- occurrence forgetting: additive, not multiplicity two;
- unsplit checksum: exactly entry 240;
- monodromy: semisimple sign \(-1\), with \(N=0\);
- individual physical boundary currents: regulator-hierarchy dependent;
- individual finite endpoint jets: uncomputed;
- direct anticanonical infinity-Gysin image: still zero;
- genuinely new carrier datum: none.

## Exact evidence

- research/benincasa/check_split_occurrence_weight_zero.rs;
- research/benincasa/split-occurrence-weight-zero.json;
- 108 exact individual-sum checks against the frozen unsplit formula;
- six exact projective-infinity interpolations, independently validated
  outside their interpolation sets;
- warnings-denied optimized Rust compilation.

## Next finite falsifier

Compute the exact meromorphic reduction of each individual weight-\(0\)
wall form,

\[
\eta_i=c_i\frac{dn}{w}+d\Phi_i,
\]

and derive the principal parts of \(\Phi_i\) at both finite endpoints
\(w=0\).

Test whether the two endpoint-jet vectors:

1. add exactly to the unsplit jet of entry 240;
2. transport in the two cyclic occurrence orbits above;
3. remain regulator-independent as algebraic relative data even though the
   individual physical boundary currents do not.

Failure of endpoint sewing falsifies canonical occurrence-resolved global
assembly inside the coefficient object. It does not justify a new carrier
unless a missing source incidence is independently derived.

## Outcome contract

~~~json
{
  "claim": "Occurrence forgetting at weight 0 is multiplication by two or cancellation of equal Kummer classes.",
  "status": "falsified",
  "raw_n2_R31": "(3*x+5*y)/(2*y)",
  "raw_n2_R23": "-(5*x+3*y)/(2*x)",
  "L31_de_rham": "-(3*x^2+7*x*y+6*y^2)/(2*x*y)",
  "L23_de_rham": "(6*x^2+7*x*y+3*y^2)/(2*x*y)",
  "kummer_coefficient_rule": "c_i=L_i/(8*(x*y)^(5/2))",
  "sum": "3*(x-y)*(x+y)/(16*(x*y)^(7/2))*[dn/w]",
  "occurrence_forgetting": "additive_not_multiplicity_two",
  "cyclic_occurrence_orbits": 2,
  "individual_endpoint_jets": "uncomputed",
  "individual_physical_currents": "not_canonical_without_regulator_hierarchy",
  "new_carrier_incidence": false,
  "next_experiment": "Reduce each individual wall form to Kummer plus exact and compute its two finite endpoint polar jets."
}
~~~
