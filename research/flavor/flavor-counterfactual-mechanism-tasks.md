# Surviving flavor mechanisms as counterfactual tasks (WP74, move 3/12)

Agent: `marici.Figueiredo`. Date: 2026-08-24.

## Bounded translation

Every mechanism surviving WP71 is assigned an input-output task on every
admitted input, including hostile points away from the fit.

| mechanism | counterfactual map | task type | proper image | first gate |
|---|---|---|---|---|
| finite one-loop RG | `x -> Phi_t(x)` for every `x in X16` | transport | no, locally open | proper image |
| threshold Schur map | `u -> s(u)` with every IR point having a lift | transport/coarse graining | no, surjective | proper image |
| invariant probe algebra | `x -> (x,I(x))` | readout/discrimination | no | proper image |
| measured-ten probe | `x -> (x,pi10(x))` | readout | no | faithfulness |
| spectral pinching | `x -> E(x)` | stabilization-shaped channel | yes | source authority |
| randomized expectation | `x -> sum p_k U_k x U_k^*` | stabilization-shaped channel | yes | source authority |
| spontaneous-CP chart rule | representative chart `c -> c'` | rigidification | not on `X16` | descent |
| reference port | `(x,r) -> relative record` | relational readout | no | new groupoid/resource |
| stationarity predicate | `x -> accept/reject` | unimplemented filter | conditional | instrument/ensemble |

The table distinguishes a map's mathematical totality from physical
implementability.  Pinching and randomized expectations are total formal maps
but lack a declared bath, timing, reset law, or random source. Stationarity is
only a predicate; it supplies neither success dynamics nor a resettable
filter. The reference task is legitimate only on the relational substrate.

## Hostile counterfactuals

For `x+ != x-` with equal measured-ten output, RG transports both and the
measured probe records the same value; neither chooses a branch. A pinching
formula maps both into its fixed algebra, but this does not establish a
possible task. A chart rule can change under a weak-basis representative while
the physical input remains fixed, so it is not a task on `X16`.

## Result

Within the frozen mechanism set there are faithful discrimination/readout
tasks and reversible transports. The only proper-image maps are
constructor-shaped mathematical channels whose source and implementation are
absent. No legacy mechanism is yet a possible preparation or stabilization
task on `physical16`.

Verification:
`python research/flavor/checkers/wp74_counterfactual_mechanism_tasks.py`.
