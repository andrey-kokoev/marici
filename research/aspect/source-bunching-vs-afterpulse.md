# Source bunching versus detector afterpulsing

## Question

Can lag correlations alone distinguish genuine source memory from detector
afterpulsing?

## Exact observational alias

In the frozen two-epoch model, either the source copies its preceding binary
record with probability `1/2`, or an otherwise iid source is observed by a
detector that copies its preceding output with probability `1/2`.

With one fixed detector, the complete observed pair laws are identical. Both
have covariance `3/8`. No statistic of that fixed-detector pair record can
identify where the memory resides.

## Separating interventions

An active detector reset before the second epoch removes detector-local memory
but leaves source memory unchanged. Likewise, routing the second epoch to a
fresh independently calibrated detector removes detector-local afterpulsing
while source bunching follows the optical stream.

In the checker, both interventions give covariance `0` for detector memory and
`3/8` for source memory.

The word independently is essential. If both detectors share an electronic
echo or disturbance path, the memory follows the routing and remains exactly
aliased with source bunching. Separate detector registers and high agreement
do not establish physical diversity.

## Experimental contract

Use time tags under three conditions: fixed detector, active reset, and
rerouting to a detector whose disturbance response has been independently
excited. Record detector identity, reset status, and electronics lineage with
every event.

Persistence under both reset and genuinely independent rerouting supports a
source-memory interpretation only relative to the tested detector-memory
models. Mixed source and detector memory, imperfect reset, loss mismatch, and
common electronics require a larger joint reachable set.

## Verification

Run:

```text
python research/aspect/checkers/check_source_bunching_vs_afterpulse.py
```

The dependency-free exact checker verifies the fixed-detector alias, both
separating interventions, and the shared-electronics obstruction.
