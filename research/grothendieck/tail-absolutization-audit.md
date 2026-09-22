# Tail-absolutization audit

This is a source audit, not a claim that every absolute bound is avoidable or unsound. It separates a deliberate worst-case contract from an analytical tail where a combined signed functional may retain information.

## Highest-value active target

`checkers/certify_signed_fixed_hat_pairing.py` is the clear remaining target.

- Lines 82, 114--115 replace the post-cutoff archimedean and prime-power kernels by symmetric radii using `abs(B0)`, `abs(J[-1])`, `abs(currentJ)`, and future-hat suprema.
- The finite sum already retains the combined signed kernel. The cutoff tail does not.
- This is exactly the mechanism exposed by the frozen midpoint DPC task. The fixed `N=10^6` enclosure was unresolved; the recorded fixed refinement ladder reaches feasibility at `N=16,000,000`.

A next analytical improvement should partition the remaining log-prime tail at hat knots and apply partial summation to the actual signed kernel on each interval. It must prove each kernel's sign/variation or retain an interval enclosure of its signed Stieltjes integral. Replacing it with a better numerical cutoff alone is not the same result.

## Genuine but currently secondary candidates

### Dual-witness mixed Gaussian tails

- `checkers/arb_t_remainder_bound.py`, lines 32--35;
- `checkers/arb_dual_x_derivative_remainder.py`, lines 27--29.

These first integrate `abs` of the two derivative integrands separately over both signs of the Gaussian variable and then use

    |A| tail_r + |B| tail_rx.

The desired Taylor coefficient is a combined functional (`A*r-B*rx` or its x-derivative analogue). Parity in the plus/minus-y contributions and correlation of the two polygamma terms are discarded. This is a plausible signed-tail project, but these files only support an unfinished dual-witness route; they are not presently the source-task calibration bottleneck.

### Theta centered-moment integration tail

`checkers/refine_theta_mass_quadrature.py`, line 57, applies a symmetric bound to the omitted v>32 contribution to the centered moment. Its coefficient can change sign, so sign/monotonicity subdivision could narrow `mu`.

This is a real interval dependency loss, but its tail is exponentially small and the prior theta refinement already showed that theta mass/moment uncertainty was not the active middle-case obstruction. It is low priority unless a new task makes moment width limiting.

### Higher theta and endpoint certificates

- `checkers/theta_moment_fourth_derivative_certificate.py`, lines 41--42;
- `checkers/theta_adjacent_block_directed_box_certificate.py`, lines 168--184;
- `checkers/theta_compact_endpoint_decimal_interval.py`, lines 228--400.

These use symmetric/absolute contour, label, or derivative-tail allowances. Some label or orbit sums may have exploitable cancellation, but the recorded allowances are either intentionally enormous safety margins or are not connected to the current source-task gain. They need a concrete limiting margin before refinement work is justified.

## Absolute bounds that are not cancellation opportunities under the stated contract

### Source-task residual tails

`checkers/three_channel_source_task.py`, lines 164--181, uses an explicit weighted L1 prior on unmeasured source coefficients. The tail region itself permits arbitrary independent signs. Replacing its bound by cancellation would strengthen the source prior or add correlation information; it cannot be done merely by rearranging the proof.

### Squared response norms

- `checkers/certify_even_response_norm.py`, lines 38--60;
- `checkers/refine_bulk_response_norm.py`, lines 53--117.

These control nonnegative squared norms. The refined version already preserves substantial log-vector/cancellation structure before the final norm tail majorant. A signed scalar pairing is the correct escape from this norm information loss, and that was implemented by the fixed-hat calculation. There is no sign cancellation in a norm square itself.

### Directed cumulant and all-integer majorants

- `checkers/xi_fifth_cumulant_transition_certificate.py`, lines 42--65;
- `checkers/integer_tail_moment_arb_bound.py`.

Here the omitted prime-power contribution is substituted by an all-integer positive majorant in a one-sided lower/upper proof. The terms have the direction needed by that certificate. Sharpening may be possible by using prime powers rather than all integers, but it is not a lost cancellation claim.

## Conclusion

The only demonstrated decision-relevant tail absolutization is the signed fixed-hat prime/archimedean cutoff tail. The dual Gaussian derivative tails are the next credible signed-functional target, but only after tying their reduced remainder to a currently limiting certified witness margin.
