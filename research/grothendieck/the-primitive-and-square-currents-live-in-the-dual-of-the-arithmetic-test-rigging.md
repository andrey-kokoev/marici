# The Primitive and Square Currents Live in the Dual of the Arithmetic Test Rigging

## The completed test space

Let `P` denote the primes and begin with finitely supported coefficient
packets.  Give them the saturated seminorms

\[
q_\delta(c)^2=\sum_{p\in P}p^{2\delta}|c_p|^2,
\qquad \delta>0,
\]

on both reciprocal sheets.  Their projective completion is the arithmetic
rapid-decay space

\[
\mathcal S_P=\bigcap_{\delta>0}\ell^2(P,p^{2\delta}).
\]

Finite cutoffs converge in every seminorm.  Mellin translation

\[
(M_tc)_p=p^{it}c_p
\]

is isometric for every `q_delta`, and the reciprocal sheet rotation remains
continuous.  Thus the two source transports extend without choosing a single
Hilbert norm.

## Boundary currents are continuous dual coordinates

Three apparently singular rows are continuous on this test space.

The augmentation row obeys, for any `delta > 1/2`,

\[
\left|\sum_p c_p\right|
\le q_\delta(c)
\left(\sum_p p^{-2\delta}\right)^{1/2}.
\]

The primitive row obeys, for every `delta > 0`,

\[
\left|\sum_p \frac{\log p}{\sqrt p}c_p\right|
\le q_\delta(c)
\left(\sum_p\frac{(\log p)^2}{p^{1+2\delta}}\right)^{1/2}.
\]

Likewise the prime-square row with coefficient `(log p)/p` is continuous for
every positive `delta`.  These estimates are source-native and uniform in the
finite cutoff.

The corresponding coefficient sequences are generally not elements of
`S_P`.  In particular, the primitive coefficient vector `p^(-1/2) log p`
fails every positive weighted state norm.  The primitive current is therefore
a covector in the strong dual, not a state vector secretly waiting for a
larger Hilbert completion.

## Rigged interpretation

The finite pro-Gram packet completes as a rigging

\[
\mathcal S_P\subset \mathcal H_0\subset\mathcal S_P',
\qquad
\mathcal H_0=\ell^2(P),
\]

duplicated over the reciprocal sheets and enlarged by the connected-tail,
seam, and archimedean graph coordinates.  The square-grade Hilbert port lives
at the middle level.  Primitive and augmentation currents live naturally in
the dual level.  Fourier saturation transports each typed level; it does not
identify a current with a state.

This removes the apparent completion escape at the level of boundary
observability: a sequence converging to zero in the projective test topology
is sent to zero by every declared boundary current.  What remains unresolved
is stronger and more precise: the zero-state supplied by the completed theta
transform must be shown to belong to the domain on which the dual Green
pairing is defined, and the reciprocal mapping-cone identity must extend by
duality to that domain.

## Hostile boundary

The physical primitive coefficient packet cannot be admitted as an ordinary
test state.  Any proof that takes its Hilbert norm, applies a bounded state
operator to it, or uses a Riesz identification between it and a vector has
crossed the rigging without authority.

Conversely, merely declaring all arithmetic data distributional is too weak.
The next theorem must construct a common graph domain `D` satisfying

\[
\mathcal S_P\subset D\subset\mathcal S_P'
\]

on which endpoint traces, the doubled differential, and all boundary currents
are jointly continuous and the relative Green identity is closed.

## Result

The restricted-product topology has a canonical first completion: a
Fourier- and Mellin-stable arithmetic test rigging whose primitive, square,
and augmentation rows are continuous with their correct regularity types.
The completion obstruction is no longer loss of these currents.  It is the
construction of the common graph domain carrying the zero-state and the
dual-valued Green identity without an illicit Riesz collapse.

