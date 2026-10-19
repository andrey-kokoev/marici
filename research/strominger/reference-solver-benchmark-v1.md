# Native reference solver: equivalent encodings and measured improvement

## Result

The baseline was correct but incurred avoidable arithmetic work for reachability. On the tested archived inputs, ranks restricted to strongly connected components (SCCs), encoded as small unsigned bit-vectors, improve performance substantially.

Most importantly, the unchanged Mg-24 origin-9 query now returns **UNSAT in 69.877 seconds** with a 120-second solver budget. The original baseline timed out at that budget. This is a new completed bounded solver result, not a formal UNSAT proof or a physical impossibility claim. Origin 10 remains untested.

The production solver and all archived inputs/receipts are unchanged. The alternate solver is an explicit research tool; it has not silently become the default search backend.

## Fair comparison setup

The primary benchmark uses five saved inputs:

- Na-23 origin 5 (known SAT);
- Mg-24 origins 5, 7 and 8 (known UNSAT);
- Mg-24 origin 9 (previously UNKNOWN).

All five encodings run sequentially in fresh worker processes, Z3 5.3.1, seed 0, with the same 30-second solver budget. Parsing, Python constraint-build time, solver time and worker wall time are recorded separately. Full solver statistics and input/source hashes are retained.

The instrumented baseline preserves the production encoder's variable names, assertion order and set iteration. The equivalence checker constructs the actual production encoder from its AST, stopping before execution of its query/output code, and verifies structural equality of every assertion on the saved Na-23 input. The different timeout is an explicit benchmark parameter, not a constraint change.

The benchmark uses archived input JSON. Universe generation and contact-table generation are not included in these timings; incremental bound reuse is not implemented here.

## Encodings

1. **baseline:** original global integer entry and exit ranks.
2. **pruned-int:** safe preprocessing, followed by global integer ranks.
3. **scc-int:** preprocessing and integer ranks only within SCCs.
4. **scc-bv:** the same SCC-local logic using unsigned bit-vectors.
5. **scc-cuts:** Boolean subset-cut constraints inside each SCC, without rank variables.

Every variant retains the exact species counts, body definitions, pair conflicts, root requirement, exit requirements and occupied-contact witness clauses.

### Safe preprocessing

- A packet conflicting with the mandatory root cannot be selected.
- A native edge whose endpoints conflict cannot occur in a selected graph.
- A selected packet must be reachable from the root and able to reach an exit in the remaining full graph. Those failing either necessary condition can be fixed false.

All original variables, body-count formulas and contact clauses remain present; removed packets are fixed false. This avoids silently changing how multiple readers count as one occupied body.

If a valid selection existed, none of these removals could remove one of its required paths. Thus this preprocessing preserves the set of valid selected packet sets. It does not solve pair compatibility or isotope counts by itself.

### Why SCC-local ranks are equivalent

Condensing the available directed graph into SCCs produces a DAG. A predecessor/successor chain can cycle only inside one SCC.

For root reachability, each selected non-root reader must have a selected predecessor. If that predecessor is inside the same SCC, require a strictly lower local entry rank. If it is outside, no rank comparison is needed: the component DAG already prevents a cycle of such dependencies. Following predecessors therefore terminates at the root. The exit construction is the corresponding successor argument, terminating at a selected exit.

Conversely, if the selected graph satisfies the original reachability conditions, take shortest paths within each SCC from its selected entry points and toward its selected exit points. Their ranks are bounded by the SCC size minus one. They satisfy the local constraints, even when the selected subgraph splits a full-graph SCC into smaller pieces.

Singleton SCCs need no rank variable; self-loops cannot justify progress. A component of size k uses ceiling(log2(k)) bits, with an explicit upper bound when k is not a power of two. Comparisons are unsigned strict comparisons, not modular differences, so wraparound cannot justify a path.

All SCCs in these native benchmark graphs have size at most two. Thus the remaining rank variables are one-bit values rather than broadly bounded integer values.

### Boolean subset cuts

For every nonempty subset T of an SCC, require that any selected vertex in T has at least one selected incoming edge from outside T, unless T contains the root. Impose the dual outgoing requirement unless T contains an exit.

A closed selected component without the root or an exit violates one of these cuts. The component DAG prevents a global cycle between SCCs. This yields another equivalent finite encoding, but subset enumeration is exponential in SCC size; the implementation refuses components larger than twelve. This cap is an encoding resource limit, not an UNSAT answer.

## Correctness checks

The equivalence audit exhaustively tests all 64 selections on ten small graphs across all five encodings: **3,200 solver/graph comparisons**. Fixtures include cycles, self-loops, disconnected components, conflicting endpoints, multiple readers per body and contact-witness clauses. A direct Boolean/count/graph checker supplies the expected result, without rank variables or Z3. Eight distinct selections satisfy those fixtures.

