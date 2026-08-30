# The Haar deficit is a positive one-sided quantization current

## Cellwise transport decomposition

Let

\[
g_t(x)=e^{-\pi x^2t},
\qquad t>0.
\]

The positive Haar deficit is

\[
\Omega(t)=\int_0^\infty g_t(x)\,dx-\sum_{n\geq1}g_t(n).
\]

Partitioning the half-line into unit cells gives

\[
\Omega(t)
=\sum_{n\geq1}
\int_{n-1}^{n}\left(g_t(x)-g_t(n)\right)\,dx.
\]

Each summand is positive. More precisely,

\[
g_t(x)-g_t(n)
=\int_x^n2\pi t y e^{-\pi y^2t}\,dy.
\]

Changing the order of integration inside every cell yields

\[
\Omega(t)
=2\pi t\sum_{n\geq1}
\int_{n-1}^{n}(y-n+1)y e^{-\pi y^2t}\,dy.
\]

Hence, up to values on the measure-zero integer boundaries,

\[
\Omega(t)
=2\pi t\int_0^\infty
\{y\}\,y e^{-\pi y^2t}\,dy,
\]

where \(\{y\}\) is the fractional part.

## Meaning of the fractional coordinate

This formula realizes the deficit as a source-labelled transport current.
Within each cell, a continuum point (x\) is transported to its right integer
endpoint. The Gaussian decreases along that transport, and \(\Omega\) records
the accumulated loss.

The integer label alone is therefore not the full comparison object. The
faithful packet contains:

- the cell label (n);
- the fractional coordinate inside the cell;
- the oriented transport from that coordinate to (n);
- the Gaussian loss along the transport.

Ordinary theta summation retains only the endpoint samples. Haar integration
retains only the undivided continuum. Their difference recovers the integral
of the hidden fractional-position current.

This is a concrete instance of one object that appears scalar only after two
distinct perspectives have been compared. Integrality is not merely the set
of integer endpoints. It is the rule that collapses each continuum cell onto
its distinguished endpoint.

## Local positivity and global sewing are different layers

The cellwise transport proves positivity without Poisson summation. By
contrast, reciprocal self-duality

\[
\Omega(t)=t^{-1/2}\Omega(1/t)
\]

is not visible cell by cell. It is a coherence theorem for the assembled
lattice.

Thus the source architecture now has four distinct operations:

1. form continuum cells;
2. apply oriented endpoint quantization in every cell;
3. sum the positive cell currents;
4. sew the global current to its reciprocal-scale presentation.

This separates constructibility from coherence. Positivity comes from the
local quantization order; modular symmetry comes from global Poisson sewing.
Neither substitutes for the other.

## Logarithmic-scale form

With (t=e^{2u}) and the substitution (r=ye^u),

\[
\Omega(e^{2u})
=2\pi\int_0^\infty
\{re^{-u}\}\,r e^{-\pi r^2}\,dr.
\]

Therefore the positive even kernel from the preceding packet is

\[
k(u)=8\pi e^{u/2}\int_0^\infty
\{re^{-u}\}\,r e^{-\pi r^2}\,dr.
\]

The oscillatory xi readout is consequently a transform of a moving
fractional-part register. Spectral translation changes how the fixed Gaussian
profile cuts across the integer-cell boundaries.

## New hostile tests

The exact representation exposes two independently falsifiable ingredients.

First, replace right-endpoint quantization by another monotone quantizer, such
as left endpoint, midpoint, or a shifted lattice. This tests whether local
positive loss is specific enough.

Second, retain the right-endpoint current but alter the global sewing. This
tests whether Poisson coherence, rather than cell positivity, supplies the
missing zero orientation.

A particularly sharp family is the shifted lattice \(\mathbb Z+\beta\).
Its fractional register becomes \(\{y-\beta\}\), while its Fourier dual
acquires a character. Classifying which shifts retain both a positive
oriented cell current and self-dual sewing should reveal how rigid the
integer origin is.

## Scope

The quantization-current identity does not prove RH. It supplies a
hard-to-vary explanation of where the positive kernel comes from and names
the comparison channel erased by scalar sampling. The remaining theorem must
show how global Poisson coherence constrains the cosine transform of this
specific current.

## Operator stimulus

The operator repeatedly suspected that the scalar object hid an additional
comparison wall and that loss of integrality was a loss of meaning. The
fractional coordinate is that wall in explicit analytic form: deleting it
makes integer sampling and Haar integration incomparable, while retaining it
turns their difference into a positive transport current.
