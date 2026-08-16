# Rees--Čech Tor Third-Edge Packet and the Vertex-Cone Gate

## Record

Date: 2026-08-15

Status: the third-edge packet and its integral residue matrix are proved,
but the direct overlap-to-third-edge total chain map is falsified. The
Čech overlap has a nonzero chart-difference boundary that cannot land in
the literal direct sum of edge-support grades. A vertex-supported cone is
the minimal additional datum. No graph admission is claimed.

## The candidate third-edge packet

For each ordered product-Rees pair, the two standard charts determine the
two previously selected corridor edges. Their common legal triangulation
vertex has one remaining codimension-one face.

The Rees cover has a canonical relative-\(\mathbf G_m\) overlap in Čech
degree \(+1\). After the primitive full-log cap, write the three source
axes as
\[
(\tau,n_0,n_1),
\]
where \(\tau\) is the conductor Tor axis and \(n_0,n_1\) are the two
moving normal axes. The chart restrictions are contraction by \(n_1\)
and \(n_0\). Contracting the overlap packet by \(\tau\) produces the
remaining edge:
\[
\iota_\tau:
\Lambda^\bullet\langle\tau,n_0,n_1\rangle
\longrightarrow
\Lambda^{\bullet-1}\langle n_0,n_1\rangle.
\]
The overlap Čech shift and Tor contraction cancel:
\[
(+1)+(-1)=0.
\]
Thus the overlap packet has the same total degree and rank as the third
edge packet.

This assignment is forced by incidence. The first chart edge omits
\(n_1\), the second omits \(n_0\), and the only remaining literal edge
omits \(\tau\). No additional face, midpoint, base localization, or
fractional coefficient is introduced.

## Integral matrix

For each ordered pair, the three residue blocks form a \(12\times8\)
matrix. The empty source state is its sole zero column. For each of the
seven nonempty states, contraction along its least present axis selects a
distinct unit pivot. Hence the block has rank seven and seven Smith factors
equal to one.

Across six ordered pairs:

- the combined residue matrix has 72 rows and rank 42;
- all 42 nonzero Smith factors are one;
- the new overlap-to-third-edge block has 24 rows, rank 24, and 24 unit
  Smith factors;
- all 72 normal-removal squares commute;
- no base section is inverted.

## Incidence and symmetry

Rotation transports all six full vertex stars. Physical reflection
\(v\mapsto3-v\) permutes every star as a set, including the previously
missing third edges. It can exchange a chart role with the overlap role,
which is why the two-edge truncation failed.

Reflection reverses both the Čech overlap orientation and the conductor Tor
orientation. Their signs multiply to \(+1\), while their degree shifts
cancel. Consequently the *packet and incidence-star* data are
reflection-compatible after the already fixed road-orientation convention.

## The total chain equation fails

The Rees overlap is not a closed third boundary component. Its Čech
differential is the primitive chart difference
\[
d_{\check C}U_\times=-U_0+U_1.
\]
Project literal entry143 to the direct sum of the three edge-support
grades of the common vertex. There is no differential from one distinct
edge summand to another in this quotient: radial maps go from an edge to
the common vertex. Therefore the target differential of the proposed
third-edge image is zero, while the image of the source differential is
\((-1,+1,0)\).

Hence
\[
d_{143}\,\Gamma(U_\times)=0
\ne
(-e_0+e_1)=\Gamma(d_{\check C}U_\times).
\]
The degree, sign, rank, and Smith checks are necessary but insufficient:
the direct overlap-to-third-edge assignment is not a chain map.

## Minimal repair

The smallest repair is a vertex-supported cone or Beck--Chevalley
homotopy whose boundary realizes the primitive chart difference. Its
radial maps must carry the actual occurrence sections, so principal-line
Gysin evaluations—not scalar identities—must compare them with the unit
Čech coefficients.

Only after adjoining and geometrically deriving that cone can one define
the spatial transformation
\[
R\pi_!\operatorname{Tot}(U_0\leftarrow U_\times\to U_1)
\longrightarrow E_{\partial,Q}^{\mathrm{BM,\check C}}
\]
whose overlap/Tor packet participates in a literal vertex-star chain map.
Proper base change, local-cohomology variance, endpoint restriction, and
the based \(q_\Sigma\) comparison remain unconstructed.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_rees_cech_tor_vertex_star.rs`

SHA-256:
`87c808735bc183fce671a442142f083920038356c0a8dbe7c351b57923c73f71`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON field checks passed. Native PowerShell was used for
Rust verification because no repository-scoped structured-command MCP
capable of invoking `rustc` is exposed.

## Outcome contract

~~~json
{
  "claim": "The relative-Gm overlap and Tor contraction produce the unique integral third-edge packet, but mapping that overlap directly to the third literal edge is not a total chain map: its Cech boundary is the nonzero chart difference while the target edge-support quotient has zero edge-to-edge differential.",
  "status": "falsified_scoped_overlap_to_third_edge_chain_map",
  "scope": "finite labelled product-Rees/Cech/Tor total complex and literal entry143 edge-support quotient; vertex-supported cone enlargements are not excluded",
  "matrix": {
    "ordered_pairs": 6,
    "edges_per_vertex": 3,
    "combined_rows": 72,
    "combined_rank": 42,
    "all_nonzero_smith_factors": 1,
    "third_edge_packet_rows": 24,
    "third_edge_packet_rank": 24,
    "third_edge_packet_smith_factors": 24,
    "normal_chain_squares": 72,
    "base_inversions": false
  },
  "degree_and_orientation": {
    "overlap_cech_degree": 1,
    "tor_contraction_degree": -1,
    "total_degree": 0,
    "reflection_cech_sign": -1,
    "reflection_tor_sign": -1,
    "loaded_reflection_sign": 1
  },
  "chain_falsifier": {
    "source_cech_boundary": [-1, 1, 0],
    "target_edge_quotient_differential_rank": 0,
    "direct_overlap_to_third_edge_chain_equation": false
  },
  "symmetry": {
    "D3_rotation_incidence_star": true,
    "physical_reflection_incidence_star": true,
    "reflection_mixes_chart_and_overlap_roles": true
  },
  "unconstructed": [
    "vertex-supported cone/Beck-Chevalley homotopy",
    "proper log-BM six-functor realization",
    "literal entry143 costalk/base-change comparison",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_rees_cech_tor_vertex_star.rs",
  "minimal_additional_geometry": "A vertex-supported cone/Beck-Chevalley homotopy whose boundary is the primitive chart difference and whose principal-line Gysin maps match the literal radial occurrence coefficients.",
  "checker_sha256": "87c808735bc183fce671a442142f083920038356c0a8dbe7c351b57923c73f71"
}
~~~
