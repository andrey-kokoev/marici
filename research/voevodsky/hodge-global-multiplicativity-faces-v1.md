# Global multiplication surface: vertical terms survive closure but are degenerate

## Question and actual source

Fresh workbench task: compute a nonconstant multiplication surface globally, not only on the generic fiber. Choose X=P1 with x=s/t, f=x, g=x+1. Use square=P1 minus {1} and the previous convention partial=(y=0)-(y=infinity)-(z=0)+(z=infinity). This is a known algebraic control, not a change of the fixed sixfold target. SCC obligations: closure, all face intersections, corners, then quotient by actual cubical degeneracies.

Write y=u/v and z=a/b. The graph z=(y-x(x+1))/(y-x) closes to the surface T in P1_x times P1_y times P1_z defined by

    F = t^2*u*(a-b) + s*v*(b*(s+t)-a*t) = 0.

This has multidegree (2,1,1). In the affine x,y chart it is the primitive linear equation z(y-x)=y-x(x+1). The polynomials y-x and y-x(x+1) are coprime: their difference is x^2, and x does not divide y-x. Hence the graph closure is irreducible; homogenization introduces no whole coordinate-divisor component. Restrict T to P1_x times square^2.

## Complete face calculation

Let V_c={x=c} times square denote a vertical degree-one cycle, and Gamma_h the graph of h restricted to square. Exact substitutions give:

| Face | Restricted equation, irrelevant invertible coordinate factors omitted | Result inside the cubical chart |
| --- | --- | --- |
| y=0 | s*(b*(s+t)-a*t) | V_0 + Gamma_(x+1) |
| y=infinity | t^2*(a-b) | 2 V_infinity; z=1 is excluded |
| z=0 | -t^2*u+s*(s+t)*v | Gamma_(x(x+1)) |
| z=infinity | t*(t*u-s*v) | V_infinity + Gamma_x |

The multiplicity two at infinity is essential. The last face also has a vertical component; it cannot be inferred from the generic graph formula alone.

All four faces have dimension one as required. Every double face is zero-dimensional, with multiplicities:

    (y=0,z=0):           [0]+[-1],
    (y=0,z=infinity):    [0]+[infinity],
    (y=infinity,z=0):    2[infinity],
    (y=infinity,z=infinity): 2[infinity].

These points remain in the cubical chart because their y,z coordinates are 0 or infinity, not 1. There are no higher corners in a two-cube. Thus T is an admissible degree-two cycle, including the special base fibers.

## Boundary before and after the legitimate quotient

In the free group of face-admissible degree-one cycles,

    partial T = Gamma_(x+1) - Gamma_(x(x+1)) + Gamma_x + V_0 - V_infinity.

The raw vertical correction is nonzero. In the normalized cubical higher-cycle group, both V_0 and V_infinity are degeneracies: they are pullbacks of the degree-zero point cycles under P1_x times square -> P1_x. Therefore the normalized boundary is

    partial T = Gamma_(x+1) - Gamma_(x(x+1)) + Gamma_x.

This is a justified quotient by specified source maps, not a fitted removal of a residual. The corners also verify the raw identity partial squared=0. Each vertical V_c has identical 0 and infinity faces, while the graph divisors satisfy div(x+1)-div(x(x+1))+div(x)=0.

## Hostiles and distinction from Hodge

1. Deleting the vertical terms before normalization gives a false equality of raw chains.
2. Counting the y=infinity component only once gives the wrong raw boundary and misses its intersection multiplicity. After normalization this mistake can become invisible, so a normalized-only test is insufficient.
3. Removing the alternating sign on the z faces destroys the desired multiplication relation.
4. Declaring all vertical terms inadmissible would reject a legitimate algebraic filler; they meet faces properly and are then removed by the standard degeneracy quotient.

The candidate 'global closure destroys this nonconstant multiplication filler' is rejected for f=x,g=x+1. The test does locate a real compression: raw vertical differences are erased by normalization. Here that erasure is explicitly licensed and does not remove the surviving multiplication witness. It gives no nonalgebraicity claim and no reason to identify an arbitrary dark mode with a degeneracy.

## Disposition and next action

The source multiplication comparison now exists for one actual nonconstant global example, with all faces and corners checked. This completes the bounded global-face task, not the general moving lemma, all-cycle hyperdescent, or a sixfold obstruction. Do not expand to an unbounded census of similar functions for confirmation.

Next bounded relation test: compose multiplication fillers for three functions and compare the two associations, retaining the raw versus normalized distinction; an associativity comparison requires an actual degree-three chain or a stated obstruction quotient. The independent quadratic-pairing task on the fixed sixfold remains executable and has higher direct relevance to the recalled quadratic-stage loss.

Verification: the companion checker uses exact sparse polynomial identities for the multihomogeneous closure and every face/corner, plus raw and normalized chain bookkeeping and deliberate multiplicity/sign/omission mutations. The graph/Cartier-intersection interpretation and cubical-cycle definitions are written standard mathematics, not proof-assistant certification.
