# Full interval energy is state norm, not Riemann overlap

## The distinguished transported state

Absorb the Mellin character into the arithmetic coefficient state:

\[
c_s=(n^{-s})_{n\ge1},
\qquad
s=\sigma+it.
\]

For \(\sigma>1/2\), its ordinary coefficient norm is

\[
\|c_s\|^2
=
\sum_{n\ge1}n^{-2\sigma}
=
\zeta(2\sigma).
\]

The full interval energy derived from the two-front tower is

\[
\mathcal E(c_s)
=
2\sum_{n\ge1}(\log n)n^{-2\sigma}.
\]

Therefore

\[
\mathcal E(c_s)
=
-\partial_\sigma\zeta(2\sigma).
\]

This is positive and finite throughout the open right half-sector. But it is
independent of \(t\).

## The observer is different data

The Riemann readout is not the norm of \(c_s\). In the Euler chamber it is the
overlap with the aggregation covector

\[
\langle\mathbf1,c_s\rangle
=
\sum_{n\ge1}n^{-s}.
\]

Outside that chamber the observer is a relative theta-heat distribution, not
an ordinary Hilbert vector. A zero is cancellation in this mixed
source–observer channel.

The full interval energy sees only

\[
|n^{-s}|^2=n^{-2\sigma}.
\]

It forgets every relative phase \(e^{-it\log n}\) responsible for scalar
cancellation.

## Minimal hostile witness

On two labels, the packets

\[
(1,1)
\quad\text{and}\quad
(1,-1)
\]

have identical coefficient magnitudes and therefore identical interval
energy. Against the aggregation observer, their readouts are two and zero.

Thus strict state energy does not imply nonvanishing overlap. The same defect
persists in arbitrarily large finite packets.

## Correction to the finite-null theorem

It remains true that any nonzero finite packet lying in a specified Mellin
observer kernel has positive interval energy. But that theorem does not
derive a conservation identity connecting the observer kernel to horizontal
spectral displacement. It only proves that the kernel contains no zero-energy
finite vector.

For RH one needs the stronger source-derived identity

\[
2\Re(s-\tfrac12)\,\mathcal E(c_s)
=
\text{completed mixed source–observer boundary flux}.
\]

The right side must vanish when the completed Riemann readout vanishes. No
such implication follows from the state norm alone.

## What the two-front result still contributes

The two-front construction remains valuable. It supplies:

- a canonical positive bulk density;
- exact primitive and valuation coefficients;
- a five-wall boundary atlas;
- the correct finite arithmetic energy domain.

The missing information is now sharply isolated: the incidence of the
relative theta observer with this positive state geometry.

That incidence must retain phases and cannot factor through the diagonal
norm. In matrix language, we have derived the positive diagonal block but not
the off-diagonal source–observer block whose determinant is the completed
section.

## Remaining gate

Construct the mixed two-front kernel

\[
\mathcal K_s(n,m;u)
\]

before diagonal compression. Its diagonal must recover the interval energy,
while contraction with the theta observer must recover the completed scalar
section. The decisive question is whether its Green identity has only the
already typed constant–delta and archimedean boundary terms.

The hostile test is phase reweighting: any proposed identity that depends
only on \(|c_n|\) cannot distinguish zero and nonzero overlaps and supplies no
RH information.

## Result

The full interval energy is exactly positive source-state norm geometry, not
the Riemann overlap. It is independent of spectral height and cannot orient
phase cancellation. The next object must be a mixed source–observer kernel
whose diagonal is the derived energy and whose boundary contraction is the
completed theta readout.
