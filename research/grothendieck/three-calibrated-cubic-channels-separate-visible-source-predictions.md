# Three calibrated cubic channels separate visible source predictions

## Result

Implemented a calibrated three-coordinate protocol retaining the positive source coefficient, crossed source coefficient and vacuum coefficient separately. It uses the existing 76-bin filters at A=2, y=3, gamma=1 and the independently acquired unit vacuum row.

The exact source audit covers ALL 720 minimal cubic basis products in the fixed six-event corner, across retained degrees zero through three. The reported three-channel map has rank three and kills the other 717 basis directions.

Two acquisition modes are certified:

| mode | existing record readings used | positive inverse-gain bound | crossed inverse-gain bound | vacuum gain |
|---|---:|---:|---:|---:|
| private | two private feature rows plus vacuum | 1.59228524e192 | 1.72141870e540 | 1 |
| reuse | the existing 449 labelled feature readings plus vacuum | 1.59228524e192 | 2.68971672e538 | 1 |

These are bounds for the explicit rationally normalized tests; their calibration defects are retained. No physical w_seam^2 factor is inserted in source-coordinate readings.

At raw feature-channel error 10^(-543), private mode gives coordinate errors below 0.01 for |a|<=1, |b|<=1/2. At error 10^(-540), reuse mode gives crossed error below 0.04 for |b|<=1/2. Private mode does NOT offer that precision at the latter budget.

A joint error-region evaluator and calibration-robust prediction-separation test are implemented. This certifies conditional discrimination of visible predictions, not physical acquisition accuracy or full source reconstruction.

## 1. Exact source coordinates, including the vacuum direction

Let

    v_0=mixed(2,3)mixed(5,7)forgotten(11,13),
    v_x=mixed(2,5)mixed(3,7)forgotten(11,13),
    k=forgotten(2,3)forgotten(5,7)forgotten(11,13).

Restrict to J_3 in the specified six-event corner. Write

    x=a v_0+b v_x+c k+nuisance.

The minimal cubic basis has 90,270,270,90 products in retained degrees 0,1,2,3 respectively. The same ordered marked-path construction used for the two-feature optimization builds all 720 actual columns.

Private mode selects the vacuum-buffer rows with arithmetic seams

- positive: 2->4 retained, 12->60 retained, 420->4620 forgotten;
- crossed: 2->4 retained, 20->60 retained, 420->4620 forgotten;
- vacuum: 2->4, 12->60, 420->4620, all forgotten.

Their source coefficients are +1 on v_0,v_x,k respectively and zero on every other basis column. The two retained slots are tested by theta_bin tensor theta_bin; the vacuum row uses its existing unit observation, not a feature test.

Put n(F)=theta_bin(O Psi(F)). The exact private measurement matrix is

    (raw_0,raw_x,raw_v)^T=diag(E_0,E_x,1)(a,b,c)^T,

    E_0=n([2,4])n([12,60]),
    E_x=n([2,4])n([20,60]).

All three gains are certified nonzero, and the first two are positive. Thus exact normalization would recover the three coordinates. The numerical implementation encloses rather than assumes exact normalization.

Higher or other source directions are not reconstructed. The 717-dimensional kernel stated here is the kernel of this REPORTED three-channel map on the declared 720-dimensional corner, not the kernel of every available labelled measurement.

## 2. Reuse the existing labelled data without losing the crossed coordinate

The matched norming construction already supplies a signed sum J_x of 448 feature-block readings, annihilating every cubic column other than v_x. The positive reserved row is outside its support. Fresh polynomial cancellation checks extend this statement from the 270 two-feature columns to all 720 columns.

In reuse mode keep the positive reserved reading separately and use J_x as the raw crossed reading. Its source gain is

    E_x,reuse=64 n([2,20])n([20,420]).

The inverse cost is approximately 64 times smaller than the private one-row cost. J_x, the reserved positive row, and the vacuum row have disjoint record supports. Therefore their vector readout is contractive in the raw labelled l1 record norm, before inverse normalization.

This needs the retained raw labelled readings or an independently acquired joint J_x readout. It CANNOT recover two coordinates from the already-combined scalar cubic observer value. Nor is the vacuum coordinate computed from arithmetic fields.

The 450 raw records may contain more information than the three reported combinations. If every raw reading is independently adjoined to a saturated observer module, its top rank need not be three. The rank-three statement concerns the declared scalar readouts P_0,P_x,chi.

## 3. Rational calibration and explicit costs

For each channel i choose the manifest's positive rational inverse g_i and enclose

    E_i in [l_i,u_i], l_i>0,
    |g_i E_i-1|<=delta_i.

The vacuum has E_v=g_v=1 and delta_v=0 exactly. In private mode, the two defects are below approximately 0.005479 and 0.005445. Shared filter and theta parameters can correlate these enclosures; no probabilistic independence is assumed.

For separately bounded raw errors epsilon_i and known coefficient budgets M_i,

    |estimated_coordinate_i-true_coordinate_i|
       <=g_i epsilon_i+delta_i M_i.

