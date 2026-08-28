# No Finite Theta-Label Cutoff Has Global Invariant Positivity

## Finite completed packet

For a fixed positive integer \(N\), set

\[
\Phi_N(u)=\sum_{n=1}^{N}\phi_n(u),
\qquad
\phi_n(u)=n^{-1/2}\phi_1(u+\log n).
\]

Its reflection-invariant projection is

\[
\mathsf E\Phi_N(u)
=
\frac{\Phi_N(u)+\Phi_N(-u)}2.
\]

## Negative reflected asymptotic

As \(v\) tends to negative infinity,

\[
\phi_1(v)\sim-6\pi e^{5v/2}.
\]

Hence, for each fixed label \(n\),

\[
\phi_n(-u)
=
n^{-1/2}\phi_1(\log n-u)
\sim
-6\pi n^2 e^{-5u/2}.
\]

Summing finitely many labels gives

\[
\Phi_N(-u)
\sim
-6\pi e^{-5u/2}\sum_{n=1}^{N}n^2.
\]

Meanwhile every direct term \(\phi_n(u)\) decays superexponentially as \(u\)
tends to infinity. Therefore

\[
\mathsf E\Phi_N(u)<0
\]

for every sufficiently large \(u\).

## Infinite completion is essential

The full theta source \(\Phi\) is even and positive, but no finite label cutoff
has a globally positive invariant projection. Positivity is created only in
the infinite label completion.

This is not convergence with one fixed globally admissible truncation.
For increasing chamber position \(u\), new labels near the moving scale

\[
\log n\approx u
\]

must enter to repair the reflected negative tail. Any fixed \(N\) eventually
falls behind that frontier.

## Completion consequence

Finite-cutoff positivity on compact \(u\)-intervals cannot be promoted
uniformly to the whole chamber. The limits

\[
N\longrightarrow\infty
\]

and

\[
u\longrightarrow\infty
\]

do not commute for invariant positivity.

This is a concrete theta instance of completion manufacturing a property
absent at every finite stage. The required transition system is moving-scale,
not merely nested by label count.

## RH relevance

Any finite Euler or theta-label certificate can control only a bounded chamber
window unless it includes an explicit uniform moving-front estimate. The
global invariant source cannot be replaced by one sufficiently large finite
packet.

The next useful object is the renormalized frontier coordinate

\[
\rho=ne^{-u},
\]

which keeps the compensating labels visible as \(u\) and \(n\) grow together.

## Falsifier

The theorem fails if some finite \(N\) has

\[
\mathsf E\Phi_N(u)\geq0
\]

for all positive \(u\). The displayed asymptotic excludes this.
