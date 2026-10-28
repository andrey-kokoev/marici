# Binary LRRR communication: a candidate seven-event chart handoff

## Result and status

The operator's nested binary proposal admits a concrete candidate binding to the recovered native central frame and the prior four-chart helix. **Three retained-context splits plus L,R,R,R form seven events; the four leaf actions advance the chart once. Four blocks have 28 events and advance the retained grade once.**

This is an exact calculation for a **declared operation binding**, not a source-derived identification of the words "left" and "right", not a geometric subdivision, and not yet the P/N/E surface generator. In particular defining R from q and L makes the chart-handoff identity a tested compatibility of that choice, not an independent derivation of q.

The current 12x12 viewer is unchanged. Its layer words are not input to this experiment.

## One shared state, four retained contexts

The proposed operation is the right-comb tree

```
split
├─ 0: L
└─ 1: split
       ├─ 10: R
       └─ 11: split
               ├─ 110: R
               └─ 111: R
```

Depth-first execution is `split, L, split, R, split, R, R`. Splits preserve parent/child context; they do not erase or independently duplicate the global transport state. The seven-event count includes these three splits, not seven FCC movements. The four leaves are not equally sized geometric pieces: no metric partition or amplitude weighting is being asserted.

Executing four independent branch copies instead gives four endpoint states, not the product LRRR. That alternative is explicitly separated by the checker.

## Binding to actual recovered references

The native replay fixes the central T184 frame

```
(C0,M0,C1,M1) = (V051,V072,V076,V077).
```

The actual source coordinate rotation induces

```
q = [1,2,3,0].
```

The native ascending/outgoing flag comparison requires the reversal

```
L = r = [3,2,1,0].
```

Choose the second operation `R = q ∘ L = [0,3,2,1]`. Both L and R are involutions. In chronological execution, L followed by R is q. Therefore L followed by R,R,R is also q. Events remain in the record even where endpoint permutations cancel.

Their finite permutation group is the eight-element dihedral group, not the whole S4. They satisfy the four-letter Coxeter braid `LRLR = RLRL`, not the three-letter Artin braid. These are frame actions: q is an odd permutation and must not be called a proper rigid spatial quarter-turn. No binding of this central frame axis to the viewer's V5–V2 axis has yet been supplied.

## The retained lift is essential

Use the existing helix state `t=4h+i`, with grade h and chart i, and choose the compatible lift

```
q(t) = t+1
L(t) = 3-t
R(t) = 4-t.
```

Both lifted reflections remain involutions. One seven-event block gives `t -> t+1`. Four blocks give `t -> t+4`, i.e. `q^4 = Sigma`, rather than identity.

Crucially, chronological LRLR moves t by +2; RLRL moves it by −2. Their finite frame images agree, but the retained outputs differ by **one Sigma**. Thus the finite braid relation is NOT an equality of retained states. A comparison witness would need to carry that grade shift. This is exactly the information an endpoint-only picture would lose.

At the level of this candidate, 28 events are one shared-state cycle. No four-branch 112-occurrence trace, opening/closing record types, or complete `1+[4×28]+1` assembler has been constructed.

## Four face ports and the third-simplex obligation

Assign the four leaf contexts to faces opposite the ordered central marks:

| Context | Action | Opposite mark | Actual port | Reversed-frame port |
|---|---|---|---|---|
| 0 | L | C0 / V051 | F538 | F403 |
| 10 | R | M0 / V072 | F406 | F404 |
| 110 | R | C1 / V076 | F404 | F406 |
| 111 | R | M1 / V077 | F403 | F538 |

F538 is the actual native P-to-N output face; F403 is the initial P active-window face. The other two ports complete the tetrahedral boundary. The wiring transports covariantly with all 24 marked frame changes. This port assignment uses the supplied ordered frame; LRRR alone does not canonically select that marking.

A proposed witness simplex has the familiar interface of **six typed edge maps, four face comparisons, and one tetrahedral comparison between the two face-composition routes**:

```
H_ACD ∘ (d_CD * H_ABC) = H_ABD ∘ (H_BCD * d_AB).
```

The third simplex is not automatically another physical cell to glue in. Its attachment and what its comparison witnesses must be supplied. A 3-cell witnesses agreement of 2-cell composites; comparing two arbitrary 3-cells instead would require higher data.

The covariance/contravariance distinction also cannot be implemented by silently inverting incidence. The existing reverse-leg construction uses dual restriction; naive deletion of chain coordinates fails the boundary law. This test retains that counterexample.

The checker includes a strict 2-category toy with one object, one 1-arrow and Z/2-valued invertible face comparisons. Half of its 16 face assignments fail tetrahedral coherence despite local invertibility. Thus the group identities and closed signed boundary do not manufacture the required analytic filler.

## Verification

```
python research/strominger/checkers/check_binary_simplex_braid.py
```

26 exact check groups pass. Inputs are the live esd7 census, its source-bound native replay receipt, and the explicit candidate definition. The receipt retains hashes, actual central IDs, four face ports, the seven-event schedule, all 28 lifted event records, and a failed witness control.

- Definition: `binary-simplex-braid-candidate-v1.json`
- Receipt: `results/binary-simplex-braid-v1.json`

## Native binding follow-up

The [executed native binding test](binary-simplex-native-binding-v1.md) finds the actual span T242–F538–T184–F403–T174. It also rejects fixing the fifth coefficient while applying the four-mark L/R actions: the L reframe needs a different external reference, and the complete 30-state native coefficient abstraction contains neither proposed five-slot reflection. The remaining constructive target is the context-changing comparison between the two readers of T184, retaining six distinct reference vertices.

## Next binding test

Interpret L/R and the split contexts on the actual retained coefficient/interface state, not just its four-mark frame. Construct the witness comparisons, carrying orientation and the Sigma discrepancy. Only then ask whether the induced P/N/E readout reproduces the prescribed layers without importing their words.

Sources: [native end-to-end binding](native-fcc-end-to-end-binding.md), [seven-stage handoff](esd7-seven-stage-handoff-v1.md), [FCC face/flag binding](fcc-face-flag-binding-v1.md), [central dual-cell adapter](central-dual-cell-handoff-v1.md), [four-chart category](../voevodsky/a-clean-universal-category-for-the-eight-lattice-four-chart-suspension-system.md), and [elementary tetrahedral coherence](../voevodsky/the-first-elementary-conductor-tetrahedron-has-four-transfer-equations-and-one-higher-coherence-equation.md).
