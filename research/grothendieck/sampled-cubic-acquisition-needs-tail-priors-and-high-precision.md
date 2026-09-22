# Sampled cubic acquisition needs tail priors and high precision

## Follow-up: a different acquisition model closes the finite-horizon gate

`time-bin-recalibration-gives-a-finite-horizon-near-optimal-cubic-observer.md` now supplies a 76-bin, horizon-64 implementation using bounded hat integrals and fresh calibration. It avoids the point-sampling and uniform old-waveform approximation requirements below. Physical acquisition accuracy remains external; the present conditional point-sample estimates remain valid in their own scope.

## Status at this stage

Implemented a conditional finite-time sampling layer for the existing finite filter, and fixed a serious precision limitation in its receiver.

Established:

- certified sup, derivative and time-tail bounds for the actual rational bulk filters;
- midpoint acquisition bounds under explicit damped-field L2, sup and bounded-variation hypotheses;
- propagation through finite-rank ordered tensors and all 449 observer blocks;
- rejection of invalid budgets and a check against the 10^(-540) acquisition target;
- a default 2048-bit receiver and a regression exhibiting failure at 192 bits.

NOT established: a practically sized sampled acquisition of the actual positive cubic source at the target error. Generic L2 bounds are much too weak, and no source-specific time-tail/BV certificates or experimental samples have been supplied. The tests are mathematical fixtures, not fabricated measurements.

## 1. Actual time kernels

For a reflected bulk field f, sample the DAMPED field g(u)=exp(-u)f(u). The previously implemented frequency filter is equivalent to

    phi(f)=integral_0^infinity k(u)g(u)du,

    k(u)=(1/(pi nu)) Re sum_j conjugate(r_j)
                              integral_(a_j)^(b_j) exp(-itu)dt.

The receiver evaluates the finite sum with Arb/Acb. At u=0 the inner integral is b_j-a_j; otherwise it is evaluated by its exact exponential antiderivative. No point sample of the frequency transform is substituted for a frequency-cell integral.

For these actual dyadic coefficients,

    M0=(1/(pi nu)) sum_j (b_j-a_j)|r_j|,
    M1=(1/(2pi nu)) sum_j (b_j^2-a_j^2)|r_j|,

bound |k| and |k'|. Put

    K=(|Im r_first|+sum_internal |r_j-r_(j-1)|+|r_last|)/(pi nu).

Integration by parts in the piecewise-constant, conjugate-symmetric frequency profile gives

    |k(u)|<=K/u,
    ||k||_L2(H,infinity)<=K/sqrt(H).

The checker verifies that the frequency cells are contiguous, that the rational normalizers make both filters contractive, and that its rounded rational bounds enclose the full sums.

Certified upper bounds are:

| bulk label | M0 | M1 | K |
|---|---:|---:|---:|
| positive compression | 6.178508121 | 2699.287044487 | 2.468173782 |
| negative leakage | 7.283807205 | 3128.772833515 | 2.019049461 |

For either weak label the kernel is a exp(-4u), a=2828427/1000000. Its bounds are M0=a, M1=4a and tail norm a exp(-4H)/sqrt(8).

## 2. A conditional sampled integral bound

Take midpoint samples on [epsilon,H] at spacing Delta. Require independent certificates for

    ||g||_L2(0,infinity)<=B,
    sup_[epsilon,H] |g|<=G,
    TV_[epsilon,H](g)<=V,
    |sample_j-g(midpoint_j)|<=sigma.

Total variation includes jumps and refers to the actual representative being sampled. These bounds are not inferred from the samples. In particular weighted L2 alone does not bound point evaluations.

The implemented error bound is

    head <= M0 sqrt(epsilon) B,
    tail <= min(K B/sqrt(H),B),
    quadrature <= Delta [M0 V+M1 G(H-epsilon)],
    sample noise <= (H-epsilon) M0 sigma.

The tail formula is replaced by the exponential weak-kernel formula for weak coordinates. Independent head/tail FIELD L2 bounds may replace the corresponding conservative terms because the full kernels have L2 norm at most one.

The quadrature estimate follows from TV(kg)<=M0 TV(g)+G TV(k). A rectangle error is bounded by its width times the integrand variation; summing cells gives the displayed conservative midpoint bound.

All kernel evaluations and sums are interval-enclosed. Arithmetic radii are retained separately from these analytical errors. An initial strip may be excluded because actual bulk fields need not have bounded variation at zero. No unproved global smoothness is assumed for the completed prime/gamma response.

