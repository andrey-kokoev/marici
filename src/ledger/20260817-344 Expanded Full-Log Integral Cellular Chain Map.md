# Expanded Full-Log Integral Cellular Chain Map

## Record

Date: 2026-08-17

Status: proved finite integral cellular realization of the minimally expanded
full-log octahedral source in the literal K6 associahedral sphere. This is a
chain-level carrier theorem. It does not construct the support-typed
proper/extraordinary six-functor correspondence.

## Expanded source

Start with the oriented octahedral complex

[
C_2=mathbf Z^8,qquad C_1=mathbf Z^{12},qquad C_0=mathbf Z^6.
]

The six opposite-sign (mixed) edges are replaced by their independently
enumerated unique three-segment K6 galleries. The six equal-sign edges remain
single source edges; their images are the independently computed two-edge K6
chains. Thus the expanded source has

[
C_2^{mathrm{exp}}=mathbf Z^8,qquad
C_1^{mathrm{exp}}=mathbf Z^{24},qquad
C_0^{mathrm{exp}}=mathbf Z^{18}.
]

The checker constructs the source incidence without importing target signs,
verifies (d_1d_2=0), and computes ranks 17 and 7. Peeling unit pivots after
deleting one top cell certifies seven unit Smith factors for (d_2).

## Literal target and chain map

The literal K6 target is independently enumerated as the 14 triangulations,
21 flips, and nine associahedral facets. The map (Gamma_0) sends each
source occurrence vertex to its labelled triangulation. The map (Gamma_1)
is obtained from the unique shortest paths, with orientations fixed by the
lexicographic target-edge basis rather than chosen to solve the top equation.

For each of the eight source top cells, the checker independently computes
(Gamma_1d_2). The two equal-sign boundaries have zero filler. Each of the
six mixed boundaries has the previously certified unique norm-three filler.
Putting these columns together defines (Gamma_2), and every entry of

[
d_2^{K6}Gamma_2=Gamma_1d_2^{mathrm{exp}}
]

is checked integrally.

The target top boundary has rank eight and eight unit Smith factors. Its
primitive kernel is the oriented K6 sphere. Consequently each of the eight
filler columns can be shifted independently by that sphere, so the complete
homogeneous solution module is

[
operatorname{Hom}igl(C_2^{mathrm{exp}},ker d_2^{K6}igr)
cong mathbf Z^8.
]

The canonical minimum-support choice has two zero columns and six three-facet
columns. Its coherently oriented sum has absolute degree two.

## Exact scope boundary

This closes the finite expanded maximal-cone comparison gate. It reuses, and
does not re-prove, the already certified Boolean/Tor/Cech facet lift.

It does not promote the cellular map to a normalization-provenanced
proper/log-excess kernel. In particular, literal corestriction squares,
endpoint framing, the based qSigma map, and the pointed endpoint/Q mapping
fiber remain uninstantiated. Physical p, its Bockstein, D8, and Jordan
coherence therefore remain undefined.

## Executable evidence

Checker:
`research/voevodsky/check_expanded_full_log_cellular_chain_map.rs`

SHA-256:
`e01f7faf04cd7b9e3cbb36b18a59fc5aa09069472d7776f25a45d1f42a550f69`

Fresh `rustfmt --edition 2021 --check`, warnings-denied optimized compilation,
runtime assertions, and JSON emission passed.

~~~json
{
  "status": "proved_expanded_full_log_integral_cellular_chain_map",
  "source_chain_ranks": [8, 24, 18],
  "source_d1_rank": 17,
  "source_d2_rank": 7,
  "source_d2_smith_unit_factors": 7,
  "target_chain_ranks": [9, 21, 14],
  "target_d2_rank": 8,
  "target_d2_smith_unit_factors": 8,
  "chain_equation": true,
  "same_sheet_zero_fillers": 2,
  "mixed_fillers": 6,
  "minimal_facets_per_mixed_filler": 3,
  "gamma2_homogeneous_module": "Z^8",
  "oriented_cellular_degree_abs": 2,
  "finite_chain_realization": true,
  "proper_extraordinary_kernel_constructed": false,
  "mapping_fiber_instantiated": false,
  "graph_admission_claimed": false
}
~~~
