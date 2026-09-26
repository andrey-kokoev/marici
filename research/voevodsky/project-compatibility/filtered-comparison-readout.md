# Filtered comparison/readout contract: exact recovery is not completion stability

## Status and programme role

Fresh input: `triangle-readout-jet.md` and the selected triangle physical-readout gate. Generalize the verified scalar information-loss mechanism into a candidate contribution to construction–observation compatibility. This does not declare all sources scalar Laurent families, select a physical finite part, or replace the independently owned research programmes.

The triangle's independently confirmed local pole remains frozen. Its physical readout and source-owner handoff remain open; the present algebraic branch can proceed without that owner.

## Typed scalar contract

Fix a nonzero commutative unital coefficient ring A and a distinguished regulator coordinate t. Let

    G in t^a A[[t]], R=t^m u(t), u0 a unit in A,
    P=R G,
    J_N^a=t^a A[[t]] / t^(a+N+1) A[[t]], N>=0.

The valuation a is a lower bound, not a claim that every G has exactly that order. Multiplication by R induces an isomorphism

    M_R: J_N^a -> J_N^(a+m).

Both the shift m and the unit jet u modulo t^(N+1) are retained data. An unshifted boundary value is generally not the correct target object.

An independently selected coefficient readout [t^q]G, q>=a, needs N=q-a. Given P through degree q+m, starting at a+m, it is recovered by

    [t^q]G = [t^(q-a)](u^(-1) t^(-a-m) P).

Equivalently, for a=-p and a finite-part readout q=0, retain P from degree m-p through degree m and u through degree p. This means R through degree m+p. The triangle example has p=m=1: P0,P1 and R1,R2, exactly as previously derived.

This is an equality with a coefficient readout specified independently on G, not a definition of an arbitrary physical observation by transport.

## Proof and sharpness

Write v=u^(-1). Its finite coefficients are determined recursively:

    v0=u0^(-1),
    vn=-u0^(-1) sum_(i=1..n) ui*v_(n-i).

Convolution proves uv=1 modulo t^(N+1), establishing recovery. For two comparisons R=t^m u and S=t^n w, multiplication on shifted jets composes as M_S M_R=M_(SR); the inverse recoveries agree with inversion of the product. This is finite filtered comparison coherence, not a claim about arbitrary EP/PE constructor commutation.

The budget is sharp in general over the rationals. Changing G by t^q leaves all P coefficients below q+m unchanged but changes the selected readout. For N>0, holding P=t^(a+m) fixed while changing u from1 to1+c*t^N changes G from t^a to t^a/(1+c*t^N); the target degree q=a+N changes by-c. Thus insufficient observation jets OR insufficient comparison jets lose information. For N0 the leading unit itself must be known.

Special readouts or source restrictions can reduce this budget; the theorem is worst-case recovery for the declared coefficient class.

## A sufficient analytic stability condition

Now take scalar real or complex coefficients depending on an external parameter x, with the finite-jet maximum norm. Assume uniformly

    |u0(x)|>=c>0, and |ui(x)|<=M for1<=i<=N.

The inverse recursion gives

    sum_(i=0..N)|vi(x)| <= c^(-1)*(1+M/c)^N.

Indeed, if S_n is the partial sum, then |v_n|<=M*S_(n-1)/c and S_n<=(1+M/c)S_(n-1). Consequently errors in the supplied shifted P jet propagate to the chosen coefficient with at most this bound. If the comparison jet also varies, inversion is continuous on this uniformly invertible bounded region.

This is a sufficient finite-jet norm estimate. It is not a theorem that the physical sector supplies this norm, coefficient class or uniform bounds.

## Hostile control: adequate jet order is still insufficient at another boundary

Let the external parameter x approach0+, and set

    R_x=x*t,
    G_0=t^(-1), G_1=t^(-1)+1.

Their retained first P jets are(x,0) and(x,x). The jets approach the SAME zero vector as x→0, while the finite parts of G remain0 and1. At every x>0 the algebraic recovery is exact, but its norm grows as1/x. At x0 the leading coefficient ceases to be a unit.

Thus even the full algebraically sufficient first jet does not give a continuous boundary recovery in the ordinary unweighted jet norm. This falsifies the unrestricted claim that retaining the required number of coefficients alone repairs completion.

The triangle has precisely a relevant warning: its leading comparison coefficient is H(E)/3, which tends to zero at total energy0. On E bounded away from0 the scalar jet theorem applies over continuous coefficients with uniform bounds. It does not automatically extend to the joint energy/regulator corner. Logarithmic or other asymptotic coefficient behavior also requires its own analytic domain and bounds.

## Structural synthesis and admission gates

A source-authorized filtered comparison/readout contract must declare:

1. the regulator coordinate and coefficient class;
2. a valuation bound and comparison shift;
3. the independently intended readout;
4. sufficient observation AND comparison jets;
5. admissible composition maps;
6. the actual completion topology and control of the inverse comparison there.

Items1–5 can give exact algebraic recovery while item6 fails. Keeping them distinct links comparison coherence to completion-stable observability without asserting that a mathematical normalization choice is the physical prescription.

Next severe test: a multicomponent comparison whose leading coefficient is singular. Does the intended observation annihilate the lost directions, permitting descent even when the entire comparison is not invertible? A scalar-unit theorem must not be promoted to that case by analogy.

## Relation to existing independent synthesis

Freshly inspected Nima's `cross-sector-tate-naturality-must-be-filtered.md` and the opening architecture of `structured-ambiguity-invariant-readout-synthesis.md`. Filtration and invariant readout are already explicit programme themes; this branch is not a claim to originate or replace them. Its narrower addition is the sharp observation/comparison jet budget plus a quantitative inverse-control gate and a counterexample to automatic completion stability.

Nima's Tate contract specifically forbids inverting the normal, Rees parameter or integer3. Our unit hypothesis cannot silently authorize u0=3 over the integers, and a Laurent/valuation-shift model cannot be identified with that supported Rees construction without a supplied admissible comparison. Rationalizing would destroy the relevant Z/3 information. No cross-sector transformation is constructed by this note.

## Verification boundary

`check_filtered_comparison_readout.py` checks exact rational truncated inverses, recovery, composition, both jet-budget hostile controls, the norm-bound arithmetic and the external-parameter instability sequence. These are finite fixtures supporting the written general proofs, not machine formalization of physical completion or an infinite analytic theorem.
