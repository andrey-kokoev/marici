# Bin-filter source tasks have three-valued feasibility and joint tail bounds

## Result

Update: `fixed-data-calibration-refinement-resolves-two-bin-filter-budget-gaps.md` adds opt-in robust inner-interval witnesses and fixed-data calibration refinement. The original fixtures below retain the supplied-witness-only default; withholding a witness need no longer be unresolved when automatic search is enabled.

Implemented a source-budget task certifier for BOTH gamma=1 acquisition modes of the three-channel bin-filter protocol.

With one fixed order-16 prior and explicit synthetic raw intervals, each mode has:

- a CERTIFIED_FEASIBLE case with an actual finite source witness;
- a CERTIFIED_INFEASIBLE case from a joint source-budget contradiction;
- an UNRESOLVED case when the witness is withheld;
- an UNRESOLVED result for a failed proposed witness, rather than a false infeasibility claim.

For every compatible source in the feasible fixtures, outward-rounded aggregate bounds are

    vacuum sum U in [0.00685258, 0.01314742],
    (sum_A lambda_(r,A)(x_A))/w_seam^2 in [0.05033200, 0.07042453].

Here and below the task's normalized residual variable t_A already denotes the readout per w_seam^2; the displayed residual interval is for sum_A t_A. The two modes have different raw calibration gains and different synthetic raw crossed-error intervals. Their normalized fixture constraints are similar, so these displayed task bounds coincide to eight decimal places. This is not a claim that the same raw readings can be switched between modes.

The inputs are synthetic exact-rational intervals, NOT experimental measurements. The order-16 source prior is an external assumption. The certificate does not establish that a device attains these amplitudes or that the prior describes an unknown physical source.

## 1. Fix the source task and the prior

At each admitted INTEGER background A>=2, allow real coefficients in the actual 270-dimensional two-feature cubic packet V_A and the one forgotten cubic line k_A. Keep all corner labels:

    x_A=sum_j a_(A,j) v_(A,j)+b_A k_A.

Disjoint marked-path supports give exactly

    p(x_A)=32 sum_j |a_(A,j)|+8|b_A|.

Use the same prior in all principal fixtures:

    sum_(A>=2) A^16 p(x_A)<=M,
    M=40*2^16=2621440.

This is the labelled background-moment prior used in Nima's task certificate, not an arbitrary globally encoded convex height or a response norm. Only A=2 is acquired.

Define

    u_A=b_A,
    t_A=sigma_0(A)a_(A,0)+sigma_x(A)a_(A,x),

where sigma_0,sigma_x are the ORIGINAL cubic source values per w_seam^2. The local pair and the separate absolute tails are primary certified outputs. U=sum_A u_A and the normalized residual sum sum_A t_A are optional scalar task summaries, not source-module morphisms to a single corner.

The 270 here counts source basis directions, not 270 separately acquired private detectors. The task domain is the specified 271-dimensional family per background, despite the stronger 720-column audit of our three-channel selector.

## 2. Actual gamma=1 raw calibration

Use the 76-bin, horizon-64 filters, not Nima's gamma=2 private residual responses.

In private mode,

    z_0=E_0 a_(2,0), z_x=E_x a_(2,x), u=b_2,

with E_0=n_bin([2,4])n_bin([12,60]) and E_x=n_bin([2,4])n_bin([20,60]).

In reuse mode the positive reading is unchanged, but the crossed raw reading is the signed J_x aggregate of the 448 matched blocks:

    E_x,reuse=64 n_bin([2,20])n_bin([20,420]).

Both require the separately acquired vacuum coordinate. Reuse requires the labelled raw block readings or an independently acquired J_x readout; it cannot invert the already-combined scalar observer.

The task engine consumes the certified positive E intervals directly. It does not treat the receiver's rationally normalized coordinate estimates as exact source data. Likewise it uses fresh original sigma_0(2),sigma_x(2) enclosures rather than the approximate scalar observer's gains.

Calibration parameters are correlated. Cartesian interval arithmetic is used only as a conservative outer enclosure, not a statistical independence assumption.

## 3. Exact-rational feasibility logic

Each real raw input is a rational interval [center-radius,center+radius]. The engine divides it by its positive calibration interval using exact rational endpoint arithmetic. This yields necessary coefficient boxes B_0,B_x,B_v.

For a real interval B put m(B)=min_(s in B)|s|. Every compatible source must spend at least

    L=2^16 [32 m(B_0)+32 m(B_x)+8 m(B_v)].

The three branches are:

1. If L>M, return CERTIFIED_INFEASIBLE.
2. Otherwise, certify a proposed rational source a v_0+b v_x+c k at A=2 only when its exact cost is <=M and its raw predictions lie inside every input interval for ALL calibration values in the enclosures. All other coefficients are explicitly zero.
3. Without either proof, return UNRESOLVED.

A necessary lower bound is never promoted to existence. A rejected witness is not a proof that no other witness exists. Universal conditional bounds may still be printed in an unresolved case, but the nonvacuous positive-task flag remains false.

The engine is a sound certificate procedure, not a complete solver for arbitrary correlated calibration constraints. It rejects unsupported prior fields and non-rational floating inputs rather than silently changing or ignoring assumptions.

