---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 667 — The Unsplit Source Zero Divisor Does Not Generate the Quartic

## Hard-to-vary claim

The algebraic quartic \(\mathcal Q\) is not the collision discriminant obtained
by restricting the elliptic branch surface to the zero divisor of the
literal unsplit occurrence numerator.

## Frozen source object

On the \(q_{\mathcal G_{12}}\)-residue surface use

\[
K_E(a,b)
\]

from Entry 661 and the source-prescribed sum

\[
\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}
=
\frac{N}{q_{g_{23}}q_{g_{31}}},
\qquad
N=q_{g_{23}}+q_{g_{31}}=a+b-x-y.
\]

No new section or normalization is introduced. The tested divisor is the
literal numerator-zero line

\[
N=0,\qquad b=x+y-a.
\]

## Exact elimination

Substitution gives a quartic polynomial in \(a\). Its discriminant factors
over \(\mathbb Q[x,y,z]\) as

\[
\operatorname{Disc}_a K_E(a,x+y-a)
=
-16\ell_1^2\ell_2^2\ell_3^4\ell_4^7P_9(x,y,z),
\]

where \(P_9\) is homogeneous of degree nine and has 55 monomials. Direct
polynomial gcd computation gives

\[
\boxed{
\gcd\!\left(
\mathcal Q,
\operatorname{Disc}_a K_E(a,x+y-a)
\right)=1.
}
\]

The checker also verifies that

\[
\mathcal Q
=
4AB-(A+B-E^2)^2
=
-16x^2y^2-8xyE^2+8(x+y)E^3-5E^4.
\]

Thus the failure is not a convention mismatch.

## Interpretation

The reflected source sum is not enough to generate \(\mathcal Q\) in either
of the two evident ways:

1. its common five-mark relative class does not become a flat line (Entry
   665);
2. the branch collision on its literal zero divisor has discriminant
   coprime to \(\mathcal Q\) (this entry).

The factors in the displayed discriminant are not promoted to physical
support. The line \(N=0\) is a numerator-zero locus, not a frozen marked
pole or integration-boundary section, so its residual factor \(P_9\) has no
carrier authority.

## Classification

\[
\boxed{
\mathcal Q
\notin
\text{single marks, mark intersections, shared-wall endpoints, or the
unsplit numerator-zero collision}.
}
\]

This further lowers the prior that \(\mathcal Q\) is ordinary incidence
support. The surviving source-derived homes are a secondary boundary/Gysin
commutator or extension data tied to the physical relative integration
chain.

## Next falsifier

Retain the proper-face subcomplex and the source-labelled localization
homotopy. Compute the kinematic commutator of its connecting morphism on
the unsplit source, then test whether \(\mathcal Q\) occurs in that
secondary term. Do not infer this map from the numerator-zero divisor.

## Evidence

- \`research/benincasa/check_unsplit_numerator_branch_discriminant.py\`;
- \`research/benincasa/unsplit-numerator-branch-discriminant.json\`;
- Entries 660, 661, 665, and 666.

## Outcome contract

~~~json
{
  "claim": "The literal unsplit numerator-zero divisor generates the source quartic as a branch collision discriminant.",
  "status": "falsified",
  "source_numerator": "a+b-x-y",
  "restricted_branch_degree": 4,
  "discriminant_energy_factor": "-16*ell1^2*ell2^2*ell3^4*ell4^7",
  "residual_degree": 9,
  "quartic_gcd": 1,
  "new_carrier_datum": false,
  "next_experiment": "Compute Q-support in the source-labelled boundary/Gysin commutator."
}
~~~
