# Theta antipodal phase is a chart; the invariant zero is state-covector incidence

## Status

Typing correction to the two-route reduction. The statement that cancellation
occurs at relative phase (-1) assumes the scalar readout is the unweighted sum
in a fixed common frame. A source-derived coefficient system may define a
different dual covector.

The gauge-invariant zero condition is incidence of the resolved route line with
the kernel of the source-normalized readout covector. The evolution of that
pairing is controlled exactly by the mismatch between state transport and dual
readout transport.

## Resolved state and resolved readout

Let

\[
r(s)=
\begin{pmatrix}
r_+(s)\\
r_-(s)
\end{pmatrix}
\]

be the two-route state, and let

\[
c(s)=
\begin{pmatrix}
c_+(s)&c_-(s)
\end{pmatrix}
\]

be the source-normalized readout covector. The scalar section is

\[
\sigma(s)=c(s)r(s).
\]

Its zero condition is

\[
[r(s)]\in\mathbb P(\ker c(s)).
\]

This projective incidence statement is independent of the chosen route basis.

## Why the antipode is only a chart

If (c_+), (c_-), and (r_-) are nonzero, the zero equation becomes

\[
\frac{r_+}{r_-}=-\frac{c_-}{c_+}.
\]

The value (-1) appears only in a frame where

\[
c_+=c_-.
\]

Under a diagonal route-frame change

\[
r\longmapsto Dr,
\qquad
c\longmapsto cD^{-1},
\]

the state ratio and coefficient ratio change inversely while the incidence
equation remains fixed. Thus antipodal exclusion is not itself invariant unless
the source has independently selected the equal-coefficient frame.

Benincasa's Kummer endpoint calculation is an exact finite warning. The raw
occurrence packet has coefficients \((-1,+1)\) and vanishing unweighted sum,
while the source-normalized primitive readout is the nonzero period

\[
\int_{-1}^{1}\frac{d\xi}{\sqrt{1-\xi^2}}=\pi.
\]

Route incidence and period vanishing are therefore different typed claims.

## Dual transport theorem

Let the state satisfy

\[
\partial_s r=A(s)r+f(s),
\]

and let the readout covector satisfy

\[
\partial_s c=-cA(s)+g(s).
\]

Then direct differentiation gives

\[
\partial_s\sigma
=g(s)r(s)+c(s)f(s).
\]

The connection terms cancel exactly. Hence:

- if (f=g=0), the pairing is constant;
- state forcing (f) changes the pairing through (cf);
- dual-readout forcing (g) changes it through (gr);
- curvature or holonomy of the common transport does not by itself change the
  scalar pairing when state and covector are transported dually.

This is the invariant form of the earlier leakage identity. Scalar zeros can be
created only by the relative forcing or anomaly between the primal and dual
constructions, not by a common invertible normalization alone.

## Consequence for modular reciprocity

If modular self-reciprocity supplies only an invertible route transport (U),
with

\[
r\longmapsto Ur,
\qquad
c\longmapsto cU^{-1},
\]

then

\[
cr\longmapsto cU^{-1}Ur=cr.
\]

Such reciprocity preserves the scalar pairing; it does not orient it. Any
RH-bearing content must therefore occur in one of three more specific places:

1. a source-derived restriction on the admissible incidence pairs ((c,r));
2. a signed law for the mismatch current (gr+cf);
3. a completion theorem proving that no new primal-dual incidence appears at
   infinity.

## Correct hostile test

The quartic hostile family must be compared at the level of the pair

\[
(c_g(s),r_g(s)),
\]

not only at the level of a conjugate saddle packet. If the same proposed
readout law applies to the hostile family and its mismatch current still drives
the pairing through zero, the law has no theta-selective force.

Conversely, changing the covector after observing the zero is fitted and
invalid. Both (c) and (r) must be constructed from the source before their
pairing is evaluated.

## Finite falsifier

At a finite labelled cutoff, compute the primal transport (U), the proposed
dual transport (V), and the readout pairing. The transport is genuinely dual
only if

\[
VU=I.
\]

The finite defect

\[
\mathfrak D=VU-I
\]

is the first falsifier. When (mathfrak D=0), any claimed change in the scalar
pairing must be accounted for by explicit primal or dual forcing. When
(mathfrak D\neq0), the residual must be typed as a source anomaly rather than
silently absorbed into a normalization.

## Revised target

Construct the source-normalized dual readout for the two theta/Tate routes and
derive its transport alongside the state transport. Then isolate the exact
mismatch current

\[
\mathcal J_{\mathrm{mis}}=gr+cf.
\]

The next noncircular RH theorem must constrain this current or its integrated
incidence flow by a theta-specific source law. A fixed antipodal phase statement
is valid only after that dual coefficient layer has selected the corresponding
frame.
