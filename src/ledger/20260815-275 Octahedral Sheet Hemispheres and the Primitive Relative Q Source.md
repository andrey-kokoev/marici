# Octahedral Sheet Hemispheres and the Primitive Relative Q Source

Date: 2026-08-15  
Status: proved in the exact normalization-labelled log-link/K6 cellular model.
Literal six-functor Beck--Chevalley realization remains open. This corrects
entry 274. No graph admission is claimed.

The cross-sheet hexagon separates the octahedral log link into two labelled
four-cone disks. Each contains one pure cone with zero carrier and three mixed
cones with entry 266's unique fillers. Their exact images satisfy
\[
H_+=F_{\rm sph}-F_{\rm hex},\qquad
H_-=F_{\rm sph}+F_{\rm hex}.
\]
Hence their sum is \(2F_{\rm sph}\), explaining the old degree-two total,
while their difference is \(2F_{\rm hex}\). Modulo \(F_B\), the hexagon
vanishes and each sheet maps to the same primitive long-facet row
\([-1,1,1]\), with Smith form \([1]\).

Thus the coefficient-one source is derived, not adjoined. The remaining gate
is categorical: promote both hemispheres and the common equatorial Rees/KN
boundary to the literal entry143 BM--Cech diagram, prove endpoint/reflection
compatibility, and identify the primitive row with based \(q_\Sigma\).

## Certificate

- `research/voevodsky/check_octahedral_sheet_hemisphere_primitive_q.rs`

~~~json
{
  "claim": "Each normalization-labelled octahedral hemisphere maps with primitive coefficient one to the relative long-facet Q row; their sum is the degree-two full-log class and their difference is twice the short hexagon.",
  "status": "proved_scoped_octahedral_sheet_hemisphere_primitive_Q",
  "scope": "exact labelled log-link and K6 cellular matrices; literal six-functor BC and endpoint framing excluded",
  "matrix": {
    "hemisphere_faces": 4,
    "mixed_fillers_per_hemisphere": 3,
    "relative_long_row": [-1,1,1],
    "relative_snf": [1],
    "sheetwise_Q_coefficient": 1,
    "full_total_coefficient": 2
  },
  "supersedes": "entry 274 image-lattice 2Z conclusion",
  "minimal_repair": "Construct the proper support-typed six-functor BC realization of both sheet hemispheres, their common Rees/KN hexagon, endpoint restrictions, and based qSigma comparison.",
  "physical_mapping_fiber": "unconstructed",
  "physical_p_partial_Q": "undefined",
  "physical_Bockstein": "undefined"
}
~~~
