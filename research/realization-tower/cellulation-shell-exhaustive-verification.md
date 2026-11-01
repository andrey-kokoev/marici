# Exhaustive shell event verification

## Results

| Frozen problem | Reachable states | Complete event schedules | Distinct semantic outcomes | Coverage |
| --- | ---: | ---: | ---: | --- |
| Two-cell fork at dot 422 | 406 | 155,117,520 | 2 | Complete |
| Four arrivals in one supported octahedron | 21 | 24 | 1 | Complete |
| Whole shell | 2,000 explored | Unknown | At least 3 observed, including replayed guides | Incomplete: state limit |

The current construction is **not confluent**. A complete enumeration of all
global states is unnecessary to disprove confluence once two legal complete
traces have different results. However, the full enumeration is incomplete:
this run does **not** identify every possible global conflict.

The two-cell experiment fixes the completed `shell:t:2,1,1` prefix and allows
all action interleavings of `shell:t:3,1,2` and `shell:t:3,2,1`, not just their
two whole-cell orders. Each cell has 15 ordered local actions. The exact number
of complete schedules is `choose(30,15) = 155117520`. Their first proposals at
`422` disagree in color (red/white) and normal. Both claims are retained.
There are no deadlocks in this local graph.

The octahedral experiment fixes the canonical completed tetrahedral prefix and
admits all four incoming arrows independently. Its 24 arrival permutations
exhaust to one semantic result. This is a local result, not a certificate for
all octahedra interleaved with all other cells.

## Source-role limitation discovered afterward

The [source-role audit](../strominger/cellulation-dot-422-compatibility.md) finds
an omitted precondition: solidness is not sufficient to copy the decorated
source. The red-producing cell starts at red 312 where its source requires white;
the white-producing cell requires red 332 where the boundary is white. Both
copies fail strict role-preserving gluing. The exhaustive counts above apply to
the weaker implemented model, not to a model enforcing those omitted role gates.
The current strict planner option blocks the patch; it does not certify a repair.

## Frozen model and scope

The full specification starts at the actual completed Step 22 renderer state.
It contains 110 target cells, 120 face-specific construction programs and 1,440
possible operations. The ten extra programs are alternative constructions of
shared cells. A complete canonical trace executes 1,350 operations; unselected
shared-cell alternatives do not execute.

- All eligible cells and faces may interleave. There is no global face lock or
  whole-cell transaction lock.
- A shared cell is claimed by its first enabled construction program. Competing
  programs cannot both construct that cell. This exposes, rather than resolves,
  the existing face-order-dependent octahedral orientation.
- **The tetrahedral Steps 3–6 stage order is frozen as the local source program.**
  It is not claimed to follow from geometry alone. If the intended legal order
  space also reorders those local stages, a separately admitted specification
  is needed; this run does not cover that relaxation.
- The four octahedral arrivals independently read supported solid ring sources;
  their joint witness requires all four. The old cyclic display serialization
  is not a prerequisite.
- Candidate introduction, arrow arrival, witness, solidification, face fill and
  cell commitment are discrete semantic operations. Animation interpolation,
  display holds, idle time and neutral scaffold draw order are outside the model.
- Retained dot readings are fixed. New dots retain their first proposal, while
  **every** competing proposal and solidification witness is recorded. This is
  the existing selection policy under test, not a proposed repair.
- Arrow identity is directed endpoints plus color. Reverse arrows are distinct;
  no unagreed rule forbidding simultaneous opposite arrows is silently added.
- New face colors use the global seed-plane reading. Old faces are opaque,
  immutable boundary constants: their prior palette is not reconstructed by
  this checker, and no transition can repaint them.
- Normals use exact primitive integer directions, normalized only for display.
  The canonical full trace is checked against actual rendered arrow sets, dot
  colors, IDs and normals.

The frozen protocol validator checks local phase signatures, return paths,
unit directed edges, candidate colors/normals, two octahedral supports, four
arrivals, dot witnesses, face sets and commitment prerequisites. It rejects
missing returns, fabricated arrival serialization, reversed arrows and altered
candidate normals. This is validation of the finite geometric program, not a
physical, particle-role or operator-level certificate.

## Exhaustive algorithm

`cellulation-state-search.mjs` explores every enabled completion operation with
DFS and exact state deduplication. It uses **no partial-order reduction** and no
sampled scheduling in the exhaustive search.

Each transition completes a previously uncompleted operation. Therefore the
search graph is finite and acyclic, with path length bounded by the operation
count. Once the frontier is exhausted, every maximal trace in that frozen
problem has been accounted for. Deadlocks are reported as counterexamples to
completion, not accepted as terminal results.

The canonical state key is an exact string, not a hash:

1. Completed operation bits determine selected programs, arrow/cell sets,
   solid flags and all claim/witness multisets by union of immutable effects.
2. The boundary state is fixed for the entire search.
3. New dot first-writer selections and new face selections are included
   explicitly because they can depend on order.

Thus the key does not merge competing readings or discard witness claims.
SHA-256 is used only to identify artifact bytes, not to decide state equality.
The compiler copies and freezes its specification to prevent caller mutation.

A dynamic count of suffix paths through the completed acyclic graph counts all
complete event schedules, including paths merged by state deduplication.
This count is withheld when the frontier has not been exhausted.

Guide traces are replayed under the frozen operation guards. They reproduce
both the dot-422 conflict and the face-order-dependent arrows. They supply
counterexamples but **never** supply enumeration coverage or pruning.

## Reproduction and artifacts

```sh
node scripts/check-cellulation-shell-exhaustive.mjs
node --test tests/cellulation-state-search.test.mjs tests/cellulation-shell-exhaustive.test.mjs
```

Artifacts:

- `test-results/cellulation-exhaustive-full.json`
- `test-results/cellulation-exhaustive-twoCellFork.json`
- `test-results/cellulation-exhaustive-fourArrivals.json`
- `test-results/cellulation-shell-exhaustive-report.json`

The report binds specification hashes and source hashes, records limits and
coverage separately for each problem, and includes executable counterexample
traces. Local specifications record their completed source prefixes and retain
prefix claims. Partial-cell prefixes are rejected rather than silently reset.

The report is marked `running`/`incomplete` before search begins, so an interrupted
run cannot leave the previous result masquerading as the new result.

Default global limits: 2,000 states and 30 seconds. Override explicitly, e.g.:

```sh
CELLULATION_MAX_STATES=10000 CELLULATION_MAX_MS=60000 node scripts/check-cellulation-shell-exhaustive.mjs
```

Exit codes: **2** = counterexample found; **3** = incomplete without a
counterexample; **0** = all requested searches completed without one. A crash
is not a verification result. Passing regression tests means the checker and
its positive/negative controls passed, not that the shell is confluent.

## Unresolved

No viewer construction rule has been changed by this work. A new shared-witness
resolution rule is still required. Merely increasing the search limit or fixing
one deterministic schedule cannot remove the already proved order dependence.
