---
author: marici.Voevodsky
---

# 4347 — Oriented Squares and Cyclic Offsets Realize Different Ramsey Gains

**Question:** [Entry 4346](20261125-4346%20Ramsey%20Growth%20Depends%20on%20Core%20Capacity%20and%20Joint%20Coverage.md) identified the optimization: a root contributes one vertex, its core contributes the vertices retained, and its red neighbors contribute as many whole neighborhoods as can coexist. Can we *construct* those neighborhoods from the predecessor rather than read them off an endpoint?

**Answer:** We found two constructions with different domains of success. An oriented square gives four neighborhoods at once, with an exact test for when they work. A cyclic offset rule gives eight on a smaller core where the square falls short. These explain attainable gains; neither is a parameter-only law for the threshold.

| Known maximum witness orders | Construction realizing the gain | Accounting against the previous maximum |
|---|---|---|
| 8 → 13 | Cyclic offsets | 8 retained + root + 4 |
| 13 → 17 | Oriented square | 12 retained + root + 4 |
| 17 → 22 | Oriented square | 17 retained + root + 4 |
| 22 → 27 | Oriented square | 22 retained + root + 4 |
| 27 → 35 | Cyclic offsets | 26 retained + root + 8 |

In particular the gains 4 and 5, against a product baseline that advances by 3, explain the changes from −1 to 0 to +2 in \(R(3,k)-3k\) at \(k=5,6,7\). The difference between those two gains is **retention**: the same four-row operation costs one predecessor vertex in the first step and none in the second. Constructions alone do not prove that a larger gain is impossible.

## From a score to a construction

Simply copying old vertices’ red neighborhoods allowed at most two copies on the tested predecessors. Even three unrestricted neighborhoods failed on the maximum 13-vertex core. Dropping to 12 vertices changed the problem: five of twelve types supported four neighborhoods, but none could keep even one exact copy. [Anchor-release tests](../../research/voevodsky/results/ramsey_anchor_release36.json).

Counting blue edges individually recolorable to red without a triangle helped select cores, but equal counts concealed different outcomes. On two tied 17-vertex cores the four recolorable edges formed a square in the successful case and a path in the failure. On the 191 stored 22-vertex cores, all 67 with a recolorable square grew to 27; four without one also succeeded. The score did not explain this until we constructed the rows. [Matched cores](../../research/voevodsky/results/ramsey_gain_tie.json) · [All-core control](../../research/voevodsky/results/ramsey_gain22_square_audit.json).

On a square \(a,b,c,d\) in cyclic order, give the newcomer at edge \(ab\) both endpoints and the red neighbors of \(c\) compatible with those endpoints. Rotate the instruction around the square. Add a root red to the four newcomers and blue to the old core; make the newcomers mutually blue. On all 81 tested squares in the 22-vertex layer, exactly the two consistent orientations worked out of the 16 possible corner choices. This is not four independent decisions. [Constructions and orientation controls](../../research/voevodsky/results/ramsey_square_support_lift.json).

**Exact criterion for two red diagonals.** In a legal \((3,k)\) core, the two red diagonals of such a square have disjoint footprints, where the footprint of \(uv\) is \(N(u)\cup N(v)\). Let \(U\) be the vertices outside both footprints. The oriented lift is legal at \((3,k+1)\) exactly when \(U\) contains no blue \((k-3)\)-clique. To see why, fix a blue clique outside the corners. If fewer than four corners can join it, the largest contribution from the corners, copies and root increases by just one. If all four can join it, the old contribution is two and the new one four. Only this case can violate the relaxed threshold. [16-case check and counterexamples](../../research/voevodsky/results/ramsey_square_lift_criterion.json).

Thus creating the square by induced deletion has a measurable price: remove the footprint intersection, then hit the offending cliques outside the union. On 472,929 of 477,142 stored 27-vertex cores the minimum intersection size alone equaled the exact price; on the others it was one short. On the stored 35-vertex witness the minimum price was five, cancelling the entire five-vertex gain. Nor did a second square compound the gain at the same root: across 6,330 qualifying square pairs on 27 vertices, retaining one full lift blocked even one prescribed row of the other. [Cost census](../../research/voevodsky/results/ramsey_square_cost_census.json) · [Composition test](../../research/voevodsky/results/ramsey_square_compose.json).

