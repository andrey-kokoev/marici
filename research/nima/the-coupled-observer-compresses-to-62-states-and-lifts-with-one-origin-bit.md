# The coupled observer compresses to 62 states and lifts with one origin bit

## Frozen DPC result

The DPC is corroborated for its explicitly frozen extension:

- the existing 638-state source/acquisition/delivery/issuance system minimizes to **62 running states**;
- adding the declared origin-audit actions yields **70 minimal states**;
- exactly **eight old classes split**;
- the old class plus one faithfully retained origin bit uniquely determines the correct refined class.

Both minimality claims have complete pairwise distinguishing-continuation certificates. The live lift is checked on every state and every accepted or rejected action, so its proof covers arbitrary finite executions rather than a bounded sample of journals.

## Current outputs and language

The observable outputs are exactly:

    typed source corner,
    locally received validated value or absence,
    issued value or absence.

The sixteen labels comprise twelve possible source-event/retained-mark combinations, acquisition, delivery and issuance of zero or one. Missing transitions are observably rejected and leave the state unchanged.

This quotient deliberately does not promise preservation of every numerical assembled-observer row or every source detail. It preserves the frozen outputs and their declared continuation behavior. In particular, the two initial source orders remain distinguishable before acquisition closes, because acquisition followed by delivery reveals different values.

## The extension and its provenance

The extension adds two labels:

    audit-origin(0), audit-origin(1).

A label is admitted precisely when its argument matches `origin_is_01`, with no state change. The bit is one for the initial prefix [0,1] and zero for [1,0].

This is an audit of a retained initialization fact, not a detector that measures an erased past. The actual initial state must be known to the trusted initializer. The bit is stored before compression and maintained unchanged under all source and evidence transitions. If the initial choice is unknown or the bit is lost, this construction does not supply it retrospectively.

This extension was specified before minimization. It is intentionally narrow; its invariant-bit mechanism is simple. The substantive checks are the actual protocol's minimal quotients, the old-behavior projection, the necessary class splits and the complete live-lift certificate. This is not a conjecture of safe migration under arbitrary future languages.

## Why compression is strict

Source order and retained marks can vary while the endpoint, relevant evidence and all remaining declared permissions agree. Those distinctions are unnecessary for this particular decision protocol.

Partition refinement identifies precisely the distinctions needed for its deterministic outputs and observable admission behavior. The original 638 concrete states give 62 equivalence classes. Every pair of different quotient states has an exported distinguishing word: 1,891 witnesses altogether.

Thus 62 is minimal for these frozen observations and continuations, not merely the size of one convenient compression.

## Why provenance is needed for the upgrade

After event 3, two runs that never acquired the earlier reading can have identical current operational behavior even though their initial source orders differ. They lie in the same old class. The new audit labels distinguish them.

The extension splits one such old class at each of the eight possible post-cut endpoint masks. There can be no faithful function from the old class alone to the actual refined class for both origins. Choosing a representative would choose an arbitrary past, not recover it.

With the retained bit, there are 70 compatible `(old class, bit)` pairs, in bijection with the 70 refined classes. The full Cartesian product of 62 classes and two bit values is unnecessary: most old classes already determine the bit through existing behavior.

A binary distinction is necessary at a split class. One bit suffices globally for this extension. This is not a claim of a universally minimal provenance format or authenticated storage.

## Preservation and lift proof

The exported projection from the refined quotient to the old quotient preserves outputs, acceptance/rejection and every old transition.

The lift table is checked on all 638 concrete states. Its retained bit is invariant under all eighteen extended labels, including rejected self-loops. There are 11,484 one-step lift checks. Correct initialization and this invariant prove correctness for every finite execution, including arbitrarily repeated idempotent deliveries.

The refined quotient has 2,415 pairwise distinguishing words, establishing its minimality under the extended language.

The negative control deliberately supplies the opposite bit at a split class. It selects a different, valid refined state corresponding to the wrong history. Therefore successful lookup or well-formedness cannot authenticate provenance. Faithful initialization and retention remain explicit assumptions.

## Verification and artifacts

    python research/nima/checkers/check_compressed_observer_live_lift.py
    python research/nima/checkers/verify_compressed_observer_live_lift.py

The producer first freshly replays the owning source/evidence coupling verifier. The independent lift verifier reconstructs the transition tables, checks both quotient congruences, replays every distinguishing word, verifies the refined-to-old projection and verifies the initialization/step lift conditions. Both pass.

Artifacts:

- `research/nima/results/compressed-observer-live-lift-contract.json`
- `research/nima/results/compressed-observer-live-lift.json`
- `research/nima/results/compressed-observer-live-lift-verification.json`

The result separates two engineering roles: a small running observer for current behavior, and a deliberately retained provenance distinction for one anticipated extension. It supplies neither an unrestricted physical-history observer nor recovery after undeclared loss of provenance.
