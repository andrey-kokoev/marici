# Neutral N-14 under the prior reference-only-proton grammar

## Result

**No neutral 7P/7N/7e reference was found through absolute realization origin
10 in the unchanged prior generator.** The finite-universe constraint solver
returns UNSAT at every tested bound; no solver timeout or packet cap occurred.
This is a bounded result, not an unbounded or physical impossibility theorem.

A charge-control search using the same origin-10 universe and the same contact,
construction and exit rules, but leaving the electron count unspecified, does
find a **7P/7N/5e reference** (formal N-14++). Its selected records were replayed
successfully through the original generator. Thus a 7P/7N nucleus remains
possible under this broader grammar, while neutrality is still obstructed
within the tested origin budget.

## What changed from the earlier isotope search

This probe imports Nima's existing `GenerativeAssemblyRules` through
`phaseUniverse`, without changing either source:

- reference proton geometry for an N reader need not be occupied;
- regular and split E targets are both allowed by their actual native window;
- honeycomb cells are generated locally, not restricted to the original list
  of 343 cells;
- the canonical marked proton root and supplied octahedral subdivision stay
  fixed;
- all five reference coefficients, explicit packet origins/permutations,
  global context-role consistency and actual contact witnesses are retained.

There is no retained C-13 or earlier isotope prefix. The target fixes only the
occupied particle counts. No octahedral neutron body, E/E contact exception or
new transition was introduced.

## Search method

`phaseUniverse` completes the existing finite origin-bounded packet universe.
Boolean variables select retained packets. The targeted constraints require:

1. The canonical root packet is selected.
2. Pairwise occupancy/species/context-role/contact guards agree with the
   original `describe` function.
3. Exactly seven occupied bodies of each species, counting cells rather than
   packets (multiple readers do not become multiple particles).
4. Every selected packet is reachable from the root through selected, validated
   source operations.
5. Every selected packet can reach a selected E exit.
6. Every occupied physical face contact has an actual selected operation
   witnessing that contact.

Root/exit reachability is encoded with bounded integer ranking witnesses.
Strictly decreasing distances provide finite paths; merely selecting an
unrooted PN cycle or an E elsewhere cannot satisfy the constraints. These
rank witnesses are graph encodings, not physical times or origin resets.
Every SAT witness must reconstruct a compatible construction word and pass the
original whole-configuration `inspect` function before being reported.

There are no imposed global cross-branch occurrence/field identifications.
As in the prior generator, local exit certification is not a generic globally
sewn quantum state, binding criterion or physical stability calculation.

## Completed neutral target bounds

| Maximum origin | Complete packet universe | Solver result |
|---|---:|---|
| 3 | 87 | UNSAT |
| 4 | 192 | UNSAT |
| 5 | 372 | UNSAT |
| 6 | 660 | UNSAT |
| 7 | 1,086 | UNSAT |
| 8 | 1,698 | UNSAT |
| 9 | 2,541 | UNSAT |
| 10 | 3,651 | UNSAT |

The origin cap is not an operation count or a final-C-index cap. Local
reference/lookahead geometry beyond occupied bodies remains available. Lower
origins are included in each larger universe. Resource limits were explicit:
5,000 packets and a 120-second solver timeout per query. All queries completed.

## Positive control with electron count free

Keeping P=N=7 and all original certificate constraints at origin cap 10, while
omitting only the E cardinality constraint, yields a locally certified model
with **five electrons**. It has maximum origin 10 and 180 selected records.

The actual count, original-rule inspection, rooted construction word, full
packets, charts, body coordinates and selected operations are saved. Every
construction prefix is checked against the unchanged global role/contact
guards. This is one charged witness, not a minimal-depth, minimum-record or
maximum-electron result. It does not classify all possible charge states.

This control shows the neutral-target failure is not simply “the solver cannot
make seven protons and seven neutrons”. It does not isolate a single remaining
rule as the explanation for failure at seven electrons.

## Independent small-case crosscheck

A fresh complete origin-1 enumeration has **108** configurations. All 26 derived
composition profiles were queried through the targeted solver encoding and
compared with the enumerator's actual exit-certification results. Additional
impossible-target controls were included. All **28 queries agree**; every SAT
selection also appears in the explicit configuration list and passes original
`inspect`.

The large-bound UNSAT results are Z3 solver results, not independently replayed
formal UNSAT proofs. The small exhaustive comparison and exact source guards
reduce encoding risk but do not turn them into an unbounded theorem.

## Disposition

The prior reference-only-P convention is genuinely broader than our old isotope
ansatz and worth recovering. Nevertheless it does **not** resolve neutral N-14
within the tested origin budget. Further possibilities remain separate:
alternative subdivisions, larger origin budgets, another justified electron
representation, or a source-supported whole-body constructor. None was silently
substituted in this run.

Production selectors, viewer options and other-owner source/receipt files were
not changed. The new N-14++ witness is diagnostic evidence only, not a viewer
admission or simulated synthesis process.

## Reproduction

Requires Node, Python and `uv`; the solver command uses `uv run --with z3-solver`
and records the actual Z3 version in each solver receipt.

```sh
node research/strominger/checkers/search_reference_n14.mjs
node research/strominger/checkers/check_reference_n14_search.mjs
node research/strominger/checkers/check_reference_n14_charge_control.mjs
```

Evidence under `results/reference-n14-search/`:
- `verification.json`: source fingerprints and completed neutral search bounds;
- `D*-input.json`, `D*-solver.json`, `D*-verification.json`: explicit finite
  constraints and per-bound outcomes;
- `crosscheck.json`: complete small-case comparison;
- `charge-control-verification.json`: revalidated 7P/7N/5e witness and word.
