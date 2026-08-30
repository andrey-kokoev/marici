# Theta half-density is the relative Haar interface but not a zero-confinement law

## Bounded question

What remains of the critical half-density after atom, coefficient, measure,
and readout are transported together between the additive and multiplicative
Haar sectors?

## The two Hilbert spaces

On the positive real line, the additive and multiplicative spaces are

\[
\mathcal H_{+}=L^2(\mathbb R_{>0},dx),
\qquad
\mathcal H_{\times}=L^2(\mathbb R_{>0},dx/x).
\]

Define the half-density transform

\[
(Jf)(x)=x^{1/2}f(x).
\]

Then

\[
\|Jf\|_{\mathcal H_{\times}}^2
=\int_0^\infty|x^{1/2}f(x)|^2\frac{dx}{x}
=\int_0^\infty|f(x)|^2dx.
\]

Thus (J) is unitary. The exponent (1/2) is forced by the Radon--Nikodym
ratio between additive and multiplicative Haar measure.

## Complete dilation transport

The additive unitary dilation is

\[
(D_af)(x)=a^{1/2}f(ax),
\qquad a>0.
\]

Transporting it through (J) gives

\[
JD_aJ^{-1}g(x)=g(ax).
\]

So additive dilation becomes ordinary multiplicative translation. No extra
diagonal weight remains after the state and measure are transported together.

## Mellin pairing and the surviving cocycle

The Mellin readout is

\[
\mathcal M f(s)=\int_0^\infty f(x)x^{s-1}\,dx.
\]

Through the half-density interface,

\[
\mathcal M f(s)
=\int_0^\infty (Jf)(x)x^{s-1/2}\frac{dx}{x}.
\]

Under complete additive dilation,

\[
\mathcal M(D_af)(s)=a^{1/2-s}\mathcal M f(s).
\]

This cocycle survives simultaneous transport because it belongs to the
relative source--readout pairing, not to a held-fixed coefficient frame.

Its modulus is

\[
|a^{1/2-s}|=a^{1/2-\Re s}.
\]

Therefore the relative Haar interface is unitary exactly when

\[
\Re s=\frac12.
\]

This derives the critical offset without reference to zeros.

## Logarithmic form

Put (x=e^u) and (g(u)=(Jf)(e^u)). Then (dx/x=du), and on the seam

\[
\mathcal M f\left(\frac12+it\right)
=\int_{\mathbb R}g(u)e^{itu}\,du.
\]

The critical-line Mellin readout is precisely the additive Fourier transform
of the half-density state in logarithmic coordinates. Fourier--Tate reflection
reverses (t) and exchanges the two valuation orientations in this common
unitary frame.

## Exact limitation

Unitary matrix coefficients can vanish. A nonzero (g\in L^1\cap L^2) may be
orthogonal to the character (e^{-itu}), giving

\[
\int_{\mathbb R}g(u)e^{itu}\,du=0
\]

while (g\ne0). More generally, off the seam the Mellin readout remains one
linear functional on the source state. Its kernel is not removed by the Haar
intertwiner.

Hence the relative interface proves:

- why the half-offset is (1/2);
- why the seam is the unitary locus;
- how additive Fourier and multiplicative Mellin descriptions normalize into
  one logarithmic carrier.

It does not prove that zeros must occur on that locus.

## Connection to the innovation tower

The reciprocal innovation energy from packet 226 uses the same cocycle at
every prime depth. Its coherent sign is therefore not an inserted norm effect;
it is the squared-modulus shadow of the relative Haar cocycle. Packet 227 still
applies: the definite energy does not turn a scalar cancellation into a null
state.

## Remaining constructor

The missing object must join the relative Haar pairing to a source-derived
boundary system whose determinant is the completed theta readout. It must make

\[
\mathcal M f(s)=0
\]

equivalent to an admissible two-endpoint state and derive the oriented
innovation energy as that system's Green current. Without this determinant or
boundary-state bridge, the half-density explains the seam but not RH.

## Scope

This packet derives the complete relative Haar transform and its dilation
cocycle. It proves that the critical line is the unitary interface between the
additive and multiplicative sectors. It also proves that this interface alone
has no zero-confinement force. It does not construct the boundary determinant
or prove RH.
