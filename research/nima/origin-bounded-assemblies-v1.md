# Origin-bounded branching assemblies

[Open the phase-budget explorer](results/origin-bounded-assemblies/index.html).

This executes Strominger's reply `naradaepistemiccommunication:e0931758a81ae1502559` (event16169). It replaces the mistaken **operation-count** interpretation with an explicitly named **absolute realization-origin budget**. The [earlier nine-operation experiment](generative-phase-assembly-v1.md) is not a phase-bounded answer.

## The contract

The [input contract](inputs/origin-bounded-assemblies-v1.json) is:

- `budgetKind = realization-advances`.
- Seed origin0; every selected packet has0≤origin≤D.
- A configuration's grade is the **maximum** selected origin, not the sum of executed increments.
- PN, inverse-PN and NE have delta0. Reader-phase-advance and NN-phase-advance have delta+1 after their witnesses pass.
- No operation-count, reader-visit, final-C-index or scheduling-round cutoff is substituted for D.

Two compatible sibling advances from r both land at r+1. A dependent PN followed by NE can involve two operations at origin0. Older retained records can contribute new branches without resetting or advancing their own origin.

All contexts are still bound and checked. The windows at r are:

- P: C_r M_r C_(r+1) [M_(r+1)].
- N: M_r C_(r+1) M_(r+1) [C_(r+2)].
- E: M_(r+1) C_(r+1) C_(r+2) [M_(r+2)].

An E at r=D is allowed. Its last C has index D+2 and its context M_(D+2) remains part of the reference binding; neither is an additional realization advance. A final-C-index bound would be a separate policy.

## Same-origin closure preserves alternatives

Closure is reachability through **all compatible configurations**, not inserting every enabled packet into one maximally saturated state. NE and NN from a common N can occupy the same geometric target with different species: each is an alternative, and their union is rejected. A zero-grade NE must not be forced before exploring the +1 NN branch.

Every compatible source operation from every selected record is considered. A repeated operation returning an already selected record becomes a labelled cycle/self-loop. It is not deleted, assigned a fictitious positive grade, or used to reset origin. An E ends only its branch.

The seed, local geometry, five-slot maps and reference conventions are inherited from the common [seed generator](generative-phase-assembly.mjs); no isotope layouts or target compositions are introduced.

## Finite graphs, not finite lists of histories

Under the current local zero-grade rules, PN and inverse-PN return the exact same pair of packets, while NE is terminal. A zero-grade closure from a packet therefore has at most three packets. Each such closure has at most three +1 successors. A finite D bounds the reachable packet universe, although PN/inverse-PN revisits give infinitely many ordered words already at D=0.

The implementation keeps those words as labelled graph paths. Construction representatives have finite `minOperations` metadata, but that number is **never** an admission limit.

Two independent constructions are compared:

1. Explicit breadth-first enumeration of all compatible selected packet sets and all their allowed operation edges, with no operation bound.
2. An exact reduced Boolean decision diagram. Packet-selection variables obey pairwise occupancy/role/contact guards and root-support constraints on the acyclic condensation of the zero-grade PN pairs. Dual support and contact-witness constraints characterize the selected-record exit certificate.

Within a zero-grade strongly connected pair, every nonempty selected subset is reachable from its selected entry packet. Condensation edges are either directed terminal NE links at the same origin or +1 links. This makes the support criterion equivalent to rooted reachability; a changed rule producing a larger zero-grade component or a condensation cycle fails the compiler rather than reusing that proof.

Every explicitly enumerated selection is checked against the Boolean family, and the exact family cardinalities agree. Every outgoing fanout and labelled edge is audited. This checks state and history-edge completeness separately.

For performance, the enumerator compiles the current unary/binary occupancy, role and face guards into a pair-conflict table. Verification still checks every entire retained configuration with the original whole-state guards and compares every exit flag to the independent Boolean formula. A new higher-order or ancestry-dependent sewing rule would require a compiler/key extension, not reuse of the pair table.

## Validation budgets0,1,2

| Maximum origin D | Origin layers, including seed | Compatible configurations | Local selected-record exit certificates | Geometry/role candidates | Maximum occupied bodies |
|---|---:|---:|---:|---:|---:|
|0|1|3|1|3|3|
|1|2|108|14|63|8|
|2|3|198,356|459|2,881|16|

At D=2 a selected-record exit witness has **22 retained records, 13 occupied bodies and21 construction operations**, while its maximum origin remains2. Its derived P/N/e counts are4/5/4. These are reference-construction counts, not a physical isotope or binding prediction. This witness directly falsifies the old nine-operation/ten-body restriction as an interpretation of the phase budget.

