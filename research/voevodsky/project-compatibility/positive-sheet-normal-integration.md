# Positive-sheet normal Taylor jets commute with the restored loop integral

## Fresh starting point and type distinction

Fresh graph state selects the restored route density. Read `research/benincasa/checkers/additive_contact_normal_grade.rs`: it explicitly marks its additive model RETRACTED (Entry2143). We retain the product density, not the old zero-mixed-jet model.

Use ledger2136's actual coordinate nu_i=P_i^2-X_i^2. Fix nonzero momentum vectors summing to zero, with P_i their positive magnitudes and distinct loop norm centers. Keep the routed y_e(l) fixed and vary the site coefficients off the physical locus by

    X_i(nu_i)=+sqrt(P_i^2-nu_i).

At nu0 this agrees with the positive physical slice. These are off-shell normal coefficient variations, not independent variations of physical on-shell momenta.

Let

    D_nu(l)=1/[y12 y23 y31 product_i(X_i(nu_i)+s_i(l))],
    s1=y12+y31, s2=y12+y23, s3=y23+y31,
    I(nu)=integral_R3 D_nu(l) d3l.

The previous route-density note establishes D0 in L1: r^-6 at infinity and at worst1/rho at each distinct norm center.

## Uniform domination on a complex normal neighborhood

For |nu_i|<P_i^2/2 on the positive square-root branch,

    Re X_i >= P_i/sqrt(2).

Since s_i>=0,

    |X_i+s_i| >= (P_i+s_i)/sqrt(2),
    |D_nu(l)| <= 2sqrt(2) D0(l).

The exceptional points y_e=0 have measure zero and retain the common integrable local bound. The bound is uniform in the normal parameters, not merely pointwise convergence.

Consequently dominated holomorphic integration makes I holomorphic on this polydisc. Cauchy estimates on smaller polydiscs give integrable bounds for every finite normal derivative. Hence

    [nu^alpha] I(nu) = integral [nu^alpha] D_nu(l) d3l

for every finite multi-index alpha. This is an actual comparison/integration result in the L1 topology for the stated restored representative. It is a written analytic proof, not a machine-formalized one.

## Explicit product jets

Write ell_i=P_i+s_i. At nu0,

    partial_i D = D0/(2P_i ell_i),
    partial_i partial_j D = D0/(4P_i P_j ell_i ell_j), i!=j,
    partial_i^2 D = D0[1/(4P_i^3 ell_i)+1/(2P_i^2 ell_i^2)].

These are derivatives, not Taylor coefficients divided by factorials. In particular the mixed second derivatives are positive and integrable. The product structure cannot be replaced by the retracted additive model. Their positivity does not by itself prove full matrix rank of a physical observer.

## Why this does not establish the singular contact grade

The algebraic equation nu_i=0 includes BOTH X_i=+P_i and X_i=-P_i. On the positive sheet, X_i+y_a+y_b cannot vanish and the above local period is holomorphic. A discriminant equation alone is not evidence of a pinch of this chosen cycle.

On the negative sheet, X_i=-P_i and the triangle inequality y_a+y_b>=P_i can be saturated along the segment between the norm centers. The domination argument fails there. That is precisely where a continued chain, local vanishing-cycle term or regulator analysis can matter.

Thus ordinary normal Taylor extraction on the positive sheet is now justified, but it has NOT been identified with the ledger's singular relative-Landau/contact readout. The restoring factor H from the previous note has not become an inverse to that singular grade. No equality between positive-sheet Taylor jets and negative-sheet residues is claimed.

## Programme decision

Freeze the positive-sheet Taylor/integration comparison as a proved scoped result. Next construct the continuation from this holomorphic germ to the negative-sheet threshold with an explicit approach prescription, and compute the local nonanalytic term. This is the remaining branch-sensitive comparison, not an unspecified failure of integration at every nu0.

The operator-lift and owner complex-typing handoffs remain open and separate; no owner artifact is changed.

## Verification

`uv run --with sympy python research/voevodsky/project-compatibility/check_positive_sheet_normal_jets.py` checks the derivative formulas, nonzero mixed jet, domination arithmetic at rational samples, and a segment witness distinguishing the two sheets. Finite checks support but do not replace the written holomorphic dominated-integration argument.
