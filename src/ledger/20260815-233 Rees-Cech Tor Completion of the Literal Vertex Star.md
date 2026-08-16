# Rees--Čech Tor Completion of the Literal Vertex Star

## Record

Date: 2026-08-15

Status: proved in the finite labelled derived product-Rees/Čech category.
The third-edge wall packet required by entry232 is constructed integrally
and the full literal vertex star is closed under \(D_3\) and physical
reflection. A proper/log six-functor realization into the literal entry143
costalks remains unconstructed. No graph admission is claimed.

## The third edge is the shifted overlap

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
Thus the overlap lands in the same total degree as the two chart edges.

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

## Symmetry

Rotation transports all six full vertex stars. Physical reflection
\(v\mapsto3-v\) permutes every star as a set, including the previously
missing third edges. It can exchange a chart role with the overlap role,
which is why the two-edge truncation failed.

Reflection reverses both the Čech overlap orientation and the conductor Tor
orientation. Their signs multiply to \(+1\), while their degree shifts
cancel. The completed finite derived star is therefore strictly
reflection-compatible after the already fixed road-orientation convention.

## Remaining geometric gate

This proves the required third-edge cell only in the finite labelled
derived Rees--Čech model. It does not yet construct the spatial
transformation
\[
R\pi_!\operatorname{Tot}(U_0\leftarrow U_\times\to U_1)
\longrightarrow E_{\partial,Q}^{\mathrm{BM,\check C}}
\]
whose overlap/Tor contraction is the literal third-edge entry143 costalk
map. In particular, proper base change, local-cohomology variance, endpoint
restriction, and the based \(q_\Sigma\) comparison are not consequences
of the finite matrix.

The next step is to realize this full star as a proper log-BM kernel and
prove that its three restrictions agree with the literal entry143
corestrictions. Only then can the endpoint cells and entry223 top be glued
and the pointed endpoint/\(Q\) mapping fiber instantiated.

## Executable evidence

Checker:
`research/voevodsky/check_dp6_rees_cech_tor_vertex_star.rs`

SHA-256:
`c62857d5bc4d47fb2c9b657866491a92f34bc6f7f777ff54d0ff02686726392b`

Fresh `rustfmt --check`, warnings-denied optimized compilation, runtime
assertions, and JSON field checks passed. Native PowerShell was used for
Rust verification because no repository-scoped structured-command MCP
capable of invoking `rustc` is exposed.

## Outcome contract

~~~json
{
  "claim": "The relative-Gm Rees overlap, shifted by its Cech degree and contracted along the conductor Tor axis, canonically supplies the missing third literal edge. The resulting six full vertex stars are integral, saturated, D3-covariant, and physically reflection closed in the finite labelled derived category.",
  "status": "proved_scoped_finite_rees_cech_tor_full_vertex_star",
  "scope": "finite labelled product-Rees/Cech/Tor and literal entry143 incidence complexes; spatial proper/log six-functor realization excluded",
  "matrix": {
    "ordered_pairs": 6,
    "edges_per_vertex": 3,
    "combined_rows": 72,
    "combined_rank": 42,
    "all_nonzero_smith_factors": 1,
    "third_edge_rows": 24,
    "third_edge_rank": 24,
    "third_edge_smith_factors": 24,
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
  "symmetry": {
    "D3_rotation_full_star": true,
    "physical_reflection_full_star": true,
    "reflection_mixes_chart_and_overlap_roles": true
  },
  "unconstructed": [
    "proper log-BM six-functor realization",
    "literal entry143 costalk/base-change comparison",
    "endpoint extensions",
    "based qSigma connector",
    "endpoint/Q mapping fiber",
    "p_partial_Q and Bockstein",
    "D8 and Jordan coherence"
  ],
  "checker": "research/voevodsky/check_dp6_rees_cech_tor_vertex_star.rs",
  "checker_sha256": "c62857d5bc4d47fb2c9b657866491a92f34bc6f7f777ff54d0ff02686726392b"
}
~~~

