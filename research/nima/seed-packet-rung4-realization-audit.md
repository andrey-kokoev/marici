# One seed packet at rung4: retained-record trace and physical construction gap

## Subsequent correction

An existing section-to-field successor was subsequently located in `section-field-promotion-cycle.md`. Its application to the actual seed is now checked in `seed-section-promotion-trace.md`. Thus the missing issue below is not existence of any explicit promotion rule, but its physical selection and connection to the confirmed transport diagram.

## Prior constructions recovered

The physical locus is already designated rung4. The open issue is its construction/readout, not choosing another physical locus.

Three distinct local constructions must not be merged by their rung names:

1. `rung-transport-diagram-and-fixed-reference.md`: the confirmed 12--9-->6, 11--8-->5, 10--7-->4 diagram. Middle labels are transport roles. Vertical maps reindex records. Candidate horizontal transports commute but are not uniquely selected.
2. `label-from-to-fibration-tower.md`: an explicit retained-total successor schedule cycling label/from/to for eight steps. It preserves original rows and provenance. It is not an established implementation of the confirmed diagram's horizontal generator.
3. `incidence-rung-tower.md`: regrouping plus line-graph promotion. Promotion changes endpoints; it is not the retained-total recurrence.

The prior table of confirmed roles is an interface, not evidence that all three implementations coincide.

## Actual seed trace in the executable retained-total candidate

Use the six supplied occurrences AB, BC, CA, AD, DB, BA; do not silently complete to twelve arrows. Each initial record is (label,from,to). Select AB as one packet to inspect while retaining all six.

Write r12=(AB,A,B), and each successor r=(selected inherited key, previous row). The membership equality is checked explicitly in the finite model.

| Rung | Selected field in this candidate | AB record | Retained seed rows |
|---:|---|---|---:|
|12|Initial|r12=(AB,A,B)|6|
|11|label|r11=(AB,r12)|6|
|10|from|r10=(A,r11)|6|
|9|to|r9=(B,r10)|6|
|8|label|r8=(AB,r9)|6|
|7|from|r7=(A,r8)|6|
|6|to|r6=(B,r7)|6|
|5|label|r5=(AB,r6)|6|
|4|from|r4=(A,r5)|6|

This is a table of one specified candidate, NOT a replacement for the confirmed transport-role table. Decoding eight retained predecessors returns (AB,A,B) exactly. All six packet labels, endpoints and composable endpoint relationships survive. At rung4, AB and AD still share source A; AB and DB still share target B; AB can still compose with BC and BA.

These are actual recovered incidence distinctions. They are not yet measurement responses or interactions between physical particles. Rung4 does not mean four rows, and each seed edge is not thereby a proton/electron packet.

## What the prior physical readout work supplies

`growth-rung4-readout.md` explicitly states that its retained-total adapter preserves graph structure but does not construct a physical four-state chart. Physical length and proper-time increments remain unspecified.

`rung4-ancestry-metric.md` supplies a conditional chart using G4=10I+J and ancestral occurrence coordinates. It has three contrast directions and a common direction. However, additive versus weight-normalized positions preserve the same retained data and give different scales. Distinct records can share a position, and candidate clocks differ. This is an explicit readout trial, not a uniquely constructed physical packet.

`carrier-probe-adapter-and-state-reference.md` supplies a stronger obstruction: endpoint-fixing arrow probes do not span the independent state probes. A three-cycle fixes a state while fixing no directed arrow. The state branch therefore cannot simply be inferred from those arrow observations. Equal arrow metrics also leave state-sector metric freedom in that model.

## Result and next construction target

One actual seed packet has now been traced to rung4 in the existing executable retained-total candidate without new averaging or particle labels. Its endpoint comparisons survive. The audit does not find a completed physical packet realization in these inspected constructions.

The specific structural gap identified by the retained-total note is endpoint promotion: dependent totals retain rows, while dependent products/sections are different types. The intended endpoint schematic L_a -> L_b, L_a -> Pi_ba, Pi_ab -> Pi_ba needs an explicit rule constructing the next endpoint fields. A two-row family can have an empty fiber and hence no global section, so replacing a total by a section space is not a valid generic step.

The next useful experiment is to apply that endpoint/section construction to the actual seed families: enumerate which sections exist, retain their member witnesses, and state how they become endpoints. Connect this to the confirmed horizontal transport and state branch before interpreting its rung4 result physically. This is more specific than freely selecting a metric or calling an invertible averaging model the particle dynamics.

## Verification

    python research/nima/checkers/check_seed_packet_rung4_trace.py

Passes. It also imports and runs the existing 147-table/1176-step finite fibration checks. New checks cover all six original seed rows, every retained successor, and equality of the complete composable endpoint relation after decoding at rung4. No mass, clock or minimal arrow cost is claimed.
