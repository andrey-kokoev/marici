# Underived Rees Two-Boundary No-Go and the Derived Wall Datum

## Record

Date: 2026-08-15

Status: falsified the support-preserving realization of the complete literal
entry143 vertex cone by an underived product-Rees exceptional
\(\mathbf P^1\) having only its two coordinate boundary sections. This is
not a no-go for a derived/log-Borel--Moore or vanishing-cycle
correspondence. No graph admission is claimed.

## Earliest exact obstruction

The two standard Rees charts have two canonical boundary sections. Their
oriented Čech boundary has the primitive row
\[
(-1,+1).
\]
These sections can realize the two chart faces of the completed vertex
cone.

The literal entry143 vertex has three distinct codimension-one faces. In
the ordered cone axes
\[
(\tau,n_0,n_1),
\]
its primitive boundary is
\[
\iota_\tau+\iota_{n_0}-\iota_{n_1}.
\]
The \(n_0,n_1\) terms are the two Rees-chart restrictions. The
\(\tau\) term is the conductor-Tor wall restriction.

A support-preserving stratum map from two source boundary components can
meet at most two of these three target faces. Exhausting all
\(3^2=9\) assignments gives no full-support assignment. This is not a
Smith or multiplicity defect: both the two-term source boundary and the
three-term target boundary are primitive with unit Smith invariant.

The failure is already visible on the Boolean state containing only
\(\tau\). It has no chart restriction and one mandatory wall
restriction. Changing the signs or multiplicities of the two chart
sections therefore cannot manufacture its image.

## Relation to the earlier middle-section obstruction

One could try to add the wall as a third strict section of the same
exceptional \(\mathbf P^1\). Entry218 independently excludes that
construction: an interior section would identify the inequivalent
principal lines \(L_{ab}\) and \(L_c\).

Consequently the existing underived two-section Rees geometry cannot
realize the complete vertex cone. The missing wall must be a genuinely new
object, not a reweighting or subdivision of the two coordinate sections.

## Minimal additional datum

The minimal repair is a derived/log boundary or vanishing-cycle object
\(W_\tau\) carrying the conductor-Tor orientation, together with proper
Beck--Chevalley maps
\[
W_\tau\longrightarrow U_0,\qquad
W_\tau\longrightarrow U_1,\qquad
W_\tau\longrightarrow i_{e_k}^{!}
E_{\partial,Q}^{\mathrm{BM},\check C}.
\]
Its extraordinary boundary must be \(\iota_\tau\), while its two
chart comparisons must recover the already certified Čech signs. Its
relative dualizing line must also realize entry236's matching
principal-line evaluation. Only such an added object can geometrically
realize
\[
D=\iota_\tau+\iota_{n_0}-\iota_{n_1}
\]
without inventing a third section of the Rees \(\mathbf P^1\).

This theorem does not rule out that derived correspondence. It sharpens
the remaining construction by proving that an underived proper
two-boundary kernel is insufficient before endpoint or generic-\(Q\)
data enter.

## Executable evidence

Checker:
research/voevodsky/check_dp6_underived_rees_boundary_no_go.rs

SHA-256:
7c54f3b84f164fc853977503ef1ef1bb602caf58d3edbf07da79b9854ed62607

Fresh rustfmt --check, warnings-denied optimized compilation, runtime
assertions, and JSON output passed. Native PowerShell was used because no
repository-scoped structured-command MCP capable of invoking Rust is
exposed.

## Outcome contract

~~~json
{
  "claim": "An underived support-preserving product-Rees exceptional P1 with only its two coordinate boundary sections cannot realize the three distinct primitive faces of the completed literal entry143 vertex cone. The missing conductor-Tor wall is a genuinely derived/log boundary datum.",
  "status": "falsified_scoped_underived_two_boundary_rees_realization",
  "scope": "underived proper/log-smooth support-preserving realizations whose exceptional boundary is exactly the two existing coordinate sections; general derived/log-BM and vanishing-cycle correspondences excluded",
  "matrix": {
    "ordered_pairs": 6,
    "source_boundary_strata": 2,
    "target_vertex_faces": 3,
    "stratumwise_assignments_checked": 9,
    "full_support_assignments": 0,
    "source_boundary_smith_all_ones": true,
    "target_boundary_smith_all_ones": true,
    "tau_only_chart_terms": 0,
    "tau_only_required_wall_terms": 1,
    "missing_primitive_wall_rows": 6,
    "multiplicity_or_sign_repair_possible": false
  },
  "minimal_additional_datum": "A genuine third derived/log boundary or vanishing-cycle object carrying the conductor-Tor contraction, with proper Beck-Chevalley maps to both Rees charts and the literal entry143 wall costalk, plus the matching principal-line dualizing evaluation.",
  "unconstructed": [
    "derived/log wall correspondence",
    "proper Beck-Chevalley realization of all 72 rows",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_underived_rees_boundary_no_go.rs",
  "checker_sha256": "7c54f3b84f164fc853977503ef1ef1bb602caf58d3edbf07da79b9854ed62607"
}
~~~
