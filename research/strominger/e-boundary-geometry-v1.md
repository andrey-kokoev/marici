# Inferring E geometry from H-1/H-2 and reversal

## Change of question

Instead of selecting an existing E solid by rotational symmetry, ask what
boundary data can represent E while retaining enough information for a reversed
volume description. The saved 24 embeddings are reference samples, not an
assumption that E must be an occupied tetrahedron.

The common interface structure is a flag:

```
H-1 attachment: edge C1--M1
H-2 attachment: triangle M1 C1 C2, containing that edge
E context: M2
```

This motivates a candidate two-dimensional E witness:

```
triangle (C1,M1,C2) joined to triangle (C1,M1,M2)
along the hinge C1--M1
```

It is a triangulated disk with four boundary vertices C1,C2,M1,M2. The second
triangle is a proposed way of encoding the existing context, not a native E
transfer face supplied by the grammar.

## Metric test

Unfold the two triangles into a plane, retaining their edge lengths. None of
the 24 resulting disks is a metric square. For the eight regular reference E
shapes, the disk is a rhombus made of two equilateral triangles. A combinatorial
square (four boundary sides) need not have four right angles.

The membrane contains five edge lengths, while a tetrahedron has six. The
missing information is the angle between the two faces about their shared
hinge (equivalently the opposite-vertex distance). All 24 reference samples
reconstruct their missing distance correctly when that angle is supplied.
Their hinge cosines are 1/3 for regular reference tetrahedra and 1/sqrt(3) for
the sampled split reference tetrahedra.

For two unit equilateral faces sharing an edge, different hinge angles retain
exactly the same intrinsic membrane but produce different fourth-edge lengths
and volumes. With height h=sqrt(3)/2:

```
opposite-edge length^2 = 2 h^2 (1-cos(phi))
tetrahedron volume     = h^2 |sin(phi)| / 6
```

A regular tetrahedron requires cos(phi)=1/3. The flat disk has phi=pi and zero
volume. Thus flattening loses information unless the fold angle is retained.
Signed orientation also matters if the embedded filling, rather than only its
lengths up to reflection, is to be reconstructed.

## Candidate interpretation of reversal

E can be explored as an interface witness carrying:

- the marked two-face disk;
- a hinge/filling datum and orientation;
- the existing reader-origin and coefficient-reference data.

P is then a volume presentation and E a boundary presentation of a more richly
specified object. An E->P conversion would reconstruct a filling; P->E would
extract boundary data while retaining what makes reconstruction reversible.
This is a proposed representation map, not a rigid rotation of a surface into
a solid. Eversion/rotation may implement or organize such a map only after the
filling law and realization dependence are specified.

The hinge angle has not been identified with the realization parameter. The
current tests show the information it must supply, not a source-derived law
fixing it. Reconstructing a split sample recovers its split tetrahedron; it
does not automatically satisfy the forward regular-only proton convention.
The eight regular samples give the simplest test family for a volume/boundary
P/E exchange with the present shape convention.

Production and viewer remain unchanged.

```sh
node research/strominger/checkers/probe_e_boundary_geometry.mjs
```

Evidence: `results/e-boundary-geometry/verification.json`, including unfolded
coordinates, side/diagonal lengths and explicit same-membrane/different-volume
examples.
