# The ordered inverse-derivative port exactly resolves the connection curvature

## Two source operators

On the rapid ray core, let

\[
D=\partial_x,
\qquad
A=x\partial_x.
\]

The window-to-theta connection curvature is

\[
\Omega=-2(A+1)D.
\]

Independently, the ordered reciprocal port is the odd
degree-minus-one inverse derivative \(S_{\mathrm{ord}}\), characterized by

\[
DS_{\mathrm{ord}}
=
S_{\mathrm{ord}}D
=
-2I.
\]

Its dilation degree is \(-1\).

## Dilation commutator

For the unitary dilation

\[
(U_af)(x)=a^{1/2}f(ax),
\]

the ordered port satisfies

\[
U_a^{-1}S_{\mathrm{ord}}U_a
=
a^{-1}S_{\mathrm{ord}}.
\]

Differentiating at \(a=1\), with generator \(A+\frac12\), gives

\[
[S_{\mathrm{ord}},A]
=
-S_{\mathrm{ord}}.
\]

Equivalently,

\[
S_{\mathrm{ord}}(A+1)
=
A S_{\mathrm{ord}}.
\]

This is the exact commutation needed to compose the ordered port with the
curvature.

## Left and right resolution identities

Using the two-sided inverse-derivative law,

\[
S_{\mathrm{ord}}\Omega
=
-2S_{\mathrm{ord}}(A+1)D
=
-2A S_{\mathrm{ord}}D
=
4A.
\]

On the other side,

\[
\Omega S_{\mathrm{ord}}
=
-2(A+1)DS_{\mathrm{ord}}
=
4(A+1).
\]

Hence

\[
S_{\mathrm{ord}}\Omega=4A,
\qquad
\Omega S_{\mathrm{ord}}=4(A+1).
\]

The one-unit discrepancy is the expected degree shift between the two
orientations.

## Gaussian seed

For the even Gaussian \(f_0=e^{-\pi x^2}\),

\[
\Omega f_0
=
8\pi f_1-8\pi^2f_3.
\]

The ordered port sends this entire reciprocal-odd curvature seed to

\[
S_{\mathrm{ord}}\Omega f_0
=
4Af_0
=
-8\pi f_2.
\]

Thus the inverse derivative collapses the first odd curvature packet to a
single even dilation grade with source-fixed coefficient and sign.

This is not a fitted projection. It follows from the complete operator
signature of the ordered port.

## Consequence for the infinite cyclic tail

The odd curvature carrier is infinite under the completion polynomial
\(P=A(A+1)\). The ordered port does not simply commute with \(P\); its
degree shift must be retained. From

\[
S_{\mathrm{ord}}A=(A-1)S_{\mathrm{ord}},
\]

one obtains, on the common core,

\[
S_{\mathrm{ord}}P
=
(A-1)A S_{\mathrm{ord}}.
\]

Therefore ordered resolution transports the odd \(P\)-cyclic module into an
even cyclic module for the shifted polynomial \((A-1)A\), not back into the
same unshifted theta block.

The shifted target is the exact algebraic reason a scalar same-grade
identification fails.

## What this closes

The source already contains an exact operator bridge between:

- the parity-changing connection curvature;
- the reciprocal-odd ordered port;
- the even dilation generator.

The curvature auxiliary carrier is therefore not unrelated to the existing
ordered seam data.

## What remains open

The ordered port \(S_{\mathrm{ord}}\) is not automatically the bounded
causal history \(H_+\) appearing in the shifted-history square. The next
constructor must compare:

\[
S_{\mathrm{ord}}
\quad\text{with}\quad
H_+
\]

on the curvature-generated joint graph carrier.

Possible source-authorized outcomes are:

1. \(H_+\) factors through a regularized ordered port;
2. \(S_{\mathrm{ord}}\) is a boundary value of the causal resolvent;
3. the two occupy distinct ports connected only after Hardy projection;
4. no such comparison exists, requiring a larger auxiliary block.

## Hostile

Use only \(DS_{\mathrm{ord}}=-2I\) and ignore the right inverse,
reciprocal character, or dilation degree. A constant-mode ambiguity can then
alter the curvature return while preserving one scalar derivative identity.

## Frontier

The next square is now explicit:

\[
\text{odd curvature}
\xrightarrow{\;S_{\mathrm{ord}}\;}
4A
\xrightarrow{\;\text{Hardy/causal comparison}\;}
\text{shifted-history auxiliary block}.
\]

The unresolved arrow is no longer from curvature to an unspecified phase. It
is the Hardy/causal realization of a fixed ordered inverse-derivative
resolution.
