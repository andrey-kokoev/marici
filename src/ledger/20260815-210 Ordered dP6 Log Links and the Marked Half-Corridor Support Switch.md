# Ordered dP6 Log Links and the Marked Half-Corridor Support Switch

Date: 2026-08-15  
Status: proved in the finite labelled log-link and carrier dictionary. The
line-valued extraordinary Gysin transformation and literal six-functor stalk
map remain unconstructed. No graph admission is claimed.

## Result

The two toric contractions of entry 165 label the six maximal cones of
(dP_6) by

[
(pi,pi_{m Cr})=
(0,1),(0,2),(1,2),(1,0),(2,0),(2,1).
]

These are exactly the six ordered pairs of distinct physical roads. Polarity
sends cone (i) to cone (i+3) and reverses its ordered pair. The omitted
road is therefore intrinsic and selects the complementary marked corridor
(q_k). The cyclicly ordered pairs select its positive marked half; their
reversals select the negative marked half.

This removes a previously unresolved carrier-level choice. It uses the actual
two toric contractions, not a fitted pairing between cones and roads.

For every ordered cone, the selected half-corridor consists of the two literal
entry-143 edges obtained from entry 99's marked half-gallery. Both edge
supports are compatible (K_6) faces of size two. Transporting the four
Boolean masks to (Hsubseteq S) on each edge gives:

[
6	ext{ cones}	imes4	ext{ masks}=24
]

source columns and (48) legal target edge-state terms. For every term the
Čech denominator support is exactly (Ssetminus H). The normal-removal
differential has the entry-143 signs

[
arnothing,qquad
{a}mapsto-arnothing,qquad
{b}mapsto-arnothing,qquad
{a,b}mapsto-{b}+{a},
]

and squares to zero. Rotation by two fan cones rotates both ordered road
labels, the complementary marked corridor, and its ordered Boolean basis. Each corridor's two halves
meet at the certified marked central vertex.

The two Tor grades remain spectator grades on each source column. They are
not the factor producing the number 24.

## Scope boundary

The checker derives a canonical target **support dictionary**. It does not
yet construct the morphism of coefficient or sheaf objects. In particular it
does not prove:

- the occurrence-line map from the crossing cone labels to the legal corridor
  edge labels;
- the multiplicity-sensitive excess-Gysin evaluation on those lines;
- the two adjacent-facet Beck--Chevalley coefficient squares;
- the literal six-functor costalk/corestriction realization;
- the strict reflection comparison 2-cell.

Accordingly this result does not instantiate the endpoint/Q mapping fiber or
determine (p_{partial,Q}).

## Next gate

On one seed cone, for example ((D_{14},D_{03})	o q_{25}^{+}), construct
the line-valued transformation

[
operatorname{or}_{log}otimes
I_{14}^{ee}otimes I_{03}^{ee}otimes
K_{m Tor/Cech}
longrightarrow
E_{143}|_{q_{25}^{+}}
]

and prove that its two log-boundary restrictions equal the certified
(D_{14}) and (D_{03}) facet packets. The present theorem fixes every
target support and Boolean sign of that transformation. Rotation and
polarity then fix the other five ordered cones.

## Certificate

- `research/voevodsky/check_dp6_ordered_pair_log_link_to_marked_corridor.rs`
- SHA-256:
  `1866dd8deca29f30c9e302419ce88c2c74678d33e7fe41691736a5e4b303ff9a`

Validation:

- `rustfmt --edition 2021 --check`: passed after formatting;
- `rustc --edition=2021 -D warnings -O`: passed;
- linked runtime assertions and JSON emission: passed;
- temporary executable removed.

## Outcome contract

~~~json
{
  "claim": "The two actual dP6 toric contractions canonically label its six cones by all ordered pairs of distinct roads. Pair reversal is polarity, the omitted road selects the complementary marked q_k corridor, and orientation selects its positive or negative marked half. This derives 24 source Boolean columns and 48 legal literal entry143 target edge-state terms with the exact normal and Cech signs.",
  "status": "proved_scoped_ordered_dp6_log_link_to_marked_half_corridor_dictionary",
  "scope": "finite labelled toric/log-link and entry143 carrier support dictionary; no line-valued extraordinary Gysin or literal six-functor realization",
  "evidence": {
    "ordered_cone_road_pairs": [[0,1],[0,2],[1,2],[1,0],[2,0],[2,1]],
    "polarity_reverses_ordered_pair": true,
    "complementary_corridors_each": 2,
    "plus_half_cones": 3,
    "minus_half_cones": 3,
    "source_boolean_columns": 24,
    "legal_target_boolean_terms": 48,
    "normal_d_squared": 0,
    "target_label_order": "moving_then_persistent",
    "D3_rotation_exact_on_ordered_boolean_basis": true,
    "retained_tor_grades": [0,1],
    "occurrence_line_map": "unconstructed",
    "adjacent_facet_BC": "unconstructed",
    "literal_six_functor_stalk_map": "unconstructed",
    "physical_mapping_fiber": "unconstructed"
  },
  "checker_sha256": "1866dd8deca29f30c9e302419ce88c2c74678d33e7fe41691736a5e4b303ff9a",
  "next_required_map": "Construct the occurrence-line/excess-Gysin transformation on one ordered cone and prove its two boundary restrictions equal the adjacent long-facet packets."
}
~~~
