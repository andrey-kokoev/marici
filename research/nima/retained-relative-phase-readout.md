# Relative path phase needs common endpoint comparisons

Fresh input: `retained-active-passive-action.md`. Work remains conditional on
the declared real defining module and its Clifford transport. This constructs
a mathematical comparator, not a native measuring apparatus.

## Compare transports with the correct types

Let U1,U2 be invertible real-linear transports between the SAME calibrated
initial and final fibers. A common base position alone is insufficient: the
full endpoint/fiber identifications must be retained. Define

\[
R_{12}=U_1^{-1}U_2.
\]

This is an endomorphism of the initial fiber. Under common initial and final
frame changes a,b, each transport becomes b*Ui*a^(-1), and

\[
R_{12}'=aR_{12}a^{-1}.
\]

Consequently the central comparisons +1 and -1 are unchanged. Three paths sew
as R12*R23=R13. This uses actual transport composition, including the odd
real-linear maps; it does not incorrectly treat an anti-linear map as a
complex-linear phase multiplication.

The two lifts giving the same FULL adjoint action can differ by -1. Merely
sharing one base point does not in general force the relative transport to be
central, since stabilizers can be larger.

## Independent arm frames require retained sewing maps

Suppose the two arms instead use frames a1,a2 at their starts and b1,b2 at
their ends. Then the correctly typed comparison, expressed in the first
initial frame, is

\[
(U_1')^{-1}(b_1b_2^{-1})U_2'(a_2a_1^{-1})
=a_1R_{12}a_1^{-1}.
\]

Both endpoint comparison maps matter. For example, start with U1=1,U2=-1.
Changing only the second final frame by -1 makes both displayed transport
matrices equal to 1. The missing final comparison is itself -1; reinserting
it recovers the original sign. This is exactly why the moving frame from the
preceding leaf cannot erase its endpoint transition.

## Scalar readings are explicitly lossy

The normalized real trace tau=tr(R)/2 is conjugacy invariant and distinguishes
+1 from -1. It does NOT distinguish J from -J: both have trace zero.

An oriented comparator can retain the declared complex-structure witness J
as well. For an even relative transport write

\[
\tau=\tfrac12\operatorname{tr}(R),\qquad
\sigma=-\tfrac12\operatorname{tr}(JR),\qquad
R=\tau\,1+\sigma J.
\]

Both scalars are frame invariant provided J is transported to a*J*a^(-1)
alongside R. In particular they distinguish the two quarter phases. Keeping
a numeric J fixed while making an odd frame change would instead silently
reverse the orientation calibration. For odd relative transports this
two-scalar phase reading is not complete; retain the full typed map.

The existing endpoint phase-chart factors involving F/kappa are common frame
changes when both endpoint packets agree. They cancel in the relative map
up to the initial conjugation above. This cancellation is not justified after
forgetting momentum or a chart's Legendre boundary data at a caustic.

## What would make the sign operational?

A single-arm norm, or the real rank-one reading w*w^T, cannot distinguish w
from -w. In contrast, two prepared arms with a shared phase calibration and
a declared linear recombination/norm readout would satisfy

\[
\|w_1+w_2\|^2
=\|w_1\|^2+\|w_2\|^2+2\langle w_1,w_2\rangle.
\]

For the same unit input and transports 1 and +/-1, this mathematical reading
is respectively 4 or 0, although both separate arm norms are 1. These numbers
are not probabilities. They require an actual joint preparation, a common
endpoint calibration, an admitted recombination map and a specified output
readout. None has been derived as a physical apparatus or Born rule here.
The identity also describes ordinary classical linear-vector interference.

For orthogonal frame changes the fixed module metric suffices. Under a general
invertible final frame b it must become b^(-T)*G*b^(-1). Holding the old numeric
metric fixed then describes a different readout, not a gauge-invariant test.

## Verification and next gate

The exact checker covers 4096 common-frame comparisons, 4096 independent-frame
sewings for the central return, 512 three-path compositions, transported
orientation, single-arm sign loss and a nonorthogonal-metric hostile.

```text
python research/nima/checkers/check_relative_phase_readout.py
```

Receipt: `results/relative-phase-readout.json`.

The next local question is calibration identifiability: determine whether the
retained rotor comparisons identify an external time rate or the action-phase
scale kappa. In particular common-endpoint rotor phase comparisons cancel
the F/kappa chart terms. Test what data would actually break that degeneracy,
rather than claiming a physical clock or Planck constant. The independent
source product/readout owner gate remains open.
