---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Weight-Minus-One Wall Form Is Meromorphically Exact

## Record

Status: the generic nonzero logarithmic coefficient found in entry 324 is
an exact one-form on the punctured algebraic wall curve. Its vanishing
symmetric source pairing is therefore stronger than an odd-integrand
cancellation: no nonzero meromorphic de Rham class survives away from the
two branch endpoints.

The primitive has poles at those endpoints. This entry claims exactness in
the punctured meromorphic wall complex and the frozen symmetric regularized
pairing; it does not claim an unqualified smooth relative extension through
the endpoints.

No carrier cell, support summand, projector, or normalization is added.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the nonzero weight }-1\text{ residue coefficient defines a nonzero
class in meromorphic }H^1\text{ of the punctured wall curve.}
}
\]

The finite falsifier was a primitive in the frozen quadratic extension.

## Frozen wall form

Put

\[
a=xy,
\qquad
s=x+y,
\qquad
v=an^2-2s.
\]

Entry 324 gives, up to its frozen common branch scalar,

\[
\eta_{-1}
=
-\frac{3(x-y)s}{8x^{5/2}y^{5/2}}
\frac{n(an^2-s)}{v^{5/2}}\,dn.
\]

The punctures are the two branch endpoints

\[
n=\pm N,
\qquad
N^2=\frac{2s}{a},
\qquad
v=0.
\]

On the quadratic wall cover write \(w^2=v\). Then \(\eta_{-1}\) is a
meromorphic algebraic one-form in \((n,w)\).

## Exact primitive

Direct differentiation gives

\[
\boxed{
\frac{n(an^2-s)}{v^{5/2}}\,dn
=
d\left[
-\frac{3an^2-5s}{3a\,v^{3/2}}
\right].
}
\]

Indeed, differentiating

\[
P=\frac{3an^2-5s}{v^{3/2}}
\]

over the common denominator \(v^{5/2}\) gives numerator

\[
6anv-3an(3an^2-5s)
=
-3an(an^2-s).
\]

Restoring the source normalization, a primitive is

\[
\boxed{
\Phi_{-1}
=
\frac{(x-y)(x+y)}{8x^{7/2}y^{7/2}}
\frac{3xyn^2-5(x+y)}
{(xyn^2-2x-2y)^{3/2}}.
}
\]

Therefore

\[
\boxed{
[\eta_{-1}]=0
\quad\text{in the meromorphic de Rham complex of the punctured wall.}
}
\]

This corrects the phrase “nonzero wall coefficient class” in entry 324:
the coefficient is generically nonzero, but its meromorphic cohomology
class is zero.

## Endpoint and physical-cycle audit

The primitive \(\Phi_{-1}\) is even under

\[
n\longmapsto-n.
\]

It has cubic poles in the local square-root coordinate \(w\) at
\(n=\pm N\). Thus ordinary endpoint evaluation is unavailable. In the
source-symmetric Hadamard/tangential prescription, however, the two endpoint
Laurent germs are exchanged by the frozen involution and have equal finite
parts. Hence

\[
\operatorname{Reg}
\int_{-N}^{N}\eta_{-1}
=
\operatorname{FP}\Phi_{-1}(N)
-
\operatorname{FP}\Phi_{-1}(-N)
=0.
\]

The zero pairing is therefore compatible with exactness and does not hide a
nonzero punctured-wall de Rham class.

This does not yet classify a Deligne extension carrying independently
chosen endpoint principal parts. Such a choice would be extra relative
data and is not inserted here.

## Relation to entries 325--326

Entry 325's direct infinity-Gysin image remains zero by disjoint support.
Entry 326's type obstruction remains correct: the wall residue does not
canonically map backward into absolute \(H^2(S)\).

The new result is stronger inside the correctly typed wall object:

\[
\boxed{
\text{the first nonzero coefficient is exact before any absolute
nine-master comparison.}
}
\]

Thus no \(e_6\), \(v_{\rm alg}\), \(L_1\), or \(\mathcal Q\) coordinate is
selected at this grade.

## Verdict

The nontrivial-wall-class conjecture is falsified:

\[
\boxed{
\eta_{-1}=d\Phi_{-1}
\quad\text{on }W\setminus\{\pm N\}.
}
\]

The literal occurrence lift has a nonzero local coefficient but no surviving
punctured-wall meromorphic cohomology class and no symmetric regularized
period. The complexity remains endpoint principal-part data over the
existing marked carrier.

## Classification

- existing carrier: unchanged wall and its two frozen branch endpoints;
- local coefficient: generic nonzero;
- punctured-wall meromorphic cohomology class: zero;
- endpoint principal parts: nonzero cubic poles, exchanged symmetrically;
- symmetric regularized physical pairing: zero;
- direct elliptic/infinity-Gysin image: zero;
- absolute nine-master coordinate: neither defined nor needed;
- genuinely new carrier datum: none.

## Exact evidence

- `research/benincasa/check_wall_form_exactness.rs`;
- `research/benincasa/wall-form-exactness.json`;
- exact derivative identity at 28,224 integer specializations;
- warnings-denied optimized Rust compilation and exact JSON comparison.

## Next finite falsifier

Test whether the endpoint principal parts themselves define a nonzero class
in the source-fixed relative/tangential extension.

Freeze the lower-half-plane sheet and local square-root coordinates at
\(n=\pm N\), compute the two Laurent principal parts of \(\Phi_{-1}\), and
form their occurrence-resolved difference in the relative de Rham cone.

The alternatives are:

1. the involution identifies the full principal parts, so the relative class
   vanishes completely at weight \(-1\);
2. their finite parts agree but an oriented polar jet survives, producing
   endpoint-supported Tate/Kummer data;
3. a new endpoint incidence is required, which would fire the shared-carrier
   falsifier.

No endpoint summand may be added after seeing the answer.

## Outcome contract

~~~json
{
  "claim": "The nonzero weight -1 wall coefficient defines a nonzero meromorphic H1 class on the punctured wall curve.",
  "status": "falsified_by_explicit_primitive",
  "primitive": "(x-y)*(x+y)*(3*x*y*n^2-5*(x+y))/(8*x^(7/2)*y^(7/2)*(x*y*n^2-2*x-2*y)^(3/2))",
  "punctured_wall_class": 0,
  "endpoint_pole_order_in_square_root_coordinate": 3,
  "symmetric_regularized_pairing": 0,
  "endpoint_relative_class": "uncomputed",
  "absolute_nine_master_coordinate": "not defined",
  "new_carrier_incidence": false,
  "next_experiment": "Compare the two endpoint Laurent principal parts in the frozen tangential relative cone."
}
~~~
