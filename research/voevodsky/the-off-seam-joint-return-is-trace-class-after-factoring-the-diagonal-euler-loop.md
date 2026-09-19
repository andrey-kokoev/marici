# The off-seam joint return is trace class after factoring the diagonal Euler loop

Let `B` be the seam-weighted completed incidence.  On the declared weighted
arithmetic Hilbert space it is Hilbert--Schmidt, and its return `C=B^dagger` is
Hilbert--Schmidt in the reverse direction.  On any compact parameter set in a
history resolvent chart, write

\[
R(z)=C(A-z)^{-1}B.
\]

The ideal product rule gives

\[
\|R(z)\|_1
\le
\|C\|_2\,\|(A-z)^{-1}\|\,\|B\|_2.
\]

Hence `R(z)` is trace class, holomorphically and compact-locally in trace norm,
wherever the history resolvent is bounded.

For the diagonal Euler loop `L(z)`, strict off-seam Schur control gives a
uniform bound for `(I-L(z))^-1` on compact subsets of either admitted strict
chart. Therefore

\[
K(z)=(I-L(z))^{-1}R(z)
\]

is trace class there, with

\[
\|K(z)\|_1
\le
\|(I-L(z))^{-1}\|\,\|R(z)\|_1.
\]

This is stronger than the requested Schatten-three property.  Consequently
the relative Fredholm determinant `det(I-K(z))` exists and is holomorphic on
every strict off-seam resolvent chart.  The bare Euler factor remains in its
separate graded/determinant-line modality; trace-class control of `K` does not
turn `L` into a trace-class operator.

The argument does not cross the critical seam.  There the history resolvent may
meet continuous spectrum and `(I-L)^-1` loses its strict-chart bound.  A
limiting-absorption or rigged boundary-value theorem is still required, and no
identification of the resulting off-seam determinant with Xi follows from
ideal membership alone.
