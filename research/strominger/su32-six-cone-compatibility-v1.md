# Six-cone simultaneous compatibility audit

## Outcome

The audit does **not** select between the two wiring-shape families.

It establishes three distinct results:

1. The globally assigned records agree on all cone intersections.
2. The four middle cones are not autonomous copies of the entry cone; they require context from the rest of the assignment.
3. Native composition/filling compatibility remains **not formulated**, because the source comparison maps and filling witnesses are unbound.

Importantly, the existing transparent relay does not consume the six-pair selection annotations. Therefore its record-flow checks cannot distinguish different selected pair placements on the same cover. The differing annotations are retained explicitly, not erased or declared equivalent.

## Independent domain, fixed candidates

The checker independently builds the entire comparison domain before applying any restrictions. It finds six residual cones, with source layers

```
1, 3, 3, 3, 3, 5.
```

Each cone contains 14 cells, 24 physical faces and 16 four-interface presentations. The four complete candidate plans are reconstructed from the already fixed middle covers; reconstruction of the saved witness is checked exactly. No new paths, local operations or face choices are generated.

## Coverage is not the same as coherence

For every cover:

| Cone | Selected faces | Selected presentations |
|---|---:|---:|
| Entry cone | 24/24 | 16/16 |
| Three middle cones | 20/24 each | 10/16 each |
| Remaining middle cone | 20/24 | 12/16 |
| Exit cone | 24/24 | 16/16 |

Which middle cone has twelve presentations depends on the cover.

Thus **none** of the four plans activates every geometric presentation of every cone. If complete presentation coverage were imposed as an additional requirement, it would reject all four covers—not distinguish the two placement families.

That requirement is not silently imposed here. A potential comparison path need not be an executed wire, and a geometric incidence does not supply its operation map. The receipt lists all unselected faces separately from the missing operation laws.

## Shared records and external context

The checker replays transparent propagation from the tagged entry registry. Other cells obtain their values only through the already selected incoming edges. Repeated identities must agree. It then restricts the resulting full values and record supports to each cone.

All **204 shared-cell comparisons** across cone pairs and covers agree. This is a consistency check of restrictions of one global assignment, not an independent Segal theorem or native filling witness.

A separate, stronger rival treats each cone as a closed entry-like computation, seeded solely with the records at its source and ignoring all external incoming context. Each middle cone then has **seven sites with missing required records**. Its source packet has only the corresponding two-record view; other records used by its interior arrive through the surrounding assignment. The middle cones have six to eight incoming context edges in these plans.

This rejects the **closed autonomous copy** interpretation for the middle cones. It does not reject the contextual global assignment. The exit cone has external incoming edges too, but its full four-record central source is sufficient for its record-support propagation; merely counting external edges would not detect the distinction.

## Why the orbit-selection test cannot currently work

Each geometric orbit contains two localized pair assignments in **each** of the four covers. Within a cover they have identical:

- relay edges and record messages;
- complete per-cell record states;
- cone coverage and imported contexts.

They differ in the selected six-pair placements. Those placements are retained in all sixteen candidate-specific cone restrictions in the receipt.

Any predicate depending only on the relay/record/context data is therefore incapable of separating the two orbits. This is a structural limitation of the current test interface, not simply failure to find a clever readout.

A meaningful stronger test must use an independently specified operation or task that actually consumes the selected pair and its contextual attachment. Declaring the shorter-distance placement preferable would add a selector rather than derive it from the present overlap checks.

## Native operation gate

Each cone references twelve two-step comparison boundaries in the source domain. Their comparison maps and filling witnesses are null. The existing entry-side candidate joins do not automatically bind those whole-depth operations.

Accordingly:

- record restriction consistency: checked;
- path coverage: counted;
- selected-pair metadata: retained;
- native composition compatibility: **not formulated**;
- higher filling/coherence: **unbound**.

No cone was declared natively coherent by defining its value to be its list of decorations, and no missing geometric path was automatically interpreted as a failed physical operation.

## Reproduction

```sh
node research/strominger/checkers/check_su32_six_cone_compatibility.mjs
```

Fresh headless execution passed the stated audit assertions. Input receipts and sources are hash checked. No production operation or previous wiring plan was modified.

Receipt: `results/su32-six-cone-compatibility-v1/verification.json`.

The next missing contract is precise: **a selected-pair comparison task with explicit contextual inputs and a stated compatibility/filling condition on the overlapping middle cones**. More checks of the unchanged transparent relay alone cannot supply that condition or select an orbit.
