# Transporting growing packets to the designated rung4 reference

## Executed adapter

The checker freshly runs the existing finite label/from/to fibration tests and
the all-source graph-geometry measurements. For every generated graph at cycles0
through7, it constructs the directed packet table `(label,from,to)` and applies
the documented eight transitions from rung12 to rung4:

    label, from, to, label, from, to, label, from

Each transition keeps the dependent total `(selected key, previous row)`.
The original-row decoder is imported from the existing finite checker. At every
stage all packet labels and endpoints are reconstructed and compared exactly
with the initial table. At rung4 the entire recovered graph equals the input
graph, so the freshly calculated unit-hop metric transports unchanged.

| Growth cycle | Rung4 retained rows | Occupied source fibers | Transported hop diameter |
|---:|---:|---:|---:|
|0|8|4|2|
|1|10|4|2|
|2|16|5|2|
|3|36|8|2|
|4|128|18|2|
|5|792|64|3|
|6|9104|396|4|
|7|202048|4552|5|

Rung numbers label presentations in this retained-total implementation; the
operator preserves row cardinality. This experiment does not collapse a whole
growing graph to four rows or construct a physical four-state reference chart.

## Readout result

The theory page designates rung4 as the physical-reference locus. The section
"Rung transports and the physical reference" also states that its numerical
reference/readout remains to be constructed. This agrees with the executable
kernel: it supplies grouping, witnesses and reconstruction, not a spatial
metric or clock map.

Consequently the report distinguishes:

- transported unit-hop diameter and mean distance: computed;
- physical length and proper-time increment: unspecified (`null`).

Merely moving the readout to rung4 cannot select its numerical scale. For any
candidate spatial metric, multiplying distances by an arbitrary positive
cycle-dependent factor leaves the table grouping and its reconstruction
identities unchanged. Assigning different durations to the same cycle indices
also leaves these operators unchanged. A fixed reference must select those
maps before the earlier graph-growth counts determine physical expansion.

This is a completed transport test and an unresolved physical-readout
construction. No cosmological length, duration or expansion rate is reported.

## Reproduction

```
python research/nima/checkers/check_growth_rung4_readout.py
```

All assertions passed for all eight tested growth stages, with fresh underlying
fibration and graph-geometry checks. See:

- `checkers/check_growth_rung4_readout.py`
- `results/growth-rung4-readout.json`
- `label-from-to-fibration-tower.md`
- `../../../docs/theory-page.md`, "Rung transports and the physical reference"
