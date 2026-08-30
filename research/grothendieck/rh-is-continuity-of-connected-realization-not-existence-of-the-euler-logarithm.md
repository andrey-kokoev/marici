# RH Is Continuity of Connected Realization, Not Existence of the Euler Logarithm

## Formal connectedization is unobstructed

Let \(\widehat{A}\) be the augmentation completion of the commutative
prime-label algebra with generators \(X_p\). The formal Euler object is

\[
Z=\prod_p(1-X_p)^{-1}.
\]

Its constant term is one, so its formal logarithm exists without any analytic
assumption:

\[
\log Z
=
\sum_p\sum_{k\ge1}\frac{X_p^k}{k}.
\]

Let \(H\) be the label-energy derivation

\[
H X_p=(\log p)X_p.
\]

Then

\[
H\log Z
=
\sum_p\sum_{k\ge1}(\log p)X_p^k.
\]

Thus the full prime-power current is already defined in the formal source
category. No zero and no analytic continuation is needed to construct it.

## Boundary realization

Realize a prime-power monomial by its logarithmic atom:

\[
X_p^k\longmapsto\delta_{k\log p}.
\]

The connected formal current becomes

\[
\mu_{\mathrm{arith}}
=
\sum_{p,k\ge1}(\log p)\delta_{k\log p}
=
\sum_{n\ge1}\Lambda(n)\delta_{\log n}.
\]

The continuum comparison current in logarithmic coordinate is

\[
\mu_{\mathrm{cont}}=e^u\,du.
\]

After the half-density twist, define

\[
\tau
=
e^{-u/2}
\left(
\mu_{\mathrm{arith}}-\mu_{\mathrm{cont}}
\right).
\]

This is the direct boundary realization of the connected source object. Its
definition does not divide by \(\xi\).

## Relation to the cumulative discrepancy

For \(u>0\), put

\[
q(u)=e^{-u/2}\bigl(\psi(e^u)-e^u\bigr).
\]

Distributionally on the open positive ray,

\[
(\partial_u+1/2)q=\tau.
\]

If both sides are extended by zero to the negative ray, the fixed origin
value \(q(0)=-1\) contributes the explicit boundary term

\[
(\partial_u+1/2)(\mathbf 1_{u\ge0}q)
=
\mathbf 1_{u\ge0}\tau-\delta_0.
\]

The origin delta is the completion boundary current; it must be retained
rather than absorbed into the bulk.

On distributions supported on the positive ray, the causal inverse of
\(\partial_u+1/2\) is convolution with
\(e^{-u/2}\mathbf 1_{u\ge0}\). Consequently \(q\) is tempered exactly
when the boundary current \(\tau\), together with its fixed origin term, is
tempered.

## The actual coherence square

There are two routes out of the same formal Euler object:

1. Fock expansion, Gaussian completion, and Mellin readout produce the
   additive completed section \(\xi\).
2. Formal logarithm, label differentiation, boundary realization, continuum
   subtraction, and half-density twisting produce \(\tau\).

On the invertible analytic locus, the two routes are related by
\(d\log\xi\) and the explicit archimedean correction. The formal upper
route exists everywhere, but the right vertical realization need not land in
the tempered boundary category.

Therefore the missing RH coherence is:

> Connectedization of the formal prime Fock object commutes with completed
> theta realization into the half-normalized tempered boundary rigging.

The preceding temperedness theorem shows that this continuity statement
implies RH.

## Why the distinction matters

It was tempting to say that the logarithm ceases to exist at a zero. That is
true only after scalar analytic evaluation. At source level the plethystic
logarithm remains perfectly meaningful because the Euler object has
augmentation one.

What fails is descent:

- formal connected current: always defined;
- analytic scalar logarithm: defined only on the nonzero locus;
- tempered boundary realization: equivalent to RH at the half-density
  threshold.

Thus the zero is not destruction of source information. It is failure of a
formal connected object to descend continuously into one scalar analytic
chart.

## Hard obstruction

Continuity cannot follow from the algebra of group-like elements alone.
Arbitrary formal prime weights still admit a plethystic logarithm, while
their realized atom currents may grow exponentially after the half twist.

The required estimate must use additional theta/Tate source structure:

- exact integer endpoint incidence;
- Poisson self-sewing;
- the continuum subtraction;
- and compatibility of those operations with connectedization.

This is the first real analytic gate after the categorical reduction.

## Falsifier

A proposed proof fails if it:

- establishes only formal existence of \(\log Z\);
- defines \(\tau\) by inverse Mellin continuation of
  \(-\zeta'/\zeta\);
- drops the origin delta;
- proves temperedness only after assuming a prime-counting bound equivalent
  to RH;
- or uses a topology in which arbitrary exponentially weighted prime atoms
  are declared tempered.

