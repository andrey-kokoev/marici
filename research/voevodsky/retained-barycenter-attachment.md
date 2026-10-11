# Retained barycenter attachment: explicit cells and root neighborhood

## Built object

Take a barycentrically subdivided tetrahedral host P and a separate, equally sized tetrahedron E. Each has 24 maximal flag tetrahedra. Identify E's body barycenter with the host's face-center vertex F_ABC. Keep every other cell and vertex separately labelled.

The electron flags are ordered body → face → edge → vertex. No vertex moves during construction and no inward growth is added to the host. The host subdivision is a fixed geometric carrier, not an animation or a new coefficient network.

This operation is the simplicial **pushout of two marked-vertex inclusions**. It is not a pullback. A pullback realization would require additional maps and a common target; those cannot be supplied by merely calling this identification a pullback.

The complete source proton coefficient packet is reverified and referenced unchanged. This new artifact constructs the cell attachment; it does not claim to implement a spatial pullback of all source coefficient ports.

## Complete retained inventory

| Object | Vertices | Edges | Triangles | Tetrahedra |
|---|---:|---:|---:|---:|
| Host | 15 | 50 | 60 | 24 |
| Electron | 15 | 50 | 60 | 24 |
| Attached complex | 29 | 100 | 120 | 48 |

Both cell inclusions are injective. Their intersection is exactly the identified root vertex. The union is closed under taking faces. All internal triangular faces have two tetrahedral owners; the oriented top chain has precisely the two outer surfaces as its boundary, with no remaining boundary edges.

The joined rational homology is (1,0,0,0). No additional cells are required for these closure properties. This does not mean the object is a boundaryless three-manifold: its outer boundary remains present.

## What is retained at the root?

Inspect the link, the complex of directions immediately around the root:

- On the host side it is a triangulated disk: 7 vertices, 12 edges, 6 triangles.
- On the electron side it is the entire direction sphere: 14 vertices, 36 edges, 24 triangles.
- In the attachment it is their disjoint union.

The joined link has two connected components and rational Betti numbers (2,0,1). The root is therefore a nonmanifold junction, not an ordinary point of a single solid tetrahedral body. Both direction complexes remain retained rather than collapsed together.

This is an explicit feature of the point attachment, not a missing cell discovered by the boundary calculation. Requiring an ordinary manifold neighborhood would be an additional condition. There is no justification here for naming a repair “neutron.”

## Why a literal overlapping-solid rendering is misleading

Translate an ordinary spatial copy of E so its barycenter is F_ABC. Because a barycenter is an interior point of E, E contains a small ball around the attachment. That ball intersects the host interior. The two solids cannot meet only at the identified point in this ordinary three-dimensional realization.

For the displayed alignment, the checker supplies the point (3/10,3/10,-3/10). Its host barycentric coordinates are (13/40,13/40,13/40,1/40); its electron coordinates are (29/120,29/120,29/120,11/40). Both are strictly positive.

Thus the supplied coordinates are a noninjective display projection, not an embedding of the abstract attachment. A visualization should expose the retained electron direction space separately, or explicitly distinguish the overlapping labelled copies. It should not silently identify their projected overlap or shrink the electron to hide it.

## Outcome

The retained cell attachment exists and closes without an extra complex. Its nontrivial feature is the root's retained disk-plus-sphere direction structure. It does not yield two isotope closures.

The next specification is which additional incidence or realization relations, if any, couple these retained directions beyond sharing the root. Phase registration alone does not provide those relations. They must be supplied before an additional geometric carrier can be tested as indispensable.

## Artifacts

```text
python research/voevodsky/checkers/check_retained_barycenter_attachment.py
```

Sixteen exact checks pass. `results/retained_barycenter_attachment_store.json` contains the full cell inventory, both inclusions via labels, outward electron flags, marked attachment, and display coordinates. `results/retained_barycenter_attachment.json` contains exact rational boundary ranks, homology, root links, overlap witness, and source/checker hashes.
