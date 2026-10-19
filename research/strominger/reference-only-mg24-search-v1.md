# Neutral Mg-24: bounded native search unresolved

## Update: equivalent encoding completes origin 9

The [solver benchmark](reference-solver-benchmark-v1.md) reran the identical saved origin-9 input using an equivalent SCC-local bit-vector reachability encoding. With the same Z3 version, seed 0 and 120-second budget, it returned **UNSAT in 69.877 seconds**. Completed negative bounds therefore extend **through origin 9**; origin 10 remains untested. No Mg-24 witness has been found.

The original timeout receipt below is preserved unchanged. The new result is in `results/reference-solver-benchmark/mg24-D9-scc-bv-seed0-120000ms.json`, with an equivalence argument, exhaustive small-instance checks and receipt audit. It is not an independently certified formal UNSAT proof. No isotope, contact or native-transfer rule changed.

## Original baseline run: target and outcome

Target: **12P/12N/12e**, using the unchanged native reference grammar, fixed canonical root and original subdivision. No experimental reference-mediated PE constructor was enabled.

No witness was found in this run. Maximum origins 3 through 8 returned UNSAT. At origin 9, Z3 returned UNKNOWN after its 120-second solver budget, with reason `timeout` and reported solver time 120.030 seconds. The runner stops on SAT or UNKNOWN, so origin 10 was not queried.

| Maximum origin | Complete packet universe | Result |
|---|---:|---|
| 3 | 87 | UNSAT |
| 4 | 192 | UNSAT |
| 5 | 372 | UNSAT |
| 6 | 660 | UNSAT |
| 7 | 1,086 | UNSAT |
| 8 | 1,698 | UNSAT |
| 9 | 2,541 | UNKNOWN: timeout |

The origin-8 solver time was 93.875 seconds. No incomplete packet universe was submitted to the solver.

## Unchanged constraints

The query preserves exact body/species counts, pairwise context and contact guards, actual native witnesses for occupied face contacts, rooted construction and electron-exit reachability for every selected reader record. It uses the existing target-constraint solver with Z3 5.3.1 and random seed 0.

This is an independent Mg-24 target search, not a requirement to extend or retain the saved Na-23 configuration. The preceding Na-23 result remains unchanged.

## Interpretation and next test

These finite solver negatives are not independently checked formal UNSAT proofs or an unbounded impossibility theorem. The origin-9 timeout supports neither existence nor nonexistence. Nothing here contradicts the known physical stability of Mg-24 or derives a binding/stability prediction from the construction grammar.

The original run left origin 9 unresolved. The equivalent-encoding follow-up above completes that bound without increasing its solver budget. **Origin 10 is now the next untested bound**, not a completed negative. No contraction rule, root, subdivision or contact law should be changed silently to obtain a positive result.

The fresh-process replay checker has been prepared but was **not run**, because there is no witness to replay. No viewer option or production admission was added.

## Evidence and reproduction

```
node research/strominger/checkers/search_reference_mg24.mjs
```

Evidence: `research/strominger/results/reference-mg24-search/verification.json` and its per-bound input, solver and verification receipts. In particular, `D9-input.json` preserves the unresolved finite query and `D9-solver.json` records its timeout.

After a future positive search, replay with:

```
node research/strominger/checkers/check_reference_mg24.mjs
```

The planned replay validates source hashes, regenerated packets/charts, body coordinates, every construction prefix, exact counts, direct vertex-based face contacts and reverse-BFS exit reachability. It does not replace the missing witness in this run.
