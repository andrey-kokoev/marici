# Test of the 4×4 filler: 1 P + 1 E + 14 neutral directions

## Definition actually tested

The stage is interpreted as **four retained reversal depths × four comparison slots (aa, ab, ba, bb)**. This uses the existing depth construction rather than introducing sixteen independent particles.

First allow a free scalar coordinate in each of those sixteen slots. Define the two endpoint readings to be the mean of the four aa coordinates and the mean of the four bb coordinates. These independent readings have rank two, hence a fourteen-dimensional kernel.

An explicit basis decomposition is

```
1 collective P line
+ 1 collective E line
+ 8 existing N-channel directions (ab/ba at each depth)
+ 3 P-history contrasts
+ 3 E-history contrasts.
```

All sixteen free coordinates are recoverable from the two collective readings and fourteen residual coordinates. No information is discarded.

## A precise law giving the proposed neutral fourteen

Let uP be one on the four aa slots and zero elsewhere; let uE be one on the four bb slots. Their squared norms are four. The proposed boundary-only charge operator is

```
Q = (uP uP* − uE uE*) / 4.
```

Its exact spectrum on the free slot space is:

- +1: one collective P direction;
- −1: one collective E direction;
- 0: fourteen residual directions.

It is self-adjoint and changes sign under role polarity. Thus the proposed **1+1+14 decomposition can be constructed algebraically** by making only the collective boundary lines charged.

This is a new law, not something the previous local role assignment already implied. Under the existing channel types, only eight residual directions are N-labelled. Q reclassifies the six charged history contrasts as boundary-neutral. Zero charge alone also does not establish neutron identity.

These are slot-mode counts. If every slot carries a full five-coefficient packet, the free space is the slot space tensored with that internal packet space; the multiplicities are not sixteen independent scalar amplitudes of the actual native replay.

## Native-state binding test

Freshly replay the actual P/E/N packet across all four depths for each of its five coefficient basis vectors. This yields sixteen five-coefficient packet occurrences, or eighty displayed complex coordinates.

The exact realization matrix has rank **five**, not eighty. The combined collective P/E endpoint observation also has rank five: the endpoints are linked by the native transports, not independently prepared.

Consequently:

- the native charged history contrasts vanish;
- the eight N packet slots retain the same coefficient vector, with distinct orientation/history metadata;
- fixing the full endpoint data leaves **zero free residual native coordinates** in this replay.

Moreover, applying the candidate Q to the realized packet vectors takes them outside the old native replay subspace. The joint span of the replay image and its Q-image has dimension ten, rather than five. A larger filler state space would therefore be a genuine extension, not a reinterpretation of already-present independent states.

## The two 56 sectors

The tiling still contains 56 whole octahedral sites labelled N on both sheets. The current polarity law copies their coefficients and reverses flow direction. Stacking these two readings has rank 56 under a scalar-per-site probe, not 112. The new free-slot charge operator does not change that independence gate.

Thus `56+56+14=126` is not yet an independently realized neutron count.

## Result

**Yes:** an explicit boundary-only operator realizes one positive, one negative and fourteen neutral free slot modes.

**Not yet:** a source-supported filler with fourteen independently preparable neutron states, independent of two independently justified 56-mode sectors.

The next missing datum is an actual extended filler state and its typed boundary maps. It must preserve native interface comparisons while admitting the new modes, rather than introducing sixteen free amplitudes solely to obtain the count.

## Reproduce

```
node research/strominger/checkers/check_four_by_four_filler.mjs
```

**9 exact check groups pass**, including the negative native-binding and independence controls.

- Candidate algebra: `four-by-four-filler-model.mjs`
- Receipt and basis: `results/four-by-four-filler-v1.json`

## Viewer integration

The existing **12x12 fibration** process now has two actions after its retained return:

- State 47: apply the candidate operator to all sixteen full native packets; display the collective P/E projection, Q(input), and residual.
- State 48: confirm exact reconstruction and Q(residual)=0 on all five complex coefficients.
- State 49: materialize the [collective P*/E* comparison cell](collective-pair-cell-v1.md) under a separate, explicit 36→1 external-carrier rule. Raw geometric cells and internal contrasts are retained; this is not an implication of Q.
- State 50: enable the [declared neutral-state extension](neutral-state-extension-v1.md): 126 independent candidate channels with editable coefficients. These additional freedoms are not native neutron realizations.

The 4×4 panel lets you select the displayed matrix and coefficient. The fourteen residual coordinates are listed separately; the six charged history contrasts vanish in this native replay. No physical tiles or particle counts are added. The displayed neutral directions are explicitly not promoted to fourteen independent neutron states.

Implementation: `four-by-four-filler-comparison.mjs`, integrated through `../realization-tower/fibration-folded-process.mjs`. Tests: `tests/filler-viewer-process.test.mjs` and `scripts/test-fibration12-process.mjs`.

This does not claim a geometric/simplicial filler or a Pb-208 derivation.