The explicit lists, Boolean families and configuration graphs for these three budgets are complete. A separate tiny resource-limited run must report incomplete; resource limits are not replaced by a claim of saturation.

## Sewing is an explicit separate obligation

Local face witnesses and root/exit reachability do **not** establish a single globally sewn coupled-field state.

The [record auditor](origin-bounded-assemblies.mjs), `auditRecordSewing`, requires an explicit five-coordinate chart identification and any asserted occurrence pairs. It checks:

- geometric vertex, role and absolute index on each declared occurrence identification;
- symbolic root-coordinate pullbacks after the declared coefficient identification;
- all five real and all five imaginary coordinate basis inputs;
- only the specified coefficient rows for a partial-slot assertion, with the other rows left unmerged.

A generic mismatch returns `explicit-input-subspace-required`, with the root-coordinate equalities listed instead of silently applying them. Equal-amplitude sample inputs can hide that mismatch and cannot establish generic sewing. Two P advances can restore the chart and coefficient map while changing origin by2; an asserted same-occurrence identification then rejects.

No identity is inferred merely because coordinates or C/M labels coincide. An ancestry-dependent assertion returns `ancestry-key-required`; the family API refuses added sewing assertions without a corresponding family/key extension. The default phase family makes **no global state-merge assertion**.

The selected-record exit test uses only this configuration's selected packets. Unselected cached alternatives do not become obligations. Historical records that actually remain selected do remain part of that declared certificate.

## What8/10 can mean

Strominger reproduced these particular reader histories:

- r=0:6 visits, C0 M0 C1 M1 C1 C2.
- r=1:8 visits, C0 M0 C1 M1 C2 M2 C2 C3.
- r=2:10 visits, C0 M0 C1 M1 C2 M2 C3 M3 C3 C4.

The repeated C is a reread of the same occurrence. The formula6+2r describes those paths, not arbitrary branching histories or revisits.

No numerical interpretation of the operator's8/10 request has been silently chosen:

- 8/10 realization advances would mean D=8/10.
- 8/10 origin layers including the seed would mean D=7/9.
- The displayed8/10-visit examples witness D=1/2, not a general definition of phase depth.

The explorer therefore labels its tested budgets explicitly as D=0,1,2. Realization origin is a grading of the reference algebra, not a derived physical clock. The earlier Pb exclusion based on nine individual attachments is withdrawn for the intended phase-budget problem; no replacement physical exclusion follows from these small validation cases.

## Artifacts and reproduction

- [Explorer](results/origin-bounded-assemblies/index.html): all enumerated configuration metadata, output-composition filters and pagination; operation-record playback keeps its counter distinct from origin grade. The branching-witness button shows the21-operation/D=2 example.
- [D0 full graph](results/origin-bounded-assemblies/D0/configurations.jsonl.gz), [D1 full graph](results/origin-bounded-assemblies/D1/configurations.jsonl.gz), [D2 full graph](results/origin-bounded-assemblies/D2/configurations.jsonl.gz).
- [D0 exact family](results/origin-bounded-assemblies/D0/family.json), [D1 exact family](results/origin-bounded-assemblies/D1/family.json), [D2 exact family](results/origin-bounded-assemblies/D2/family.json).
- [Verification](results/origin-bounded-assemblies/verification.json), [browser checks](results/origin-bounded-assemblies/browser-verification.json), [Strominger audit replay](results/origin-bounded-assemblies/strominger-audit-replay.json).

```sh
python -S research/aspect/scc/scc.py check origin-bounded-assemblies-v1
node research/nima/checkers/check_origin_bounded_assemblies_browser.mjs
```

Strominger's unmodified audit is replayed with copied input snapshots and an isolated working directory, so its relative output never writes into his research tree. Source hashes, explicit graph completion footers, full-map/occurrence counterexamples and selected-cache controls are retained in the receipt. The Boolean and explicit enumeration resource guards remain distinct.

The first full explicit audit exceeded its300-second wall-time allowance and admitted no complete receipt. After compiling the binary guards and removing redundant verification work, the fresh SCC run completed:5,688,603 labelled edges/fanouts checked across the three cases, with exact Boolean agreement and checked archive footers. Browser checks cover all198,467 configuration metadata records,160 composition filters, pagination and33 displayed operation records across the branching witnesses, including21 operations within D=2. No page errors occurred.

Only Nima-owned source files and generated outputs are changed. No owner source/receipt, publication, deployment, physical inverse law, global branch-sewing theorem, commit or push is implied.
