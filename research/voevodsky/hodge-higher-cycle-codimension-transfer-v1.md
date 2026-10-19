# Codimension transfer: higher coherence cells do not supply a new degree-zero class

## Question and actual fixed-X support

Fresh workbench task: higher-cycle-codimension-transfer. Keep the selected polarized sixfold (X,E). Choose an integer m such that the ample line bundle L with c1(L)=mE is very ample. Two general sections give a codimension-two complete intersection W with class m^2 E^2. Standard Bertini supplies a smooth choice; its projective equations are not computed. This is a supplied algebraic support on the fixed X, not a new exceptional cycle.

SCC obligations: source product typing, boundary/degeneracy transport and realization degree. Cubical dimension n is a homological index, not physical time or algebraic codimension.

## The actual product chain map

For any supplied codimension-two cycle W on X, exterior product gives

    j_W: z^1(Spec(C),n)_Q -> z^3(X,n)_Q,
    C -> W external C.

A field cycle C of codimension one has dimension n-1. W has dimension four, so the product has dimension n+3 in X times square^n, whose dimension is n+6. Its codimension is three for every n, not just for n=3.

Proper face intersection is preserved by this product: intersecting the parameter face gives W external (C intersect face). Dimensions add as required. Pullback along coordinate-forgetting maps also commutes with the product, so degeneracies remain degeneracies. W has cubical degree zero; the product differential has no extra Koszul sign:

    partial(W external C)=W external partial C.

These standard exterior-product/cycle intersection facts apply to rational signed cycle combinations as well as the chosen complete intersection.

## The three constructed levels on X

For constants a,b,c with the nondegeneracy conditions already checked:

- W external [a] is in z^3(X,1), with zero boundary.
- W external T(a,b) is in z^3(X,2), with boundary W external ([b]-[ab]+[a]).
- W external (-S(a,b,c)) is in z^3(X,3), with normalized boundary W external A(a,b,c).

The raw degenerate term W external D_a remains the pullback of W external [a] along a cubical projection. The product neither hides a new raw term nor licenses quotienting by anything beyond the specified degeneracies.

But z^1(Spec(C),0)=0: a point has no codimension-one subvariety. Hence the whole decomposable source chain map has ZERO degree-zero component. It supplies higher cycles and relations on X, not a new ordinary codimension-three cycle. Taking repeated boundaries cannot change this: partial squared=0. The parameter-space three-dimensional cube did not create a degree-six cohomology class.

## A nonconstant control also distinguishes relations from classes

Choose two further general sections s,t of the same L, restricting nontrivially to W. Their ratio f=s/t is a rational function on W. The graph construction yields

    partial Gamma_f = Z_s - Z_t,

where Z_s and Z_t are actual codimension-three complete intersections on X. Both have class m^3 E^3, so their difference has zero cycle class. It can be nonzero as a raw cycle, but is a principal-divisor relation. Its intersection degree against E^3 is zero, despite each effective cycle having degree 2160 m^3.

By contrast alpha has period one on the marked all-x six-torus, whereas E^3 has period zero there. Neither the constant product-chain construction nor this principal-divisor difference supplies alpha. This is an exclusion of these specific operations as constructors of a new nonzero class, not an exclusion of all algebraic cycles.

## Realization degree is another independent check

With the standard higher-Chow regulator grading, z^p(X,n) homology maps to Deligne cohomology H_D^(2p-n)(X,Q(p)). For p=3 the respective degrees for n=0,1,2,3 are 6,5,4,3. Thus the constructed higher cells do not themselves live in the ordinary cycle-class target H^6(X,Q). A further claimed comparison must type its degree shift, not identify all levels by a common tetrahedral picture.

This regulator grading is imported standard background; no full regulator construction or value on the higher cells is computed here. In particular a degree-one higher cycle need not be zero merely because its ordinary degree-zero boundary is zero.

## Disposition and next actual interface

The codimension transfer is constructed and is coherent at all three tested levels. It exposes a restriction: these constant-source cells have no degree-zero output, and the nonconstant rational-function boundary is homologically trivial. The tested tower therefore repairs relations among supplied algebraic data; it does not establish existence or nonexistence of an algebraic representative of alpha.

The next independently specified comparison is the degree-six Deligne realization interface: determine whether a rational Hodge class already has a Deligne lift without an algebraic cycle, and distinguish that lifting problem from the image of the algebraic cycle regulator. This is a concrete standard exact-sequence test, not a request for the operator to supply a missing map. It addresses whether the richer cohomological target can carry the proposed existence obstruction.

Verification: dimension/codimension formulas, degree-zero source, chain and degeneracy transport identities on the already checked formal boundaries, regulator degree bookkeeping, and exact E^3/alpha period and intersection controls. Bertini, exterior-product compatibility and regulator grading are imported written mathematics, not proof-assistant certification. No fixed-alpha algebraicity or nonalgebraicity result is claimed.
