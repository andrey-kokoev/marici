# Retained geometric phase records connect to the existing energy accounting

## Result and precise boundary

A partial bridge is now checked. The generated full geometric records recover
all twelve proton and eighteen belt native triangle modes, their exact collective
returns, the existing native constraint Hamiltonians and all 21 belt seam
projectors. No new energy weights or mass fits were introduced.

This requires the existing ordered-corner character, coefficient-frame adapter,
and native local grouping/alignment data. The centroid-mode records alone do not
supply those data. The electron five-cycle does not preserve the tetrahedral cell
on which its existing spinor is defined, so a common three-species energy bridge
is not yet closed.

## What is actually mapped

The test first generates the new geometries from the compact source records,
then finds their exact marked geometric correspondence with the stored carriers.
An affine coordinate adapter maps the generated vertices to the native frame.
It is checked on every vertex and against the complete metric pullback.

Every admitted facet is subdivided using its own centroid. For each retained
ordered triangle (F,a,b), construct its native complex mode from the newly
recovered coordinates:

    v = F + omega*a + omega^2*b
      = F-(a+b)/2 + i*sqrt(3)*(a-b)/2.

The ordering and selected character omega are retained source data, not selected
from the desired energy. For the belt, its existing intrinsic-plane decoder
recovers the exact 36 stored numerator coordinates from the 54 ambient ones.
The decoder preserves the physical norm with metric diag(1/d).

The belt frame has squared scale 8/3 relative to the new scaled-coordinate source;
this existing conversion is retained explicitly. Proton frame scale is one.
Neither conversion is counted as an extra stored-energy resource.

## Native operation energy is recovered, not replaced

Reconstruct each local cyclic operation from its retained triangle frame or
intrinsic plane. Exact checks establish its order three, selected character
line and nonunitarity in the retained physical metric. With the existing rule

    D = A-omega*I,
    H_D = (pi/4) D^sharp D,

and the existing full-field alignment actions, the entire native Hamiltonian
matches the stored operator entry by entry. Both generated selected vectors
recover the exact stored rank-one return N, and

    H_native N = 0.

For each unitary order-three alignment action T, the checker additionally proves

    P_fixed = (I+T+T^2)/3,
    (T-I)^sharp(T-I) = 3*(I-P_fixed).

Thus the new phase decomposition resolves the **existing** alignment-energy
observable: its nonfixed modes carry the inherited defect weight 3*pi/4, in the
already declared unit. This does not identify the local nonunitary triangle
cycle with a unitary centroid rotation. An isometric conjugacy between those
two operations is impossible because unitarity would be preserved.

## Native seams and the stored occupation law

Using the reconstructed triangle modes, rebuild every normalized shared-edge
mismatch projector within the native local groups. All matrices match exactly.

| Carrier | Native triangle modes | All geometric shared edges | Admitted native seam projectors |
|---|---:|---:|---:|
| Proton | 12 | 18 | 0 |
| Belt | 18 | 24 | 21 |

The distinction between geometric adjacency and native seam admission is
essential. The proton groups are individual triangle records; the belt groups
are the three declared paired-face sectors. This grouping is still adapter
input, not derived merely from centroid motion.

For every recovered belt seam projector P_e, the checker verifies

    P_e N = 0,
    (I-P_e)N = N.

These are exactly the controls needed by the already constructed persistent
occupation mechanism:

    S_e = c-P_e,
    h_e = epsilon*n_e + J*(n_e-S_e)^2 - g*X_e.

The current occupation certificate is hash-bound to the freshly regenerated
native energy store. Under its existing kappa>delta condition, the return is
preserved and the registers contribute 21*delta relative to the same inactive
reference. At the existing zero-mixing fixture epsilon=1/4, J=1/2, kappa=1,
g=0, this is 21/4 in the declared energy unit, with all 21 seam records occupied.
It is not a calibrated neutron mass or a newly chosen coefficient.

The meaningful connection is therefore

    retained full geometric records
      -> ordered local phase modes
      -> native phase/alignment and satisfied-seam controls
      -> existing persistent occupations and vacuum-relative stored energy.

Complex phase is present while formation-constraint energy is zero. Stored
energy belongs to the occupation Hamiltonian, not to the mere use of complex
coordinates or the number of displayed arrows. Coupling records to the defects
P_e instead would leave them inactive on N; the occupation law remains substantive
source/model input.

## Two obstructions exposed by the test

### Centroid-only information loses phase orientation

Swapping a and b leaves the triangle centroid unchanged but conjugates its mode.
The two native rank-one projectors differ. The checker verifies this for every
triangle. A centroid-only map therefore cannot recover the selected chiral line;
ordered corners and phase provenance must remain in the retained package.

### The electron action leaves the existing spinor cell

The new electron generator cycles all five pentachoron vertices. Its distinguished
attachment tetrahedron visits all five boundary cells and returns only after five
applications. It is not preserved after any of the first four.

The existing electron spinor and 144-transfer construction live on that one
attachment cell. Restricting the new action to it is not a closed operation.
Transport to all five cells, compatible with the actual spinor phase, metric and
energy operators, is missing. The checker reports this gate as blocked instead
of inventing a five-cell electron Hamiltonian.

## Verification

Fresh executions:

    python research/voevodsky/checkers/check_native_operation_energy_lift.py
    python research/voevodsky/checkers/check_seam_occupation_energy.py
    python research/voevodsky/checkers/check_geometric_phase_energy_bridge.py
    python research/voevodsky/checkers/check_seam_mass_comparison.py

The bridge receipt is `results/geometric_phase_energy_bridge.json`, with source
hashes and exact operation/seam comparison results. The earlier seam-only mass
comparison failure remains in force; rereading phases as occupations does not
repair it.

## Scope

The bridge is exact for the proton/belt retained phase and energy records **with
the listed native adapters supplied**. It does not derive those adapters or the
occupation ontology from the centroid selector. There is no new mass prediction,
no new stage-gap selection, and no common electron/proton/neutron coefficient or
energy closure. The facet-versus-subdivision limitation of centroid admission
also remains unchanged.

## Persistence and source-necessity follow-up

`phase-occupation-persistence-frontier.md` freezes this bridge with the complete
native operator records and occupation certificate, and records a successful
immutable replay. The existing bond-versus-syndrome countermodel is now checked
on this bridged source: the same retained phase data and carrier return admit
occupied bond records or inactive defect records. Occupation follows from the
admitted bond law, not from geometric/phase persistence alone.