Every positive benchmark assignment is also checked directly against the archived input. All five Na-23 witnesses are then rebuilt in separate Node processes using the original native generator, validating counts, rooted construction and every prefix, selected operations, direct vertex-based occupied contacts and reverse-BFS exit reachability.

The written equivalence arguments establish the intended transformation. These finite implementation checks are not a proof-assistant verification, and the negative solver outputs do not have independently checked UNSAT certificates.

## Primary results

Solver seconds, seed 0, common 30-second budget:

| Input | Baseline | Pruned integer | SCC integer | SCC bit-vector | SCC cuts |
|---|---:|---:|---:|---:|---:|
| Na-23 D5, SAT | 0.094 | 0.098 | 0.058 | 0.041 | 0.026 |
| Mg-24 D5, UNSAT | 0.113 | 0.124 | 0.077 | 0.049 | 0.047 |
| Mg-24 D7, UNSAT | 20.156 | 24.626 | 16.698 | 5.026 | 7.367 |
| Mg-24 D8 | timeout | timeout | timeout | timeout | timeout |
| Mg-24 D9 | timeout | timeout | timeout | timeout | timeout |

Timeouts are censored observations—not estimates of completed runtime and not new negative results. Safe pruning alone was slower on D7 despite producing a smaller active graph. Removing variables does not guarantee better search heuristics.

On D7, the baseline worker wall time was 21.527 seconds versus 6.161 seconds for SCC bit-vectors; the gain is not merely hidden setup overhead. Encoding time was approximately 1.20 versus 0.97 seconds.

## Seed and longer-budget checks

At D7, seed 1 gave baseline **20.838 s** and SCC bit-vectors **6.878 s**, confirming an improvement on a second seed without claiming seed-independent performance.

At the original 120-second budget, SCC bit-vectors gave:

| Mg-24 input | SCC bit-vector result | Solve time | Build time | Archived baseline |
|---|---|---:|---:|---|
| D8 | UNSAT | 32.664 s | 1.813 s | UNSAT, 93.875 s |
| D9 | UNSAT | 69.877 s | 3.269 s | UNKNOWN after 120 s |

The baseline D8 comparison is to its archived run, not a fresh paired 120-second benchmark. The controlled D7 comparisons are the stronger direct speed measurements.

### What the statistics suggest

For D7 seed 0:

| Statistic | Baseline | SCC bit-vector |
|---|---:|---:|
| Conflicts | 202,320 | 183,189 |
| Decisions | 275,091 | 252,683 |
| Arithmetic columns | 4,841 | 4 |
| Z3-reported maximum memory | 72.07 MB | 42.89 MB |

The search still performs substantial Boolean/pseudo-Boolean work, but arithmetic overhead is sharply reduced. These statistics support that explanation; they do not uniquely identify every bottleneck.

At D9 the preprocessing removes only 60 of 2,541 packets. The SCC bit-vector variant has 3,352 one-bit rank variables versus 5,082 original integer ranks. The main gain is not wholesale removal of the universe.

## Operational recommendation

Use SCC bit-vectors as an explicitly selected candidate backend for the next bounded search, keeping original semantics, input hashes and fresh witness replay. Keep the original solver available as a reference; do not claim the new variant is universally fastest from these five inputs.

No broad parameter tuning, incremental solver reuse, universe-generation optimization or physical rule change was performed. Incremental reuse across expanding universes requires care: predecessor/exit clauses referring to a smaller universe cannot simply remain frozen when new support becomes available.

## Reproduction

Primary comparison and equivalence audit:

```
uv run --with z3-solver==5.3.1 python research/strominger/checkers/run_reference_solver_benchmark.py
```

One bounded alternate query (the recorded origin-9 follow-up):

```
uv run --with z3-solver==5.3.1 python research/strominger/checkers/benchmark_reference_solver.py --input research/strominger/results/reference-mg24-search/D9-input.json --output research/strominger/results/reference-solver-benchmark/mg24-D9-scc-bv-seed0-120000ms.json --mode scc-bv --timeout-ms 120000
```

Receipt verification without rerunning the timed searches:

```
python research/strominger/checkers/check_reference_solver_benchmark.py
```

Evidence directory: `research/strominger/results/reference-solver-benchmark/`. The primary manifest is `benchmark-30000ms-seeds-0.json`; the four follow-up files separately retain the second-seed D7 pair and the 120-second D8/D9 results. Earlier pilot files are exploratory and excluded from the primary/follow-up audited set. Original isotope timeout receipts remain unchanged.
