# Policy independence requires scoped admission and reserved baseline progress

## Question and disposition

Try to falsify the claim that a total source-bound WG refinement engine can admit
heuristic/resource-optimized strategies without sacrificing correctness or
completeness. The concrete risks are certificate reuse across requests, resource
comparison at incompatible accuracies, and starvation of the completeness route.

A naive policy-independent wrapper fails all three tests below. A bounded
controller with source/request admission and reserved baseline slots survives
five adversarial/cooperative policy cases on the actual stored certificates.
This is not a refutation of the broader existential conjecture, nor its total
implementation: the baseline here contains only three already constructed
certificates.

## Actual cross-request counterexample

The old 312-gate result has `word_accepted: true` for epsilon=1/10. At a request
of 1e-6 its certified lower error bound is approximately 0.0379692. Copying its
accepted flag into the new request would therefore accept a mathematically
refuted implementation.

The controller ignores that flag when judging a new request. It compares the
retained exact lower/upper bounds against the current epsilon after matching
source identities. Its three-way dispositions on the actual records are:

- old word: refuted;
- new word with coarse evaluator: unresolved;
- same new word with refined evaluator: accepted.

A mismatched source-contract hash is separately rejected. These are different
failure types; no tolerance or source is silently changed to secure acceptance.

## Optimization hostile

The old implementation costs 2184 primitive macros; the new costs 3276. The old
is cheaper but inadmissible at 1e-6. Minimizing cost across accepted flags from
different requests would choose the wrong implementation. Resource comparison
must first restrict to implementations certified for the SAME source and request.
No shorter valid candidate is constructed in this test.

## Starvation hostile and the checked scheduling policy

The deliberately unfair recurrence always consumes the heuristic's old-word
proposal and never advances the baseline. Every such proposal is refuted; by
induction no tick reaches the already available valid certificate. The checker
records a 32-tick prefix; the universal starvation claim follows from the
specified unchanged recurrence, not from extrapolating that prefix.

The tested fair controller reserves even-numbered ticks for baseline progress
and odd-numbered ticks for at most one proposal identifier. Its baseline is
[old, new_coarse, new_fine]. Policies are:

1. repeat the refuted old candidate;
2. repeat the unresolved coarse candidate;
3. propose invalid identifiers;
4. alternate those obstructions;
5. propose the helpful refined candidate.

All five reach the valid new certificate by tick 4 (zero-based), or earlier if
the heuristic helps. More generally, any baseline success at zero-based index k
is visited by tick 2k, provided each scheduled step returns. Heuristic quality
cannot take the reserved slots away.

This is cooperative policy isolation: the policy supplies a finite proposal
identifier, not arbitrary code executing synchronously inside the controller.
An unrestricted nonreturning heuristic would still block a single-threaded
engine if invoked directly. External producers need bounded execution,
cancellation or isolation; fairness of selection alone is not that mechanism.

## Honest failure at tighter tolerance

The same finite baseline is tried at 1e-8. No certificate is accepted, and the
controller reports no result within this baseline. This is INCOMPLETENESS of
this finite implementation, not proof that the task is impossible. A universal
compiler still needs fair enumeration of new words and precision levels rather
than replay of the known finite successes.

## Verification and retained witness

    python research/strominger/checkers/check_encoder_fair_refinement_controller.py

Fresh execution exits 0. It validates all direct source/checker hashes of the
actual certificates before scheduling them. The result stores every proposed
identifier, channel, request-relative disposition, and baseline progress count:
`results/encoder-fair-refinement-controller.json`.

No new numerical optimization or unitary execution is inferred from replaying
a certified record. No formal WG term, complete baseline enumerator, physical
scheduler, all-tolerance termination proof, graph publication, commit or push
was supplied.

The surviving conjecture must retain scoped acceptance and nonstarvable bounded
baseline progress as explicit executable obligations. Search strategies can be
independent of correctness only behind that interface, not by unconstrained
replacement of it.
