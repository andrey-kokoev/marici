# Metric regularity: full operational theorem constructed

Selected action: `prove/completion-phase-metric-regularity`.
The same resumed attempt is now **completed ++**, after fresh safe Agda closure of `TickConstructedPhaseDerivative`. Metric continuity and the derivative law are proved for all completion-valued scales, times and increments. No standard-real interpretation or mixed-level acceptance is used in this regularity proof. The component history below is retained; its former open gates are discharged by the final assembly.

## Constructed theorem

`agda/TickPhaseMetricContinuity.agda` constructs:

```agda
operational-phase-metric-continuous : (p : MetricCompletionCandidate)
  → ComplexMetricContinuous (phase p)
```

This applies at every completion-valued time and for every completion-valued scale, to the existing `TickCompletionPhase.phase`, not a substitute real-number backend. There are also unconditional continuity theorems for operational cosine, sine and multiplication by a fixed completion scalar.

### Metric, not path-equality continuity

`agda/TickCompletionMetric.agda` defines dyadic balls on the quotient by the existence of representatives satisfying an eventual rational error bound. It does **not** incorrectly descend `EventuallyWithin` at a fixed precision: that relation can change when representatives are replaced at a boundary.

The proved `within-representatives` theorem recovers the usual eventual bound for any chosen representatives, with two bits of slack. Reflexivity, symmetry, a quantitative triangle law and separation are proved. This gives the Cauchy metric uniformity. Continuity has quantifier order

`for every center and output precision, there exists an input precision, valid for every neighboring point`.

### Closing the pairwise-modulus gap

The library's trigonometric comparison bounds depend on **both** input representatives. That alone is not a local continuity theorem.

`agda/TickLocalRadiusBound.agda` proves that if y is eventually within 1 of x, then

`canonicalDyadicExponent(y) <= canonicalDyadicExponent(x) + 3`.

Regular Cauchy bounds control even y's early samples. Leastness of the canonical dyadic exponent then bounds every possible comparison exponent by a number depending only on x. A finite maximum of the existing schedule-depth function supplies a local modulus, without assuming that the schedule function is monotone.

The cosine/sine moduli and fixed-product modulus descend to the actual quotient. Composition gives angle continuity. The existing exact `phase-real` and `phase-imaginary` identities identify the result with the operational phase, and a shared modulus controls both coordinates.

## Original derivative specification (now inhabited)

`agda/TickCompletionDerivative.agda` defines the completion's closed nonnegative cone using eventual rational inequalities with arbitrarily small additive slack. Its derivative predicate is the standard squared first-order remainder criterion:

`||f(t+h) - f(t) - h*v||^2 <= epsilon^2 * h^2`

for all sufficiently small **completion-valued** increments h. It is not restricted to rational increments, sampled times or formal derivatives of a symbolic surrogate.

`agda/TickPhaseMetricRegularity.agda` specifies

```agda
PhaseDerivativeLaw = (p t : MetricCompletionCandidate)
  → HasMetricDerivative (phase p) t (phaseGenerator p t)
```

where `phaseGenerator p t = (0,-p) * phase p t`. The full `PhaseMetricRegularity` type pairs this law with the constructed continuity theorem. The final assembly below now inhabits this exact full type.

## New kernel component: exact reduction to the origin

`agda/TickPhaseDerivativeReduction.agda` reuses the unconditional operational addition theorem and unit-norm theorem constructed before/during the pi branch. For arbitrary completion-valued p, t, h it proves

```text
firstOrderRemainder (phase p) t (phaseGenerator p t) h
  = phase p t * (cos(-p*h)-1, sin(-p*h)-(-p*h))
```

and, by multiplicativity of squared norm and exact unit norm of `phase p t`,

```text
normSquared(firstOrderRemainder at t) = normSquared(local remainder at -p*h).
```

No bound depending on the centre t is needed. The module proves both conversion directions between the specified derivative at the origin and `LocalPhaseDerivativeBound p`, and constructs `origin-derivative-to-all-times`. These are exact operational-completion theorems, not transfer through the written standard-real interpretation. The local bound is an explicit remaining input, not a postulate or claimed inhabitant.

