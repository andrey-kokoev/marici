# The Gaussian derivative-comb current reduces to one seam port

## Bounded question

After value sampling loses the oscillator annihilator, does the smallest
faithful derivative-comb lift produce a new distributed current, or does it
reduce to the existing theta amplitude and its boundary?

## Scaled Gaussian comb

For (u\ge0), define

\[
f_u(x)=e^{u/2}e^{-\pi e^{2u}x^2}
\]

and the nonzero-label amplitude

\[
A(u)=\sum_{n\ne0}f_u(n).
\]

The transported annihilator satisfies

\[
a_uf_u=0,
\qquad
a_u=\partial_x+2\pi e^{2u}x.
\]

For translations (T_n), the source commutator is

\[
[a_u,T_n]=2\pi e^{2u}nT_n.
\]

Value sampling alone does not carry (partial_x). The smallest faithful lift
therefore retains both (f_u(n)) and (partial_xf_u(n)).

## Odd current cancels

On the Gaussian vacuum,

\[
\partial_xf_u(n)=-2\pi e^{2u}n f_u(n).
\]

The derivative port is thus determined by the marked label and value port.
Because (f_u(n)=f_u(-n)),

\[
\sum_{n\ne0}n f_u(n)=0.
\]

The first commutator current vanishes by source parity after the two labels are
retained and paired. It is not a new scalar output.

## Even current is the dilation derivative

Direct differentiation gives

\[
\partial_u f_u(n)
=
\left(\frac12-2\pi e^{2u}n^2\right)f_u(n).
\]

Hence the even number current

\[
E(u)=2\pi e^{2u}\sum_{n\ne0}n^2f_u(n)
\]

satisfies the exact identity

\[
E(u)=\frac12A(u)-A'(u).
\]

Thus the positive (n^2)-weighted current is not an independent bulk field.
It is a first-order differential image of the ordinary comb amplitude.

## Half-Mellin transform

Let

\[
H(z)=\int_0^\infty A(u)e^{izu}\,du.
\]

The Gaussian tail decays at infinity. Integration by parts yields

\[
\int_0^\infty E(u)e^{izu}\,du
=
\left(\frac12+iz\right)H(z)+A(0).
\]

Every distributed contribution therefore factors through the existing
half-line amplitude (H). The derivative-comb lift contributes exactly one
additional datum: the seam evaluation (A(0)).

Higher even number currents behave similarly. They are polynomials in
(partial_u) applied to (A), so their half-Mellin transforms are polynomial
multiples of (H) plus a finite jet of seam evaluations. No finite oscillator
ladder produces an independent bulk orientation law.

## Result

The smallest legitimate boundary lift has the following exact structure:

1. the odd derivative-comb current cancels under (n\leftrightarrow-n);
2. the even number current is positive on the real source chart;
3. its bulk is the dilation derivative of the existing amplitude;
4. after half-Mellin transform, its only new output is (A(0));
5. the full-source Fourier commutator remains exact up to its phase.

Therefore the proposed oscillator--Poisson mismatch is not a distributed
anomaly. It localizes completely at the half-line seam.

## Remaining gate

The reciprocal sheet has its own half-line amplitude and seam orientation.
The next calculation must sew the two formulas before scalar aggregation and
determine whether their (A(0)) ports cancel, double, or enter an antisymmetric
route channel. If they cancel or merely reconstruct the scalar functional
equation, the entire finite oscillator-ladder route closes. If they leave a
source-fixed transverse seam current, that current is the first object in this
lane with possible zero-confinement force.
