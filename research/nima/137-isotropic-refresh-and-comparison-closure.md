# Isotropic refresh versus completed comparison

Use the16-dimensional tensor comparison space of the previous operation test.
Whiten its Gram metric and let u be a unit comparison direction. Write
Q=uu^T, P=I-Q. A comparison followed by independent zero-mean back-action with
covariance N sends C to P C P + N. We test the existing fixed order of121
arrow slots followed by16 state slots, with unit injected trace per step.

## Refresh required by isotropy

For target covariance C=sigma^2 I, stationarity at EVERY step requires

    N = sigma^2 I - P(sigma^2 I)P = sigma^2 Q.

Thus within this independent additive model the refresh covariance is fixed:
it injects precisely along the comparison direction. The removed and injected
budgets both equal sigma^2 at each step; total stored budget is16 sigma^2.
A full sweep removes and receives137 sigma^2. This is throughput, not an
increase in stored state energy.

The normal refresh reopens the measured direction: its final variance is
sigma^2. It does not leave the just-tested equality satisfied. This is an
exact incompatibility between full isotropy and exact current equality for
nonzero sigma, under the stated post-update readout.

## Equality-preserving alternative

The earlier back-action prototype instead injected into the equality plane.
In this16-dimensional model the normalized version is N=sigma^2 P/15.
It leaves u^T C_next u=0 and injects the same trace sigma^2. It cannot preserve
a full isotropic covariance. It can produce a periodic covariance under the
fixed schedule, with unequal losses at individual slots.

## Numerical outcomes

Starting from zero at sigma^2=1, both trials reach the1e-12 end-of-sweep
covariance change threshold in nine sweeps.

| Quantity | Normal refresh Q | Tangent injection P/15 |
|---|---:|---:|
| End-of-sweep total budget | 16 | 9.92145173356 |
| Minimum per-slot removal | 1 | 0.12084616586 |
| Maximum per-slot removal | 1 | 5.94395522844 |
| Mean arrow-slot removal | 1 | 0.490767657432 |
| Mean state-slot removal | 1 | 4.85106959067 |
| Removed/injected per sweep | 137 / 137 | 137 / 137 |

The normal rule restores isotropy without137 independent resets, but it supplies
an ongoing source of137 sigma^2 per sweep. The tangent rule balances the same
total source without equalizing slot response. All reported budgets are squared
amplitudes, not calibrated physical energies. The numerical periodic state and
per-slot values depend on the specified schedule and injection law.

## Implication for the137 programme

We now have a concrete sufficient operation for equal expected slot response,
and its exact replenishment cost. The carrier has not selected that operation,
its strength, or the relevant pre/post-update observation time. The competing
equality-preserving operation gives a different response distribution while
satisfying the same total budget balance.

A physical explanation must identify which comparison notion applies:
continually refreshed sampling or an agreement that remains enforced, or an
explicit alternating protocol combining phases. Average incoming resource per
scheduled attempt alone cannot decide this. Neither trial identifies1/137
with the electromagnetic interaction observable.

## Verification

    uv run research/nima/checkers/check_137_isotropic_stationarity.py

Checks per-step covariance/trace balance, isotropic covariance identity,
tangent-plane equality, convergence and stationarity, positivity, total sweep
balance, normal refresh scaling, and zero-input/no-source behaviour. NumPy
numerics use explicit tolerances; the covariance identities are given above.
