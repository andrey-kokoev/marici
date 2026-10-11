# Iteration 1: local identities versus global Merkle transport

## Result

The existing surface verifier now separately decides global path independence for its exact invertible affine rational edge language. A 3-by-3 periodic square mesh has 9 vertices, 18 edges and 9 faces. It is a connected orientable closed genus-one surface with Euler characteristic zero. Every face identity is valid, but its horizontal loop acts by x -> x+3 and its vertical loop by x -> x+6. Thus local coherence and closed topology do not imply trivial global holonomy.

The fixture gives each positive horizontal edge translation +1 and each positive vertical edge translation +2. Opposite traversals use exact inverses. Translations commute, so square boundaries and the torus commutator evaluate to the identity. The two generating loops are nevertheless nontrivial.

## Complete criterion in the supported language

Choose a spanning forest. Let P[v] be the composite along its unique path from the component base to v. For every edge E:u->v, path independence requires E = P[v] composed with inverse(P[u]). The discrepancy inverse(P[v]) composed with E composed with P[u] is a based-loop witness.

Tree edges satisfy this by construction. Checking all non-tree edges is sufficient: when every discrepancy is identity, arbitrary path composites telescope to P[target] composed with inverse(P[source]). Conversely, any nonidentity discrepancy supplies two conflicting paths. This checks all finite graph walks, not just a bounded sample or the named torus generators.

The report retains the explicit signed edge path and affine coefficients for every fundamental graph cycle. The torus has cycle rank E-V+1=10; the cube has rank 5. These are graph cycle bases, not a minimal presentation of the surface fundamental group. Valid face relations may identify graph cycles; no such minimization is needed to decide whether all their transports are trivial.

All references originate in the hash-verified surface. The experiment independently replays every reported loop to verify continuity, closure, membership and its computed map. The diagnostic report is not a standalone trusted proof: replay or rerun the verifier against its recorded surface root.

## Tests

All 19 new checks pass, and all 14 original surface checks still pass.

- Flat torus: valid face identities, genus one, but global path independence false.
- Named loops: translations +3 and +6; reversed horizontal loop translates -3.
- Trivial torus: both local and global checks pass.
- Cube: all fundamental graph cycles are trivial, strengthening the prior six-route comparison.
- Noncommuting scale and translation labels: topology stays closed, local and global checks fail.
- Nonconstant vertex frame changes: flatness and nontriviality survive conjugation.
- Pure frame changes of trivial transport: individual edges can be nonidentity while all loops remain trivial.
- 4-by-4 periodic mesh: the same local/global distinction survives refinement of the fixture size.
- Serialized-store replay and CLI policy separation: ordinary verification accepts the flat torus; explicitly requiring global path independence rejects it with exit code 1.

Global nontriviality is not inherently an error. A flat connection may legitimately represent nontrivial loop transport. The caller chooses whether local coherence or global path independence is required. Neither decision constructs a higher-dimensional filler.

## Reproduction

```text
python research/voevodsky/checkers/check_merkle_torus_holonomy.py
python research/voevodsky/checkers/check_merkle_identity_surface.py
python research/voevodsky/checkers/check_merkle_identity_surface.py --verify research/voevodsky/results/merkle_torus_store.json
python research/voevodsky/checkers/check_merkle_identity_surface.py --verify research/voevodsky/results/merkle_torus_store.json --require-path-independence
```

The last command intentionally exits 1. Results: `research/voevodsky/results/merkle_torus_holonomy.json`; serialized surface: `research/voevodsky/results/merkle_torus_store.json`.

## Remaining scope

General expression/proof input, gluing discovery, higher fillers, general dependent witness transport and engineering work remain open. This iteration discharges the concrete torus/global-holonomy test and supplies a reusable all-walk criterion only for the present affine rational language. It does not infer a topology from equations or add a general symbolic theorem prover.
