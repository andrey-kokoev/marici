# Imperfect environment access: deterministic loss and heralded recovery

## Any missing fraction forbids deterministic exact recovery

After complete transfer out of the system, let the environment record pass
through a collection channel of efficiency `eta`. This is itself an amplitude
damping channel. For the orthogonal inputs `|0>` and `|1>`, their accessible
output trace distance is only `eta`.

A deterministic physical recovery channel cannot increase trace distance.
Therefore no deterministic decoder can restore both orthogonal inputs unless
`eta=1`. This remains true even though the channel is linearly invertible for
every positive `eta`.

The smallest Bloch reconstruction margin is `eta`, so the formal inverse gain
is `1/eta`. Partial collection changes catastrophic collapse into an
ill-conditioned inference problem, but it does not produce a deterministic
physical inverse.

## A heralded reverse arrow survives

If the loss event is monitored, the no-loss branch has filter
`diag(1,sqrt(eta))`. A second physical filter `diag(sqrt(eta),1)` composes with
it to `sqrt(eta)` times the identity. Conditional on success, every unknown
input state is recovered exactly. The total success probability is `eta`,
independent of the input.

This gives a useful three-way distinction:

- full coherent access: exact deterministic recovery;
- partial monitored access: exact heralded recovery with success `eta`;
- partial unmonitored access: no exact physical recovery, only inference.

Rank alone fails to distinguish these regimes. Port typing must include whether
discard events are coherently retained, classically heralded, or inaccessible.

## Optical instrument

Implement collection loss with a calibrated beamsplitter. Detect the rejected
port to herald no loss, then apply the compensating polarization-dependent
filter and tomographically verify the conditional output. Report unconditional
throughput alongside conditional fidelity: high postselected fidelity without
the success probability would conceal the operational margin.

## Claim boundary

The argument treats ideal single-qubit loss with perfect heralding and filtering.
Dark counts, mode mismatch, multiphoton components, and detector dead time
remain open.

## Verification

```text
python research/aspect/checkers/check_imperfect_environment_access.py
```
