# Optical/endpoint synthesis, iteration 2: independent calibration bounds

## Fresh starting point

The first combined test found that the frozen lossy cavity is not exchange,
while its ideal lossless boundary is. This iteration freshly reruns that test
and derives a prospective calibration certificate. All calibration data used
here are SYNTHETIC. No apparatus has been measured or independently certified.

## Analytic control budget

In the common energy-normalized selected record/carrier coordinates, write

    T = diag(1,h) M,
    M = [[-r1,t1],[t1,r1]],
    h = rho*exp(i phi),   rho=a*r2,
    phi=arg(p*q).

Assume the positive near-ideal branch t1,r2,a>=0, normalized mirror/loss pairs,
and a round-trip phase bound |phi|<=pi. For the swap J,

    ||T-J||_2 <= sqrt(2*(1-t1))
                 +(1-rho)+2*rho*sin(|phi|/2).

The first term is exactly ||M-J||_2; the remaining terms bound |h-1|. Thus
mirror error, retained-amplitude deficit and independently measured phase error
have separate contributions. Phase adjustment cannot undo lost amplitude.

The unused-input feedthrough into retained ports has norm

    ||E||_2 = sqrt(1-rho^2).

For independent vacuum inputs its added quadrature covariance is E E^dagger/2.
In particular T T^dagger/2+E E^dagger/2=I/2. Omitting that term gives an incorrect
coherent-state covariance even if the environment has zero mean.

## Mode-router error

Let u be the intended normalized carrier supermode and v the actual calibrated
one. The ideal exchange normals are d_u=(u,-e_i)/sqrt(2) and d_v=(v,-e_i)/sqrt(2).
The rank-one projector bound gives

    ||H_v-H_u||_2 <= sqrt(2)*||v-u||.

For a calibrated vector error ||v-u||<=epsilon_router, the retained system
operator error is therefore bounded by the optical two-port error plus
sqrt(2)*epsilon_router. Phase is part of this vector error: the record port is
neutral, so an unmeasured phase of v cannot be quotiented away.

Both u and v transform by the endpoint phase matrix D; the error bound is
unchanged. This is a fixed-frame statement, not yet a time-varying-frame model.

## Independent port calibration protocol

Before exchange validation:

1. Establish common energy/amplitude normalization and stable phase-referenced
   input/output quadratures.
2. Inject four known coherent unit basis probes into the four INPUT ports,
   including normally unused ports, and read all four complex outputs.
3. Bound each complex calibration entry error by epsilon_entry using independent
   metrology. The current test supplies that bound synthetically; it does not
   derive it from calibration shot counts.
4. Independently characterize the16-mode router vector, including relative phase,
   and supply epsilon_router.
5. Freeze the resulting operator bounds and acceptance threshold before using
   held-out exchange inputs.

For the estimated retained2-by2 block T_hat and environment block E_hat,

    epsilon_system = ||T_hat-J||_2 +2*epsilon_entry
                     +sqrt(2)*epsilon_router,
    epsilon_environment = ||E_hat||_2 +2*epsilon_entry.

The factor2 follows from the Frobenius bound on four bounded complex entries.
For system mean x and environmental mean e,

    ||output_actual-output_ideal||
      <= epsilon_system*||x|| + epsilon_environment*||e||.

This is a deterministic amplitude/operator certificate under the stated model.
It is not a diamond-norm bound for arbitrary quantum states, nor an assumption
that environment correlations or uncontrolled input noise are absent. The vacuum
covariance calculation requires independent vacuum environment inputs.

## Executed synthetic test and hostiles

The settings are frozen before generating any held-out inputs:

    r1=.002, t2=.003, ell=.004, round-trip phase=.005,
    epsilon_entry=.0001, epsilon_router=.0011.

The other mirror/loss coefficients follow normalization on the positive branch.
Synthetic four-port complex probe responses produce bounds approximately
.00747633 for the retained system and .00517769 for environmental feedthrough.
The declared retained acceptance threshold is.02. Forty separately seeded
complex input states satisfy the predicted error inequality; their maximum
observed error is approximately.00118867. These tests regress the analytic
bound, not prove it by sampling.

Two severe controls pass:

- The original frozen lossy cavity fails the same exchange tolerance.
- An output phase flip preserves every basis-probe intensity while changing the
  retained swap operator by norm2. Intensity-only calibration cannot certify
  the signed exchange, even with perfect noiseless intensities.

## Next gate and verification

Time-dependent endpoint frames need the temporal connection and explicit
round-trip timestamps. Next test whether calibration transports consistently
through a delayed multi-event experiment rather than treating all phases as
simultaneous static settings.

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_optical_exchange_calibration_bounds.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-optical-exchange-calibration-bounds

Tolerance1e-10. Report: `results/optical-exchange-calibration-bounds.json`.
No1/137 statistic selects or certifies any optical control in this calculation.
