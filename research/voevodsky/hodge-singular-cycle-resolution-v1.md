# Singular cycle generators via smooth proper-map sources

## Fresh task and exact domain

Execute singular-cycle-resolution-pushforward on the unchanged smooth projective sixfold X. The cycle domain is all finite rational combinations of irreducible algebraic threefolds, not only smooth embedded centers.

Let Z be any irreducible reduced algebraic threefold in X. In characteristic zero a projective resolution rho:Y->Z exists with Y smooth projective of dimension three. Compose with the inclusion to obtain f:Y->X. Proper pushforward of cycles and cycle-class naturality give

    rho_*[Y]=[Z],
    f_*[Y]=[Z] in Z_3(X),
    f_*(1_Y)=cl_X(Z) in H^6(X,Q).

The cohomological map has degree shift six: H^0(Y) to H^6(X), with Hodge type shifted by (3,3). It is defined by Poincare duality and the proper homology pushforward, not by treating f as an embedding. For beta in H^6(X,Q), its normalization is

    integral_X f_*(1_Y) cup beta = integral_Y f*beta.

These are standard proper-pushforward and resolution facts. No cycle representing alpha is assumed as input.

## Degree, exceptional sets and resolution independence

A birational resolution has generic degree one, which fixes the fundamental-class coefficient. More generally, for a proper map from a smooth connected projective threefold Y with three-dimensional image Z, cycle pushforward is d[Z], where d is its generic degree. If the image has dimension less than three, the dimension-three cycle pushforward is zero. Counting every proper map as degree one would be wrong.

Exceptional divisors of a resolution have dimension two, not three. They cannot be added to f_*[Y] as extra codimension-three cycle generators. Their own pushforwards, when dimension is preserved, belong to the dimension-two cycle group and thus a different cohomological degree; dimension-dropping images vanish in that group. Lower-dimensional exceptional topology can be substantial without altering the degree-one fundamental-class statement.

Any two projective resolutions have a common smooth projective domination (resolve the graph of their birational correspondence). Functoriality and generic degree one show that both give the same pushed fundamental class. This is choice independence of that class, not a canonical identification of all higher cohomology on the resolutions.

Consequently there is an exact coverage statement for the cycle IMAGE:

    im(cl:CH^3(X)_Q -> H^6(X,Q))
      = span_Q{ f_*(1_Y) : Y smooth projective threefold, f:Y->X a morphism }.

The forward inclusion uses resolutions of each irreducible generator; the reverse inclusion uses the degree/dimension rule for proper cycle pushforward. This supplies all generators, not a finite enumeration or proof of Hodge surjectivity.

## Actual singular control on the fixed X

Fix a point p of X and choose k sufficiently large to prescribe second jets of H^k and apply Bertini away from p. Choose two sections s1,s2 vanishing at p with independent first derivatives, defining a smooth fourfold W. Choose a third section s3 vanishing to order two at p, with a nondegenerate quadratic restriction on T_p W. Generic choices are smooth away from p, by the base-point-free system away from p. Then

    Z=(s1=s2=s3=0)

is a complete-intersection threefold with a single ordinary double point at p and no other singularities, and [Z]=k^3 c1(H)^3 in CH^3(X). One may take Z irreducible: ample complete-intersection connectedness, smoothness off p and the locally irreducible threefold node rule out distinct components. The sufficiently-large-k jet/Bertini assertions are standard geometric existence results, not explicit equations for the fixed period matrix.

Locally in W the equation is u1^2+u2^2+u3^2+u4^2=0. Blow up the vertex. The strict transform is smooth, with exceptional quadric surface

    Q^2={u1^2+u2^2+u3^2+u4^2=0} in P^3,

isomorphic over C to P^1 times P^1. Its two ruling families do not become extra threefold generators. The resulting Y->Z is a projective resolution of degree one.

## Embedded blowup calculation: an auxiliary ambient, not the original X

For a direct check, blow up the point in X: pi:B=Bl_p X->X, with exceptional F=P^5. Write e=c1(O_B(F)) and Ebar=pi*E. The strict transforms of the three defining divisors have classes

    k Ebar-e, k Ebar-e, k Ebar-2e.

Their proper intersection is the same smooth resolution Y. On F, the two linear initial equations cut P^3 and the third quadratic initial equation cuts the smooth Q^2, so there is no extra three-dimensional component supported in F.

Because Ebar restricts to zero on F, Ebar cup e=0. Hence

    cl_B(Y)=(k Ebar-e)^2(k Ebar-2e)=k^3 Ebar^3-2e^3.

The exceptional coefficient two records the multiplicity of the node. Proper pushforward gives

    pi_* Ebar^3=E^3,  pi_* e^3=0,
    pi_* cl_B(Y)=k^3 E^3=cl_X(Z).

The point blowup formula identifies H^6(B)=pi*H^6(X) plus Q e^3. This extra summand is algebraic and killed by pushforward. With complex orientation integral_B e^6=-1, so e^3 is not a zero class before pushforward. The original exceptional Q^2 on Y has dimension two; e^3 instead represents an auxiliary dimension-three class on B. These two different exceptional objects are not conflated.

## What is and is not bridged

Every singular generator is now covered by an actual smooth proper-map source. But f:Y->X can contract exceptional sets; it is not a smooth embedded center in X. In the control Y embeds in B, whose topology and polarization differ from X. Applying the smooth-center envelope theorem on a changed ambient requires transporting its full support map back, not silently using the old Lefschetz subspace.

The all-cycle necessity gate can now be written P_prim f_*(1_Y)=0 for EVERY such source map. This is the same unresolved gate, not a consequence of resolution. Any proposed witness reader must also respect degree, pushforward and independence of the chosen resolution before it descends to the cycle class.

## Next executable construction

Embed an arbitrary smooth proper-map source by its graph in X times P^N. Test whether sufficiently positive hypersurfaces through the graph cut a smooth auxiliary sixfold containing it. If so, type the projection back to X and compute the pushforward of the auxiliary Lefschetz sector. The rank-drop locus of normal derivatives along the graph must be checked, not replaced by an unjustified Bertini assertion with base locus. This would connect the proper-map coverage with the embedded-center construction without assuming smoothability inside the unchanged X.

Verification: exact degree-shift/dimension rules, strict-transform polynomial, exceptional intersection orientation and degree-one pushforward controls. Resolution, jet generation, Bertini and cycle-class naturality are imported standard theorems in the written proof, not mechanized by the finite checker. No all-cycle annihilation or Hodge verdict is established.
