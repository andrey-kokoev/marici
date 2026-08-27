# The Tate ratio and product are birational shadows of two faithful quadratures

## The local amplitude pair

For \(z=s-1/2\), define

\[
D_+(z)=1-p^{-1/2}p^{-z},
\qquad
D_-(z)=1-p^{-1/2}p^z.
\]

Reciprocal reflection exchanges the two amplitudes:

\[
D_+(-z)=D_-(z).
\]

The ratio and product are

\[
\Gamma=\frac{D_+}{D_-},
\qquad
P=D_+D_-.
\]

They encode phase comparison and symmetric magnitude away from their
divisors.

## Birational failure at the divisor

Formally,

\[
D_+^2=P\Gamma,
\qquad
D_-^2=\frac{P}{\Gamma}.
\]

Thus reconstruction requires square-root choices even where both expressions
are defined. More seriously, if \(D_+=0\) and \(D_-\neq0\), then

\[
P=0,
\qquad
\Gamma=0.
\]

Every pair \((0,c)\) with \(c\neq0\) has the same ratio–product value
\((0,0)\). The fiber is infinite. Ratio and product therefore lose exactly
the complementary amplitude needed at a divisor.

This is unacceptable for a zero-confinement argument: a readout cannot
explain a zero after discarding the surviving channel.

## Faithful linear quadratures

Retain instead

\[
T=D_++D_-,
\qquad
A=D_+-D_-.
\]

They reconstruct the labelled amplitudes linearly:

\[
D_+=\frac{T+A}{2},
\qquad
D_-=\frac{T-A}{2}.
\]

Reciprocity acts diagonally by parity:

\[
T(-z)=T(z),
\qquad
A(-z)=-A(z).
\]

The nonlinear invariants are derived shadows:

\[
P=\frac{T^2-A^2}{4},
\qquad
\Gamma=\frac{T+A}{T-A}
\]

where the denominator is nonzero.

## Seam geometry

On \(\Re z=0\), one has

\[
D_-(z)=\overline{D_+(z)}.
\]

Consequently,

\[
T=2\Re D_+,
\qquad
A=2i\Im D_+.
\]

The even and odd channels are precisely the two real quadratures of the
local amplitude. Neither is redundant. A scalar cancellation in one
quadrature need not destroy the other.

## Categorical correction

The ratio–product pair is a quotient chart on the two-amplitude object, not
its faithful normal form. Its singularity at divisors is the algebraic
version of finite-to-one not being one-to-one.

The correct pullback is therefore

\[
(P,\Gamma)
\longleftarrow
(T,A)
\longleftrightarrow
(D_+,D_-).
\]

Any determinant, Green current, or Clifford comparison used for RH must be
constructed before the leftward compression.

## Global next gate

Construct the restricted product of the labelled two-quadrature packets and
the archimedean pair. Then test whether the complete scalar section is a
specific projection of this faithful amplitude object and whether an
off-seam scalar zero would leave a forbidden nonzero complementary
quadrature.

The hostile falsifier is immediate: any proposed global invariant that maps
all packets \((0,c)\) to one state is not faithful on the divisor and cannot
support zero confinement.

## Result

Tate ratio and product are birational compressions that become unfaithful at
zeros. The even sum and odd difference are globally faithful linear
quadratures and remain meaningful on the divisor. The next-level RH carrier
must retain both before forming scalar invariants.
