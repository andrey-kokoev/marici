# Auxiliary projections tighten the fixed bin response without changing the detector

## Result

A fresh 136-dimensional auxiliary projection sharpens the response calibration of the SAME deployed rational bin filters:

    C_bin in [1.97196784, 1.97239638]

with endpoints rounded outward. Its exact enclosure is about 4.273 times narrower than the previous C_bin enclosure. The positive forward-gain enclosure is about 2.780 times narrower in both acquisition modes.

The frozen middle task remains UNRESOLVED. In units of 2^16, its necessary source cost is approximately 39.98727645 and its cheapest calibration-uniform inner-box witness costs approximately 40.01294680. The budget remains 40. Neither rounded midpoints nor the narrower width decide which side of the physical feasibility threshold the actual gain occupies.

All previously conclusive task cases retain their status and positive-task guarantees. Aggregate outer bounds are nested. Ten extended portable identity-refinement chains cover both modes and the five existing cases per mode.

No detector, source, prior or observation was changed. No new reference was acquired.

## 1. Replace a coarse pairing bound, not the hats

Let g be either actual damped bulk response in L2(0,infinity), and let b be the corresponding DEPLOYED normalized piecewise-linear hat filter, extended by zero after time 64.

The older calibration compared b with its small exponential design approximation and used a residual Cauchy--Schwarz bound. The new computation reads b directly from the immutable deployed manifest. It introduces an auxiliary space

    V=span{exp(-rho_j t)},
    rho_j=2^(j/8), -40<=j<=96, j!=8.

These 136 distinct positive rates have the positive-definite Cauchy Gram matrix

    G_ij=1/(rho_i+rho_j).

Rate 2 is omitted to avoid a removable divided-difference singularity in the owning response-moment formula. The auxiliary space is used ONLY in the proof. Its coefficients are not new filter coefficients and are never deployed.

## 2. Exact moment identities and a certified remainder

Put

    m_i=<g,exp(-rho_i t)>,
    h_i=<b,exp(-rho_i t)>.

The m_i use the existing all-prime Euler-line response identities, with spectral parameter s=7/2 and receiver line beta=3/2. They are evaluated by Acb zeta/logarithmic-derivative enclosures. The h_i and ||b||^2 are elementary integrals of the fixed rational hats. No point samples are substituted for these integrals.

For the orthogonal projection P onto V,

    <Pg,Pb>=m^T G^(-1) h,
    ||Pg||^2=m^T G^(-1) m,
    ||Pb||^2=h^T G^(-1) h.

Therefore

    <g,b>=m^T G^(-1) h + <g-Pg,b-Pb>.

Given the freshly certified whole-response squared-norm upper bound B_g, the remainder satisfies

    |<g-Pg,b-Pb>|
      <=sqrt[(B_g-m^T G^(-1)m)(||b||^2-h^T G^(-1)h)].

The computation uses outward upper bounds on the two nonnegative factors. It requires finite certified matrix solves and strictly positive residual enclosures; it does not clip an inconclusive negative residual to zero or accept an approximate linear solve.

The Cauchy matrices are ill-conditioned. The calculation uses 3072-bit Arb/Acb arithmetic. High precision here supports the auxiliary proof, not a claim about physical acquisition precision.

For the two bulk components, the certified pairing-error radii are approximately 0.00011421 and 0.00010006. The unchanged weak and endpoint contributions complete the new C_bin enclosure.

## 3. Replay the same window calibration and task

The positive gain is recomputed as

    E_0=2 Xi_A Xi_B
        [C_bin+h_bin(mu_A-L)] [C_bin+h_bin(mu_B-L)],

for the unchanged windows [2,4] and [12,60]. The theta computation retains the parent's 262144 complete cells, 192-bit arithmetic and cutoff 32. Thus this step isolates the response-pairing improvement rather than combining it with a new quadrature rule or regenerated data.

Exact endpoint comparisons prove strict inclusion in the old C_bin and positive-gain intervals. Both crossed gains, vacuum gain, original source-functional enclosures and tail multiplier are retained. Only positive-gain knowledge is sharpened.

The source task still uses the original order-16 budget, integer backgrounds and disjoint path costs. The deployed 76-bin/horizon-64 filters and rational observer coefficients remain byte-for-byte unchanged. The new auxiliary exponentials do not alter the acquisition geometry or source-kernel support.

For each mode, the saved outcomes are:

| Existing case | Result after refinement |
| --- | --- |
| Lower threshold | CERTIFIED_FEASIBLE |
| Upper threshold | CERTIFIED_INFEASIBLE |
| Middle threshold | UNRESOLVED |
| Earlier feasible fixture | CERTIFIED_FEASIBLE |
| Earlier joint contradiction | CERTIFIED_INFEASIBLE |

The remaining gap is substantially smaller, but conditional positive task bounds are not promoted to nonvacuous conclusions at the middle node.

## 4. Portable transition evidence

The new calibration bundle cites the previous planning calibration as its parent and records the fixed filter digest, quadrature settings and auxiliary projection parameters. A standalone verifier checks the extension

    original -> 32768-cell -> 262144-cell -> fixed-hat pairing refinement.

The last edge has identity source, observation and target coordinates; all old data and the prior are equal and the gain enclosure is nested. Every endpoint's exact source-budget and task certificate is checked independently. Isolated verification needs only the verifier and one bundle.

These numerical transition checks do not independently establish the analytic projection identities or the correctness of the new physical calibration enclosure. Those remain obligations of the fresh owning Arb computation. Digests bind evidence, not authenticate a physical identification.

This is also consistent with Nima's finite mixed-history verifier: it is one supported identity-calibration step, not a gain change, a vacuum-tail split or structural transport. The narrower enclosure still concerns ONE physical detector.

## 5. Reproduction

Fresh analytical proof, gain refinement and frozen-task replay:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_fixed_bin_response_refinement.py

Exact-rational replay and ten portable chain exports:

    uv run python research/grothendieck/checkers/check_fixed_bin_response_refinement.py

If the preceding portable chains are absent, first run:

    uv run python research/grothendieck/checkers/check_portable_source_task_transitions.py

Independent verification of the still-unresolved chain:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-middle_threshold-fixed-hat.json

Artifacts:

- `results/three-channel-source-task-calibration-fixed-hat.json`;
- `results/fixed-hat-response-refinement.json`;
- `results/fixed-hat-response-refinement-tests.json`;
- `results/portable-source-task-transitions/*-fixed-hat.json`.

The sharper enclosure is a genuine computational improvement, not a new successful acquisition or a resolved middle task. Further work must still bound the actual fixed-filter response and the remaining window uncertainty tightly enough to separate the gain from the frozen threshold.
