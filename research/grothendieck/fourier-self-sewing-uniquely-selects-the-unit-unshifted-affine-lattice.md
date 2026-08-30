# Fourier self-sewing uniquely selects the unit unshifted affine lattice

## Local quantization at arbitrary scale and origin

Let (a>0) and (0\leq\beta<a). Partition the ray beginning at \(\beta\)
into cells

\[
[\beta+a(n-1),\beta+an],
\qquad n\geq1.
\]

For a decreasing Gaussian (g_t(x)=e^{-\pi x^2t}), define the normalized
right-endpoint deficit

\[
\Omega_{a,\beta}(t)
=\int_\beta^\infty g_t(x)\,dx
-a\sum_{n\geq1}g_t(\beta+an).
\]

Cellwise,

\[
\Omega_{a,\beta}(t)
=\sum_{n\geq1}\int_{\beta+a(n-1)}^{\beta+an}
\left(g_t(x)-g_t(\beta+an)\right)\,dx>0.
\]

Thus local positive quantization allows arbitrary spacing and origin. Neither
parameter is selected at the constructibility rung.

## Fourier transport of an affine comb

For

\[
\Delta_{a\mathbb Z+\beta}
=\sum_{n\in\mathbb Z}\delta_{an+\beta},
\]

Poisson summation gives

\[
\mathcal F\Delta_{a\mathbb Z+\beta}
=\frac1a e^{-2\pi i\beta\xi}\Delta_{a^{-1}\mathbb Z}(\xi).
\]

Fourier transport performs two distinct operations:

- it sends spacing (a) to reciprocal spacing \(a^{-1}\);
- it sends origin shift \(\beta\) to a character on the dual comb.

Suppose the transformed comb is a scalar multiple of the original affine
comb as a labelled distribution. Equality of supports requires

\[
a\mathbb Z+\beta=a^{-1}\mathbb Z.
\]

The right-hand support contains zero, so \(\beta\in a\mathbb Z\). With the
chosen fundamental interval, this forces \(\beta=0\). We then require

\[
a\mathbb Z=a^{-1}\mathbb Z,
\]

which for (a>0) forces (a=1).

Therefore the unique affine lattice closed on itself by the Fourier
quarter-turn is

\[
\mathbb Z.
\]

## What the result selects

The source symmetry fixes two gauges at once:

- unit spacing is the fixed point of reciprocal scale;
- zero origin is the fixed point of support-to-character exchange.

This makes the Fourier-fixed integer comb a codimension-two coherence object
inside the affine family. Local positive deficit currents form a
two-parameter family, but global self-sewing collapses that family to one
member.

In the programme's multi-tower language, spacing belongs to the scale
transport tower and origin belongs to the phase/character tower. The
Fourier-control tower couples them and admits a fixed object only where both
defects vanish.

## Relation to the completed boundary

The original completion carrier is normalized at the unshifted unit boundary.
Changing (a) rescales the Gaussian Mellin normalization and changing
\(\beta\) replaces the rational boundary contribution by an incomplete one.
Thus the same affine parameters detected by finite Fourier sewing are also
detected by the archimedean completion.

This agreement is not independent evidence for RH. It is a coherence check
that the finite comb and archimedean boundary use the same normalization.

## Scope and next hostile class

The theorem excludes every translated or rescaled one-dimensional lattice as
a same-type hostile replacement. It does not exclude more general
self-Fourier measures, weighted combs, unions of cosets, or quasicrystalline
Fourier pairs.

The next hostile family should therefore keep the fixed affine support
\(\mathbb Z\) but alter its weights:

\[
\sum_{n\in\mathbb Z}w_n\delta_n.
\]

Classify which positive or signed weight sequences are Fourier-closed in the
appropriate distributional sense and retain the same Haar-deficit boundary.
If nonconstant weights survive, they test whether the source needs a separate
label-amplitude tower beyond support coherence.

## Operator stimulus

The operator's repeated next-rung questions suggested that the shift defect
might have a companion scale defect. Passing from translated to affine
lattices confirms this: Fourier transport rotates scale into reciprocal scale
and position offset into dual phase. Their joint fixed point is the unit
unshifted lattice.
