# Operational phase unit norm: proved

**Conjecture:** `completion-phase-unit-norm`.
**Outcome:** ++, with fresh safe Agda dependency closure.

The unconditional theorem in `agda/TickConstructedScheduledNorm.agda` is

```agda
operational-phase-unit-norm : (p t : MetricCompletionCandidate)
  → Transfer.normSquared (phase p t) ≡ oneCompletion
```

`ScheduledNormBound` is constructed inside the proof, not passed in as an assumption.

## Uniformity and actual schedules

`agda/TickUniformTrigResidual.agda` supplies the missing uniform estimate. For a nonnegative rational radius r and every q with |q| <= r, induction gives

`|exponentialTerm(q,k)| <= exponentialTerm(r,k)`.

The library's constructed exponential majorant at r then dominates the dense cosine and sine coefficients for **all** q in that radius. The earlier exact operational cutoff alignment and triangular residual identity therefore give one coefficient K(r) such that

`|cosinePartialSum(q,N)^2 + sinePartialSum(q,N)^2 - 1| <= K(r)*precision(N)`.

K depends on the radius, not on the moving rational sample q.

For a regular Cauchy input x, use its canonical dyadic radius. Every common rational input chosen by `TickCommonTaylorControls` lies in this radius, and its common Taylor cutoff is at least the actual output depth n. Thus the control norm defect is bounded by K*precision(n).

The existing sample-to-control comparisons give errors at most precision(n). Choose the common amplitude M to be the actual sample amplitude bound plus one; this bounds both samples and controls. The total perturbation budget is

`4*M*precision(n) + K*precision(n) = (4*M+K)*precision(n)`.

A constructed Archimedean exponent absorbs the fixed coefficient. This gives an explicit threshold for every requested output precision, valid at **every later sample**. It inhabits `EventualSampleControls`, hence `ScheduledNormBound`. The existing quotient-transfer theorem then proves the trigonometric identity in the operational completion and the phase norm identity for every p and t.

## Verification

`checkers/check_constructed_scheduled_norm.py` ran safe Agda with `--ignore-interfaces` and completed successfully, rebuilding the dependency closure. Elapsed time was approximately 1,647 seconds. Source hashes, library hashes, compiler hash and the full command are recorded in:

- `results/constructed-scheduled-norm-fresh.json`
- `results/constructed-scheduled-norm-fresh.log`

The earlier cached pass is retained separately. Earlier 300/600-second timeouts remain historical attempt receipts; they are not the current verification status of this proof. No predecessor source or export was rewritten.

## Net effect

The norm node changes to **++**. The imported standard-C4 node remains ++. The ready frontier is now:

- `completion-pi-half-turn`;
- `completion-phase-metric-regularity`.

The unit-circle-flow node now waits only for metric regularity. The half-turn and final assembly are not closed by this norm theorem.

## Reproduce

```text
python research/nima/checkers/check_constructed_scheduled_norm.py --timeout 1800
python research/nima/checkers/test_completion_refinement_net.py
python research/nima/checkers/check_completion_refinement_net.py
```
