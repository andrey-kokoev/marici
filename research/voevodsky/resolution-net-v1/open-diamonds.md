# Open-context simulation and the receipt-order qualification

The independent open_observer.py reads a net as a context with typed holes, a denotation after structural flattening, a pending-work count, an alpha-invariant wired-tree shape, and the UNQUOTIENTED receipt sequence. The evaluator does not import this observer.

## General argument for this extension

Assume a finite compiled context, pure level0 input histories fixed for its distinct slots, and distinct accepted tickets. Structural rules preserve the open denotation. Arrival at slot s substitutes exactly the supplied pure history for that hole; no new F agent is inserted. These facts follow by structural recursion through the surrounding constructors.

The pending outer-constructor count mu stops at layered seeds, excluding their evidence subtrees. Arrivals may enlarge a retained pure evidence subtree but do not alter mu. Structural rewrites decrease mu by1. Arrival decreases the number h of missing slots by1. Therefore mu+h decreases by1 per successful event. Structural normality with h>0 is possible and must not release. Release is exactly mu=h=0. Missing environment input is not magically supplied by this termination argument.

Local pairs:

* R/R: the previously proved disjoint pending-region diamond, modulo fresh IDs.
* A/R disjoint: rewrite and splice operate on separate interfaces.
* A/R adjacent to F/seed: arrival-first inserts d below the seed and the rewrite removes F/seed; rewrite-first exposes the input port at the result interface and arrival inserts d there. Both yield exactly d in the same surrounding context. No copying or erasure of d occurs.
* A/A at distinct slots/tickets: both insertions yield the same wired shape and slot-to-evidence map, but their receipt SEQUENCES differ.

Consequently full-state confluence including ordered receipts is FALSE without a specified comparison. The valid conclusion is convergence of the graph/denotation/availability projection for fixed compatible inputs, while arrival histories remain distinct. With a fixed arrival order, structural scheduling commutes with arrivals and retains that receipt order. Same-slot or same-ticket races are conflicts, not admissible diamonds.

This is a written structural proof argument, not an Agda formalization. Bounded implementation checks pass381 states and378 single-event simulation/decrease checks,41 R/R diamonds,103 A/R diamonds (41 adjacent critical cases), and16 A/A projected diamonds with16 explicitly DIFFERENT receipt histories. Result: results/open-diamonds.json.

Next compare the online release observation with an actual legacy join fixture under corresponding arrival boundaries. The new observer is persistent readiness, not a consumable READY token. A weak/stuttering observation relation may exist; strict step-for-step timing is not promised. Resource forks and formal Agda crosswalk remain independent open branches.
