# Reference consistency and bounded nine-model decisions

Iteration 2 of the sign-action critical path. Physical admission is not a
research gate. The preceding exact census and native reference/probe binding
are in `record-sign-action-census.md`. This packet concerns complete record
laws, not equality of quantum instruments or empirical selection of a source.

Contract: `contracts/record-reference-decision.v1.json`.
Checker: `checkers/check_record_reference_decision.py`.

## 1. Exact reference consistency

Write the four reference tables as P_B, P_A, Q_00, Q_11, with 27, 27, 9, 9
cells respectively. Keep the missing-herald and both no-click categories.
Let M_B and M_A be their herald/X-detector marginals. Let z_A^+,z_B^+ be the
Q_00 marginals and z_A^-,z_B^- the Q_11 marginals.

For normalized nonnegative references, a common balanced, conditionally
independent channel explanation exists **if and only if**:

1. P_B = z_A^+ times M_B and P_A = z_B^+ times M_A, with the original record
   order retained. Each Q is the product of its two marginals.
2. M_A and M_B have the same herald marginal mu.
3. The concatenation [C_A C_B] has rank at most one, where
   C_X = M_X - mu nu_X^T.
4. F(M_A) and F(M_B) are nonnegative, where F(M) = 2 mu nu^T - M.

These are data-compatibility conditions, not proof of the actual physical
noise mechanism. They do not require a separate calibration admission.

### Necessity and a constructive sufficiency proof

Any balanced binary mixture has

\[
M_X=\tfrac12(k_0r_{X,+}^T+k_1r_{X,-}^T)
    =\mu\nu_X^T+uv_X^T,
\]

with k_0,k_1 = mu +/- u and r_X,+,r_X,- = nu_X +/- v_X. The shared herald
channel forces the same u in both matrices. Reflection swaps the two detector
columns, so F(M_X) is also a probability table. This proves necessity.

For sufficiency, the rank-zero case permits u=v_A=v_B=0. Otherwise factor
[C_A C_B] = u_0 [w_A^T w_B^T] by taking any nonzero column and its coefficients.
All three vectors have zero sum. Choose a positive scale lambda satisfying

\[
\max_{X,j:\nu_{X,j}>0}\frac{|w_{X,j}|}{\nu_{X,j}}
\ \leq\ \lambda\ \leq\
\min_{i:u_{0,i}\ne0}\frac{\mu_i}{|u_{0,i}|}.
\]

Zero-marginal rows or columns have zero corresponding coefficients and are
omitted from these ratios. Nonnegativity of M_X and F(M_X) gives
|u_0,i w_X,j| <= mu_i nu_X,j, proving that the interval is nonempty.
Set u=lambda u_0 and v_X=w_X/lambda. Then mu +/- u and nu_X +/- v_X are
normalized nonnegative columns and reproduce both matrices. The Z columns
are the basis marginals already read above. The full product closures finish
the reconstruction. The resulting channels need not be the actual channels;
the scalar interval explicitly retains their non-identifiability.

Consequences: matching herald means and separately admissible X tables are
not sufficient; their centered herald directions must agree. Normalization
and nonnegative entries of M alone are not sufficient either: for
M=diag(9/10,1/10,0), F(M) has entry -2/25. Clipping it would change the model.

## 2. Uniform reference-prediction error bounds

Every norm here is **entrywise L1**, not half-L1 total variation. Suppose each
estimated full table is a probability table and lies within epsilon_i of its
true table. Marginalization contracts L1. For probability tables M,N,

\[
\|\mu_M\nu_M^T-\mu_N\nu_N^T\|_1\leq2\|M-N\|_1,
\]
\[
\|C(M)-C(N)\|_1\leq3\|M-N\|_1,\qquad
\|F(M)-F(N)\|_1\leq5\|M-N\|_1.
\]

These follow by adding and subtracting the mixed product of marginals.
They do not require the estimated table to be compatible with a binary mixture.
Its reflected table can have negative entries; retain them.

