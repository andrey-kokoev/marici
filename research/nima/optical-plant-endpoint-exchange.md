# Optical/endpoint synthesis, iteration 1: a conditional exchange boundary

## Freshly reused contracts

Reread and rerun the prior optical plant checker
`research/aspect/checkers/reciprocal_lossy_cavity_plant.py` and the endpoint adapter
`checkers/check_137_local_phase_covariance.py`. This test combines their actual
operations, not just their port counts. No laboratory calibration is supplied.

## Ordered four-port dilation and a phase-order repair

Keep input ports (u,x,v2,w_env) and output ports (y_ref,y_trans,x_next,y_env).
The physical ordering is input mirror, forward phase p, end mirror, return
phase q, then the loss coupler. With f=t1*u+r1*x and b=r2*p*f+t2*v2,

    y_ref = -r1*u+t1*x,
    y_trans = t2*p*f-r2*v2,
    x_next = a*q*b+ell*w_env,
    y_env = -ell*q*b+a*w_env.

The return phase MUST enter both branches of the subsequent loss coupler.
The prior prose wrote the last row without q, while its checker fixed p=q=1.
That omission is harmless at the checked zero-phase fixture but cannot be
extended to arbitrary return phases: the resulting two-port loss map is not
unitary. The present independently composed dilation inserts q before loss
and explicitly checks the hostile omitted-phase alternative. This is a scoped
correction in the combined model; the original owner's files are unchanged.

All ports use common energy-normalized complex amplitudes. Environment outputs
are retained, not treated as disappearing energy.

## Is it exchange?

Identify incident u with the addressed record amplitude and returning x with
an addressed normalized carrier supermode s=u_i^dagger*q_carrier. The retained
(record_next,carrier_next) matrix is

    B_ret = [[-r1, t1],
             [a*q*r2*p*t1, a*q*r2*p*r1]].

The frozen prior parameters r1=.6,t1=.8,r2=.8,t2=.6,a=.6,ell=.8 give retained
singular values1 and.48. They do not implement exchange, and phase changes alone
cannot repair the lost singular value.

For the positive-amplitude ideal boundary, exact exchange requires

    r1=0, t1=1, r2=1, t2=0, a=1, ell=0, p*q=1.

Then B_ret=[[0,1],[1,0]] and environmental inputs have zero feedthrough into the
retained pair. This is a limiting lossless delay-line/swap configuration, not the
original partially transmitting lossy cavity. Predeclared phases+.37 and-.37
are used as a nonzero-phase test; they are not fitted to exchange outputs.

The round-trip delay remains physical: the old return exits at y_ref, while
the incident record becomes the next carrier return only after the declared T.
Reusing the pulse requires capturing/routing the outgoing record and respecting
that event boundary. A numerical matrix does not provide those storage controls.

## Embedding and endpoint-phase transport

For each of137 labels, extract s=u_i^dagger*q_carrier, pass (w_i,s,v2,w_env)
through the four-port plant, and replace only that carrier component and record.
All carrier directions orthogonal to u_i and all other records remain intact.

At the ideal boundary this gives exactly

    q_carrier_next=q_carrier+u_i*(w_i-s),
    w_i_next=s.

The original16 conserved anchors remain fixed. Implementing the selected
supermode requires a calibrated16-mode routing network and its inverse, or an
equivalent coupler. Its existence in linear algebra is not a calibrated device.

Use a positive square-root whitening frame C=sqrt(K). For the endpoint phase
matrix D, transport K_new=D*K*D^dagger, v_new=D*v and C_new=D*C*D^dagger.
Then the whitened carrier and comparison vector transform as

    q_carrier_new=D*q_carrier,   u_i_new=D*u_i.

Records and environment ports are neutral in this declared representation.
Both the full lossy plant and the ideal exchange commute with this transport
when the addressed supermode is transported too. The checker tests all137 labels
in three independently generated endpoint frames. Leaving the supermode control
unchanged while transforming the carrier fails. These are fixed-frame tests;
time-varying frames additionally require the previously derived connection term.

## Calibration boundary and next executable test

The ideal controls are predeclared theoretical values, not measured calibration
certificates. Independent calibration must establish mirror amplitudes, loss,
round-trip phase, common port normalization, supermode routing and delay BEFORE
using the exchange discriminator. The native comparison geometry supplies none
of those measured controls by itself.

Next derive a tolerance budget and an independent port-calibration protocol for
nonzero loss, mirror deviations, phase drift and mode-routing errors. The frozen
plant already provides a decisive non-exchange control. No1/137 response fraction
is used to choose or certify these optical parameters.

## Verification

    OPENBLAS_NUM_THREADS=1 uv run research/nima/checkers/check_optical_plant_endpoint_exchange.py
    OPENBLAS_NUM_THREADS=1 uv run --with 'numpy>=2,<3' python research/aspect/scc/scc.py check nima-optical-plant-endpoint-exchange

Numerical tolerance1e-10. Both prior checkers are freshly executed. The report
is `results/optical-plant-endpoint-exchange.json`.
