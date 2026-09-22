# Order-16 vacuum acquisitions have a source-bound, order-independent task bridge

## Result

The gamma=1 source-task lane now admits the specified background-3 and background-4 unit-vacuum readings under its UNCHANGED order-16 prior. Both acquisition orders have portable certificates with the same final source-summary restriction and task bounds.

For the existing feasible A=2 fixture, the new conditional synthetic readings are

    b_3 in [0.0004,0.0006],
    b_4 in [0.0000015,0.0000025].

Both modes have explicit genuine-source witnesses. Every compatible source satisfies the final outward bounds

    aggregate vacuum U in [0.00940105,0.01160295],
    aggregate residual per w_seam^2 in [0.05124759,0.06944299].

Before the additions, the corresponding bounds were

    U in [0.00688078,0.01311922],
    residual per w_seam^2 in [0.05064238,0.07004819].

This improves already-positive task bounds; it is not advertised as a transition from ambiguity to positivity. The old A=2 data and calibration are frozen. No physical reading is claimed to have occurred.

Appending the SAME proposed vacuum returns to the existing middle-threshold fixture instead gives a source-budget contradiction: the coarse node is unresolved, and either new reading already makes the refined problem infeasible. This is the effect of additional hypothetical data, not a computational resolution of the old middle data by themselves.

## 1. Pin the actual new source rows

For A=3,4 use precisely the vacuum row with outer corner

    (A,30030 A)

and seams

    A->2A, 6A->30A, 210A->2310A.

It selects the canonical all-forgotten word (2,3,5,7,11,13) and annihilates words with retained marks by feature degree. The portable verifier independently enumerates all 720 forgotten orders and their cut triples to check this selection.

The source coefficient b_A refers to the actual cubic product

    k_A=forgotten(2,3) forgotten(5,7) forgotten(11,13).

Its expansion has eight distinct signed paths, common-path cost eight, and selected canonical coefficient one. Consequently

    chi_A(b_A k_A)=b_A.

This unit gain is combinatorial, not inferred from a theta calibration ball. The cost belongs to this declared cubic SOURCE family. It is not a quotient norm obtained by minimizing over arbitrary lower-ideal representatives of the same observer state.

The primitive source binding is gamma-independent, but all existing retained-feature data, calibration and tail bounds remain the gamma=1/order-16 ones. Nima's order-12 constants are not copied.

## 2. What is bound to the structural artifact

The producer freshly runs Voevodsky's owning audit

    research/voevodsky/checkers/check_vacuum_acquisition_increment.py

and embeds its artifact with a digest. The portable checker independently reconstructs:

- both chain-vertex lists and all 15 contiguous-interval basis corners per block;
- actual forgotten I-source representatives dual to those coordinates;
- all 192 packet prime-edge actions per block by actual path multiplication;
- the declared ideal layers of dimensions 15,6,1,0;
- exclusion from the old terminal-divisor support and mutual disjointness;
- the image of k_A as the full-corner basis vector z_(0,6).

The source identification for the new cubic contributions is therefore

    (b_3,b_4) |-> b_3 z_(0,6)^3 + b_4 z_(0,6)^4.

The two acquired rows read those two coordinates. They do not invert the observation map on the general 30-dimensional saturated increment. On the admitted cubic-source family, the absence of other new-block coordinates follows from the SOURCE restriction and endpoint/degree support, not from reconstructing them with two measurements.

The owning structural theorem supplies the canonical split increment for an old observer supported in the A=2 packet. That old-packet support identification remains an explicit bridge premise; this bundle does not reconstruct the full old numerical observer as a source module.

The previously acquired chi_2 is retained in the baseline. Nothing here calls its acquisition split. Voevodsky's background-two nonsplitting result concerns that different enlargement and is fully compatible with the disjoint A=3,4 additions.

## 3. Keep one source prior through the square

Use the existing family

    x_A=sum_j a_(A,j) v_(A,j)+b_A k_A,
    sum_(integer A>=2) A^16 [32 sum_j |a_(A,j)|+8|b_A|] <= M,
    M=2621440.

For an unacquired group of vacuum backgrounds with first index r, its scalar sum T has the necessary coarse cost

    8 r^16 |T| <= sum_in_group 8 A^16 |b_A|.

A coarse scalar witness has an actual finite realization: put T k_r at the group's first background. It does NOT follow that every coarse state extends to later acquired constraints.

An unacquired coordinate has the explicitly PRIOR-DERIVED range

    [-M/(8r^16), M/(8r^16)].

This is not a measured vacuum channel. In particular no detector is installed for T_5.

## 4. Two genuine acquisition orders

The first route acquires b_3 and then b_4:

    T_3 -> (b_3 acquired, T_4 prior)
        -> (b_3 acquired, b_4 acquired, T_5 prior).

