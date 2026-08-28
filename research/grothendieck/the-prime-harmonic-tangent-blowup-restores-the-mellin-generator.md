# The Prime-Harmonic Tangent Blowup Restores the Mellin Generator

## Blow up the cutoff boundary

For each cutoff \(X\), define a measure on \((0,1]\) by

\[
\nu_X=
\sum_{p\le X}\frac1p
\delta_{\log p/\log X}.
\]

The coordinate

\[
y=\frac{\log p}{\log X}
\]

records prime scale relative to the moving Euler boundary.  The total mass of
\(\nu_X\) is the divergent prime-harmonic mass \(H_X\), so these are not
probability measures.

For every continuous function \(f\) compactly supported away from \(0\), the
prime number theorem and partial summation give

\[
\int f(y)\,d\nu_X(y)
\longrightarrow
\int_0^1 f(y)\frac{dy}{y}.
\]

Thus

\[
\nu_X
\longrightarrow
\nu_\partial,
\qquad
d\nu_\partial(y)=\frac{dy}{y},
\]

vaguely on \((0,1]\).

The measure \(dy/y\) is the canonical tangent measure of prime-harmonic
escape.  Its infinite mass at \(y=0\) is precisely the grade-zero corona from
Entries 3936--3938.

## Exact jet moments

For every integer \(r\ge1\),

\[
\int_0^1 y^r\frac{dy}{y}=\frac1r.
\]

The finite prime moments converge to these values:

\[
\sum_{p\le X}\frac1p
\left(\frac{\log p}{\log X}\right)^r
\longrightarrow
\frac1r.
\]

Equivalently,

\[
\sum_{p\le X}\frac{(\log p)^r}{p}
\sim
\frac{(\log X)^r}{r}.
\]

The incompatible derivative scales from Entry 3939 are therefore not
arbitrary divergences.  They are the moments of one source-derived
sigma-finite boundary measure.

Grade zero remains divergent:

\[
\int_0^1\frac{dy}{y}=\infty.
\]

Every positive jet grade is finite.  This is the precise filtered structure
that a single Hilbert graph norm could not retain.

## Microscopic Mellin transport

Fixed vertical shifts become mutually orthogonal in the macroscopic Haar
corona.  On the tangent chart, scale the shift with the cutoff:

\[
t_X=\frac{\tau}{\log X}.
\]

Then

\[
p^{-it_X}
=\exp\!\left(-i\tau\frac{\log p}{\log X}\right)
=e^{-i\tau y}.
\]

Hence the limiting tangent action on

\[
L^2\!\left((0,1],\frac{dy}{y}\right)
\]

is

\[
(W_\tau f)(y)=e^{-i\tau y}f(y).
\]

Unlike the macroscopic action, \(\tau\mapsto W_\tau\) is strongly continuous.
Its self-adjoint generator is multiplication by \(y\).

Thus the Mellin generator is not destroyed absolutely.  It survives on the
next blowup of the corona, after simultaneously rescaling spectral displacement
and prime position.

## Two-level completion

The completed primitive object cannot be one Hilbert space with one vacuum.
It has at least two coupled levels:

1. a grade-zero Haar corona retaining finite Mellin shifts but no derivative;
2. a tangent chart with measure \(dy/y\) retaining microscopic continuous
   transport and every positive jet moment.

The constant function is not square-integrable in the tangent chart, while
\(y^r\) is square-integrable for every \(r>0\).  Therefore the tangent chart
does not replace the corona vacuum.  It is a relative boundary sector attached
to it.

This is the operator meaning of the earlier regularity tower: the primitive
state is distributional at grade zero, while its positive logarithmic jets are
ordinary tangent vectors after blowup.

## Source covariance

The construction uses only:

- the actual Euler cutoff \(X\);
- the prime-harmonic weight \(1/p\);
- the logarithmic label coordinate;
- Mellin transport.

No moment normalization is fitted independently at each order.  The single
coordinate \(y=\log p/\log X\) and single measure \(dy/y\) generate the whole
tower \(1/r\).

## Remaining gate

The tangent blowup restores a continuous generator, but it has not yet been
sewn to the archimedean gamma channel or reciprocal theta sector.  The next
theorem must determine how Fourier--Tate reflection acts on \(y\), on the
singular endpoint \(y=0\), and on the tangent generator.

The decisive compatibility question is whether the completed boundary current
uses the direct sum of the Haar corona and tangent chart, or a nontrivial
extension in which the Mertens finite part is the connecting map.

The smallest falsifier is a proposed completion that either makes the constant
mode square-integrable in \(dy/y\) without a source counterterm or discards the
grade-zero mass while claiming to reconstruct finite Euler cutoffs.  Either
move erases one of the two required levels.
