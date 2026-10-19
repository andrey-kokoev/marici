# An actual nonzero nodal residue killed by ambient pushforward

## Fresh task and retained source

Execute known-cycle-nodal-residue-control. Keep Z=CI(kE,kE,kE) in the fixed X, and a general sufficiently high-degree containing divisor D of class mE. Its N=2160 k^3(m-k)^3 nodes all lie on Z. Put Sigma=Sing(D), U=D minus Sigma. The previous construction supplied

    H^4(U) --res--> Q^N --gamma--> H^5(D),
    K_D=ker gamma,
    psi_D:K_D -> H^6(X)/(E cup H^4(X)).

We compute a real cycle input to both maps, not their full ranks.

## Keep the subvariety while normalizing the node

At each node choose tangent coordinates x on Z and normal coordinates y, with

    f(x,y)=sum_i y_i g_i(x,y), Z={y=0}.

The matrix partial g/partial x at the node is invertible by the prior normal-transversality proof. Hence the change of variables (x,y)->(g(x,y),y) is locally biholomorphic. It puts the PAIR in the exact form

    D: sum_i x_i y_i=0,   Z: y=0.

This is stronger than normalizing f alone: it retains Z as a maximal isotropic linear three-plane in the quadratic cone. The germ of Z is therefore not lost in an arbitrary Morse coordinate change.

## The projective quadric and the nonzero link class

Projectivizing the cone gives a smooth quadric Q^4 in P^5. The plane Z projectivizes to one ruling plane P^2. Let a,b in H^4(Q^4,Q) denote the two ruling-plane classes and h the hyperplane class. Standard quadric cohomology gives

    H^2(Q^4,Q)=Q h,
    H^4(Q^4,Q)=Q a direct_sum Q b,
    h^2=a+b,
    integral a^2=integral b^2=1, integral ab=0.

The self-intersection can also be checked from the normal sequence of P^2 in Q^4: c(N)=(1+h)^3/(1+2h), whose degree-two coefficient is 1. Together with h^2=a+b and hyperplane degree one on each plane, this gives the displayed intersection matrix. In particular neither a nor b is a multiple of a+b.

The link K is the circle bundle of O_Q(-1); its Euler class is -h. The circle-bundle Gysin sequence, with H^3(Q^4)=0, gives

    H^4(K,Q)=H^4(Q^4,Q)/Q(a+b).

Thus the pullback of a is NONZERO, the pullback of b is its negative, and the pullback of the primitive class a-b is twice the pullback of a. Losing this factor of two would conflate a ruling-plane residue with its primitive normalization.

On the punctured cone the threefold Z is the inverse image of that ruling plane. Its codimension-two cycle class is therefore the pullback of a. The cone connecting isomorphism

    delta_p:H^4(K_p,Q) -> H^5_p(D,Q)

takes it to a nonzero local residue. Fix the basis e_p of the latter one-dimensional group to be delta_p of this particular ruling-plane class. This explicitly specifies the local generator and connecting sign; it does not pretend there is a canonical ordering of the two rulings independent of Z.

## Both actual global map values

The smooth locus contains the closed algebraic subvariety Z minus Sigma of codimension two. Let h_Z in H^4(U,Q) be its cycle class, equivalently the Poincare dual of its Borel-Moore fundamental class. The calculation at EVERY node gives

    r_Z=res(h_Z)=sum_(p in Sigma) e_p != 0.

In these Z-adapted bases its coordinate vector is (1,...,1). Other independent generator choices change the corresponding signs, not nonvanishing. Exactness, not an independence assumption, gives

    gamma(r_Z)=0.

Under the previously typed support pushforward Phi_D, the class h_Z maps to cl_X(Z)=k^3 E^3. This belongs to E cup H^4(X), so

    psi_D(r_Z)=0.

Consequently the actual K_D is nonzero and ker psi_D is nonzero. The nodes support a genuine global residue relation which contributes NO ambient primitive class. No rank-one or spanning claim about K_D follows yet.

## A supplied algebraic cycle with nonzero support class but zero ambient Chow class

Choose q sufficiently large and two general divisors A_1,A_2 in |H^q|, each avoiding the finite set Sigma, with proper intersections. Let Y=D intersect A_1 intersect A_2. It is an algebraic threefold cycle contained in U. Its residue is zero because it misses every node. Its ambient class is m q^2 E^3.

The rational cycle on D

    C=Z - (k^3/(m q^2)) Y

has the same nonzero residue r_Z, so its Borel-Moore class in H_6(D,Q) is nonzero. But its pushforward to X is zero even in CH^3(X)_Q: both complete intersections are the stated scalar multiples of c1(H)^3 in the Chow ring. In particular its ambient cohomology class is zero.

This is actual algebraic geometry on the fixed X, not a formal countermodel. It shows explicitly why a witness that retains the chosen support and its local residues need not descend to the ambient cycle class. The support pushforward is not injective. This does not imply that C is rationally trivial inside the singular divisor D, nor that every support class behaves this way.

## Disposition and next independent calculation

The nonzero local contributions and both global map values have now been computed on a supplied algebraic cycle. A nonzero residue relation cannot by itself be used as an obstruction to algebraicity or as a nonzero Weil component. No algebraic representative of alpha has been constructed or excluded.

Next bounded test: compute the FULL rank of K_D for this specific complete-intersection envelope family using the blowup of X along Z. Compare the smooth strict transform, its exceptional fibers over the nodes, and the blowup over U. Track purity degrees before subtracting cohomology dimensions. This could decide whether r_Z exhausts the residues for this family rather than leaving a merely unknown extra sector. It does not assume that arbitrary supports of alpha are complete intersections.

Verification includes the exact quadric intersection and quotient matrices, the primitive factor of two, fixed-polarization intersection numbers and rational Chow coefficient cancellation. The quadric cohomology, circle-bundle Gysin and cycle-class naturality are standard imported geometry supporting the written argument, not conclusions of the finite checker. No proof-assistant certification or Hodge verdict is claimed.
