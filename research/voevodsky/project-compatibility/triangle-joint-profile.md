# Joint energy–collinear profile and its angular boundary collision

## Scope

Freshly read the collinear obstruction and transverse coordinate formulas. Work conditionally in the same candidate real reduced family and literal source normalization, on a compact x interval inside0<x<a. Set w=E*lambda and retain z. This note derives a leading profile and its integrability; it does NOT yet identify the asymptotic of the finite-E integrated period or the physical continued chain.

Write s0=a-x, t0=x+b, h=8ab(a+b). Below s,t in profile coefficients mean s0,t0, not the finite-E lengths.

## Derive the actual denominator profile

From the exact transverse formulas,

    H=hE+O(E^2), G=-2ab+2(a+b)E-E^2,
    r^2=x^2+E lambda,
    s_E^2=(a-x)^2+E lambda,
    t_E^2=(x+b)^2
       +E[lambda-2(a+b)x/a-sqrt(h lambda)z/a]+O(E^2).

For bounded lambda and z these give

    q23/E → D23=1+a lambda/(2xs),
    q3/E → D3=A+B lambda-2 sqrt(A B lambda) z,
    A=bs/(at), B=(a+b)/(2st).

The square-root coefficient follows from h/(4a^2t^2)=4AB. Other denominators retain the nonzero limiting values from the preceding audit. The terms containing1/q23 dominate the six-term bracket, yielding, wherever D3 is nonzero,

    E^2 A_E → W=1/(4xst D23 D3).

This is a pointwise leading-profile statement, locally uniform away from its zeros; it is not a bound permitting integration across a zero.

## A finite-lambda angular collision

The exact identity

    D3=(sqrt(A)-sqrt(B lambda))^2
           +2 sqrt(A B lambda)(1-z)

shows D3 is nonnegative and vanishes only at

    lambda_star=A/B=2b(a-x)^2/[a(a+b)], z=1.

D23 remains strictly positive there. Thus energy scaling does not simply replace the double collinear pole by two uniformly positive denominators: a denominator collides with the angular endpoint. Replacing the z integration by the earlier denominator-free beta factor would miss this correlation.

## Matching the previously established overlap

For large lambda, uniformly in z,

    W ~ (a-x)/[a(a+b)] * lambda^(-2).

Multiplying by E^(-2) recovers the preceding w^(-2) coefficient. This is a consistency check between profiles, not a proof of uniform matching for the original integrals over a growing lambda domain.

## Profile density and its genuine convergence strip

The full local measure from the transverse calculation gives the FORMAL leading density

    2a L h (4a^2)^epsilon E^(epsilon-1)
      * lambda^epsilon (1-z^2)^(-1/2+epsilon) W dx d(lambda) dz.

The E power follows from F^epsilon supplying E^epsilon, dw supplying E, and A_E supplying E^(-2). The coefficient profile on lambda in(0,infinity), z in(-1,1) is absolutely integrable precisely for

    0 < Re(epsilon) < 1,

at fixed regular regulator and compact interior x. Proof:

- At lambda0, D3 tends to A>0 and D23 tends to1; the radial requirement is Re(epsilon)>-1.
- At infinity W is comparable to lambda^(-2), so the requirement is Re(epsilon)<1.
- Away from the collision, the angular endpoints require Re(epsilon)>-1/2.
- Near the collision put u=lambda-lambda_star and v=1-z. Smooth positive coefficients give D3 comparable to u^2+v. The absolute density is comparable to v^(Re(epsilon)-1/2)/(u^2+v). Integrating u on a fixed neighborhood gives order v^(Re(epsilon)-1), requiring Re(epsilon)>0.

These estimates are uniform on compact interior x intervals. At epsilon0 the collision produces a logarithmic divergence of the profile integral. This does not rule out analytic regularization or a cancellation with the regulator-dependent source normalization; neither has been performed here.

## What this does and does not establish

The profile is a concrete source-derived candidate for an E^(epsilon-1) layer, rather than an arbitrarily appended endpoint functional. Its coefficient integral exists in a nonempty regulator strip, and its overlap agrees with the E0-first obstruction.

It is NOT yet a proved finite-E period asymptotic. The collision location can move with E. Pointwise convergence away from it plus integrability of the limiting profile does not guarantee convergence of the integrals. The lambda domain also grows as E decreases. A uniform moving-collision comparison and tail bound are still required. Meromorphicity, regulator removal and any ordinary total-energy residue remain open.

Next local task: derive the exact finite-E geometric location of the q3 boundary collision and an integrable bound after recentering it. Treat the other interior interval, x endpoints and infinity separately. The Benincasa/Nima normalization/continuation request remains active; none of these conditional calculations supplies owner acceptance or a physical cycle.

## Verification

`check_triangle_joint_profile.py` passes27 exact rational collision/overlap fixtures and144 additional Taylor-jet fixtures. It checks the squared-root coefficient identity, the collision location, positivity of D23 there, and the large-lambda leading coefficient against the previous audit. `triangle-joint-profile.json` records source hashes and unchanged-source checks. The universal formulas and integrability argument are written mathematics; the finite fixtures are not a formal proof of all parameters or any integrated asymptotic.
