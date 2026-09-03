# Xi paired-Hadamard multiplicity contract

## Question

What exact orbit and multiplicity convention makes the paired Xi resolvent agree with the endpoint--gamma--prime inverse-Laplace formula?

## Claim boundary

The algebraic convention and convergence reduction are fixed. Authoritative classical citations and joint source-owner review remain absent.

## Completed normalization

Use

\[
\xi(s)
=
\frac12s(s-1)
\pi^{-s/2}
\Gamma(s/2)
\zeta(s).
\]

Set

\[
\Xi(y)=\xi\left(\frac12+y\right).
\]

The functional equation gives

\[
\Xi(y)=\Xi(-y).
\]

For a zero \(\rho\), write

\[
a_\rho=\rho-\frac12.
\]

The functional involution sends \(a_\rho\) to \(-a_\rho\).

## Orbit convention

Group zeros into orbits under

\[
a\sim-a.
\]

Retain one representative per orbit and retain the original holomorphic multiplicity \(m_a\). Do not double it.

The centered paired product is

\[
\frac{\Xi(y)}{\Xi(0)}
=
\prod_{[a]}
\left(1-\frac{y^2}{a^2}\right)^{m_a},
\]

under symmetric Hadamard convergence.

Since

\[
N(T)=O(T\log T),
\]

one has

\[
\sum_{[a]}\frac{m_a}{|a|^2}<\infty.
\]

Thus pairing converts the order-one product in \(y\) into a genus-zero product in \(x=y^2\), locally uniformly on compact sets away from its poles.

## Logarithmic derivative

Define

\[
B(x)
=
\log\frac{\xi(1/2+\sqrt x)}{\xi(1/2)}.
\]

For one orbit,

\[
\frac{d}{dx}
\log\left(1-\frac{x}{a^2}\right)^{m_a}
=
\frac{m_a}{x-a^2}.
\]

Hence

\[
B'(x)
=
\sum_{[a]}
\frac{m_a}{x-a^2}
=
\sum_{[a]}
\frac{m_a}{x+\lambda_a},
\qquad
\lambda_a=-a^2.
\]

The same factor follows directly from

\[
\frac1{2y}
\left(
\frac1{y-a}+rac1{y+a}
\right)
=
\frac1{y^2-a^2}.
\]

## Conjugation convention

Off the critical line, \(a\) and \(\bar a\) are generally distinct modulo \(a\sim-a\). They contribute conjugate poles

\[
\lambda_a=-a^2,
\qquad
\lambda_{\bar a}=\overline{\lambda_a}.
\]

On the critical line,

\[
a=i\gamma,
\qquad
\bar a=-a.
\]

Conjugation and the functional involution then define the same orbit. One positive ordinate \(\gamma>0\) represents that orbit and is counted once with multiplicity \(m_a\).

This removes the possible factor-of-two ambiguity.

## Endpoint coefficient

With

\[
s=\frac12+y,
\]

the elementary completed factors obey

\[
\frac1{2y}
\left(
\frac1s+rac1{s-1}
\right)
=
\frac1{y^2-1/4}
=
\frac1{x-1/4}.
\]

Its inverse-Laplace kernel is exactly

\[
e^{t/4}.
\]

The gamma/pi term retains coefficient

\[
\frac{\psi(s/2)-\log\pi}{4y},
\]

and the Euler-product term retains

\[
\frac{\zeta'(s)/\zeta(s)}{2y}.
\]

The zeta pole cancellation occurs only in the completed sum. The endpoint must not be removed from one presentation without transporting that cancellation.

## Remaining source object

The mathematical convergence reduction now needs authoritative references for:

1. the symmetric Hadamard product of \(\xi\);
2. the zero-count bound \(N(T)=O(T\log T)\);
3. termwise logarithmic differentiation after pairing;
4. inverse-Laplace interchange on the declared half-plane.

A joint audit must then compare this orbit convention with every endpoint--gamma--prime checker and positive-ordinate sum.

## Disposition

The multiplicity contract is no longer conceptually open: one functional-equation orbit contributes one resolvent pole with the original multiplicity. The remaining blocker is bibliographic and cross-artifact verification, not another normalization choice.

## Verification

- `research/voevodsky/xi-paired-hadamard-multiplicity-contract-v1.json`
- `research/voevodsky/checkers/check_xi_paired_hadamard_multiplicity_contract.py`
- `research/voevodsky/results/xi_paired_hadamard_multiplicity_contract.json`
