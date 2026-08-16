# Relative K6 Top Boundary and the Primitive Log-Interior Source Gate

Date: 2026-08-15  
Status: proved for the literal target cellular pair. A coefficient-one
normalization/log-excess source map is not constructed. No graph admission is
claimed.

## Primitive target row

Let \(B_{\rm short}\subset K_6\) be the union of the six short facets. In
outward-oriented facet bases, the unique K6 three-cell has boundary equal to
the sum of all nine facets. Passing to the relative cellular pair kills the
six short terms and leaves
\[
\bar\partial[\tau]=\ell_{14}+\ell_{03}+\ell_{25}.
\]
The row \([1,1,1]\) is primitive, with Smith form \([1]\). Rotation cycles
the three terms. Reflection reverses the ambient top orientation and hence
acts by the corresponding signed permutation; the relative generator is
reflection-odd.

Entry 272's unique hexagon filler is precisely the short-boundary part and
vanishes in this quotient. Thus the target-side primitive relative interior
is canonical.

## Source obstruction

The currently constructed full-log maximal-cone source maps its oriented
total to twice the primitive K6 sphere. Its relative long-facet row is
therefore
\[
[2,2,2],
\]
with Smith factor two. It cannot provide the coefficient-one relative
interior needed by entry 270's odd column.

The projective-conductor Gysin has an abstract primitive unit, but entries
198 and 271 show that its sheetwise pair-vertex geometry does not supply the
literal connected corridor comparison. The earliest missing arrow is a
proper support-typed map
\[
R\pi_!\operatorname{Tot}(\text{normalization/log-excess interior})
\longrightarrow C_3(K_6,B_{\rm short})
\]
whose relative degree is one and whose boundary restricts to the constructed
hexagon and three long-facet packets.

Until that arrow exists, the endpoint/\(Q\) mapping fiber and its physical
parity remain undefined.

## Certificate

- `research/voevodsky/check_relative_k6_top_long_q_boundary.rs`

~~~json
{
  "claim": "The literal relative K6 top has primitive reflection-odd long-facet boundary [1,1,1], while the existing full-log maximal-cone source reaches it only with coefficient two.",
  "status": "proved_scoped_relative_K6_top_target_with_source_degree_two_gate",
  "scope": "literal target cellular pair and already-certified source degree; no new proper log-interior comparison",
  "matrix": {
    "absolute_facets": 9,
    "short_facets_quotiented": 6,
    "relative_long_boundary": [1,1,1],
    "relative_snf": [1],
    "existing_source_boundary": [2,2,2],
    "existing_source_snf": [2]
  },
  "minimal_repair": "Construct a proper support-typed normalization/log-excess relative interior of degree one into C3(K6,B_short), compatible with the literal hexagon, long-facet packets, and endpoint framing.",
  "physical_mapping_fiber": "unconstructed",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined"
}
~~~
