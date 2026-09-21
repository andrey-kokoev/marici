# Canonical rejoin naturality: an explicit attachment-cube proof

## Result

For f:A->B, g:B->C, and h:C->D, the model now constructs and proves the commuting square whose horizontal maps are the explicit rejoin equivalences (C/A)/(B/A) -> C/B and (D/A)/(B/A) -> D/B, and whose vertical maps are induced by h.

The theorem `Naturality.rejoinSquare` compares transport-then-rejoin with rejoin-then-transport on the entire double cofiber. `Naturality.cutSquare` proves the corresponding square for the inverse maps.

Implemented in `agda/ClosureCanonicalRejoin.agda`, with regressions in `agda/ClosureCanonicalRejoinRegression.agda`.

## Why an explicit implementation

The earlier 3-by-3 proof gives a cofiber equivalence by composing several transported equivalences. Its naturality is not exposed by constructor equations. Instead of assuming that naturality, this increment independently constructs the rejoin equivalence by higher-inductive elimination.

The forward map is defined on points, inner attachments, outer attachments, and nested attachment squares. On a nested square indexed by a:A and interval coordinates u,v, it gives the target attachment at u meet v.

The inverse sends a target point to its doubly included source point and each B-attachment to the corresponding outer attachment. One round trip is constructorwise reflexivity. The other requires an explicit three-dimensional filler `attachmentCube`, built with Cubical homogeneous composition and checked on all faces.

This is the actual extra coherence in the proof: the double attachment has to deform compatibly with the inverse map. No equality of point values substitutes for the cube.

## Parallel maps and common boundary

Let P:B/A->C/A, Q:C/A->D/A, R:B/A->D/A be the normalized cofiber transports.

The new `upper` map is defined directly from cofib(P) to cofib(R), acting on the complete higher-inductive structure. Its codomain attachment paths match by the constructor behavior of QP and R; no anonymous comparison is an input.

The two functions are:

- `transportThenRejoin`: upper followed by the explicit rejoin for f and hg;
- `rejoinThenTransport`: explicit rejoin for f and g followed by fixed-source transport for g and h.

Both have source cofib(P) and target cofib(hg). Their equality is proved on every constructor, including the nested attachment square. The proof is reflexivity there because the independently given formulas reduce to the same expression. This is not an identification created by defining one composite to be the other.

## Relationship with the previous open type

This proves naturality for the new explicit equivalence, with independently checked inverse homotopies. It does not claim the new forward map has already been identified with the previous `normalizedCofiberComposition` obtained via 3-by-3 and univalence transport.

Consequently the older type `ClosureCofiberTransportCoherence.RejoinNaturality.RejoinSquare` for those particular opaque maps remains without an inhabitant in that module. The new theorem supplies the intended model-level natural rejoin using a concrete choice. Comparing the two chosen implementations is a separate implementation-comparison theorem, not an analytical obstruction.

No existing module was modified to silently change that earlier statement.

## Tests

The circle regression uses empty A, two-point B, and one-point C. The new explicit quotient equivalence identifies the iterated cofiber with the circle, not with a set quotient.

The naturality regression instead uses nonempty A=Bool, B=Unit, C=D=Bool, with g selecting false and h negating Bool. This exercises both a nonidentity target map and nonempty nested attachments. The code checks the full forward and inverse square families, and explicitly requests the inverse law on the two-dimensional attachment.

## Verification

Fresh dependency-closure command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureCanonicalRejoinRegression.agda`

Agda 2.8.0.1 / Cubical 0.9, exit 0. Both added modules use `--safe --cubical --guardedness`. No holes, postulates, or assumed rejoin-naturality witnesses were added. The initial incremental run found the module import needed `using (module Transport)` rather than `using (Transport)`; the corrected build and fresh closure check passed.

## Next level

The next comparison is between assemblies of these naturality squares, with their inverse/attachment coherence. The present proof supplies a specific square to compare. It does not yet claim the full pentagon for all filtration decompositions, an infinite closure tower, or an analytical realization functor.
