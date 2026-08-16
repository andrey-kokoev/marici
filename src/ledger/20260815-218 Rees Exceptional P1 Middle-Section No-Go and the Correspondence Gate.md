# Rees Exceptional P1 Middle-Section No-Go and the Correspondence Gate

## Record

Date: 2026-08-15

Status: falsified the intrinsic section-based strict KN subdivision of the
product-Rees exceptional bundle. This is not a no-go for proper log-BM,
nearby-cycle, root-stack, or multivalued correspondences. No graph admission
is claimed.

## Earliest exact obstruction

Entry 216 constructs the exceptional bundle
[
mathbf P(L_{ab}oplus L_c),
]
where (L_{ab}) is the ordered product-branch line and (L_c) is the
complementary road line. Its two coordinate endpoint sections are canonical.

The literal marked half-corridor has two edges and therefore needs a third,
middle stratum. A global section of this projective bundle disjoint from both
coordinate endpoints has two nowhere-vanishing components
[
Nlongrightarrow L_{ab},qquad Nlongrightarrow L_c.
]
Both are line-bundle isomorphisms, so such a section forces
(L_{ab}cong L_c).

Their universal degrees are respectively ((1,1,0)) and ((0,0,1)).
Neither difference is nonnegative, so no homogeneous polynomial
isomorphism exists in either direction. Equivalently, relative
(mathbf G_m)-rescaling fixes the two endpoints and moves every point of
the open orbit; endpoint and orientation data do not select a midpoint.

Thus the primitive finite map (emapsto e_1+e_2) of entries 214 and 217
cannot be promoted by intrinsically subdividing the bare Rees
(mathbf P^1). This failure occurs before the 24 literal corestriction
rows: the source has no canonical middle support stratum to map to their
marked middle costalks.

## Scope and minimal repair

The no-go applies only to a strict realization obtained from a third section
of the exceptional projective bundle. It does not exclude a genuine
bivariant correspondence whose middle support is a proper span rather than a
section.

The minimal additional datum is one of:

1. a normalization-provenanced reduction/trivialization of the relative
   (mathbf G_m)-torsor, equivalently a clutching between (L_{ab}) and
   (L_c); or
2. a proper log-BM/nearby-cycle correspondence with a middle object mapping
   to both Rees charts and to the literal entry143 marked costalk, together
   with its Beck--Chevalley 2-cells.

Without such data, the adjacent-facet restrictions are not literal maps, so
the (q_Sigma) connector and endpoint/Q mapping fiber remain undefined.

## Certificate

Executable:
`research/voevodsky/check_dp6_rees_p1_middle_section_no_go.rs`

SHA-256:
`4df879ec5632fe11d1c24b6d8081159b488a7588ccf0853e431a0651c5d8860d`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed. Native PowerShell was used only because structured-command
MCP was unavailable.

## Outcome contract

~~~json
{
  "claim": "The bare product-Rees exceptional bundle P(L_ab plus L_c) has two canonical endpoint sections but no intrinsic third section realizing the marked corridor midpoint: such a section would force the forbidden isomorphism L_ab congruent L_c.",
  "status": "falsified_scoped_intrinsic_rees_p1_strict_subdivision",
  "scope": "section-based strict KN subdivision of the product-Rees exceptional P1; general bivariant correspondences excluded from the no-go",
  "factorization": {
    "endpoint_sections": 2,
    "required_corridor_strata": 3,
    "L_ab_degree": [1,1,0],
    "L_c_degree": [0,0,1],
    "forward_polynomial_isomorphism": false,
    "reverse_polynomial_isomorphism": false,
    "interior_section_requires_line_isomorphism": true,
    "relative_scaling_fixed_points": 2,
    "ordered_pairs": 6,
    "finite_log_gysin_matrix_still_valid": true,
    "general_bivariant_correspondence_no_go": false
  },
  "minimal_additional_datum": "A normalization-provenanced reduction of the relative Gm torsor, or a proper log-BM/nearby-cycle middle correspondence with maps to both Rees charts and the literal marked costalk plus Beck--Chevalley cells.",
  "evidence_refs": [
    "research/voevodsky/check_dp6_rees_p1_middle_section_no_go.rs",
    "src/ledger/20260815-215 Toric Star-Subdivision Line No-Go and the Clutching Datum.md",
    "src/ledger/20260815-216 Product-Branch Rees Clutching and the Literal Realization Gate.md",
    "src/ledger/20260815-217 Product-Rees Log-Excess Cap and the Literal Support Gate.md"
  ],
  "checker_sha256": "4df879ec5632fe11d1c24b6d8081159b488a7588ccf0853e431a0651c5d8860d",
  "next_experiment": "Construct or falsify a proper middle correspondence over the relative Gm torsor that realizes the marked entry143 middle costalk without choosing an interior section."
}
~~~
