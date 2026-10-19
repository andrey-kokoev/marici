# Origin-lifted obstruction repairs — net iteration7

Targeted source search resolves all nine cases: **eight D2 obstruction cores complete at D3; one remains impossible at D3**. No full D3 atlas or target-membership lookup was used.

| Retained D2 core | D3 result | Counts P/N/E | Retained records | Construction operations |
|---|---|---|---:|---:|
|14|certified|1/2/1|6|5|
|3,18|certified|1/3/1|9|8|
|4,7|certified|1/2/2|8|7|
|4,19|certified|1/3/2|11|10|
|7,18|certified|1/2/2|9|8|
|13,18|impossible at D3|—|—|—|
|16,9|certified|3/4/3|21|20|
|18,19|certified|1/3/1|8|7|
|9,10|certified|3/4/3|20|19|

All eight positive witnesses have maximum origin exactly3. Their D2 impossibility certificates establish that3 is the minimum origin for a completion retaining each core. Saved witnesses are minimal under single optional-record deletion; global minimum record/body/operation counts were not searched.

These searches retain each complete marked **core**, while other packets are free choices. They do not assert that every full D2 configuration containing that core can be repaired by additions.

## Source-guided search

Each core is mapped into the D3 universe by cell key, species, full reference aliases, absolute origin and five-coordinate map. Search alternates:

- direct inspection of the current selected set for a certificate;
- optimistic source elimination of impossible optional packets;
- selected/absent branching, prioritized toward incoming routes to stranded readers and outgoing routes from readers lacking exits.

It stops on a source-checked certificate, a complete contradiction tree, or an explicit resource bound. All nine searches finished in7–24 search nodes; none reached its50,000-node or60-second guard. Node/time-stop controls return incomplete.

For every positive case, optional records were removed only when the full source certificate survived. The final construction was replayed from the root with compatible, rooted prefixes. The receipt preserves all native/PE factors, active origin3 interfaces, and an exit path for every mandatory core reader.

## The persistent NN obstruction

Core `[13,18]` consists of two origin2 neutron records on adjacent cells8 and12. The initial search returned a complete15-node,8-leaf contradiction tree. A subsequent forced-support analysis compresses it:

1. If packet1 is absent, the mandatory core cannot be rooted; packet1 is therefore required.
2. With packet1 retained, absence of packet4 blocks rooting; packet4 is therefore required.
3. With `[root,13,18,1,4]` selected, the mandatory NN face between cells8/12 has no possible native witness in the D3 universe.

The proof retains the candidate native factor IDs31,32,43,44 and the source elimination trace. This is a coupled entry-support/contact obstruction, not just a missing terminal electron.

The eight positive cases demonstrate genuine depth repair. The ninth demonstrates why surviving optimistic reachability alone was insufficient: optional connections can look adequate before the root-support consequences are imposed.

## Next test

Probe the persistent NN core at D4. Enumerate the candidate witnesses of its shared face, record exactly how each interacts with forced incoming support, and seek a certified extension or a source contradiction. This determines whether the remaining blockage is another depth threshold or a more persistent structural conflict.

## Artifacts

[Source-guided search](guarded-extension-search.mjs) · [Checker](checkers/check_origin_lifted_repairs.mjs) · [Witnesses, proof tree, forced-support explanation and registry](results/origin-lifted-repairs/verification.json)

```sh
node research/nima/checkers/check_origin_lifted_repairs.mjs
```
