# Marked four-source fibers to four L1 stars

## Positive finite correspondence

The executable candidate consumes the actual initial twelve rows of `results/two-ended-sector-trace.json`, rather than a new 12-element fixture. A row retains `(label,source,target)` with source != target on four marked endpoints.

Assign source index s to displayed star s. Assign its three outgoing rows to satellite arms by `(sourceIndex XOR targetIndex)-1`. This arm order is an explicit presentation convention. Transporting endpoint labels AND the marking preserves all node assignments across all 24 permutations. It is not a claim that arbitrary endpoint permutations are rigid spatial symmetries of the square support.

The same construction works for L1 and L1′. It is bijective on the twelve satellite addresses, preserves arbitrary supplied row payloads by value, retains the supplied history, and reconstructs the source table. Payload retention is not a new typed full-field transport theorem.

## What a centre can represent

Source and target fibers are different:

| Star key | Source fiber: outgoing rows | Target fiber: incoming rows |
|---|---|---|
| 0 | 0→1, 0→2, 0→3 | 1→0, 2→0, 3→0 |
| 1 | 1→0, 1→2, 1→3 | 0→1, 2→1, 3→1 |
| 2 | 2→0, 2→1, 2→3 | 0→2, 1→2, 3→2 |
| 3 | 3→0, 3→1, 3→2 | 0→3, 1→3, 2→3 |

A centre may expose a fiber key and the retained three-row packet; it is not an additional sector row. Interpreting the opposite-side receiving centre as the target fiber is a candidate boundary interface. It must not be confused with the three satellites of that centre's own source star. Neither interpretation alone establishes the physical meaning of its opposite-colour arrow.

A sum of the three values is insufficient: the explicit nonzero input (1,-1,0) has zero sum. Full row packets/history must survive if recovery is required. The adapter records both grouping references rather than silently selecting a physical return law.

## Current wiring: connectivity succeeds, addressed transport is missing

For each of the twelve source satellites, independently propagate one normalized scalar input through the current directed graph with equal outgoing splits. In both directions, each source contributes exactly 1/4 to EACH of the four opposite minority centres.

The resulting scalar transfer is a 4×12 matrix with every entry 1/4, rank one. Uniform input gives three units at every receiving centre, which explains why the previous steady-flux balance test passes. It does not demonstrate target-address preservation.

Every row's marked target is reachable, so the graph does not obstruct addressed delivery. A candidate target demultiplexer would send row (s,t) only to receiving centre t, retaining row payload and all route witnesses. Its scalar target matrix has three ones in each row, with disjoint supports (rank four), and still produces centre fluxes (3,3,3,3) on uniform inputs. This scalar matrix is only an accounting projection; a lossless implementation must store the three individual row packets, not just those four totals.

The existing L2/L2′ common junctions provide routes to all four destination centres. A label-aware exit can therefore be investigated without moving arrows or adding edges. If the upstream three paths carry repeated presentations of one packet, retain shared packet identity and route weights; do not count them as three independent fields.

## Scope and next binding

No production wiring or boundary adapter was changed. This is a tested presentation codec and graph reachability/transfer audit. The proposed demultiplexer is not installed, no actual parent face has been selected, and the native 44-coordinate field maps and their readout squares have not been bound to these belt nodes.

The meaningful next experiment is addressed full-packet transport over this graph, using the existing marked-table/history machinery and checking source/target regrouping and recovery. That remains distinct from proving the 1+4×28+1 global construction or mechanical stability.

## Reproduce

- `node scripts/audit-belt-source-fibers.mjs`
- `node --test tests/belt-source-fiber-binding.test.mjs`
- Receipt: `results/belt-source-fiber-binding.json`
- Model: `../realization-tower/belt-source-fiber-binding.mjs`

Four new test groups cover prior-fixture agreement and payload recovery, all 24 marked relabelings and hostile controls, both current scalar transfer matrices and intended target reachability, and loss under fiber summation. Fifteen combined binding/wiring/flux tests pass.
