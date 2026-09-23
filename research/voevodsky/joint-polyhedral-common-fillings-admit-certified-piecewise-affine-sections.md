# Joint polyhedral common fillings admit certified piecewise-affine sections

## Theorem and exact hypotheses

Let Q be a compact rational polytope in public coordinates. A group of histories defines a common relation R subset Q x R^r by finitely many jointly affine rational inequalities, including all source admission conditions. The relation is convex in the joint variables, not merely convex separately in each fiber.

Then the following are equivalent:

1. Every public point has a common filling.
2. Every vertex of Q has a common filling.
3. R admits a continuous, rational piecewise-affine section over Q.

Proof: (1) implies (2). For (2) choose one rational feasible lift at each vertex. Nonempty rational polyhedra have rational points, so rational choices exist. Triangulate Q using its vertices, consistently across shared faces. On each simplex interpolate the chosen fine lifts with the public barycentric coordinates. Every joint point is a convex combination of admitted lifted vertices, so all joint inequalities hold. Interpolants agree on a shared face because they use the same selected vertex lifts there. This gives (3), which implies (1).

The argument applies to lower-dimensional polytopes in their affine hull. It needs no uniform positive fiber volume. It does not cover nonlinear or merely pointwise-convex relations without joint convexity.

## Finite obstruction and history grouping

For these hypotheses, all-domain compatibility of a history group is decided by common-fiber feasibility at the FINITELY MANY public vertices. Failure somewhere implies failure at at least one vertex by contraposition of the construction.

At a fixed vertex, if fibers lie in a common affine space of dimension at most r, Helly supplies an incompatible subfamily of at most r+1 histories. Rational infeasibility can be certified by a Farkas combination of that subfamily's rows. Thus the earlier compatibility hypergraph can be built, in principle, from vertex-local obstructions; successful groups have explicit continuous sections, not just pointwise choices.

Minimum lifting-state count therefore equals the minimum partition into vertex-compatible groups under this exact finite family and contract, with shared code and proof resources charged separately. Hypergraph coloring and public vertex enumeration can be expensive; the theorem makes no efficient minimization claim.

## Owning example: piecewise-affine is genuinely needed

Use m=4 with source center (50,51,52,53), delta=128^-4 and local coordinates

    U=Ucenter+delta*p, V=Vcenter+delta*q,
    t0=50+delta*h, t1=51+delta*k.

Solve the other two moments for t2,t3. This inverse is affine. Exact admission of all 16 corners of the local cube [0,1]^4 proves the cube lies in the owning source image with these fine coordinates.

On the public square 0<=p,q<=1 retain the complete common relation

    max(p,q)<=h<=min(1,p+q), 0<=k<=1.

It is defined by joint affine inequalities and every public fiber is nonempty. The common section

    h=max(p,q), k=0

is affine on each side of the diagonal p=q and continuous across it. The source inverse then supplies the actual atom vector.

No global affine section exists: the four public corners force h values (0,1,1,1) at (0,0),(1,0),(1,1),(0,1). An affine function on a square must satisfy h00+h11=h10+h01; these forced values violate that identity. This rules out every affine section, not merely a selected interpolation.

## Certificate and independent verification

The producer exports the admitted local cube, the complete joint rows, four selected source lifts and the diagonal triangulation. The independent verifier imports neither the producer nor a solver. It checks source caps, moments, original rows and all vertex lifts.

Coverage uses explicit barycentric formulas: for q<=p, weights (1-p,p-q,q) on vertices (00,10,11); for p<=q, weights (1-q,p,q-p) on (00,11,01). These are nonnegative, sum to one and reproduce the public point. On p=q both formulas reduce to (1-p)X00+p X11. Thus continuum coverage, shared-face agreement and source admission follow algebraically. Sixteen rational interpolation controls check implementation; they are not the continuum proof.

## Resource boundary

The theorem closes the continuous-selection gap for jointly polyhedral histories over a compact polyhedral public domain. It does not make their common sections cheap. Enumerating vertices, testing feasible fibers, triangulating, recording fine lifts and locating a query simplex can all grow. Some selected sections can have simpler generative formulas, as max(p,q) does here. No lower bound on all section representations follows from a large chosen triangulation.

Nor does a common section restore every history's fine relation. It returns one point lying in their intersection and is sufficient only for the declared valid-lifting contract and its permitted public continuations. Fine re-exposure remains a stronger promise.

## Reproduction

    python research/voevodsky/checkers/check_polyhedral_common_section.py
    python research/voevodsky/checkers/verify_polyhedral_common_section.py

Artifacts:

- `results/polyhedral-common-section.json`
- `results/polyhedral-common-section-verification.json`

The source inverse and cube admission are checked directly; this is not a fresh upstream analytical-admission proof, general-purpose triangulation implementation or authenticated observation protocol.
