# Iteration 3: discover gluing from separately witnessed faces

## Input and search

The new `merkle_gluing_search.py` accepts a Merkle packet of separate polygon faces. Each face has local corner positions, Q port types, an ordered cycle of invertible affine rational maps, and a polynomial-kernel proof of its boundary identity. There are no vertex names shared between faces, supplied edge pairings, or global adjacency.

Candidate boundary ports must lie on different faces and carry inverse affine maps. Only orientation-reversing pairings are searched. Endpoints are then identified in reverse order by union-find. The resulting quotient must be a connected, simple-edge regular polygon surface, with distinct corners on every face, circular vertex links, and valid attached identities. The existing surface verifier checks the result independently.

Search chooses the remaining port with the fewest compatible partners and enumerates perfect matchings under an explicit node budget. It does not solve arbitrary symbolic map equivalence or permit coordinate changes while matching; labels must agree exactly as rational affine maps. Local proofs are verified before search. Unsupported or false input is invalid, not evidence of impossible gluing.

## What was found

For six separated cube faces, the search reconstructs an 8-vertex, 12-edge, 6-face sphere in 13 search nodes. The labels deliberately come from distinct vertex-potential differences, making each reversed edge label unique. Original endpoint IDs and potentials are omitted from the input. This is a constrained positive fixture, not evidence that arbitrary ambiguous gluing is easy.

The source face proof roots remain retained. A hashed gluing certificate binds the source packet, complete port pairing and discovered surface root. Verification independently rebuilds the quotient and checks its exact root and topology. Corner identification therefore cannot silently replace local witnesses with unrelated equalities.

## Result semantics

| Status | Meaning |
| --- | --- |
| `unique_labelled_gluing` | Exactly one accepted labelled pairing after exhaustive search within the declared grammar |
| `ambiguous` | At least two distinct labelled pairings verified; search may stop once ambiguity is established |
| `no_gluing_in_supported_grammar` | Exhaustive search found none within the restricted grammar |
| `search_limit` | Budget exhausted; no impossibility or uniqueness claim, even if one candidate was found |
| CLI `invalid_input` | Hash, schema, type, proof or input validation failed |

Uniqueness is about labelled local port pairings, not homeomorphism or unlabelled isomorphism classes. Two identical identity-labelled squares yield multiple valid sphere gluings differing in port attachment. Removing one cube face exposes four ports with no compatible partner. A one-node budget returns `search_limit`, not a false impossibility claim.

## Verification

All 20 new checks passed. Controls cover unique discovery, 24 ports paired once, face reordering and corner rotation, missing faces, prohibited self-pairing, ambiguity with independently valid alternatives, budget exhaustion, false local identities, tampered source hashes, rehashed source substitution, reused ports, incompatible map pairings, serialized certificate replay and fresh CLI discovery.

The search currently excludes self-pairings, nonorientable identifications, parallel quotient edges, singular attaching maps and disconnected results. An exhaustive negative result is qualified by those restrictions. No higher filler is generated.

## Reproduce

```text
python research/voevodsky/checkers/check_merkle_gluing_search.py
python research/voevodsky/checkers/merkle_gluing_search.py research/voevodsky/results/merkle_unglued_cube_faces.json --output research/voevodsky/results/merkle_discovered_cube.json
```

The Python API `face_packet(faces)` accepts each face as a list of directed `[a,b]` coefficients for x -> ax+b and builds the local polynomial proof stores. `search(packet, max_nodes=10000)` returns diagnostics and candidate artifacts. `verify_certificate(packet, certificate, surface)` independently checks a candidate.

Artifacts:

- `research/voevodsky/results/merkle_unglued_cube_faces.json`: separately witnessed faces, no global incidence.
- `research/voevodsky/results/merkle_discovered_cube.json`: search result, surface store and replayable gluing certificate.
- `research/voevodsky/results/merkle_ambiguous_gluing.json`: ambiguous square fixture and two valid attachments.
- `research/voevodsky/results/merkle_gluing_search.json`: checks and code fingerprints.

The next unresolved architectural step is an explicit higher-filler type and boundary restriction rule. A discovered closed surface still does not itself supply that higher witness.
