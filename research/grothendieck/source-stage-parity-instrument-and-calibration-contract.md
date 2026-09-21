# Source-stage parity instrument and calibration contract

## Outcome

A single authorized source-stage parity channel separates the established positive-mixture collision. This packet constructs the conditional finite instrument and gives its statistical acceptance rule. It does not claim a measured apparatus, measured calibration, or a map from the arithmetic theta source to accessible route events.

## Declared source and one-output objective

Fix the ordered pair block ((0,1),(2,3)). Its four routes are 0123,0132,1023,1032. Their parity signs are s=(+1,-1,-1,+1), determined by the product of the two internal pair orientation signs.

The rival distributions are p_plus=(1/2,0,0,1/2) and p_minus=(0,1/2,1/2,0). Their complete edge marginals agree, but the parity expectations are +1 and -1. The task is discrimination of these two declared source distributions, not tomography of arbitrary routes or a proof of arithmetic confinement.

A source event interface must expose the ordered prime-index events while each route is running. A finite accumulator stores the pending first label of a pair and a parity bit, toggling that bit when a completed pair is reversed. It must validate the ordered-pair block. If routes from multiple blocks are admitted, their block identity must be retained or separately selected; the single-block contract cannot silently discard leakage into other blocks.

This event access is an input requirement, not an inference from the final edge record. Any instrument taking only those equal edge marginals must fail the discrimination test.

## Classical instrument

For classical route probabilities p, the instrument outputs Y in {+1,-1} with ideal law

Pr(Y=y)=sum_(routes r with s_r=y) p_r.

Thus E[Y]=s^T p. This is a legitimate parity record for a classical mixture. It is not a linear measurement of complex route amplitudes.

Suppose each pair orientation bit is independently flipped with probability q_1,q_2<1/2, independently of the input route. The observed sign is Y=s_r (-1)^(F_1+F_2), so

g=(1-2q_1)(1-2q_2), E[Y]=g s^T p.

The calibrated estimator mu_hat=mean(Y)/g has variance (1-g^2 mu^2)/(N g^2) for N independent identically distributed trials. The unit is a dimensionless parity contrast. These independence and stationarity assumptions must be established by the calibration protocol; they are not implied by the combinatorial source.

If flips are correlated, the gain is instead g=1-2 Pr(F_1 != F_2). Marginal flip rates alone do not determine it. The checker supplies the hostile q_1=q_2=1/4 with perfectly correlated flips: the actual gain is one, whereas the independent formula predicts one quarter.

## Frozen numerical fixture, not measured calibration

Choose q_1=1/10 and q_2=1/5, giving g=12/25. The rival means are +/-12/25. For either extremal rival, a wrong-sign decision requires a sample mean error at least g. Hoeffding for bounded signs gives

Pr(wrong sign) <= 2 exp(-N g^2/2).

Since log 40<4, N=36 is sufficient for error less than 0.05 under the stated independent-trial model. This is a conservative mathematical fixture, not an experimental sample-size certification.

For gain uncertainty |g-g_hat|<=delta_g, readout offset |b|<=delta_b, and sampling error at most epsilon, use a positive lower gain g_min=g_hat-delta_g. The extremal signs are separated whenever g_min>delta_b+epsilon. For estimating a general mu with |mu|<=1, division by g_hat gives error at most (delta_g+delta_b+epsilon)/g_hat. Calibration drift and route-dependent errors require additional bounds.

## Coherent source: different instrument and observable

For a route amplitude x=sum_r x_r |r>, implement the reversible controlled marker

U |r>|b> = |r>|b XOR f(r)>, where (-1)^f(r)=s_r.

If the marker is initialized in |->, phase kickback gives U(x tensor |->)=D_s x tensor |->, with D_s=diag(s). The route register remains coherent. Irreversibly measuring intermediate route labels instead generally changes the source experiment.

Recombine against the normalized reference row u=(1,1,1,1)/2. The output mode amplitude is

a=<u,D_s x>=(1/2) sum_r s_r x_r.

Intensity measures |a|^2, not a. A calibrated phase reference and two quadratures are required to recover its complex value in a coherent-field implementation. For an unknown single-photon state, one must instead specify an appropriate operational reference and measurement model; a complex state coefficient is not automatically an observable.

The checker contrasts x=(1,1,1,1)/2 and z=(1,-1,-1,1)/2. They have identical route intensities but signed amplitude sums zero and two. Parity counts on their route probabilities therefore cannot replace the coherent amplitude instrument.

This finite controlled-unitary model assumes accessible coherent route control. It is not a physical constructor for the arithmetic source.

## Admission requirements before promotion

A real source adapter must supply:

1. source state class: probabilities, coherent amplitudes, or density operators;
2. a source-derived map into ordered route events or a coherent route register;
3. authorized interactions implementing pair orientation parity, with environmental leakage controlled;
4. block-selection and invalid-event handling, without outcome-fitted postselection;
5. declared record units, gain, offset, joint covariance, trial dependence and drift bounds;
6. for coherent amplitudes, a nonzero phase reference and its calibration;
7. a commutative source-to-instrument comparison on declared generators, including the collision witness.

Current status: items 1 and the finite conditional implementation can be specified here; the arithmetic map in item 2 and measured calibration in item 5 remain absent from this packet. The earlier raw theta inverse barrier is not removed by this hypothetical source intervention.

## Verification and provenance

`python research/grothendieck/checkers/check_route_parity_instrument.py` passes exact checks of both rival laws, independent flips, a correlated-noise hostile, equal edge marginals, phase kickback, intensity/amplitude distinction, and the rational constants in the sample bound. It runs no hardware experiment or stochastic simulation.

The parity source is the block-kernel theorem in `research/voevodsky/prime-packet-signature-order-scaling-and-walsh-completion.md`. Instrument boundaries follow the accessible-marker and reference-phase contracts in `research/aspect/polarization-marker-quantum-eraser.md`. Calibration requirements follow `research/voevodsky/sector_derived_product_metrics_are_noise_whitened_readout_metrics_not_arbitrary_direct_sums_20260911.md`.
