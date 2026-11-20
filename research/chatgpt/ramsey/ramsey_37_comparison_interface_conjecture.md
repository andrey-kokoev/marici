# R(3,7): twenty comparison positions and three interface positions

**Research note · 2026-11-18 · Status: conjecture.** The proposed representation of 23 has twenty comparison positions and three cells of one interface. The cells have proposed comparison counts 8, 6, and 6. No construction or Ramsey proof is claimed here.

## Source of the count

The proposed circular closure starts with four occurrence lists: `aw`: 3a + 3w; `wb`: 7w + 7b; `waw`: 4w + 3a; `bwb`: 7b + 6w. There are 40 written occurrences. The first two lists contain ten w occurrences, as do the last two. Equality of counts does not identify witnesses or produce twenty distinct comparisons.

## Interface and symmetry

The four positions are `wa` (Some A−), `aa` (No B−), `wb` (Some B−), and `bb` (No A+). These are readings at positions, not kinds of link. To transfer a finding, retain the identity and scope of its witness. For the same nonempty binary groups, `aa` negates `wb`, and `bb` implies `wa`. The ordinary determinant `wa·bb − aa·wb` with Boolean values encoded as 0 and 1 therefore equals `bb`; it does not compute the proposed closure.

Partition the four positions into two unordered pairs. Exchange the positions `aa` and `wb`. This is a permutation of labels, not a claim that their readings are identical.

| Cell | Pairing | Effect of exchange | Proposed comparison count |
|---|---|---|---:|
| Fixed | (wa, bb) and (aa, wb) | Fixed | 8 |
| Mixed 1 | (wa, aa) and (wb, bb) | Goes to Mixed 2 | 6 |
| Mixed 2 | (wa, wb) and (aa, bb) | Goes to Mixed 1 | 6 |

The fixed cell and the exchanged pair follow from the permutation. Equality of the two mixed counts requires that it preserve segment identifications. Neither 8 nor 6 follows from the permutation. Eight written slots can refer to six distinct addresses when two addresses are shared. This illustrates the counting issue; it does not specify a gluing rule.

## What would make 20 + 3 a count of addresses?

First specify the segments, their witnesses, and all identifications, without using 23 as a selection rule. Show that the resulting twenty comparison positions are distinct addresses. Then show that each interface cell supplies one more address, distinct from the other cells and from those twenty. If the cells only summarize comparisons, the interface has three cells but does not add three addresses. If the cells share comparison addresses, adding their local counts can also count an address twice.

Even a verified count of 23 would describe a representation, not prove that every coloring on 23 addresses has a positive triple or a negative seven-set. For a separate 22-address construction and its proof scope, see the [pair-incidence note](ramsey_pair_incidence_coherence_22_to_23_2026-11-09.md).

[Ledger entry 4333](../../../src/ledger/20261118-4333%20Ramsey%20Comparison%20Interface%20Conjecture.md)