## 4. Feasible and jointly infeasible fixtures

In each mode set:

- positive raw center to the exact rational midpoint of its E_0 enclosure, with radius one tenth of that center;
- crossed raw center to zero, with radius one hundredth of the midpoint of that mode's E_x enclosure;
- vacuum center to 1/100, with radius 1/1000.

The source

    x=v_(2,0)+(1/100)k_2

fits every raw interval for every calibration value. Its exact moment cost is

    52559872/25 < M.

The artifact saves the rational raw intervals and witness. Using calibration to construct a fixture is not evidence of physical acquisition capability.

For the infeasible case, keep the same feature data and prior but change the vacuum center to 2, retaining radius 1/1000. The necessary feature cost is separately below M, and the necessary vacuum cost is separately below M, but their sum exceeds M. Hidden coefficients and unacquired tails cannot cancel these nonnegative disjoint-support costs.

The contradiction concerns data AND calibration AND the stated prior. It does not identify which assumption would be at fault experimentally.

## 5. Uniform source-functional and source-domain bounds

The original y=3 window moments satisfy

    |sigma_0(A)|, |sigma_x(A)| <= (1+log A)^2, A>=2.

The builder freshly verifies the constants needed for this bound:

    L(7/2)>0,
    log(2)tanh(3log(2))>L(7/2),
    [(1+log 6)(1+log 210)]/18<1.

The interval support bounds mu_F<=log(upper arithmetic endpoint) and positivity of the residual means give the uniform coefficient estimate. The ratio (1+log A)^2/A^16 decreases for A>=3; the checker verifies the sufficient derivative inequality 16>2/(1+log 3).

Actual-letter admissibility is not inferred from a response norm. Using the owning completed-theta H4 tail majorant, with q_0=4pi and

    H_0=1+16 exp(-3q_0)/[1-(3/2)^4 exp(-5q_0)],

the builder freshly certifies

    ||1_[log 2,infinity) Phi||_H4^2
      <=8pi^(-9/2)H_0^2 exp(-2q_0)
           sum_(k=0)^10 binomial(10,k)q_0^(10-k)k!/2^(k+1)
      <1/4.

Thus the actual forcing letters are uniformly bounded. With fixed length six and fixed positive physical seam weight, finite path mass implies both common-path and actual-letter summability on this specified family. This does not establish every possible global height moment or a depth-uniform response bound.

## 6. Universal tails and their shared budget

Put B=M-L. Every compatible source has unacquired background cost at most B. Therefore

    sum_(A>=3)|u_A| <= B/(8*3^16),
    sum_(A>=3)|t_A| <= B(1+log 3)^2/(32*3^16).

The engine uses a rational upper bound D for (1+log 3)^2. It also retains the stronger coupled tail region

    8*3^16 sum_(A>=3)|u_A|
      +[32*3^16/D] sum_(A>=3)|t_A| <= B.

The vacuum and residual tails compete for the same source budget. Their separate maxima need not be jointly attainable.

Local residual bounds use sigma_0(2)B_0+sigma_x(2)B_x with full interval arithmetic. Adding the signed tail bounds gives the aggregate intervals in the result, valid for EVERY compatible source. The exhibited source supplies nonemptiness, so the positive conclusions are not vacuous.

A separate regression relaxes the budget and verifies that the witness remains feasible while universal aggregate positivity can disappear. Positivity is a consequence of data plus the stated prior, not of the witness alone.

## 7. Executable workflow

Fresh all-prime calibration, source audit and task fixtures:

    uv run --with sympy --with python-flint python research/grothendieck/checkers/certify_three_channel_source_task.py

Fast exact-rational regression tests:

    uv run python research/grothendieck/checkers/check_three_channel_source_task.py

Evaluate external real interval data:

    uv run python research/grothendieck/checkers/three_channel_source_task.py task.json

The deployed task engine uses only the Python standard library and certified rational calibration endpoints. Input fields are `mode`, `raw`, optional `budget`, optional `witness`, and optional boolean `auto_witness` (default false). Each raw channel has exact rational `center` and `radius`; the three labels are `positive`, `crossed`, `vacuum`. The acquired background and moment order are fixed at 2 and 16. Complex-data or additional coupled acquisition constraints are not silently discarded; those require a separately specified extension of this real-interval task.

Artifacts:

- `results/three-channel-source-task-calibration.json`;
- `results/three-channel-source-task-fixtures.json`;
- `results/three-channel-source-task-certificate.json`.

Protocol and bin-filter hashes are checked before the stored calibration is used. All displayed task endpoints are rounded outward, with exact rational endpoints retained.

## 8. Structural boundary

Voevodsky's new 270-row enlargement preserves I N=L but breaks the old graded-line lift and the right equality N I=L. None of those module hypotheses is used by this task engine.

This certificate observes only the three declared scalar coordinates. It neither adjoins the 270 private rows nor constructs a source-module nullhomotopy. Its proof uses source basis support, actual raw calibration, and the explicit moment prior. Numeric feasibility does not reconstruct the intrinsic relative boundary, its source-calibrated comparison, or an arbitrary source continuation.
