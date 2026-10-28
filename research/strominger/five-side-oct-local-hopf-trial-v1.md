# Local Hopf trial: local phases work; naive overlap gluing fails

**Experimental, not admitted wiring.** This tries the local hypothesis from [the Hopf probe](five-side-oct-hopf-hypothesis-v1.md) on actual native comparison rings. No P/E contents, routes, boundary identifications or viewer geometry were changed.

## Explicit trial assumptions

For each of the 44 interior vertices, assign each incident cell the normalized direction from that vertex to the cell centre. Lift that direction with the north or south Hopf section. This supplies a hypothetical complex line at each comparison-graph vertex; it does not identify that line with a retained native packet.

For neighbouring directions with normalized spinor representatives `q_a,q_b`, use the overlap connection

```
A_ab = arg <q_a, q_b>.
```

This is the shortest-geodesic/Pancharatnam choice. Antipodal endpoints are rejected as ambiguous. Under independent section changes `q_a -> exp(i theta_a) q_a`, the edge phase changes by `theta_b - theta_a`, so a loop phase is gauge invariant.

For overlap gluing, the trial identifies the same incident cell in two neighbouring vertex stars and asks for **connection-preserving U(1) gauge changes**. This is an additional, testable restriction, not an authorized native comparison law.

## Local result

Every star has twelve dual quadrilateral faces. Each outward-oriented spherical face has solid angle `pi/3`; its overlap loop phase is `-pi/6`. The phase is minus half the solid angle, as expected for this Hopf convention.

The twelve face phases add to `-2 pi`: unit winding in magnitude. The sum is retained **before** reduction modulo `2 pi`. Looking only at its exponential would misleadingly report identity and lose the integer winding. The sign here follows the overlap-connection and outward-face conventions; the earlier section transition was written as `s_S = exp(i phi) s_N` and had degree `+1`.

The checker also evaluates the previous exact integer sphere-sweep witnesses against these face phases. All 44 residual diagrams in reading `0:-1` give zero winding for zero sweeps and winding magnitude one for a once-swept sphere. This connects the trial phases to the actual comparison diagrams, not merely to unrelated sample Hopf circles. The geometry-only sphere witnesses were previously checked in all six readings; this new phase/witness evaluation is explicitly bounded to one reading.

## Overlap result: a gauge-invariant mismatch

There are **168 native edges joining interior vertices**. Each gives two stars a common ring of four cells. Evaluate both connections around the **same ordered cell ring**:

- one star gives phase `-pi/6`;
- the other gives `+pi/6`;
- their difference has magnitude **`pi/3`**.

This occurs on every shared ring. No choice of U(1) section gauges can repair it, because closed-loop holonomy is gauge invariant. Independent numerical gauge changes are tested. Passing to ordinary direction frames doubles the mismatch to `2 pi/3`; it does not remove it.

This rejects the stated **connection-preserving same-cell gluing**, not Hopf bundles in general. The two stars use different direction maps. A different base comparison or a connection correction could change the question, but neither is supplied by the local construction.

## Why conjugating every neighbour is not a repair

Complex conjugation reverses the circle phase, so it matches the two ring holonomies pairwise. However, the interior-vertex adjacency graph contains **176 native triangles**. Each is an actual three-star overlap containing two common cells.

Conjugating on all three overlap edges composes to an anti-linear map, never the identity on a complex line, whatever phases are included. Thus it cannot satisfy a chart-transition cocycle on these triple overlaps. Pairwise matching is insufficient.

This argument concerns attempted bundle transition maps. It does not prohibit a separately specified comparison system with nontrivial transport or additional retained witnesses; those must be constructed rather than inferred from pairwise phase matching.

## Outcome and next question

The trial establishes a usable **local Hopf connection**, and exposes exactly where a naive global assembly fails. It is not a source-derived realization of the 80 retained fibres.

The next problem is to derive the **between-star comparison map** from the actual native operands and retained histories. In particular, determine whether it moves the direction base, changes the connection, or introduces a larger lifted state than a single common phase. Any proposed correction must be tested on the existing shared rings and triple overlaps—not merely selected to cancel their measured mismatch.

No filling rule, sign meaning, phase transformation of payloads, or boundary law has been inferred from this experiment.

## Replay

```sh
node --test tests/five-side-oct-local-hopf-trial.test.mjs
node research/strominger/checkers/check_five_side_oct_local_hopf_trial.mjs --record
```

Implementation: `five-side-oct-local-hopf-trial.mjs`.
Receipt: `results/five-side-oct-local-hopf-trial-v1/verification.json`.

The receipt retains the sphere-sweep windings, all 168 shared-ring mismatches and all 176 triple-overlap witnesses, with `trialAdmitted: false` and `constructionAdmitted: false`.
