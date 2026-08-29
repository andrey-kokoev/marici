# Actuator-metric authority gate: WP997

## Question

Can the formal two-coordinate control regions of WP992-WP996 be promoted to
physical robustness statements using an already declared source operation?

## Admitted objects

The quotient-level control coordinate is (c=(Q,R)^T).  A physical command
packet would require a command space (U), a source-derived actuator map

\[
A:U\longrightarrow \mathbb R^2,
\qquad c=Aa,
\]

and a positive command-cost Gram matrix (G_U).  For a requested reachable
displacement, the induced minimum quadratic cost is

\[
d_A(c)^2=\min_{Aa=c}a^T G_Ua.
\]

When (A) has row rank two this equals

\[
c^T(A G_U^{-1}A^T)^{-1}c.
\]

This is the exact linear control-distance lift of WP996.  A coordinate square
or Euclidean norm chosen directly on ((Q,R)) is not a substitute for this
source data.

## Exact hostile pair

WP277 already provides the relevant hostile actuator type: one command affects
only the first state coordinate.  In the present notation take

\[
A_1=\begin{pmatrix}1\\0\end{pmatrix}.
\]

Then the left blind covector ((0,1)) annihilates (A_1).  The two requested
controls (c_0=(0,0)) and (c_1=(0,1)) are distinct in the formal control
plane but every admitted command has identical second coordinate.  Therefore
(c_1) is unreachable and has infinite authorized control distance.  No
choice of feedback law or readout rank repairs this actuator kernel.

By contrast (A_2=I_2) with (G_U=I_2) has rank two and induces the Euclidean
metric.  This is an exact mathematical completion witness, not a flavor-source
construction.

## Cross-sector transfer audit

- Kitaev's control-distance packet supplies the correct factorization and
  requires the controls, amplitudes, inverses, and costs to be source-authorized.
- Nima's metric critique proves that naked margins change under coordinate
  rescaling and become physical only with an authorized source metric.
- WP228 supplies no lift: its source-authorized cost is flat, while its strict
  quadratic cost is externally imposed.
- WP700 supplies a conditional support interval, not a two-channel actuator or
  detector-calibrated command cost.
- WP277 proves that observed-state rank does not imply actuator rank and leaves
  the second source actuator undeclared.

Thus the existing research contains the theorem schema but not the flavor
constructor (A) or its cost (G_U).

## Classification

The formal adaptive operation remains a mathematical control section.  It is
neither a source-derived selector nor a physical instrument.  Conditional on
a future rank-two source actuator it can select any of the three WP992 regions;
conditional on a source cost it can also carry an authorized robustness
distance.  Neither condition is presently met.

## Smallest exact falsifier

One source command with actuator column (A_1=(1,0)^T) is sufficient.  The
nonzero covector ((0,1)) lies in the left kernel, so the requested (R)
displacement cannot be executed.  This falsifies any inference from formal
two-coordinate feedback to physical two-coordinate control.

## Claim boundary

WP997 proves a typing obstruction and the necessary linear metric pullback. It
does not prove that flavor has only one actuator, that all nonlinear or ordered
routes fail, or that a rank-two flavor actuator is impossible.  It makes no
claim about laboratory energy, time, noise, reset, or degradation without a
declared source implementation.

## Falsifiers and reopening condition

The negative disposition is falsified by a source packet that names a common
flavor substrate, derives two independent command couplings, proves full weak-
basis descent, calibrates (A) and (G_U) in one frame with uncertainties,
and supplies a physical instrument.  A merely invertible coordinate change,
formal pole coordinate, or fitted norm does not qualify.

## Disposition

Close the WP996 square as algebraic only.  Reopen physical robustness only
after the actuator-metric pair ((A,G_U)) is source-derived and the calibrated
rank-two lower bound survives uncertainty.

