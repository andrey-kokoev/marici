# Native-face closure of materialization failures — net iteration12

This test retains the entire selected packet set of every rejected body materialization. It distinguishes two different failures: a native witness that has not yet been selected, versus a retained marked core that no D2 extension can repair.

## Method

1. Deduplicate the70 rejected candidates by complete selected packet set, retaining their source-macro mappings.
2. Recheck compatibility, rootedness and exit reachability, and identify missing native contact witnesses.
3. Replay all nine bounded source obstruction certificates, including complete selected/absent split proofs and source hash checks. A contained certified core proves the entire candidate impossible at D2.
4. For the remaining candidates, run guarded source extension search with5,000-node/5-second per-case limits. Retain the entire candidate, then remove optional records only if the final source certificate survives.
5. Record selected native factors witnessing each previously missing face. Check singleton schedules within the repaired target; an atomic final certificate is not silently called a singleton path.
6. Only afterward, read the complete D2 target family and compare certified-superset membership with each source classification.

Resource limits remain incomplete outcomes, not obstruction certificates. Subset proofs are bound to D2 and must not be reused at higher origins.

## Result

**All70 candidates are repairable at D2**. There are70 distinct selected sets, no contained certified obstruction cores, no unsatisfiable results and no resource stops. Each source-produced completion retains the entire materialized selection, supplies the missing native witness and admits a compatible rooted singleton schedule. Independent final-family comparison agrees in every case.

All failures concern exactly one **PN face**, in three locations:

| Missing contact | Cases | Native reader pair supplied |
|---|---:|---|
|cells0/2|42|P2 ↔ N6|
|cells2/5|26|P20 ↔ N51|
|cells1/5|2|N5 ↔ P16|

The endpoints here are packet IDs, not species counts. The source checks preserve their full chart, occurrence and map data.

Two compact support templates suffice for all70 cases:

- For face0/2, add the missing members of `[2,6,8]`: P1→N1→E1 at the corresponding marked readers.
- For faces2/5 or1/5, add the missing members of `[1,5,16,20,51,53]`: the rooted native chain N0→N1→P1→P2→N2→E2.

Subscripts in these two descriptions are absolute origins. The root P0 is already selected. Both templates include downstream exits, not merely the two face endpoints. They were checked against every applicable selected set before opening the target family. Their listed order gives a rooted singleton replay. Actual additions number2 in4 cases,3 in64 cases and6 in2 cases; these are compact validated templates, not claims of minimum size. The independently reduced search witnesses can be smaller.

The70 rejected macros were therefore **incomplete contact closures, not bounded impossibilities**. They must not be pruned as dead solely because the immediate result lacks a face witness. Materialization and contact closure are separate construction obligations.

## Remaining frontier

Replace these bounded packet-ID templates with an interface-driven contact-closure planner: choose native factors from a missing face, then propagate incoming and exit obligations with guard-aware scheduling. Test on materializations of the eight previously certified D3 core repairs, where the interfaces and support differ from the D2 family. This is executable new work; no general higher-origin completeness claim is made here.

## Artifacts

```sh
node research/nima/checkers/check_materialization_face_closure.mjs
```

[Checker](checkers/check_materialization_face_closure.mjs) · [Source classifications and closures](results/materialization-face-closure/verification.json)