Fresh `--safe --ignore-interfaces` closure passed in **1517.349 seconds**. Receipt: `results/phase-derivative-reduction-fresh.json`. It explicitly records `derivative_proved: false` and `local_derivative_bound_proved: false`.

## New kernel component: closed-order limit transfer

`agda/TickCompletionOrderLimits.agda` now proves `rational-limit-nonnegative` directly for the existing existential-representative cone. It combines all-precision eventual rational lower bounds with metric convergence, spending one bit on splitting the additive slack and two bits on arbitrary-representative comparison. No choice of infinitely many representatives is needed.

`rational-limit-order` consequently transfers moving rational inequalities into `CompletionLE`. In particular `rational-quadratic-bound-limit` proves:

```text
r_n -> x, s_n -> y, u_n -> h
and, for each k, eventually
  r_n^2 + s_n^2 <= epsilon^2 * u_n^2 + precision(k)
imply
  CompletionLE (normSquared (x,y)) (epsilon^2 * h^2).
```

The actual increment factor survives the limit. The theorem neither divides by h nor assumes h is nonzero; it also covers h=0. It uses operational multiplication continuity for two independently moving rational sequences. The rational estimate and convergence of the supplied sequences are explicit premises: this is a constructed transfer theorem, not a constructed derivative bound.

Fresh safe `--ignore-interfaces` closure passed in **79.501 seconds**. Receipt: `results/completion-order-limits-fresh.json`, admitted as a supporting component with `rational_derivative_estimate_proved: false` and `derivative_proved: false`.

## New kernel component: actual relative residual estimate

`agda/TickTrigRelativeRemainder.agda` improves the earlier fixed-radius estimate to retain the actual rational angle: for |q| <= 1/2 and independent cutoffs n,m,

```text
|cosinePartialSum(q,n)-1| <= q^2
|sinePartialSum(q,m)-q| <= q^2
squared residual norm <= 2*q^4.
```

The proof splits the decidable sign of the rational angle and reuses the existing all-cutoff Taylor tail bounds. It then proves `scaled-relative-residual-bound`: for |p| <= P, |h| <= d, |-p*h| <= 1/2 and `2*P^4*d^2 <= epsilon^2`, the squared residual is at most `epsilon^2*h^2`. This is uniform in both cutoffs and covers h=0 without division.

`agda/TickRationalPhaseDerivativeBound.agda` supplies the actual cosine/sine residual sequences, proves convergence to the implemented operational values, and applies `rational-quadratic-bound-limit`. The resulting `rational-operational-relative-bound` is a CompletionLE inequality at embedded rational p,h, not merely a finite polynomial claim. Its explicit scalar/radius budget hypotheses remain.

Fresh safe `--ignore-interfaces` closure passed in **856.666 seconds**. Receipt: `results/rational-phase-derivative-bound-fresh.json`. The receipt records rational-input operational closure, not all-completion-input differentiation.

## New kernel component: extension to arbitrary completion inputs

`agda/TickCompletionClosedOrder.agda` proves that the actual closed nonnegative cone, and hence `CompletionLE`, is preserved by convergent **completion-valued** sequences with eventual inequalities. Each tolerance selects only one sequence value and one representative; no countable choice or boundary-sensitive quotient descent is used. Joint continuous order transfer and bounded rational density follow.

`agda/TickCompletionRelativeBound.agda` instantiates this transfer with the rational operational estimate. For arbitrary representatives x,y with eventual rational bounds P,d, and the explicit budgets `P*d <= 1/2` and `2*P^4*d^2 <= epsilon^2`, it proves the operational squared residual at angle `-( [x]*[y] )` is at most `epsilon^2 * [y]^2`. Both scale and increment are now arbitrary completion values, not restricted to embedded rationals. The proof uses their moving rational approximants, operational residual continuity, multiplication continuity and closed order.

Fresh safe `--ignore-interfaces` closure passed in **763.890 seconds**. Receipt: `results/completion-relative-bound-fresh.json`. This is the bounded completion-input estimate, not yet the quantified derivative modulus.

### Historical remaining gate (discharged below)

Construct `(p : MetricCompletionCandidate) -> LocalPhaseDerivativeBound p`. The squared local residual must be at most `precision(k)^2 * h^2` in the existing `CompletionLE`, for every sufficiently small completion-valued h, including zero. The modulus may depend on p and k, but not t or h.

