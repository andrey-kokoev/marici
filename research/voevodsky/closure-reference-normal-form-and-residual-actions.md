# One reference operation, normalized views, and residual cycle actions

## Architectural prototype

`agda/ClosureReferenceNormalForm.agda` is an additive layer over the checked model, not a rewrite or removal of earlier proofs.

Its inputs are one operation F:A->B and the realization frames for each cut. It exposes:

- `view`: the presentation derived from those frames;
- `normalize`: comparison of a compatible independently constructed presentation with that generated view, including the square witness;
- `toReference`: a path of typed values from that presentation to the common reference operation;
- the existing all-level compatible-coherence machinery through its `Cuts` module;
- the existing dependent boundary decomposition through `OutputBoundary`.

The boundary default remains a dependent pair over a specified observation. Product decomposition remains a theorem requiring coherent fiber trivialization; the facade does not invent a new boundary assumption.

## Finite routes now normalize as typed-realization paths

The finite-route semantics and actual cut-change maps are reused from `ClosureAllDimensionalCutCoherence`.

For typed-realization paths, a transition from p to q goes through the common reference: first `toReference p`, then the reverse of `toReference q`. `routePath` composes these transitions along the actual finite route. Intermediate compatible presentations are the results of the checked cut-change maps, not unspecified placeholders.

`routeNormalForm` proves that this entire composite equals the direct path through the reference. Its proof is induction on arbitrary finite routes plus explicit path associativity, cancellation, and unit laws.

A closed cut route still ends at a potentially different compatible-presentation term. `closedCycle` closes that value endpoint using the earlier checked compatible cycle law. `closedCycleIsTrivial` then proves the resulting loop of TYPE-AND-VALUE realizations is homotopic to the stationary path.

This is stronger than merely checking that the ending type, or even the selected inhabitant, matches the start.

`residualIsIdentity` additionally proves that the residual transport of these particular closed cycles is identity on every inhabitant of the presentation's function type, not only on the tracked operation.

These are the paths explicitly defined through the common reference here. Arbitrary independently specified cut paths are not silently replaced by them or declared null-homotopic.

## Residual-action extraction

`agda/ClosureRealizationHolonomy.agda` extracts from a loop of typed realizations (T,v) a pair consisting of:

- an automorphism T≃T, obtained from the type component of the loop;
- a witness that its action returns the selected value v.

The module supplies `residual`, `residualAction`, and `residualFixesValue`. This is an invariant extraction, not a newly proved complete classification of all loops by such data.

## A sharper distinction, checked by counterexample

In the regression, take T=Bool×Bool and selected value (false,false). Coordinate swap is an equivalence which fixes that value. Univalence and the fixed-point witness therefore construct a loop based at the same typed value (T,(false,false)).

Nevertheless the loop is not homotopic to the stationary loop. Its action sends the probe (true,false) to (false,true). A hypothetical null-homotopy, projected to the type path and evaluated by transport on that probe, would imply false=true.

Both `valueReturns` and `notTrivial` are checked. Thus:

1. matching endpoint type;
2. returning selected value;
3. being homotopic to doing nothing

are distinct tests. The reference-based cycles above satisfy the strongest test. The swap loop demonstrates that the weaker tests cannot substitute for it.

## Connection to existing computations

`agda/ClosureReferenceNormalFormRegression.agda` reuses the existing cofiber example, common frames, independently constructed indexed operation, and clockwise/counterclockwise routes.

It checks normalization of that independent presentation, its typed path to the reference, null-homotopies of both reference-based typed cycles, and equality between those cycles. No new abstract compatibility assumptions are supplied by the regression.

The same file contains the fixed-value/nontrivial-loop counterexample described above.

## Verification

Fresh final-source command:

`agda --ignore-interfaces --transliterate -i research/voevodsky/agda -i C:/Users/andrey/tools/cubical-agda/cubical-0.9 research/voevodsky/agda/ClosureReferenceNormalFormRegression.agda`

Exit 0. All three added modules use `--safe --cubical --guardedness`, without holes or postulates. Existing source modules were left unchanged.

## What has and has not been simplified

The client-facing organization now uses one common operation and generated views, reuses the existing coherence theorem, and exposes one dependent boundary mechanism. Long reference-based typed routes reduce to an endpoint normal form. Residual actions distinguish genuinely stationary cycles from point-fixing but nontrivial ones.

This does not manufacture the realization frames, prove a new analytical identification, eliminate the distinction between arity depth and homotopy depth, or formalize every local refinement tree. Old independently chosen higher paths remain subject to explicit comparison before being replaced by these normal-form paths.
