---
authors:
  - marici.Nima
date: 2026-08-18
---
# 657 — The Complete Physical Source Occupies the Rank-Twenty Residue Quotient

## Hard-to-vary claim

Although Entry 653 tested only a rank-twenty-one three-pole subpacket, the
complete physical five-pole source is nevertheless known to occupy the
\(q_{G_{12}}\)-residue quotient. This follows directly from the
source-derived nonzero conductor boundary, without constructing a full
five-axis pivot lattice.

## Deletion--restriction sequence

For either physical five-pole family, Entry 596 gives

\[
\operatorname{rank}M_5=35,
\qquad
\operatorname{rank}M_4=15,
\qquad
\operatorname{rank}M_{4|G_{12}}=20.
\]

Thus

\[
\boxed{35=15+20}
\]

is the rank identity for the deletion--restriction sequence along
\(q_{G_{12}}=0\).

## Source residue is nonzero

The complete unsplit source factor is

\[
\Omega_{\rm phys}
\propto
\frac1{q_{G_{12}}}
\left(\frac1{q_{g_{23}}}+\frac1{q_{g_{31}}}\right)
\frac1{q_{g_1}q_{g_2}q_{g_3}}.
\]

Entries 593--594 compute its Poincare residue and then normalize the three
shared walls. All three conductor resultants are generically nonzero.
Entry 648 shows that these components assemble into the legal closed
cocycle

\[
\rho_{\rm phys}=(\rho_1,\rho_2,\rho_3;0),
\qquad
\rho_i\ne0.
\]

Therefore

\[
\boxed{
\operatorname{Res}_{G_{12}}[\Omega_{\rm phys}]\ne0
\text{ in the rank-twenty residue quotient}.}
\]

By exactness, the complete source cannot lie in the rank-fifteen deletion
submodule:

\[
\boxed{[\Omega_{\rm phys}]\notin M_4.}
\]

## Scope

This is the correctly typed complete-source occupancy theorem missing from
Entry 653. It proves nonzero occupancy of the rank-twenty quotient. It does
not assert that the complete source spans a one-dimensional proper top
grade relative to every one of the five deletion faces.

The result also does not provide a retained chain-level residue matrix.
Ordinary cohomology proves nonvanishing, while Entry 655 shows that exact
IBP corrections have zero wall-cohomology image. The remaining ambiguity is
secondary homotopy data, not source occupancy.

## Computational consequence

A full \(3^5\) pole lattice is unnecessary for the binary question of
whether the complete source reaches the residue quotient. It remains useful
only for:

1. resolving the source against all proper deletion faces;
2. retaining explicit homotopies;
3. comparing alternative syzygy reductions at chain level.

The next efficient construction should therefore factor the complex by
deletion--restriction: retain pivot certificates for the rank-fifteen
deletion module and rank-twenty residue module separately, then glue them by
the source Poincare-residue column map.

## Evidence

- `research/benincasa/physical_five_pole_residue_occupancy_gate.py`;
- Entries 593--596, 648, 655, and 656.

## Outcome contract

~~~json
{
  "claim": "The complete physical five-pole source lies in the rank-fifteen q_G12-deletion submodule.",
  "status": "falsified",
  "five_pole_rank": 35,
  "deletion_rank": 15,
  "residue_quotient_rank": 20,
  "nonzero_normalized_shared_wall_components": 3,
  "mixed_occurrence_component": 0,
  "complete_source_residue_nonzero": true,
  "one_dimensional_proper_top_claimed": false,
  "next_experiment": "Build a block deletion-residue retained presentation and glue it with the source Poincare-residue column map."
}
~~~
