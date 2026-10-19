# Deuterium: an explicit four-dimensional turn in both directions

Constructed a continuous deformation of the actual canonical deuterium's six
labelled vertices, starting in the original three-dimensional embedding with
fourth coordinate zero. Paired vertices are C0/M2, M0/C2 and C1/M1.

## Endpoint results

| Travel | Half-turn | Full turn |
|---|---|---|
| Positive direction | P/E vertex sets exchanged, N set preserved | Original labelled vertices restored |
| Negative direction | P/E vertex sets exchanged, N set preserved | Original labelled vertices restored |

Both paths implement the same order-two permutation at their halfway point.
They travel on opposite sides of the deformation. Choosing the opposite sense
does not yield a different half-turn endpoint: +pi and -pi realize the same
involution. At the halfway point, applying the previously tested context-aware
reader order and M/C/index relabelling gives valid P/N/E reader templates.

## Explicit motion

For a paired vertex x and its partner y, let m=(x+y)/2, d=(x-y)/2. Give the
three pairs distinct signed heights h=+/-1,+/-2,+/-3 and corresponding signed
unit vectors u along the three ordinary axes. Define

```
ordinary coordinates: m + cos(theta)*d + sin(theta)*u
fourth coordinate:    h*sin(theta)
```

Use theta from 0 to +2pi or from 0 to -2pi. At pi, x moves to y. At 2pi, x
returns to itself. Pair members have opposite h and u.

The six heights are distinct. Thus when sin(theta) is nonzero, all vertices
have distinct fourth coordinates; when it is zero, they are distinct original
or swapped vertices. Vertex collisions are excluded throughout the paths.

A preliminary purely axial lift (u=0) flattened tetrahedra at a quarter turn.
The lateral terms above remove that observed degeneracy. At 721 samples per
direction, the minimum tetrahedron Gram determinant is approximately 0.156674
and minimum intervertex distance is approximately 0.509013. Sampled nonzero
volume is not a proof of nondegeneracy at every intermediate angle.

This is a constructed deformable labelled-vertex motion, not a rigid rotation:
pair distances change. Shared abstract faces remain shared because incident
cells use the same vertex trajectories. Intersections of cell interiors have
not been certified; neither torus topology nor a complete embedded-solid
eversion follows from the vertex test. The local lattice transfer rules are
checked at the reader endpoints, not asserted during the deformation.

Production and isotope viewer remain unchanged.

## Reproduction

```sh
node research/strominger/checkers/probe_deuterium_4d_turn.mjs
```

Evidence: `results/deuterium-4d-turn/verification.json`, including quarter-turn
coordinates for both directions, initial failed axial-lift diagnostic, source
hash, transformed reader frames and sampled geometry checks.
