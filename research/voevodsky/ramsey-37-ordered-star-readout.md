# Four signed claims from two pole viewpoints in a (3,7) witness

**Scope.** One 22-vertex triangle-free red graph with independence number six. Its red edge list is retained in [the dual-star record](results/ramsey_37_dual_stars.json). This is a readout of that witness, not a proof of the Ramsey threshold or a classification of all witnesses.

## What is read

The graph has a rotation with four five-cycles and two fixed poles (0 and 6), and a color-preserving involution exchanging the poles and reversing this rotation. For each pole its five non-pole red neighbors define five stars: intersect each neighbor's red neighborhood with the ten middle vertices. Within a pole, each star contains four positions, each pair of stars meets in one position, and each position belongs to two stars. The two poles give different star systems on the same positions.

For each star, the unique opposite-pole star disjoint from it is its counterpart. Find instead the unique opposite-pole star with overlap one and take *its* counterpart: this is the successor of the original star. The resulting five-cycle runs oppositely at the two poles. For a source star S, its four slots u are its intersections with successor powers d = +1, -1, +2, -2. Write T for that other same-pole star. Call positive d the R channel and negative d the B channel; these are **channel names, not edge colors**.

Let U and V be the two opposite-pole stars containing u. Define h(X) = |X ∩ U| + |X ∩ V|. The signed value is h(T) − h(S). Separately, test the actual red edge from u to the slot with the same d in the next frame. The domain of the claims is exactly these four one-tick tests per star, not all edges at a vertex.

| d | Slot at pole 0, frame 0 | h(S) → h(T) | Next slot | Red edge? |
|---|---:|---|---:|---|
| +1 | 7 | 5 → 4 | 12 | no |
| −1 | 10 | 4 → 5 | 7 | no |
| +2 | 8 | 4 → 5 | 13 | yes |
| −2 | 9 | 5 → 4 | 14 | yes |

Thus the red continuations satisfy **no R−, no B+, some R+, some B−**. The same four channel/sign/existence combinations hold at every frame at both poles, in their local clocks. The observed sign is ordered; undirected red adjacency alone does not give it. A different probe (two ticks) does not have the same existence pattern. Neither uniqueness of this readout nor its validity on other witnesses is claimed.

## Reproduction

Run from `research/voevodsky` in this order:

```sh
python -B checkers/ramsey_37_dual_stars.py
python -B checkers/ramsey_37_star_addresses.py
python -B checkers/ramsey_37_clock_witnesses.py
python -B checkers/ramsey_37_ordered_star_sign.py
```

[Ordered-sign checker](checkers/ramsey_37_ordered_star_sign.py) · [All 40 comparisons](results/ramsey_37_ordered_star_sign.json) · [Source witness construction](../chatgpt/ramsey/ramsey_pair_incidence_coherence_22_to_23_2026-11-09.md)
