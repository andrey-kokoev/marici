# Second observation as a nested coherence certificate

## Prior clue and candidate meaning

The operator suggests that being observed twice within the same coherence complex is required for something to be 'real'. This audit does not adopt a physical-reality criterion. It tests a narrower proposed completion condition: a second route must agree with the first while retaining and validating the first observation and its ancestry.

Relevant prior work is [nested-electron-roles.md](../nima/nested-electron-roles.md): the second witness attaches to the retained first composite, not just the original core. [nested-active-comparison.md](../nima/nested-active-comparison.md) shows, in its declared affine model, that a core-only second comparison can reopen the first agreement. Those results do not identify a physical electron with an arbitrary certificate.

## Executed candidate

Use the confirmed binary ancestry with levels 1,2,4,8. At each internal node supply a Bool x Bool presentation square for its two child records. Compare the routes LR and RL from 00 to11. They have different intermediate presentations and the same endpoint under the supplied commuting flips.

The first receipt retains both child records and the full LR history. The second retains the RL history and a reference to the complete first receipt. Recursive validation checks the children, both histories and the reference, not merely the terminal bits. Hashes implement integrity references; they are not proposed mathematical coherence morphisms.

This is a new finite certificate protocol, inspired by the prior constructors. The assignment of a square to each internal node and the requirement to audit both routes are declared candidate assumptions. No P/E window or esd7 binding has yet derived them. Both observations use the same supplied operators, so their agreement is structural consistency, not independent empirical corroboration.

## Result: 28 work units, but not a selected 28-stage law

There are seven internal nodes. Each has two two-step observations:

    7 nodes x 2 routes x 2 flips = 28 elementary operations.

This count follows from the ancestry and protocol; no stop-at-28 instruction is used. But work and stages remain different:

| Execution convention | Count |
|---|---:|
| Fully serialized local flips | 28 operations/stages |
| Sibling subtrees parallel, second observation after first | 12 move rounds |
| Both route computations parallel as well | 6 move rounds |

The last convention permits concurrent computation followed by comparison and therefore is not the same strict sequential-observation policy. The counts exclude validation/comparison costs. They are not physical durations. For branching depth d, serial work is 4(2^d-1), sequential-observation span is4d, and parallel-route span is2d.

No scheduling rule has been shown to force serialization. In particular, this does not derive the conjectured single global operator with28 stages, or its four synchronized branch traces.

## Hostile controls

The validator rejects:

- repeating LR as the purported second route;
- a wrong second endpoint;
- a fabricated intermediate history despite the correct endpoint;
- a detached first receipt;
- replacement by an equal-shaped but differently addressed child;
- a failed descendant hidden behind an agreeing root endpoint;
- missing child data.

An additional control uses two involutions that do NOT commute. Their route endpoints disagree, demonstrating that taking two observations alone cannot manufacture coherence. For the positive fixture, commutation is supplied and checked, not a newly discovered physical fact.

## Consequence

There is a concrete candidate meaning of 'observed twice': route agreement plus retained nested evidence. It supplies a completion predicate for the candidate certificate and makes28 appear as total work. It still lacks the mechanism selecting28 global stages, the oriented P/N/E readout, sector-to-ancestry binding, and a full-state geometric action preserving coherence at every intermediate stage.

The next discriminating question is whether the actual transport/window construction imposes these seven comparison obligations and dependencies. Without that binding, this remains a useful protocol model rather than a derivation of the operator's global fibration conjecture.

## Open rung4 identification conjecture

At the operator's request, net revision 4 records `rung4-double-observation-readout`: the completed twice-observed complex may realize the Realization Tower's rung4 reference/readout presentation, with ancestry retained. Acceptance requires an explicit map from the higher presentations, a separation of visible data from retained witnesses, and reconstruction or continued transport compatible with the shared coherences. Neither the numeral four nor the 28-operation count establishes this assignment. The global 28-stage operator remains a separate open node.

Contract: [persistent-seam-pe-conjecture-net.v1.json](contracts/persistent-seam-pe-conjecture-net.v1.json).

## Reproduction

`python research/strominger/checkers/check_nested_double_observation.py`

17 exact checks passed. [Receipt](results/nested-double-observation.json) retains the nested certificate, all28 serialized events, negative-control names, a depth census and source hashes. No physical reality, isotope count, P/E exchange, new Agda theorem or production change is claimed.
