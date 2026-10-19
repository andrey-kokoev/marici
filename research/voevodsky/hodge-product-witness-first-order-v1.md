# First-order failure of the product-fiber divisor witness

## Fresh source and an admissible direction

Execute product-fiber-witness-deformation using the native period chart, not a new family. Write P for its period matrix to avoid confusing it with algebraic cycle supports. At the product origin P=0, u1,u2,u3 are holomorphic and u4,u5,u6 antiholomorphic for J0. Let u_j=dx_j+i dy_j and D=diag(1,1,3).

Choose the real path P(t) with its sole nonzero entry P_(1,2)=t (one-based indices: negative coordinate4 mixed with positive coordinate2). Then

    I-P(t)* D P(t)=diag(1,1-t^2,1),

which is positive for |t|<1. The chart formula J=A diag(iI,-iI) A^-1 gives an honest polarized Weil-family deformation; E and the lattice marking remain fixed. This path is a bounded local control, not the selected transcendental endpoint X.

## Differentiate the actual complex structure

For a degree-k form let D_J be the derivation applying J* to each one-form factor. Its eigenvalue on type(p,q) is i(p-q). For real degree-two classes, D_J=0 is precisely type(1,1); for degree six its kernel is type(3,3).

Differentiating the chart at zero gives, on native complex one-forms,

    dot J* u2 = -2i u4,
    dot J* u4 =  2i u2,

with all other dot J* u_j zero; conjugate forms transform by conjugation. This is the commutator derivative of the chart, not a freely chosen variation of the Hodge operator.

At finite t put c=(1+t^2)/(1-t^2), s=2t/(1-t^2). On these two one-forms,

    J(t)*u2 = i c u2 - i s u4,
    J(t)*u4 = i s u2 - i c u4.

The remaining native eigenvalues stay as at J0. The exact rational controls at t=plus/minus 1/8 verify J^2=-1, E's type and the following first-order calculation.

## The actual divisor factors do not all remain Hodge

The retained product-fiber expression uses

    b_j=u_j wedge u_(j+3)=r_j+i s_j,  j=1,2,3.

The notation s_j here means the imaginary part of b_j, not the scalar s in the displayed finite-t matrix. At the origin all six rational classes r_j,s_j are type(1,1), hence divisor classes by Lefschetz(1,1).

The differentiated Hodge operator gives

    D_dotJ b1 =  2i u1 wedge u2,
    D_dotJ b2 = -2i u4 wedge u5,
    D_dotJ b3 = 0.

Taking real and imaginary parts yields

    D_dotJ r1 = -2 Im(u1 wedge u2),
    D_dotJ s1 =  2 Re(u1 wedge u2),
    D_dotJ r2 =  2 Im(u4 wedge u5),
    D_dotJ s2 = -2 Re(u4 wedge u5),
    D_dotJ r3 = D_dotJ s3 = 0.

The first four output forms are rational and linearly independent. Thus on the six-dimensional span of the displayed divisor factors, the infinitesimal Hodge-condition map has rank4 and kernel span(r3,s3). The first two complex b_j fail type(1,1) already to first order. At t=1/8 the exact operator also rejects all four corresponding real factors.

A family of line bundles with the fixed central Chern class would have a locally constant Chern class in the marked cohomology local system, and it must remain (1,1). Hence these four chosen divisor classes cannot be transported as line-bundle classes even infinitesimally along this direction. Allowing a different representative of the same class does not repair the Hodge-type failure. The two factors with zero derivative have only passed this particular test; in fact they remain type(1,1) along this path because their coordinates are untouched.

## The determinant class nevertheless stays Hodge

On the native six-dimensional u-space, J(t)* has three eigenvalues i and three eigenvalues -i. The induced derivation on its determinant U=u1...u6 is trace(J(t)*) times U, identically zero. Therefore

    D_J(t) R = D_J(t) I = 0

along the entire admissible path, where U=R+iI. Infinitesimally this is also visible in U=-b1 b2 b3: each derivative term has a repeated u2 or u4 and vanishes. Preservation of the total determinant type is compatible with failure of its degree-two factors.

The exact identity expressing R as a signed sum of divisor products at the origin remains an identity of flat cohomology classes. It does NOT remain a displayed product of divisor classes along this path. Another algebraic representative of R, if one exists, is not excluded by this computation. A cycle is not required to retain these particular factors or this presentation.

## Disposition and next independent test

Rejected at scope: transporting the known product-fiber divisor witness merely because its determinant class is flat and remains Hodge. Constructed: a legitimate infinitesimal family direction, four independent factor obstructions, and a preserved determinant class. This supplies no fixed-X nonalgebraicity theorem.

Next bounded test: compute the simultaneous Hodge locus of all six FIXED divisor factors in the full period chart. Determine its tangent space and, if possible, its exact equations, with diagonal period matrices as a positive control. This asks where the actual witness survives, not whether every possible witness is absent outside that locus. Keep the selected fixed period distinct from both the product point and this test path.

Verification uses rational exterior arithmetic, an exact chart-derived J(t), the first-order matrix and a rank calculation. Riemann projectivity and Lefschetz(1,1) are imported as in the original candidate note. No formal deformation of all codimension-three cycles or Hodge verdict is claimed.
