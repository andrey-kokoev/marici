# Native binding: the three-simplex span exists, but the five-slot braid lift fails

## Result

The next test finds an actual geometric version of the proposed two-simplices-with-a-third-witness picture:

```
T242 (N) -- F538 -- T184 (P witness) -- F403 -- T174 (N)
```

The two N tetrahedra share the actual edge **E368**. Each meets T184 on a complete, distinct triangular face. All IDs come from the existing esd7 census. Each PN leg is freshly constructed and validated by the native packet rules, with a separate marked P reader for the second leg. No viewer cells or P/N/E word tables are used to fit this span.

However, **sharing T184 does not identify its two retained readers**. The required change between them is precisely the unconstructed interface map. This is not yet a simultaneous phase-compatible assembly or an analytic third-simplex filler.

## What was tested

The previous [LRRR frame candidate](binary-simplex-braid-v1.md) used

```
L = [3,2,1,0], R = [0,3,2,1].
```

The deliberately naive coefficient extension fixes the fifth slot:

```
L5 = [3,2,1,0,4], R5 = [0,3,2,1,4].
```

It is tested rather than assumed. L/R frame actions were recovered/declared on four marks, not on the native full five-slot packet.

### The fifth reference actually changes

Native P completion derives its outside C2 vertex from the neighbouring cell. Reversing the four central marks changes that required neighbour:

```
old C2 = (-1,1,0,1)
new C2 = ( 1,0,1,-1).
```

Both readers use the four central vertices, but they do not use the same fifth reference. Retaining both contexts therefore requires **six distinct geometric references**, not a permutation of five that fixes the fifth. R happens to preserve the outside context in this fixture; that alone does not admit R as a native transfer.

The central comparison must relate these readers without deleting the old context, inventing the new coefficient, or identifying different references because they occupy the same P body. The six-reference union is a support observation, not a claim that a six-dimensional physical wavefunction or a unique coefficient law has been derived.

### Complete finite coefficient obstruction for this naive lift

The current source rules induce the following typed permutation automaton:

- P -> P: the actual P reader advance;
- P -> N: PN;
- N -> N: N reader/NN phase advance;
- N -> P: inverse-PN;
- N -> E: NE;
- E: no outgoing native operation.

Forget geometry and occurrence origin to obtain a permissive over-approximation, but retain species and all five coefficients. Its reachable closure has **30 states: ten per species**. The closure is checked under every transition. Neither L5 nor R5 occurs in any species.

Because the abstraction includes every current native transition type, no native word of any length from this seed realizes those exact fixed-fifth-slot permutations. This is **not** a no-go theorem for a context-growing lift, a different L/R binding, or new source-supported operations.

The concrete native packet search independently reaches **296 states through depth eight**, without hitting its 20,000-state cap. It validates every expanded transfer and finds no L5/R5 coefficient hit. It records one shortest route per packet; it does not exhaust all retained histories or certify simultaneous occupancy.

### Real transfers and contravariance remain intact

Actual PN then NE is replayed on five distinct complex coefficients. Every coordinate is recoverable by inverse permutation replay. Forging L5 as the PN permutation is rejected by the native validator. Inverse-PN is a genuine typed return; E does not acquire an invented onward operation.

Passive coefficient pullback reverses the order of a frame action. Abstract chronological LRRR gives the inverse-q pullback on the coefficients, as it should. This algebraic fact is checked separately and is not promoted into a native transport.

The helix grade t and the native nonnegative occurrence origin remain distinct clocks. The previous seven-event/28-event count is not reinterpreted as a sequence of native phase increments.

## Retained-context follow-up

The [eight-reference lift](retained-context-braid-v1.md) closes the support under L/R and verifies complete-bank naturality with the actual PN/NE transfers. It constructs a strict context-transport comparison diagram, while retaining three unspecified preparation coefficients. Simultaneous field/reader transport leaves the P/N/E spectral readout unchanged, so it is not yet a layer-growth law.

## Communication wiring now localized

The proposed composite has the actual form

```
N(T242)
  -- inverse-PN --> P(T184, old reader)
  -- [missing context-changing comparison] --> P(T184, reversed reader)
  -- PN --> N(T174).
```

The old-reader output/input ports are the same F538/F403 ports recovered in the binary schedule. This identifies a concrete target for the third-simplex witness rather than another anonymous square model.

A witness between composites requires their typed endpoints and coefficient/context maps first. The middle comparison is not supplied by geometric incidence, a finite permutation braid equality, or the count of 28 events. An additional retained context is a plausible place to construct it; its value law is still to be supplied or derived.

## Reproduce

```
python research/strominger/checkers/check_binary_simplex_braid.py
node research/strominger/checkers/check_binary_simplex_native_binding.mjs
```

The binding checker passes **16 check groups**, including the negative controls. The receipt is `results/binary-simplex-native-binding-v1.json`; it records live source hashes, actual operation maps and complex vectors, context coordinates, the complete 30-state coefficient closure, bounded native search, and source cell/face/edge IDs.

The current Three.js viewer and its layer definitions are unchanged. No P/N/E surface generation from LRRR is claimed.
