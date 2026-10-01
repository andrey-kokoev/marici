# Twelve triangles, a collective eigenline, and an explicit 1836-arrow realization

## Construction from the original seed

Take the four endpoint states at the vertices of a regular tetrahedron:

    A=( 1, 1, 1), B=( 1,-1,-1),
    C=(-1, 1,-1), D=(-1,-1, 1).

The two original oriented triangles give the vertex rotations (ABC) and (ADB). Their permutation closure has twelve elements: the proper tetrahedral rotation group A4. Thus the twelve positions here are generated from the two seed cycles, not supplied as twelve independent copies.

For every face, insert its centroid and join it to the three vertices. The twelve small oriented triangles are:

| Parent face | Three triangles, with centroid first | Outer arrow labels |
|---|---|---|
| ABC | (F_ABC,A,B), (F_ABC,B,C), (F_ABC,C,A) | AB, BC, CA |
| ADB | (F_ABD,A,D), (F_ABD,D,B), (F_ABD,B,A) | AD, DB, BA |
| ACD | (F_ACD,A,C), (F_ACD,C,D), (F_ACD,D,A) | AC, CD, DA |
| BDC | (F_BCD,B,D), (F_BCD,D,C), (F_BCD,C,B) | BD, DC, CB |

Equivalently, these are the A4 orbit of the reference triangle (F_ABC,A,B). There is exactly one small triangle per original directed tetrahedral arrow.

This is a triangulated tetrahedron, not a new convex polyhedron with twelve distinct supporting planes. The underlying body has four facets; each has been divided into three triangles.

## Closed positive geometry

The surface has eight vertices, eighteen undirected edges and twelve triangles. Every shared edge occurs with opposite orientations in its two adjacent triangles. Consequently:

    boundary(sum of triangles)=0,
    V-E+F=8-18+12=2.

All twelve triangles lie in outward supporting planes. Coning each to the origin produces a positive oriented tetrahedron of volume 2/9. Their total volume is 8/3.

This is also a positive geometry in the standard simplex sense. Put

    lambda_k(x)=(1+v_k dot x)/4.

The four lambda values sum to one and are positive inside the tetrahedron. Its oriented canonical form is

    Omega = d(lambda_A) wedge d(lambda_B) wedge d(lambda_C)
            / (lambda_A lambda_B lambda_C lambda_D)
          = 16 dx wedge dy wedge dz / product_k(1+v_k dot x).

It has the simplex's logarithmic boundary poles. The twelve-triangle surface is a boundary triangulation of that same positive geometry.

## Triangle eigenlines and their transport

Let C be the three-slot cyclic coefficient operator and omega=exp(2*pi*i/3). Its positive complex eigenvector is c=(1,omega,omega²).

For triangle g, form X_g with its three spatial vertex coordinates as columns. Its spatial cyclic operator and eigenvector are

    A_g=X_g C X_g^{-1}, v_g=X_g c.

The matrices X_g are invertible because their face planes do not pass through the origin. A_g³=I and A_g v_g=omega v_g. The rank-one Hermitian projector onto that eigenline is

    P_g=v_g v_g^dagger/(v_g^dagger v_g).

The tetrahedral rotation R_g carries the reference triangle to triangle g, so

    X_g=R_g X_0,
    R_g^T v_g=v_0,
    R_g^T P_g R_g=P_0.

These are exact identities over Q(i*sqrt(3)). Each local cyclic operator is a linear coordinate realization of a coefficient cycle; it need not be a Euclidean rotation of the small isosceles triangle.

The lines coincide AFTER transport into the reference frame. They are twelve distinct lines in the common ambient spatial coordinate frame, and sum_g v_g=0 there. This difference is essential. Literal coincidence of all nonreal triangle eigenlines in ambient C³ would give all triangles the same real tangent plane; a connected surface of that kind cannot enclose positive three-dimensional volume.

## The collective identity is an intersection of two projections

Use the direct sum of the twelve local spatial coefficient spaces, of dimension 36. The three coordinates are the spatial/contrast directions of the four-state tetrahedron; they are not an extra three-state particle.

Define:

    L = blockdiag(P_g),                       rank 12;
    G[g,h] = R_g R_h^T / 12,                 rank 3;
    N = G L = L G,                          rank 1.

G is the average of the group action that permutes triangle positions while rotating their local vectors. Its fixed space consists of assignments v_g=R_g w for one common w. Imposing the selected local eigenline restricts w to the reference line, leaving exactly one collective eigenline.

For u=(v_0,...,v_11), u^dagger u=80 and

    N=u u^dagger/80,
    N²=N,
    Nu=u.

