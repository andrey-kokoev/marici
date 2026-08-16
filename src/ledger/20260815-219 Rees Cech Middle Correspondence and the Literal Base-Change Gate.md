# Rees Cech Middle Correspondence and the Literal Base-Change Gate

## Record

Date: 2026-08-15

Status: proved for the canonical finite Rees/Čech correspondence carrier.
Literal entry143 ringed proper base change and mixed-variance Gysin naturality
remain unconstructed. No graph admission is claimed.

## Construction

The midpoint obstruction of entry 218 is avoided without selecting a section.
Cover
[
mathbf P(L_{ab}oplus L_c)
]
by its two canonical standard opens (U_{ab}) and (U_c). Their intersection
is the relative (mathbf G_m)-torsor (U_	imes). The Čech incidence is
the primitive column
[
U_	imeslongmapsto -U_{ab}+U_c.
]
On the overlap, the homogeneous transition coordinates satisfy
(t=B/A), (s=A/B), and (ts=1). Only projective chart coordinates are
inverted; neither base section (ab) nor (c) is inverted.

Assign the two opens to the two marked corridor edges and the overlap to the
middle costalk. The proper total (mathbf P^1) class maps to the sum of the
two edges. With
[
partial e_0=m-o,qquad partial e_1=c-m,
]
the overlap terms cancel and
[
partial(e_0+e_1)=c-o.
]
Thus the middle is supplied by the cover nerve, not by a third section.

Tensoring with four Boolean states over six ordered pairs gives 24 source
columns, 48 edge rows, and 24 overlap rows. The top matrix again has rank 24
and 24 unit Smith factors. Both adjacent restrictions are the canonical chart
restrictions. Reflection exchanges the charts and reverses the Čech
orientation; rotation relabels the road copies.

## Remaining exact gate

This is a canonical proper carrier and resolves the midpoint-choice problem.
It still does not prove the ringed Beck--Chevalley transformation from the
Rees chart nerve to entry143's localized ([S,H]) summands. The target
localizations invert specified normal sections (u_a), whereas the source
cover inverts homogeneous Rees coordinates. The primitive excess cap supplies
the coefficient comparison, but a six-functor proper-base-change cell must
identify these operations on every occurrence/normal/Tor/Čech state.

Accordingly the first remaining map is
[
BC_{mathrm{Rees},143}^{!,check C}:
Rpi_!operatorname{Tot}(U_{ab}leftarrow U_	imes	o U_c)
longrightarrow (F_B/F_V)^{BM,check C},
]
with both adjacent-facet restrictions and endpoint framing. Until it exists,
the generic (q_Sigma) connector and endpoint/Q mapping fiber remain
undefined.

## Certificate

Executable:
`research/voevodsky/check_dp6_rees_cech_middle_correspondence.rs`

SHA-256:
`3893248c92bae75b31ff0f48c1123809a98d32bd79bf1dd6496f61cf790b67b9`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed. Native PowerShell was used only because structured-command
MCP was unavailable.

## Outcome contract

~~~json
{
  "claim": "The two canonical Rees charts and their relative-Gm overlap replace the nonexistent midpoint section by a canonical Cech middle correspondence; its primitive incidence derives the two-edge corridor boundary and the 24 integral top columns without base localization.",
  "status": "proved_scoped_rees_cech_middle_correspondence_carrier",
  "scope": "finite labelled Rees/Cech proper carrier, excluding literal entry143 ringed base-change realization",
  "factorization": {
    "cover": ["U_ab","U_c"],
    "overlap": "relative Gm torsor",
    "cech_incidence": [-1,1],
    "transition_exponents": [1,-1],
    "base_inversions": false,
    "source_columns": 24,
    "target_edge_rows": 48,
    "middle_overlap_rows": 24,
    "top_rank": 24,
    "top_smith_unit_factors": 24,
    "branch_restrictions": [1,1],
    "reflection_exchanges_charts_and_reverses_cech_orientation": true,
    "proper_rees_space_global": true,
    "literal_entry143_ringed_base_change_constructed": false,
    "mixed_variance_gysin_naturality_constructed": false
  },
  "minimal_remaining_datum": "The proper-base-change transformation from the Rees chart Cech nerve to the literal entry143 localized [S,H] diagram, including all normal/Tor rows and both adjacent-facet endpoint restrictions.",
  "evidence_refs": [
    "research/voevodsky/check_dp6_rees_cech_middle_correspondence.rs",
    "src/ledger/20260815-214 Finite Ordered Log-Link Gysin Matrix and the Spatial Realization Gate.md",
    "src/ledger/20260815-217 Product-Rees Log-Excess Cap and the Literal Support Gate.md",
    "src/ledger/20260815-218 Rees Exceptional P1 Middle-Section No-Go and the Correspondence Gate.md"
  ],
  "checker_sha256": "3893248c92bae75b31ff0f48c1123809a98d32bd79bf1dd6496f61cf790b67b9",
  "next_experiment": "Construct or falsify BC_Rees,143 on one ordered pair by comparing the Rees homogeneous-chart Cech nerve with the four literal localized normal states."
}
~~~
