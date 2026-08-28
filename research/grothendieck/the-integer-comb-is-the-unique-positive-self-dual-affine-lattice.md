# The Integer Comb Is the Unique Positive Self-Dual Affine Lattice

## Affine lattice family

Consider the positive affine comb

\[
\Delta_{\alpha,\beta}
=
\sum_{n\in\mathbb Z}
\delta_{\alpha(n+\beta)},
\qquad
\alpha>0.
\]

Under the Fourier convention used for the frontier current, Poisson summation
gives

\[
\widehat{\Delta_{\alpha,\beta}}
=
\frac1\alpha
\sum_{k\in\mathbb Z}
e^{2\pi i k\beta}
\delta_{k/\alpha}.
\]

## Positivity of the dual weights

For the Fourier image to remain a positive comb, every phase must be a
nonnegative real number. Since each phase has modulus one, this requires

\[
e^{2\pi i k\beta}=1
\]

for every integer \(k\). Hence

\[
\beta\in\mathbb Z.
\]

Such a translation merely reindexes the original lattice, so the affine shift
is trivial.

## Self-dual support

The primal support is

\[
\alpha\mathbb Z,
\]

while the dual support is

\[
\alpha^{-1}\mathbb Z.
\]

Equality of these lattices requires

\[
\alpha=1.
\]

Therefore, within the one-dimensional positive affine-lattice family, the
integer comb is the unique Fourier self-dual object, up to trivial integer
reindexing.

## Consequence for theta positivity

The reciprocal positivity mechanism of the Fourier-fixed frontier current is
not generic under lattice deformation:

- a nonintegral translation introduces signed or complex dual phases;
- a nonunit scale changes the lattice under Fourier transport;
- only the integer comb returns as the same positive observation boundary.

This passes the hostile deformation test proposed for the source explanation.
Self-Fourier current geometry alone is insufficient; the observation boundary
must also be the positive self-dual integer comb.

## Scope boundary

Uniqueness of the positive self-dual comb explains source rigidity and the
functional equation. It does not imply that its Mellin matrix coefficient has
no off-seam zeros. A canonical section can still vanish inside a rigid
self-dual system.

## Falsifier

The classification fails if some nontrivial pair \((\alpha,\beta)\) produces
the same positive comb after Fourier transformation. The phase and support
conditions exclude it.
