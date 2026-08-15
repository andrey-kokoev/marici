---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Generic Lower Radical Has No Literal Physical-Sheet Picard--Lefschetz Jump

## Record

Date: 2026-08-15

Status: generic nonsoft physical-chain classification for one frozen lower-sector radical.

This entry continues entries 180, 181, and 185. It changes no source denominator, normalization, marked support, coefficient summand, integration chain, or carrier cell.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{a generic lower-sector Cayley--Menger radical has nonzero
Picard--Lefschetz variation on the literal source-weighted Bunch--Davies chain.}
}
\]

Freeze the literal six-term three-site source form, the positive Cayley--Menger integration domain, and the Bunch--Davies boundary value before computing. The finite falsifier is either:

1. cancellation of the local vanishing-period coefficient after the six source terms are assembled; or
2. zero intersection of the resulting vanishing thimble with the literal physical chain.

The first falsifier fails. The second succeeds.

## Frozen source form

The three-site one-loop source integrand is

\[
I=\kappa_0\int_\Gamma\prod_e(dy_e\,y_e)\,
\frac{K^\chi}{q_{\mathcal G}\prod_{j=1}^3q_{\mathfrak g_j}}
\left[
\frac1{q_{\mathcal G_{12}}}
\left(\frac1{q_{\mathfrak g_{23}}}+\frac1{q_{\mathfrak g_{31}}}\right)
+\text{cyclic}
\right],
\]

with all six source coefficients equal to (+1). For (d=3), three sites, and one loop,

\[
\chi=-\frac12.
\]

The source contour is the positive-oriented Cayley--Menger domain: loop edge weights are nonnegative, and the simplex and face volumes are nonnegative. The Bunch--Davies prescription gives all energies a common small negative imaginary part. This prescription is fixed by positivity and preservation of orientation in Albayrak--Benincasa--Duaso Pueyo, arXiv:2305.19686.

## Frozen radical and local model

Take the double residue

\[
q_{\mathfrak g_1}=q_{\mathfrak g_2}=0.
\]

Writing the three loop weights as (a,b,c), the residue equations are

\[
a=-X_2-c,
\qquad
b=-X_1-c.
\]

The restricted Cayley--Menger polynomial is quadratic,

\[
K_r(c)=Ac^2+Bc+C,
\]

with discriminant

\[
\Delta_{12}^{-}
=
-4(P_1^2-X_1^2)(P_2^2-X_2^2)
\Lambda(P_1^2,P_2^2,P_3^2)
\bigl(P_3^2-(X_1-X_2)^2\bigr).
\]

Isolate the generic component

\[
R=P_3-X_1+X_2=0
\]

away from all other factors and source poles. At its double root (c_*),

\[
K_r
=
A\left[
(c-c_*)^2-\frac{\Delta_{12}^{-}}{4A^2}
\right].
\]

## Literal cyclic source weight

Substitution of the complete six-term source sum, including the common measure numerator and all remaining denominators, gives a local coefficient (H_*). Exact symbolic reduction proves

\[
H_*|_R\neq0
\]

generically, and likewise on the conjugate component (P_3+X_1-X_2=0).

Hence the vanishing-cycle period at (chi=-1/2) is

\[
\int_\delta \frac{H_*\,dc}{\sqrt{K_r}}
=
C_0\frac{H_*}{\sqrt A},
\qquad C_0\neq0.
\]

There is no cancellation among the six literal cyclic source terms.

## Physical-chain intersection

At the positive-energy Bunch--Davies base point,

\[
a\ge0,qquad b\ge0,qquad c\ge0
\]

on (Gamma_{\rm phys}). But the frozen residue equations require

\[
a+c=-X_2,
\qquad
b+c=-X_1.
\]

Their real parts are strictly negative for (X_1,X_2>0). Therefore

\[
\overline\Gamma_{\rm phys}
\cap
\{q_{\mathfrak g_1}=q_{\mathfrak g_2}=0\}
=
\varnothing .
\]

The common negative imaginary energy displacement preserves this separation and fixes the physical boundary value. Thus the dual vanishing thimble has zero intersection with the literal physical chain:

\[
\boxed{
\nu_{\rm phys}
=
\langle\Gamma_{\rm phys},\delta^\vee\rangle
=
0.
}
\]

Picard--Lefschetz therefore gives

\[
\boxed{
\operatorname{Var}_{R}
(\Gamma_{\rm phys})
=
\nu_{\rm phys}\,\delta
=
0.
}
\]

This does not erase the local radical. It says that its nonzero vanishing period belongs to an analytically continued sheet reached after crossing the frozen pole geometry, not to the literal positive Bunch--Davies sheet.

## Classification

For the selected generic lower radical:

- existing energy/Cut carrier: sufficient;
- Cayley--Menger coefficient support: yes;
- local analytically continued vanishing period: nonzero;
- literal physical-sheet Picard--Lefschetz variation: zero;
- soft support: excluded;
- graph homology: not invoked;
- new carrier datum: none.

The surviving narrow statement is

\[
\boxed{
\text{generic lower radicals are coefficient support whose physical
activation is sheet-sensitive; algebraic presence does not imply a
literal Bunch--Davies-chain jump.}
}
\]

This strengthens H2 while preserving the distinction

\[
\text{coefficient discriminant}
\not\Rightarrow
\text{physical-cycle monodromy}.
\]

## Scope boundary

The result is for the isolated mixed component of the frozen
(q_{\mathfrak g_1}=q_{\mathfrak g_2}=0) lower sector, at generic nonsoft
kinematics. It does not claim that every factor of every generic lower
radicand has zero physical variation. Endpoint and face pinches, and
components whose Landau locus meets the positive Cayley--Menger domain,
remain separate tests.

## Exact evidence

- `research/benincasa/check_generic_lower_physical_variation.py`
- `research/benincasa/generic_lower_physical_variation_result.json`
- `research/benincasa/generic_lower_physical_variation_run.log`
- primary source: Benincasa et al., arXiv:2408.16386, equation
  `eq:Triangle`, together with `eq:ukchi` and the source contour
  definition;
- boundary-value prescription: Albayrak, Benincasa, Duaso Pueyo,
  arXiv:2305.19686.

## Next finite falsifier

The next attack must select a lower-sector radical component whose critical
residue locus can meet the closure of the positive Cayley--Menger domain.
Freeze one endpoint or face-pinch component before calculation, compute its
oriented Landau signs, and test whether the literal six-term source weight
survives on a thimble with

\[
\langle\Gamma_{\rm phys},\delta^\vee\rangle\neq0.
\]

No carrier modification is admissible.

## Outcome contract

~~~json
{
  "claim": "The selected generic mixed lower-sector radical produces nonzero Picard-Lefschetz variation on the literal Bunch-Davies chain.",
  "status": "falsified",
  "local_vanishing_period": "nonzero",
  "cyclic_source_cancellation": false,
  "physical_intersection_number": 0,
  "physical_variation": 0,
  "analytic_continuation_sheet_variation": "nonzero when the corresponding thimble is crossed",
  "classification": "Cayley-Menger coefficient support with sheet-sensitive activation",
  "new_carrier_datum": "none",
  "next_experiment": "Choose a frozen endpoint or face-pinch lower radical whose Landau locus meets the positive Cayley-Menger closure and compute its oriented physical intersection."
}
~~~
