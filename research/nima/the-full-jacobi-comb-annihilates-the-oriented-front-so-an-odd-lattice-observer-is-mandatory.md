# The full Jacobi comb annihilates the oriented front, so an odd lattice observer is mandatory

The even Jacobi Green cell cannot supply the reciprocal-odd front by itself.
The full integer comb kills that channel exactly.

## Two oriented fronts

At heat scale \(r>0\), define

\[
g_{z,r}^{+}(n)=e^{-\pi r(n+z)^2},
\qquad
g_{z,r}^{-}(n)=e^{-\pi r(n-z)^2}.
\]

Their full-comb readouts are

\[
\sum_{n\in\mathbb Z}g_{z,r}^{+}(n)=\Theta(z,r),
\]

and

\[
\sum_{n\in\mathbb Z}g_{z,r}^{-}(n)=\Theta(-z,r).
\]

Since the integer lattice is reflection invariant,

\[
\Theta(-z,r)=\Theta(z,r).
\]

Therefore the oriented difference satisfies

\[
\sum_{n\in\mathbb Z}
\left(
g_{z,r}^{+}(n)-g_{z,r}^{-}(n)
\right)
=0
\]

for every \(z\) and \(r\).

This is not a limiting degeneracy. It is exact cancellation at every finite
heat scale.

## Odd Jacobi current

Differentiating in the elliptic coordinate gives

\[
\partial_z\Theta(z,r)
=
-2\pi r
\sum_n(n+z)e^{-\pi r(n+z)^2}.
\]

It is odd under reflection:

\[
\partial_z\Theta(-z,r)
=
-\partial_z\Theta(z,r).
\]

At the unmarked seam,

\[
\partial_z\Theta(0,r)=0.
\]

Thus even retaining the odd current as a formal derivative does not produce a
nonzero scalar seam value. One needs its directed jet, a marked endpoint, or
another odd observer.

## Consequence for scalar Poisson sewing

The scalar comb pairing

\[
F\longmapsto\langle\Delta_{\mathbb Z},F\rangle
\]

is faithful on neither the two-front plane nor the odd Jacobi sector. It maps
the front pair to one even coordinate and annihilates their difference.

Therefore scalar Poisson naturality can establish the theta functional
equation while erasing the reciprocal orientation required by the Adams mixed
block.

## Minimal repairs

Three source-typed repairs are possible.

### Derivative comb

Use

\[
\Delta_{\mathbb Z}'
=
\sum_n\delta_n'.
\]

On a test function,

\[
\langle\Delta_{\mathbb Z}',f\rangle
=
-\sum_nf'(n).
\]

This observer is reflection odd and detects lattice flux. Fourier transport
sends it to a linearly weighted dual comb, so derivative-atom typing must be
retained.

### Marked or one-sided comb

Use a marked half-lattice, such as positive and negative labels retained as
separate ports. Their difference is odd. This breaks scalar reflection
invariance at the observer level while preserving the two-copy reciprocal
system.

### Endpoint jet

Retain \(\partial_z\Theta\) as an operator-valued boundary jet before
evaluation at \(z=0\). Its first transverse derivative can be nonzero even
though its seam value vanishes.

These constructions are not interchangeable until a source comparison
between their odd coordinates is proved.

## Smallest faithful observer

On the two-front source plane, define even and odd rows

\[
J_{\mathrm{even}}(f_+,f_-)=f_++f_-,
\]

\[
J_{\mathrm{odd}}(f_+,f_-)=f_+-f_-.
\]

The full comb realizes only \(J_{\mathrm{even}}\). A faithful local observer
must retain both rows, or an equivalent rank-two frame.

The minimal hostile is

\[
(f_+,f_-)=(1,-1).
\]

It is nonzero, has zero scalar comb readout, and represents pure orientation.

## Relation to the theta scale derivative

The reciprocal-odd companion \(\Phi'\) is odd in the scale coordinate \(u\).
The Jacobi front current is odd in the elliptic coordinate \(z\). These are
different odd representations.

The heat equation relates \(r\)-derivatives to even \(z\)-derivatives. It does
not identify \(\partial_u\) with \(\partial_z\). A further source cell must
compare scale-odd and front-odd channels. Equality of their scalar signs is
insufficient.

## Revised frontier

The even analytic Jacobi cell is closed. The next source constructor must
supply an odd lattice observer and prove:

1. reflection-odd covariance;
2. Fourier–Poisson transport with derivative atoms retained;
3. nonzero response on the two-front difference;
4. compatibility with the relative wall map;
5. comparison with the scale-odd theta companion;
6. boundedness and radical descent in the Jacobi rigging;
7. prime/grade attachment before scalar aggregation.

Until this observer exists, the mixed Green polarization remains rank
deficient.

No Adams type edge, boundary pencil, or coercivity statement is promoted.

## Source locators

- research/nima/the-jacobi-heat-green-identity-closes-the-even-completion-channel-after-zero-mode-reduction.md
- research/nima/theta-gaussian-vacuum-selection-produces-a-lattice-ward-current-not-yet-rh-orientation.md
- research/nima/theta-global-fourier-action-exists-boundary-observer-lift-is-missing.md
- research/nima/rh-seam-may-require-value-and-flux-observers.md
