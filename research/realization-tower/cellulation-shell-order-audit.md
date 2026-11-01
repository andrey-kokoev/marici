# Shell construction-order audit

## Result: order dependence reproduced

Obligation: construction-order compatibility of the existing finite geometric
witness programs. This is not a physical or operator-level coherence claim.

Prerequisite validity does **not** imply confluence. The current constructor
retains the first proposed dot color and normal, and a shared octahedron's
construction orientation depends on the face that first introduces it.
Neither policy is justified by an order-independence result.

## Small two-cell counterexample

In Step 23, complete `shell:t:2,1,1`, then compare these two adjacent orders:

1. `shell:t:3,1,2`, followed by `shell:t:3,2,1`.
2. `shell:t:3,2,1`, followed by `shell:t:3,1,2`.

The prefix and remaining suffix are identical. Both plans complete and satisfy
all current source, return-path, dot, face and cell prerequisites. The final
rendered dot `shell:4,2,2` differs:

| First cell | Color | Normal |
| --- | --- | --- |
| `shell:t:3,1,2` | red | `(1,1,-1)/sqrt(3)` |
| `shell:t:3,2,1` | white | `(1,-1,1)/sqrt(3)` |

Its coordinate and ID remain identical. The normal difference also affects
click-to-lock orientation; this is not merely event numbering or timing.
The test constructs both actual renderers and checks their sphere materials and
anchor normals, independently of the audit's final-state projection.
This is a two-adjacent-cell witness, not a claim of the shortest possible prefix
among every conceivable construction.

## Search coverage

The checker reruns the real planner rather than permuting an already serialized
trace (which would hide the first-writer choices).

- 466 per-patch schedule trials: baseline, reverse cell priority, all adjacent
  swaps of the baseline cell order, 64 reproducibly seeded cell-priority
  shuffles per patch, and all 24 uniform octahedral arrival permutations.
- The actual eligible-cell schedules are recorded; 95, 95, 84 and 84 distinct
  cell schedules occur for Steps 23, 24, 25 and 26 respectively.
- Every patch exhibits dot-color and dot-normal order dependence.
- All 24 octahedral arrival permutations tested within each patch give the same
  semantic result at its fixed cell order. This is not exhaustive over independent
  arrival permutations for every octahedron or arbitrary action interleavings.
- All 24 macro-face orders complete, with canonical eligible-cell order inside
  each face. Eighteen differ from the baseline in directed arrows, dot colors
  and dot normals.
- For example, face order `(0,2,1,3)` instead of `(0,1,2,3)` omits the baseline's
  white `121 → 132` arrow. Face indices name the four shell planes in the
  existing Steps 23–26 order, not a relabeling of coordinates.
- Cell geometry/identity, geometric face ownership, and assigned face colors
  agree in the tested schedules. These observations do not establish their
  invariance under every possible schedule.

Whole-cell witness transactions remain atomic in this search. The tetrahedral
internal protocol is fixed. Arbitrary interleavings between different cells'
individual arrows and mixed cell/face/arrival permutations are not exhausted.
Timing, first-writer provenance and neutral scaffold draw order are excluded
from semantic equality; directed colored arrows, dot IDs/colors/normals, face
colors, cells and geometric face ownership are compared explicitly.

## Reproduction

- Checker: `node scripts/check-cellulation-shell-confluence.mjs`
- Tests: `node --test tests/cellulation-shell-confluence.test.mjs`
- Report: `test-results/cellulation-shell-confluence.json`

The report includes source SHA-256 hashes, schedules and concrete differences.
The checker exits **2** on a reproduced semantic conflict, **0** if no tested
counterexample was found; a crash is not a confluence result. Passing regression
tests here means the conflict detector and counterexamples reproduced, not that
the construction is confluent.

## Exhaustive event-model follow-up

The [exhaustive event verification](cellulation-shell-exhaustive-verification.md)
now closes the two-cell fork's entire reachable graph: **406 states representing
155,117,520 permitted action interleavings**, with two different dot-422
readouts. A supported octahedron's 24 arrival orders also exhaust to one result.
The full-shell event search reproduces the global conflicts but remains
incomplete at its explicit 2,000-state limit. These coverage statements are
separate; the local completion is not a global exhaustive certificate.

## Unresolved rule

The display still uses the original selected order. This audit does not resolve
competing dot readings, reverse an arrow, merge colors, or privilege a new cell
sort order. A repair must retain competing local witnesses and specify how a
shared vertex/interface is read, and must choose shared octahedral orientation
independently of which face happens to be processed first. Repeat this audit
against that explicit rule; do not use deterministic scheduling to conceal the
conflict.
