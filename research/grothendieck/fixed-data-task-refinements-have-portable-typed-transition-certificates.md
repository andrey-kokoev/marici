# Fixed-data task refinements have portable typed transition certificates

## Result

The existing gamma=1, order-16 task refinements now have portable, independently checked transition certificates.

The producer exports 16 chains:

- ten analytical chains: both modes, the three frozen boundary cases, and the earlier feasible/infeasible fixtures;
- six hypothetical controlled-reference chains: both modes, with task-positive, source-prior-incompatible and unresolved outcomes.

Every node's necessary cost, aggregate task bounds and claimed witness are rechecked by a standalone exact-rational verifier. Every edge binds its endpoint problems and checks its declared transition rule. Isolated execution succeeds outside the repository with only ONE verifier file and a bundle.

This implements the identity-scale portion of Nima's portable-change approach, while retaining our infinite-background tail bounds rather than silently replacing the source task by a three-variable reconstruction problem. It does not implement arbitrary coordinate rescalings or a new nontrivial source/observer square.

## 1. Node certificates retain the actual task obligations

The portable problem declares the fixed real source family at integer backgrounds A>=2, the three local raw intervals and gains, original source-functional enclosures, order-16 budget, and residual tail multiplier.

The verifier independently recomputes

    L=2^16 [32 min|B_0|+32 min|B_x|+8 min|B_v|],

where each B is the outer quotient of its raw interval by its positive gain interval.

- Infeasibility requires the exact claimed L to exceed the budget.
- Feasibility requires an explicit rational local source whose endpoint predictions fit all gain values and whose cost fits the budget. Every other coefficient and background is zero by certificate convention.
- For a non-infeasible node, the verifier independently recomputes the local and aggregate bounds using the remaining budget and the first unacquired background 3.
- A positive-task flag requires BOTH a checked source witness and strictly positive universal lower bounds for the vacuum and normalized residual sums.

An unresolved certificate does not prove absence of a witness, optimality, or genuine source ambiguity. It can retain conditional bounds but cannot assert nonvacuous positivity.

The verifier imports no solver, source recorder, numerical integration code or repository module. It uses exact rational arithmetic and strict JSON parsing; duplicate keys, floating JSON numbers and nonfinite JSON values are rejected.

## 2. Analytical identity-refinement edges

An analytical edge requires exact equality of:

- source model, acquisition mode and external assumption list;
- existing raw data and source budget;
- source-functional and tail bounds, hence the declared task;
- deployed protocol and filter evidence digests.

Each new gain interval must be contained in the corresponding old interval. A narrower analytical enclosure must cite distinct owning calibration evidence.

The exported chain is

    original -> 32768-cell refinement -> 262144-cell planning refinement.

The source, observation and target coordinate maps are identities. Their finite composition is therefore identity; endpoint nesting is checked again. This is not presented as a nontrivial commuting-square theorem.

These enclosures concern ONE fixed physical detector. The proof applies to compatible parameter/source pairs and does not assert that all enclosure values are realized physical detectors. A witness checked for the smaller enclosure need not fit every value in the old larger enclosure.

## 3. Controlled-reference restrictions are a different edge type

A reference edge retains the analytical evidence and all old source-task constraints, but carries an explicit hypothetical reference premise:

    known source v_(2,0), all other coefficients zero;
    same positive aggregate;
    valid total reference error, including preparation and acquisition.

The new positive-gain interval must be EXACTLY the intersection of the old gain enclosure and the declared reference interval. The other gains must remain unchanged. An empty intersection is rejected as a transition; the acquisition planner separately reports calibration incompatibility for such outcomes.

The entire chain is marked conditional on that reference premise. It cannot erase that marker, silently change the reference source, alter unrelated channels, or claim new analytical evidence. Simply relabelling the reference as an analytical refinement while keeping the same evidence is rejected.

No reference was acquired. A task-positive node at the end of one of these chains is conditional on the validity of the hypothetical reference-error contract, not an assertion that the proposed return actually occurred.

## 4. What the portable verifier does NOT establish

Evidence digests bind the declared artifacts; they do not authenticate an issuer or prove the analytical inequalities encoded in those artifacts. In particular, a fabricated narrower interval is not made physically valid merely because it is nested and assigned a new digest.

The fresh owning Arb computations remain responsible for calibration containment and uniform source-functional/tail estimates. The declared source family, source-cost identity and prior remain explicit assumptions. A physically valid controlled-reference error bound is another external premise, not a computational enclosure theorem.

Rewriting a bundle's assumptions and fabricating new evidence is outside numerical provenance authentication. The verifier prevents inconsistent or silently erased declared premises; it is not a signature system or an independent reconstruction of the experiment.

## 5. Corruption and portability tests

The suite rejects 13 mutated bundles, including changed raw data, a stronger prior passed off as identity, a changed target or protocol, widened calibration, a vacuous positive flag, a false witness, and erased or misidentified reference premises. Digests are rebound after mutations so these tests exercise semantic obligations rather than only checksum mismatches.

Additional tests invoke the edge checker directly on changed data and budgets, exercise strict JSON parsing, and run under isolated Python outside the repository. Original calibration and observation files remain unchanged.

Run producer and tests:

    uv run python research/grothendieck/checkers/check_portable_source_task_transitions.py

Verify an analytical chain independently:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/private-lower_threshold.json

Verify an explicitly conditional reference chain:

    python research/grothendieck/certificates/verify_source_task_transition.py research/grothendieck/results/portable-source-task-transitions/reuse-reference-task.json

Summary artifact: `results/portable-source-task-transition-tests.json`.

## 6. Boundary with tail splitting and structural coherence

Nima's `../nima/vacuum-tail-splitting-has-an-order-independent-restriction-certificate.md` introduces a genuinely different transition: new source coordinates with a partition/sum restriction map. It must not be accepted as an identity calibration edge here.

Our verifier deliberately rejects coordinate additions and unsupported transition kinds. An order-16 tail-splitting extension would need its own labelled source realizations, weighted triangle inequalities, preservation of already acquired aggregate constraints, partition coverage checks and route-composition verification. The order-12 constants in that example do not transfer numerically.

No source-ideal action, filtration change, corrected module-frame transport, adjacent extension class or infinite-tower coherence follows from these scalar task-transition certificates.
