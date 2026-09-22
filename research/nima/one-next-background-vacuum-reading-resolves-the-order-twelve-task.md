# One next-background vacuum reading resolves the order-twelve task

## Result

Keep the previous baseline raw readings AND the same prior

`sum_A (A/2)^12 p(x_A)<=40`.

If an additional unit-vacuum reading at background A=3 returns a certified interval [-0.001,0.001], then every compatible source satisfies

`aggregate vacuum >0.00767627`,

`aggregate residual / w_seam^2 >0.03344470`.

An explicit finite source is compatible with these data, so the conclusion is not vacuous. No prior is strengthened and no feature reading is refined.

This is conditional on the returned interval; it does not predict a future measurement. The interval must include all acquisition errors. The example is not a report of a physical experiment.

## 1. Hold the experiment assumptions fixed

Use the real labelled source family V_A plus the forgotten line k_A at integer arithmetic backgrounds A>=2, including A=3. At A=2 retain exactly the baseline raw feature intervals with rho_0=1/10 and rho_x=1/100, and the vacuum interval [0.009,0.011]. All actual-theta calibration uncertainty remains included.

The new observable is the existing three-seam vacuum coordinate at background 3, with its complete outer corner [3,90090]. It measures b_3 directly. Its unit scalar observation is not an arithmetic feature port or a division by a tiny window amplitude.

Background/endpoint labels are essential: this is not the A=2 vacuum coordinate reused without its changed outer corner.

## 2. The budget-coupled bound

Let a_min be the certified lower local coefficient bound and b_min=0.009. The unspent normalized budget is at most

`B=40-32 a_min-8 b_min`.

Set q_3=(3/2)^12 and q_4=2^12. Suppose the newly acquired reading bounds |b_3|<=epsilon. If 8q_3 epsilon<=B, the vacuum sum satisfies

`U>=b_min-epsilon-[B-8q_3 epsilon]/(8q_4)`.

To prove this, the remaining unknown vacuum coefficients begin at A>=4. For a fixed b_3 their adverse sum is at most (B-8q_3|b_3|)/(8q_4). The resulting lower-bound expression is increasing in b_3 on both sides of zero, since q_3/q_4<1. Its minimum on [-epsilon,epsilon] occurs at -epsilon.

Unused feature coefficients can only consume budget, so omitting their cost is conservative. The sufficient zero-centered radius threshold is

`epsilon < [b_min-B/(8q_4)]/[1-q_3/q_4]`.

The exact rational threshold is saved in the artifact; its outward decimal enclosure is [0.00892738,0.00892739]. This is a sufficient threshold from the certified outer model, not an assertion of globally optimal acquisition precision.

At epsilon=0.001 the vacuum lower bound is positive as stated.

## 3. Do not pretend the whole next packet has been observed

Only b_3 is newly acquired. The feature coefficients at A=3 remain unobserved, so the previous residual-tail bound still begins at A=3, not A=4.

That independently certified residual lower bound is already positive: 0.03344470 in the normalized residual units. The new observation cannot invalidate it because it only narrows the feasible source set.

The finite positive source v_(2,0)+(1/100)k_2, with every other coefficient zero, fits both old data and the new A=3 interval. Its cost is below the unchanged budget.

## 4. Two controls show why the selected measurement matters

The checker reconstructs the previous negative-vacuum witness: a lower-cost local source at A=2 plus a negative forgotten-product coefficient at A=3 that uses the remaining budget. Its aggregate vacuum lies in [-0.00119643,-0.00119642]. It fits every old raw interval and the same order-twelve prior.

- A new A=3 interval [-0.02,0.02] still contains both this witness and the positive source. It does not settle the task.
- A new A=4 interval [-0.001,0.001] also leaves them both compatible: both have b_4=0. Precision at the wrong background does not remove the exhibited ambiguity.

The sharper A=3 interval excludes the old negative witness AND provides a universal positive bound for all remaining sources. Merely excluding one witness would not suffice without that second argument.

## 5. Relation to the new 270-row module audit

Voevodsky's `../voevodsky/the-270-row-enlargement-preserves-left-relative-completeness-but-breaks-the-old-line-lift.md` establishes IN=L for that enlargement, while NI has codimension one and the old graded-line lift fails. Relative completeness survives; the old lift-based source comparison does not automatically transfer.

No such line lift or adjacent-pushout conclusion is used here. This certificate concerns scalar acquisition, labelled supports and source-budget inequalities. It neither supplies the missing new source comparison nor claims to reconstruct the intrinsic boundary from measured states.

## Verification

`uv run --with python-flint --with sympy python research/nima/checkers/check_next_vacuum_acquisition.py`

Artifact: `research/nima/results/next-vacuum-acquisition.json`.

Fresh checks cover actual calibration intervals, the positive feasible source, the exact budget-saturating negative source, the new universal bound and both nonresolving controls. Exact rational witnesses and raw baseline intervals are retained for reproduction.
