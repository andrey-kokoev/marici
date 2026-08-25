# Schur contractivity does not exclude zeros; the denominator must be Hermite--Biehler

## 1. Contractive functions may vanish

A scalar Schur function can have zeros anywhere in its analytic domain. In
the upper half-plane, for any \(a\) with \(\operatorname{Im}a>0\), the
Blaschke factor

\[
  b_a(z)=\frac{z-a}{z-\bar a}
\]

is analytic and contractive in the upper half-plane, has unit-modulus
boundary values, and vanishes at \(z=a\).

Therefore:

\[
\boxed{
\text{half-plane contractivity}
\not\Longrightarrow
\text{zero-free transfer section}.}
\]

The proposed operator-valued \(J\)-Schur continuation is a meaningful
positivity target, but it cannot carry RH if \(X\) itself is merely one of
its contractive entries.

## 2. Correct de Branges placement

Let \(E\) be entire and define

\[
  E^\#(z)=\overline{E(\bar z)}.
\]

The Hermite--Biehler condition is

\[
  |E^\#(z)|<|E(z)|
  \qquad(\operatorname{Im}z>0).
\]

Then

\[
  \Theta(z)=\frac{E^\#(z)}{E(z)}
\]

is Schur in the upper half-plane. The contractive function is the *ratio* of
the reflected and unreflected sectors, while \(E\) is its zero-free
denominator there.

Write

\[
  E=A-iB,
\]

with \(A\) and \(B\) real entire. Then

\[
  A=\frac{E+E^\#}{2}.
\]

If \(A(z)=0\) in the upper half-plane, then \(E^\#(z)=-E(z)\), contradicting
the strict Hermite--Biehler inequality. Reflection gives the same exclusion
in the lower half-plane. Hence every zero of \(A\) is real.

## 3. RH-bearing assignment

The completed theta scalar must occupy the symmetric slot:

\[
  A(z)=X(z),
\]

not the Schur slot. The missing source datum is its oriented companion
\(B(z)\), producing

\[
  E(z)=X(z)-iB(z).
\]

RH would follow from a source-derived proof that \(E\) is
Hermite--Biehler, together with the required reality, growth, and
normalization statements.

This placement matches the two-sector interpretation:

\[
\boxed{
\begin{aligned}
E&=\text{one oriented localization},\\
E^\#&=\text{the reciprocal localization},\\
X&=\tfrac12(E+E^\#)=\text{symmetric scalar shadow},\\
E^\#/E&=\text{contractive transition function}.
\end{aligned}}
\]

## 4. The missing companion cannot be arbitrary

Given \(X\), one can manufacture many functions \(B\). Choosing one after
inspecting the zeros or requiring the Hermite--Biehler inequality by
definition is circular.

The companion must arise before scalar compression from an oriented source
operation. Current candidates are:

1. the mixed right--left Green flux;
2. the moving-seam Hilbert transform selected by a Hardy polarization;
3. the conjugate boundary observable of the adelic Weyl crossing; or
4. a source-derived Clark/de Branges boundary current.

These candidates must agree by theorem if they represent the same physical
orientation.

## 5. Connection to the unitary defect theorem

On the real axis, \(X(x)=0\) is already the kernel event of the complete
excited compression. A valid companion \(B\) must orient that defect:

\[
  X(x)=0
  \quad\Longrightarrow\quad
  B(x)\ne0
\]

for a simple crossing, with the sign of \(B\) determining the direction in
which the principal angle passes through \(\pi/2\).

Thus \(B\) is not extra scalar decoration. It is the signed velocity or flux
of the coupled-sector defect that \(X\) detects without orientation.

## 6. Sharp next theorem

Construct \(B\) directly from the labelled mixed seam crossing and prove the
de Branges kernel identity

\[
  \frac{
  E(z)\overline{E(w)}
  -
  E^\#(z)\overline{E^\#(w)}
  }{-i(z-\bar w)}
  =
  \langle\Gamma_z,\Gamma_w\rangle_{\mathcal K}
\]

for source-derived boundary features \(\Gamma_z\). Positivity of the right
side yields the Hermite--Biehler inequality.

The hostile test is whether a Fourier-stable positive source with off-line
zeros admits the same labelled Gram factorization. It must fail before its
zeros are used.

## 7. Scope

The Blaschke falsifier, Hermite--Biehler implication, and correct placement of
\(X\) as the symmetric part are exact. No source-derived companion \(B\),
positive de Branges Gram identity, or RH theorem is constructed.
