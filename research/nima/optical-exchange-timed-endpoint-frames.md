# Optical/endpoint synthesis, iteration 3: delayed and time-dependent frames

## Fresh contracts and distinction

The prior endpoint adapter explicitly requires the temporal connection
H_new=S H S^-1+i dot(S) S^-1. The optical plant has a nonzero round-trip delay.
This iteration freshly reruns the plant/calibration tests and combines these
two facts. Known coordinate-frame motion is not an additional physical field,
nor can it compensate an unknown physical optical phase drift by declaration.

## Event timestamps

On the whitened carrier, records and two environment modes, define

    S(t)=diag(D(t),I137,I2).

If the laboratory event F maps an input boundary at t_in to the next stored
boundary at t_out, its moving-frame representation is

    F_new(t_out,t_in)=S(t_out) F S(t_in)^dagger.

Both timestamps matter. Using S(t_in) on both sides generally gives the wrong
output. For contiguous event intervals these maps telescope:

    F_new,n ... F_new,1
      = S(t_final) (F_n ... F_1) S(t_initial)^dagger.

A gap between events would also need its declared laboratory evolution and
frame transport; it must not silently disappear. Zero or negative round-trip
delays are rejected in the tested event API.

The physical plant emits some ports earlier than the next return. The model
assumes they are captured in declared storage and assembled at an event boundary;
it does not infer a capture/synchronization apparatus from the matrix formula.

## Retained state, covariance and history

The combined test uses155 complex amplitude coordinates:16 carrier,137 records
and TWO retained environmental modes. The same two environment modes are reused
coherently through the four-event word. They are not traced out and reintroduced
as independent vacuum at each event.

Mean and full Hermitian complex-amplitude covariance obey

    mu_next=F_new mu,
    C_next=F_new C F_new^dagger.

The test verifies their frame transport, total mean-plus-covariance budget, and
composition for both the ideal exchange boundary and the nonideal calibrated
plant. This covariance is an amplitude-moment object; a general quantum Gaussian
state additionally needs both quadratures/anomalous moments. No general quantum
state reconstruction is claimed here.

At the ideal boundary the laboratory16-anchor vector is conserved. In the moving
frame it is D(t)*a, not the same frozen numerical vector. Records stay neutral,
and the transported comparison directions make the mismatch representation
consistent. Nonideal lossy retained dynamics is not claimed to conserve those
same anchors, although the full155-port norm remains conserved.

## Continuous connection check

For a prescribed endpoint phase D(t)=diag(exp(i chi_k(t))),

    i dot(S) S^dagger = -diag(dot(chi_k),0,0).

The checker differentiates the transformed trajectory of the previously admitted
rank-one ideal Hamiltonian pulse and verifies the Schrödinger equation only when
this term is included. An additional isolated environmental phase reproduces
the ideal plant's unused-port sign. This is an interpolation consistency test,
NOT a derivation of distributed propagation inside the actual delayed cavity.
The finite event result above does not require choosing that interpolation.

Dropping the connection or using only the input-frame conjugation produces a
nonzero error on the declared hostile input.

## Calibration transport and clock error

For exactly known endpoint frames, left/right unitarity preserves the operator
error certificate:

    ||S_out (F_actual-F_ideal) S_in^dagger||_2
      = ||F_actual-F_ideal||_2.

Timing uncertainty is different. If the output timestamp is wrong by Delta t,
then

    ||S(t+Delta t)-S(t)||_2
      <= |Delta t| sup_interval max_k |dot(chi_k)|.

The synthetic clock hostile Delta t=.02 gives operator error approximately
.01185793, bounded by.01186. Thus a small clock error can exceed the optical
control error from the preceding iteration. Time/phase records belong in an
independent calibration certificate, not a post-hoc change of frame.

All phases and timestamps here are prescribed mathematical fixtures. No clock,
phase trace or synchronization apparatus has been measured.

## Next gate and verification

Next combine port/router/clock bounds into a multi-event error budget, with an
explicit choice between retained environmental memory and independently reset
ports. The accumulated error and covariance cannot be certified by switching
between those models mid-history.

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_optical_exchange_timed_frames.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-optical-exchange-timed-frames

Tolerance1e-10. Report: `results/optical-exchange-timed-frames.json`.
