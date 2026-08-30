# The derivative comb descends through the Jacobi wall but is unbounded in the bare Green energy

## Result

The odd derivative-comb observer passes the algebraic radical test for the Jacobi heat Green form:

\[
\Delta'(1)=0.
\]

However, it is not bounded in the quotient norm supplied only by the first-order heat energy. Therefore radical descent does not by itself produce a bounded Green observer.

The correct domain must retain a higher Sobolev or completion-jet graph norm.

## Jacobi Green radical

On the periodic Jacobi fiber, use the heat energy

\[
\mathcal E(F)
=
\int_{\mathbb T}|F'(z)|^2\,dz.
\]

Its radical is exactly the constant mode:

\[
\ker\mathcal E=\mathbb C1.
\]

The periodized derivative-comb port is derivative evaluation at the marked lattice point, with the frozen sign convention:

\[
O(F)=\langle\Delta',F\rangle=-F'(0).
\]

Since

\[
O(1)=0,
\]

the observer factors algebraically through

\[
H^s(\mathbb T)/\mathbb C1.
\]

This verifies the required kernel inclusion for the Jacobi wall:

\[
\ker\mathcal E\subseteq\ker O.
\]

The wall itself remains available through the separately typed Wronskian connecting morphism. Quotienting the heat-energy radical therefore does not erase the wall port.

## Bare-energy hostile

The descended observer is not continuous in the norm \(\mathcal E(F)^{1/2}\).

For \(N\ge1\), define

\[
F_N(z)
=
\frac1{\sqrt N}
\sum_{n=1}^{N}
\frac{e^{2\pi inz}}{2\pi n}.
\]

Then

\[
F_N'(z)
=
\frac{i}{\sqrt N}
\sum_{n=1}^{N}e^{2\pi inz}.
\]

Orthogonality gives

\[
\mathcal E(F_N)
=
\|F_N'\|_{L^2}^2
=
1.
\]

But

\[
|O(F_N)|
=
|F_N'(0)|
=
\sqrt N.
\]

Hence

\[
\sup_{\mathcal E(F)\le1}|O(F)|=\infty.
\]

This is an exact finite Fourier hostile. It shows:

\[
\text{radical annihilation}
\not\Rightarrow
\text{bounded quotient observer}.
\]

No completion or prime limit is needed for the failure.

## Correct Sobolev threshold

Pointwise derivative evaluation is continuous on \(H^s(\mathbb T)\) when

\[
s>\frac32.
\]

Indeed, if

\[
F(z)=\sum_{n\in\mathbb Z}\widehat F(n)e^{2\pi inz},
\]

then

\[
|F'(0)|
\le
\left(
\sum_n(1+n^2)^s|\widehat F(n)|^2
\right)^{1/2}
\left(
\sum_n\frac{(2\pi n)^2}{(1+n^2)^s}
\right)^{1/2},
\]

and the second factor is finite exactly for \(s>3/2\).

The earlier even completion channel was placed in \(H^s\) with \(s>9/2\) because it contains fourth spatial derivatives. The odd current uses a fifth-order front jet before the derivative-comb contraction, and its scalar realization contains sixth derivatives. A common source graph domain must therefore be selected from the actual completion operator, not merely from the order of the observer distribution.

For the scalar sixth-jet formula, a simple sufficient Hilbert realization is

\[
H^s(\mathbb T),
\qquad
s>\frac{13}{2},
\]

if sixth derivative evaluation is demanded directly. More economical anisotropic or graph domains may suffice, but require a separate closed-operator theorem.

## Relative form typing

Let

\[
\mathcal D_{\mathrm{comp}}
=
\operatorname{Dom}
\left(
\partial_z^2,\partial_z^4,\partial_z^6
\right)
\]

with its source-derived graph norm. On a sufficiently regular periodic core, the odd functional

\[
F\longmapsto
-\left\langle
\Delta',
\left[
\frac{r^3}{8\pi^3}\partial_z^5
+
\frac{15r^2}{8\pi^2}\partial_z^3
+
\frac{15r}{4\pi}\partial_z
\right]F
\right\rangle
\]

annihilates constants and is continuous in the corresponding high-order trace topology on compact \(r\)-regions.

The needed Green theorem is therefore not a boundedness theorem in \(\mathcal E^{1/2}\). It is a closed graph-form theorem for the pair

\[
\left(
\mathcal E,
\mathcal C_{\mathrm{Jacobi}}
\right),
\]

where \(\mathcal C_{\mathrm{Jacobi}}\) carries the completion jets.

## Consequence for global margins

A global coercivity estimate cannot use the first-order Jacobi Green energy alone to dominate the odd seam observer. Any such estimate is falsified by \(F_N\).

There are only two authorized repairs:

1. include the source completion-jet graph energy in the analytic block;
2. prove that the incidence range is a much smaller heat-smoothed subspace on which derivative evaluation is bounded by the first-order energy.

The second route may be sharper. For a fixed positive heat time, smoothing suppresses the Fourier hostile exponentially. But the positive time and its lower bound must come from the source scale path; allowing heat time to approach zero restores the divergence.

## Next gate

The immediate theorem is now precise:

> Determine the actual range of the prime-labelled Jacobi incidence and prove either a uniform positive-time smoothing bound or a closed high-order graph-form bound for the derivative-comb contraction, after quotienting only the constant wall.

Until that theorem is established, radical descent is valid but the odd observer is not yet a bounded component of the relative Green cell.
