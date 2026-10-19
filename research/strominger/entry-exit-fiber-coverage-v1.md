# Entry–exit coverage on retained window states

## Tested condition

Every required cell must have at least one admitted state reachable forward
from entry **and** backward from exit:

```
F = forwardReach(entry states)
B = reverseReach(exit states)
covered cells = projectToCells(F ∩ B)
```

The intersection occurs before projection. Two different windows or phases at
the same geometric cell cannot supply separate halves of an invented route.
Reverse traversal is an analysis of existing edges, not an electron-to-proton
operation. Exit states have no forward continuation. Branching is permitted;
one fiber need not visit every cell.

`fiber-coverage-model.mjs` separates two responsibilities:

- `auditStateCoverage`: reachability on a caller-supplied admitted state graph.
  It does not certify that arbitrary supplied edges are physical transitions.
- `windowPrefixGraph`: strict admission adapter for the implemented window
  constructor. It replays only the committed prefix and checks its geometry,
  ordered windows, global bindings, history, mode, phase and events before
  exposing graph edges. It never creates an entry at each separate proton.

## Result for the current construction

The retained P→N→E packet covers cells **0, 13, 16**. It is covered relative to
its own three-cell domain, but it does not cover the ambient four-level space.

| Layer | Required primitive cells | Entry–exit covered |
|---|---:|---:|
| 0 | 1 | 1 |
| 1 | 16 | 2 |
| 2 | 44 | 0 |
| 3 | 282 | 0 |
| Total | 343 | 3 |

These three primitives touch two assembled items out of 175. Only the seed
item is fully covered; two of the four components of one first-layer octahedron
are covered. Touching that octahedron is not reported as covering all its cells.

Including the legacy Pb extension gives **3/761** covered primitive cells.
Those legacy packets are not connected to the entry merely because their
unmarked solids share faces. This audits the currently admitted root-packet
boundary and states against a larger target; it does not establish the missing
full-assembly entry/exit and branch maps.

Even the union of 24 separately supplied seed-marking experiments reaches only
**15/343** primitive cells, and none in layer 3. That union is an optimistic
geometric bound, **not** one coherent construction or permission to merge
incompatible initial states. Coverage does not yet select a full-space binding.

## Controls

- Bare shared-face adjacency reports 343/343. This is a deliberately unadmitted
  control: it carries no window, phase or history and must not count as success.
- Two disjoint state paths can occupy the same three cells. Projecting forward
  and backward sets first falsely covers all three; the state-level test
  correctly covers zero and reports the incompatible states.
- A branched toy graph with two declared terminal boundary states passes;
  adding a dead-end branch fails. This is a graph-kernel test, not a new
  physical branching rule.
- A forward continuation from an exit is rejected.
- Mutated window order, branch, history or coordinate binding is rejected by
  the replay adapter, even when the unmarked cell is unchanged.
- A construction prefix without a committed exit is pending, not condemned
  as a dead-end or impossibility.

## Viewer and verification

The viewer API retains these ambient coverage diagnostics. The current default
[deuterium trial](deuterium-tunnel-trial-v1.md) shows construction progress and
3/3 coverage of its own three-carrier domain in the readout, not coverage of all
343 ambient primitives. No whole-lattice clutter or alternative-frame overlays
were added.

Run:

```
node research/strominger/checkers/check_fiber_coverage.mjs
node research/strominger/checkers/check_fiber_space.mjs
```

Evidence: `results/fiber-coverage/verification.json`.

The criterion is implemented and tested. The global condition currently fails
because the admitted model contains only the root packet, not the additional
internal branching transfers. This identifies missing model coverage, not an
obstruction to every possible full construction.
