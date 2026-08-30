# Fourier-conjugated Tate trace is Hankel and generates the full moment boundary

## Question

The global Gaussian–comb cell exists, but its arithmetic observer lift is
missing.  What is the additive Fourier operator after restriction to the
multiplicative real trace, and what boundary coordinates are required for
that operator to act continuously?

## The two-sign logarithmic trace

For a Schwartz function φ on the real additive carrier, retain both signs and
write

\[
h_\sigma(q)=\phi(\sigma e^q),
\qquad
\sigma\in\{+1,-1\}.
\]

This is the archimedean component of the idelic trace before Hilbert
completion.  It is injective because the nonzero reals are dense and φ is
continuous.

Let (K) be additive Fourier transform conjugated through this trace.  A
change of variables (y=\tau e^r) gives the exact formula

\[
(Kh)_\sigma(q)
=
\sum_{\tau=\pm1}
\int_{\mathbb R}
e^r
e^{-2\pi i\sigma\tau e^{q+r}}
h_\tau(r)\,dr.
\]

The kernel depends on (q+r), so (K) is a two-sign Hankel operator in log
coordinates.  It is not a translation convolution and is not reconstructed
from a scalar Tate integral.

## Exact Mellin covariance

Additive unitary dilation becomes

\[
(V_ah)_\sigma(q)=e^{a/2}h_\sigma(q+a).
\]

The Hankel formula gives

\[
KV_a=V_{-a}K.
\]

Thus the multiplicative trace realizes the metaplectic reversal exactly:
Fourier transport reverses Mellin translation.  This is the requested
operator-valued trace-naturality square at the real place.

## The endpoint becomes a global moment tower

The endpoint (q\to-\infty) corresponds to (x=e^q\to0).  Expanding the
kernel in (x) gives

\[
e^r e^{-2\pi i\sigma\tau x e^r}
=
\sum_{k\ge0}
\frac{(-2\pi i\sigma\tau)^k}{k!}
x^k e^{(k+1)r}.
\]

Therefore the (k)-th endpoint jet of (Kh) is the global moment

\[
\partial_x^k(Kh)_\sigma(0)
=
(-2\pi i\sigma)^k
\sum_{\tau=\pm1}\tau^k
\int_{\mathbb R}e^{(k+1)r}h_\tau(r)\,dr.
\]

Fourier transport converts a local endpoint coordinate into a moment of the
entire logarithmic trace.  No fixed finite endpoint-jet packet is invariant
on the full Schwartz source: retaining orders through (m) leaves order
(m+1) as the first missing Fourier boundary coordinate.

This is not an argument for adding arbitrary walls.  The full moment tower is
forced by the Taylor expansion of the source-derived kernel.

## Relation to the typed boundary vessel

The archimedean determinant line is sufficient for scalar completed-zeta
reconstruction.  It is not sufficient for an operator-valued Fourier trace.
The latter requires a rigged moment boundary or an equivalent generating
function that retains every endpoint derivative continuously.

This does not merge the arithmetic ports.  The primitive and square currents
remain in their Mellin-analytic and Hilbert grades, and the connected tail
remains absolute-summable.  The new result says that the archimedean port is
itself infinite-rank before determinant compression.

Consequently the observer object has the shape

\[
O=
O_{k=1}
\oplus O_{k=2}
\oplus O_{\ge3}
\oplus O_{\mathrm{seam}}
\oplus O_{\infty}^{\mathrm{mom}},
\]

where (O_{\infty}^{\mathrm{mom}}) is a moment rigging rather than one scalar
line.  The scalar archimedean determinant is a downstream compression of
this port.

## First observer-level falsifier

Take two Schwartz traces having the same first (m) moments but different
((m+1))-st moments.  Their Fourier-conjugated traces have identical endpoint
jets through order (m) and different next jets.  Hence every finite jet
observer has a nontrivial Fourier-invisible fiber.

The full trace square fails if the proposed boundary topology:

- retains only finitely many archimedean jets;
- treats the determinant line as the complete Fourier boundary state;
- omits one sign component;
- or makes the Hankel moment functionals discontinuous.

## Scope

The real-place Hankel kernel, Mellin reversal, and full moment-tower
requirement are exact.  The nonarchimedean primitive and square incidences
have not yet been assembled with this real-place operator, and no RH
consequence follows.

## Result

The additive-to-multiplicative trace square can be written explicitly at the
real place.  Its Fourier operator is a two-sign Hankel transform and its
boundary action generates every global moment.  Thus the previously declared
single archimedean line is a scalar determinant compression, not the faithful
operator port.  Completion-level Fourier naturality requires the full
archimedean moment rigging.
