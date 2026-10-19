# Algebraic correspondence transfer realizes the joint-control classes

## Fresh task and the imported algebraic input

Execute joint-control-algebraic-correspondence-transfer on X_joint=A times B. This remains the specified joint-family control, NOT the original fixed sixfold X.

From the preceding primary-source audit, choose a rational cycle

    Gamma in CH^2(C times A)_Q,
    cl(Gamma)=gamma=f external p-e external q,

where Omega_A=u1 u2 u4=p+i q, omega_C=e+i f, and integral_C e f=1. Existence of Gamma uses the explicitly audited Markman fourfold theorem. We do not replace this algebraic input by a mere Hodge tensor, nor claim equations or a canonical representative for Gamma.

Let tau:C->C be multiplication by -i. It is an algebraic automorphism, with tau*e=f and tau*f=-e. Define the actual rational Chow class

    Gamma_prime=-(tau times id_A)*Gamma.

Its cohomology class is

    gamma_prime=e external p+f external q.

Both signs are part of the construction.

## A holomorphic projection with the correct conjugation

The inactive B has native coordinates3,5,6 with complex structure i,-i,-i. Define lambda:B->C by the coordinate5 projection followed in native real coordinates by conjugation:

    lambda*(e)=dx5,  lambda*(f)=-dy5,
    lambda*(omega_C)=conjugate(u5).

This map is holomorphic because the domain coordinate5 has the reversed complex structure. It respects the Gaussian lattice and is a homomorphism of projective abelian varieties, hence algebraic. It is a smooth projection with an abelian-surface kernel.

Define

    h:A times B -> C times A,  h(a,b)=(lambda(b),a).

This is smooth of relative dimension two. Flat pullback takes CH^2(C times A) to CH^2(A times B); no naive excess-intersection assumption is needed.

## Check the odd-degree factor-order signs

Set

    V=Re(Omega_A wedge u5)=p dx5-q dy5,
    W=Im(Omega_A wedge u5)=p dy5+q dx5.

Forms from C are written first in gamma. After pullback, moving the resulting degree-one B form past a degree-three A form contributes a minus sign. Consequently

    h*gamma=W,
    h*gamma_prime=-V.

For example lambda*f wedge p=(-dy5) wedge p=+p wedge dy5. Treating the factor order as sign-free would give incorrect cycle classes.

## Actual Chow expressions

The classes r3=Re(u3 wedge u6), s3=Im(u3 wedge u6) are rational integral (1,1) classes on B. By Lefschetz(1,1), choose divisor classes D_r,D_s in CH^1(B)_Q with those cycle classes. Pull them back to A times B, denoted by the same symbols.

Define in CH^3(A times B)_Q

    Z1= -h*Gamma_prime . D_r,
    Z2= -h*Gamma       . D_s.

These are compositions of licensed algebraic operations on an imported algebraic correspondence and actual divisor classes. Their cycle classes are

    cl(Z1)=V r3=K1,
    cl(Z2)=-W s3=K2.

To match the retained original coordinates, b1 b2=-Omega_A u5, and

    U=u1 u2 u3 u4 u5 u6=Omega_A u5 (u3 u6).

The sign in the last identity comes from moving u5 past u3 together with the corresponding permutation in U. Hence

    R=V r3-W s3=K1+K2,
    I=W r3+V s3.

It follows that

    Z_R=Z1+Z2,
    Z_I=h*Gamma . D_r-h*Gamma_prime . D_s

are rational algebraic cycle classes with cohomology classes R and I on X_joint.

No individual effective representative is asserted. Rational signs and products in the Chow ring of the smooth variety are permitted by the original Hodge problem. Different choices of Gamma or of divisors with the same cycle class leave these cohomological conclusions unchanged; a canonical Chow class is not asserted.

## What the control now establishes

At the specified algebraically independent pair, the previous exact Picard/product certificate proved K1,K2 and every nonzero combination lie outside the twenty-dimensional divisor-product span. They are now nevertheless proved algebraic by the above theorem-backed expressions. Thus this is an actual NON-DIVISOR algebraic control, not only a failure to find divisor witnesses.

The same pointwise construction works whenever the retained A times fixed-B source and theorem hypotheses hold. No relative cycle family over the parameter space is constructed. In particular nothing here transports Z_R to the original selected period with full off-diagonal matrix, where the active/inactive abelian product and lambda need not exist.

This rejects interpreting axis-witness incompatibility, odd active degree or failure of divisor generation as universal nonalgebraicity detectors. It does not establish the Hodge conjecture for the original fixed X or all degree-six classes even on this control.

## Next executable extension and its gate

The next test is to allow BOTH threefold factors to vary while preserving signatures(2,1) and(1,2). The fixed inactive elliptic projection used above may disappear. Replace it, if justified, by a second codimension-two elliptic correspondence and compose the two correspondences over C. Compute the Tate/CM choices, Hermitian discriminants, factor-order signs and pushforward degree. In particular the second fourfold may be nonsplit, so its coverage must use the audited ALL-fourfold statement rather than silently reusing a split-only theorem.

This is a strictly larger decomposable control family, not a substitution for the original target. Verification tests exact pullbacks, CM signs and all four degree-six identities; it retains imported-theorem dependence rather than presenting finite exterior arithmetic as proof of cycle existence.
