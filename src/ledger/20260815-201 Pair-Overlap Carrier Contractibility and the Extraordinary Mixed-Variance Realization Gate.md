# Pair-Overlap Carrier Contractibility and the Extraordinary Mixed-Variance Realization Gate

Date: 2026-08-15  
Status: proved at the integral homotopy-coherent carrier level.  
The extraordinary mixed-variance realization into entry143 remains unconstructed.
No graph admission is claimed.

## Result

Entry200 proves that an ordinary facewise pair-intersection map cannot exist:
each physical dP6 cone is labelled by a crossing pair of short diagonals and
therefore has no literal entry143 face. That obstruction does not imply that
the carrier homotopy required by a future extraordinary correspondence is
ambiguous.

Let

\[
d_2:C_2(B_{\rm short})\longrightarrow C_1(B_{\rm short})
\]

be the boundary restricted to the six short facets of the labelled
associahedron. Reconstructing all K6 faces gives the census

\[
(1,9,21,14).
\]

The exact integral matrix of \(d_2\) has rank six and a unit maximal minor.
Consequently its Smith form is

\[
\boxed{\operatorname{SNF}(d_2)=(1,1,1,1,1,1)}.
\]

Thus \(d_2\) is a saturated injection. Once an extraordinary pair object
has supplied a fixed relative road class, any two strict carrier
representatives differ by a unique integral short-facet 2-chain. There are
no carrier 2-automorphisms and no integer torsion. The formerly visible
rank-six family is therefore contractible in the homotopy-coherent carrier
category; it is not a residual choice of correspondence.

For the equivariant dP6 ray labelling \((2,3,4,5,0,1)\), every cone residue
is the primitive difference of its two legitimate short-facet chains. The
six residues telescope to zero. Hence the cyclic triple-coherence equation
has no further carrier obstruction once the six support-switch objects and
their boundary restrictions exist.

## Exact scope

This theorem does not construct a map

\[
\Gamma_{ij}^{!,\log}\longrightarrow C_\bullet(q_k)\subset F_B/F_V.
\]

The three pair objects remain external to entry143's face category because
the long-road pairs cross. Tensoring the split carrier injection with an
external spectator complex preserves injectivity, but that formal operation
does not derive the support-changing occurrence, Tor, normal-circle, or
Čech maps.

The first missing geometric datum is still a branch-selected extraordinary
pair object with:

1. log residues to both adjacent long-facet packets;
2. a support-switch comparison to the complementary marked corridor;
3. the four Boolean normal states and both Tor grades;
4. Beck--Chevalley compatibility at the endpoints and under reflection and
   \(D_3\).

The new theorem sharpens the gate: after those restrictions are derived, the
carrier comparison homotopies and cyclic filler are forced integrally. The
remaining obstruction is geometric realization, not carrier rank, torsion,
or homotopy ambiguity.

Because that realization remains absent, the endpoint/Q mapping fiber is
not instantiated and \(p_{\partial,Q}\), its Bockstein, \(D_8\), and Jordan
coherence remain undefined.

## Certificate

- `research/voevodsky/check_p2_pair_overlap_homotopy_contractibility.rs`
- SHA-256:
  `877c9f66dc560498d9eae293800cc4f78ab27353e8d4f49a8e3a38ab13163127`

Validation after explicit MSVC environment initialization:

- `rustfmt --edition 2021 --check`: pass;
- `rustc --edition=2021 -D warnings -O`: pass;
- linked executable: exit zero;
- emitted JSON: parsed with the expected status and Smith form;
- temporary executable: removed and confirmed absent.

## Outcome contract

~~~json
{
  "claim": "For the actual labelled K6 short boundary, the six short-facet boundary columns form a saturated injection with Smith form [1,1,1,1,1,1]. Therefore strict representatives of a fixed pair-overlap road class have unique integral comparison 2-chains and no 2-automorphisms; the six primitive dP6 residues telescope to zero.",
  "status": "proved_scoped_carrier_homotopy_contractibility",
  "scope": "integral K6 carrier and external spectator tensor only; no mixed-variance six-functor realization, literal support-changing Tor/Cech rows, endpoint/Q mapping fiber, or graph admission",
  "evidence": {
    "k6_faces": [1, 9, 21, 14],
    "short_boundary_d2_rank": 6,
    "short_boundary_d2_kernel_rank": 0,
    "short_boundary_d2_smith": [1, 1, 1, 1, 1, 1],
    "unit_maximal_minor": true,
    "integer_torsion": "none",
    "dp6_cone_residue_rows": 6,
    "dp6_cyclic_residue_sum": 0,
    "external_spectator_tensor_preserves_split_injection": true,
    "pair_objects_external_to_literal_face_category": 3,
    "support_changing_tor_cech_comparison": "unconstructed",
    "literal_mixed_variance_realization": "unconstructed",
    "physical_mapping_fiber": "unconstructed",
    "physical_p_partial_Q": "undefined",
    "physical_bockstein": "undefined",
    "D8_and_Jordan": "untested"
  },
  "checker_sha256": "877c9f66dc560498d9eae293800cc4f78ab27353e8d4f49a8e3a38ab13163127",
  "minimal_additional_geometry": "Construct one branch-selected extraordinary seed correspondence with derived log residues and literal support-changing Boolean/Tor/Cech rows; D3 rotation then supplies the other two, and the carrier comparison homotopies are uniquely forced by the saturated injection."
}
~~~
