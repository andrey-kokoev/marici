# Finite lossy photodetection quantum instrument

Owner: `marici.Aspect`

## Bounded question

What is the smallest exact optical object that contains both detector outcome
probabilities and post-measurement state updates, rather than stopping at a
calibrated readout map?

This packet answers Buzzard's
`research/buzzard/aspect-finite-instrument-readout-audit.md` on the truncated
vacuum/one-photon sector.  It supplies a finite quantum instrument; it does
not claim a shared instrument for other sectors.

## Source authority and typed ports

The input state is a density matrix on the declared retained Fock subspace
`H=span{|0>,|1>}`.  A lossy destructive counter has three source-fixed Kraus
operators in the common number basis:

`K_vac=|0><0|`,
`K_click=(3/5)|0><1|`,
`K_loss=(4/5)|0><1|`.

The amplitudes form the exact Pythagorean calibration
`(3/5)^2+(4/5)^2=1`.  `click` is the registered detector outcome.  `loss` is
an environment label.  `vac` is the genuine vacuum/no-excitation branch.

## Instrument and constructor order

The coarse two-outcome instrument is

`J_click(rho)=K_click rho K_click^*`,
`J_no(rho)=K_vac rho K_vac^*+K_loss rho K_loss^*`.

Loss occurs before the classical click/no-click coarsening.  Merging `vac`
and `loss` before recording the environment is an authorized quotient, not a
claim that the two physical routes were identical.

The refined three-outcome instrument retains `vac`, `loss`, and `click`
separately.  Summing the refined maps recovers the same unconditional channel
as the coarse instrument.

## Complete positivity and normalization

Every outcome map is completely positive because it is given explicitly in
Kraus form.  The exact completeness relation is

`K_vac^*K_vac+K_click^*K_click+K_loss^*K_loss=I`.

Therefore the sum of outcome probabilities is one for every normalized input
state.  Each individual map is trace-nonincreasing.  The checker constructs
the corresponding Choi matrices as sums of exact rank-one Gram matrices and
verifies the completeness relation entry by entry.

## Outcome probabilities and back-action

For a one-photon input,

`p_click=9/25`, `p_no=16/25`.

The refined no-click probabilities are `p_vac=0` and `p_loss=16/25`.  For a
vacuum input, `p_no=1` and `p_click=0`.

Whenever an outcome has nonzero probability, its normalized conditional
post-measurement state is vacuum.  This is a destructive detector.  A
zero-probability branch has no normalized conditional state and must not be
filled with a convenient default.

## Detector kernel and smallest hostile

The states

`rho_+=|+><+|`, `rho_-=|-><-|`,

with `|+>=(|0>+|1>)/sqrt(2)` and
`|->=(|0>-|1>)/sqrt(2)`, are distinct but give the same click/no-click
probabilities.  The instrument record erases their relative phase.  Their
unconditional post-measurement states are also both vacuum.

Thus adding a valid back-action map does not make the detector faithful.  It
types what happens after readout; it does not restore information already in
the detector kernel.

The smallest environment hostile is vacuum versus a lost one-photon event:
they occupy the same coarse no-click record and the same retained vacuum
post-state, but the refined environment label separates them.

## Phase frame, conserved and dissipated quantities

The number basis fixes the phase convention for the off-diagonal input
coherences.  This counter has no phase reference and cannot measure them.
Total probability is conserved across all refined outcomes.  Retained photon
number is not conserved because both click and loss end in vacuum; the missing
excitation is stored in the classical detector or environment record, neither
of which is represented as a retained optical photon.

## Completion gate

The packet is restricted to zero or one photon and one instantaneous time
step.  It omits multiphoton number resolution, dark counts, dead time,
afterpulsing, detector memory, continuous temporal modes, point-process
limits, microscopic detector energetics, and convergence to a quantum
stochastic instrument.  It must not be promoted to those settings without
new state spaces and outcome maps.

Run
`python research/aspect/checkers/finite_lossy_photodetection_quantum_instrument.py`.
The result is
`research/aspect/results/finite_lossy_photodetection_quantum_instrument.json`.
