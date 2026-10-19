# Neutral Na-23 under the unchanged native grammar

## Result

A neutral **11P/12N/11e** construction passes at maximum realization origin **5**. The bounded search returned UNSAT at caps 3 and 4, then SAT at cap 5 and stopped.

No experimental reference-mediated P/E constructor was used. The canonical root, original subdivision, native transfer/phase rules, reference-geometry policy and occupied-contact requirements were unchanged.

| Maximum origin | Complete packet universe | Solver result |
|---|---:|---|
| 3 | 87 | UNSAT |
| 4 | 192 | UNSAT |
| 5 | 372 | SAT |

The saved witness has:

- 34 occupied bodies: 11 protons, 12 neutrons and 11 electrons;
- 74 selected reader records;
- 73 rooted construction operations;
- 40 occupied triangular face contacts, each with a selected native operation witness;
- native electron-exit reachability from every selected record.

Reader records and construction steps are not additional particles.

## Fresh replay

A separate process regenerates the bounded universe without Z3. It checks the saved input/source hashes, packet and chart identities, native operations, exact body coordinates, isotope counts and every rooted construction prefix.

It independently enumerates occupied face contacts by vertex equality rather than using the generator's neighbor/contact enumeration, and checks exit reachability by reverse BFS rather than solver rank values. The whole configuration also passes the original `inspect` gates.

This replay shares the original generator and geometry; it is not an independently derived physical model or a formal UNSAT certificate.

## Relation to the preceding isotope work

Na-23 is the next stable-isotope target after the tested Ne-22 reference. Its neutral counts add one P and one E while keeping twelve neutrons. The search is nevertheless an **independent target search**: it does not require retaining the saved Ne-22 configuration or prove a Ne-22->Na-23 growth sequence.

The success is native and does not depend on the experimental PE rule used in the earlier N-14 and Ne-21 deletion repairs. Those experimental results retain their separate status.

## Bounds and physical scope

This is a local construction certificate, not a derivation of sodium's physical stability, binding energy, spin, global coupled-field sewing or synthesis dynamics. The maximum origin is a realization bound, not physical time or operation count.

The negative bounds are solver results, not independently checked formal UNSAT proofs. No unique geometry or minimum-reader witness is claimed. No production or viewer option was changed by this search.

## Evidence and reproduction

```
node research/strominger/checkers/search_reference_na23.mjs
node research/strominger/checkers/check_reference_na23.mjs
```

Evidence: `research/strominger/results/reference-na23-search/verification.json`, `D5-verification.json` (full witness), per-bound input/solver receipts, and `replay-verification.json`.

The search uses the existing `solve_reference_n14.py` target-constraint solver with Z3 5.3.1, random seed 0 and a 120-second per-query solver budget. It stops on its first positive witness or unresolved solver outcome. Existing isotope receipts are unchanged.
