# Finite-frequency filters implement the near-optimal cubic observer

## Acquisition follow-up

`sampled-cubic-acquisition-needs-tail-priors-and-high-precision.md` adds conditional time-domain sampling bounds and a 2048-bit receiver precision regression. The generic L2 tail estimate is not a practical sampled-acquisition certificate; actual-field tail and regularity budgets remain required.

## Implemented and certified

A finite rational-filter implementation now replaces the abstract simultaneous norming test in `matched-private-corrections-attain-the-full-cubic-observer-norm.md`.

At A=2, y=3, gamma=1 it uses the same 449 actual analytical blocks and the same source functional calibration targets. The filter has 151552 positive frequency cells, with explicitly specified reflected negative cells, and dyadic complex coefficients. All normalization and observer gain coefficients in the manifest are rational.

Fresh verification proves:

- each one-feature filter has response-dual norm at most one;
- the observer norm is bounded by 3.43969364*10^537 w_seam^2, less than 1.03 times the ideal optimum;
- the 268 zero source basis values remain EXACTLY zero;
- the two nonzero source calibration errors are below 0.000702 and 0.00147 per w_seam^2, respectively;
- total independent response/joint-filter error 10^(-540) leaves positive margin greater than 0.05 w_seam^2, after calibration discrepancy.

If the finite filter is recalibrated with its exact analytical gains, its exactly feasible norm upper bound is below 1.05 times the optimum. This separately certifies filter quality rather than mistaking a calibration defect for an optimization gain.

The rationally calibrated observer is an APPROXIMATION to the original functional on its two visible coordinates. Its small norm is not asserted to be the norm of an exactly feasible rational optimizer. Exact source calibration would use the analytically defined gains; the displayed certificate bounds their numerical replacement errors.

This is a finite computation on bounded integral measurements. It is not an assertion that point samples determine arbitrary weighted-L2 fields, nor a certificate for a physical acquisition device.

## 1. Replace each bulk norming waveform by a finite filter

Reflect the negative half-line to u>0. For either bulk label f put g(u)=exp(-u)f(u), extended by zero to the negative half-line, and use

    g_hat(t)=integral exp(-itu)g(u)du.

The actual even response has bulk transforms -H_+ and -H_- from the optimum certificate. Both signs are prescribed: B=-positive Tate compression and the second label is -leakage.

Use bands [0,16], [16,128], [128,2048], with respectively 2048, 512 and 32 cells per unit frequency. On each positive cell I_j=[j/rate,(j+1)/rate], choose a complex number r_j whose real and imaginary parts are integer multiples of 2^(-40), near the certified target transform midpoint. On -I_j use conjugate(r_j). Set the waveform to zero outside these cells.

For each bulk label choose the rational normalizer nu ABOVE

    sqrt((1/pi) sum_j |I_j| |r_j|^2).

Its bounded linear functional is

    phi(f)=(1/(2pi nu)) sum_j [conjugate(r_j) integral_(I_j) g_hat(t)dt
                                      +r_j integral_(-I_j) g_hat(t)dt].

Plancherel gives ||phi||<=1. The two cell integrals are independent for complex data. Replacing them by twice a real part would be wrong in the receiver, even though conjugation symmetry simplifies evaluation on the real calibration profile.

The inverse Fourier waveforms are bandlimited L2 functions with L2 derivatives. Multiplication by exp(-u), and restriction to the appropriate half-line, therefore puts the bulk tests in the admitted unrestricted-trace graph spaces D^+,D^-. Thus these filters have an actual realization in the original test space Z, unlike an arbitrary abstract norming functional. Their graph-test norms need not be one; the bound one is their response-dual norm.

There is no omitted-frequency error in implementing THIS filter: its coefficients are exactly zero outside the finite passband. Its lost response relative to the ideal norming filter is included in the certified calibration and efficiency comparison.

## 2. Endpoint and weak labels

The even endpoint vector is (2/5,2/7), after the prescribed swap. Use that vector divided by a rational upper bound on its Euclidean norm.

On each weak coordinate use

    (2828427/1000000) integral exp(-5u)f(u)du.

The multiplier is less than sqrt(8), so these functionals also have norm at most one. Their value on e(u)=exp(-3u) is h_fin=2828427/8000000.

