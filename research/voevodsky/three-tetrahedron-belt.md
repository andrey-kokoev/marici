# Three tetrahedra around the pair axis

## Candidate geometry

Start with the two face-sharing tetrahedra ABCD and ABCe from the three-arrow receiver display. The same five geometric vertices admit three tetrahedra

```text
ABDe, BCDe, CADe.
```

All three meet on the apex-to-apex edge De. They share the internal triangular faces ADe, BDe, CDe pairwise. The link of De is the triangle A-B-C-A: a circle around the axis.

This is the standard 2-to-3 bistellar/Pachner move. It supplies a precise three-piece ring to test, rather than guessing a belt from the number three.

## What stays the same

The two arrangements have exactly the same oriented outer boundary: six triangles. They occupy the same triangular bipyramid, with total volume 16/3. The three new cells each have volume 16/9.

Both derived barycenters lie on De. Measured from D at parameter 0 to e at parameter 1, their positions are 3/8 and 5/8; the original shared-face center is at 1/2. Thus the center-to-center segment lies inside the ring's core axis.

The entire filled three-cell complex is a ball, not an annulus. Its **edge link** is circular. A belt collar around the core has an annular transverse region only when the core neighborhood is excluded; the calculation does not silently remove it.

## What changes

The old internal face ABC is replaced by the new internal edge De and three internal faces. Thus the move changes retained incidence but does not add material volume or another geometric object to the old pair.

It cannot by itself represent “adding a neutron while retaining the old pair unchanged.” That would require a different construction or a specified retained operation associated with the changed incidence.

Nor does calling the three pieces quarks assign electric charge. The source's four center-to-face constituent tetrahedra were geometric support sectors, not a demonstrated identification with Standard Model quarks. These new cells also have a different shape from those sectors.

## Retaining both decompositions

The face center F is the intersection of De with ABC. Insert F and split each of the three ring cells at that point. The resulting six tetrahedra simultaneously refine both decompositions:

- each old tetrahedron has three children;
- each ring tetrahedron has two children.

All six children have volume 8/9, and their outer boundary is unchanged. The artifact records both parent labels. This allows comparison without erasing the old decomposition's history.

This six-cell common refinement is not automatically the earlier unrelated six-belt assembly.

## Arrow structures are not supplied by the picture

If every ring tetrahedron were assigned a complete directed K4, the union would have twenty unique primitive arrows. Relative to the current fifteen-arrow receiver source, that requires

```text
e→A, e→B, e→C, D→e, e→D.
```

These are not generated merely by drawing the three cells. Two full K4 tetrahedra sharing ABC would instead have eighteen arrows; the actual earlier receiver source had fifteen because its new legs were one-way.

No expanded coefficient count or charge is assigned to the ring here.

## Test outcome

The proposed three-piece geometry exists exactly and surrounds the pair's center axis. But it is an alternative subdivision of the same external body. To distinguish a neutron-like state, one must specify a retained internal operation or observable that distinguishes the two-cell and three-cell structures under their common refinement.

## Verification

```text
python research/voevodsky/checkers/check_three_tetrahedron_belt.py
```

Nineteen exact checks pass. Artifact: `results/three_tetrahedron_belt.json`, containing volumes, oriented-boundary comparisons, rational homology, axis positions, directed-arrow differences and the six-cell refinement with both parent maps.