Let e_0=epsilon_00, e_1=epsilon_11, and c(q)=1+4q for a bit q. For a rival
v=(h,a,b), the preceding reference-only predictor has error envelopes

\[
L_{T,v}=e_a+c(h\oplus b)\epsilon_B,\qquad
L_{S,v}=e_b+c(h\oplus a)\epsilon_A.
\]

For the projective candidate P,

\[
L_{T,P}=e_0+5\epsilon_B,\qquad
L_{S,P}=e_0+\epsilon_A.
\]

To prove these, expand the difference of each tensor product using the estimated
Z marginal and the TRUE M or F(M). Both have L1 norm one: the former is a
probability vector and the latter is a probability table under the candidate
model. Do not assume the estimated F(M) is nonnegative.

## 3. Decision rule and uncertainty semantics

Compute all nine predicted probe pairs directly from the estimated reference
tables, never by fitting the held-out probes. For each candidate m, **reject**
its compound source/channel hypothesis if either

\[
\|\widehat T-\widehat T_m\|_1>\epsilon_T+L_{T,m}
\quad\text{or}\quad
\|\widehat S-\widehat S_m\|_1>\epsilon_S+L_{S,m}.
\]

Otherwise report **not excluded**, not accepted or physically established.
The implementation exposes `prepare_rule(reference_tables, reference_errors)`
and `evaluate(rule, (T, S), (epsilon_T, epsilon_S))`. Inspect
`reference_region_status` first: invalid input is not evidence against a model;
a region excluded by necessary reference conditions excludes the common
compound class. An unresolved region is not certified feasible.
The strict inequality is intentional. On the simultaneous six-table error
event, the true candidate is never rejected. Several survivors mean that this
rule is inconclusive; none means that no listed compound model survives.
These outcomes do not identify which source/channel/stationarity premise failed.

A reference-only sufficient separation certificate is that the sum of the
predicted T/S L1 gaps between P and EACH rival exceeds the sum of both
candidates' two rejection radii. Then any probe pair inside P's envelope is
outside every rival's envelope. This certificate uses only reference tables
and preassigned error budgets. Zero-error evaluation reduces to exact equality
and the previous four-contrast degeneracy criterion.

### Finite-error reference checks

Do not demand exact rank/product identities of fluctuating point estimates.
The checker distinguishes an exactly compatible point (a feasible reference
witness), an excluded reference-error region, and an unresolved region.
Necessary bounds for any compatible point in that region are:

- basis product residual <= 3 epsilon_00 or 3 epsilon_11;
- bypass product residual <= 2 epsilon_B + epsilon_00, or
  2 epsilon_A + epsilon_00;
- herald mean difference <= epsilon_A + epsilon_B;
- twice the negative mass of F(M_X) <= 5 epsilon_X;
- a 2-by-2 minor of [C_A C_B], using columns from X,Y, has absolute value
  <= 6(epsilon_X+epsilon_Y).

The first three follow by tensor-product expansion and contraction. For the
fourth, equal total mass makes L1 distance to any probability table at least
twice the negative mass. For the last, expand the determinant difference;
centered entries have absolute value <=1 and each column entry error is at
most 3 epsilon_X. These bounds are conservative, not a complete finite-radius
feasibility solver. Passing them never certifies feasibility. A point estimate
that fails the exact test can still have a nonexcluded error region.

### Optional sampling wrapper

For each fixed table i, suppose its N_i attempted trials are iid categorical
samples over d_i COMPLETE record cells. Fix the sample sizes and alpha_i>0
before seeing outcomes, with sum alpha_i<1; optional stopping is not covered.
Coordinatewise Hoeffding and a union bound give

\[
\epsilon_i=\min\left(2,\ d_i\sqrt{\frac{\log(2d_i/\alpha_i)}{2N_i}}\right).
\]

