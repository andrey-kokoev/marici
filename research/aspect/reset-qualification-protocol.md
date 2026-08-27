# Qualification protocol for the common optical reset

The candidate reset is tested as an operation, not inferred from quiet detector output.

For each of the four crossed treatments, prepare it as an adversarial predecessor. Apply the candidate reset. Then apply each of the four treatments as target and retain the full output. This produces all sixteen predecessor-target cells.

The reset qualifies only if, for every fixed target, the complete target response is invariant under predecessor choice within absolute tolerance `1/20`. The reset monitor must independently satisfy the same predecessor-invariance bound. Failed reset monitors remain ordinary recorded outcomes.

A no-reset negative control repeats the same sixteen cells without the reset and must exhibit predecessor spread of at least `1/10`. This proves that the qualification arrangement can see the memory it claims the reset removes. A quiet reset monitor by itself is insufficient: the executable hostile keeps the monitor exactly zero while leaving `1/5` of predecessor dependence in the target response, and the protocol rejects it.

Qualification and science epochs are disjoint. The reset construction and thresholds are frozen before the associator labels are opened. Passing this protocol licenses insertion of the same reset between every science trial's predecessor and target; it does not license fitted subtraction from science data.

The finite qualification therefore has the required form:

`adversarial predecessor → reset → target → full readout`

Contract: `contracts/reset-qualification.v1.json`.

Executable checker: `checkers/check_reset_qualification.py`.
