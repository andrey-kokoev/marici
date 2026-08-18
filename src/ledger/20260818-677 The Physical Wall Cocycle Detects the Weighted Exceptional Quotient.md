---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 677 — The Physical Wall Cocycle Detects the Weighted Exceptional Quotient

## Hard-to-vary claim

On the generic nonsoft shared-wall locus, the source-defined physical cocycle
\(\rho_{\rm phys}\) pairs nontrivially with the rank-one weighted exceptional
quotient of Entry 672. The physical weighting preserves the exceptional
functional's two-dimensional kernel.

## Typed pairing

The exceptional map acts on logarithmic primitives, not directly on wall
cohomology. Their canonical interaction is the weighted local Stokes
coefficient. At each reduced tangency point it is

\[
E_{{\rm exc},i}(V)\,\rho_i|_{h_i=0}.
\]

Thus the comparison is legal exactly where the physical residue is regular
and nonzero on the reduced tangency divisor.

## Exact resultant calculation

Using the canonically normalized reduced factors \(h_i\), eliminate the wall
coordinate between \(h_i\) and the numerator and denominator of the literal
physical residue. All three denominator resultants are nonzero. The numerator
resultants are

\[
\boxed{
\operatorname{Res}(h_1,N_1)=-R_1,\qquad
\operatorname{Res}(h_2,N_2)=R_2,\qquad
\operatorname{Res}(h_3,N_3)=E^2,
}
\]

where \(R_1,R_2,E^2\) are exactly the physical conductor factors of Entry
668.

Therefore, over the complement of the established conductor support, the
physical weighted evaluation differs from \(E_{\rm exc}\) only by invertible
row scalings. Hence

\[
\boxed{
\ker E_{\rm phys,exc}=\ker E_{\rm exc},
\qquad
\dim\ker E_{\rm phys,exc}=2,
\qquad
\operatorname{rank}E_{\rm phys,exc}=1.
}
\]

This identifies the exceptional quotient as a detector of the actual
physical relative wall class. It does not provide an absolute
\(\mathcal T_7\) coordinate or a localization splitting.

## Quartic classification

Entry 668 proves

\[
\gcd(\mathcal Q,R_1R_2E^2)=1.
\]

Consequently the physical pairing is generically nonzero through
\(\mathcal Q=0\), away from intersections with the known conductor support:

\[
\boxed{
\mathcal Q\text{ is not support of the physical exceptional pairing.}
}
\]

The weighted corner now has a physical interpretation, but it still does not
house the algebraic quartic. Any relation to \(\mathcal Q\) must be a
secondary supported comparison or extension datum.

## Classification

- existing carrier: shared walls and Cayley--Menger tangencies;
- coefficient support: \(R_1R_2E^2=0\);
- canonical relative detector: the rank-one physical exceptional quotient;
- new carrier datum: none;
- \(\mathcal Q\)-home: unresolved secondary comparison/extension data.

## Next falsifier

Construct the supported Gysin/connection comparison on this now
source-identified quotient and compute its off-diagonal transport. The finite
test is whether \(\mathcal Q\) occurs in that secondary map while remaining
absent from the diagonal detector and conductor supports.

## Evidence

- \`research/benincasa/check_physical_residue_at_weighted_tangencies.py\`;
- \`research/benincasa/physical-residue-weighted-tangency-pairing.json\`;
- Entries 648, 668, and 672--674.

## Outcome contract

~~~json
{
  "claim": "The physical wall cocycle vanishes or becomes singular on the reduced weighted tangencies, so it cannot detect the exceptional quotient.",
  "status": "falsified",
  "all_physical_tangency_residues_generically_regular": true,
  "all_physical_tangency_residues_generically_nonzero": true,
  "physical_numerator_resultants": ["-R1", "R2", "E^2"],
  "exceptional_kernel_preserved": true,
  "physical_exceptional_rank": 1,
  "Q_is_pairing_support": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute the supported Gysin/connection comparison on the physical exceptional quotient."
}
~~~
