# Scoped executable local diamond statement

## Domain and statement

Let G be a finite port-linear forest with the fixed agent arities and two distinct enabled principal pairs from the fifteen admitted COPY/Q/E rules. Require the allocator high-water premise: its integer serial is at least every allocated suffix currently live, with all subsequent names obtained by monotonically incrementing `fresh`. Assume runtime tags, if checked, agree with the admitted consumed-node roles. We discuss the local replacement operation, not `run_order`'s whole-normalization assertion or its behavior on malformed scheduler candidates.

Then either the chosen redexes coincide, giving the same reduct, or their two residual reductions exist and yield port/kind-isomorphic graphs. If tags propagate by the stated ORIGINAL/COPIED rule effects, the isomorphism preserves live tags too. This is a written conditional local diamond theorem about the inspected templates, not a machine-checked global confluence theorem.

## Proof bridge to the executable templates

1. Distinct principal pairs have disjoint agents by one principal port and linear wiring. In a forest the only internal wire of either pair is its principal wire: any second internal wire would form a parallel-edge cycle. Thus every other pair port really is an external boundary slot.
2. The static production-AST audit checks ten replacement templates, representing fifteen admitted typed cases under its manually reviewed branch manifest. Each old auxiliary slot and each new port occurs exactly once. All old boundary slots attach to new ports, not to other boundary slots.
3. The high-water allocator induction makes every allocated slot globally fresh. Different evaluation orders may use different serials, but name each fresh node by (original redex identity, local allocation slot) to compare results. No rule reads serial values to choose a Boolean or topology.
4. `replace` records outside peers, removes the pair, and substitutes the corresponding new endpoints. A boundary wire between the two redexes acquires both substituted endpoints in either order. Neither step alters the other pair's principal edge or its types. New internal edges depend only on their own rule. Therefore the two results agree under the slot bijection.
5. Local replacements used here have forest-shaped components that attach each boundary once and never merge previously separate outside regions around the same pair. Their residual principal pairs remain executable; no extra internal pair edge is introduced. ORIGINAL/COPIED roles on the other pair are unchanged, and new tags depend on each rule, not order.

## What this does and does not establish

Local diamonds do not require a termination argument. Indeed a globally closed rewrite relation with the appropriate strong-diamond property can admit a direct confluence proof without termination; alternatively termination plus local confluence allows Newman's argument. Neither route should silently assume that the graph/tag/allocator domain is preserved. For the intended constructor class, the full invariant establishment/preservation ledger still needs an integrated review. Termination is separately needed to guarantee that normalization reaches a result, even if confluence has been established.

Next assemble one theorem dependency ledger: constructor -> graph and allocator invariants -> closure; rule effects -> well-founded rank; interface/freshness -> local diamonds; closure plus rank plus diamonds -> unique normal form; root conditions -> two Boolean outputs; semantic interpretation -> correct membership answers. Mark exactly which arrows are written arguments, executable tests, or unproved. Avoid treating the finite 15,525-diamond run as the theorem itself.
