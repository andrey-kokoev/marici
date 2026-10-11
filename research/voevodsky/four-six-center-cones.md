# Four proton pieces versus six pieces of the displayed connecting belt

## The construction actually tested

This uses **`papers/witness-generators/tetrahedron.html`**, including its gap 0.7, opposing-base rotation, and nearest-neighbor stitches. It does not use the later outward-tetrahedra page, the shared-face receiver, or the three-piece Pachner rearrangement.

For each original tetrahedron, join its four triangular faces to its own barycenter. This gives four tetrahedral pieces.

For the connecting belt, join its six triangular faces to the combined barycenter of the eight original vertices. This gives six tetrahedral pieces. The original outer geometry and face incidences are unchanged. No return arrows or extra cap pieces are introduced.

## Exact results

- All four pieces of one original tetrahedron are mutually congruent.
- All six belt pieces are mutually congruent.
- The belt pieces form a six-cycle of face adjacencies.
- The belt pieces and proton pieces are **not congruent to each other**.
- The pieces have disjoint interiors: the construction is the center fan of the convex antiprism, with its two cap cones omitted.

For the page's edge scale, the squared edge lengths of one piece are:

```text
proton: 9/8, 9/8, 9/8, 3, 3, 3
belt:   449/400, 449/400, 449/400, 149/100, 149/100, 3
```

So “same building block” is true as a face-to-center construction and as an abstract tetrahedron, but not as a rigid geometric shape.

Changing only the gap cannot make the distinguished face-to-center pieces congruent. At general gap g, a belt base triangle has squared sides 3, 1+g², 1+g². Making it equilateral requires g²=2, but then its three center-edge squares are 3/2 rather than the proton piece's 9/8.

## Volumes are not assigned masses

With g the separation between the triangular rims:

```text
one proton piece = sqrt(6)/16
whole proton     = sqrt(6)/4
one belt piece   = sqrt(3) g/8
all six pieces   = 3 sqrt(3) g/4
```

At g=0.7:

- one belt piece has about 0.989949 times one proton piece's volume;
- the complete six-piece belt has about 1.484924 times the proton volume.

At g=1/sqrt(2), individual piece volumes would agree, but their shapes would still differ; total belt volume would then be exactly 3/2 of the proton volume.

Consequently a hypothesis assigning the same additive mass to each piece predicts 6/4=1.5, not the neutron/proton ratio. That is a limitation of that extra mass assumption, not a mass prediction from the geometric checker. No coefficient/resource law has been compiled here.

## The common center is different

The four-piece proton fills an ordinary tetrahedral solid. Its center has a spherical link.

The six-piece belt is the cone over an annulus. Its common center has an **annular link**, so the union has a non-manifold point there. It is not an ordinary hollow solid tube: the radial pieces all meet at the center.

There are six outer belt faces and six additional boundary triangles from the center to the two rims. Two more tetrahedra, one over each triangular cap, would fill the entire antiprism gap and give its center a spherical link. Those two pieces are identified in the checker but deliberately not added to the proposed six-piece belt or its visualization.

## Visualization

`papers/witness-generators/tetrahedron-four-six.html` is a new copy of the exact original layout, with a **Face-to-center tetrahedra** control enabled by default. Each original has four colored pieces and the belt has six: fourteen pieces in the complete displayed assembly. Yellow markers show the derived centers.

Use **Explode** to separate the pieces. The un-exploded layout is the geometry checked. Turning the new control off restores the original surface view. The original `tetrahedron.html` remains unchanged.

## Verification

```text
python research/voevodsky/checkers/check_four_six_center_cones.py
```

Seventeen exact checks pass, covering source binding, convex supporting faces, oriented boundary cancellation, volumes, piece congruence, adjacency and center links. Artifact: `results/four_six_center_cones.json`.

The new page also passed JavaScript module syntax checking and a headless Chromium load; its explosion and face-to-center toggle controls were exercised without page errors.

The next unresolved construction question is whether the intended “quark complex” is an abstract face-to-center carrier or must preserve the original piece's metric and coefficient protocol. The six-versus-four geometry is now explicit; the original protocol has not been transferred to the differently shaped belt pieces by assumption.
