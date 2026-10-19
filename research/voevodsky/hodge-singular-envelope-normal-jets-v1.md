# Generic singular envelopes: transverse normal zeros are ordinary double points

## Fresh task and fixed control

Execute singular-envelope-normal-jet-control from the freshly read workbench. Fix the same polarized sixfold X, and a polarization line bundle H with c1(H)=E. Choose k with H^k very ample and let Z be a smooth complete intersection of three general sections of H^k. Thus dim Z=3, [Z]=k^3 E^3 and N_(Z/X)=(H^k|Z)^3. Z is known algebraic and is not a representative of alpha.

We prove that for every sufficiently large integer m, a general member D of |I_Z tensor H^m| is smooth away from Z and has exactly

    N=2160 k^3(m-k)^3

singular points, all ordinary double points on Z. The phrase sufficiently large is justified by coherent-sheaf vanishing/generation, not by an asserted numerical bound.

## Global generation and the missing lifting hypothesis

Write I=I_Z and M=H^m. The conormal exact sequence is

    0 -> I^2 tensor M -> I tensor M
      -> (I/I^2) tensor M|Z -> 0,

where the last term is a sheaf on Z extended to X. Its bundle on Z is

    B=N*_(Z/X) tensor M|Z = (H^(m-k)|Z)^3.

Serre vanishing gives H^1(X,I^2 tensor M)=0 for m sufficiently large. Hence

    H^0(X,I tensor M) -> H^0(Z,B)

is surjective. This is the actual normal-derivative map: its value on a defining section s is sigma_s, and a point on Z is singular on D=(s=0) exactly when sigma_s vanishes there.

For sufficiently large m, B is globally generated. In characteristic zero a general section of a globally generated vector bundle on a smooth variety has a smooth zero scheme of the expected codimension when nonempty: the universal evaluation is a submersion, followed by generic smoothness. Here rank B=dim Z=3, so its zeros are isolated and reduced. The top Chern degree is positive for m>k, so a nowhere-zero section is impossible and this generic zero scheme is nonempty. Its length equals the top Chern degree.

Surjectivity of the normal-derivative map ensures that this open generic condition is achieved by general global defining sections; we are not assuming arbitrary local normal data can always be lifted.

Also I tensor M is globally generated for sufficiently large m. Away from Z this is the line bundle M, so the associated linear system has no base points there. Bertini in characteristic zero gives smoothness of a general member away from Z. These two nonempty generic open conditions on the same parameter space may be imposed simultaneously. Bertini is NOT used to claim smoothness on the base locus.

## Local Hessian at a transverse zero

Choose holomorphic coordinates (x1,x2,x3,y1,y2,y3) centered at a zero of sigma_s, with Z defined by y=0. Locally

    f(x,y)=sum_i y_i g_i(x,y),
    sigma_s(x)=(g_1(x,0),g_2(x,0),g_3(x,0)).

All g_i(0,0)=0. Transversality means the matrix A_ij=partial g_i/partial x_j at zero is invertible. The Hessian of f has block form

    Hess(f) = [ 0    A^T ]
              [ A     B ],

where B is some symmetric 3 by 3 matrix. There are no tangent-tangent terms because f(x,0)=0 identically. For EVERY B,

    det Hess(f)=(-1)^3 det(A)^2 != 0.

For example interchange the two blocks of three rows, then use the resulting block triangular matrix; the row permutation has sign (-1)^9. Thus the quadratic part is nondegenerate independently of the normal-normal second derivatives. By the holomorphic Morse lemma, f is analytically equivalent to a nondegenerate quadratic form in six variables. D is a complex five-dimensional hypersurface with an ordinary double point (Milnor number one).

If A is singular, any nonzero x in ker A makes (x,0) a Hessian kernel vector. A nontransverse zero therefore cannot be declared a node by this argument. The top Chern number alone had not supplied the necessary invertibility.

## Count, scope and algebraic control

Transverse zeros each have multiplicity one, so

    #Sing(D)=integral_Z c3(B)
            =(m-k)^3 integral_Z E^3
            =2160 k^3(m-k)^3.

There are no additional singularities away from Z for the general choice above. This is now a count and a local analytic classification, not only an obstruction to smoothness. It is a theorem about general sufficiently high-degree containing divisors, not every member of the linear system and not every integer m>k.

At degree m=k, the first defining divisor of Z is a smooth containing divisor, as already checked. The new high-degree nodes are compatible with [Z]=k^3 E^3 throughout. Thus positive node counts, nontrivial local Milnor fibers and necessary singular envelopes occur on a supplied algebraic class. None alone detects failure of algebraicity of alpha. No transfer to an unknown support of alpha is made.

## Next executable geometric interface

The next test is the local-to-global support interface for these nodal envelopes. Compute the rational link groups of a complex five-dimensional ordinary double point and the localization sequence comparing H^4(D), H^4(D minus Sing(D)) and the pointwise local terms. Determine which local classes survive global relations before identifying any extra degree-six support image in X. N nodes do not automatically give N independent global obstruction classes.

Verification consists of the written Serre/Bertini/transversality argument, the general determinant proof, exact Hessian controls including a nontransverse hostile, and the inherited fixed-polarization intersection number. Serre vanishing, generic smoothness, the zero-section Chern formula and holomorphic Morse lemma are imported standard results. No numerical threshold, explicit global equation, global vanishing-cycle independence or Hodge verdict is claimed.
