# The differentiated theta packet cannot equal the four-front Stieltjes boundary before scale transport

## Two differentiated objects

The raw Stieltjes boundary is

\[
b_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0,
\qquad
L=\log p.
\]

It is a finite linear combination of translated Gaussians.

The wall-subtracted theta packet satisfies

\[
\Psi_p^{\mathrm{rel}}(u)
=
c_{0,p}\zeta\!\left(-\frac12\right)e^{u/2}
+
O(e^{3u/2})
\]

as \(u\to-\infty\), unless a coefficient cancellation occurs. Since

\[
c_{0,p}=-2\pi L^2
\]

and

\[
\zeta\!\left(-\frac12\right)\ne0,
\]

the leading coefficient is nonzero for every prime. Therefore

\[
D_u\Psi_p^{\mathrm{rel}}(u)
=
-\pi L^2\zeta\!\left(-\frac12\right)e^{u/2}
+
O(e^{3u/2}).
\]

## Asymptotic mismatch

If one identifies the Stieltjes coordinate \(q\) directly with the Mellin
coordinate \(u\), then

\[
b_p(u)
\]

decays Gaussianly as \(u\to-\infty\), whereas

\[
D_u\Psi_p^{\mathrm{rel}}(u)
\]

has a nonzero \(e^{u/2}\) tail. Hence

\[
D_u\Psi_p^{\mathrm{rel}}
\ne
b_p
\]

as functions or distributions on the common line.

This is not a failure of regularity: both sides are smooth and lie in every
finite Sobolev rung. It is a failure of direct constructor identification.

## Required comparison arrow

The missing arrow must change the asymptotic model. It must include the
source-authorized scale transport between:

- the additive Gaussian coordinate \(q\);
- the logarithmic half-density coordinate \(u\);
- the theta-tail or Green propagation.

Schematically, the theorem must have the form

\[
\mathcal T_{\mathrm{src},p}
\left(
D_u\Psi_p^{\mathrm{rel}}
\right)
=
b_p
\]

in the reduced Green target, or an equivalent intertwining square. The map
\(\mathcal T_{\mathrm{src},p}\) cannot be the identity.

Its obligations are now explicit:

1. derive the coordinate change and half-density Jacobian;
2. preserve the ordered reciprocal character;
3. carry the coefficient-wall subtraction to the Stieltjes wall convention;
4. intertwine the relevant differential graphs;
5. annihilate the declared Green radicals;
6. remain uniformly controlled after Euler weighting.

## Fourier-side contrast

The Stieltjes boundary has transform

\[
\widehat b_p(\xi)
=
2i\left(
\sin(L\xi)-\sin(2L\xi)
\right)\widehat f_0(\xi).
\]

Thus it is a Gaussian multiplier times a finite trigonometric polynomial.
The differentiated theta packet is instead an infinite label synthesis with a
fractional Mellin-end expansion. Equality before the source scale transform
would collapse these distinct analytic types without authority.

## Consequence for the first Adams edge

The previously reduced target

\[
J_{\mathrm{src}}e_p=d_p
\]

cannot be proved by simply identifying the completed theta packet with
\(d_p\) in one coordinate chart. The exact ordered-primitive factorization
moves the comparison to derivatives, but the scale-transport arrow remains
essential.

The earliest unresolved constructor is therefore no longer label synthesis,
wall regularity, or ordered inversion. It is the source-derived
additive-to-logarithmic Green transport \(\mathcal T_{\mathrm{src},p}\).

## Hostile

An \(L^2\)-unitary chosen after the fact can send one normalized vector to the
other. That proves only abstract Hilbert equivalence. A valid comparison must
intertwine the frozen differential, wall, reflection, and label structures;
otherwise it is a fitted transport rather than the Adams constructor.
