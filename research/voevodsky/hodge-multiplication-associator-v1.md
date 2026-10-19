# An explicit algebraic filler for the multiplication associator

## Question and frozen conventions

Fresh workbench action: multiplication-associator-control. Retain square=P1 minus {1}, partial_n=sum_i (-1)^(i-1)(face_i^0-face_i^infinity), and the curves

    T(a,b): y(z-1)-a(z-b)=0,
    partial T(a,b)=[b]-[ab]+[a].

Work over C with the concrete rational triple a=2,b=3,c=5; the same calculation applies when a,b,c,ab,bc,abc avoid 0 and 1. SCC obligations: ordered composition, every face/corner and the actual normalized higher filler. No Hodge cotower or sixfold class is identified with these weight-one cycles.

## The closed associator

The two associations differ by

    A(a,b,c)=T(a,b)+T(ab,c)-T(b,c)-T(a,bc).

Their point boundaries cancel term by term. This proves partial A=0, not that A is a boundary. The four curves are distinct for (2,3,5), so A is not the zero raw cycle.

## A source-derived degree-three surface

In square^3 with ordered coordinates x,y,z, define

    S(a,b,c): x(y-1)(z-1)-a(yz-y-bz+bc)=0.

Its multihomogeneous closure, with x=X0/X1, y=Y0/Y1, z=Z0/Z1, is

    X0(Y0-Y1)(Z0-Z1)
      -a X1(Y0 Z0-Y0 Z1-b Y1 Z0+bc Y1 Z1)=0.

The coefficient of x and the constant term are coprime as polynomials in y,z under the stated nondegeneracy conditions. At y=1 the second factor is not identically zero; at z=1 it equals b(c-1), nonzero. Hence the primitive equation linear in x is irreducible. Its multidegree is (1,1,1); restricting the projective closure to square^3 gives an integral codimension-one cycle of dimension two.

## All six faces

| Face | Cycle after restricting remaining coordinates to square |
| --- | --- |
| x=0 | T(b,c) in (y,z) |
| x=infinity | empty: (y-1)(z-1)=0 is entirely deleted |
| y=0 | T(ab,c) in (x,z) |
| y=infinity | D_a={x=a} times square_z; z=1 part is deleted |
| z=0 | T(a,bc) in (x,y) |
| z=infinity | T(a,b) in (x,y) |

Nonzero scalar multiples of a defining equation do not change the effective face cycle. All surviving factors have multiplicity one. Applying the alternating boundary signs gives

    partial S=T(b,c)-T(ab,c)+D_a+T(a,bc)-T(a,b)
             =D_a-A.

D_a is a genuine cubical degeneracy: pull back the point [a] along square^2 -> square in the x coordinate. Therefore in the normalized cubical complex

    partial(-S)=A.

This is an explicit higher filler, not an appeal to vanishing of a homology group.

## Every proper face is admissible

For the twelve double faces, seven have one retained point:

    x=0,y=0: z=c;
    x=0,z=0: y=bc;
    x=0,z=infinity: y=b;
    y=0,z=0: x=abc;
    y=0,z=infinity: x=ab;
    y=infinity,z=0: x=a;
    y=infinity,z=infinity: x=a.

The other five meet only deleted coordinate-one loci and are empty in the cube. Every retained point avoids 0,1,infinity in its remaining coordinate. All eight triple faces are empty: direct substitution leaves a nonzero constant. Thus all intersections have the required dimensions; an empty face here is an admitted intersection with no points, not an absent face in the indexing category.

Before normalization the extra D_a is nonzero. Its own boundary is zero because its two last-coordinate faces coincide. The raw and normalized calculations are consistent with partial squared=0. Dropping D_a prematurely would nevertheless make the raw chain equality false.

## Consequence and disposition

The apparent multiplication associator defect is algebraically fillable for this explicit sector. It cannot be used as a nonfillability obstruction. The sequence now includes actual degree-one rational-function graphs, degree-two multiplication relations and a degree-three associator, with their discarded terms identified as specific degeneracies rather than arbitrary invisible information.

This is still codimension one on the cubical parameter space over Spec(C). Three cubical coordinates do not turn the construction into codimension three on the fixed X. A product with a supplied codimension-two algebraic support changes total codimension but does not create a new representative of alpha. The next bounded task is to type precisely this transfer and its limits before any further coherence-level construction. Do not infer a universal Hodge realization from a tower of controls on already supplied algebraic inputs.

Verification: exact multihomogeneous identities for six faces, twelve double faces and eight corners, free-chain boundary cancellation, four-curve distinctness and raw-versus-normalized controls. Algebraic-cycle intersection conventions are imported standard facts; no proof-assistant certification or Hodge verdict is claimed.
