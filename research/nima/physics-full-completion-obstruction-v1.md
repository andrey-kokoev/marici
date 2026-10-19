# Full quantum completion is not identifiable from the frozen classical vocabulary

## Disposition

Reject **full detector CP-completion identification from classical records**. This is a scoped impossibility result, not a rejection of physical realizability or of eta/gamma/readiness identifiability inside the fixed classical reference family.

The result strengthens the earlier pair of countermodels to a continuum of distinct normalized CP instruments and covers arbitrary finite adaptive classical policies. No new experiment, measurement plan or empirical claim is made.

Contract: `contracts/physics-full-completion-obstruction.v1.json`.
Checker: `checkers/check_physics_full_completion_obstruction.py`.

## A continuum of valid completions

Let Phi_0 be the frozen separately labelled source instrument and Phi_1 the instrument obtained by merging the vacuum-ready and vacuum-dead-stay no-click Kraus operators, leaving every other operator unchanged. Both are CP instruments and have the same complete normalization effects, as checked in the dynamics audit.

For each lambda in [0,1], define each outcome map by

`Phi_lambda^y=(1-lambda) Phi_0^y+lambda Phi_1^y`.

Convex combinations of CP maps are CP. They can be represented by the union of both endpoint Kraus lists with coefficients sqrt(1-lambda) and sqrt(lambda). Complete effects remain identity because both endpoints are normalized. Efficiency, recovery and all source preparations are unchanged; this is not a parameter refit.

On every diagonal optical/memory input the endpoints give identical outcome maps, and both preserve the diagonal algebra. Consequently Phi_lambda has no lambda dependence on that algebra.

The instruments are nevertheless genuinely different. For the hypothetical coherent-memory vacuum state `(vac,R+vac,D)/sqrt(2)`, the no-click RD matrix entry is `(2/5)lambda` and memory-X expectation is `(4/5)lambda`. This is a mathematical distinction of channels, not a preparation/readout authorized by the charter. Different lambda therefore yield distinct full CP completions with the same classical operation laws.

## All admissible adaptive classical policies also alias

Assume the initial state is classical memory and sharp optical input. At any public-record prefix, a permitted policy may choose the next zero/one input from that prefix, apply other common diagonal-preserving classical operations, or stop. The policy and its randomization must be independent of the unknown lambda except through the available records.

Induct on prefixes. Initially all completions have the same state and empty-record mass. If a prefix has the same unnormalized classical state under all lambda, the policy chooses the same operation distribution; the preparation keeps the state diagonal, and Phi_lambda agrees there. Thus every child has the same unnormalized posterior and outcome mass. A stopping decision is a function of the same prefix and consequently also has the same distribution.

This proves equality of all finite public-record laws. Randomized policies follow by averaging deterministic policies. Parameter-independent terminating stopping rules follow by summing the identical terminal-prefix masses; no optional-stopping claim about a new estimator is needed.

More classical records, different adaptive input policies, or a record-based stopping rule cannot identify lambda within this vocabulary. The mathematical result extends beyond the three-bin charter as an induction theorem; it does not enlarge the admitted physical target horizon.

## A sharp quantitative inverse obstruction

Let T be any estimator of lambda based only on these classical records and parameter-independent randomness. Its distribution is identical at lambda=0 and lambda=1. Therefore

```
max(E_0[T²], E_1[(T-1)²])
  >= (E[T²]+E[(T-1)²])/2
  = E[(T-1/2)²] + 1/4
  >= 1/4.
```

If a second moment diverges, the bound is trivial. Otherwise this is the sharp squared-error minimax lower bound over lambda in [0,1]: constant T=1/2 has maximum risk 1/4. There is no data-dependent improvement while the record distribution is constant in lambda.

This differs from an ill-conditioned but injective inverse. The full-completion parameter has a nontrivial entire observational fibre even with exact laws and arbitrarily many records. The previously constructed inverse for eta,gamma,r remains valid within the reference family and does not remove this fibre.

## Implications for physical realization and explanation

A valid conditional CP construction establishes neither that this apparatus realizes a particular lambda nor that a native source selects it. The classical physical target may be realized by any member of this operational equivalence class without identifying its larger quantum completion.

There are two honest routes:

1. State recovery and identifiability only on the charter's classical operational equivalence class.
2. Supply an independent source premise selecting the environmental/quantum completion before making a broader claim.

No measurement extension is requested here. Actual physical preparation/routing/reset authority, source-law selection, clock and energy bindings remain missing. This obstruction does not prove that no physical instrument exists; it proves that the current vocabulary cannot select the full completion.

## Verification

Fresh exact checks cover nine rational lambda values, all 72 diagonal outcome-map cases and every depth-three deterministic public-record input policy (128 policies). Across three initial readiness states, they compare 27,648 complete adaptive word cases, with full normalization and identical posteriors. The affine construction, diagonal-algebra identity and prefix induction prove the full continuum/all-policy result; the fixtures corroborate it.

The coherent-memory channel distinction and the exact endpoint-risk polynomial identity are also checked. All inputs are hash-verified before and after execution. No acquired observations are used.

```
python research/nima/checkers/check_physics_full_completion_obstruction.py
python research/aspect/scc/scc.py check physics-programme-v18
```
