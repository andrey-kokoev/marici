# Noisy vacuum/residual task has feasible, infeasible and unresolved certificates

## Result

An executable task certificate now combines noisy RAW readings, actual-theta calibration enclosures and one fixed source-tail budget.

For a synthetic feasible input it exhibits a genuine source and proves, for EVERY compatible source, the aggregate readout bounds

`vacuum sum in [0.00678375, 0.01321625]`,

`residual sum / w_seam^2 in [0.04126399, 0.07970396]`.

A second input is certified infeasible by a JOINT source-budget contradiction, although its vacuum and feature costs separately fit the budget. A third run deliberately withholds the feasible witness and returns UNRESOLVED rather than mistaking a necessary budget test for existence.

These are rigorous certificates for explicitly specified synthetic inputs. No measurements were performed and no experimental capability at the required amplitudes is asserted.

## 1. Source domain and task

At each admitted integer background A>=2, allow real coefficients in the actual 270-dimensional two-feature cubic packet V_A, together with the line spanned by the forgotten cubic product k_A. Keep all original corner labels. Write

`x_A=sum_j a_(A,j)v_(A,j)+b_A k_A`.

The disjoint-support path norm is

`p(x_A)=32 sum_j |a_(A,j)|+8|b_A|`.

Fix the SAME prior for every case:

`sum_A A^16 p(x_A)<=M`, `M=40*2^16=2621440`.

This is a strong, explicit background-moment prior, not an inferred consequence of the readings. It ensures common-path and actual-letter summability on this fixed-length family. It is not silently identified with an arbitrary globally encoded convex height.

The labelled readouts are u_A=b_A and

`t_A=lambda_(r,A)(x_A)/w^2
    =sigma_0(A)a_(A,0)+sigma_x(A)a_(A,x)`.

The certificate reports the local pair at A=2 and separate l1 bounds on the unacquired tails. It also reports U=sum_A u_A and T=sum_A t_A as optional scalar task summaries. Those sums are NOT asserted to be source-module morphisms to one fixed corner module.

## 2. Raw observations and calibration

Only three rows at A=2 are acquired:

`z_0=E_0 a_(2,0)`, `z_x=E_x a_(2,x)`, `u=b_2`.

E_0,E_x are the actual positive, unscaled private residual responses at spectral point 3i and receiver gamma=2. They are not replaced by normalized coefficient data. Complete-theta Arb integration encloses them near 1.4*10^(-194) and 1.5*10^(-542), respectively.

The synthetic input intervals are exact rational balls:

- z_0 has center equal to the exact rational midpoint of the certified E_0 ball and radius one tenth of that center;
- z_x has center zero and radius one hundredth of the exact rational midpoint of the E_x ball;
- u has center 1/100 and radius 1/1000.

The artifact saves those exact rational centers and radii. Using calibration to construct a test fixture is not evidence that a real sensor can acquire it. A deployed input interval must contain all acquisition errors.

The actual constants sigma_0,sigma_x are separately enclosed from the full theta moments. All calibration uncertainty is retained in interval division and target evaluation. Correlations between these constants are NOT assumed absent; independent interval arithmetic merely gives conservative outer bounds valid for their true correlated values.

## 3. Three-valued feasibility logic

Divide the raw feature intervals by the certified positive E intervals to obtain necessary outer coefficient boxes for a_0,a_x. The vacuum interval is already a box for b.

For a real interval B let m(B)=min_(v in B)|v|. Every compatible source must spend at least

`L=2^16 [32 m(B_0)+32 m(B_x)+8 m(B_v)]`

of its moment budget. The checker computes an exact rational LOWER bound using outward Arb endpoints.

- If L>M, return CERTIFIED_INFEASIBLE.
- Otherwise, a proposed finite rational-coefficient source is certified feasible only if its moment cost is <=M AND its predicted raw readings are inside all input intervals for every value in the calibration enclosures.
- Without either certificate, return UNRESOLVED.

The lower-bound test alone is never used to assert feasibility. This is a sound certificate procedure, not a complete solver for arbitrary correlated calibration constraints. A witness need only describe a source; it does not invert the entire observer module.

## 4. The feasible source and universal target bounds

The source witness is

`x=v_(2,0)+(1/100)k_2`,

with every other coefficient zero. Its exact moment cost is 52559872/25, below M. Arb verifies that its raw predictions lie inside all three prescribed intervals.

Every compatible source, not merely this witness, satisfies the following local enclosures:

`u_2 in [0.00899999,0.01100001]`,

`t_2 in [0.04370418,0.07726378]`.

Let B=M-L. Since other unobserved coefficients at A=2 only consume budget, the remaining backgrounds A>=3 have moment cost at most B. The previously established coefficient bound |sigma_0(A)|,|sigma_x(A)|<=(1+log A)^2 and its decreasing ratio to A^16 give

`sum_(A>=3)|u_A| <= B/(8*3^16)`,

`sum_(A>=3)|t_A| <= B(1+log 3)^2/(32*3^16)`.

The certified upper bounds are respectively 0.00221625 and 0.00244019. Adding these signed tail uncertainties to the local intervals gives the positive aggregate bounds in the result.

The independent interval bounds need not describe a jointly attainable rectangle. They are universal OUTER bounds. The separate source witness establishes that the feasible set itself is nonempty, so positivity is not vacuous.

## 5. A genuinely joint infeasibility certificate

Keep the same raw feature intervals and the same moment prior, but change the vacuum reading to center 2 and radius 1/1000.

The necessary feature cost is separately below M. The necessary vacuum cost is also separately below M. Their SUM exceeds M. Therefore no single source can meet the two observations and the prior together.

No choice of calibration inside the certified enclosures, hidden source coefficients, or unobserved tail can rescue the data: each can only respect or increase the necessary nonnegative source costs. This detects incompatibility between the stated data and assumptions; it does not identify whether a sensor, calibration or source prior is responsible.

## 6. What the certificate does not infer

The module audit remains a distinct input. Numeric intervals do not reconstruct I^2E, the action of the specified ideal, the transition map, or the intrinsic relative boundary. Nor do they supply the calibrated source comparison to the original attachment.

Likewise, two positive scalar readouts on this single feasible source do not by themselves establish independence of two extension classes. The earlier two-witness determinant criterion and the owning module argument address that separate task.

The 270-row enlargement's line-lift hypothesis is not used or assumed here. Only actual source basis supports, selected scalar responses and the stated moment prior enter the certificate.

The present result is operational in the limited mathematical sense: it consumes explicit interval data and returns auditable guarantees or a contradiction. It is not a claim of practical acquisition at amplitudes around 10^(-542), nor proof that this strong order-16 prior is justified for any physical source.

## Reproduction

`uv run --with python-flint --with sympy python research/nima/checkers/certify_noisy_attachment_task.py`

Artifact: `research/nima/results/certified-noisy-attachment-task.json`.

Fresh checks cover completed-theta calibration enclosures, the finite feasible witness, necessary moment costs, all unacquired-tail bounds, a joint infeasibility case and the non-vacuous use of the UNRESOLVED outcome. Displayed task endpoints are explicitly rounded outward, rather than relying on a low-accuracy midpoint/radius printout to convey their signs.
