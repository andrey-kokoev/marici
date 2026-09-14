# Unblocking analysis for fractional monodromy and physical readout

## Question

Can either residual blocker in the completed Aspect realization be removed using objects already present in the source envelope?

## Fractional-monodromy blocker

The audited conductor Kummer local systems have branch support at

\[
\Delta_i=0.
\]

The linked relative contour instead surrounds the conductor total-energy divisor

\[
E=0.
\]

On its generic locus,

\[
\Delta_i|_{E=0}=4x^2y^2\ne0.
\]

Therefore each conductor Kummer cover is locally unramified and its sign local system is locally constant near the linked \(E\)-normal circle. It cannot supply the missing quarter twist on that circle.

The intersection of total energy with Kummer branch support obeys

\[
E=0,
\qquad
\Delta_i=0
\quad\Longrightarrow\quad
xy=0.
\]

But the relative normal construction requires \(Y_0=2xy\ne0\) so that the complementary factors remain nonzero. Moving the contour to the Kummer branch locus therefore destroys the current three-divisor model rather than completing it.

Hence the first blocker cannot be removed from existing conductor square roots. It requires a new fractional local system supported along \(E=0\), or a different geometric comparison whose contour surrounds \(\Delta_i=0\) directly.

## Physical-record blocker

The same-parity lattice is the exact image of the algebraic matrix

\[
R:\mathbb Z^2\longrightarrow\mathbb Z^2.
\]

Aspect's physical detector semantics use raw nonnegative count records and calibrated probability distributions. Existing records such as \((1,0)\) and \((0,1)\) are not same-parity. Nothing in those packets makes the algebraic output coordinates literal count channels.

This blocker can be removed only by withdrawing that identification. Retype the layers as

\[
\text{integral route lattice}
\longrightarrow
L_{\rm rec}
\longrightarrow
\mathbb R^2_{\rm estimator},
\]

for the algebraic and calibrated estimator stages, while the physical record map has type

\[
\text{trial data}
\longrightarrow
\mathbb R^2_{\rm estimator}.
\]

The same-parity condition then constrains exact algebraic coefficients, not individual detector records. A physical experiment need only establish that calibrated estimators reproduce the real extension of \(R\) within declared uncertainty. It need not produce same-parity raw counts.

This retyping removes an unnecessary physical-lattice demand, but it does not fabricate the missing calibration data.

## Disposition

- Fractional monodromy: not unblockable from current sources; the existing Kummer covers are unramified along the linked total-energy contour.
- Physical readout: the same-parity-record blocker can be dissolved by correcting the type. What remains is an ordinary empirical calibration requirement for a real-valued estimator map.