## 3. Tensor and observer propagation

Sum the four field acquisition errors and the Euclidean endpoint acquisition error to obtain a one-feature error e. The true feature response norm bound is the sum of the declared field L2 bounds and an endpoint norm bound.

For an actual finite-rank ordered tensor sum_l c_l u_l tensor v_l, with feature norm bounds B_l,C_l and errors e_l,f_l, the joint-filter error is bounded by

    sum_l |c_l| [B_l f_l+C_l e_l+e_l f_l]
      + certified_projective_remainder.

This requires a supplied genuine finite-rank decomposition or certified approximation. It does NOT multiply marginal readings to reconstruct an arbitrary joint tensor. A general two-dimensional sampled-field acquisition remains a separate possible implementation.

Sum these bounds over the 449 measured blocks. The existing receiver applies its rational coefficients and reports the resulting interval. Its acquisition budget check now also includes the output arithmetic radius, converted conservatively to joint-norm units.

The original two-coordinate calibration defects remain separate. A budget check is conditional on the field assumptions; it is not evidence that real hardware or an unknown source satisfies them.

## 4. Why the generic estimate is not a practical solution

For a unit total projective-response norm budget, a time cutoff changes the two-slot filter by at most 2K_max/sqrt(H), ignoring the additional head and sampling costs. Making this particular sufficient bound at most 10^(-540) requires

    H >= (2 K_max / 10^(-540))^2
      = 2.4367527272608734096 * 10^1081.

This is NOT a necessary lower bound on all acquisition schemes. It demonstrates that this generic L2 tail estimate is computationally unusable at the desired precision. A smaller signal budget improves the formula, but it is not legitimate to silently replace a response budget by a source Gamma budget.

The productive remaining gate is to certify substantially stronger time-tail and local regularity information for the actual measured fields, or to supply a different independently justified acquisition model. Finitely many point values cannot provide those guarantees for arbitrary L2 inputs.

## 5. Precision repair

The previous default of 192 bits was inadequate for large independently measured terms that cancel in the 449-block sum. Consider two readings of size 10^(-193) differing by 10^(-540), with opposite crossed-row signs. Their gain is approximately 3.44*10^537.

The regression recovers the true difference 0.00343969364. At 192 bits its arithmetic uncertainty is about 2.54*10^287; at 2048 bits it is below 4*10^(-272).

The receiver now defaults to 2048 bits and exposes a configurable precision and its actual arithmetic error radius. It restores its configured precision on entry rather than inheriting a different observer's global Flint setting. An earlier 192-bit output enclosure was not falsely narrow, but it could be far too wide to certify the desired margin.

This repair does not manufacture measurement precision. Approximately 347 decimal orders separate these example readings' common scale and their difference; acquisition must still justify the required absolute errors.

## 6. Code and reproduction

`checkers/sample_finite_cubic_observer.py` provides:

- `Acquisition.certify_kernel_bounds()` and freshness-checked loading;
- `sample_field(...)` for conditional damped-field midpoint acquisition;
- `feature(...)` for the five-label response;
- `tensor(...)` for certified finite-rank ordered tensors;
- `evaluate(...)` for the 449-block budget and final enclosure.

Use decimal strings or Arb/Acb values, not binary-float samples advertised as high precision. Sample arrays contain values of exp(-u)f(u), not f(u).

Fresh tests:

    uv run --with python-flint python research/grothendieck/checkers/check_sampled_cubic_acquisition.py
    uv run --with python-flint python research/grothendieck/checkers/check_finite_cubic_evaluator.py

Artifacts:

- `results/finite-cubic-acquisition-kernels.json`;
- `results/sampled-cubic-acquisition-tests.json`.

The sampling tests include an analytic weak exponential fixture, exact zero data, tensor/error composition, invalid-budget rejection, and the large-cancellation precision regression. They do not assert a positive-source sampled experiment.

## 7. The independent vacuum probe remains independent

Nima's `../nima/a-vacuum-channel-distinguishes-sources-the-residual-observer-tower-cannot-see.md` supplies a valuable separate observation. Its unit vacuum coordinate distinguishes a degree-zero perturbation invisible to this homogeneous degree-two observer. It must be independently acquired; neither our 449-block evaluation nor its numerical precision can reconstruct it.

That probe's noise threshold does not replace this cubic functional's acquisition budget. Adding it enlarges the information recorded, rather than changing the frame or proving the existing observer faithful.
