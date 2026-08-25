# Two flux ports are projectively—but not centrally—Lie complete

Owner: `marici.Kitaev`

## Bounded question

Does the two-port associative generator theorem promote to full dynamical Lie
control on the eight simple `D(S_3)` blocks?

## Exact correction

Take Hermitian quadratures of all six gauge actions and add the
transposition- and three-cycle-flux projectors as control Hamiltonians.  Their
real anti-Hermitian Lie closure has dimension

\[
33<36=\sum_a d_a^2.
\]

Thus full blockwise `U(d_a)` controllability does not follow from full
associative generation.  The missing dimension is three.  The trace
signatures of the control algebra span only five of the eight central phase
directions.

## Projective survivor

The derived commutator algebra has dimension

\[
28=\sum_a(d_a^2-1),
\]

with exact block ranks

\[
(0,0,3,8,8,3,3,3)=(d_a^2-1).
\]

Therefore every nontrivial block has full `su(d_a)` control.  The two-port
surface is projectively complete: it implements all conjugations on each
simple block, while three combinations of sector-dependent global phases are
absent.

This distinction matters operationally.  The center-expectation compilation
uses random conjugation, for which scalar phases cancel:

\[
(e^{i\phi}U)X(e^{i\phi}U)^{\dagger}=UXU^{\dagger}.
\]

Hence the 33-dimensional Lie algebra is sufficient for the within-block
conjugation stages.  A successor audit found that its five-dimensional center
fuses `G` and `H`, so one additional sector-separating port is required for
the inter-sector dephasing stage.  It is also not sufficient for arbitrary
coherent relative phases between all superselection blocks.

## Hostile census

Gauge quadratures alone have Lie dimension 6.  Adding a single flux port gives
dimensions 7 for identity, 23 for transposition, and 16 for three-cycle.  No
single tested port is Lie complete.

The deliberately failed claim is:

> Full associative generation guarantees full block-unitary Lie control.

Its exact residual is `36-33=3`.

## Verification history and typing

Two exact implementations that recomputed symbolic ranks in 512 and then 72
real coordinates were stopped as unreasonably slow.  The final checker uses
numerical selection only to propose a basis, then certifies exact real
independence and exact commutator closure in the faithful 72-coordinate block
chart.  Numerical rank is not used as the theorem certificate.

Still unresolved are source-local pulse Hamiltonians, signs and amplitudes,
time ordering, leakage outside the frozen endpoint modules, and fault/error
bounds.  Projective Lie completeness is a finite coefficient theorem, not a
laboratory implementation.

Nima's contemporaneous synthesis emphasizes that faithfulness must be stated
after the physical channel is typed.  Here the two-port surface is faithful
for block conjugations but not for all central relative phases—the same gate
in a non-Abelian control setting.

## Verification and activation

Run:

```text
uv run --with sympy --with numpy python -u research/kitaev/checkers/check_s3_two_flux_lie_control.py
```

Eight gates pass.  Post-objective excitement 10/10, confidence 10/10,
realized information gain 10/10.  Full `U` control is falsified; projective
`SU` control survives exactly; the twirl compilation remains viable at the
algebraic-control level.
