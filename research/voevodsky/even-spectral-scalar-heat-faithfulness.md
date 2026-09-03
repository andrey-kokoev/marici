# Even-spectral scalar heat faithfulness

## Question

Does global scalar heat complete monotonicity already recover positivity of an even completed spectral distribution?

## Claim boundary

The theorem identifies the faithful scalar criterion. It does not prove that the arithmetic heat function satisfies it.

## Pushforward and Laplace transform

Let \(\rho\) be an even tempered distribution on \(\mathbb R\), and use the proper map \(u\mapsto u^2\) to define

\[
\eta=(u^2)_*\rho
\]

on \([0,\infty)\). Then

\[
\Theta(t)=\langle\rho,e^{-tu^2}\rangle
=
\langle\eta,e^{-t\lambda}\rangle.
\]

Assume global complete monotonicity:

\[
(-1)^k\Theta^{(k)}(t)\geq0
\qquad
(k\geq0,
\ t>0).
\]

Bernstein's theorem supplies a positive measure \(\mu\) with the same Laplace transform. Injectivity of the Laplace transform for tempered distributions supported on \([0,\infty)\) gives \(\eta=\mu\).

## Lift through evenness

For a nonnegative compactly supported smooth test \(\phi\), its symmetrization

\[
\phi_{\rm ev}(u)=\frac{\phi(u)+\phi(-u)}2
\]

is nonnegative and has the form \(\psi(u^2)\) for a nonnegative smooth \(\psi\) on the half-line. Since \(\rho\) is even,

\[
\langle\rho,\phi\rangle
=
\langle\rho,\phi_{\rm ev}\rangle
=
\langle\eta,\psi\rangle
\geq0.
\]

Thus \(\rho\) is positive. The converse follows by differentiating under the positive pairing. Hence positivity of \(\rho\) is equivalent to global complete monotonicity of \(\Theta\).

## Falsifier boundary

The criterion requires every derivative order at every \(t>0\). A signed measure can satisfy all derivative signs at one parameter and fail positivity elsewhere. The checker uses

\[
\delta_2-\frac14\delta_1,
\]

whose signed heat derivatives are positive at \(t=1\) for every order but whose heat value is negative at \(t=2\).

## Disposition

The independent all-character lift gate is eliminated under even source typing. The remaining RH-strength target is the global scalar inequality above for the explicit completed arithmetic heat function. Order zero, finite jets, and even all jets at one parameter are nonfaithful projections.

## Verification

- `research/voevodsky/even-spectral-scalar-heat-faithfulness-v1.json`
- `research/voevodsky/checkers/check_even_spectral_scalar_heat_faithfulness.py`
- `research/voevodsky/results/even_spectral_scalar_heat_faithfulness.json`
