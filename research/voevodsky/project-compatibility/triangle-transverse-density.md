# Conditional transverse density for the reduced triangle

## Scope and fresh source interface

Continue the exact Cayley/Gram audit in `triangle-normalization-degeneration.md`. This is a local result for a candidate real nonnegative-volume representative with a,b>0, E down to0, c=E-a-b. It is NOT an identification of the physical analytically continued cycle. Retain the literal printed normalization pending the active owner request.

Freshly read applications.tex eq:Triangle: its loop measure is the product y_e dy_e, not flat Lebesgue measure in the lengths. Choose the canonical simplex labeling

    r=y12, s=y31, t=y23;
    base sides a=X1 between r,s; b=X2 between r,t; c=X3 between s,t.

This matches the pairs of incident loop edges at each source site. It supplies a local distance/denominator dictionary, not a global continuation prescription.

## Derive the Jacobian rather than assume a fixed domain

Use H,G,U,V,C,Hface from the preceding audit; write F=Hface and R=r^2,S=s^2,T=t^2. On H>0,F>0 set

    C=sqrt(H F) z,  -1<z<1.

The checked Gram identity gives

    K=H F(1-z^2)/(576a^2),
    T=b^2+R-[G U+sqrt(H F)z]/(2a^2),
    dT/dz=-sqrt(H F)/(2a^2).

Since r dr s ds t dt=(1/8)dR dS dT, the positive measure density is

    sqrt(H F)/(16a^2) dR dS dz.

The coordinate reverses orientation in T. These formulas use positive density; an oriented physical cycle still needs its independently sourced orientation/transport. The exact checker verifies dC/dt=-4a^2t, the underlying polynomial Jacobian identity.

## Full local density cancels the apparent fractional E power

For fixed regular epsilon, gamma=-1/2+epsilon, the literal source normalization is kappa0=C(d)(H/16)^(1-epsilon). Including K^gamma, the Jacobian and the displayed1/E gives

    L(a,epsilon) * (H/E) * F^epsilon * (1-z^2)^(-1/2+epsilon)
       dR dS dz,

where, with consistent positive-real bases and the chosen powers,

    L=C(d)*16^(epsilon-1)*(576a^2)^(1/2-epsilon)/(16a^2).

Indeed the total H exponent is (1-epsilon)+(-1/2+epsilon)+1/2=1. Thus the earlier fixed-coordinate prefactor estimate E^(-epsilon) is NOT the pulled-back period density. The shrinking direction and the twist both matter.

This cancellation is conditional on the literal normalization. It does not validate that convention physically or compare different continuation sheets.

## The remaining source denominators on the regular patch

Let A_E be the full rational factor in eq:Triangle after removing1/E. In this labeling,

    q1=r+a+s, q2=r+b+t, q3=s+c+t,
    q12=a+b+s+t, q23=b+c+r+s, q31=c+a+r+t,
    A_E = [ (1/q23+1/q31)/(E+r)
           +(1/q31+1/q12)/(E+t)
           +(1/q12+1/q23)/(E+s) ]/(q1 q2 q3).

At E0 and F>0, put x=U/(2a) and rho^2=F/(4a^2)>0. Then

    r=sqrt(x^2+rho^2),
    s=sqrt((x-a)^2+rho^2),
    t0=sqrt((x+b)^2+rho^2).

Strict triangle inequalities imply

    r+s>a, r+t0>b, s+t0>a+b.

Hence every displayed denominator of A0 is positive. On a compact patch with F bounded away from zero, these denominators have a common positive lower bound. The lifted lengths converge uniformly in z to r,s,t0 with O(sqrt(E)) error. Consequently A_E converges uniformly to A0, independently of z, on this patch. The checker includes one exact noncollinear fixture; the all-patch positivity argument is the strict triangle inequality, not numerical sampling.

## A local, explicitly delimited convergence result

Take a bounded smooth cutoff chi(R,S) compactly supported in F>0. For a fixed regular regulator with Re(epsilon)>-1/2, the z-weight is absolutely integrable. F stays bounded and bounded away from zero, A_E is uniformly bounded, and H/E tends to8ab(a+b). Dominated convergence therefore gives the localized candidate period limit

    L * 8ab(a+b) * Beta(1/2,epsilon+1/2)
      * integral chi(R,S) F^epsilon A0(R,S) dR dS.

The beta factor is the integral of (1-z^2)^(-1/2+epsilon) over[-1,1]. This proof concerns a fixed regulator, not removal of regularization or an interchange of epsilon and E limits.

In particular the local period is bounded and E times this localized period tends to zero. This is NOT a claim about a Laurent residue without establishing meromorphicity. It rules out a1/E divergence from this compact noncollinear patch under the stated representative/normalization hypotheses.

Any singular contribution for that same candidate family must evade at least one local hypothesis: approach F=0/length or denominator collisions, escape to unbounded ends, or involve a regulator/normalization/chain issue. The full physical period can additionally involve a different continued cycle or parameter map.

## Next discriminating test

Study the F=0 collinear stratum and its source denominator collisions, separating bounded intervals of x from infinity and retaining the regulator. This is an independently executable local task while the Benincasa/Nima normalization/continuation handoff remains open. Do not infer the global period residue from the regular-patch result.

## Verification

`python research/voevodsky/project-compatibility/check_triangle_normalization.py` passes the existing determinant checks plus the Jacobian derivative and affine exponent cancellation. Receipt: `triangle-normalization.json`, with stable source hashes. The coordinate, positivity and dominated-convergence arguments above are written proofs, not formalized analytic theorems or owner acceptance.