The existing `TickCompletionTrigSmallAngle` bounds each trigonometric residual by e squared whenever the angle has rational magnitude bound e (e at most 1/4). A fixed-radius absolute e-squared estimate alone does **not** prove the required relative h-squared estimate as h approaches zero. The new relative Taylor estimate and its convergent residual sequences now instantiate that bridge for rational p,h with explicit bounds. The density extension is now constructed. Next choose a dyadic radius from a bound on the completion scale p and the desired precision, and obtain the required eventual representative bounds from `CompletionWithin zeroCompletion h l`, allowing the two bits of representative-comparison slack. Finally align `localResidualNorm` (angle `-(p*h)`, cosine subtracting embedded one) with `phaseLocalRemainder` (angle `(-p)*h`, cosine subtracting completion one). These algebraic paths and the modulus instantiate LocalPhaseDerivativeBound; no further rational-input restriction is permitted. No division by a possibly zero/non-apart h is justified. Once that gate is proved, the new reduction supplies all times and the existing continuity theorem supplies the full regularity pair.

## Final assembly: modulus and full derivative

`agda/TickPhaseDerivativeModulus.agda` supplies an explicit modulus. For representative scale bound `P = 2^d`, output tolerance `epsilon = 2^-k`, choose

```text
residualDepth d k = d + (d + (k+1))
delta = 2^-(2d+k+1)
derivativeDepth d k = residualDepth d k + 2.
```

The two additional input bits pay for arbitrary-representative comparison. Exact dyadic cancellation proves `P*delta <= 1/2` and `2*P^4*delta^2 <= epsilon^2`.

`agda/TickConstructedPhaseDerivative.agda` constructs:

- `canonical-magnitude`: a bound on every scale sample;
- `ball-eventual-magnitude`: the actual completion ball supplies eventual bounds on every shifted increment sample;
- `local-residual-identification`: the operational residual is exactly the one used by the origin-reduction theorem;
- `constructed-local-phase-derivative-bound`: quotient elimination gives the required truncated modulus at every completion scale;
- `operational-phase-derivative : PhaseDerivativeLaw`;
- `operational-phase-metric-regularity : PhaseMetricRegularity`.

All increments, including zero, are covered without division. The proof constructs the local bound, transfers it to every time using exact unit norm, and pairs it with the existing metric continuity theorem.

Fresh safe `--ignore-interfaces` closure passed in **1698.374 seconds**. Receipt: `results/constructed-phase-derivative-fresh.json`, with `derivative_proved: true`, `full_metric_regularity_proved: true`, and `outcome: ++`. The net admits only this full fresh receipt for regularity closure. The next ready node is `completion-unit-circle-flow`; full half-turn and whole-return assembly remain open.

## Verification and net bookkeeping

The checker records cached and fresh runs separately:

- `results/phase-metric-continuity-cached.json`
- `results/phase-metric-continuity-fresh.json`

The fresh `--safe --ignore-interfaces` dependency closure **passed in 284.913 seconds**. Only such a passing fresh closure admits the continuity checkpoint to the net. Sources, library files and compiler are hash-pinned. The receipt explicitly says `derivative_proved: false` and `full_metric_regularity_proved: false`.

The full regularity node is now ++. Its earlier component receipts retain their historical false derivative flags and are archived under completed progress. The new full receipt resolves the same attempt; unit-circle flow is now ready but not automatically proved. The planner's original numerical forecast is retained as a **pre-attempt** forecast, not relabeled as a new remaining-work estimate. This resumption is the same unfinished attempt, not a new independent trial.

```text
python research/nima/checkers/check_phase_metric_continuity.py --timeout 2400
python research/nima/checkers/check_phase_derivative_reduction.py --timeout 2400
python research/nima/checkers/check_completion_order_limits.py --timeout 2400
python research/nima/checkers/check_rational_phase_derivative_bound.py --timeout 2400
python research/nima/checkers/check_completion_relative_bound.py --timeout 2400
python research/nima/checkers/check_constructed_phase_derivative.py --timeout 2400
python research/nima/checkers/test_completion_refinement_net.py
python research/nima/checkers/check_completion_refinement_planning.py
python research/nima/checkers/check_completion_refinement_net.py
```
