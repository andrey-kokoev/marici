# Afterpulse memory and confidence contracts

## Question

Can detector afterpulsing leave measured correlations unchanged while
invalidating the independent-trial confidence contract?

## Frozen memory model

Each binary record either copies the preceding detector record with
probability `a` or refreshes from the physical source distribution. In the
stationary model, every one-time marginal is exactly the source marginal.
Ordinary correlation tables therefore do not reveal the memory.

For source mean `1/2`, copy probability `1/2`, and four records, the iid sample
mean variance is `3/16`. The afterpulse variance is `99/256`, an inflation by
`33/16`. Any Hoeffding contract derived for independent trials is therefore
unauthorized even though every marginal check passes.

## Temporal witness

The iid adjacent-repeat probability is `5/8`; afterpulsing raises it to
`13/16`. A lag-resolved time-tag record detects the detector memory that the
science marginals forget.

Simply retaining every second event is not an exact repair. The lag-two
covariance remains `3/16` in the frozen model. Passive separation reduces
memory geometrically but does not erase it.

## Active reset

An active holdoff/reset that forces the detector state to refresh before every
retained event restores the iid joint law exactly in this declared one-state
model. This is a hardware operation, not a statistical relabelling. Its reset
success and memory depth require independent calibration.

For longer afterpulse kernels, branching cascades, cross-channel echoes, or
source bunching, a one-bin reset is insufficient. Those processes require a
larger temporal Carrier model or a confidence inequality proved for the
measured mixing law.

## Verification

Run:

```text
python research/aspect/checkers/check_afterpulse_memory_confidence.py
```

The dependency-free exact checker enumerates the iid and Markov joint laws,
verifies identical marginals, computes variance inflation and lag witnesses,
and verifies the active-reset law within the frozen model.
