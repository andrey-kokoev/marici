# Arbitrary-start extension scheduling — net iteration10

Seed completeness does **not** imply that every existing rooted selection can be extended one packet at a time to every compatible rooted superset, even with only negative guards.

## Minimal generic obstruction

Use four packets r,a,b,c, no compatibility conflicts, and these edges:

- r→a, forbidden when b is selected;
- r→b, unconditional;
- b→c, unconditional;
- c→a, unconditional.

The start A={r,a} and target S={r,a,b,c} are both rooted. But adding b alone disables the only path to a, and adding c alone leaves c unrooted. There is no admissible first addition. From the seed, the ordering r,b,c,a succeeds.

Adding {b,c} atomically repairs the start. The minimum required batch size for this example is exactly2: both singleton additions fail and the full batch succeeds. This is a generic interface example, **not an asserted P/N/E realization**. A batch transition is a proposed planner operation, not a change to existing native rules.

The checker exhausts all729 three-packet negative-third-guard graphs and every rooted interval A⊆S. No smaller example occurs. More generally, with at most three packets, either A is the singleton root (covered by seed completeness), at most one packet remains to add, or A=S. Thus four packets are minimal, independently of the enumeration.

## Sufficient scheduling condition: a stable rooted anchor

Let A⊆S satisfy the seed theorem hypotheses. Form the final active graph E(S). If its restriction to A is already rooted, then a singleton-addition schedule from A to S exists.

Proof: begin with the rooted anchor A in E(S). Because all of S is rooted, unless the current prefix is S there is a final-active edge crossing from the prefix to an unselected packet. Add its target. Every retained final-active edge stays active in the prefix by endpoint heredity; compatibility is inherited from S. Inductively every prefix is rooted. ∎

This condition is sufficient, not claimed necessary: temporary edges can sometimes maintain rootedness while a final anchor is being built. The counterexample fails the condition because r→a is absent from the final graph.

An exact bounded planner can instead search rooted subsets between A and S. Allowing batch additions makes the full difference S\A a trivial upper bound, but minimizing batch size is a separate optimization problem.

## Actual P/N/E test

The checker opens the complete proof-pruned D2 live graph and independently rechecks its states and698 final certificates with the source auditor. It computes a target-specific reachability bitset for every state by reverse DAG propagation. Separately, it computes all selected-set-containing certificates. Comparing these sets asks whether **every individual certified superset** is reachable, not just whether at least one completion exists.

The earlier exact pruning receipt supplies coverage of the entire live family. Dead states have no certified supersets by the pinned completion-policy result, so do not supply additional pairs. This test does not classify arbitrary rooted noncertified targets or higher-origin configurations.

The exact comparison finds **1,803 unreachable pairs among216,531 certified-superset pairs**. Thus the source grammar itself has a target-specific scheduling obstruction already at D2. This does not contradict earlier completion results: each live state reaches some certificate, but need not reach every certified superset.

### A directly checked source realization

The start is `[0,1,2,5,16,8,20,53]`, itself certified. The target adds neutron records6 and51 and is also certified. Both new records occupy the same neutron body (cell2), at origins1 and2 respectively.

- Initially P2→E8 and P20→E53 are active terminal-PE edges sharing that vacant reference neutron body.
- Adding record6 alone occupies the body and disables **both** shortcuts. Native P2→N6→E8 replaces the first, but E53 becomes unrooted.
- Adding record51 alone also disables both shortcuts. Native P20→N51→E53 replaces the second, but E8 becomes unrooted.
- Adding both records atomically supplies both native replacements, preserving rootedness and restoring the complete certificate.

Every possible singleton first step within this target has been source-audited and fails; the two-record batch passes. This is a body-vacancy guard interaction across different readers, not a generic hypothetical counterexample. The fixed-target difference contains exactly these two records, so the minimum batch size is2.

## Next frontier

Develop **body-coherent PE materialization**: when occupying a reference neutron body, replace all active PE edges depending on its vacancy together, using their retained native PN/NE factors. Prove rootedness and exit preservation conditional on compatibility, separately test new occupied-face witness obligations, and exhaust these macro candidates on D2 certificates. This is an explicit atomic planner operation, not an alteration of native transfer rules.

```sh
node research/nima/checkers/check_extension_scheduling.mjs
```

[Checker](checkers/check_extension_scheduling.mjs) · [Receipt](results/extension-scheduling/verification.json)
