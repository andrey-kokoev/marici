# Merkle identity surface: the cube boundary

## Test

Six identity-labelled squares are supplied with explicit directed boundary attachments. The question is whether these data form a closed surface and whether the attached algebraic identities actually hold. This is a supplied gluing, not a search for a gluing from arbitrary equations.

Every vertex carries type Q. An edge carries an invertible affine rational map x -> ax+b; reversing an edge uses its exact inverse. Each face witnesses that its directed boundary composite is the identity. Equivalently, its two routes between opposite vertices agree. Rational coefficient comparison checks equality for every rational input, not merely sample values.

The fixture assigns each binary vertex v a chart g_v(x)=2^(sum(v))*x+(v_0+2v_1+3v_2), and defines each edge u -> v by g_v composed with inverse(g_u). This deliberately constructs a positive control; the checker is not given these charts and independently checks the edge labels and faces. It does not discover the identities automatically.

## Merkle representation

Domain-separated SHA-256 addresses immutable vertices, edges, face-boundary witnesses, faces, and the whole surface. References bind ordered endpoints and signed boundary occurrences. A shared edge is one object used by two faces, not two unrelated copies. The surface retains face occurrences even when their content hashes coincide.

The verifier checks each reachable reference against its hash, the exact record shape, endpoint types, invertibility, closed simple polygon boundaries, and witness attachment. Witness records name an executable verification rule; their claims are recomputed rather than trusted.

## Topology and algebra are separate

For this finite regular polygon-complex grammar, closure requires every edge to have two distinct incident face occurrences and every vertex link to be a single circle. The checker also reports connectedness, orientability, consistency of the supplied face orientations, Euler characteristic and (for connected orientable closed surfaces) genus.

The cube has 8 vertices, 12 edges and 6 faces: Euler characteristic 2, genus 0, no boundary edges, and circular links at all vertices. Every face identity holds. All six monotone paths from vertex 000 to vertex 111 independently compose to x -> 8x+6.

Here `coherent_closed_surface` means a closed surface with well-typed, correctly attached, valid face identities. On general positive-genus surfaces, local face flatness does not establish trivial holonomy around noncontractible loops. The iteration-one extension now independently reports `globally_path_independent`: spanning-forest transports and every non-tree edge test all graph walks in the supported affine language. Explicit signed cycle witnesses accompany the result. The cube passes this stronger test; the flat torus in `merkle-torus-holonomy.md` does not. Add `--require-path-independence` to `--verify FILE` to require this stronger property rather than local coherence alone.

## Negative controls

| Mutation | Outcome |
| --- | --- |
| Remove one face | Four unmatched boundary edges; not closed |
| Add a duplicate face occurrence | Four edges with three incident faces; not a surface |
| Join two spheres at one vertex | Every edge still has two faces, but the shared vertex link is disconnected; not a surface |
| Change one edge map and honestly rehash | Topology remains a sphere; two face identities fail |
| Reverse one face orientation | Still an orientable sphere; supplied orientation is inconsistent |
| Substitute an incompatible port type | Topology unchanged; typed coherence fails |
| Alter an object without rehashing | Integrity failure |
| Delete a witness object | Missing-reference failure |

All 14 checks passed, including JSON serialization and reverification. No algebraic three-dimensional filler is supplied or inferred. A topological sphere may bound a ball; that fact is distinct from constructing a higher witness for these labelled identities.

## Reproduce and feed another fixture

Generate the cube and controls:

`python research/voevodsky/checkers/check_merkle_identity_surface.py`

Independently verify a serialized store:

`python research/voevodsky/checkers/check_merkle_identity_surface.py --verify research/voevodsky/results/merkle_identity_surface_store.json`

For new inputs, the importable `encode(model)` accepts vertex declarations, directed affine edge maps, and polygon cycles; `verify(artifact)` returns the separate topology and algebra diagnostics. The current encoder names edges by lexicographically ordered endpoint names (`u>v`) and expects maps in that direction. This restricts the encoder to one edge per endpoint pair; the lower-level verifier uses explicit edge hashes. This prototype is not an arbitrary symbolic identity parser, arbitrary CW-complex checker, or general theorem prover.

Artifacts:

- `research/voevodsky/checkers/check_merkle_identity_surface.py`
- `research/voevodsky/results/merkle_identity_surface.json`
- `research/voevodsky/results/merkle_identity_surface_store.json`
