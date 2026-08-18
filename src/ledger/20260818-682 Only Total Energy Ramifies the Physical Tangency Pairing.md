---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 682 — Only Total Energy Ramifies the Physical Tangency Pairing

## Hard-to-vary claim

Among the source-derived zero and pole divisors of the six physical
reduced-tangency residues, every generic conductor or marked-section
collision is étale on its quadratic tangency cover except the \(g_3\)
total-energy boundary \(E=x+y+z=0\). There, physical numerator vanishing and
cover ramification coincide.

## Sheetwise classification test

For each shared wall, let \(h_i(t)=0\) be the reduced quadratic cover. For
each irreducible factor \(f\) of

\[
\operatorname{Res}(h_i,N_i)
\quad\text{or}\quad
\operatorname{Res}(h_i,D_i),
\]

compare \(f\) with

\[
\Delta_i=\operatorname{Disc}_t(h_i).
\]

If \(f\nmid\Delta_i\), the cover is étale at the generic point of \(f=0\).
A resultant zero then belongs to one analytic sheet: one residue has the
corresponding zero or pole while the other remains regular. No deck
monodromy is generated locally around that component.

## Exact result

For \(g_1\) and \(g_2\), every physical numerator and denominator resultant
factor is coprime to the corresponding \(\Delta_i\). This includes the
physical conductor cubics \(R_1,R_2\) and all signed-energy or site-energy
denominator collisions.

For \(g_3\), all denominator collisions are likewise étale except

\[
E=x+y+z=0.
\]

The total-energy factor satisfies

\[
E\mid\Delta_3,
\qquad
E^2\mid\operatorname{Res}(h_3,N_3),
\qquad
E^2\mid\operatorname{Res}(h_3,D_3).
\]

Thus

\[
\boxed{
E=0
\text{ is the unique tested physical boundary where tangency-sheet
ramification and residue collision coincide.}
}
\]

This is precisely the scattering degeneration already known to require
nearby cycles and a choice of physical sheet.

## Consequence

Away from \(E=0\), extending the physical exceptional pairing across a
generic conductor component requires an ordinary sheetwise elementary
modification, not a new ramified carrier or nearby-cycle object.

At \(E=0\), the two-sheet description itself degenerates. The norm cannot
separate the colliding numerator, denominator, and ramification orders.
This boundary must be treated by logarithmic nearby cycles before deciding
whether the rank-one image remains locally free, becomes torsion, or joins
another coefficient block.

The quartic \(\mathcal Q\) is absent from every boundary factor in this
classification.

## Classification

- generic conductor and marked-section boundaries: étale one-sheet
  coefficient modifications;
- total-energy boundary: ramified nearby-cycle coefficient geometry;
- new carrier datum: none;
- \(\mathcal Q\)-home: not diagonal sheetwise boundary data.

## Next falsifier

Choose a transverse parameter \(E\) at generic \(X_1X_2\ne0\), normalize
the \(g_3\) quadratic cover over \(\mathbb Q((E^{1/2}))\), and compute the
two physical residue Laurent orders and deck action. Compare the resulting
nearby-cycle graded line with the known Tate/Kummer scattering limit.

## Evidence

- \`research/benincasa/classify_physical_tangency_sheet_boundaries.py\`;
- \`research/benincasa/physical-tangency-sheet-boundaries.json\`;
- Entries 673--675, 677, and 680;
- allocator claim \`seqclaim-989a28bb34375a3955e84967\`.

## Outcome contract

~~~json
{
  "claim": "Generic conductor collisions necessarily ramify the physical tangency double covers.",
  "status": "falsified",
  "generic_conductor_collisions_etale": true,
  "unique_ramified_physical_boundary": "g3 at total energy E=0",
  "total_energy_requires_nearby_cycles": true,
  "Q_is_sheet_boundary_factor": false,
  "new_carrier_datum": false,
  "next_experiment": "Compute g3 residue Laurent orders and deck action over the E^(1/2) nearby-cycle cover."
}
~~~
