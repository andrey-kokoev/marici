# A nontrivial algebraic unipotent control family with zero Weil readout

## Fresh task and formal arc

Execute control-unipotent-arc-algebraization. Fix the retained abelian sixfold X, an ample L=H^k, and a regular section s of E0=L tensor C^3 cutting out the smooth complete intersection Z0. Let u be a nonzero invariant class in H^1(O_X) and put

    J = [[0,1,0],[0,0,1],[0,0,0]],
    M_1=tJ, M_2=...=M_6=0.

J^3=0 but J^2!=0. These matrices commute identically, so the preceding formal model gives an all-order bundle arc. Its tangent J tensor u is nonzero. Since the section-to-Hilbert tangent comparison is an isomorphism, any compatible lift of s gives a nonconstant formal embedded deformation, not merely a change of bundle presentation.

## Proper formal existence, with its actual scope

Over A_m=C[t]/(t^(m+1)), the integrable operators bar-d_E+tJu give compatible locally free sheaves E_m. H^1(E0)=0 allows compatible section lifts through every small extension. Each zero locus is flat because the central section is regular.

On the projective scheme X_R with R=C[[t]], proper formal existence algebraizes the compatible coherent sheaves and their section maps. Local freeness and the regular/flat zero-locus properties hold near the special fiber by the usual local criteria. The bad locus is closed; its proper image in Spec R cannot be a nonempty closed subset avoiding the closed point. Hence these properties hold on the algebraized family. This supplies an algebraic family over the complete base Spec R.

This argument alone would NOT supply a specified finite-type curve over C or analytic convergence of arbitrarily chosen formal section coefficients. In this particular arc a stronger finite-type construction is available, as follows.

## Finite nilpotent exponentials give algebraic transition functions

Represent u by an algebraic additive Cech cocycle a_ij in O_X on an affine cover, with a_ij+a_jk=a_ik. Such a cocycle exists by coherent cohomology and GAGA; no numerical equations for X or for this representative are claimed.

On X times A^1 define

    g_ij(t)=exp(t J a_ij)
           =I+t J a_ij+(t^2/2)J^2 a_ij^2.

These are finite polynomial matrices, with inverse g_ji and determinant1. Since all exponents are scalar multiples of the same J,

    g_ij(t) g_jk(t)=g_ik(t)

exactly, not just modulo a power of t. They define an algebraic rank-three vector bundle mathcal U. Its standard flag is preserved, with all three associated graded line bundles O. Put mathcal E=pr_X^*L tensor mathcal U.

The Cech/Dolbeault comparison identifies its formal completion with the commuting arc above, using compatible signs for u. No noncommuting corrections are needed: changes of local scalar primitives exponentiate in the same nilpotent one-parameter algebra.

## An algebraic section and a smooth family near zero

The flag of mathcal E has three quotients pr_X^*L. For p:X times A^1->A^1, ample vanishing and base change give R^q p_* pr_X^*L=0 for q>0. The flag then gives R^q p_* mathcal E=0 for q>0 as well. Since the parameter line is affine, H^1(X times A^1,mathcal E)=0. The sequence obtained by multiplication by t therefore makes restriction of global sections onto H^0(X,E0) surjective.

Choose an algebraic section mathcal s restricting to the original s. Near the entire central fiber its zero locus is relatively smooth of dimension3, by regularity and transversality of s. Properness allows removing the closed image of the nonsmooth locus. Thus for a Zariski open V subset A^1 containing0, its zero locus

    mathcal Z -> V

is a smooth projective family of embedded threefolds in fixed X. Its first-order bundle class is J tensor u, so the prior tangent comparison proves this is not a constant embedded family near0. This does not assert that all its nonzero abstract bundle fibers are mutually nonisomorphic.

The completion of this chosen algebraic section gives one of the compatible formal section lifts above. We do not claim that every arbitrary formal choice of section coefficients is the completion of a section on a finite-type neighborhood.

## Exact K-theory and Chow computation

The preserved flag, including its quotient identifications, algebraizes with the transition functions. Consequently on X times A^1,

    [mathcal E]=3[pr_X^*L] in K0,
    c(mathcal E)=(1+l)^3,
    ch(mathcal E)=3 exp(l),

where l=c1(pr_X^*L). On X times V the regular zero section formula gives

    [mathcal Z]=c3(mathcal E)=l^3 in CH^3(X times V).

For every complex t in V, refined restriction yields

    [Z_t]=k^3 c1(H)^3 in CH^3(X).

This is an equality of Chow classes, stronger than constancy of their cohomology. The bundle is not asserted to split; its nonsplit extensions simply have the same additive K-class. Note that ch3(mathcal E)=l^3/2, whereas the zero-locus class is c3(mathcal E)=l^3. Interchanging these two invariants would give a wrong normalization.

## Weil-plane readout at the unchanged fixed source

In cohomology the class is k^3 E^3. The retained Hodge basis is (E^3,R,I), with cup matrix diag(2160,-32,-32). Hence the Weil-plane projector on this space is

    P_W(c)=c-(integral_X c E^3 /2160) E^3.

It gives P_W([Z_t])=0, and both pairings with R and I vanish. The corresponding rational Chow subtraction using c1(H)^3 also kills [Z_t], by the exact Chow equality just established.

Thus a genuinely moving, algebraic, all-order control family can be entirely invisible to the Weil readout. This does not imply the same for arbitrary cycles: the calculation applies to the supplied filtered bundle and its regular zero loci. The original R remains unresolved.

## Next bounded source-class audit

Test how far this bundle construction class can be enlarged without changing the readout. Audit the Chern-character formula for SIMPLE semihomogeneous bundles on the fixed Picard-rank-one X and track only explicitly justified operations such as sums, extensions, tensor products and duals. Determine whether their degree-three Chern characters/classes remain in Q E^3. Do not assert that all algebraic bundles or all cycles belong to that class, and do not apply the simple-bundle formula to arbitrary nonsimple inputs without a separate argument.

Verification checks the exact polynomial transition identity, nilpotence, characteristic-class normalization and retained cup/projector arithmetic. Formal existence, section lifting and regular-section geometry are written imported facts, not inferred from finite matrix checks. No original Hodge verdict or proof-assistant certification is claimed.
