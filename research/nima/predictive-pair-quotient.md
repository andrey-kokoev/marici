# History, predictive state and observation: one checked contract

## Structural synthesis

For the declared source-generator scheduling adapter, there are three distinct
layers:

    retained history --project--> predictive state --observe--> marked reading

History is a nonempty valid contextual word from (A,E). Predictive state is its
joint endpoint and labelled proton/electron centroid frames. The reading is
the joint endpoint together with coordinate 1 of the proton ABC facet centroid.

The predictive carrier has **60 states and 150 labelled transitions**. It is a
quotient of histories, not a replacement for the retained history store. The
current reading alone has only 35 classes and is not a predictive state.

Implementation: `checkers/predictive_pair_quotient.py`.
Verification: `checkers/check_predictive_pair_quotient.py`.
Receipt: `results/predictive-pair-quotient.json`.

## Reusable interface

`PredictivePairQuotient` takes the freshly checked phase-bridge binding and exposes:

- `project(history)`: predictive state ID;
- `admitted(state)` and `step(state, request)`: finite partial action;
- `observe(state)`: endpoint and marked scalar;
- `advance_history(history, request)`: original contextual path extension;
- `retain(history, policy)` and `restore(record)`: original rung transport;
- `project_rung`, `observe_rung` and `advance_rung`: the corresponding rung interface.

State IDs are local table indices, not physical labels or stable external IDs.
The state/output/transition tables and witness words are serialized in the
receipt. Transition maps are read-only. Empty histories, foreign requests,
invalid state IDs, malformed paths and unknown policies are rejected.

This interface binds single histories, not arbitrary mixed-depth path families.
The preceding phase-profile checker separately treats multiplicity profiles.

## Operation and observation contract

Let q project a history, F_a append request a, delta_a act on predictive states,
and R_p retain a history under rung policy p. For either existing policy:

    q(F_a(h)) = delta_a(q(h))
    restore(R_p(h)) = h
    advance_rung(R_p(h), a, p) = R_p(F_a(h))
    observe_rung(R_p(h)) = observe(q(h)).

Undefined requests are rejected at the history, predictive-state and rung
interfaces. All 11 registered requests are tested at every state, including
rejections. Every admitted transition is independently compared with the native
mode-step recurrence, not merely read back from the transition table.

The exhaustive finite check tests every transition and every state witness,
plus an alternative history for each state. It is not enumeration of infinitely
many histories. Extension to arbitrary valid words follows by induction:
request admission depends only on the stored endpoint, while the native update
depends only on the stored frame and request. The graph is closed under every
such update. Equal predictive states therefore remain equal under any common
admitted continuation. The original packet's exact path recovery supplies the
separate retained-provenance identity.

## Predictive equivalence is not provenance identity

The proton AB/BC/CA loop returns both the joint endpoint and the full native
centroid frame to the preparation. Prepending it to any state witness creates
a different, longer history with the same predictive state.

For all 60 witnesses the checker verifies that both rung policies retain the
two histories as distinct records and restore each exactly. Thus no inverse
from predictive state to original history is claimed. A table witness is only
a representative, not recovery of the history that actually produced a state.

## Minimality for the declared reading and requests

The receipt contains an explicit distinguishing continuation for **all 1770
unordered pairs** of distinct predictive states. Every continuation is replayed
through the transition interface and ends at unequal readings. The longest
needed continuation has **three requests**; some pairs already differ now.

Together with successor closure, this establishes that no two states in this
finite carrier can be merged while preserving every future reading under the
registered labelled requests. This is relative to the specified preparation,
request alphabet and marked reading. It is not a claim of minimal physical
state, minimal memory for aggregate families, or a spacetime dimension count.

## Gate for a future coherence-sensitive admission rule

An actual supplied rule can now be tested against a precise obligation. If it
assigns admission A(h,a), descent requires

    q(h) = q(k)  implies  A(h,a) = A(k,a).

If admitted updates change, their resulting predictive states must also agree.
A counterexample requires enriching the state or changing the declared domain;
provenance should not silently be discarded or treated as an observable.
Checking only one representative per state cannot establish descent of an
arbitrary history-sensitive rule. It needs a factorization through the state,
a proof, or independently justified finite history classes.

No new admission rule was invented here. Current admission remains endpoint
compatibility. Phase-sensitive response is established; a proton/electron
interaction, physical measurement selection, clock and energy calibration are
still outside this contract.

## First existing coherence condition tested

`predictive-pair-coherence-descent.md` tests the native normalization-coordinate
condition on the actual finite source-action carrier. Transported coordinates
descend to the 60 states; endpoint-only faithful coordinates are obstructed by
a nontrivial loop. This validates target presentations without selecting a
new physical operation-admission policy.

## Verification

    python research/nima/checkers/check_predictive_pair_quotient.py

Fresh result: **6986 contract checks pass**, after freshly rebuilding the
4603-check phase bridge and its 965-check endpoint dependency. These are exact
Python checks plus the recurrence argument above, not a new Agda theorem.
