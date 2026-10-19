# Retaining rational-equivalence witnesses in descent

## Question and source construction

Continue the actual Zariski cycle restriction test by retaining the witnesses erased by local Chow quotients. SCC obligations: restriction, overlap compatibility and compatibility of witness changes. Coefficients are Q throughout unless a concrete integral control is stated.

For a smooth irreducible complex variety X and nonempty open U, define

    R^p(U) = direct_sum_{W in U^(p-1)} C(W)^* tensor_Z Q,
    C^p(U) = Z^p(U)_Q,
    d: R^p(U) -> C^p(U).

For a generator (W,f), d is the principal Weil divisor of f on W, pushed into U. For singular W this uses the usual valuations on its normalization and proper pushforward of the divisor. The group law in C(W)^* is written additively after tensoring. In particular [fg]=[f]+[g], not f+g as rational functions. Open restriction commutes with d. Its cokernel is CH^p(U)_Q by the definition of rational equivalence. These are actual source operations, not matrices fitted to a desired detector.

This two-term complex places R^p in degree -1 and C^p in degree 0. It is a FIRST witness-retaining presentation, not a claim that two terms compute motivic cohomology or all higher descent in p>1.

## Overlap and witness equations

Choose local cycles z_i and overlap witnesses f_ij with

    d f_ij = z_j - z_i.

On a triple overlap the compatibility residual is

    k_ijk = f_jk - f_ik + f_ij,
    d k_ijk = 0.

Thus the residual lives in ker(d), not in the cycle group. Adding a kernel-valued overlap cochain h_ij changes k by delta h. Changing representatives using local witnesses g_i changes

    z_i' = z_i - d g_i,
    f_ij' = f_ij - (g_j - g_i),

and leaves k unchanged. These equations follow from d delta = delta d and delta squared = 0. They locate a possible obstruction to a coherent lift of a SPECIFIED local matching datum; a nonzero representative k is not itself a choice-independent obstruction. One must quotient by allowed witness changes and, in a longer complex, include the actual next boundary map.

Every actual global cycle supplies z_i by restriction and f_ij=0. It therefore supplies a coherent object in this first presentation in every codimension. This is a universal necessity statement for supplied cycles, not a construction of such local z_i from alpha.

## The P1 control recovers exactly what the quotient erased

Let U0=P1 minus infinity with coordinate t and U1=P1 minus zero with coordinate u=1/t. For D=[0], its restrictions are z0=[0] and z1=0. They agree on G_m, so initially f01=0 in additive witness notation.

Use g0=[t] and g1=0. Their divisors are z0 and z1 respectively. The witness change yields

    z0'=z1'=0,
    f01'=[t].

The overlap function t is invertible on G_m and has zero divisor there. It is not a unit on U0. Units on either affine chart are constants; units on G_m are c*t^k. Hence the exponent k survives admissible changes of trivialization on the two charts. The residual transition exponent 1 represents a degree plus or minus one line bundle according to convention, while the local Chow-class pair is (0,0).

Discarding f01' collapses this object to the zero divisor's local readout. Retaining it recovers the global degree distinction. There is no triple-overlap obstruction for the two-chart example; the lost information is a transition class, not a failed triple cocycle.

## Why codimension one closes

On a smooth irreducible variety the sheaf sequence

    0 -> O_X^* -> K_X^* -> Div_X -> 0

is exact: regular local rings are factorial, so Weil divisors are locally principal. Tensoring over Z with Q preserves exactness. Consequently the two-term rational divisor complex above is quasi-isomorphic to (O_X^* tensor Q) placed in degree -1. With that convention its hypercohomology in degree zero is H^1(X,O_X^* tensor Q). No unproved interchange of tensoring and sheaf cohomology is needed for the explicit integral P1 calculation.

For the finite P1 chart calculation, the quotient of overlap units by chart units has exponent group Z, or Q after rationalization. This establishes the control directly. Algebraic line-bundle descent and the exponential sequence explain how the retained transition data feed the usual divisor class; merely taking local degree-two cohomology groups would discard the overlap contribution.

These are imported standard sheaf/Picard facts, not formalized here. The source complex itself has been explicitly typed and its equations are checked.

## Higher codimension: the exact next constructor

For p=3, R^3 has rational functions on codimension-two supports and d lands in codimension-three cycles. The overlap kernel now contains relations among those principal divisors. It cannot simply be renamed O_X^*, nor can every kernel element be declared a missing algebraic filler.

A concrete next comparison is with the higher cycle complex z^p(U,*): codimension-p cycles on U times the algebraic simplex meeting faces properly, with alternating face boundary. Its degree-zero homology is CH^p(U). The challenge is to bind the rational-function witnesses to actual admissible degree-one chains, check their face signs and boundary, and then see which triple residuals are boundaries of degree-two chains. No assertion that the elementary two-term R^p presentation already IS the higher cycle complex is made. Closure under required moving/refinement operations must also be proved before global descent is claimed.

This is now a source-defined research route. It does not supply an algebraic local lift of alpha or a rational nonzero obstruction on that class. The fixed-target Hodge conclusion still requires independence from EVERY choice of local representative and witness, plus compatibility with rational signed combinations.

## Disposition and verification

Constructed: the rational-function boundary map, its restriction compatibility, overlap and witness-change equations, and an algebraic control recovering global degree from a retained transition. Rejected: interpreting local zero Chow readout as absence of gluing data, or identifying every nonzero overlap-kernel representative with a nonfillable boundary.

The checker uses Laurent monomial divisors at 0/infinity on P1, exact rational coefficients, representative changes and a three-chart formal witness fixture. The latter checks the general equations, not actual higher-codimension geometry. A deliberately erased transition loses degree. A deliberately altered overlap boundary fails its typed equation. The general geometric claims use the written standard facts, not extrapolation from these controls.

Next: construct the admissible degree-one higher-cycle chain for a rational-function witness and test its boundary with a known divisor. The independent quadratic-pairing task remains available. No Hodge or cotower-existence verdict is assigned.