Combine the five coordinate functionals. Because the response norm is a labelled SUM norm, the dual norm is the maximum of the coordinate norms. Thus the combined theta_fin has norm at most one, not five.

## 3. Certified source response and gains

Let C_fin=theta_fin(c_even). The checker encloses C_fin by integrating WHOLE real frequency cells, not just the points used to choose r_j. All dyadic coefficients and rational normalizers are included in that calculation. Then

    theta_fin(O Psi(F))
       =sqrt(2)X_F [C_fin+h_fin(mu_F-L)].

These values are certified positive. The exact same-window private cancellation works for ANY common functional theta_fin, hence preserves all 268 zero source values without numerical residual tests.

The crossed signed filter sum J has response

    N_x,fin=64 n_fin([2,20])n_fin([20,420]),

and the reserved positive row has response

    N_0,fin=n_fin(A_1)n_fin(B_1).

The builder chooses explicit rational gains k_x,k_0 near S_x/N_x,fin and S_0/N_0,fin. It rigorously bounds

    d_x=|k_x N_x,fin-S_x|,
    d_0=|k_0 N_0,fin-S_0|.

For a source with visible coefficients a,b, calibration error is at most d_0|a|+d_x|b|. No uniform relative bound is inferred for cancellation-prone combinations.

## 4. Actual receiver interface

`checkers/evaluate_finite_cubic_observer.py` provides:

- `Observer.feature`: evaluates the finite one-feature filter from its bounded bulk-cell integrals, two endpoint coordinates, and two weak integrals;
- `Observer.finite_rank_tensor`: evaluates a supplied ordered finite-rank tensor by bilinear extension;
- `Observer.evaluate`: combines the 449 joint-filter readings with the signed rational gains and optional final conjugation for the original first-slot convention.

Finite frequency support does not itself impose a finite time-acquisition horizon. A hardware time cutoff or numerical quadrature of raw field samples needs an additional certified error budget.

A joint theta_fin tensor theta_fin measurement is NOT the product of two marginal readings. For a completed projective tensor, a certified finite-rank approximation error can be included in the acquisition budget since ||theta_fin tensor theta_fin||<=1.

The compact CLI input is

    {
      "joint_filter_values": [["real decimal", "imaginary decimal"], ...],
      "total_joint_l1_error": "1e-540",
      "conjugate": true
    }

There must be exactly 449 readings, in manifest row order. These are unscaled measurements; the returned value and error are per w_seam^2. Bulk inputs to `feature` are CELL INTEGRALS, not cell averages or point values.

If the sum of joint-filter acquisition errors is eta, the final error is at most

    max(|k_x|,|k_0|) eta w_seam^2.

A full response error of projective l1 norm eta implies this budget by contractivity. An arbitrary list of sampled errors does not. Arb arithmetic encloses the evaluator's arithmetic rounding separately; calibration remains the explicit two-coordinate defect above.

For the positive source, the checker proves

    S_0-d_0-|k_x|*10^(-540)>0.05.

## 5. Artifacts and reproduction

Build and freshly certify:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_finite_cubic_observer.py

Receiver tests:

    uv run --with python-flint python research/grothendieck/checkers/check_finite_cubic_evaluator.py

Evaluate an acquisition file:

    uv run --with python-flint python research/grothendieck/checkers/evaluate_finite_cubic_observer.py observations.json

Artifacts:

- `results/finite-cubic-filter-cells.json.gz`: deterministic compressed dyadic coefficients;
- `results/finite-cubic-observer.json`: normalizers, gains, actual row descriptors and coefficient-file checksum;
- `results/finite-cubic-observer-certificate.json`: certified efficiency, calibration and noise bounds.

The checksum, complex frequency signs, endpoint/weak coordinates, ordered-tensor bilinearity, and invalid input rejection are tested. No experimental measurement file has been fabricated.

## 6. Source-realization boundary

Nima's `../nima/arb-certifies-a-minimum-source-lift-and-an-all-depth-realizable-tail.md` certifies a different object: a minimum source lift and an explicitly summable continuation, with its own gamma=2 private protocol. Those source budgets are not substituted for this gamma=1 acquisition error bound. The finite filter here does not infer an unseen source tail, source summability, or a calibrated inverse from noisy observations.
