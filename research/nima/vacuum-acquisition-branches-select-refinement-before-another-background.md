# Vacuum acquisition branches select refinement before another background

## Result

With the order-12 prior and previous feature readings unchanged, the next A=3 vacuum reading now has an outcome-dependent certificate procedure.

A finite scan of 29 possible centers, from -0.014 to 0.014 with radius 0.001, gives:

- 19 task-certified outcomes;
- 4 outcomes with explicit opposite-sign feasible sources;
- 4 outcomes incompatible with the prior;
- 2 unresolved outcomes.

No task-contradicted outcome was certified in this scan. Infeasible data are not reported as evidence that the task is false. The scan is not an exhaustive partition of all possible real intervals.

For the ambiguous returned interval [-0.011,-0.009], acquiring the A=4 vacuum coordinate alone cannot resolve the exhibited ambiguity. Two compatible sources already disagree using only A=2 and A=3, and both have b_4=0.

A conditional refinement of the existing A=2 and A=3 readings instead certifies positivity without strengthening any prior.

## 1. Fixed assumptions and target

Retain the labelled source family, exact raw feature intervals and physical calibration of `one-next-background-vacuum-reading-resolves-the-order-twelve-task.md`. The prior remains

`sum_A (A/2)^12 p(x_A)<=40`.

The old A=2 vacuum interval is [0.009,0.011]. The task is strict positivity of both aggregate vacuum and normalized residual readouts. The residual lower bound remains greater than 0.03344470, because the new vacuum constraints only narrow the old feasible set. They do not acquire feature data at A=3.

Consequently only the vacuum sign requires outcome-dependent analysis here. The classification concerns scalar task values, not intrinsic boundary construction or a norm on extension classes.

## 2. Classify a returned interval without confusing emptiness and sign

Let [l,h] be a returned A=3 interval, including all errors. Use certified local bounds a_0>=a_min and b_2 in [b_min,b_max]. Put

`B=40-32 a_min-8 b_min`,

`q_3=(3/2)^12`, `q_4=2^12`.

Intersect [l,h] with [-B/(8q_3),B/(8q_3)]. An empty intersection proves incompatibility with the prior. It does not establish a negative task value.

For a nonempty clipped interval [l',h'], universal bounds are

`U >= b_min+l'-(B-8q_3|l'|)/(8q_4)`,

`U <= b_max+h'+(B-8q_3|h'|)/(8q_4)`.

Both endpoint selections follow from monotonicity: q_3/q_4<1. The upper bound conservatively uses b_max for its direct contribution and b_min for the budget charge. Correlation is not assumed away as a claim of exact attainability.

A strictly positive lower bound certifies the task ONLY when a compatible finite source is also verified. A strictly negative upper bound likewise contradicts the task only with verified feasibility. Otherwise the procedure seeks two compatible finite sources of opposite vacuum sign. Without either kind of certificate it returns unresolved.

The witness search uses rational local coefficients whose predictions fit every value in the actual calibration enclosures, and an optional budget-bounded forgotten source at A=4. Failure of this bounded witness search is not a proof that no opposing source exists.

## 3. An ambiguous branch that another background cannot settle

Suppose the new A=3 interval is [-0.011,-0.009]. The checker verifies two sources with the SAME b_3=-0.01 and b_4=0, but

`b_2=0.0091` versus `b_2=0.0109`.

They use the same certified lower-cost local retained-feature coefficient and fit the old raw feature data. Both satisfy the unchanged moment budget. Their vacuum sums are -0.0009 and +0.0009.

Thus even an exact new b_4=0 reading would retain this pair. The obstruction is uncertainty in already acquired coordinates, not merely an unseen farther tail. This rules out b_4 alone as a resolving measurement for this branch; it is not a claim that all possible additional channels are unhelpful.

## 4. A conditional resolving refinement

If justified refined acquisitions return

`b_2 in [0.00999,0.01001]`,

`b_3 in [-0.00961,-0.00959]`,

both intervals refine the old data. The procedure verifies a compatible finite source and proves

`U in [0.00032925,0.00047139]`.

The residual positivity guarantee is unchanged. Both tasks are therefore certified under the same source prior.

This is conditional on what the refinement returns. It does not predict an outcome, claim physical acquisition, or prove an optimal measurement-cost policy. Other returned intervals are evaluated by the same feasibility/sign procedure.

## 5. What has become adaptive

A near-zero A=3 outcome settles the task immediately. The ambiguous negative-centered outcome instead calls for refinement of existing vacuum readings: blindly advancing to another background does not remove its witnessed ambiguity.

The procedure now selects between these responses using source witnesses and universal bounds, rather than only the width of an interval. It retains unresolved and infeasible branches explicitly. Algebraic frame coherence and relative completeness remain separate inputs, not substitutes for the acquired constraints.

## Verification

`uv run --with python-flint --with sympy python research/nima/checkers/check_vacuum_outcome_branches.py`

Artifact: `research/nima/results/vacuum-outcome-branches.json`.

The run freshly verifies the baseline calibration and residual guarantee, evaluates the finite outcome grid, records feasible and opposing-source witnesses, and certifies the conditional refinement. All examples are synthetic acquisition intervals on the declared actual source family.
