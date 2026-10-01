# Optical/endpoint synthesis, iteration 4: full-history calibration certificate

## Fresh basis and declared environment

The timed-frame checker and its optical/calibration dependencies are freshly
rerun. The history retains all155 complex amplitude coordinates, including two
coherently reused environment modes. Resetting those modes is not part of this
certificate. The calibration observations and timing traces remain synthetic.

## Full-port and router bound

The preceding retained2-by2 certificate is insufficient when environment memory
returns at a later event. Use the COMPLETE four-port estimate B_hat, including
both unused inputs and both environment outputs. For entrywise complex error
radius epsilon_entry and independently bounded router-vector error epsilon_u,

    epsilon_event = ||B_hat-B_ideal||_2
                    +4*epsilon_entry+sqrt(2)*epsilon_u.

The factor4 is the Frobenius bound for sixteen complex entries. The router term
compares the ideal exchanges on the intended and actual normalized carrier
supermodes. Both full155-dimensional event operators are unitary under the
stated complete-port model.

For a word of m events, the telescoping product identity and unitary norms give

    ||F_actual_word-F_ideal_word||_2 <= sum_j epsilon_event,j.

This bound does not reset or trace out the environment between events.

## Endpoint clock uncertainty

The same timestamp is used for the output boundary of an event and the input
boundary of its successor. Thus intermediate coordinate frames cancel exactly,
including their shared timestamp errors. Only initial/final frame uncertainties
remain in the history-level coordinate comparison:

    epsilon_history <= min(2, sum_j epsilon_event,j
                              +epsilon_clock,in+epsilon_clock,out).

Clock terms use the previous phase-rate-times-timestamp-error bound. This
cancellation concerns coordinate-frame timestamps, NOT physical control drift,
unknown propagation phase or a changed router setting. Those must already be
covered by calibration valid throughout the entire history. Inconsistent adjacent
frame records do not qualify for this cancellation.

The validator checks presence of port/router/frame evidence IDs, their declared
error bounds, a covering calibration-validity interval, environment policy and
strict event ordering even after timestamp uncertainty. It rejects missing
reference evidence, stale calibration and potentially reversed/overlapping
boundaries. IDs check contract completeness, not empirical authenticity.

## Mean and covariance consequences

For the same initial full-state mean mu and positive Hermitian amplitude
covariance C,

    ||mu_actual-mu_ideal|| <= epsilon_history*||mu||,
    ||C_actual-C_ideal||_2 <= 2*epsilon_history*||C||_2.

The second inequality follows by adding/subtracting one mixed product and using
unitarity. It is a complex-amplitude covariance certificate, not a general
quantum-channel distance or an unbounded-energy guarantee. Initial preparation
errors would need their own terms; the current comparison fixes preparation.

## Executed fixture and hostile

The predeclared four-event tolerance is.08. The synthetic independent port,
router and clock bounds give:

- per-event full operator bound: .01039734;
- combined endpoint clock bound: .00232808;
- four-event operator bound: .04391744;
- actual synthetic four-event operator error: .01089884.

The separately generated mean and covariance satisfy their predicted bounds.
These are regression tests of the inequalities, not empirical confidence levels.

A severe environment control applies the same nonideal event three times.
Coherently retaining its environment versus silently zeroing that environment
after every step changes the final record mean by approximately6.99997e-6.
The fresh-vacuum policy is therefore rejected by this retained-memory contract.
It can be a legitimate different experiment, but needs its own dilation, reset
resources and statistical assumptions.

## Next decision and verification

The final packet must distinguish theoretical exact exchange, a bounded
approximate exchange, rejection of the frozen lossy plant, and absence of
measured independent calibration. A synthetic certificate must not be promoted
to evidence that an apparatus has realized the exchange.

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_optical_exchange_history_certificate.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-optical-exchange-history-certificate

Tolerance1e-10. Report: `results/optical-exchange-history-certificate.json`.
