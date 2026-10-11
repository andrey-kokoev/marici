# Spatial realization of the three-arrow receiver

[Open the Three.js page](../../papers/witness-generators/three-arrow-receiver.html).

## Fixed geometric rule

Keep the proton tetrahedron ABCD and its twelve directed primitive arrows. The new receiver has only A→e, B→e, C→e. Give those three spatial edges the same length as the existing regular tetrahedron edges, and choose e on the opposite side of ABC from D.

Equal distances to A,B,C place e on the normal line through the face center F. The common edge-length equation has exactly two solutions: D and its reflection across ABC. The outward condition selects the latter:

```text
F = (A+B+C)/3,
e = 2F-D.
```

This metric rule is additional to the three-channel compatibility equations: the latter specify signal matching, not spatial lengths.

With the existing coordinates:

```text
A=(1,1,1), B=(1,-1,-1), C=(-1,1,-1), D=(-1,-1,1),
F=(1/3,1/3,-1/3),
e=(5/3,5/3,-5/3).
```

Both tetrahedra have edge length squared 8 and volume 8/3. They share face ABC and lie on opposite sides of its plane. Their shared face cancels in the consistently oriented boundary, leaving six outer triangles.

## Centers last

Only after constructing the two tetrahedra derive

```text
bP=(A+B+C+D)/4=(0,0,0),
bQ=(A+B+C+e)/4=(2/3,2/3,-2/3).
```

Their midpoint is F. The connecting segment is perpendicular to ABC and has squared length 4/3. It is a derived representation of the pair, not a sixteenth primitive arrow.

The receiver apex e and barycenter bQ are distinct. The construction does not silently equate them. The tetrahedral silhouette on the receiver side also does not imply a second complete directed graph: its four vertices have only nine inherited/new primitive arrows, not twelve.

## Visualization

- **Primitive arrows:** twelve blue proton arrows and three gold arrows entering e.
- **Centers last:** derived barycenters bP,bQ and their segment.
- Hide the frames and shared face to view only that segment.
- The receiver-value control demonstrates the same three incoming phase maps for z=1,ω,ω². Changing signal values does not change the geometry.

The two existing tetrahedra are never shrunk, their centers are never identified, and no belt is introduced.

## Verification

```text
python research/voevodsky/checkers/check_three_arrow_receiver_geometry.py
node research/voevodsky/checkers/check_three_arrow_receiver_page.mjs
```

Twelve exact geometry/graph checks and fourteen browser/math checks pass. Artifacts include `results/three_arrow_receiver_geometry.json`, `results/three_arrow_receiver_page_check.json`, and screenshots for primitive, center, segment-only, and mobile views.