The private examples at epsilon_0=epsilon_x=10^(-543) give

    positive error <0.005479, for |a|<=1,
    crossed error <0.004444, for |b|<=1/2.

At 10^(-540), private crossed noise alone exceeds one normalized unit. The good noise margin of the original scalar observer must not be mistaken for equally precise recovery of each source coefficient.

Reusing J_x reduces the crossed inverse-gain bound to 2.68971672e538. At raw crossed error 10^(-540) and |b|<=1/2, its total bound is below 0.029620.

## 4. Joint regions without a hidden source-amplitude prior

The receiver also computes data-dependent regions. For measured raw value z_i, the exact coefficient satisfies

    |c_i|<=(|z_i|+epsilon_i)/l_i.

Therefore a disk centered at g_i z_i with radius

    g_i epsilon_i+delta_i (|z_i|+epsilon_i)/l_i

contains the true coordinate. Arithmetic radii are added explicitly. The product of these disks is a conservative joint outer region, not a statistical confidence statement.

A sharper joint description is retained in the output: for some calibration gains in their certified intervals,

    |E_i c_i-z_i|<=epsilon_i,

and, if a total raw l1 budget eta is supplied,

    sum_i |E_i c_i-z_i|<=eta.

The rectangular calibration range is an outer bound on the actual correlated calibration set. It does not claim that every combination of interval endpoints is physically realized.

## 5. Calibration-robust separation of competing predictions

For predicted source coordinates p and q, use nominal forward centers p_i/g_i and q_i/g_i. The calibration uncertainty around them is bounded by delta_i |p_i|/g_i and delta_i |q_i|/g_i.

Hence a lower bound on the distance between their raw calibration sets in channel i is

    D_i=max(0,(|p_i-q_i|-delta_i(|p_i|+|q_i|))/g_i).

The predictions are certified distinguishable if any D_i>2epsilon_i. With a total l1 error budget, sum_i D_i>2eta is another sufficient test. These comparisons include BOTH calibration uncertainty and acquisition noise. Failure to certify separation is not a proof of equality.

The tests show:

- crossed coefficients 1/2 and 3/4 are separated in private mode at 10^(-543), but not certified there at 10^(-540);
- reuse mode separates them at 10^(-540);
- coefficients 1000 and 1001 in the positive direction are not spuriously declared distinguishable at zero acquisition noise while calibration uncertainty remains;
- a joint l1 budget can separate a pair even when none of the marginal disk tests does.

## 6. The independent vacuum discrimination survives the conditioning audit

For Nima's realized alternatives differing by 10^(-10) w_seam k, the vacuum coordinate difference is exactly 10^(-10) w_seam. Its gain and calibration are exact, so

    epsilon_v<=2.5*10^(-11) w_seam

gives strict separation for every w_seam>0. This is checked symbolically in the positive parameter; no value of w_seam is assigned.

Poor feature-channel precision cannot erase this separately acquired distinction. Conversely, precise positive/crossed readings do not manufacture the vacuum reading. The receiver rejects missing vacuum input instead of filling it with zero.

This is consistent with Voevodsky's intrinsic-boundary audit: the labelled source-module structure supplies the boundary, and source calibration identifies its normalization. Our numerical readout does not reconstruct the module action, transition, source representative, or an unseen tail. The vacuum relative attachment is not reinterpreted as a surviving adjacent pushout.

## 7. Implementation and data contract

Build and certify both modes:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_three_channel_cubic_protocol.py

Test enclosures and discrimination:

    uv run --with python-flint python research/grothendieck/checkers/check_three_channel_cubic_protocol.py

Evaluate:

    uv run --with python-flint python research/grothendieck/checkers/evaluate_three_channel_cubic_protocol.py observations.json

The JSON input supplies:

- `mode`: `private` (default) or `reuse`;
- `raw`: separately labelled `positive`, `crossed`, `vacuum` complex pairs;
- `errors`: nonnegative raw error bounds for those same labels;
- optional `total_l1_error`, `precision_bits`, and two `predictions` in source-coordinate units.

In reuse mode the raw crossed value means J_x, NOT the one-row private reading. The Python `aggregate_reuse` method takes all 449 raw feature readings, their error bounds, and an independently supplied vacuum value/error. It forms the two feature coordinates without using the scalar observer's gains.

The protocol delegates bounded hat-integral and joint-tensor evaluation to the time-bin receiver. It defaults to 2048 bits and checks both protocol and bin-filter calibration hashes. Source coordinates are linear; no w_seam^2 multiplier or automatic first-slot conjugation is applied. To compare with the earlier conjugate-linear scalar convention, form the corresponding conjugated combination of these coordinates, with its declared S_0,S_x and physical w_seam^2.

Artifacts:

- `results/three-channel-cubic-protocol.json`;
- `results/three-channel-cubic-certificate.json`;
- `results/three-channel-cubic-tests.json`.

Tests are analytical and synthetic fixtures. The asserted accuracy remains conditional on the actual acquisition budgets. The gamma=1 noise constants here are not silently substituted for Nima's separate gamma=2 source-lift protocol.
