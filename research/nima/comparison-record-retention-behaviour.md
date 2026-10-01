# Record retention controls settling versus recurrence

## Update and accounting

Use normalized comparison rows u and record amplitudes w. Before each
comparison return rho*w, with 0<=rho<=1. With a=u^T q, update

    q_next = q + u(rho*w-a),
    w_next = a.

The exact squared-budget identity is

    ||q_next||^2 + w_next^2
      = ||q||^2 + w^2 - (1-rho^2)w^2.

The exported budget is (1-rho^2)w^2. Thus rho is amplitude retention;
its budget fraction is rho^2. An explicit passive dilation could send
sqrt(1-rho^2)*w to an external record. Reusing that external port would require
including its feedback; here the export is removed from the modeled subsystem.

## Stability

At rho=1 the map is the closed orthogonal record-exchange sweep. At rho<1
it is contractive. A unit-modulus eigenvector would have zero loss, requiring
all incoming record amplitudes to vanish. Every record is visited once per
sweep; the eigenvector condition then also requires all outgoing records to
vanish. Every comparison mismatch is consequently zero, so the carrier lies
in the common kernel of all rows. The rows span all six coordinates, making
that kernel zero. Hence no nonzero unit-modulus eigenvector exists, and the
finite-dimensional sweep has spectral radius strictly below one for rho<1.
All initial states therefore tend to zero without driving. This argument
uses the full-rank comparison family and the specified once-per-sweep schedule.

## Numerical experiment

Start with unit covariance in the six carrier coordinates and empty records.
Initial total budget is 6. The first sweep is identical for every rho because
all returned records initially vanish.

| rho | Spectral radius | Slowest amplitude e-fold time (sweeps) |
|---:|---:|---:|
| 0 | 0.00292593758 | 0.171405 |
| 0.25 | 0.285696644 | 0.798196 |
| 0.5 | 0.533017474 | 1.58932 |
| 0.75 | 0.769924531 | 3.82464 |
| 0.9 | 0.908664782 | 10.4407 |
| 0.99 | 0.990904946 | 109.449 |
| 1 | 1 | infinite |

The e-fold time is -1/log(spectral radius), an asymptotic modal amplitude
rate. It is not a bound on all transients or an instantaneous carrier budget
rate. Carrier budget can receive backflow even as total subsystem budget falls.

After 1000 sweeps, rho=0.99 retains total budget 2.56726893e-8 and exports
5.9999999743. At rho=1, total remains 6 and carrier budget is 0.178749641.
Small displayed zeros for lower rho reflect floating-point underflow or
numerical rounding during the long decay experiment.

## Architectural meaning

A record export policy selects a settling subsystem. Closed record reuse
selects recurrent dynamics. A positive stationary budget with rho<1 requires
ongoing input. Finite memory retention alone supplies no nonzero steady floor.
These budgets are squared amplitudes; conversion to physical energy remains
an additional identification and normalization.

## Verification

    uv run research/nima/checkers/check_comparison_record_retention.py

NumPy script with inline dependency metadata. Checks spectra, local/sweep
budget balance, cumulative exported budget over 1000 sweeps, orthogonality
at rho=1, and identical first sweeps. No measured constants are used.
