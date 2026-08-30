# Monotone theta density would force the one-sided transfer to be outer

## Zero-free half-plane lemma

Let \(\Phi:[0,\infty)\to[0,\infty)\) be nonzero, integrable, and nonincreasing. Define

\[
m(z)=\int_0^\infty\Phi(t)e^{-zt}\,dt,
\qquad
\operatorname{Re}z>0.
\]

Let \(\mu=-d\Phi\) be the positive Stieltjes measure associated with the monotone tail. Since

\[
\Phi(t)=\mu((t,\infty))
\]

after routing any endpoint atom separately, Tonelli gives

\[
m(z)
=
\frac1z
\int_{(0,\infty)}
(1-e^{-zs})\,d\mu(s).
\]

Therefore

\[
\operatorname{Re}(z,m(z))
=
\int_{(0,\infty)}
\left(
1-e^{-s\operatorname{Re}z}
\cos(s\operatorname{Im}z)
\right)
d\mu(s).
\]

For \(\operatorname{Re}z>0\), every integrand is strictly positive for \(s>0\). Hence

\[
\operatorname{Re}(z,m(z))>0,
\]

and consequently

\[
m(z)\ne0
\qquad
(\operatorname{Re}z>0).
\]

This is a source-level no-Blaschke-factor theorem. It uses monotonicity of the time-domain density, not desired spectral zero exclusion.

## Boundary qualification

On the imaginary axis the same argument becomes nonnegative:

\[
\operatorname{Re}(i\omega m(i\omega))
=
\int(1-cos \omega s),d\mu(s)\ge0.
\]

Boundary zeros may occur for lattice-supported step measures, as the indicator-kernel example shows. They do not create interior right-half-plane zeros.

For a smooth strictly decreasing theta density with nonlattice support, the integral is positive for every \(\omega\ne0\), so the boundary transfer is also nonzero away from infinity.

## From zero-free to outer

Zero-freeness removes the Blaschke factor but does not by itself remove all inner factors. Two additional source properties suffice here:

1. analytic continuation across every finite segment of the imaginary axis rules out a singular inner factor supported there;
2. nonvanishing immediate incidence at \(t=0\), reflected in polynomial rather than exponential decay of \(m(x)\) as \(x\to+infty\), rules out a delay factor \(e^{-az}\), \(a>0\).

If \(\Phi\) is continuous at zero with \(\Phi(0)>0\), then

\[
m(x)\sim\frac{\Phi(0)}x
\qquad(x\to+infty).
\]

Thus no positive delay is present. With the standard Hardy integrability of \(\log|m(i\omega)|\), the inner factor is constant and \(m\) is outer up to a unimodular scalar.

The logarithmic integrability must still be checked in the exact weighted Hardy class. It should not be inferred only from pointwise nonvanishing.

## Consequence for the history pair

If the completed theta density satisfies these hypotheses, then

\[
\ker H^*=0
\]

by analytic multiplication and

\[
\ker H=0
\]

by outerness. Hence the filtered history Dirac has no exact dark state:

\[
\ker\mathscr D_H=0.
\]

Nevertheless the transfer tends to zero at high frequency, so the history pair remains noncoercive. The theorem closes exact kernel faithfulness, not a uniform Green margin.

## Separation from RH

The bilateral completed section is obtained from both one-sided boundary values. Schematically,

\[
\Xi(\omega)
=
m(i\omega)+m(-i\omega)
=
2\operatorname{Re}m(i\omega)
\]

in the frozen normalization.

Zeros of this real sum can occur by cancellation between two nonzero reciprocal boundary values. Therefore zero-freeness and outerness of the one-sided transfer do not imply RH and are not equivalent to it.

This is exactly the desired architecture:

- one-sided causal propagation is minimum phase and zero-free;
- the completed zero divisor can arise only through reciprocal arithmetic sewing or boundary-value cancellation;
- the scalar zero mechanism remains downstream.

## The actual source gate

The project has established positivity, evenness, smoothness, and rapid decay of the completed theta kernel. It has not yet recorded a proof that

\[
\Phi'(t)<0
\qquad(t>0).
\]

That single inequality is now decisive for the one-sided realization.

The correct next calculation is termwise differentiation of the source theta series, with a domination theorem justifying the exchange, followed by a sign proof for the full sum.

## Series-level audit

For a representation

\[
\Phi(t)
=
\sum_{n\ge1}P_n(e^{2t})e^{-\pi n^2e^{2t}},
\]

differentiate each summand exactly. The polynomial prefactors can create local sign competition even though every Gaussian exponential decreases. Therefore positivity and rapid decay alone do not prove monotonicity.

The audit must establish one of:

1. every differentiated summand is negative;
2. negative leading terms dominate all positive prefactor terms;
3. a heat-equation or total-positivity identity rewrites \(-\Phi'\) as a manifestly positive source sum.

A numerical plot is not authority for this gate.

## Hostiles

A positive smooth rapidly decreasing function can have small oscillatory shoulders and a Laplace transform with interior zeros.

A nonincreasing step kernel has a zero-free open half-plane but boundary zeros, showing why strict smooth monotonicity matters for boundary faithfulness.

A zero-free analytic function may still contain a singular or delay inner factor, showing why continuation and the zero-time incidence must be retained.

## Frontier contraction

The next theorem is now concrete:

> Prove strict half-line monotonicity of the completed theta density from its labelled source series.

If successful, it supplies a forward-derived outer/minimum-phase theorem for the one-sided theta history while leaving the reciprocal sewing determinant as the unique possible completed zero mechanism.
