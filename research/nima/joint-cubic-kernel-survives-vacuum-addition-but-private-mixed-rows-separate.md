# Joint cubic kernel survives vacuum addition but private mixed rows separate

## Result

On the actual 270-dimensional two-feature cubic packet V:

- the currently retained two private coordinates have rank 2;
- adding every fully vacuum observation contributes rank ZERO on V;
- the joint kernel therefore still has dimension 268;
- a specified family of 270 existing mixed private rows instead separates V exactly.

This rejects the claim that adding fully vacuum channels to the current feature selection makes the observation theory complete. It also gives a concrete finite-packet repair. It does not establish separation on the entire completed source, or a uniform conditioning bound.

## 1. Which observations are being audited

V is the minimal six-event I^3 corner on primes (2,3,5,7,11,13), with exactly two retained features. Its 270 disjoint-support source products are the ordered pair partitions with factor types (mixed,mixed,forgotten), (mixed,forgotten,mixed), or (forgotten,mixed,mixed).

The old protocol here means the saturated all-depth residual-gap observers, their declared cubic frame corrections, and the two private coefficient readings P_0,P_x from the worked source certificate. It does NOT mean every possible feature observation in the full carrier.

The original cubic functional and its matched full-response extensions take values only on v_0 and v_x on V. They add no rank once P_0,P_x are retained. Source contexts of a cubic row on this same six-event outer corner must have zero length. Lower-depth detector corners are too short.

Higher original gap detectors cannot contribute additional rank here either: every detector of depth at least four requires a retained seam in EACH of the first three prescribed diamonds. A source in V contains only two retained events within that entire initial six-event packet. A right context begins after it and cannot supply the missing third retained seam; a left context at the initial vertex must be trivial. Thus their source-action translates vanish on V.

These support arguments concern the specified detector family. Other higher-depth tests would require their own audit.

## 2. Why fully vacuum channels cannot repair this kernel

A fully vacuum observation has forgotten seams and vacuum coefficient buffers. Source recording and ordered derivatives preserve total retained degree. A positive-degree feature in a buffer does not become a vacuum merely because it was not cut.

Every term from V has retained degree two. Therefore every fully vacuum row vanishes on V. This remains true under source contexts: multiplying marked paths only adds nonnegative retained degree.

Consequently the joint kernel on V is exactly

`{sum_j a_j v_j: a_0=a_x=0}`,

of dimension 268. Fully vacuum observations detect useful degree-zero directions, as in the previous probe, but do not substitute for sufficiently rich feature observations.

## 3. An explicit surviving source and its distinguishing observation

Take

`v_y=mixed(2,3) forgotten(5,7) mixed(11,13)`.

It is a nonzero, finite, admissible I^3 source. It is invisible to the old selected feature tower and to all fully vacuum rows.

Its distinguishing existing private row has seams

- 2->4, retained;
- 12->60, forgotten;
- 420->4620, retained;

and all four coefficient buffers vacuum. The raw marked-record coefficient of this row on D3(v_y) is +1. On every other basis column of V it is zero.

The difference from the preceding all-vacuum probe is substantive: this test retains the two feature slots in their correct positions. The middle vacuum is a compositional unit and a structural label, not a replacement for either feature measurement.

## 4. A full separating family in this finite packet

For each of the 270 basis products choose the first edge of each of its three diamond factors, with the corresponding retained/forgotten mark, and use vacuum coefficient buffers.

Each resulting row is globally private among these 270 columns. The checker constructs every actual source product and its factored ordered derivative, then verifies that the entire 270-by-270 projected record matrix is the identity. It also checks disjoint source supports.

These are actual marked-seam/vacuum-buffer shapes. No formal nonvacuum potential monomials are being declared independent measurement channels.

To turn the two retained slots into scalar observations, use the existing residual test kappa on each, with the unit observation on the forgotten slot. At a fixed admitted point, the actual positive-window evaluations are nonzero: the bound

`mu_F >= log(2)tanh(3log(2)) > L`

and the positive X_F give this for every required interval. This positivity is supplied by the existing actual-window calibration and the common-window norming argument. It is not inferred from the integer record matrix.

Write E_j>0 for the product of the two actual residual evaluations on row j. The physical scalar measurement matrix is therefore diagonal with entries E_j, not numerically the identity. Dividing by those exact nonzero constants gives basis coordinates.

Thus the enlarged finite observation map is injective on V. All 268 previously missing directions are separated by genuinely additional mixed rows, not by a frame change of the old two-dimensional observation space.

## 5. Reconstruction and what conditioning remains to be certified

For raw selected scalar data z_j the unique source in V is

`x=sum_j (z_j/E_j)v_j`.

Let nu_j=||v_j||_Gamma. Disjoint supports give the exact norm formula

`Q_R(x)=6!R^6 sum_j nu_j |z_j|/E_j`.

Hence on the declared scalar l1 data space the exact inverse operator norm is

`C_R=6!R^6 max_j(nu_j/E_j)`.

For an error vector e this proves Q_R(reconstruction error)<=C_R||e||_1. The residual tests have their admitted slotwise norms; translating a full response-error budget into this scalar budget must retain those norms and the actual presentation multipliers.

This formula is finite but has NOT been numerically enclosed across all 270 physical rows here. The tiny E_j can make the inverse very poorly conditioned. The previous optimization of one scalar functional's response norm does not bound this full source-reconstruction norm.

The immediate next analytical task is a certified evaluation of C_R, or a better acquisition/reconstruction design with an explicit bound. No uniform-in-packet or uniform-in-depth inverse is claimed.

## 6. What this settles and what it does not

Settled:

- a finite-packet obstruction to completeness of the current feature-plus-fully-vacuum selection;
- an explicit surviving admissible source direction;
- a separating 270-row observation family for the actual two-feature cubic packet;
- an exact finite inverse and a precisely defined conditioning constant.

Still open:

- numerical conditioning and acquisition budgets for all 270 scalar rows;
- separation on other retained degrees and larger source packets;
- uniform estimates sufficient to pass to summable source completions;
- source-action/frame-compatible assembly of the enlarged families at all depths.

The useful conjecture is therefore not simply that vacuum and features are complementary. It is that a SPECIFIED sufficiently rich joint family separates the declared source class with controlled inverse bounds. This finite calculation tells us which measurements the existing selection lacks.

## Verification

`uv run --with sympy python research/nima/checkers/check_joint_cubic_observation_kernel.py`

Artifact: `research/nima/results/joint-cubic-observation-kernel.json`.

The exact finite audit verifies 270 disjoint source columns, zero fully vacuum projections, the two old private pivots, and all entries of the expanded private matrix. All-depth exclusion of the original gap detectors uses the retained-slot support proof above, rather than extrapolation from a finite numerical rank test.
