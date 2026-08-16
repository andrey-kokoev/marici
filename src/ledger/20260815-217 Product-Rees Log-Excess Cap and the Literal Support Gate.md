# Product-Rees Log-Excess Cap and the Literal Support Gate

## Record

Date: 2026-08-15

Status: proved in the finite labelled characteristic-lattice/Koszul model.
The support-typed realization in the literal entry143 diagram remains
unconstructed. No graph admission is claimed.

## Primitive full-log cap

For an ordered adjacent branch pair, let (a,b) be its characteristic
generators and let (c) be the complementary Rees direction. The product
branch is the primitive diagonal
[
d=a+b.
]
The quotient functional
[
delta(a)=-1,qquad delta(b)=+1,qquad delta(c)=0
]
is primitive and has kernel (mathbf Zlangle d,cangle).

Contraction by (delta) gives a degree-lowering integral map
[
iota_delta:Lambda^ulletmathbf Zlangle a,b,cangle
 longrightarrow
Lambda^{ullet-1}mathbf Zlangle d,cangle.
]
In the ordered bases ((a,b,c)), ((awedge b,awedge c,bwedge c)),
and (awedge bwedge c), its nonzero matrices are
[
[-1  1  0],qquad
egin{bmatrix}-1&0&0\0&-1&1end{bmatrix},qquad
[-1].
]
Their ranks are (1,2,1), and their Smith factors are respectively
((1)), ((1,1)), and ((1)). The cap is therefore surjective and
torsion-free in every nonzero degree.

The target exterior packet has ranks ((1,2,1)), exactly the four
two-normal Boolean/Tor states. The two adjacent branch residues are
((-1,+1)), so multiplicity and orientation are derived rather than
stipulated. Across six ordered pairs this gives 24 labelled Boolean rows.
Reversing the pair changes both (delta) and the log orientation sign;
their product is invariant. Rotation merely relabels the three roads.

## Scope boundary

This computation supplies the missing primitive excess algebra for entry
216 and composes coefficientwise with entry 214's finite 24-column map. It
does not prove that the exceptional Rees (mathbf P^1), its KN strata,
or these exterior generators map to the literal entry143 ([S,H])
stalks. Consequently the adjacent-facet six-functor Beck--Chevalley
squares and endpoint framing are still not established.

The next gate is a support-typed KN/log-BM realization whose restrictions
to the two labelled Rees charts recover the adjacent facet packets and
whose four target states are the actual entry143 occurrence,
normal-circle, Tor, and Čech rows. Only after that comparison can the
generic (q_Sigma) row and endpoint/Q mapping fiber be instantiated.

## Certificate

Executable:
`research/voevodsky/check_dp6_product_rees_log_excess_cap.rs`

SHA-256:
`92f340d99bbfe77e6cdea75add0e975ef0c4b6045596f9caf9f3db8c8ad6cefa`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed. Native PowerShell was used only because structured-command
MCP was unavailable.

## Outcome contract

~~~json
{
  "claim": "The product-branch log characteristic sequence has a canonical primitive anti-diagonal excess functional whose exterior contraction maps the eight three-direction log states surjectively onto the four legal two-normal Boolean/Tor states, with all Smith factors one.",
  "status": "proved_scoped_primitive_log_excess_cap",
  "scope": "finite labelled characteristic-lattice and Koszul coefficient geometry, excluding literal entry143 support realization",
  "matrix": {
    "characteristic_map": "1->(1,1)",
    "excess_functional": [-1,1,0],
    "source_exterior_ranks": [1,3,3,1],
    "target_boolean_ranks": [1,2,1],
    "cap_ranks": [1,2,1],
    "cap_smith_factors": [[1],[1,1],[1]],
    "integer_torsion": false,
    "branch_residues": [-1,1],
    "ordered_pairs": 6,
    "derived_boolean_rows": 24,
    "D3_covariant": true,
    "reflection_loaded_covariant": true,
    "base_inversions": false
  },
  "unconstructed": [
    "literal entry143 support map",
    "adjacent-facet six-functor Beck--Chevalley squares",
    "endpoint framing",
    "generic qSigma connector",
    "endpoint/Q mapping fiber and physical parity"
  ],
  "evidence_refs": [
    "research/voevodsky/check_dp6_product_rees_log_excess_cap.rs",
    "src/ledger/20260815-214 Finite Ordered Log-Link Gysin Matrix and the Spatial Realization Gate.md",
    "src/ledger/20260815-216 Product-Branch Rees Clutching and the Literal Realization Gate.md"
  ],
  "checker_sha256": "92f340d99bbfe77e6cdea75add0e975ef0c4b6045596f9caf9f3db8c8ad6cefa",
  "next_experiment": "Construct the support-typed KN/log-BM map from the Rees exceptional P1 to the 24 literal entry143 rows and verify both adjacent-facet BC squares."
}
~~~
