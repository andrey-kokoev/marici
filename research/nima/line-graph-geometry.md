# Hop geometry of the growing relational graph

## Metric and computation

Use exactly the paw seed and shared-endpoint line promotion of the previous
experiments. Assign each undirected relationship unit length. Compute shortest
paths by bitset breadth-first search from EVERY vertex at promotions0 through7.
No vertex samples, late-cycle extrapolations, or physical length calibration
are used. Average distance excludes identical source/target pairs; a ball
includes its centre and is averaged across all centres.

| Promotion | Records | Links | Diameter | Mean pair distance | Mean ball radius1 | Mean ball radius2 |
|---:|---:|---:|---:|---:|---:|---:|
|0|4|4|2|1.333333|3.000|4.000|
|1|4|5|2|1.166667|3.500|4.000|
|2|5|8|2|1.200000|4.200|5.000|
|3|8|18|2|1.357143|5.500|8.000|
|4|18|64|2|1.581699|8.111|18.000|
|5|64|396|3|2.009921|13.375|51.000|
|6|396|4552|4|2.560338|23.990|165.101|
|7|4552|101024|5|3.242070|45.387|588.044|

Stored distances, ball volumes and degree averages are exact rational numbers;
the table displays decimals. Full distance and eccentricity histograms are in
the result file.

## Interpretation

The graph develops both larger hop distances and much larger neighborhoods.
Diameter remains2 through promotion4 and reaches5 at promotion7. Meanwhile the
record population increases from4 to4552 and the radius-one ball grows from3
to about45.4 records. Thus population growth greatly outpaces hop-diameter
growth, and local coordination also changes strongly.

Global edge density decreases from2/3 to about0.00975; larger local degree does
not mean an increasing fraction of all possible pairs is connected. The relevant
measured distinction is larger local neighborhoods versus slowly increasing
global hop distances, not a blanket claim of densification.

Under fixed unit edge length, this is not an example of uniform expansion of a
fixed-degree lattice: local structure changes during growth. The data do not
establish a three-dimensional continuum, an FLRW scale factor, inflation, or a
Big Bang model. Physical edge lengths and cycle durations remain unspecified.
The early decline in mean distance also prevents treating record count alone
as a monotone physical distance scale.

## Retained source support

Each promoted record also retains the union of the seed-address supports of its
two endpoints. At promotion7,4549 of4552 records depend on all four seed addresses.
The proliferating records overwhelmingly recombine the same ancestral support.
This is a structural provenance observation, not a statement that an arbitrary
coherent quantum state can be copied into every record.

## Verification

```
python research/nima/checkers/check_line_graph_geometry.py
```

Checks include:

- independent triangle and four-vertex-path distance examples;
- all ordered distinct pairs accounted for exactly;
- distance-one count equals twice the edge count;
- final ball covers the entire graph for every centre;
- connectedness of every measured graph.

All assertions passed. This extends geometric measurements through promotion7;
the separate18-cycle count report remains exact only for its stated prefix and
provides bounds beyond it.

- Checker: `checkers/check_line_graph_geometry.py`
- Results: `results/line-graph-geometry.json`
