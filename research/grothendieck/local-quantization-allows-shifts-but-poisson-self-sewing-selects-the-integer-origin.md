# Local quantization allows shifts but Poisson self-sewing selects the integer origin

## Shifted positive currents

Fix (0\leq\beta<1). On the ray beginning at \(\beta\), use the shifted
right-endpoint quantizer with cells

\[
[\beta+n-1,\beta+n],
\qquad n\geq1.
\]

Its Gaussian Haar deficit is

\[
\Omega_\beta(t)
=\int_\beta^\infty e^{-\pi x^2t}\,dx
-\sum_{n\geq1}e^{-\pi(\beta+n)^2t}.
\]

Exactly as for the integer origin,

\[
\Omega_\beta(t)
=\sum_{n\geq1}\int_{\beta+n-1}^{\beta+n}
\left(e^{-\pi x^2t}-e^{-\pi(\beta+n)^2t}\right)\,dx>0.
\]

Thus local monotone quantization does not select the integer origin. Every
shift on the positive fundamental interval carries the same cellwise
positivity mechanism.

## Fourier transform of the shifted comb

Use the convention

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
\]

For the shifted Dirac comb

\[
\Delta_{\mathbb Z+\beta}
=\sum_{n\in\mathbb Z}\delta_{n+\beta},
\]

Poisson summation gives

\[
\mathcal F\Delta_{\mathbb Z+\beta}
=e^{-2\pi i\beta\xi}\Delta_{\mathbb Z}(\xi).
\]

The Fourier transform therefore separates the two pieces that translation
had combined:

- its support returns to the unshifted dual lattice;
- its shift survives as a character on that dual lattice.

For the transformed comb to be a scalar multiple of the original shifted
comb, their supports must agree:

\[
\mathbb Z=\mathbb Z+\beta.
\]

This forces \(\beta=0\) modulo one. At that value the character is trivial and
the comb is Fourier-fixed with eigenphase one.

Hence the unshifted integer origin is uniquely selected among translated
unit lattices by same-object Poisson sewing.

## Constructibility versus coherence

The shifted family cleanly separates two questions.

Local constructibility asks whether the continuum-to-endpoint transport has
positive loss. Every \(\beta\in[0,1)\) passes.

Global coherence asks whether the quantized boundary returns to the same
labelled object under Fourier transport. Only \(\beta=0\) passes without
doubling the object to include a separate character-decorated dual comb.

The integer origin is therefore not selected by positivity. It is selected by
closure of the comparison under the source symmetry.

## The boundary carrier also detects the shift

At \(\beta=0\), the Haar comparison begins at the fixed point (x=0), and its
half-Mellin contribution produces the rational terms that cancel the
completion carrier exactly.

For \(\beta\neq0\), the continuum begins at a displaced boundary. Its Mellin
transform contains an incomplete boundary contribution rather than the same
universal rational carrier. Thus the shifted source fails closure twice:

1. Fourier transport produces an independently typed character channel;
2. the archimedean boundary no longer matches the original completion
   carrier.

These failures occur before inspecting any zero set.

## Consequence for hostile models

A shifted positive quantization current is not a valid same-type replacement
for the integer theta source. To become source-complete, it must be enlarged
to a primal-support and dual-character pair with additional boundary data.
Its scalar transform may still be mathematically interesting, but it belongs
to a different constructor type.

This proves a limited source rigidity theorem:

> Among translated unit combs, the unshifted integer comb is the unique object
> combining positive one-sided quantization, Fourier self-sewing without an
> extra character port, and the original completion boundary.

It does not prove RH because other non-translation hostile sources may share
all three properties.

## Operator stimulus

The operator's multi-tower proposal suggested that a comparison surviving
locally might fail at a higher coherence rung. The shifted lattice realizes
that pattern exactly: the input and output quantization towers exist and are
positive, but the control tower acquires a character defect under Fourier
transport unless the origin is integral.
