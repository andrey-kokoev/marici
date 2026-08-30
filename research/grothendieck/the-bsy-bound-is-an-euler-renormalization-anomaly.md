# The BSY bound is an Euler renormalization anomaly

## The finite Euler calculation

Let `T` have the centered Cauchy law of scale `1/2`:

\[
d\mathbb P(T=t)
=
\frac1{2\pi}\frac{dt}{\tfrac14+t^2}.
\]

Its characteristic function is

\[
\mathbb E e^{iuT}=e^{-|u|/2}.
\]

For a finite prime cutoff, put

\[
Z_X(t)=\prod_{p\le X}(1-p^{-1/2-it})^{-1}.
\]

The logarithmic series is finite over primes and absolutely convergent over
prime powers, so expectation may be taken term by term:

\[
\begin{aligned}
\mathbb E\log|Z_X(T)|
&=
\sum_{p\le X}\sum_{k\ge1}
\frac{p^{-k/2}}k
\mathbb E\cos(kT\log p)\\
&=
\sum_{p\le X}\sum_{k\ge1}\frac{p^{-k}}k\\
&=
\sum_{p\le X}-\log(1-p^{-1}).
\end{aligned}
\]

Thus every finite Euler chart has strictly positive Cauchy log-energy, and
Mertens' theorem gives

\[
\mathbb E\log|Z_X(T)|
=
\log\log X+\gamma+o(1).
\]

It diverges rather than approaching the finite BSY entropy.

## The operations do not commute

The completed boundary value is not obtained by applying the following
operations in an arbitrary order:

```text
Euler cutoff limit
logarithm
critical-boundary continuation
Cauchy expectation
endpoint and archimedean renormalization
```

At finite cutoff the Cauchy expectation evaluates the Euler character at the
interior anchor `s=1`; it therefore sees the harmonic-series divergence of
the prime current. Analytic continuation and completion remove that divergent
mode before the BSY boundary functional is formed.

Consequently the hoped-for source inequality cannot be proved by monotone
passage from finite Euler positivity. The limit is not uniformly integrable
for the logarithmic boundary observable.

## Why ordinary Mertens subtraction is insufficient

Subtracting the universal divergence

\[
\log\log X+\gamma
\]

produces a finite normalization, but its vanishing is already governed by
ordinary Mertens asymptotics. It does not retain the off-line divisor entropy.
The RH-sensitive object is therefore not the scalar constant term of the
finite Euler expectation by itself.

The missing completion operation must retain more structure while removing
the divergent common mode. In the earlier typed language, it must carry:

- the primitive current producing the logarithmic divergence;
- the square current at the Hilbert but non-trace-class level;
- the connected tail;
- the endpoint and archimedean boundary channels;
- the order in which continuation and boundary expectation are taken.

## The sharpened source target

Let `R` denote a source-authorized, boundary-bearing renormalization, `B` the
critical-boundary Cauchy expectation, and `L_E` the labelled Euler logarithm.
The actual target is not an inequality for every finite product. It is a
commutator identity whose residual is the BSY entropy:

\[
\mathfrak A=[B,R](L_E).
\]

The notation is schematic: both operations and their domains must be derived
before the residual is evaluated. A successful construction must prove

\[
\mathfrak A=\mathcal D_{\mathrm{BSY}}
\]

and then orient the anomaly nonpositively from the theta--Tate source. Since
factorization independently gives `D_BSY >= 0`, this would force equality.

The cheapest falsifier is a source-compatible renormalization whose scalar
constant term exists but whose commutator residual changes under a hostile
symmetric divisor multiplier. Such a renormalization has erased the very
information it was meant to control.

## Scope

This packet proves the exact finite-cutoff expectation and identifies the
failure of uniform integrability. It does not construct the required
boundary-bearing renormalization, prove the anomaly identity, establish the
opposite BSY inequality, or prove RH.
