# Optical plant + endpoint adapter: final bounded verdict

## Answer

The two prior constructions combine consistently. The frozen lossy optical
plant does NOT realize exchange. An ideal lossless boundary realizes all137
addressed exchanges, and a nearby plant admits a prospective independent-control
error certificate. The certificate has been tested on synthetic calibration
and held-out inputs; no independently measured apparatus realization is claimed.

## What was combined, and what was repaired

- The prior four-port optical dilation retains incident/returning fields, end-
  mirror input, loss input and every output, with its ordered propagation delay.
- The prior endpoint adapter transports the tensor state, metric and normalized
  comparison features together; records are neutral under the declared action.
- The return phase must enter BOTH branches of the subsequent loss coupler.
  The prior optical prose omitted it in the environment-output row, although
  its zero-phase checker was unaffected. The combined model explicitly corrects
  this phase-order extension without changing the original owner's files.
- A calibrated supermode router selects u_i^dagger*q from the16-mode carrier.
  Its inverse returns the modified component, with all orthogonal components
  and other records retained.

## Exact versus approximate exchange

At the positive-amplitude ideal boundary

    r1=0, t1=1, r2=1, t2=0, a=1, ell=0, p*q=1,

the retained two-port matrix is the swap and environment inputs do not feed it.
This is a lossless delay-line/swap limit, not the original lossy resonator.
The original retained singular values are1 and.48, so phase correction alone
cannot restore exchange.

For independently estimated complex four-port amplitudes and bounded router
error, the full-event certificate is

    epsilon_event = ||B_hat-B_ideal||_2
                    +4*epsilon_entry+sqrt(2)*epsilon_router.

For a history with retained environment, sum these event bounds and add the
initial/final frame timestamp bounds. The synthetic four-event example yields
.04391744 against a PREDECLARED tolerance.08. Its actual synthetic operator
error is.01089884. Neither number is an experimental measurement.

A failed upper-bound test is inconclusive, not a disproof of the plant. The
final checker enforces that distinction: a tighter.03 threshold is not certified
by this bound even though the synthetic error is below.03. A lower error bound
above tolerance, in contrast, rejects the tested frozen plant.

## Timed reference transport and environment memory

For an event crossing a round-trip boundary,

    F_new = S(t_out)*F*S(t_in)^dagger.

Using only the input timestamp fails. Continuous ideal-pulse coordinates also
require i*dot(S)*S^dagger; this connection is coordinate transport, not a new
physical force. Contiguous shared frames telescope, so consistent intermediate
coordinate timestamp errors cancel. Physical phase/control drift still needs
its own calibration bounds and cannot be removed by changing representation.

The certified history reuses two environment modes coherently. Silently replacing
them by fresh vacuum changes a later record mean. A reset environment is a
possible different apparatus, but requires its own dilation, reset and statistical
contract. The same distinction applies to capture/storage at delayed event
boundaries.

## What independently calibrated controls must contain

The physical claim remains blocked until a measured packet supplies:

1. Four known input-port probes with complex, phase-referenced output records,
   amplitude standards and independently justified uncertainty bounds.
2. Phase-sensitive16-mode router characterization for every addressed slot.
3. Time-stamped endpoint phase and clock/synchronization uncertainty records.
4. A calibration validity interval and acceptance tolerance fixed before the
   held-out exchange tests.
5. An environment access/reuse/reset policy and stored-port timing contract.
6. Held-out exchange/echo/rectangle observations with preparation and detector
   calibration; no fitting controls to those target observations.

Intensity-only tomography is insufficient. A source-ID or a metadata field
claiming `measured` is also insufficient: it does not verify experimental
provenance or uncertainty. The final gate never promotes such a label by itself.

The tolerances here concern common energy-normalized amplitudes and Hermitian
complex-amplitude covariance. They do not establish a general quantum-channel
distance or derive a current/field coupling. No1/137 statistic is used to choose
or calibrate the optical controls.

## Evidence and reproduction

- [Combined optical/phase test](optical-plant-endpoint-exchange.md)
- [Independent calibration bounds](optical-exchange-independent-calibration-bounds.md)
- [Timed frames and connection](optical-exchange-timed-endpoint-frames.md)
- [History certificate and environment hostile](optical-exchange-history-calibration-certificate.md)

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_optical_exchange_final_gate.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-optical-exchange-final-gate

The final test freshly reruns all four synthesis checkers and both original
optical/endpoint checkers through their dependency chain. Numerical tolerance
is1e-10 where specified. Report: `results/optical-exchange-final-gate.json`.

The bounded mathematical synthesis is complete. Hardware validation awaits the
measured packet above. Further synthetic passes cannot substitute for that input.
