# A genuine quadratic obstruction invisible to the control semiregularity map

## Fresh task and fixed ambient source

Execute control-bundle-quadratic-obstruction. Keep X fixed, with L ample and Z the smooth zero locus of a regular section s of E=L tensor C^3. Write B1=C[t]/(t^2) and B2=C[t]/(t^3). These are infinitesimal deformations INSIDE the fixed X, not ambient Kodaira-Spencer directions. The previous positive lift along polarized ambient deformations is unchanged.

## An actual bundle deformation and its nonzero obstruction

Choose independent invariant (0,1)-forms u,v on the abelian sixfold. Their classes are independent in H^1(O_X), and u wedge v is nonzero in H^2(O_X)=Lambda^2 H^1(O_X). Set

    A=E_12, B=E_21, a=A u+B v.

Since End(E)=O_X tensor Mat_3(C), the operator D1=bar-d_E+t a is an integrable Dolbeault operator modulo t^2. It defines a locally free first-order holomorphic deformation E1 of E. Proper complex GAGA identifies this with an algebraic deformation over B1.

An extension D2=bar-d_E+t a+t^2 b would require

    bar-d b + a wedge a = 0,
    a wedge a = [A,B] u wedge v
                = diag(1,-1,0) u wedge v.

This is the primary obstruction (equivalently one half of the graded bracket [a,a]). It is nonzero in H^2(End E): the invariant scalar two-form represents a nonzero class, and its diagonal matrix coefficient is nonzero. Thus it cannot be removed by a second-order correction b or a first-order gauge change. E1 does not extend over B2.

Its trace is zero. Under the previous Koszul identification and semiregularity formula, l^2 tr(a wedge a)=0. This is a geometric cohomology obstruction, not merely a nonzero numerical matrix.

## The defining section DOES lift at first order

H^1(X,E)=0 by ample-line-bundle vanishing. Thus the equation

    bar-d s1 = -a s

has a solution: its right side is closed and has zero cohomology class. The section s+t s1 is holomorphic for D1. Its zero locus Z1 is a flat embedded B1-deformation of Z, since a regular section on the central fiber remains a relative regular sequence over the Artinian base. No smoothness assumption on a hypothetical Weil-cycle representative enters this construction.

Nonextendability of E1 alone would not yet prove nonextendability of Z1. The comparison below is essential.

## Obstruction-compatible comparison, not a vector-space analogy

For pairs (E,s) on fixed X, the standard deformation complex is

    C=[End(E) --f maps to f(s)--> E]

in degrees0,1. Its hypercohomology in degrees1 and2 supplies tangent and obstruction spaces. The evaluation on the zero locus defines a morphism of complexes

    C -> i_*N[-1],

where N occurs in degree1. This is the tangent/obstruction morphism induced by taking the regular zero locus. It is compatible with primary obstruction classes, not just with dimensions.

Here is the local reason for that compatibility. Given first-order pair data, choose arbitrary second-order local transition and section lifts. Their transition defect is a two-cocycle beta in End(E); the section defect is an E-valued one-cochain eta satisfying d eta=beta(s), with compatible signs. Restricting eta to Z gives a normal one-cocycle because s|Z=0. It is exactly the mismatch of the lifted local zero equations, hence the embedded Hilbert obstruction. Its connecting image in H^2(I_Z E), and then H^2(End E), is beta. Changes of chosen lifts add coboundaries and leave these classes unchanged.

In this control the induced obstruction map is an isomorphism. Indeed its kernel complex is

    [End(E) -> I_Z E],

quasi-isomorphic to F=ker(End(E)->I_Z E) in degree0. Koszul gives

    0 -> E tensor Lambda^3 E* -> E tensor Lambda^2 E* -> F -> 0.

These first two terms are sums of L^(-2) and L^(-1); consequently H^q(F)=0 for q<5. Thus the comparison on tangent and obstruction hypercohomology is an isomorphism. Also H^1(E)=H^2(E)=0 identifies the pair obstruction space with H^2(End E). This supplies the inverse of the earlier normal connecting identification delta, now WITH its obstruction-operation compatibility.

For the specific Z1 constructed above, therefore,

    delta(ob_Hilb(Z1/B2))=[A,B] [u wedge v] != 0.

Z1 has no embedded extension over B2, although its semiregularity image is zero. This is an actual obstructed Hilbert tangent direction in a supplied, already algebraic complete intersection.

## How much of the invisible space is attained?

The LINEAR SPAN of these quadratic obstruction values is the entire

    sl_3(C) tensor H^2(O_X), of dimension120.

Indeed commutators span sl_3: [E_ii,E_ij]=E_ij for i!=j, and [E_ij,E_ji]=E_ii-E_jj. Decomposable wedges of invariant one-forms span H^2(O_X). For each such pair of matrices/forms the first-order section lifts by the same H^1(E)=0 argument, and the comparison above transfers the obstruction to an actual Hilbert direction.

This is a span statement, NOT a claim that every vector of the 120-dimensional space is a single quadratic obstruction value. The distinction matters for the geometry of the tangent cone.

## No contradiction with polarized lifting or with algebraicity

Previously, varying the ambient abelian variety gave first-order normal obstruction values in scalar matrices. Here X does not vary at all: a chosen vertical Hilbert tangent direction is obstructed at the NEXT order, and its value is trace-free. These are different deformation problems and different orders.

The constant deformation of Z still exists, as do the previously constructed polarized-family lifts with other tangent choices. Its class l^3 is already algebraic and stays Hodge. An obstructed selected deformation does not imply nonexistence of other representatives or of another lifting direction. Nothing here proves or refutes algebraicity of the original Weil class R.

## Next bounded construction

Determine whether the formal local deformation problem is captured by commuting six-tuples of 3 by 3 matrices, together with smooth section parameters and the appropriate gauge quotient. On an abelian variety, invariant Dolbeault forms are a candidate multiplicative quasi-isomorphism for the End(E) deformation algebra. Verify that comparison and the zero-locus/gauge conditions before promoting the computed quadratic obstruction to a complete formal model. Do not infer all-order sufficiency from the quadratic equations alone.

Verification checks the exact commutator, exterior-cohomology model, trace and span dimensions. Dolbeault deformation theory, GAGA, regular-section flatness and the obstruction-compatible pair-to-Hilbert construction are the written geometric inputs, not consequences of finite matrix checks. No proof-assistant certification or Hodge verdict is claimed.