## Why the next gain needed a different search

At every root of the stored 35-vertex witness, the 26-vertex blue core supports eight newcomers. Yet it cannot be obtained by deleting a vertex from a legal 27-vertex predecessor: it cannot accept that vertex back at the old threshold. Nor can it be obtained by adding red edges to a legal sparser 26-core: deleting any red edge makes a blue eight-clique. A blind screen of 62 sparse cores found none supporting even five under the largest-clique compatibility test. [Candidate-source audit](../../research/voevodsky/results/ramsey_gain26_blind.json).

Instead, place the vertices on a circle, prescribe symmetric red offsets at zero and translate them to every vertex. Translation moves any forbidden clique to one containing zero, so the root test is global. Scanning the two largest predecessor orders and all admissible positive root degrees, the only success at the 27-vertex step used order 26 and degree eight. Four of 2,380 opposite-offset choices in that case produced the same core type; one was \(\pm\{1,7,11,16\}\) modulo 35. The checker did not read the endpoint or its distances, but earlier knowledge of its symmetry inspired the family. The unchanged cyclic rule missed all three middle steps in the table. [Offset reconstruction](../../research/voevodsky/results/ramsey_gain26_offset_search.json) · [Cross-step control](../../research/voevodsky/results/ramsey_offset_growth.json).

## What we certified, and what we did not

- **Upper bound:** The previously open 44–49 red-edge window for a 20-vertex root core in a hypothetical 28-vertex witness is closed, conditional on the smaller catalogues and checker correctness. The 46-edge layer required an integer obstruction where fractional mass sufficed. At 49 edges the degree count forces 7-regularity; paired-root tests then excluded every remaining case. The final coverage audit matched core IDs, not just totals. A separate audit regenerated the 15 minimum 44-edge types and derived sufficient floors of 49 and 59 at orders 21 and 22 without assuming the published minima there. This recovers the **known** \(R(3,8)=28\), not a new Ramsey number or an independent verification of the whole chain. [Integer obstruction](../../research/voevodsky/results/ramsey_38_integer46.json) · [Final coverage](../../research/voevodsky/results/ramsey_38_final_coverage.json) · [Degree-floor audit](../../research/voevodsky/ramsey38-edge-floor-audit.md).
- **Local explanations:** Recoloring incidence alone can identify two cores as identical while one extends and the other fails. Support–clique incidence separated them: on core 66 a weighted budget of seven cannot pay four supports costing at least two each. On core 69 a single blue triple defeats the remaining whole assignments but not a fractional one. These are certificates for selected cores, not universal selection rules. [Matched collision](../../research/voevodsky/results/ramsey_recolor_collision.json) · [Fractional control](../../research/voevodsky/results/ramsey_core69_triple_dual.json).
- **Numerical field:** Eleven diagonal discounts, from 109/128 through 119/128, tied on the archived 26×26 bound audit. On the million-cell grid 113/128 and 114/128 disagreed on 482,365 unordered cells, but neither repaired the separate third-row failure at (3,13). A bounded unrestricted search for a 44-vertex (5,5) coloring returned unknown; cyclic exclusions do not choose a factor. [Factor sweep](../../research/voevodsky/results/ramsey_discount_identification.json) · [Unrestricted run](../../research/voevodsky/results/ramsey_55_order44_cyclic_1.json).

**Unanswered:** What tells us *before seeing an endpoint* when to retain the maximum predecessor, when to use a smaller core, and whether to use the oriented square, a cyclic construction, or neither? We now have explicit operations, their costs, and failures on adjacent steps. We do not yet have a single rule deriving the signed correction from the two parameters and proving that its readout is the first forbidden order.

Ledger sequence claim: `seqclaim-32e660b4f514b770b4506836`.
