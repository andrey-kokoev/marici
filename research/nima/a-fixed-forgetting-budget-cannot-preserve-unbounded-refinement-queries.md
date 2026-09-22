# A fixed forgetting budget cannot preserve unbounded refinement queries

## Disposition

The first attack on bounded interface synthesis finds a necessary limitation:

> Exact preservation of arbitrary future finite-support feasibility queries has no uniform finite memory bound, even when the source history, marked-cut answer, optimizer, current optimum and positive decision certificate all agree.

This is an obstruction in the existing declared source/tail control coupling, not a newly designed parity/interval fixture. It is still not an adapter for the actual prime-calibration task: that correspondence remains absent.

For a fixed finite query horizon, the restricted refinement family tested here has a simple, sufficient and irredundant representation. The constructor derives its needed coordinate mask and refuses an insufficient budget. Thus this is a lower-bound gate for synthesis, not a claim that certified forgetting is generally impossible.

## 1. Freeze the source and current certificate

Use origin zero and the existing accepted protocol path:

    acquire; source(3,0); deliver; source(2,0).

The resulting source state is `[15,0,0,0,None]`. The receipt was already present immediately before the marked source(2,0) cut. That marked historical answer is true in every tested development.

The final source operation halves both tails. Channel zero has even support; channel one has adjacent capacity. Write their coordinates x and y. The current task remains

    F = -sum 2^-n (x_n+y_n) > -31/32.

Every history below retains the same valid finite certificate

    F >= -17/32 > -31/32.

The source operations and current numerical carrier are those already bound by the mixed constructor. The extension tested here is a declared language of finite-support evidence frames and compatibility queries on this same tail snapshot. Truthfulness of the original frames is assumed; no new physical observation adapter is asserted.

## 2. Many refinements leave the same optimizer unchanged

Let J be any finite subset of even indices n>=6. Retain the frames

    y_n <= 0, for n in J.

They all hold at the same infinite optimizer:

    x_even = 1/2, x_odd = 0;
    y_odd = 1/2, y_even = 0.

That point has objective -1/2. The original source carrier has the same minimum: the scaled even-support and adjacent-capacity bounds sum to -1/2. Restricting the carrier cannot lower its minimum, and the displayed point still attains it. Consequently every J has **exactly the same minimum and a common minimizing point**.

This is not an exact-threshold pathology. The current decision has a substantial positive margin, and the same finite certificate proves it for all J.

## 3. Future feasibility distinguishes every retained subset

Allow the read-only future query

    Is adding y_n >= 1/2 jointly feasible?

This asks about compatible possibilities; it does not declare that an actual tail changed.

- If n is in J, the old row y_n<=0 and the queried row -y_n<=-1/2 sum to `0<=-1/2`. Multipliers (1,1) are an exact Farkas certificate of inconsistency.
- If n is not in J, take x identically zero and y with one mass 1/2 at n. This satisfies every prior zero frame and every adjacent-capacity interval bound. Its zero-extended infinite tail is an explicit feasibility witness.

Thus a future query reads whether n belonged to J. No selected optimizer can substitute for the retained possibility set: the common optimizer has y_n=0 in both cases, but the two carriers admit different alternatives.

## 4. Storage lower bound

Choose H distinct even coordinates. Their 2^H subsets produce 2^H pairwise different future-answer functions. Any exact deterministic interface must distinguish them, so it needs at least H bits of history-dependent information.

H is unbounded in the declared finite-support query language. Therefore no fixed finite bit budget works for the whole language.

All retained history-dependent information counts: hashes, certificate variants, specialized code, and any external journal used to recover discarded frames. A fixed-size digest does not defeat the counting argument. Encoding a subset in an exact real or rational does not make its bit storage constant.

The source state and marked answer are fixed in this subfamily. Adding more source or historical queries cannot remove the existing distinctions.

## 5. A synthesis rule and its independently tested refusal

The frozen rule takes dependencies on the declared probe coordinates and retains the zero-frame membership mask on those coordinates. It is defined before the global distinguishability check, not extracted from a previously minimized observer.

For the finite test:

- ten probe coordinates, 6,8,...,24;
- an eight-bit budget for all history-dependent refinement information;
- 1,024 retained refinement states;
- 10,240 exact primal/Farkas feasibility checks;
- 523,776 pairwise separating-query checks.

All 1,024 continuation signatures are distinct. The constructor therefore returns `REFUSE_BUDGET`: ten bits are necessary.

An explicit unsafe forgetting rule retaining only the lowest eight bits merges J=empty with J={22}. Their source history, current numerical certificate and retained eight-bit interface coincide. The query y_22>=1/2 is feasible for the first and inconsistent for the second.

With a ten-bit budget the membership mask is sufficient and irredundant for this restricted family of zero frames and read-only probes. Repeated frames and their order may be forgotten because they do not affect the declared queries. Removing any membership bit loses a separating query.

This is not a ten-bit sufficiency claim for arbitrary linear evidence or a larger historical query language.

## 6. What this changes in structural synthesis

Uniform tail control for one objective does not control an entire future query language. Here the current objective and decision are exactly unchanged, yet arbitrarily late coordinates remain observable through feasibility queries.

A finite positive decision certificate is therefore not a uniformly bounded reusable admission interface. These are different products with different guarantees.

The next synthesis contract must specify at least one of:

- a fixed query horizon or another finite family of residual distinctions;
- a storage bound that grows with the admitted query/evidence family;
- a justified uniform approximation policy, with weaker answers explicitly allowed;
- a narrower future language for which the discarded information is provably unobservable.

A sound synthesizer should be allowed to return a **storage obstruction**, rather than silently erase distinctions to meet a requested budget. The present control supplies both a sufficient horizon-dependent representation and exact evidence that a smaller fixed budget cannot meet the promise.

## Verification

    python research/nima/checkers/check_certified_forgetting_storage_obstruction.py
    python research/nima/checkers/verify_certified_forgetting_storage_obstruction.py

The producer freshly replays the independent mixed-certificate verifier. The new independent verifier imports neither the producer nor an optimizer. It reconstructs the source path, checks the marked cut, exact geometric optimum, feasible spike tails, Farkas contradictions, all continuation signatures and pairwise separators. Both pass.

Artifacts:

- `research/nima/results/certified-forgetting-storage-obstruction-contract.json`
- `research/nima/results/certified-forgetting-storage-obstruction-packet.json`
- `research/nima/results/certified-forgetting-storage-obstruction.json`
- `research/nima/results/certified-forgetting-storage-obstruction-verification.json`
