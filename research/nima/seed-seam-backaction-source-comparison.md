# Existing back-action laws versus the actual seam

## Positive result: one comparison already changes later readings

The existing conservative exchange model has carrier q, retained records w_i and unit feature vectors u_i. It executes

    delta_i=w_i-u_i^T q,
    q'=q+u_i delta_i,
    w_i'=w_i-delta_i,

with all other w_j unchanged. Direct substitution gives

    delta'_i=-delta_i,
    delta'_j=delta_j-<u_j,u_i> delta_i  (j != i).

Equivalently delta'=delta-K[:,i]*delta_i for K=I+UU^T. This is actual endogenous back-action in the declared model: the shared carrier changes the next comparison, even when that next record has not been touched. It precedes the random-schedule/mean reduction and does not require a new relaxation gain.

The existing checker now explicitly verifies this formula for all 137 events on two preparations, including a single-record excitation whose overlaps change other readings. These are floating-point fixture checks at tolerance 1e-10; the formula itself follows algebraically.

Each event is an invertible orthogonal reflection. The packet (a=q+U^T w, delta=w-Uq) reconstructs the full numerical state and preserves its quadratic budget. Recovering a prior state requires the event identity; preserving current numerical state is not preservation of an entire unknown schedule history.

## What supplies its kernel

`check_137_closed_record_stationarity.py` constructs U from tensor-product features on two four-state carriers, with Gram G=10I+J, one excluded directed edge per carrier, eleven remaining arrow differences and four state basis features. Features are whitened and normalized. The source therefore contains a specified metric, feature encoding, comparison domain and event law.

These are not extracted from the six primitive seed occurrences or their two-by-two seam square. In particular, encoding an entire path merely by its additive endpoint displacement identifies AB with AD DB (both e_B-e_A), and BA with BC CA. That naive extension would lose the direct/indirect distinction. A sequence of primitive exchanges with separate records is a different possible protocol; its carrier binding, feature assignments and occurrence law would need to be supplied.

## Family feedback is a different law

The family-disagreement construction acts on the thirty primitive matrix legs of the existing fixture, preserving weighted family means and archiving the kicks. It changes later factored products through terms linear and bilinear in the surviving fluctuations. Thus it also provides state-derived changes rather than arbitrary external increments.

But it postulates relaxation, the grouping and gain. It does not create a preparation from zero or select family means. Its source data are matrix legs, not the exchange model's q,w coordinates.

The existing adapter obstruction remains decisive: the exchange mismatch mean has no nonzero fixed vector, while family feedback preserves a 32-dimensional mean sector. A linear intertwiner cannot retain those family means; even the full exchange mean has only sixteen conserved linear directions. We reran this control rather than asserting that one law derives the other.

## Applicability decision

There IS a working prior answer to 'what does one comparison change?': an exchange changes the shared carrier, propagating to other mismatch readings through a source-feature overlap kernel. The missing item is NOT a generic back-action formula.

Neither inspected law is already bound to the seam's direct/indirect path ports. Adopting exchange would require an explicit interpretation of the seed as carrier plus records and an independently justified feature/metric assignment. Adopting family relaxation would require a physical calibration principle and its group/gain selection. Those are hypothesis decisions, not consequences of path incidence.

Therefore keep the existing exchange law as the strongest reversible back-action candidate, with its precise unmet adapter obligations. Do not build a third guessed update or transfer its equilibrium/budget claims to the family model or the seed.

## Fresh verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_exchange_feedback_adapter.py
    python research/nima/checkers/check_family_disagreement_preparation.py

Both pass. The first includes new event-level cross-response checks and the original failed linear-adapter controls; the second is unchanged and checks retained-kick recovery and family-mean preservation. Existing result files were refreshed. No physical seed interpretation or calibration was asserted.
