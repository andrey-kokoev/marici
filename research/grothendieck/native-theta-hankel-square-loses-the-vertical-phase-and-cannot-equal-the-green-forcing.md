# Native theta Hankel square loses the vertical phase and cannot equal the Green forcing

## Question

After the arithmetic inverse-frequency lift becomes abelian, Hardy compression
is the remaining noncommutative operation.  Does the source-native theta
symbol make the doubled Green forcing an ordinary positive Hankel square?

## The source-native causal symbol

Let

\[
h_z(q)
=
\mathbf 1_{q\ge0}f(q)e^{zq}
\]

and define its Fourier symbol

\[
\phi_z(\xi)
=
\widehat h_z(\xi)
=
A(z-i\xi).
\]

This symbol is fixed by the half-line theta source and character transport.  It
is not reconstructed from the completed divisor.

Compressing multiplication by \(\phi_z\) to the Hardy space gives the
Wiener--Hopf operator (T_{\phi_z}).  The complementary Hankel operator has,
up to the Fourier normalization, kernel

\[
K_z(x,y)
=
f(x+y)e^{z(x+y)},
\qquad x,y\ge0.
\]

## Canonical positive defect

The Toeplitz multiplicativity defect is

\[
T_{|\phi_z|^2}
-
T_{\bar\phi_z}T_{\phi_z}
=
H_{\phi_z}^*H_{\phi_z}
\ge0.
\]

Its Hilbert--Schmidt mass is

\[
\lVert H_{\phi_z}\rVert_{\mathrm{HS}}^2
=
\int_0^\infty
t f(t)^2 e^{2\Re(z)t}
\,dt.
\]

The imaginary part of (z) cancels completely.

More strongly, writing (z=\sigma+i\tau), the phase of the Hankel kernel is

\[
e^{i\tau(x+y)}.
\]

It is removed by diagonal unitaries on the source and target Hardy spaces.
Thus every unitary invariant of the positive Hankel square depends on
\(\sigma\) but not on \(\tau\).

## Mismatch with the Green forcing

The doubled Green forcing is

\[
\Re\mathcal K(\sigma+i\tau)
=
\int_0^\infty
\rho(d)
\sinh(\sigma d)
\cos(\tau d)
\,dd.
\]

Its vertical oscillation is essential.  Therefore it cannot equal:

- the positive Hankel square (H_{\phi_z}^*H_{\phi_z});
- its trace or Hilbert--Schmidt norm;
- any unitary-invariant spectral functional of that square;
- or the difference of the corresponding reciprocal-sheet norms, which also
  loses \(\tau\).

The native theta Hankel square and the Green forcing have different variance
types.

## What compression still retains

The full, uncompressed matrix coefficient of reciprocal Hankel blocks can
retain relative phase.  For example, cross-sheet terms of the form

\[
H_{\phi_z}^*H_{\phi_{-\bar z}}
\]

need not be positive and need not lose \(\tau\).  But such a mixed block must
be derived from the doubled source incidence.  It is not the canonical
Toeplitz positivity defect.

This agrees with the model-space warning: positive Toeplitz defects naturally
count interior zeros rather than exclude them.  The RH-bearing object, if it
exists in this language, must be a typed reciprocal cross-sheet matrix
coefficient plus its explicit DC boundary channel.

## Falsifiers

Any proposed equality between the Green forcing and a positive Hankel square
fails immediately if its right-hand side is invariant under changing
\(\tau\) while the left-hand side is not.

A surviving cross-sheet proposal must reproduce the factor

\[
\cos(\tau d)
\]

on a two-shell source and must retain the zero-frequency archimedean endpoint
without a fitted scalar term.

## Result

The theta-native Hardy symbol is (A(z-i\xi)), but its canonical positive
Hankel square loses the vertical spectral phase.  It cannot be the completed
Green forcing.  The simple Toeplitz-positivity route is closed; only a
source-derived reciprocal cross-sheet compression remains possible.
