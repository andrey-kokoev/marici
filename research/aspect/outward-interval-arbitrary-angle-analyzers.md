# Outward interval certificates for arbitrary-angle analyzers

## Question

How can source-declared analyzer angles outside a fixed algebraic number field be propagated into rigorous Jones-effect and SDP certificates?

## Claim boundary

This packet gives rational Taylor enclosures for real angles with magnitude at most one radian and a Lipschitz positivity-margin certificate. It does not implement general argument reduction, complex dispersive phases, or machine-directed rounding.

## Rational trigonometric enclosures

For rational \(x\) with \(0\le x\le1\), the alternating Taylor series have decreasing terms. Hence

\[
x-\frac{x^3}{6}+\frac{x^5}{120}-\frac{x^7}{5040}
\le\sin x\le
x-\frac{x^3}{6}+\frac{x^5}{120},
\]

and

\[
1-\frac{x^2}{2}+\frac{x^4}{24}-\frac{x^6}{720}
\le\cos x\le
1-\frac{x^2}{2}+\frac{x^4}{24}.
\]

All endpoints are rational. Negative angles follow parity. Wider domains require certified argument reduction before applying these formulas.

Interval addition and multiplication propagate these enclosures through a Jones matrix. For the linear analyzer vector

\[
u(\theta)=(\cos\theta,\sin\theta),
\]

the effect

\[
E(\theta)=u(\theta)u(\theta)^*
\]

is positive by construction. Its entries receive rational interval enclosures. The analytic identity \(\sin^2\theta+\cos^2\theta=1\) establishes exact normalization; naive independent interval arithmetic generally encloses rather than proves that identity.

## Separation of structural and interval proofs

Structural identities should be retained symbolically:

- \(E=uu^*\) proves positivity;
- \(\|u\|=1\) proves projector normalization;
- unitary conjugation preserves effects.

Intervals then bound numerical entries and deviations. Requiring interval multiplication alone to rediscover correlated identities introduces dependency inflation and may produce inconclusive residuals.

## Angle uncertainty and SDP margins

For rank-one two-mode analyzer projectors,

\[
\|E(\theta)-E(\theta_0)\|
=|\sin(\theta-\theta_0)|
\le|\theta-\theta_0|.
\]

If a nominal dual slack has certified minimum eigenvalue \(\gamma>0\), analyzer terms with nonnegative multipliers \(w_j\) and angle radii \(r_j\) retain positivity whenever

\[
\sum_jw_jr_j<\gamma.
\]

The residual margin is at least

\[
\gamma-\sum_jw_jr_j.
\]

This admits arbitrary source angles through local interval/Lipschitz bounds without pretending their trigonometric values are algebraic.

## Exact fixture

At \(x=1/3\), rational alternating-series intervals enclose sine and cosine, and the interval for \(\sin^2x+\cos^2x\) contains one. A nominal slack margin \(1/20\), two unit-weight angle uncertainties of radius \(1/100\), leaves certified margin \(3/100\). Increasing both radii to \(1/20\) exceeds the nominal margin and is rejected by this certificate.

## Failure semantics

A nonpositive residual does not prove the physical analyzer invalid or the SDP slack indefinite. It means the current enclosure cannot certify the claim. Repair requires tighter trigonometric intervals, correlated arithmetic, smaller source-angle uncertainty, or a stronger nominal margin.

## Disposition

Arbitrary analyzer angles can enter the exact verification boundary through rational outward enclosures and structural projector identities. SDP positivity survives when the weighted angle-radius budget is strictly below the exact nominal spectral margin. Insufficient separation from zero is reported as nonverification, not rounded into success.
