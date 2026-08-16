# Mixed-Cone Toroidal Map No-Go and the Minimal Log Expansion

## Record

Date: 2026-08-16

Status: definitive scoped no-go for a direct label-preserving toroidal map
from the six mixed cones of the full-log conductor source into the literal
entry143 (K_6) cone complex. The minimal equivariant boundary expansion is
proved. Maximal-cone Beck--Chevalley cells, the global six-functor kernel,
and the based (q_Sigma) comparison remain unconstructed. No graph
admission is claimed.

## First obstruction in the log category

The full-log toric source has six mixed cross-sheet two-cones. The two
labelled endpoint chambers of each mixed cone are literal (K_6)
triangulations, but their common compatible face is empty.

A toroidal/log morphism induces a map of cone complexes and must carry each
source cone into one target cone. A direct label-preserving map would
therefore require a common target cone for the two endpoint labels of every
mixed source cone. The executable census proves that no such cone exists for
any of the six mixed cones.

This obstruction is stronger in scope than the ordinary face-poset
observation: it rules out the unexpanded fs-log/toroidal source map itself.
It does not rule out a logarithmic expansion, derived correspondence, or
proper extraordinary push--pull.

## Minimal boundary expansion

The (K_6) flip graph has fourteen triangulation chambers. For each mixed
source cone, the two endpoint chambers have distance three and admit exactly
one shortest gallery. Thus the minimal cone-complex repair subdivides the
source-link interval into three chambers by inserting two intermediate
strata.

Across the six mixed cones this gives:

- eighteen expanded chambers;
- twelve inserted vertices; and
- six uniquely determined galleries.

Rotation and physical reflection permute the complete six-gallery system.
No road multiplicity is divided and no occurrence or normal line is
identified with another.

## Remaining construction

The expansion fixes the first missing support map but does not yet construct
the extraordinary correspondence. The next object must extend these six
expanded boundary galleries over the eight maximal cones of
(prod_Dmathbf P(mathcal Ooplus L_D)), with:

1. the independently defined occurrence, normal-circle, Tor, and Čech
   differentials;
2. the twenty-four maximal-cone Beck--Chevalley homotopies;
3. proper pushforward to the literal entry143 facet and endpoint stars; and
4. the hemisphere/top comparison to the based (q_Sigma) generator.

Only after those vertical maps are constructed can the integral global
matrix, pointed endpoint/(Q) mapping fiber, physical
(p_{partial,Q}), its Bockstein, (D_8), and Jordan coherence be
computed.

## Executable evidence

Checker:
`research/voevodsky/check_full_log_mixed_cone_toroidal_expansion_gate.rs`

SHA-256:
`0ab2fbeb2287acbe078c3ea828a1f6643004bf741c97873c6c3ba012824e6103`

Fresh `rustfmt --edition 2021 --check`, warnings-denied optimized
compilation, runtime assertions, and JSON emission passed.

## Outcome contract

~~~json
{
  "status": "falsified_scoped_direct_full_log_toroidal_map",
  "scope": "direct label-preserving cone-complex/toroidal map from the six unexpanded mixed source cones; logarithmic expansions and extraordinary correspondences remain open",
  "mixed_edges": 6,
  "endpoint_common_target_cones": 0,
  "k6_triangulations": 14,
  "unique_shortest_gallery_length": 3,
  "unique_galleries": 6,
  "minimal_log_expansion": {
    "chambers": 18,
    "inserted_vertices": 12
  },
  "D3_rotation": true,
  "physical_reflection": true,
  "integer_inverted": false,
  "unconstructed": [
    "occurrence/normal/Tor/Cech vertical transformations on the expansion",
    "maximal-cone Beck-Chevalley realization",
    "global six-functor kernel",
    "based qSigma attachment",
    "pointed endpoint/Q mapping fiber",
    "physical p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_full_log_mixed_cone_toroidal_expansion_gate.rs",
  "checker_sha256": "0ab2fbeb2287acbe078c3ea828a1f6643004bf741c97873c6c3ba012824e6103",
  "graph_admission_claimed": false
}
~~~
