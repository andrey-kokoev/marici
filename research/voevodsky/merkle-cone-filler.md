# Iteration 4: an explicit Merkle cone filler

## Chosen filler type

`thin-affine-Q-cone-v1` is an explicitly supplied simplicial cone over a verified, consistently oriented sphere boundary, together with invertible affine rational transport on all its edges. Its boundary restriction retains the original polygon-surface root and a face-by-face fan triangulation. Its three-dimensional cells are oriented tetrahedra.

This is a filler in a deliberately thin semantic model: equal affine maps have only the equality obligation checked by exact coefficients. It is not a construction of equality between arbitrary proof terms or dependent higher witnesses. The original boundary witness records remain bound by the surface root, but the filler does not compare their proof histories.

## Construction and verification

1. Verify closed connected orientable genus-zero topology, consistent supplied orientation, valid face identities and globally trivial transport.
2. Triangulate each polygon by a fan, retaining which original face each triangle subdivides.
3. Add a fresh interior apex and one tetrahedron for every boundary triangle.
4. Construct tree potentials P[v] on the boundary and give the apex identity potential. Assign every edge u -> v the exact map P[v] composed with inverse(P[u]).
5. Independently verify every simplex hash, incidence, original boundary edge restriction, and triangle composite.
6. Compute the oriented tetrahedral boundary: interior triangles must occur twice with opposite signs; exterior triangles must reproduce the original face subdivision exactly.

The construction is specifically a cone over a sphere, so the standard cone(S^2) = 3-ball theorem supplies its ball topology. Euler characteristic one is an additional check, not a sufficient standalone ball-recognition criterion. A flat torus is deliberately rejected: its cone has a singular apex, not the required ball interior.

## Cube result

| Cell dimension | Count |
| --- | ---: |
| Vertices, including apex | 9 |
| Edges | 26 |
| Triangles | 30 |
| Tetrahedra | 12 |

The 30 triangles comprise 12 boundary triangles and 18 interior triangles. Interior contributions cancel in the oriented boundary chain. All transport identities hold exactly; restriction recovers the original cube's 12 edge maps and six face attachments. The sphere discovered from separated faces in iteration 3 also receives a verified cone filler after replaying its gluing certificate.

## Tests and limits

All 22 checks passed. The verifier rejects an unfilled surface presented as a filler, a missing tetrahedron, incorrect tetrahedral orientation, rehashed wrong transport, missing edge, wrong edge type, rebound boundary root, hash tampering and lost face restriction. Open surfaces, inconsistent supplied orientations and both trivial/nontrivial-transport tori are refused by this constructor. Serialization and fresh CLI verification pass.

Refusal of a torus by this cone-to-ball constructor is not a theorem that it cannot bound another three-manifold. Nor does a successful cone imply a canonical or minimal filling. Other fillings, comparison of fillings, non-thin proof coherence and genuinely dependent witness transport remain open.

## Reproduce

```text
python research/voevodsky/checkers/check_merkle_cone_filler.py
python research/voevodsky/checkers/merkle_cone_filler.py research/voevodsky/results/merkle_cube_cone_filler.json
```

Construct a new filler from an eligible surface store:

```text
python research/voevodsky/checkers/merkle_cone_filler.py SURFACE.json --construct FILLER.json
```

Artifacts:

- `research/voevodsky/checkers/merkle_cone_filler.py`: constructor and independent verifier.
- `research/voevodsky/checkers/check_merkle_cone_filler.py`: tests and negative controls.
- `research/voevodsky/results/merkle_cone_filler.json`: receipt and code fingerprints.
- `research/voevodsky/results/merkle_cube_cone_filler.json`: explicit cube-boundary filler.
- `research/voevodsky/results/merkle_discovered_cone_filler.json`: filler of the independently discovered sphere.
