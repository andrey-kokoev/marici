# The Bordered Valuation System Has All Transmission Zeros on Its Stability Wall

Scope correction: the wall in this theorem is the unweighted local shift wall
\(|p^{-s}|=1\), namely \(\Re s=0\). It is not the half-density global Hilbert
wall \(\Re s=1/2\). Entry 3959 performs the source-Hilbert retyping and shows
that the local zeros then lie strictly outside the closed critical stability
disk.

## Source-derived Rosenbrock matrix

On the truncated valuation chain (V_{p,N}\), let

\[
A_N(a)=I-aS_N,
\qquad
B=e_0,
\qquad
C=\varepsilon_N.
\]

The input, internal state, and output port form the bordered system matrix

\[
\mathcal R_N(a)
=
\begin{pmatrix}
A_N(a)&-B\\
C&0
\end{pmatrix}.
\]

Every constituent is source-derived: (S_N\) is valuation transport, (e_0\)
is primitive endpoint incidence, and \(\varepsilon_N\) is valuation-orbit
augmentation.

## Determinant equals transfer

Since \(\det A_N(a)=1\), the Schur-complement identity gives

\[
\det\mathcal R_N(a)
=C A_N(a)^{-1}B
=1+a+\cdots+a^N.
\]

Thus Entry 3957's distinction is exact:

- the internal differential determinant is one;
- the bordered system determinant is the boundary transfer polynomial.

The zero-to-kernel bridge becomes legitimate only after including the
independently derived source ports.

## Transmission-zero state

If

\[
g_N(a)=1+a+\cdots+a^N=0,
\]

then

\[
x=A_N(a)^{-1}Bu,
\qquad
u\ne0
\]

satisfies

\[
A_N(a)x-Bu=0,
\qquad
Cx=0.
\]

The internal state is driven by a nonzero source input but is invisible at the
output. This is a genuine invariant or transmission zero, not internal
cohomology.

## Exact wall theorem

The transfer polynomial is

\[
g_N(a)=\frac{1-a^{N+1}}{1-a}.
\]

Its zeros are precisely the nontrivial \((N+1)\)-st roots of unity. Therefore

\[
g_N(a)=0
\quad\Longrightarrow\quad
|a|=1.
\]

The open stability disk \(|a|<1\), where the infinite shift resolvent exists,
contains no transmission zero. Every finite-chain zero lies exactly on its
loss-of-stability wall.

## Explanation and hostile test

The boundary confinement is forced by three source facts:

1. one directed valuation orbit;
2. equal augmentation of every orbit state;
3. endpoint input at valuation zero.

Changing the observation to arbitrary weights replaces (g_N\) by

\[
w_0+w_1a+\cdots+w_Na^N,
\]

whose zeros need not lie on the unit circle. Thus the wall theorem is not a
generic property of finite colligations or positive coefficients. It is a
consequence of the source-fixed equal augmentation.

## Global transfer target

This is a complete finite-place transfer-zero model, but its unweighted wall
is not the RH wall:

1. ordinary states exist in an open stability sector;
2. the scalar readout is a bordered transfer coefficient;
3. a zero is a nontrivial driven state invisible at the boundary;
4. source coherence confines every such zero to the stability wall.

The remaining global theorem is not to repeat this argument prime by prime.
It is to derive the completed theta/Tate Rosenbrock operator and identify the
global analogue of equal augmentation after restricted-product and
archimedean sewing. Cross-prime interference is precisely where the local
root-of-unity argument stops.
