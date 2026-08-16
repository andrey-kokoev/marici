# Single-Top Generic Normalization No-Go and the Can-Var Two-Top Gate

Date: 2026-08-15  
Status: falsified for identifying the projective-conductor coherence top with
the primitive physical mixed top. A two-top log can--var extension remains
open. No graph admission is claimed.

## Result

Entry 202 fixes the cyclic carrier equation:

    F_14,03 + F_03,25 + F_25,14 = -2 * boundary(K6_top).

Consequently, if a single primitive projective-conductor source top maps to
the primitive K6 top line, the carrier chain equation forces its coefficient
to have absolute value two. Entry 203 identifies the geometric source of that
magnitude: the regular conductor center has codimension three, so its
relative-canonical discrepancy is 3-1=2.

The same top cannot simultaneously be entry 113's physical mixed top. That
block has independently fixed primitive normalization

    d H_Sigma = q_Sigma - sum_D x_D * xi_D,

and projective-bundle Gysin normalization q_*(xi^2)=1. Therefore the
coefficient of the based q_Sigma leg has absolute value one. Orientation
changes signs but cannot change the incompatible magnitudes |2| and |1|.

In the fixed entry-202/entry-113 orientations, the affine requirements on one
coefficient are a=-2 and a=+1; their difference is -3. The homogeneous
coefficient matrix is primitive with Smith factor 1, so the failure is an
affine normalization incompatibility, not torsion removable by a contractible
stabilization.

## Consequence

Entry 203 remains valid in its stated conditional carrier scope: discrepancy
two saturates the enlarged carrier matrix once a primitive coherence-top
column is supplied. The coherence top must not be identified with physical
mixed H_Sigma.

The smallest algebraic enlargement has two primitive generators:

- C_Sigma, the cyclic-coherence top, with coefficient two into the K6 top;
- H_Sigma, the physical mixed top, with primitive coefficient one into the
  based q_Sigma boundary.

Their coefficient matrix is the unimodular diagonal matrix diag(1,1).
Geometry must join them by an independently constructed log nearby-cycle
can--var or Beck--Chevalley cell.

## Earliest remaining datum

Construct a normalization-provenanced two-top log object with:

1. discrepancy-two cyclic-coherence generator C_Sigma;
2. primitive mixed generator H_Sigma;
3. a can--var/nearby-cycle comparison between them;
4. residues to all three long-facet packets;
5. support-switch maps deriving all 24 literal entry-143 rows;
6. endpoint framing and reflection compatibility.

Only then can the literal full matrix, endpoint/Q mapping fiber,
p_partial,Q, Bockstein, D8, and Jordan tests be formed.

## Certificate

- research/voevodsky/check_p2_single_top_qsigma_normalization_no_go.rs
- SHA-256:
  8337c6fa0dff225578d1080bc0066a34333cd02edf390f0d478c43ff7eba8111

Validation through the user-site structured-command MCP:

- rustfmt --edition 2021 --check: pass;
- rustc --edition=2021 -D warnings --emit=metadata: pass;
- optimized linked executable: pass;
- runtime assertions and JSON parse: pass;
- temporary artifacts and validation script: removed.

## Outcome contract

~~~json
{
  "claim": "A single primitive projective-conductor source top cannot both close the certified pairwise cyclic K6 defect and realize entry113's primitive qSigma mixed boundary: the first forces absolute coefficient two and the second absolute coefficient one.",
  "status": "falsified_scoped_single_top_spatial_promotion",
  "scope": "single-top integral promotion only; no no-go against a two-top log can-var extension or a general extraordinary spatial kernel",
  "evidence": {
    "pairwise_cyclic_top_defect": -2,
    "conductor_codimension": 3,
    "relative_canonical_discrepancy": 2,
    "carrier_forced_absolute_coefficient": 2,
    "projective_gysin_top": 1,
    "physical_qSigma_coefficient": 1,
    "generic_forced_absolute_coefficient": 1,
    "simultaneous_integer_solution": false,
    "fixed_orientation_affine_difference": -3,
    "homogeneous_smith": [1],
    "minimal_two_top_matrix_smith": [1, 1],
    "literal_entry143_rows": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_bockstein": "undefined",
    "D8_and_Jordan": "untested"
  },
  "checker_sha256": "8337c6fa0dff225578d1080bc0066a34333cd02edf390f0d478c43ff7eba8111",
  "minimal_additional_geometry": "Separate cyclic-coherence top C_Sigma and physical mixed top H_Sigma, then construct a geometric log nearby-cycle can-var/Beck-Chevalley cell between them before deriving the 24 literal rows."
}
~~~
