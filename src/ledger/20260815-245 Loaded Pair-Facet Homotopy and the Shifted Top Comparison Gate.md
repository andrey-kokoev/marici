# Loaded Pair-Facet Homotopy and the Shifted Top Comparison Gate

## Record

Date: 2026-08-15

Status: proved in the finite labelled constructible/exit-path category. The
six oriented KN vertex packets extend canonically from literal entry143
vertices and edges to all incident loaded facet states. The requested 24
pair-corridor rows occur as a distinguished subset, but reflection closure
forces 48 additional third-wall rows. The normalization-source six-functor
realization and global shifted top comparison remain unconstructed. No graph
admission is claimed.

## Loaded facet construction

For each ordered long-road pair, the completed KN packet has three oriented
axes
\[
(\tau,n_0,n_1),
\]
which entry329 identifies with the three labels of one literal compatible
\(K_6\) triangulation vertex. Retaining one axis and contracting the other
two maps to the corresponding one-label facet.

For every source mask containing the two omitted axes, the two contraction
orders satisfy
\[
\iota_j\iota_i=-\iota_i\iota_j.
\]
Their target mask is the same, and both coefficients are primitive units.
This is the required shifted facet-homotopy equation; it is derived from the
exterior differential rather than inserted as a scalar correction.

Each facet has two literal Boolean states. Retaining both conductor Tor
grades gives
\[
6\ \text{vertices}\times3\ \text{facets}\times2\ H\text{-states}
\times2\ \text{Tor grades}=72
\]
literal loaded rows.

Of these:

- 24 are the corridor-persistent rows requested for the six ordered pair
  objects;
- 48 are the complementary moving/third-wall rows required for physical
  reflection closure.

The selected two-edge corridor alone is not reflection-stable. The complete
three-facet vertex star is stable under rotation and reflection.

## Integral matrix

Choosing either oriented contraction order supplies one unit pivot for each
of the 72 literal facet/Boolean/Tor rows. Hence the matrix has rank 72 and
all 72 nonzero Smith factors are \(1\). There is no integer torsion, no
occurrence-section inversion, and no division by two.

The checker independently verifies 36 pairs of contraction paths and 144
principal-line evaluations. The opposite path signs are the mapping-cone
shift that the same-degree negative control in entry332 proved necessary.

## Remaining gate

This closes the loaded vertex-to-facet continuation only in the finite
constructible realization. The next chain equation must assemble:

1. these 72 loaded facet homotopies;
2. the nine carrier facet cells and their primitive K6 top boundary;
3. entry223's external projectivized-conductor top and based
   \(q_\Sigma\) row; and
4. the two normalization-provenanced endpoint odd counits.

That assembly must be a shifted mapping cone. Treating its odd orbit as an
ordinary extra column is ruled out by entry332.

Until the shifted global top comparison is constructed in the literal
BM–Čech mapping complex, the endpoint/\(Q\) mapping fiber,
\(p_{\partial,Q}\), its polarity Bockstein, and \(D_8\)/Jordan coherence
remain undefined.

## Executable evidence

Checker:
research/voevodsky/check_dp6_loaded_vertex_facet_pushforward.rs

SHA-256:
1139596ce687b37e27f0a3b702ea89d66fc36414600ad3b67d80bfd74e319a79

The user-site structured-command MCP ran rustfmt check, warnings-denied Rust
metadata compilation, linked optimized compilation, and the executable
assertions. All returned exit code zero. The linked executable and temporary
validation scripts were removed.

## Outcome contract

~~~json
{
  "claim": "The six oriented KN vertex packets admit a canonical loaded continuation to all literal entry143 facet states; the two excess-contraction orders have opposite Koszul signs and give a saturated shifted facet homotopy.",
  "status": "proved_scoped_loaded_KN_vertex_to_literal_facet_homotopy",
  "scope": "finite labelled constructible/exit-path vertex-edge-facet realization; normalization-source six-functor and global top comparison excluded",
  "matrix": {
    "ordered_pair_vertices": 6,
    "literal_facets_per_vertex": 3,
    "boolean_states_per_facet": 2,
    "tor_grades": [0,1],
    "literal_facet_rows": 72,
    "corridor_persistent_rows": 24,
    "reflection_completing_rows": 48,
    "two_contraction_path_checks": 36,
    "principal_line_evaluations": 144,
    "rank": 72,
    "smith_nonzero_all_ones": true,
    "torsion": false
  },
  "symmetry": {
    "D3_rotation": true,
    "physical_reflection_full_vertex_star": true,
    "selected_two_edge_star_reflection_closed": false
  },
  "unconstructed": [
    "normalization-source sheaf-level six-functor realization",
    "shifted literal K6-to-entry223 top comparison",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_loaded_vertex_facet_pushforward.rs",
  "checker_sha256": "1139596ce687b37e27f0a3b702ea89d66fc36414600ad3b67d80bfd74e319a79"
}
~~~