The second route acquires b_4 and then b_3:

    T_3 -> (b_3 prior, b_4 acquired, T_5 prior)
        -> (b_3 acquired, b_4 acquired, T_5 prior).

Exposing b_3 as a prior-bounded source coordinate in the second intermediate node is NOT acquiring it. The actual measured rows are tracked separately from prior-derived coordinates.

Both source-summary restrictions compose to

    T_3=b_3+b_4+T_5.

The A=2 coordinates and task are unchanged. On actual acquired readings, restriction simply forgets the newly acquired rows. The verifier checks complete, nonduplicated partitions, background coverage, weight monotonicity, retention of already acquired constraints, equality of the composed partitions, and the induced direct edge.

When independent child intervals have a sum wider than a coarse prior interval, the SHARED budget still implies the coarse interval by the weighted triangle inequality. No old observation is discarded to make the routes commute.

These scalar sum maps across different source corners are not source-bimodule morphisms. They must not be identified with the structural observer restriction or its canonical splitting.

## 5. Vacuum acquisition does not measure retained-feature backgrounds

Let L be the joint necessary cost of the old local coefficient boxes and newly acquired vacuum intervals. Put R=M-L. For any compatible source, if r is the first still-unacquired vacuum background,

    sum_unacquired |b_A| <= R/(8r^16),
    sum_(A>=3)|t_A| <= R D_3/(32*3^16),

where D_3 is the existing certified upper bound for (1+log 3)^2.

After BOTH readings, r=5 for the vacuum remainder. The residual sum still starts at 3: the new vacuum rows kill retained-feature sources and have not observed a_(3,j) or a_(4,j).

The same remaining budget gives the stronger coupled constraint

    8r^16 sum_unacquired |b_A|
      +[32*3^16/D_3] sum_(A>=3)|t_A| <= R.

Separate extreme tail bounds need not be jointly attained. Local and acquired contributions are added with exact interval arithmetic, and a fresh finite source witness is required for nonvacuous task positivity at each node.

A concrete check makes the feature boundary explicit. To the final feasible witness, add

    (1/10000) v_(3,0) + (1/1000000) v_(4,0).

The new vacuum readings are unchanged by homogeneous degree, and the old A=2 readings are unchanged by support. The total moment cost is

    81827803169/31250 = 2618489.701408 < M.

Thus nonzero retained-feature backgrounds at BOTH 3 and 4 remain permitted by the data. Moving the residual tail start to 5 would silently exclude admitted sources. The verifier rejects that change.

## 6. Destination witnesses and outcomes

A final feasible witness in either mode is

    v_(2,0)+(1/100)k_2+(1/2000)k_3+(1/500000)k_4,

with every other coefficient zero. Its cost is 2343301.240736 < M. The verifier checks its raw endpoint predictions and full joint cost, not just the source values at acquisition centers.

For the original feasible fixture, all four nodes are certified feasible and task-positive. Destination witnesses are checked anew; the earlier zero-tail witness is not falsely claimed to fit the new nonzero readings.

For the old middle-threshold fixture, the root remains unresolved while each acquired branch and the final node are certified infeasible. Universal bounds at the old unresolved node are not treated as proof of nonemptiness.

The artifact contains four squares: two acquisition modes times these two existing A=2 cases. These examples do not classify every possible pair of returned vacuum intervals.

## 7. Verification and limits

Generate, freshly audit the structural source data, test both routes and run isolated verification:

    uv run python research/grothendieck/checkers/certify_order16_vacuum_bridge.py

Independent verification:

    python research/grothendieck/certificates/verify_order16_vacuum_bridge.py research/grothendieck/results/order16-vacuum-bridge/private-feasible.json

Isolation requires only this verifier, its sibling `verify_source_task_transition.py`, and one square bundle. No solver, recorder, SymPy or numerical integration package is needed by verification.

The suite rejects 14 corruptions: background-two substitution, wrong endpoints/gain/source cost, asserted thirty-coordinate reconstruction, altered structural action or filtration, an erased residual background, missing or duplicated partition coordinates, fictitious tail acquisition, discarded b_3 constraints, a false witness and an equivariant-tail claim. Digests are rebound in corruption tests so semantic obligations are exercised.

Artifacts:

- `results/order16-vacuum-acquisition-inputs.json`;
- `results/order16-vacuum-bridge/*.json`;
- `results/order16-vacuum-bridge-tests.json`.

The new-row source binding is concrete, but the old packet-support identification, analytical gain/source-functional enclosures, prior justification and actual acquisition error contracts remain explicit premises. Digests do not authenticate those premises. No new claim about the old adjacent filtered class, the nonsplit chi_2 acquisition extension, or an equivariant unacquired-tail quotient is inferred from these scalar task certificates.
