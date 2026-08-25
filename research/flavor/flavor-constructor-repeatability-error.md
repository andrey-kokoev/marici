# Repeatability needs an apparatus trajectory (WP76, move 5/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

A constructor design supplies joint maps
`C_eta:(x,a_eta)->(T_eta x,a'_{eta,x})`, bounding both substrate error and
apparatus degradation uniformly over admitted inputs. Reuse requires a reset
or catalytic law. With only triangle control, `N` uses bound both errors by
`N` times their one-use values. An algebraic channel without apparatus,
timing, reset, and resource supply has untyped error—not zero error.

Finite-time RG is exact substrate evolution but has no proper image. Invariant
measurement has a typed readout interface but does not prepare. Pinching lacks
bath/coupling/timing/reset; randomized expectations also lack randomness and a
branch compiler; stationarity lacks success, rejection, and reset dynamics; a
reference experiment must account for reference degradation.

A claim is falsified if it reports channel error without constructor
degradation, proves only one use, hides a consumed reference, or tunes its
bound to the fitted input.

Verification:
`python research/flavor/checkers/wp76_constructor_repeatability_error.py`.
