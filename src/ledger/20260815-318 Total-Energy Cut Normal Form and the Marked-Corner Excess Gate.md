---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Total-Energy Cut Normal Form and the Marked-Corner Excess Gate

## Record

Status: exact frozen-polynomial normal-form theorem and finite falsification of
depth-two Rees sufficiency for the physical Cut--nearby comparison at the
nonsoft marked corners.

This entry continues entries 161, 180, 199, and 220. It uses the literal
source normalization

\[
q_{\mathcal G_{12}}=E_T+y_{12},
\qquad dq_{\mathcal G_{12}}=dy_{12},
\]

the canonical Leray germ of entry 180, and the frozen Cayley--Menger family.
It adds no denominator, support summand, projector, normalization, marked
section, or carrier cell.

## Deutsch--Popperian claim tested

The hard-to-vary claim was:

\[
\boxed{
\text{the predeclared nearby/Gysin/excess calculus through second
\(E_T\)-Rees grade controls the Cut specialization at every nonsoft marked
intersection.}
}
\]

The finite falsifier was a source-forced marked intersection at which both the
first and second normal coefficients vanish while a higher coefficient is
nonzero.

## Frozen Cut family

Take the source nonseparating Cut

\[
\operatorname{Cut}_{12}
=\operatorname{Res}_{q_{\mathcal G_{12}}=0}.
\]

On the residue surface set

\[
x=X_1,
\qquad y=X_2,
\qquad E=E_T,
\qquad a=y_{23},
\qquad b=y_{31}.
\]

The frozen Cayley--Menger family is

\[
S_E:\quad w^2=K_E(a,b).
\]

At total energy zero,

\[
K_0=R^2,
\qquad
R=xa^2+yb^2-xy(x+y).
\]

Thus the central surface has the two source-defined components

\[
w=R
\qquad\text{and}\qquad
w=-R.
\]

## Exact first normal coefficient

Direct expansion of the frozen determinant gives

\[
\boxed{
[E]K_E
=-2(x+y)(a^2-y^2)(b^2-x^2).
}
\]

With

\[
U=w-R,
\qquad V=w+R,
\]

the generic conductor therefore has local form

\[
UV=E\cdot\text{unit}+O(E^2)
\]

away from

\[
a=\pm y
\qquad\text{or}\qquad
b=\pm x.
\]

Hence generic Cut--nearby base change is the ordinary semistable nodal model.
Every failure of first-order transversality is confined to four already frozen
axial marked divisors. No new carrier support appears.

## The four nonsoft marked corners

The axial divisors meet the reduced conductor at

\[
(a,b)=(\pm y,\pm x).
\]

For generic

\[
xy(x+y)\ne0,
\]

these are nonsoft points. At all four corners the exact specialization is

\[
\begin{aligned}
K_E(\pm y,\pm x)
=E^3\big[&-8xy(x+y)\\
&+(5x^2+14xy+5y^2)E\\
&-6(x+y)E^2+2E^3\big].
\end{aligned}
\]

Consequently

\[
[E]K_E=[E^2]K_E=0,
\qquad
\boxed{[E^3]K_E=-8xy(x+y)\ne0.}
\]

The first nontrivial smoothing datum at the marked Cut corner is third normal
order. Neither the first jet nor the second Rees grade sees it.

## Relation to the quartic \(\mathcal Q\)

The established coefficient identity remains

\[
\operatorname{gr}^{(2)}_{E_T}\mathcal Q=-8xy.
\]

It concerns the source algebraic-letter quartic. The new coefficient

\[
-8xy(x+y)
\]

is instead the third normal coefficient of the Cayley--Menger Cut family at
the marked physical-chain corner. Their common factor does not identify their
types or make \(\mathcal Q\) support.

## Verdict

The tested depth-two claim is falsified:

\[
\boxed{
\operatorname{Rees}_{\le2}
\text{ is insufficient for the full marked physical Cut--nearby comparison.}
}
\]

The stronger carrier falsifier does not fire. The entire excess locus is the
pre-existing union

\[
\{a=\pm y\}\cup\{b=\pm x\},
\]

and its four pairwise corners. Therefore:

- existing carrier: total-energy normal, Cut divisor, axial marked sections,
  reduced conductor, and their flagged intersections;
- soft support: excluded by \(xy(x+y)\ne0\);
- graph homology: no new class derived;
- Tate/Kummer data: unchanged;
- Legendre/Gauss--Manin data: unchanged rank-two nodal quotient;
- extension/excess data: first possible marked-corner contribution occurs in
  third normal grade;
- genuinely new carrier incidence: none;
- falsified mechanism: truncation of the shared comparison envelope at
  second Rees order.

Thus H2 survives only after deleting the unsupported depth-two bound. This is
a reduction of the surviving conjecture, not permission to fit a third-grade
correction to the target answer.

## Exact evidence

- `research/benincasa/check_et_cut_nearby_normal_form.rs`;
- `research/benincasa/et-cut-nearby-normal-form.json`;
- 4,225 exact integer specializations of the complete frozen polynomial;
- warnings-denied optimized Rust compilation and zero-result execution through
  the governed Scheduler MCP.

## Next hostile falsifier

Freeze the third normal coefficient just derived and construct the minimal
log blowup of the local marked-corner model. Compute the relative
can--variation map of the canonical Leray chain and test whether its class is
the functorial third-Rees excess of the existing axial-flag square.

Admissible outcomes:

1. the class is generated canonically by the frozen flagged carrier and the
   ordinary higher-Rees/excess calculus, strengthening unbounded-grade H2; or
2. the class cannot be produced without an additional support-switch object,
   falsifying the current shared-calculus form of H2 at this corner.

No third-grade correction may be chosen from the desired commutator.

## Outcome contract

~~~json
{
  "claim": "Nearby/Gysin/excess comparison through second E_T-Rees grade controls the source-defined nonseparating Cut at every generic nonsoft marked intersection.",
  "status": "falsified_at_four_nonsoft_marked_corners",
  "cut": "Res_{q_G12=0}, q_G12=E_T+y12, Jacobian 1",
  "central_fiber": "K_0=R^2",
  "first_normal": "-2*(x+y)*(a^2-y^2)*(b^2-x^2)",
  "generic_cut_nearby_model": "semistable",
  "excess_support": ["a=y", "a=-y", "b=x", "b=-x"],
  "corner_gr1": 0,
  "corner_gr2": 0,
  "corner_gr3": "-8*x*y*(x+y)",
  "corner_nonsoft_open": "x*y*(x+y)!=0",
  "depth_two_sufficient": false,
  "new_carrier_incidence": false,
  "surviving_hypothesis": "shared frozen carrier plus sector-specific coefficients and unbounded higher-Rees/excess calculus",
  "next_experiment": "Compute the third-Rees relative can-var class on the minimal log blowup of one marked corner."
}
~~~
