# Neutral Ne-21: bounded search unresolved

## Budget-only retry update

The identical origin-9 input was retried with a 600-second solver budget,
Z3 5.3.1 and the same random seed. It returned **UNSAT** after 174.587 solver
seconds (178.712 seconds overall). The original input, solver and summary
receipts were hash-checked and preserved. Thus completed negative bounds now
extend **through origin 9**. Origin 10 remains untested; this is still not an
unbounded or physical impossibility result. No viewer option was added.

Retry evidence: `results/reference-ne21-search/origin9-600s/verification.json`.
Reproduction: `node research/strominger/checkers/retry_reference_ne21_origin9.mjs`.

## Original 120-second run

Target: **10P/11N/10e**, with the unchanged reference-only-proton grammar,
canonical root, original uniform subdivision and original contact/exit rules.

No witness was found in this run. Origins 3 through 8 returned UNSAT. At origin
9 the finite packet universe completed, but Z3 returned UNKNOWN after its
120-second solver limit (`unknownReason: timeout`, elapsed 120.037 seconds).
Origin 10 was not queried: the runner stops on unknown or a positive witness.

| Maximum origin | Complete universe packets | Result |
|---|---:|---|
| 3 | 87 | UNSAT |
| 4 | 192 | UNSAT |
| 5 | 372 | UNSAT |
| 6 | 660 | UNSAT |
| 7 | 1,086 | UNSAT |
| 8 | 1,698 | UNSAT |
| 9 | 2,541 | UNKNOWN: solver timeout |

The query retains exact particle counts, pairwise context/species/contact
guards, actual operation witnesses for occupied contacts, rooted construction
and selected-record E-exit reachability. It does not require retaining a Ne-20
prefix. No subdivision or transport/contact law was changed.

These finite solver negatives are not independently checked formal UNSAT proofs
or an unbounded impossibility claim. The origin-9 timeout supports neither
existence nor nonexistence. No global field sewing or physical binding/stability
conclusion follows. This search does not contradict the experimental stability
of neon-21.

No Ne-21 viewer option was added because no passing witness exists in this
run. A fresh replay checker was prepared but has no witness to check and was
not run. Earlier isotope selectors and receipts remain unchanged.

## Evidence and reproduction

- `results/reference-ne21-search/verification.json`: bounded search summary,
  target and source hashes;
- per-bound inputs, solver receipts and verification files in that directory;
- `D9-solver.json`: actual UNKNOWN/timeout receipt.

```sh
node research/strominger/checkers/search_reference_ne21.mjs
```

After the budget-only retry above, the next untested bound is origin 10.
The original timeout receipt remains unchanged for provenance.
