# Product-Branch Rees Clutching and the Literal Realization Gate

## Record

Date: 2026-08-15

Status: proved in the universal product-branch Rees coefficient geometry.
The literal entry143 six-functor realization and adjacent-facet
Beck--Chevalley maps remain unconstructed. No graph admission is claimed.

## Construction

For two ordered adjacent branch sections (a,b) and the complementary
long-road section (c), use the Rees blowup
[
Y=operatorname{Bl}_{(ab,c)}operatorname{Spec}mathbf Z[a,b,c].
]
With homogeneous coordinates ([A:B]), its equation is
[
cA-abB=0.
]
On (A
e0), writing (t=B/A) gives the polynomial chart
(c=abt). On (B
e0), writing (s=A/B) gives the normal conifold
chart
[
cs=ab.
]

The tautological Rees line carries (ab) and (c) as its two labelled
sections. It therefore interpolates the product branch and complementary
road without identifying their multidegrees and without inverting any base
section. This bypasses, but does not contradict, entry 215's direct
line-isomorphism no-go.

After (b) is made a unit, the construction is the ordinary blowup of
((a,c)); after (a) is made a unit, it is the blowup of ((b,c)).
Thus the two adjacent branch packets are recovered with multiplicities
((1,1)). Over (ab=c=0), the exceptional fibre is canonically
(mathbf P^1).

The center ((ab,c)) is a regular sequence. Its Koszul row has
(d_1=[ab,c]), (d_2=[-c,ab]^T), so (d_1d_2=0), and the derived
self-intersection has exterior ranks ((1,2,1)). Rotation permutes the
three labelled coordinates. Reversing the ordered branch pair fixes the
product and Rees equation while reversing the separate log orientation.

## Exact scope boundary

This establishes a canonical multiplicity-sensitive clutching carrier and
its two branch restrictions. It does not yet identify the exceptional
(mathbf P^1), its KN/log-BM cap, or its derived Tor packet with the
literal entry143 ([S,H]) stalks and corestrictions. In particular, the
adjacent-facet Beck--Chevalley squares, endpoint framing, generic
(q_Sigma) connector, endpoint/Q mapping fiber, physical parity,
Bockstein, and (D_8)/Jordan tests remain open.

The next exact step is to construct the oriented log-excess cap. At the
characteristic-lattice level this means comparing the product map
[
mathbf Zlongrightarrowmathbf Z^2,qquad 1longmapsto(1,1)
]
with its primitive anti-diagonal quotient, and proving that its exterior
contraction realizes the four legal Boolean/Tor states and the two adjacent
facet restrictions. That calculation must then be promoted to the literal
entry143 support diagram.

## Certificate

Executable:
`research/voevodsky/check_dp6_product_branch_rees_clutching.rs`

SHA-256:
`8d35cd75398302c8fb912ba2ea39ef01373f9e83e3f1895684b82d91ebf7c28a`

Rustfmt, warnings-denied optimized compilation, runtime assertions, and JSON
parsing passed. Native PowerShell was used only because structured-command
MCP was unavailable.

## Outcome contract

~~~json
{
  "claim": "The blowup of the product-branch ideal (ab,c) canonically interpolates the two adjacent multiplicity-one Rees packets and the complementary road through its tautological line, without a direct multigraded line isomorphism or base localization.",
  "status": "proved_scoped_product_branch_rees_clutching_geometry",
  "scope": "universal algebraic/log coefficient geometry of Bl_(ab,c), excluding literal entry143 six-functor realization",
  "factorization": {
    "center_ideal": "(a*b,c)",
    "rees_equation": "c*A-a*b*B=0",
    "A_chart": "Z[a,b,t] with c=a*b*t",
    "B_chart": "Z[a,b,c,s]/(c*s-a*b)",
    "B_chart_normal": true,
    "branch_restrictions": [
      "Bl_(a,c) after b is a unit",
      "Bl_(b,c) after a is a unit"
    ],
    "branch_multiplicities": [1, 1],
    "triple_center_fibre": "P1",
    "center_regular_sequence": true,
    "derived_self_intersection_tor_ranks": [1, 2, 1],
    "tautological_rees_interpolation": true,
    "direct_line_isomorphism": false,
    "base_inversions": false,
    "D3_covariant": true,
    "reflection_log_orientation_odd": true,
    "literal_entry143_realization_constructed": false,
    "adjacent_facet_BC_as_six_functor_map_constructed": false
  },
  "minimal_remaining_datum": "The KN/log-BM realization of the Rees P1 and a support-typed comparison identifying its two branch restrictions, Tor/excess grades, and Cech rows with the literal adjacent entry143 facet packets.",
  "evidence_refs": [
    "research/voevodsky/check_dp6_product_branch_rees_clutching.rs",
    "src/ledger/20260815-214 Finite Ordered Log-Link Gysin Matrix and the Spatial Realization Gate.md",
    "src/ledger/20260815-215 Toric Star-Subdivision Line No-Go and the Clutching Datum.md"
  ],
  "checker_sha256": "8d35cd75398302c8fb912ba2ea39ef01373f9e83e3f1895684b82d91ebf7c28a",
  "next_experiment": "Construct the primitive characteristic-lattice excess contraction and derive its literal four-state entry143 branch/corestriction rows."
}
~~~
