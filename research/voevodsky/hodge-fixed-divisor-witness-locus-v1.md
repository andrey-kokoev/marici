# Exact Hodge locus of the six fixed divisor factors

## Fresh task and retained marking

Execute fixed-divisor-witness-hodge-locus. Use the full positive-plane chart P in Mat_3(C) with I-P*DP positive definite, D=diag(1,1,3). The native forms are u_j=dx_j+i dy_j, and the fixed product witness uses b_j=u_j wedge u_(j+3)=r_j+i s_j for j=1,2,3.

We determine where ALL SIX specified real rational classes r_j,s_j remain type(1,1). This is not the locus where every possible algebraic representative of R exists.

## The exact criterion, not just its derivative

Let S_j=span_C(u_j,u_(j+3)) in the native cotangent eigenspace for K. For an endomorphism M of a vector space and independent u,v,

    D_M(u wedge v)=0

holds iff M preserves span(u,v) and its restriction to that plane has trace zero. To see necessity, decompose M u and M v into components in the plane and a complement. The coefficients of u wedge w and v wedge w for complement basis vectors w are independent, forcing the outside components to vanish; the remaining coefficient of u wedge v is the trace. Sufficiency follows by reversing the calculation.

Apply this to M=J* on the native six-dimensional u-space. Since D_J commutes with real conjugation, r_j and s_j are both type(1,1) iff D_J b_j=0. Requiring this for all j therefore makes all three S_j invariant. Their direct-sum decomposition implies the dual tangent planes V_j=span_C(e_j,e_(j+3)) are also invariant under J.

The positive eigenspace W of J is then the direct sum of W intersect V_j. Each V_j has Hermitian signature(1,1), so each intersection has complex dimension at most one; their dimensions sum to three. Thus each has dimension exactly one. The projection W->the positive coordinate C^3 is an isomorphism in this chart, and W is the graph of P. Consequently the graph splits along the three coordinate pairs, which forces P to be DIAGONAL.

Conversely diagonal P makes the chart matrix A and J preserve the three V_j. On each plane J has one eigenvalue i and one -i, so the dual restriction has trace zero. Hence all three b_j, and their real and imaginary parts, are type(1,1).

The exact simultaneous locus is therefore

    P=diag(z1,z2,z3),
    |z1|<1, |z2|<1, 3|z3|^2<1.

There are NO nonlinear off-diagonal solutions in this positive-plane chart. This conclusion is the linear-algebra argument for all periods, not extrapolation from the finite tests.

## Full tangent-space control

At P=0, differentiating the chart gives

    dot J* u_p = -2i sum_n conjugate(dot P_np) d_n u_(n+3),
    dot J* u_(n+3) = 2i sum_p dot P_np u_p.

Here d=(1,1,3); the weight on the conjugate upper block must not be omitted. Apply D_dotJ to all six r_j,s_j and regard the output as a six-tuple of real degree-two forms. The resulting real-linear map has domain dimension18, rank12 and kernel the six real diagonal directions. This agrees with the exact locus's complex dimension3 and complex codimension6. The earlier single-direction rank4 was a different map: it varied the input factor in a six-dimensional factor space while keeping the direction fixed. Those two ranks must not be conflated.

The checker constructs all eighteen derivatives from the native real commutator [dot A,J0], records zero diagonal columns, and verifies rank12 for the off-diagonal columns. Finite exact periods check complex diagonal examples and mixed off-diagonal hostiles, including the weighted third negative coordinate.

## Positive family and fixed-endpoint exclusion

On the diagonal locus the integral lattice and complex structure split along the three coordinate pairs. The corresponding polarized torus is a product of three projective abelian surfaces. All six fixed rational factors are Hodge divisor classes there by Lefschetz(1,1), so the identities expressing R and I as rational products of these divisors give actual algebraic witnesses throughout this subfamily. This is class-level existence; a universal choice of divisors or relative line bundles is not asserted.

The chosen fixed sixfold has every period-matrix entry nonzero by its explicit positive exponential coordinates. It is therefore outside this locus. This rules out these six fixed factor classes as a simultaneous divisor witness at that endpoint. It is consistent with the already known Picard-rank-one certificate; it does not strengthen that certificate into an all-cycle theorem.

In particular an alternative rational divisor basis, a different signed decomposition or a non-divisor codimension-three cycle is not classified by this locus. R and I remain Hodge on the full Weil family, not just on this subfamily.

## Next nonredundant test

The factor obstruction is now completely located. Next test the actual degree-six algebraic summands in the product identity for R: compute their first-order Hodge derivatives in the prior off-diagonal direction and the kernel of the map on their span. This distinguishes failure of a divisor presentation from failure to transport those supplied codimension-three cycle classes themselves, and measures cancellation in the total Hodge class. Even nontransportability of each chosen summand would not rule out a different total cycle realization.

Verification uses the written decomposable-form stabilizer proof, exact chart matrices and derivative rank tests. Hodge theory and Lefschetz(1,1) are imported standard facts. No smoothability theorem, universal cycle exclusion, proof-assistant certification or Hodge verdict is claimed.