With probability at least 1-sum alpha_i all six L1 bounds hold, hence so does
the simultaneous no-false-rejection guarantee for the true listed candidate.
Here d_B=d_A=d_T=d_S=27 and d_00=d_11=9. Between-table independence is not
required. Within-table iid/stationarity is an additional assumption, not a
consequence of the source algebra. No trials are postselected, and zero trials
cannot supply a finite-data confidence claim. Without this sampling premise,
the deterministic error-envelope theorem still applies to justified bounds.

## 4. No uniform precision threshold without a contrast margin

Hold the informative fixture fixed except
z_B^-(theta)=z_B^+ + theta(z_B^- - z_B^+). For every theta>0 all four exact
contrasts are nonzero. Yet rival 001 has the same twist table as P and a swap
gap theta times the original B-Z column L1 difference. That difference is 1
in the frozen fixture. Thus no positive uniform separation gap exists over
all informative channels. At a swap error budget of 1/1000 and otherwise exact
predictions, theta=1/1000 lies on the non-rejection boundary; smaller positive
theta remains exactly identifiable but unresolved by this error envelope.
This is lost statistical power, not a new exact alias. At theta=0 it becomes
the previously established exact alias.

## Tested disposition

All **1,754 checks pass**, including constructive recovery of complete references
and all nine source-bound probe predictions in the 32 predecessor strata, plus
a zero-support boundary case. All **288 candidate-truth perturbation tests**
preserve the true candidate, across **2,592 candidate comparisons**. At the
fully informative fixture, each of the nine perturbed candidate truths is the
sole non-rejected candidate. The reference-only separation certificate also
passes there.

The checker rejects the prescribed basis/bypass correlations hidden from their
marginals, unequal herald means, nonshared covariance directions and negative
reflection. It does NOT reject a finite-error region merely because its point
estimate fails exact factorization. A negative estimated prediction is retained
without clipping while the true model remains non-rejected.

The near-blind fixture gives:

| theta | Gap to 001 | Non-rejected candidates with probe error 1/1000 |
|---|---|---|
| 1 | 1 | P |
| 1/10 | 1/10 | P |
| 1/1000 | 1/1000 | P, 001 |
| 1/100000 | 1/100000 | P, 001 |
| 0 | 0 | P, 001 |

With zero error, only theta=0 retains 001. These are exact synthetic calculations,
not sampled measurements. General guarantees follow from the constructive
factorization and norm proofs above, not extrapolation from the finite fixtures.

## Verification and closure

- Validation: `e_38524_1791437611349433900_196`.
- Prospective freeze: `scc-freezes/nima-record-reference-decision.552042aa06e174c4.json`.
- Frozen challenge: `e_38524_1791437634225160400_198`, survives.
- Fresh headless closure: `e_38524_1791437749195968800_199`, pass.
- Failure/record-transport controls: `e_38524_1791437862962820100_200`.
  AssertionError and RuntimeError delete temporary prior successes. A normalized
  perturbation of a retained projective probe table is rejected at
  `witness-reconstructs-source-probes`. Live and foreign receipts are unchanged.
- Result: `results/record-reference-decision.json`, with channel witnesses,
  full perturbed reference/probe records, decisions and near-blind cases.
- Final source reconciliation: `e_38524_1791438139452122600_202`; both current
  receipts retain 8,268 passing checks in total.
- Prospective notice: `ep_99021cd0-028c-4a20-8a0e-49ab1f6872aa`.
- Tested report: `ep_ad7fd534-9223-44f9-a6c6-d8eca7c16484`. This communication
  interval and the owner artifacts remain uncommitted.

**Requested steps 2-4 are complete in the declared model class:** exhaustive
sign actions, reference/probe identifiability with exact degeneracies, and a
noise-parameter-independent decision rule with deterministic and conditional
sampling uncertainty bounds. This is not a complete noisy-region feasibility
solver, an optimal-power test, a Born derivation, an exclusion of arbitrary
correlated/context-dependent noise, or an empirical source selection. Such
extensions are separate objectives, not reasons to repeat this closed test.
Physical admission remains a claim boundary, never a research gate.
