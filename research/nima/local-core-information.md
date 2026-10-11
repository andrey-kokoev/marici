# What information would the local-core test provide?

**Current update:** A and P have now been proved under the agreed uniform-construction meaning in standard complex semantics with external whole-record return paths; see `spectral-whole-return-proof.md`. Only the A=true, P=true world remains for this clarified mathematical pair. Its uncertainty is zero because both claims are decided, not because a numerical Bayesian update was performed. The historical prior and calculations below are not revalidated for this clarification. Completion-backend and stronger interpretation questions remain outside this pair.

This is a dependency-aware planning analysis, not a new mathematical observation or an optimizer. It concerns the same L in `A = exists f L(f)` and `P = exists f (L(f) and R(f))`.

## Only three possible truth configurations

| A: local core exists | P: full lift exists | Interpretation |
|---|---|---|
| false | false | Obstruction already at the local core |
| true | false | Local cores exist, but none extends |
| true | true | Some local core extends |

The fourth assignment (A false, P true) is excluded by projection. The universal obstruction `forall f (L(f) -> not R(f))` is logically equivalent to not P; it is not a third independent uncertain bit. These truth configurations are a classical probability-model abstraction, not constructive witnesses for any branch.

## The missing probability is now identifiable

Let `p = Pr(P)` and leave `q = Pr(A | not P)` unspecified. Then the three world probabilities are `(1-p)(1-q)`, `(1-p)q`, and `p`.

`q` asks a substantive question: **if a full lift does not exist, how plausible is it that local lifts nevertheless exist?** It measures whether the obstruction lies before or after the local-core boundary. The graph alone does not answer it.

With binary entropy h:

- `H(P,A) = h(p) + (1-p)h(q)`.
- For a perfectly resolved A-test, `I(P;A) = h(p) - a*h(p/a)`, where `a = p+(1-p)q` (using the continuous endpoint convention).

Thus a weaker test can be either highly informative or nearly irrelevant:

- At `q=0`, A and P coincide in the probability model; deciding A settles P.
- At `q=1`, A is certain whether or not P holds; deciding A provides no information about P.
- Intermediate q gives intermediate information. No q has been elicited.

At the historical, subjective parent marginal `p=0.1950464396`, the information from a perfect A-test lies between 0 and about 0.712 bits. The joint entropy lies between 0.712 and 1.517 bits. These are bounds, not estimates of the current net entropy. The larger joint entropy reflects a finer distinction about where failure occurs, not uncertainty created by drawing more nodes.

## Consequences for our next step

The split is structurally useful but does not yet justify prioritizing an expensive local-core proof. We need both a meaningful L and evidence about how independent the return-extension obstruction is from L. A cheap or automatic local-core construction might be excellent for obtaining a witness while providing little information about P; information value and constructive usefulness remain different objectives.

The standalone and parent outcomes are now ++ in the explicitly scoped standard semantics. No historical parent probability has been numerically updated. The original sequential portfolio remains stopped; its old objective is not a live recommendation after this scoped proof.

Reproduce with `python research/nima/checkers/check_local_core_information.py`. The result is `results/local-core-information.json`.
