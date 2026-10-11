# Operational unitary half-turn: proof attempt

Target: the existing `TickCompletionPhase.phase pi` is a differentiable unit-circle curve, starts at 1, ends at -1 at time one, and satisfies the generator equation with the same identified pi.

**Attempt outcome: +- (not proved).** No counterexample was found or claimed.

## Finite algebra established

`agda/TickBinomialLeibniz.agda` proves, over any commutative ring,

`sum_(j=0)^n choose(n,j) a(j) b(n-j) = productDerivative(a,b,n)`.

This supplies the previously missing connection between the explicit binomial sum and the recursive Leibniz derivative model. Applying the existing cosine/sine derivative cancellation gives constant norm coefficient one and every positive norm coefficient zero. A fresh safe Agda dependency check passes.

`agda/TickNormalizedTrigConvolution.agda` then uses the existing factorial/binomial split and the library's actual `cauchyProductCoefficient` and `finiteSumAsBigOp`. For every rational q, put

`a(k)=cosineDerivative(k)*exponentialTerm(q,k)` and
`b(k)=sineDerivative(k)*exponentialTerm(q,k)`.

It checks the all-degree identity

`cauchyProductCoefficient(a,a,k) + cauchyProductCoefficient(b,b,k) = delta(k,0)`.

This module passes with cached dependencies. The fresh closure timed out at 300 seconds while rebuilding dependencies, last logging `ExponentialTailSchedule`; it did not report a failed theorem. The cached result is retained separately, not relabeled fresh.

## Still needed for the actual phase

1. Align the dense sequences with the operational even/odd partial-sum cutoffs.
2. Instantiate the existing majorant and triangular residual estimates and transfer the identity to completion values.
3. Construct and identify the completion pi and prove its half-turn endpoint.
4. Prove metric continuity and the derivative law for the implemented phase.

The finite coefficient identity does not by itself prove the infinite/completed norm identity, much less the half-turn.

## Net update

Two intermediate nodes now record the requested shared-phase combinations:

- norm + regularity → `completion-unit-circle-flow`;
- that flow + pi half-turn → `operational-unitary-half-turn`.

The second carries this +- attempt. The assembly target remains unresolved and the predecessor's pinned ++ is unchanged. These dependency arrows describe sufficient proof routes, not automatic outcome propagation.

Checks: `checkers/check_half_turn_coefficients.py` (fresh by default, `--cached` separately), `checkers/record_half_turn_attempt.py`, and `checkers/check_completion_refinement_net.py`.
