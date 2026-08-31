# The strict prime Schur margin gives a cutoff-uniform Cayley impedance gap

> **Spectral-role correction.** The successor packet
> `the-uniform-cayley-impedance-gap-overcoerces-the-seam-and-cannot-carry-the-xi-divisor.md`
> observes that this gap persists on the seam. The same-sign passive
> characteristic is therefore everywhere invertible and cannot be a
> divisor-preserving Xi pencil. Retain the estimates below as a zero-free
> comparison-system theorem, not as the completed RH characteristic.

## Strict Schur bound

For the labelled prime-delay network,

\[
\|S_X(z)\|
\le r,
\qquad
r=2^{-1/2}<1,
\]

uniformly in the prime cutoff and throughout the open upper-half-plane chart.

Define

\[
\Theta_X(z)
=i(I+S_X(z))(I-S_X(z))^{-1}.
\]

## Exact imaginary-part formula

The Cayley identity gives

\[
\operatorname{Im}\Theta_X
=
(I-S_X^*)^{-1}
(I-S_X^*S_X)
(I-S_X)^{-1}.
\]

For every source vector \(x\),

\[
\langle x,
\operatorname{Im}\Theta_X x\rangle
\ge
\frac{1-r^2}{(1+r)^2}
\|x\|^2.
\]

Thus

\[
\operatorname{Im}\Theta_X
\ge
\delta_\Theta I,
\qquad
\delta_\Theta
=
\frac{1-r}{1+r}
=3-2\sqrt2>0.
\]

The bound is independent of the number of primes.

## Addition of the history Weyl return

Choose the Green convention in which the history return satisfies

\[
\operatorname{Im}M_{H,X}(z)\ge0
\]

in the same upper-half-plane chart. Then

\[
M_{U,X}(z)
=
\Theta_X(z)+M_{H,X}(z)
\]

obeys

\[
\operatorname{Im}M_{U,X}(z)
\ge
\delta_\Theta I.
\]

If the opposite Weyl convention is used, reverse both source and history
signs before addition. Mixing conventions would destroy the estimate.

## Uniform invertibility

For every \(x\),

\[
\delta_\Theta\|x\|^2
\le
\left|
\langle x,M_{U,X}x\rangle
\right|
\le
\|x\|\,\|M_{U,X}x\|.
\]

Hence

\[
\|M_{U,X}x\|
\ge
\delta_\Theta\|x\|.
\]

The same coercive estimate, or the complex Lax--Milgram theorem after rotation,
gives surjectivity. Therefore

\[
\|M_{U,X}(z)^{-1}\|
\le
\delta_\Theta^{-1}
=3+2\sqrt2.
\]

This is cutoff uniform and does not deteriorate as the chart approaches the
seam from within the open half-plane.

## Coupled numerator bound

Since

\[
N_X=M_{U,X}(I-S_X),
\]

one has

\[
N_X^{-1}
=(I-S_X)^{-1}M_{U,X}^{-1}.
\]

Consequently

\[
\|N_X^{-1}\|
\le
\frac{3+2\sqrt2}{1-2^{-1/2}}.
\]

Thus the coupled numerator has no finite-cutoff upper-half-plane collision and
has a uniform inverse gap. Reciprocal transport supplies the corresponding
lower-half-plane result.

## Completion consequence

If \(S_X\to S\) and \(M_{H,X}\to M_H\) locally in operator norm on the
completed source space, the inverse bounds pass to the limit. No numerator
zero or spectral pollution can appear in either open half-plane.

Determinant convergence requires the separate relative ideal estimates, but
operator invertibility no longer depends on determinant convergence.

## Remaining Xi bridge

The quantitative gap proves zero confinement for the paired passive
characteristic. It does not prove that its completed determinant section is
Xi. The missing theorem remains

\[
\det_{\rm rel}M_U(z)=E(z)\xi(s),
\qquad E(z)\ne0.
\]

Without that divisor comparison, the passive pencil may simply be a different
zero-free characteristic.

## Disposition

The arithmetic Cayley law and history Weyl return give a cutoff-uniform
impedance gap

\[
\delta_\Theta=3-2\sqrt2.
\]

This closes off-seam invertibility and numerator inverse control for the
paired passive candidate, conditional only on common sign convention and
operator-norm completion. G4 remains open at determinant-line identification
with Xi. No RH conclusion is authorized.
