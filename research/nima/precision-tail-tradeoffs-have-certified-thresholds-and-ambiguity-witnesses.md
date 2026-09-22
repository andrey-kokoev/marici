# Precision–tail tradeoffs have certified thresholds and ambiguity witnesses

## Result

The acquisition certificate now distinguishes three causes of failure: an unobserved source tail, inadequate local measurements, and an unresolved enclosure gap.

For the previous synthetic raw readings, with a fixed normalized path budget, the order-16 prior is stronger than necessary:

- orders eta<=12 admit two compatible sources giving opposite vacuum-sum signs;
- eta=13 certifies both aggregate readouts positive;
- the same certificate remains valid for stronger integer orders.

This is an exact integer threshold for that specified precision policy and source family, not a universal optimal acquisition theorem.

A different, coarser local policy admits opposite residual signs even with sources supported entirely at the measured background. No strengthening of the tail prior can resolve that ambiguity. The planner also reports unresolved cases rather than misidentifying a loose bound as impossibility.

## 1. Fix the task, source family and comparable priors

Use real sources in the labelled cubic spaces V_A plus the forgotten line spanned by k_A. For this protocol the integer arithmetic backgrounds A>=2 are admitted, including A=3. All original corner labels are retained.

The task is to establish strict positivity of BOTH scalar summaries

`U=sum_A b_A`,

`T=sum_A [sigma_0(A)a_(A,0)+sigma_x(A)a_(A,x)]`.

T is the residual evaluation divided by its fixed physical factor w_seam^2. These scalar summaries are not claimed to be source-module morphisms to one common corner target.

Compare the independently specified priors

`sum_A (A/2)^eta p(x_A)<=40`, integer eta>=1.

Thus the allowed budget at the acquired background A=2 is always 40. Increasing eta restricts the unacquired tail; it does not enlarge the local source allowance. At eta=16 this is exactly the preceding budget M=40*2^16.

A prior order is an assumption to justify independently, not a quantity learned from these data. If the admitted background list excludes A=3, its first unacquired background must replace 3 throughout, including in the counterexamples.

## 2. Precision policies retain raw measurement units

Let m_0,m_x be the exact rational midpoints of the certified positive E_0,E_x calibration enclosures at A=2. For each policy use

`z_0 in [m_0-rho_0 m_0, m_0+rho_0 m_0]`,

`z_x in [-rho_x m_x,rho_x m_x]`,

`u_2 in [0.009,0.011]`.

The crossed reading is centered at zero; rho_x is a radius relative to the calibration scale, NOT a relative error of that zero reading.

The default audit evaluates nine policies: rho_0 in {1/4,1/10,1/20} and rho_x in {1/100,1/10,1/2}, with eta=1,...,20. Actual amplitudes remain near 10^(-194) and 10^(-542). The scan does not make those measurement requirements experimentally achievable.

## 3. Budget-coupled target bounds

After outward calibration division, let a>=a_min>0, |c|<=c_max, and b>=b_min>0 denote the local outer bounds for a_0,a_x,b. Define

`L=32 a_min+8 b_min`, `B=40-L`, `theta=(2/3)^eta`.

L>40 is a necessary-cost infeasibility certificate. Otherwise the vacuum target has the universal lower bound

`U>=b_min-B theta/8`.

For the residual target take certified rational bounds s_0<=sigma_0(2), s_x<=sigma_x(2), with s_0>0 and s_x<0. Let R be a certified upper bound on

`(1+log 3)^2 theta/32`.

The source-tail bound gives the following conservative minimization problem for T:

`s_0 a+s_x c-R[40-32a-32|c|-8b]`.

The minimum occurs at a=a_min, b=b_min and c>=0. If s_x+32R<0 choose

`c=min(c_max,B/32)`;

otherwise choose c=0. The resulting value is a universal lower bound for T.

This is stronger than subtracting independent worst-case local and tail errors: it respects the fact that the same budget cannot pay for both a large adverse local crossed coefficient and a large adverse unobserved tail.

It is still an OUTER relaxation of the true calibration constraints. A negative lower bound is not by itself evidence of a negative feasible target.

## 4. Sound outcomes

The procedure returns:

