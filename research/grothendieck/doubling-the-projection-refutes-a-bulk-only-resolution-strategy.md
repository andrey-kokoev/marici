# Doubling the projection refutes a bulk-only resolution strategy

## Conjecture, fixed before the computation

**Doubling the proof-only exponential projection from 136 to 272 dimensions will resolve the frozen middle task, without changing the detector, data, prior or theta quadrature.**

This conjecture failed in both private and reuse modes. The failed outcome is preserved, rather than reclassified as success because the numerical bounds improved.

A stronger diagnostic succeeded: with the current independent theta-mass intervals, even exact knowledge of every remaining gain factor within its new enclosure cannot resolve the middle threshold by Cartesian interval arithmetic. The obstruction is to this enclosure method, not a claim of physical ambiguity.

## 1. What was changed and what was protected

The auxiliary rates are now

    2^(j/16), -80<=j<=192, j!=16,

giving 272 distinct positive rates. They include the previous 136-rate space. The Gram solve uses 6144-bit Arb arithmetic.

The deployed rational hats, source observations, original task, order-16 prior, old calibration files and certified bulk norm upper bounds are unchanged. Theta quadrature remains 262144 whole cells at 192 bits and scaled cutoff 32. No new observation or reference was acquired.

For the fixed hat b and response g, the argument remains

    <g,b> = <Pg,Pb> + <g-Pg,b-Pb>,
    |remainder| <= sqrt((N-||Pg||^2) * ||b-Pb||^2),

where N is the existing certified squared-norm upper bound. The positive-definite exponential Gram matrix is G_ij=1/(r_i+r_j). Exact analytic Laplace moments and rigorous interval linear algebra enclose the projection quantities. Enlarging this proof space is not redeploying the filter.

The owning completed-theta window functions are reused through AST extraction of only their definitions, avoiding the legacy script's deployment-writing side effects. The same finite Mangoldt sum and analytical remainder produce L. Parent gain enclosures are replayed as a consistency check.

## 2. Numerical result

Approximate new bounds are

    C_bin in [1.9721380562444015, 1.9722264454352658],
    positive gain in [6.279304290069520, 6.281599812559705] * 1e-193.

The C_bin width improves by about 3.58647 times. Exact rational endpoints, not these displayed approximations, control all decisions.

The frozen threshold is approximately

    h = 6.280468234234755 * 1e-193.

Both middle cases remain UNRESOLVED. Their normalized costs are approximately

    necessary lower cost: 39.992808741709126,
    robust witness cost: 40.007399649535960,
    budget:              40.

Earlier feasible/infeasible certificates and task-positive conclusions survive. Aggregate bounds nest. Ten extended portable chains record the new calibration refinement.

## 3. Attack the proposed explanation, not just the numerical outcome

Write the gain as

    E(C)=2 X_A X_B (C+H(mu_A-L)) (C+H(mu_B-L)),

where H is the fixed weak-filter pairing. All masses and factors are positive on the certified intervals.

Use subscripts minus/plus for the rational interval endpoints. Define

    E_low_max = 2 X_A,- X_B,-
                (C_+ + H_+(mu_A,+ - L_-))
                (C_+ + H_+(mu_B,+ - L_-)),

    E_high_min = 2 X_A,+ X_B,+
                 (C_- + H_-(mu_A,- - L_+))
                 (C_- + H_-(mu_B,- - L_+)).

These deliberately give the LOW mass corner every favorable remaining factor, and the HIGH mass corner every unfavorable remaining factor. The independent rational verifier proves

    E_low_max < h < E_high_min.

Approximately,

    E_low_max  = 6.279773014945799e-193,
    E_high_min = 6.281131088688573e-193.

The strict margins are about 6.95219e-197 and 6.62854e-197.

Therefore, for EVERY fixed choice of C, H, mu_A, mu_B and L in their declared intervals, the Cartesian mass box still admits one gain below the threshold and another above it. This is stronger than observing that a single outward-rounded gain ball straddles h. It does not depend on sampled agreement or on roundoff inflation alone.

The two mass endpoints need not be simultaneously realizable by the actual completed-theta source. They are countermodels of the independent-box abstraction, not two physically established calibrations. Exploiting proved correlations could invalidate this abstraction-level obstruction without contradicting this result.

## 4. What the failed conjecture tells us to do

Do not spend the next iteration solely on a larger projection or a sharper bulk norm. Even perfect C knowledge inside the new interval leaves this particular mass-box obstruction.

The next concrete target is a justified higher-order enclosure for the completed-theta mass integrals, replacing first-order whole-cell range summation—not merely increasing the number of the same cells. This attacks the demonstrated bottleneck. The centered moments, omitted theta terms and infinite integration tail must still carry rigorous error bounds.

That improvement is not implemented or presumed here. After it, the remaining projection error may again matter; the present result does not promise that theta refinement alone will resolve the actual middle case.

## 5. Reproduction and independent verification

Fresh analytical computation:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/attack_projection_resolution_conjecture.py

Exact floor audit, frozen-task replay, corruption tests and portable export:

    uv run python research/grothendieck/checkers/check_projection_resolution_attack.py

Standalone verification:

    python research/grothendieck/certificates/verify_projection_resolution_attack.py research/grothendieck/results/projection-resolution-refutation-certificate.json

The standalone verifier needs only its sibling `verify_source_task_transition.py` and the certificate. It checks the exact mass-corner obstruction, threshold binding and middle-task certificates. Analytical validity of the supplied projection and theta enclosures remains the owning computation's obligation.

Artifacts:

- `research/grothendieck/results/projection-resolution-conjecture-attack.json`
- `research/grothendieck/results/projection-resolution-conjecture-tests.json`
- `research/grothendieck/results/projection-resolution-refutation-certificate.json`
- `research/grothendieck/results/three-channel-source-task-calibration-projection272.json`
- `research/grothendieck/results/portable-source-task-transitions/*-projection272.json`

All ten chains and the refutation certificate pass isolated execution. Five corruptions are rejected, including a false success claim, a physical-ambiguity claim, a detached threshold and silently erased mass uncertainty. A precision-context serialization mismatch was also caught during exact replay and fixed by preserving the projection endpoints captured at their original precision; the corrected computation was rerun.

The source-retention and control studies supply a useful methodological boundary, not an extra physical premise: keep the failed baseline, retain the relevant evidence and correlations, and do not turn an implementation-dependent result into a universal impossibility claim.
