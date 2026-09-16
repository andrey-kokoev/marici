# The first theta-tail transform is not completely monotone

## Candidate transform

After direct positive-exponential representation of \(\Phi\) failed, the simplest boundary quotient candidate is its positive tail

\[
C(u)=
\int_u^\infty
\Phi(v)\,dv.
\]

If \(C\) were completely monotone, Bernstein's theorem would give

\[
C(u)=
\int_0^\infty
e^{-\alpha u}
\,d\mu(\alpha),
\qquad
\mu\ge0.
\]

This would place the tail state in the positive exponential cone while retaining a canonical derivative relation

\[
-C'(u)=\Phi(u).
\]

## Derivative test

For \(k\ge1\),

\[
C^{(k)}(u)
=-
\Phi^{(k-1)}(u).
\]

Complete monotonicity requires

\[
(-1)^kC^{(k)}(u)
\ge0.
\]

At order three this becomes

\[
\Phi''(u)
\ge0.
\]

The completed theta kernel has negative second derivative near the modular seam. Numerically,

\[
\Phi''(0)
\approx
-16.73050077470325686679.
\]

Hence

\[
(-1)^3C'''(0)
=
\Phi''(0)
<0.
\]

The first tail is not completely monotone.

## Reconnaissance

Checker:

`research/voevodsky/checkers/scout_theta_tail_complete_monotonicity.py`

Result:

`research/voevodsky/results/theta-tail-complete-monotonicity-scout.json`

The checker tests derivative orders one through eight on \(0\le u\le4\). It finds violations beginning at order three and many further violations at higher orders.

This is high-precision reconnaissance, not an interval certificate. A formal rejection needs a directed enclosure proving

\[
\Phi''(0)<0.
\]

That should be inexpensive because the numerical margin is large and the theta-label tail is superexponentially small.

## Consequence

Neither of the two simplest source-preserving maps reaches the positive exponential cone:

1. \(\Phi\) itself fails because modular evenness gives \(\Phi'(0)=0\);
2. its first tail fails complete monotonicity at the third derivative.

Repeated integration does not automatically solve the problem. For an \(m\)-fold tail, complete monotonicity eventually tests the same derivative sequence of \(\Phi\), merely shifted in order. Any sign violation in the derivative hierarchy reappears at a later complete-monotonicity condition.

## Revised construction space

A successful type-changing map cannot be a finite number of ordinary positive tail integrations. It must use additional structure, such as:

- a nonlocal modular quotient coupling \(u\) and \(-u\);
- a positive dilation with extra boundary coordinates;
- a resolvent transform in the squared spectral coordinate;
- or a signed exponential representation with a source-derived contraction.

## Scope

Failure of complete monotonicity rejects this route to the existing positive-mode theorem. It does not challenge the theta source, the finite Pick certificates, or RH.
