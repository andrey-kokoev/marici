# The next task acquisition should resolve the bin-response calibration gate

## Decision

For the frozen middle case, do NOT spend more computation solely on theta quadrature with the current C_bin interval, or expect a repeated unknown-source reading to restore the current calibration-uniform witness.

The productive target is the response calibration of the SAME deployed bin filter:

1. Tighten its bulk-response pairing C_bin computationally; or
2. If a controlled reference is available, acquire the same positive bounded joint-bin aggregate on the known unit source v_(2,0), with TOTAL absolute error at most 10^-197.

The second option has a complete conditional outcome partition, including an explicit unresolved band. It is not a promise of resolution for every returned value. No operational cost optimum is asserted without computation, preparation and acquisition costs.

The source prior, old raw observations, receiver gamma=1, 76-bin/horizon-64 filters, and original source-functional bounds remain unchanged. This result concerns the already-frozen middle case in BOTH modes, not a newly selected success fixture.

## 1. The task gate is exactly a scalar calibration threshold

The frozen middle input has crossed reading zero and vacuum reading 1/100, both exact. Its positive reading is

    d in [d_lo,d_hi],
    d_lo=(499/400) theta,
    d_hi=2 f_original,

where theta is the exact rational midpoint of the ORIGINAL positive-gain enclosure. The prior remains

    sum_(integer A>=2) A^16 [32 sum_j |a_(A,j)|+8|b_A|] <=40*2^16.

After paying for b_2=1/100, the largest affordable positive coefficient is

    a_*=499/400.

Let E be the actual positive forward gain. The old source problem is feasible exactly when E>=theta:

- Necessity: a_(2,0)>=d_lo/E, while the budget requires a_(2,0)<=a_*.
- Sufficiency: choose a_(2,0)=499/400, b_2=1/100 and every other coefficient zero. This genuine finite rational source spends exactly M. When E>=theta its positive reading is at least d_lo, and E<=f_original ensures it is below d_hi. The coefficients are explicit, but their compatibility with the old raw interval cannot yet be certified while the gain enclosure crosses theta. No midpoint is substituted for E.

All compatible sources already have strictly positive aggregate vacuum and normalized residual bounds. Thus there is no established opposite-sign source ambiguity in this case. The missing task certificate is nonemptiness, controlled by which side of theta the ACTUAL calibration lies on.

The two modes share E. Their different crossed calibrations do not affect this zero-crossed-reading case.

## 2. Fresh computation locates an enclosure-method floor

The checker increases only the two positive-window integrations from 32768 to 262144 complete cells, retaining 192-bit arithmetic and scaled cutoff 32. It recomputes the fixed-filter calibration and requires exact equality of the rational filter coefficients with the deployed manifest. No new detector is deployed.

The resulting gain enclosure, approximately,

    [6.274833783808, 6.286061206617] * 10^-193,

still straddles

    theta approximately 6.280468234235 * 10^-193.

These displayed scientific values are approximate; all comparisons use saved exact rational endpoints. In units of 2^16, the necessary source cost is about 39.96448, while the cheapest calibration-uniform inner-box witness costs about 40.03585. The budget is 40. Both modes remain unresolved, with conditional task positivity intact.

This is not merely a failed refinement experiment. Write

    E(C)=2 Xi_A Xi_B (C+alpha)(C+beta),
    alpha=h_bin(mu_A-L), beta=h_bin(mu_B-L).

All factors needed for monotonicity in positive C are certified positive. Holding C at the lower endpoint of its existing interval, the checker proves

    upper(E(C_lower)) < theta.

Holding it at the upper endpoint, it proves

    lower(E(C_upper)) > theta.

These inequalities hold uniformly over the entire remaining window, weak-response and L enclosures. Hence even making those quantities exact cannot remove the threshold crossing from THIS Cartesian evaluation while the same C interval is retained.

This is a floor of the enclosure method, NOT irreducible physical uncertainty. The C endpoints are not asserted to be independently realizable physical calibrations. Better response computation or use of physical correlations can escape this limitation.

## 3. The next computational precision target

The critical response value is

    C_* = -(alpha+beta)/2
          + sqrt((alpha-beta)^2/4 + theta/(2 Xi_A Xi_B)).

Fresh outward bounds are

    C_bin in [1.97126580, 1.97309692],
    C_*   in [1.97200559, 1.97236527].

Thus sufficient computational stopping conditions are:

- a new certified C lower bound at least the certified C_* upper bound: E>=theta;
- a new certified C upper bound below the certified C_* lower bound: E<theta.

The appropriate computation is a tighter pairing of the FIXED hats with the actual bulk response, or a sharper certified projection-residual estimate. Increasing theta cells alone with the current response bound cannot meet this target. Numerical midpoints of either C interval do not decide the task.