This constructs the collective identity algebraically. It does not assume that arbitrary initial phases have synchronized. For example, alternating signs on the twelve transported eigenvectors leave every local P_g unchanged but produce a vector annihilated by N.

## An explicit three-stage interaction graph

Implement the three maps as actual separate port stages:

    raw ports --L--> local-mode ports --G--> aligned ports --N--> raw ports.

Each stage has 36 ports, indexed by (triangle outer arrow, spatial axis). An elementary graph arrow is one directed pair of these typed ports with nonzero map coefficient. The stage labels identify distinct ports of the circuit, not histories attached to primitive packets.

The axis frame comes from the three pairs of opposite tetrahedral edges. In this frame the rotations are signed permutation matrices, so each 3-by-3 block R_g R_h^T has exactly three nonzero entries. Each local eigenvector has three nonzero coordinates.

| Operation | Nonzero directed arrows |
|---|---:|
| Local spectral selection L | 12 * 3² = 108 |
| Symmetry averaging G | 12² * 3 = 432 |
| Dense collective-projector feedback N | (12 * 3)² = 1296 |
| Total | 1836 |

In expanded form:

    108 + 432 + 1296
      = 12*3² + 12²*(3+3²)
      = 12*3² + 12²*12
      = 12*(3²+12²)
      = 1836.

The final equality uses 3+3²=12: the number of directed nonidentity relationships between four endpoint states.

The return operator is

    N G L = N² = N.

It is identity on the collective eigenline. It projects, rather than invertibly transports, general off-line inputs.

## Literal closed-traversal union

Every dense feedback arrow belongs to one closed three-step path consisting of an L arrow, a G arrow and that N arrow. There are exactly 1296 such cycles when based at the raw stage. Their union contains every one of the 1836 elementary directed arrows, each counted once.

For each feedback pair, the signed-permutation symmetry block makes the intermediate axis unique. The cycle weight is the squared modulus of the corresponding entry of N, hence strictly positive. Summing these cycle weights gives trace(N²)=trace(N)=1.

Thus this particular graph has both:

- a unique-arrow union of size 1836 for its specified identity-return traversals;
- a coherent return that is the rank-one collective identity.

No separate extra nine-arrow triangle copy was added to a larger arrow set. The 108 local-mode arrows, 432 symmetry arrows and 1296 feedback arrows have different source/target port types, and are explicitly enumerated.

## What fixes this count

**Stagewise positivity:** the spatial surface itself is positive, but the [stagewise audit](stagewise-geometric-positivity.md) distinguishes this from positive geometric transport. The coefficient maps preserve positive cell amplitudes; applied literally to spatial corner coordinates, they produce split seams and nonreal points. An atlas/embedding interpretation of the intermediate stages is still required.

The subsequent [minimality audit](twelve-triangle-net-minimality.md) proves that the 1836-arrow graph is pruning-minimal at fixed weights, but the same geometry and exact collective projector admit a 73-arrow three-stage realization (or 72 arrows in two passes). These smaller counts attain their respective layered-network lower bounds.

The count belongs to THIS implementation: three distinct stages, the natural tetrahedral axis frame, and dense collective-projector feedback.

If the stages are identified as the same port set, the union has only 1296 arrows because the supports overlap. If dense N feedback is replaced by 36 straight identity wires, the cycle still evaluates to N but uses 108+432+36=576 arrows. Factoring the dense maps through lower-rank interfaces also changes the primitive graph.

Therefore this constructs a genuine 1836-arrow realization and its closed traversals. It does not prove 1836 is a basis-independent count or a minimum imposed by identity closure. Its maps are linear coherent filters; conservative phase-locking dynamics or a physical proton interpretation would require further structure.

## Verification and artifacts

    python research/nima/checkers/check_twelve_triangle_positive_geometry.py

Checks use exact rationals and Q(i*sqrt(3)). They cover the seed-generated group, all facet placements, boundary cancellation, supporting halfspaces, signed volumes, local eigenpairs, transport covariance, commuting projector intersection, collective idempotence, all 1836 explicit arrows, closed-cycle coverage and positive cycle weights summing to one.

Controls reverse one triangle (three nonzero boundary edges), flatten the surface (zero volume), change relative phases (local projectors remain aligned while the collective amplitude cancels), and identify the port stages (the unique-arrow count drops to 1296).

Artifacts:

- `results/twelve-triangle-positive-geometry.json`: check results and all triangle placements/transports.
- `results/twelve-triangle-positive-geometry.obj`: the oriented twelve-triangle spatial mesh.
- `results/twelve-triangle-1836-arrows.json`: every elementary arrow, with typed endpoints and its exact complex weight.
