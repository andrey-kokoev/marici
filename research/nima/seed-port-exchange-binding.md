# Conditional native-port binding of the prior reversible exchange

## What is reused

The source is the actual six-arrow seed registry and validated occurrence
execution from `check_seed_typed_execution.py`, including source/target
attachments and unique event identities. The dynamics are the existing
16-carrier/137-record exchange from `check_137_closed_record_stationarity.py`.
Neither source is modified. The checker reruns both before testing the adapter.

## Explicit adapter policy

Label the four carrier coordinates A,B,C,D. For each primitive arrow a->b,
select the EXISTING tensor-state slot (a,b) in the 16-state block of the
137 comparison ports. In zero-based indexing this is `121+4a+b`.
The first tensor factor reads tail; the second reads head.

This is a declared interpretation of the two carrier factors, not a rule
forced by native path incidence. It avoids the excluded reference arrow
in the separate 121-arrow block rather than silently restoring that arrow.
It also avoids identifying an entire composite path with its endpoint
vector difference.

The inherited carrier metric is H=G tensor G, G=10I+J. In unwhitened
coordinates the existing normalized state feature is

    f_ab=(e_a tensor e_b)/11,
    f_ab^T H f_ab=1.

For one occurrence, execute the original law:

    delta = r_ab - f_ab^T H y,
    y' = y + f_ab delta,
    r_ab' = r_ab - delta.

The six selected record channels are persistent. Every execution occurrence
has a separate retained before/after receipt; revisiting a channel does not
invent a new independently initialized mode. The remaining 131 records of
the old full model are retained unchanged. The checker compares this exact
22-coordinate active restriction against the original whitened 153-coordinate
update, with tolerance 1e-12 for that numerical comparison only.

## Properties checked

- Each event is involutive and preserves `y^T H y + sum r_i²`.
- The retained anchor `y+sum f_i r_i` is invariant.
- The prior cross-response formula holds exactly for the selected ports:
  `delta'=delta-(I+F^T H F)[:,i] delta_i`.
- The adapter's features and metric transform covariantly under all 24
  vertex relabellings. Thus the event law also transforms covariantly by
  substitution in the displayed formula; no labelling selects a coupling.
- Source-validated direct and indirect paths are executed as ordered words,
  not collapsed to equal endpoint displacements.
- Reversing the retained numerical event sequence recovers the entire
  starting numerical state. This numerical inverse is not asserted to be
  a directed inverse path in the seed.
- Repeated words with identical effects retain distinct occurrence histories.

The original native path validator is reused rather than replacing it with
an unconstrained list of port labels.

## Honest preparation control

Supply one unit in the AB record and zero elsewhere. This preparation
is external; the source did not create it.

It distinguishes AB from AD,DB numerically. An initial assertion that it
also distinguished BA from BC,CA FAILED: both return protocols remain idle
on this preparation. That failure is retained as a control. Their full
linear operators are distinct, and their histories remain distinct even
when their outputs agree. No preparation was tuned to conceal the failure.

Both the zero state and every matched preparation `r=F^T H y` remain fixed.
The new adapter therefore does not evade yesterday's initialization
obstruction or manufacture excitation from a silent source baseline.

## Boundary with the interaction pipeline

This supplies the previously missing executable CONDITIONAL port adapter,
not physical charge/mass/recoil. The carrier y is a mode amplitude, not the
particle position in the earlier impulse–drift fixture; the record exchange
is not yet its mechanical momentum transfer. No map identifying these
readouts or their energy units has been supplied.

Likewise the direct/indirect native paths here have common endpoints, not
a proved equality of their numerical actions. Any additional source face
or higher witness must be checked against this realization separately.

The remaining substantive obligations are:

1. Select or justify the tail/head tensor encoding, metric and execution law
   from the intended source, rather than merely choosing a compatible model.
2. Supply native preparation or an admitted external interaction source.
3. Construct physical configuration, momentum, inertial and coupling readouts
   compatible with the exchange and today's comparison packet.
4. Attach the execution schedule and duration to the intended intrinsic
   clock without identifying event count with calibrated physical time.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run --with sympy --with 'numpy>=2,<3' python research/nima/checkers/check_seed_port_exchange_binding.py

267 checks pass. The new identities are exact rational matrix checks,
except the explicitly numerical comparison with the old whitened fixture.
The imported source/model checkers also rerun. Receipt:
`results/seed-port-exchange-binding.json`. No new Agda physical-model
instantiation or native selection theorem is claimed.