## 4. Why repeating the unknown-source reading does not fix this certificate

An additional positive reading [s-r,s+r] on the unknown source intersects the existing raw interval. Its joint lower endpoint cannot decrease below d_lo.

At the current gain lower bound e<theta, even the old data require

    a_(2,0)>=d_lo/e > a_*.

Consequently no source fits the old data and prior uniformly over the current calibration box. Merely adding another source constraint cannot make that robust feasible set nonempty.

For a repeated positive reading the full decision is:

- empty intersection with the old raw interval: incompatible readings;
- nonempty intersection whose lower endpoint exceeds a_* times the gain upper bound: source-prior incompatible;
- otherwise: unresolved by the present certificate method.

There is no new robust task-certified branch. This is a statement about fixed calibration and this witness method, not an information-theoretic prohibition on self-calibrating sensors, additional physical correlations, or other existence proofs.

## 5. A controlled reference has different informational value

Read the SAME positive channel on the known unit source v_(2,0), with all other coefficients zero. Its response is E itself. The reference source is finite and its moment cost 32*2^16 fits the stated budget.

This requires controlled source preparation, not just another reading of the unknown source. It is one additional aggregate channel record under the existing bounded joint-bin acquisition contract, NOT one primitive hat integral or point sample. Products of unknown marginal readings do not replace the joint measurement.

Let the certified current gain interval be [e,f]. For a reference center s and a valid total absolute error radius r, the updated enclosure is

    J=[e,f] intersect [s-r,s+r].

The complete real-center partition is:

| Returned center | Conclusion |
| --- | --- |
| s<e-r or s>f+r | Incompatible with the certified calibration/error model |
| e-r<=s<theta-r | Source data and prior incompatible |
| theta-r<=s<theta+r | Unresolved |
| theta+r<=s<=f+r | Task certified, conditional on the valid reference contract |

At the lower decision boundary theta-r, the necessary budget cost can equal 40; equality is NOT an infeasibility certificate. At theta+r the robust witness fits the budget at equality, so the task-certified branch is closed on that side.

For the task-certified branch, choose the rational coefficient d_lo/lower(J), keep b_2=1/100, and set all other coefficients to zero. Its cost is at most M and its predicted readings fit for every gain in J. Shrinking the gain interval preserves the already-positive universal task bounds. Thus this branch supplies both a witness and positivity for EVERY compatible source, not just positivity of that witness.

These are hypothetical future outcomes. [e-r,f+r] is only an OUTER range of centers; no assertion is made that every center is realizable by the fixed physical calibration. No controlled reference has been acquired by this checker.

## 6. Explicit precision and worst-case-noise guarantees

The proposed total radius is

    r=10^-197.

The unresolved CENTER band has width 2*10^-197. For every measurement error of magnitude at most r:

- if actual E<theta-2r, the reference proves source-prior incompatibility;
- if actual E>=theta+2r, the reference gives the nonvacuous positive-task certificate.

The checker verifies both separated regions lie inside the current gain enclosure. It does not assert which contains the actual E.

At actual E=theta, a valid returned center s=theta remains unresolved for every positive r. Therefore no positive finite error radius guarantees resolution uniformly at this boundary. The plan does not assign probabilities to the branches.

The raw positive test has certified response-norm upper bound one. A sufficient external contract is

    acquisition response error + visible reference-preparation response error <=10^-197.

Rounding/evaluation error must also be charged to that total. If the reference has only a known coefficient error |a_ref-1|<=delta and no other visible contamination, its contribution is at most f*delta. These are accuracy requirements, not demonstrated instrument capabilities.

## 7. Reproduction

Fresh calibration-floor proof and decision artifact:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_source_task_acquisition_plan.py

Fast exact-rational replay, including strict branch boundaries, hypothetical witnesses, worst-case noise endpoints and repeated-reading obstruction:

    uv run python research/grothendieck/checkers/check_source_task_acquisition_plan.py

Classify a HYPOTHETICAL reference return, without modifying the source data or calibration files:

    uv run python research/grothendieck/checkers/plan_source_task_acquisition.py private 6.2807e-193

The default radius is 10^-197; an optional final argument supplies another exact rational radius. This is a planning tool, not a data-acquisition tool.

Artifacts:

- `results/three-channel-source-task-calibration-planning.json`;
- `results/source-task-acquisition-plan.json`.

The fresh run checks hashes of the original observations, prior calibration, deployed filters and prior refinement results. Earlier conclusive cases remain conclusive. No source-module lift, intrinsic relative boundary, or derived pushout conclusion is inferred from this decision analysis.
