# The theta precursor fixes the two Wronskian trace normalizations exactly

## Precursor decomposition

On the positive modular chamber,

\[
h(u)
=
e^{u/2}
\left(
\frac12+A(u)
\right),
\qquad
A(u)=\sum_{n\ge1}e^{-\pi n^2e^{2u}}.
\]

Write

\[
f(u)=\frac12+A(u),
\qquad
h(u)=e^{u/2}f(u).
\]

The reciprocal Wronskian traces are

\[
\mathcal B_-(h;u)
=
e^{-u/2}
\left(
h'(u)+\frac12h(u)
\right)
=
f'(u)+f(u),
\]

and

\[
\mathcal B_+(h;u)
=
e^{u/2}
\left(
h'(u)-\frac12h(u)
\right)
=
e^u f'(u).
\]

## Traces at infinity

The nonzero theta labels and all their derivatives decay super-exponentially as \(u\to+\infty\). Hence

\[
A(u)\to0,
\qquad
A'(u)\to0,
\]

and

\[
\mathcal B_-(h;\infty)=\frac12,
\qquad
\mathcal B_+(h;\infty)=0.
\]

Thus the surviving growing-wall coefficient is exactly \(1/2\) in the unrescaled theta precursor.

## Traces at the seam

Poisson reflection makes \(h\) even, so

\[
h'(0)=0.
\]

Also,

\[
h(0)
=
\frac12+\sum_{n\ge1}e^{-\pi n^2}
=
\frac12\vartheta(1),
\]

where

\[
\vartheta(1)
=
\sum_{n\in\mathbb Z}e^{-\pi n^2}.
\]

Therefore

\[
\mathcal B_-(h;0)
=
\frac12h(0)
=
\frac14\vartheta(1),
\]

and

\[
\mathcal B_+(h;0)
=
-\frac12h(0)
=
-\frac14\vartheta(1).
\]

The seam traces are equal in magnitude and opposite in orientation.

## Exact weighted source masses

Since

\[
\mathcal Ch=\Phi,
\]

the relative Green identities give

\[
\int_0^\infty
e^{-u/2}\Phi(u)\,du
=
\mathcal B_-(h;\infty)-\mathcal B_-(h;0)
=
\frac12-\frac14\vartheta(1),
\]

and

\[
\int_0^\infty
e^{u/2}\Phi(u)\,du
=
\mathcal B_+(h;\infty)-\mathcal B_+(h;0)
=
\frac14\vartheta(1).
\]

Their sum is

\[
\int_0^\infty
2\cosh(u/2)\Phi(u)\,du
=
\frac12.
\]

These are source-exact normalizations, requiring no fitted wall coefficient.

## Meaning of the factor two

If the coefficient wall basis is normalized to unit amplitude, while the theta precursor carries wall coefficient \(1/2\), the comparison map necessarily includes a factor two:

\[
2\,\mathcal B_-(h;\infty)=1.
\]

This factor is not the bilateral doubling of the completed history kernel. It is the normalization converting the precursor zero mode to a unit wall coordinate.

Conflating these two factors would square or duplicate the wall weight.

## Reciprocal completion balance

The two completed weighted masses partition the precursor wall:

\[
\left(
\frac12-\frac14\vartheta(1)
\right)
+
\frac14\vartheta(1)
=
\frac12.
\]

So the killed wall is distributed between reciprocal Wronskian variations, not represented as an identity in either completed sheet separately.

This suggests that the relative auxiliary block should use a two-port wall metric whose total coefficient is \(1/2\), with unit normalization imposed only after the source comparison.

## Hostiles

1. Set both sheet wall traces equal to one. The relative mass is overcounted by a factor four at Gram level.
2. Treat the factor two converting \(1/2\) to a unit wall as bilateral history doubling.
3. Retain only the decaying-sheet mass \(\vartheta(1)/4\), losing the complementary wall fraction.
4. Square the two trace amplitudes independently and expect their sum to equal the square of the total wall amplitude; the mixed term is then missing.

## Next finite block

Freeze the two-dimensional trace vector

\[
b(h)
=
\begin{pmatrix}
\mathcal B_-(h;\partial)\\
\mathcal B_+(h;\partial)
\end{pmatrix}
\]

with the above seam and infinity values. Derive its polarized boundary Gram before any unit-wall rescaling. Then determine whether eliminating one reciprocal trace produces the effective unit identity required by the causal-history block.

This is now a finite \(2\times2\) relative-wall calculation with source-fixed entries.
