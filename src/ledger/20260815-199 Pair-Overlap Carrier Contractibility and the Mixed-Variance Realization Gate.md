# Pair-Overlap Carrier Contractibility and the Mixed-Variance Realization Gate

Date: 2026-08-15  
Status: proved for the integral unloaded carrier and external spectator tensors.
The support-changing Tor/Čech realization, endpoint/Q mapping fiber, and physical
parity remain unconstructed. No graph admission is claimed.

## Correction to the rank-six interpretation

Entry 198 correctly records that the six short-facet boundaries form a
saturated rank-six sublattice of the twenty-one edge chains. It treated the
corresponding choice of corridor representative as a remaining strict
ambiguity. In the homotopy-coherent carrier category this ambiguity is
contractible.

Let
[
d_2:mathbb Z^6longrightarrowmathbb Z^{21}
]
be the actual oriented short-facet boundary matrix. The established unit
maximal minor implies that (d_2) is a split integral monomorphism. Therefore,
if two endpoint-pointed corridor representatives determine the same fixed
class in (H_1(B_{m short},V)), their difference is (d_2z) for a unique
integral (zinmathbb Z^6). There is no comparison automorphism because
(ker d_2=0).

For three cyclic comparisons, an alternating sum whose edge boundary
vanishes lies in (ker d_2), hence is zero. Thus carrier triple coherence is
automatic. Rotation and reflection transport the unique comparison, so no
additional carrier choice can break (D_3) covariance.

Because the monomorphism is integrally split, tensoring with an external
spectator complex preserves this conclusion degreewise. This statement does
not cover a support-changing Tor or Čech map: such a map is not an external
tensor factor.

## What remains missing

The three pairwise long-road intersections are still not objects of the
literal entry-143 face category. Distinct long diagonals cross, so no
compatible (K_6) face contains a pair. The canonical projective-conductor
SNC points therefore require an extraordinary comparison, not an ordinary
face corestriction.

The exact first missing arrow is a mixed-variance realization
[
Gamma_{ij}^{!,log}longrightarrow
C_ullet(q_k)subset F_B/F_V,
qquad {i,j,k}={14,03,25},
]
whose two restrictions agree with the adjacent long-facet packets and whose
image is the fixed complementary marked corridor. It must identify the
occurrence duals, both normal-circle removals, Tor grades, and Čech signs on
the 24 pair-vertex incidences. Carrier uniqueness will then make its
comparison and cyclic coherence canonical; it does not construct those
vertical maps.

Consequently this result removes only the rank-six carrier-choice objection.
It does not remove entry 135's larger rank-nine butterfly ambiguity, produce
the based (q_Sigma) comparison, instantiate the endpoint/Q mapping fiber,
or define (p_{partial,Q}).

## Certificate

A focused executable source is present at

- `research/voevodsky/check_p2_pair_overlap_homotopy_contractibility.rs`.

Current source SHA-256:

- `617be8dc031a0dcb499bc7e8a6f1db324165de96abfffb616e0091263595280e`.

It reconstructs the actual (K_6) face census ((1,9,21,14)), the oriented
short-boundary matrix, rank six, a unit maximal minor, (d_1d_2=0), zero
kernel, and the three crossing long-road pairs. It also maps all six dP6
cones to primitive differences of legitimate short-facet chains and verifies
that their cyclic residue sum telescopes to zero. Its mathematical input is
also independently covered by entry 119's validated rank-six/unit-minor
certificate. The new source has been completely reread through filesystem
MCP and passes `rustfmt --edition 2021 --check`. A bounded validation did produce the checker metadata artifact before its
worker report timed out, proving `rustc --edition=2021 -D warnings
--emit=metadata` succeeded. Linking and runtime execution remain unavailable
because the inherited Windows worker environment has no MSVC linker.

## Consequence

The minimal additional geometry is not a choice of a carrier 2-chain. It is a
support-typed log/nearby-cycle correspondence realizing the external SNC
pair points inside the literal entry-143 mixed-variance target. Once one such
realization exists with the prescribed boundary class, the carrier
comparison, reflection transport, and cyclic 2-coherence are forced
integrally.

## Outcome contract

~~~json
{
  "claim": "For each fixed endpoint-pointed road class, the actual K6 short-boundary rank-six ambiguity is contractible in the integral homotopy-coherent carrier category: comparison 2-chains exist integrally, are unique, have no automorphisms, and satisfy cyclic coherence.",
  "status": "proved_scoped_carrier__mixed_variance_realization_open",
  "scope": "unloaded integral carrier and external spectator tensor factors only; no support-changing Tor/Cech realization, literal entry143 pair map, endpoint/Q mapping fiber, parity, or graph admission",
  "evidence": {
    "k6_face_census": [1, 9, 21, 14],
    "short_boundary_rank": 6,
    "short_boundary_kernel_rank": 0,
    "unit_maximal_minor": true,
    "cokernel_torsion": false,
    "crossing_long_pairs": 3,
    "dp6_cone_residue_rows": 6,
    "dp6_cyclic_residue_sum": 0,
    "carrier_comparison_groupoid": "contractible for a fixed homology class",
    "external_spectator_tensor": "preserves the split injection",
    "support_changing_tor_cech": "unconstructed",
    "literal_pair_vertex_rows": "unconstructed",
    "rank9_butterfly_contraction": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined"
  },
  "checker_sha256": "617be8dc031a0dcb499bc7e8a6f1db324165de96abfffb616e0091263595280e",
  "validation": {
    "filesystem_mcp_full_reread": "PASS",
    "rustfmt": "PASS via worker MCP run-3e7ac8218dec4f1cbcbee0c69b3ec942",
    "rustc_metadata": "PASS: warnings-denied metadata artifact produced by bounded MCP validation",
    "runtime": "NOT EXECUTED: inherited MCP worker environment has no MSVC linker"
  },
  "minimal_geometry": "Construct a support-typed log/nearby-cycle pair correspondence Gamma_ij whose two facet restrictions and complementary marked-corridor image satisfy all occurrence, normal, Tor, Cech, endpoint, reflection, and D3 Beck-Chevalley squares."
}
~~~