- **SUFFICIENT_PLAN:** a feasible positive source witness is verified, and both universal lower bounds are strictly positive.
- **AMBIGUOUS_UNACQUIRED_TAIL:** two explicit finite sources fit the same data and prior but have opposite vacuum-sum signs.
- **AMBIGUOUS_LOCAL_DATA:** two explicit sources at A=2 fit the same data and prior but have opposite residual-sum signs.
- **UNRESOLVED_BOUNDS:** neither a sufficient certificate nor a verified opposing source pair was obtained.
- **CERTIFIED_INFEASIBLE:** the necessary local moment cost already exceeds the budget.

Witnesses are checked against the raw intervals using the full calibration enclosures. They do not merely satisfy the enlarged coefficient boxes.

## 5. A sharp integer prior threshold for the baseline policy

For rho_0=1/10 and rho_x=1/100, the scan gives:

| Prior order | Certified result |
|---|---|
| 1 through 12 | Ambiguous unacquired tail |
| 13 through 20 | Both readouts strictly positive |

The positive witness is v_(2,0)+(1/100)k_2. For the opposing witness choose a lower-cost positive local source that is verified inside all raw intervals. Spend its remaining normalized budget on a negative vacuum coefficient at A=3:

`b_3=-(40-local_cost)(2/3)^eta/8`.

It satisfies the prior with equality. Through eta=12 its total vacuum sum is strictly negative. It remains a genuine finite source in both summable domains; no invented invisible coefficient or nonsummable continuation is used.

At eta=13 the universal target bounds are positive. They remain so for higher orders: theta and R decrease, while every feasible relaxed source has nonnegative unused budget. Both minimized lower bounds are therefore nondecreasing. This extension is an inequality argument, not extrapolation from the scan.

The same integer threshold holds for rho_x=1/10. Improving the crossed-row precision from that level to 1/100 does not help this particular threshold: the vacuum tail is the obstruction.

## 6. Local precision can be the obstruction instead

For rho_0=1/4, rho_x=1/2, compare the positive witness with the source supported only at A=2 having

`a_0=39/50`, `a_x=93/200`, `b=1/100`.

Its normalized path cost is 39.92, below 40. Arb verifies that it fits every raw interval and has strictly NEGATIVE residual target. The positive witness has positive residual target.

Because both sources are supported at A=2, they satisfy the same prior for every eta. No stronger tail order can settle this local measurement ambiguity. Additional precision, an additional justified constraint, or another acquired observation is required.

## 7. Unresolved cases remain explicit

For rho_0=1/20, eta=12 remains unresolved in this certificate, while eta=13 succeeds. A negative conservative lower bound and a failure of the available witness search do not establish either feasibility of an opposite sign or impossibility of certification.

Similarly rho_0=1/10, rho_x=1/2 remains unresolved at higher scanned orders. Sharper calibrated target bounds or a more complete feasible-source optimization may settle those cases.

Consequently "first certified order" is not generally an optimal threshold. It becomes a proved threshold only when lower orders have explicit opposing-source certificates, as in section 5.

## 8. Reproduction and single-plan use

Full scan:

`uv run --with python-flint --with sympy python research/nima/checkers/check_attachment_acquisition_tradeoff.py`

Single requested plan:

`uv run --with python-flint --with sympy python research/nima/checkers/check_attachment_acquisition_tradeoff.py --eta 13 --rho0 1/10 --rhox 1/100 --budget 40 --vacuum-radius 1/1000`

Artifact: `research/nima/results/attachment-acquisition-tradeoff.json`. Each run replaces this artifact with its own selected cases. It records exact rational raw intervals, finite witness coefficients, the tail-witness formula and all certified outcomes.

The command currently implements this declared real, positive-diagonal, zero-centered-cross acquisition family, not arbitrary measurement configurations. Calibration is enclosed using the actual completed theta source. The fixtures are synthetic, and source priors remain explicit inputs.

## Meaning for this lane

The useful output is no longer only "a stronger prior works." It distinguishes WHEN stronger tail information helps, WHEN local sensor precision must improve, and WHEN the proof procedure has not settled the question.

None of these state-value certificates reconstructs the intrinsic module boundary or changes the relative completeness theorem. They certify what a specified acquisition can warrant about specified task readouts, with auditable assumptions and counterexamples.
