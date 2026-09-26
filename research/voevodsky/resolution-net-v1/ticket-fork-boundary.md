# Proof reuse is not resource consumption

The fork experiment exposes the exact boundary of resolution-as-primitive.

## Counterexample

Clone an admitted open net with one missing input. Each copy has an empty receipt set. Supply the same ticket and the same Admission evidence to both. Both pass all local checks, normalize and release, with identical receipt content. This is not a contradiction in witness-bearing closure: it retains two legal histories. It IS a violation if these are interpreted as two committed uses of one globally single-use capability.

Any decision procedure seeing only identical copyable local states and the same accepted input cannot distinguish these two uses. Pure witness data or a richer local history does not add the missing shared observation. A linear host language could instead forbid copying the relevant capability, but Python data here are deliberately copyable.

## Smallest tested extra boundary

A separate TicketAuthority model owns a live spent-ticket table plus branch revisions. Registered ticket evidence is looked up in that authority, not accepted merely because a caller supplies a witness string. A successful event stages a candidate net, validates it, then records both the new branch revision and the ticket consumption under one lock. Failed package/slot checks or stale revisions spend nothing.

Tests demonstrate:

* both serial fork orders allow exactly the first committed consumer;
* two real threads competing through one authority produce exactly one success;
* three invalid requests and a stale-revision request leave state/ownership unchanged;
* two distinct tickets may legitimately carry the SAME mathematical evidence;
* TWO independent authority realms can again consume the same named ticket twice.

Thus uniqueness is relative to an authoritative commit realm. The lock model is not distributed consensus, persistence, authentication, fairness, or security against bypassing private fields. No production service or repository task authority was introduced. No new internal net agents or rewrite schemas were needed, but one external coordinated effect was necessary for this execution interpretation.

## What this teaches about the single operator

Resolution can stay the uniform calculus for constructing and composing witnessed derivations. Treating a witness as a consumable permission is a separate decision. An admitted reference derivation does not by itself prove that an external action happened once. Flattening composes evidence; it must not re-execute consumption recorded in that evidence.

The meaningful split is NOT many domain primitives versus one opaque resolve agent. It is pure compositional resolution versus committing effects at an explicit resource boundary. The latter may itself be described by typed rules, but obtaining a witness of an actual committed transition requires its owning executor/authority. Encoding the description does not eliminate the obligation.

Fresh command: python research/voevodsky/resolution-net-v1/check_ticket_forks.py. Results: results/ticket-forks.json.

Next examine a resource-indexed rule signature: packages include a world/resource state; consumption changes that state, and sequential composition cannot reuse a removed capability. Determine formally what this prevents WITHIN a derivation and what it cannot prevent across alternate histories starting from the same world. This will locate the extra structure without silently replacing resolution by a hidden legacy executor.
