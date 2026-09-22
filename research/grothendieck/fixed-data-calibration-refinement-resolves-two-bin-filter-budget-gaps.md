# Fixed-data calibration refinement resolves two bin-filter budget gaps

## Result

Follow-up: `the-next-task-acquisition-should-resolve-the-bin-response-calibration-gate.md` diagnoses the remaining middle case, proves a fixed-response enclosure floor, and gives a continuous controlled-reference outcome partition with explicit precision requirements.

For BOTH gamma=1 acquisition modes, a fixed-data regression now gives:

| Frozen synthetic case | Baseline | Refined |
| --- | --- | --- |
| Lower threshold | UNRESOLVED | CERTIFIED_FEASIBLE |
| Upper threshold | UNRESOLVED | CERTIFIED_INFEASIBLE |
| Middle threshold | UNRESOLVED | UNRESOLVED |

The positive-gain enclosure becomes about 2.836 times narrower. The raw intervals, order-16 prior, deployed rational bin filters, acquisition modes and original source-functional bounds are unchanged. Both modes share the positive channel; this result does not compare their different crossed-channel acquisition costs.

The earlier explicit feasible sources and joint infeasibility certificates remain valid. Their positive task conclusions survive, and the refined aggregate outer intervals are contained in the earlier ones.

This implements the strategy from Nima's `../nima/refined-calibration-resolves-both-open-vacuum-outcomes-as-infeasible.md`, NOT its gamma=2/order-12 constants or its A=3 acquisition outcomes.

## 1. Try an actual robust witness before refining

For a real reading interval [l,u] and positive calibration interval [e,f], the necessary coefficient box is the hull of the four endpoint quotients. Its minimum absolute value gives a necessary source cost, not an existence proof.

The sufficient, calibration-uniform coefficient interval is instead

    [l/e,u/e] intersect [l/f,u/f].

Every coefficient in this inner interval fits the raw reading for EVERY calibration value in [e,f]. The new automatic search selects the closest point to zero in each nonempty inner interval and checks the combined exact weighted source cost. Other source coefficients and backgrounds are explicitly zero. This supplies a genuine finite rational source witness whenever it fits the prior.

An empty inner interval or excessive robust-witness cost returns no feasibility certificate; neither is called infeasibility. Correlated physical calibration parameters are not treated as independently realizable.

`three_channel_source_task.py` enables this search with `auto_witness: true`. The default remains false for compatibility with the original supplied-witness interface. A failed supplied witness may be replaced by a successful automatic one; the output distinguishes both checks and records the accepted witness's origin.

## 2. Freeze the experiment before improving calibration knowledge

The regression saves exact rational inputs BEFORE the refined computation and reuses that file on subsequent runs. Its baseline-calibration hash must match; changed inputs are not silently regenerated.

Let [e,f] be the baseline positive-gain interval. Keep

    M=40*2^16,
    crossed reading=0 exactly,
    vacuum reading=1/100 exactly.

After paying the vacuum cost, the largest affordable positive coefficient is

    a_*=(40-8/100)/32=499/400.

For theta equal to e+(f-e)/4, e+(f-e)/2, or e+3(f-e)/4, freeze the positive raw interval

    [a_* theta, 2f].

All three cases pass the necessary baseline cost test but fail the baseline robust-witness budget test. These are explicitly synthetic boundary fixtures, not measurements or evidence that a physical acquisition system reaches such precision.

## 3. Refine the SAME deployed filters

Only the two positive-channel theta-window integrations change, from 8192 to 32768 complete cells per scaled window. They remain at 192-bit arithmetic with cutoff 32 and the same completed-theta tail bounds. The windows are [2,4] and [12,60].

For the existing bin-filter response constants C_bin and h_bin, the forward gain is enclosed afresh as

    E_0=n_bin([2,4]) n_bin([12,60]),
    n_bin(F)=sqrt(2) Xi_F [C_bin+h_bin(mu_F-L)].

The checker recomputes the filter calibration and requires exact equality of every proposed rational filter coefficient with the deployed manifest. It does NOT deploy a newly fitted waveform. The 76-bin, horizon-64 integral acquisition remains unchanged; no point samples replace those integrals.

The fresh gain interval must lie strictly inside the old one by exact endpoint comparisons. No midpoint is substituted for the gain. Original source-functional and tail bounds are retained, as are both crossed-channel gain intervals.

A separate refinement bundle binds the parent calibration and unchanged protocol by hashes. Loading checks exact nesting and rejects stale parents or widened gain intervals. These freshness checks are not an independent proof of the analytical enclosure: that proof comes from the fresh owning Arb computation.

## 4. The two resolved certificates

For the lower-threshold case, the new robust source has normalized moment cost

    cost/2^16 <=39.96800244 <40.

Its coefficients and their calibration-uniform raw predictions are saved exactly.

For the upper-threshold case, every compatible source would have

    cost/2^16 >40.03212180 >40.

The necessary positive-feature cost alone is below 40, and the vacuum cost alone is 0.08; their SUM exceeds 40. Crossed coefficients and unobserved sources cannot reduce these nonnegative, disjoint-support costs.

The upper-threshold case had positive conditional aggregate lower bounds even before refinement. It did NOT have a nonvacuous positive-task certificate. Its subsequent infeasibility illustrates why feasibility cannot be skipped.

The middle case remains unresolved after this one refinement. This is not a demonstrated source ambiguity, nor a claim that further computation must resolve it. The procedure remains sufficient-witness/necessary-contradiction certification, not a complete optimizer.

## 5. Reproduction and use

Fresh calibration refinement and fixed-data regression:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/refine_three_channel_source_task.py

Fast exact-rational replay, including witness, nesting, early-exit and rejection tests:

    uv run python research/grothendieck/checkers/check_fixed_data_calibration_refinement.py
    uv run python research/grothendieck/checkers/check_three_channel_source_task.py

Automatic witness search followed, ONLY if unresolved, by the stored refinement:

    uv run python research/grothendieck/checkers/certify_source_task_adaptively.py task.json

The adaptive entrypoint enables automatic witness search, records each attempted certificate, and never changes the input file. If the first attempt is conclusive, it does not load a refinement. If no refined bundle exists, it returns unresolved with an explicit computation instruction rather than silently launching an expensive build. It performs at most one stored refinement; a remaining unresolved result is retained honestly.

To use a certified refinement directly with the original interface:

    uv run python research/grothendieck/checkers/three_channel_source_task.py task.json research/grothendieck/results/three-channel-source-task-calibration-refined.json

Set `auto_witness` to true in that input to enable the new witness search.

Artifacts:

- `results/calibration-refinement-frozen-inputs.json`;
- `results/three-channel-source-task-calibration-refined.json`;
- `results/fixed-data-calibration-refinement.json`.

No intrinsic boundary, module lift or adjacent extension-class conclusion follows from these numerical certificates. The recent lower-filtration nullhomotopy result and this source-budget workflow answer different questions.
