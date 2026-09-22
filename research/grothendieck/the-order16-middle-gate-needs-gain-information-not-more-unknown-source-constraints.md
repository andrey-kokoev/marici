# The order-16 middle gate needs gain information, not more unknown-source constraints

## Decision

At the latest bulk-norm calibration, acquiring chi_3 and chi_4 can refute the declared source prior or tighten conditional task bounds. It cannot produce a calibration-uniform source witness for the frozen middle fixture. This remains true for exact zero returns.

A controlled positive-gain reference CAN produce a nonvacuous task certificate, conditional on a valid total-error contract and a favorable returned interval. It is therefore the relevant acquisition of these two options if the goal is resolving this calibration gate. This is not a hardware-feasibility or cost-optimality claim. Further analytical gain refinement remains an alternative.

The result holds in both private and reuse modes. Observations, filters, source family, and order-16 prior are unchanged. No reference or vacuum reading was acquired.

## 1. Complete vacuum outcome map for the declared certificate method

Write the frozen positive raw interval as [d_l,d_u], its calibrated gain interval as [g_l,g_u], and set

    W=32*2^16,
    f=8*2^16/100,
    M=40*2^16.

The crossed raw reading is exactly zero and b_2=1/100. For returned unit-vacuum intervals I_3,I_4, put

    m=8*3^16 min_(x in I_3)|x| + 8*4^16 min_(x in I_4)|x|,
    C=M-f-W*d_l/g_u.

The exact map is:

- m>C: SOURCE_PRIOR_INCOMPATIBLE;
- m<=C: UNRESOLVED under the declared outer-cost/calibration-uniform-witness method.

For this fixture, approximately

    C = 714.880222624709,
    f+W*d_l/g_l-M = 729.368703727709 > 0.

The first quantity is the remaining necessary-cost allowance, not available physical budget known to be attained. The second is the pre-existing robust-witness deficit. Acquiring additional source constraints cannot remove it: a source fitting the old reading at g_l already needs more than M, even before paying for b_3 or b_4.

In particular, intervals containing zero have m=0 and remain unresolved. There is no vacuum-only feasible branch here. This is NOT proof of physical ambiguity or an impossibility of stronger analysis using further gain information or physical correlations.

For exact readings, the boundary is the weighted diamond

    8*3^16 |b_3| + 8*4^16 |b_4| = C.

Its axis intercepts are approximately 2.07588466e-6 and 2.08057528e-8. Equality is unresolved, not an infeasibility certificate. Signs cannot cancel the source cost.

The artifact's universal task bounds keep unmeasured retained features at backgrounds 3 and 4. Acquiring their vacuum coordinates does not move the residual tail start to 5.

### Worst-case vacuum errors

For true coefficients b_A and valid absolute error radii rho_A, returned centers satisfy |s_A-b_A|<=rho_A and the reading interval is [s_A-rho_A,s_A+rho_A]. The returned necessary added cost ranges exactly over endpoints

    m_min=sum_(A=3,4) 8*A^16 max(|b_A|-2*rho_A,0),
    m_max=sum_(A=3,4) 8*A^16 |b_A|.

This follows by choosing each center closest to, or farthest from, zero within its allowed error interval. Hence:

- m_min>C: every allowed error yields a prior contradiction;
- m_max<=C: every allowed error leaves this method unresolved;
- otherwise: the outcome depends on the error.

The portable query interface checks these envelopes. Tested illustrative radii are rho_3=1e-7 and rho_4=1e-9; their attainability is not asserted.

## 2. Complete controlled-reference outcome map

Prepare the known unit source v_(2,0), all other coefficients zero, and read the SAME bounded positive aggregate. This measures the gain, not another unknown-source coefficient. Its preparation is a separate trial, not an additional charge against the unknown source's budget.

Require a valid total absolute error radius

    epsilon=1e-197.

All visible preparation error, acquisition error, and any transfer/drift error must be covered. The owning protocol declares this aggregate's test norm at most one. A response-norm error bound can therefore supply the preparation component. The policy does not establish that such a contract is experimentally achievable.

For returned center s, intersect [s-epsilon,s+epsilon] with [g_l,g_u]. An empty intersection is CALIBRATION_INCOMPATIBLE, distinct from a source-prior contradiction.

Define the exact threshold

    h=d_l/((M-f)/W).

On compatible returns the complete map is

    s+epsilon<h       : SOURCE_PRIOR_INCOMPATIBLE,
    s-epsilon>=h      : TASK_CERTIFIED_CONDITIONAL_ON_VALID_REFERENCE,
    otherwise         : UNRESOLVED.

Approximately,

    [g_l,g_u] = [6.278717792640549,6.282184851714008] * 1e-193,
    h         = 6.280468234234755 * 1e-193.

These displayed numbers are explanatory approximations; certificates use exact rational endpoints.

### Why the task branch has an actual witness

For a nonempty conditioned gain interval [a,z] with a>=h, take

    (d_l/a) v_(2,0) + (1/100) k_2,

all other coefficients zero. Its cost is at most M. The checked inequality

    d_l/g_l <= d_u/g_u

makes the raw upper endpoint nonbinding throughout every reference subinterval, so this SAME source fits every gain in [a,z]. The verifier checks endpoint predictions, budget and task positivity with the existing standalone source-task verifier.

Both task lower bounds are positive on the entire high-side gain interval [h,g_u]. Restricting that interval preserves their validity. Thus the conclusion is nonvacuous, not positivity over an empty compatible set.

### Worst-case reference errors

If the true gain is g, the center can itself differ from g by epsilon. Therefore the guarantees require TWO radii:

    g<h-2*epsilon  => every allowed error certifies prior incompatibility,
    g>=h+2*epsilon => every allowed error certifies the positive task.

The corresponding approximate thresholds are 6.280268234234755e-193 and 6.280668234234755e-193. The lower inequality is strict; the upper is inclusive. A one-radius guarantee is unsound.

No positive finite error radius guarantees resolution arbitrarily close to h. No probability for a favorable reference return is inferred from a calibration midpoint.

## 3. Portable policy, queries and validation

Reproduce both policies and independent outcome replays:

    uv run python research/grothendieck/checkers/check_order16_acquisition_policy.py

Verify a policy:

    python research/grothendieck/certificates/verify_order16_acquisition_policy.py research/grothendieck/results/order16-acquisition-policy/private.json

Add a query JSON path as the final argument to classify a hypothetical return. Examples:

    {"kind":"reference","center":"6.2807e-193"}

    {"kind":"vacuum","readings":{"3":["0","0"],"4":["0","0"]}}

    {"kind":"vacuum_error_envelope","true_values":{"3":"0","4":"0"},"radii":{"3":"1e-7","4":"1e-9"}}

The reference radius is pinned in the policy, not silently overridden by a query. Vacuum interval queries accept general rational intervals; error-envelope queries explicitly describe hypothetical true values and bounded errors.

Portable execution needs only the policy, this verifier, and its siblings `verify_order16_vacuum_bridge.py` and `verify_source_task_transition.py`. The new-row source binding is checked against the embedded structural artifact. The old support identification, analytical enclosures, source family, prior and acquisition-error contracts remain explicit external premises.

Artifacts:

- `results/order16-acquisition-policy/private.json` and `reuse.json`;
- corresponding `*-examples.json` files;
- `results/order16-acquisition-policy-tests.json`.

Validation includes 66 independent outcome replays against the existing source-task engine, twelve worst-case vacuum profiles, strict boundary and signed-cost cases, eleven rejected corruptions, and isolated standard-library verification. Finite tests supplement the all-outcome inequalities above; they are not their proof.
