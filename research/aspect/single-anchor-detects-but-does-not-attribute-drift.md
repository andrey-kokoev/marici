# One external anchor detects drift but does not attribute it

## The same mismatch has two incompatible causes

Represent frame angles by quarter turns modulo four. Begin with a science frame
`S` and two anchors `A` and `B` aligned.

Two later worlds give the same measurement of `S` relative to `A`:

- `S` rotates forward by one quarter turn;
- `A` rotates backward by one quarter turn.

In both cases the single edge `S-A` reports `1`. A perfect cross-locus
measurement detects a change but cannot decide which endpoint caused it.

With the second anchor, the edge patterns differ:

```text
science drift:  S-A=1, S-B=1, A-B=0
anchor A drift: S-A=1, S-B=0, A-B=3
```

Under the explicit assumptions that links are stable and at most one locus
moves, the triangle localizes the changed locus.

## Loop closure is consistency, not causal attribution

Both edge patterns satisfy exact triangular closure. Closure proves that the
relative measurements compose; it does not by itself say which node moved.
Causal attribution comes from additional dynamical assumptions, interventions,
or independently frozen loci.

This separates three instrument claims:

- mismatch detection;
- compositional consistency;
- fault attribution.

They require increasing authority. A calibrated crossing identifies realized
relative scale or frame; it does not automatically select a source law or name
the drifting component.

## Optical instrument

Compare an analyzer against two independently mounted polarization or frequency
references, and measure the anchor-to-anchor edge directly. Perturb each mount
and transfer link in turn. Reciprocal two-way transfer is needed when path delay
or nonreciprocity can mimic endpoint drift.

## Claim boundary

The checker uses exact quarter-turn frames, noiseless pairwise differences,
stable links, and a single-moving-locus attribution model. Simultaneous drift,
link bias, nonreciprocity, and statistical decision thresholds remain open.

## Verification

```text
python research/aspect/checkers/check_single_anchor_detects_but_does_not_attribute_drift.py
```
