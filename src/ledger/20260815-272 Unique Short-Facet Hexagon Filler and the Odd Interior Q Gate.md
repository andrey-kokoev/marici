# Unique Short-Facet Hexagon Filler and the Odd Interior Q Gate

Date: 2026-08-15  
Status: proved for the exact integral K6 cellular carrier. The independent
relative-interior map to literal \(Q\) is not constructed. No graph admission
is claimed.

## Exact filler

Order the six cross-sheet sector rays as
\[
(0,+),(1,-),(2,+),(0,-),(1,+),(2,-).
\]
Entries 266, 341--343 give the unique length-three K6 geodesic for every adjacent
pair. Their concatenation is a closed 18-edge chain, supported on 15 distinct
oriented K6 edges.

Solving its boundary equation against all nine oriented K6 facets gives a
unique integral solution of minimum \(\ell^1\)-norm six:
\[
F_{\rm hex}=F_{02}+F_{04}+F_{13}+F_{15}+F_{24}+F_{35}.
\]
These are precisely the six short facets; every coefficient is \(+1\), and
all three long-facet coefficients vanish. The solution is primitive and
torsion-free. This supplies the connected carrier and a canonical minimal
cellular contraction that entry 271 showed cannot come from two disjoint
projective triangles.

## Exact remaining obstruction

All six summands lie in \(F_B\). Therefore
\[
F_{\rm hex}\longmapsto0\quad\text{in}\quad Q=F_K/F_B.
\]
The primitive short-facet filler does not provide the missing odd generic
\(Q\) counit. Entry 270 remains decisive: the ordinary equivariant trace row
has Smith factor two, and saturation requires an independently derived odd
relative-interior column.

The next geometric datum is therefore a relative/log conductor interior
whose boundary comparison is \(F_{\rm hex}\) but whose extraordinary
restriction has primitive coefficient \(+1\) in the based literal
\(q_\Sigma\) line. It cannot be an ordinary class already lying in \(F_B\).

Until that support-changing map is constructed, the endpoint/\(Q\) mapping
fiber, \(p_{\partial,Q}\), its Bockstein, \(D_8\), and Jordan coherence remain
undefined.

## Certificate

- `research/voevodsky/check_cross_sheet_hexagon_short_facet_filler.rs`

~~~json
{
  "claim": "The six literal cross-sheet K6 corridors have a unique minimum integral filler: the primitive sum of all six short facets. Its literal Q projection is zero.",
  "status": "proved_scoped_unique_short_facet_hexagon_filler",
  "scope": "exact integral K6 cellular carrier; no extraordinary relative-interior-to-Q map",
  "matrix": {
    "corridors": 6,
    "subdivision_edges": 18,
    "distinct_boundary_edges": 15,
    "minimum_l1": 6,
    "minimum_solutions": 1,
    "short_facet_coefficients": [1, 1, 1, 1, 1, 1],
    "long_facet_coefficients": [0, 0, 0],
    "primitive": true,
    "literal_Q_projection": 0
  },
  "minimal_repair": "Construct a support-typed relative/log interior class with boundary comparison equal to the short-facet hexagon and independently normalized odd counit to the based literal qSigma line.",
  "physical_mapping_fiber": "unconstructed",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined"
}
~~~
