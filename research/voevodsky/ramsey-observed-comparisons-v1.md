# Fixed-observation comparison gate

Fresh inspection of the atomic-path result confirms the issue: carrier equivalence can give native package equality while changing the raw value in a fixed carrier. This turn adds an owner-local interpretation condition, leaving the owning native signature untouched.

## Gate and kernel checks

For explicit observations observeA : A -> O and observeB : B -> O into one fixed type O, an observed equivalence consists of:

    e : A equiv B,
    observeB(e x) = observeA(x) for every x.

Safe Cubical constructs identity, inverse and composition with their preservation witnesses. If e(x)=y, it proves observeA(x)=observeB(y).

The observation is recorded outside the universe-varying atomic package. An aligned observed equivalence induces a path between the correctly constructed tagged atoms. Projection of any such tagged path preserves the fixed observation, so the univalence path cannot silently relabel that observation.

## Discriminating examples

With identity observation on Bool, no observed equivalence can take false to true. The swap that passed raw package-path admission fails the observation-preservation gate, and a hostile claimed swap guard is rejected.

With constant Unit observation, the same Boolean swap is accepted and gives a tagged package path. This positive control is important: the gate protects exactly the declared observation, not every hidden field. A weak observation is not secretly strengthened to literal-record identity.

## Scope and remaining enforcement

This does not replace raw path-closed seed admission, guard every native rule, or prove that arbitrary tagged metadata describes an arbitrary native package. The tagged-atom constructor computes the correct observation for its explicit fixed-carrier value; a full operational interpretation still needs corresponding binding witnesses for all allowed state/rule constructors.

The distinction is deliberate. We have a composable comparison gate, not an unreviewed alteration of Nima's native calculus or a completed source-admission theorem.

For actual role-chart transitions, invariant observations must also be chosen correctly. Geometric vertex identity can be required to remain fixed, while C/M role assignments may be intended to change with explicit law-domain witnesses. Freezing those changing roles as invariant labels would rule out the requested transition by definition rather than test it.

## Next executable step

Instantiate separate source-bound observations on actual port data: geometric support, named reference packet, reader/provenance information and role-domain data. State which observations are invariant and which require a declared transport relation. Test actual candidate comparisons against those components before lifting a guarded policy to native derivations.

## Verification

- Contract: `contracts/ramsey-observed-comparisons-attempt.v1.json`.
- Formal source: `agda/RamseyObservedComparisons.agda`.
- Checker: `checkers/check_ramsey_observed_comparisons.py`.
- Receipt: `results/ramsey-observed-comparisons-v1.json`.
- Passing freeze: `scc-freezes/ramsey-observed-comparisons-v1.aab26015052c7154.json`.

Fresh safe Cubical checks pass with ignored interfaces and stable source/compiler inventories. The first freeze encountered unresolved observation-function implicits; explicit arguments fixed that elaboration issue. Its failed challenge remains recorded, not reinterpreted as a mathematical counterexample.

The net remains local revision23. The existing retained-correspondence result and broader open descent verdict are unchanged; no graph mutation or Git checkpoint occurred.
