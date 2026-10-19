# Guarded interface composition — synthesis iteration2

The registered D0/D1 critical-pair test is complete. An interface-record interpreter predicts occupied support, global roles, native face witnesses, active connections and root/exit reachability without calling the generator's configuration inspector. Every prediction agrees with direct source auditing.

## Complete tested families

| D | Base configurations | One-packet extensions | Two-packet extensions | Both insertion orders | Exactly one order | Neither order |
|---|---:|---:|---:|---:|---:|---:|
|0|4|4|1|1|0|0|
|1|136|784|2082|413|160|1509|

Every extension uses packets absent from its base configuration. Order counts concern rooted compatible construction prefixes, not a requirement that each prefix already have an exit certificate. There are no rooted final two-addition states for which both insertion orders fail in this tested domain. The graph retains distinct admitted histories even when they end at the same selection.

The checker audited946 distinct depth-indexed selected sets (4 at D0,942 at D1), all788 one-addition incidences and2083 two-addition incidences. It also checked associativity of full coefficient permutation composition on35 endpoint-matched interface triples. Associativity of maps and admissibility of occupied support are separate checks.

## The composition rule

An interface is active when:

1. Its endpoint packets are selected.
2. Its required occupied sites are present.
3. Its required vacant sites remain empty.
4. None of its forbidden selected successors is present.

Upon a packet addition, only interfaces watching that packet as an endpoint, forbidden successor, or occupant of a required-vacant site need their activity recomputed. This incremental update exactly matches full interface re-evaluation for every tested extension and both insertion orders. Global compatibility and graph reachability are then checked on the updated environment.

This gives a usable synthesis primitive: **update affected connections, then decide whether the assembly remains rooted**. Rejecting every extension that disables a shortcut would discard valid constructions.

## Small structural obstruction records

At D1,30 additions disable a selected PE shortcut. All30 remain geometrically/role compatible. In28 cases root connectivity survives through other routes; in2 it fails. Four distinct interface/trigger pairs explain the disablements:

- selected native intermediate N: both vacancy and successor guards fail;
- selected same-body P advance: successor guard fails;
- a different N packet on the reference N body: vacancy guard fails;
- the analogous selected intermediate N for the next-origin P reader.

Each record stores the endpoint pair and a single triggering packet. Removing the trigger restores eligibility. Separate mutations omitting either vacancy or successor conditions produce false eligibility and are rejected by the comparison.

All incompatible extensions contain a two-packet obstruction. Four distinct minimal pairs occur at D1: one occupied-cell species conflict and three forbidden face contacts. The checker verifies each singleton is compatible and the pair is incompatible. No higher-order compatibility obstruction is needed in this domain; connectivity still requires the full graph.

## A concrete ordering example

Using D1 registry IDs:

- Start with packets `[0,3]`: P and E connected by the experimental shortcut.
- Add N packet1 first: native P→N→E replaces the shortcut and preserves the exit certificate.
- Add P-advance packet2 next: the configuration remains rooted; packet2 still needs an exit continuation.
- Reverse the first two additions: `[0,2,3]` disables P→E before its replacement exists, leaving E unrooted.

The final set `[0,1,2,3]` is rooted in either description, but only the N-first insertion order has admissible prefixes from that starting state. This is why synthesis must track available connections, not merely final occupied sites.

## Evidence and next test

[Checker](checkers/check_pne_guarded_composition.mjs) · [Receipt, interface tables and obstruction examples](results/pne-guarded-composition/verification.json)

```sh
node research/nima/checkers/check_pne_guarded_composition.mjs
```

Three negative controls reject stale active-interface caching and omission of either vacancy or successor guards. The predictor consumes the saved path catalog and serialized source records; direct validation uses the existing generator separately.

Next: use the tested interface activity update and obstruction records to build an **interface-driven D2 generator**, then compare its complete family against the existing guarded Boolean model and direct audits. This tests whether the interface calculus can construct the atlas, rather than merely describe its entries.
