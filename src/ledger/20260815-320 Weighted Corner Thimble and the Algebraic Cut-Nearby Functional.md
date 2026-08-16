---
authors:
  - marici.Benincasa
date: 2026-08-15
---
# Weighted Corner Thimble and the Algebraic Cut-Nearby Functional

## Record

Status: the exceptional carrier interval is mapped to a source-basis
coefficient functional; its universal regularized Leray scalar remains to be
evaluated before claiming the literal Cut--nearby commutator.

This entry continues entry 224. It adds no denominator, carrier cell, support
summand, projector, or normalization.

## Deutsch--Popperian conjecture tested

The hard-to-vary claim was

\[
\boxed{
\text{the marked-corner exceptional interval cannot be located canonically
inside the frozen nine-master coefficient system.}
}
\]

The finite falsifier was a weighted local limit that selected a unique
nonzero source-basis functional and showed whether it had algebraic or
elliptic support.

## Frozen weighted model

At the positive real corner write

\[
a=y+A,\qquad b=x+B,\qquad E=E_T.
\]

The cubic tangent calculation of entries 222--224 requires the weights

\[
E=\tau^2,\qquad
A=\tau^2r,\qquad
A+B=\tau^3n.
\]

Exact substitution into the frozen Cayley--Menger residue family gives

\[
\boxed{
K
=
\tau^6
\left[
4x^2y^2n^2
+
8xy(x+y)(r^2-1)
\right]
+O(\tau^7).
}
\]

The source double-pole numerator is not the total-\(E\) derivative used in
entry 222. It is independently frozen by equation (58):

\[
K_1=
\left.\frac{\partial K}{\partial q_{\mathcal G_{12}}}\right|_{q=0}.
\]

The same weighted substitution gives

\[
\boxed{
K_1
=
16xy(x+y)\tau^4+O(\tau^5).
}
\]

Both identities were checked exactly at 3,025 integer specializations.

## Master scaling

The coordinate Jacobian has weight

\[
da\wedge db
=
\tau^5\,dr\wedge dn
\]

at fixed \(\tau\), while

\[
K^{1/2}=O(\tau^3).
\]

Therefore every simple-pole source master has period order

\[
\tau^{5-3}=\tau^2=E
\]

and vanishes in the exceptional nearby grade.

For the source-normalized double-pole forms

\[
-\frac12
\frac{aK_1\,da\wedge db}{K^{3/2}},
\qquad
-\frac12
\frac{bK_1\,da\wedge db}{K^{3/2}},
\qquad
-\frac12
\frac{K_1\,da\wedge db}{K^{3/2}},
\]

the total weight is

\[
\tau^{4+5-9}=\tau^0.
\]

At the corner \(a=y,\ b=x\), their leading coefficients occur in the ratio

\[
y:x:1.
\]

In the literal equation-(58) master order this gives the exceptional period
functional

\[
\boxed{
\Lambda_{\rm exc}
=
(0,0,y,0,x,1,0,0,0)\,I_{\rm loc},
}
\]

where \(I_{\rm loc}\) is the single universal regularized local thimble
functional determined by the frozen lower-half-plane Leray prescription.
The common source numerator is

\[
-8xy(x+y).
\]

No basis rotation was used to obtain this vector.

## Gysin and nearby classification

The exceptional thimble is supported at the finite marked corner. It has no
boundary at the anticanonical infinity divisor. Consequently

\[
R_\infty(\Lambda_{\rm exc})=0.
\]

This independently agrees with the source basis: the surviving entries
\(e_3,e_5,e_6\) lie in the parity blocks contributing to the rank-seven
algebraic kernel, and \(R_\infty(e_6)=0\).

Thus the marked-corner correction has:

- zero projection to the rank-two elliptic quotient;
- zero new elliptic nilpotent rank;
- support in the rank-seven Tate/Kummer algebraic kernel;
- no new carrier incidence.

Entry 223's extraordinary triple top does not supply the missing scalar: it
fixes a different finite external \(q_\Sigma\) comparison and explicitly
lacks the literal realization functor. It therefore cannot be transported
into this coefficient calculation by analogy.

## Verdict

The coefficient-location conjecture is falsified:

\[
\boxed{
\text{the frozen third-Rees interval maps canonically to an algebraic
nine-master functional with ratios }(e_3:e_5:e_6)=(y:x:1).
}
\]

This is stronger than merely knowing that the carrier group has rank two.
It shows that the elliptic Gysin quotient is uninvolved in the marked-corner
Cut--nearby correction.

The literal commutator is not yet claimed. Its remaining datum is the
universal regularized value and sign of \(I_{\rm loc}\), including the
source-fixed \(2\pi i\) Leray convention. Setting it to one would be a
post-hoc normalization and is prohibited.

## Classification

- existing carrier: the frozen total-energy/Cut marked corner and its
  minimal weighted log model;
- soft support: excluded by \(xy(x+y)\ne0\);
- graph homology: none;
- Tate/Kummer coefficient data: \(\Lambda_{\rm exc}\);
- elliptic Gauss--Manin data: zero image;
- extension data: no algebraic-to-elliptic component in the leading
  exceptional grade;
- genuinely new carrier incidence: none.

## Exact evidence

- research/benincasa/check_et_cut_nearby_normal_form.rs;
- research/benincasa/et-cut-nearby-normal-form.json;
- 4,225 exact tests of the global normal expansion;
- 3,025 exact tests of the weighted corner expansion;
- warnings-denied optimized Rust compilation and zero-result execution
  through the governed Scheduler MCP.

## Next finite falsifier

Evaluate the regularized local Leray pairing

\[
I_{\rm loc}
=
\operatorname{Reg}
\int_{\Gamma_{\rm exc}}
\frac{dr\wedge dn}{
\left(
4x^2y^2n^2+8xy(x+y)(r^2-1)
\right)^{3/2}}
\]

with the source lower-half-plane boundary value, positive sheet, and
orientation. Insert the resulting scalar into \(\Lambda_{\rm exc}\) and
compare directly with

\[
\psi_{E=0}\circ\operatorname{Res}_{q_{\mathcal G_{12}}=0}
-
\operatorname{Res}_{q_{\mathcal G_{12}}=0}\circ\psi_{E=0}.
\]

A nonzero source-fixed match closes the marked coefficient-level gate using
the existing higher-Rees/excess calculus. A mismatch, or the absence of a
canonical regularization in the frozen physical chain, falsifies the current
shared-calculus form of H2.

## Outcome contract

~~~json
{
  "claim": "The weighted marked-corner limit canonically locates the exceptional period functional in the frozen nine-master coefficient system.",
  "status": "survived",
  "weighted_surface_order": 6,
  "weighted_K1_order": 4,
  "simple_master_order": 2,
  "double_master_order": 0,
  "exceptional_functional": [0, 0, "y", 0, "x", 1, 0, 0, 0],
  "infinity_gysin_image": 0,
  "sector": "rank-seven algebraic Tate/Kummer kernel",
  "elliptic_component": 0,
  "new_carrier_incidence": false,
  "literal_commutator_computed": false,
  "remaining_datum": "source-normalized universal regularized local Leray scalar I_loc"
}
~~~
