# Paired-Incidence Lines on the Ordered Marked Corridors

## Record

Date: 2026-08-15

Status: proved for the normalization/conductor coefficient-line dictionary on
the six ordered (dP_6) cones. The proper/log-BM realization, adjacent-facet
Beck--Chevalley naturality, and literal six-functor map remain unconstructed.
No graph admission is claimed.

## Result

Entry 210 derives the six ordered long-road pairs and their complementary
marked half-corridors. Entry 164 supplies the normalization-provenanced paired
branch labels
[
z_0=(x_5,x_2),qquad z_1=(x_3,x_0),qquad z_2=(x_1,x_4).
]
On each ordered cone, the first marked-corridor edge consists of two short
labels that occur uniquely in the appropriate plus or minus sheet of this
paired list. The second edge retains the persistent branch label and replaces
the moving short label by the complementary long-road coordinate.

This derives a homogeneous occurrence-line dictionary for all six cones.
For every one of the four Boolean normal states, the target Čech denominator
is exactly the product indexed by (Ssetminus H). Hence the census is
[
6cdot4=24
]
source columns and two legal literal entry-143 target terms per column, for
48 target terms. The ordered Boolean basis is preserved by rotation;
polarity reverses the ordered cone and exchanges sheets. The normal-removal
differential squares to zero. Tor grades (0,1) remain external spectators
and are not incorrectly counted as extra source columns.

## Exact boundary

This theorem fixes line labels and Čech legality. It does not construct a
proper push--pull or an extraordinary natural transformation. In particular,
it does not prove that the two boundary restrictions of the proposed
(Gamma_{ij}^{!,log}) equal the already constructed adjacent long-facet
packets. That equality still requires a spatial log-BM/nearby-cycle kernel and
its Beck--Chevalley cells. Consequently the endpoint/Q mapping fiber,
(p_{partial,Q}), its Bockstein, and downstream (D_8)/Jordan coherence
remain undefined.

## Certificate

The executable certificate is
`research/voevodsky/check_dp6_incidence_line_to_corridor.rs`, SHA-256
`7bbb841027a58c006ec17ccc71ae99919f021cf1d271bd2a28be95a23e71a54e`.

Native PowerShell was used only because structured-command MCP was not exposed.
`rustfmt --edition 2021 --check`, `rustc --edition=2021 -D warnings -O`,
runtime assertions, and JSON parsing passed.

## Outcome contract

~~~json
{
  "claim": "The entry164 paired branch labels and the omitted projective coordinate canonically determine the occurrence-line labels of all 24 ordered dP6 Boolean source columns and their 48 legal marked-corridor target terms.",
  "status": "proved_scoped_coefficient_line_dictionary",
  "scope": "normalization/conductor coefficient lines, ordered dP6 carrier, and literal entry143 label/Cech legality only",
  "factorization": {
    "ordered_cones": 6,
    "source_boolean_columns": 24,
    "literal_target_terms": 48,
    "paired_branch_provenance": "proved",
    "complementary_long_coordinate": "proved",
    "cech_S_minus_H": "proved",
    "normal_d_squared": 0,
    "D3_rotation": "proved",
    "polarity_sheet_exchange": "proved",
    "Tor_grades": [0, 1],
    "proper_log_BM_realization": "unconstructed",
    "adjacent_facet_BC": "unconstructed",
    "literal_six_functor_map": "unconstructed",
    "endpoint_Q_mapping_fiber": "unconstructed"
  },
  "evidence_refs": [
    "research/voevodsky/check_dp6_incidence_line_to_corridor.rs",
    "src/ledger/20260815-164 Paired-Incidence Descent and the Reduced cdh Vertex Connector.md",
    "src/ledger/20260815-165 dP6 Common Refinement and the Log-Boundary Gysin Gate.md",
    "src/ledger/20260815-210 Ordered dP6 Log Links and the Marked Half-Corridor Support Switch.md"
  ],
  "checker_sha256": "7bbb841027a58c006ec17ccc71ae99919f021cf1d271bd2a28be95a23e71a54e",
  "next_experiment": "Construct one proper/log-BM seed kernel realizing this forced line dictionary and prove its two boundary restrictions are the adjacent long-facet packets; rotate only after that Beck-Chevalley square is established."
}
~~~
