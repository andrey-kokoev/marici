---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# Correction: The Top Cousin Boundary Retains the Lower-Pair Stratum

## Defect

Entry 568 assigned the vector

\[
(1,-1,0)
\]

to the canonical top boundary by replacing the lower-pair face with its zero
proper Möbius grade.  Entry 341 had already established the correct typing:
the lower-pair intersection stratum exists, and the logarithmic residue along
\(q_{\mathcal G_{12}}\) is nonzero even though insertion of the lower pair
creates no new proper support grade.

Thus the canonical geometric boundary is

\[
\boxed{(1,-1,1).}
\]

Möbius ranks classify associated support increments.  They are not the
targets of the geometric Cousin differential.

## Surviving results

The following computations remain valid:

- the transverse triple section and unit Jacobian;
- the identity
  \[
  K|_P=E^2(X_2+X_3-X_1)^2(X_1+X_3-X_2)^2;
  \]
- the cancellation of the two iterated-residue paths through the mixed
  \(q_{\mathcal G_{12}}\)-lower faces;
- the moving-normal horizontal lifts of Entry 573;
- Gauss--Manin naturality on the clean rank-one support line.

Entry 571 is therefore a valid two-face coherence calculation, not a complete
replacement for the three-face Cousin complex.

## Corrected frontier

The source exponent in physical dimension is

\[
\gamma=-\frac12.
\]

Consequently the clean top coefficient line is

\[
K_P^{-1/2}
=
\frac{\pm1}{E(X_2+X_3-X_1)(X_1+X_3-X_2)}.
\]

Its three logarithmic residues are integral, so its generic rank-one
monodromy is trivial after rational gauge.  The next nontrivial question is
not the intrinsic Kummer character of this line; it is whether the line has a
nontrivial nearby-cycle extension by the remaining rank-20 top module at the
three energy boundaries.

## Classification

- corrected geometric face vector: existing Cousin/Gysin calculus;
- zero lower-pair Möbius increment: coefficient-filtration datum;
- clean rank-one line: rational Tate/Kummer line on a resolved sheet;
- possible boundary extension: open;
- new carrier datum: none.

## Evidence

- Entry 341, which has precedence for the full geometric boundary;
- corrected `top_sector_residue_boundary.rs` and result JSON;
- Entries 568, 571, and 573 with the qualifications above.

## Outcome contract

~~~json
{
  "defect": "Entry 568 conflated a zero proper Mobius grade with absence of the lower-pair Cousin face.",
  "disposition": "repaired_and_verified",
  "correct_geometric_boundary": [1, -1, 1],
  "mixed_to_q_cousin_sum": 0,
  "moving_normal_naturality_survives": true,
  "new_carrier_datum": false,
  "next_experiment": "Test nearby-cycle extension of the rational top line by the rank-20 complement at E and the two signed-energy boundaries."
}
~~~
