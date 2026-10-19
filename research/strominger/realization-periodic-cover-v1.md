# Periodic realization chart with retained origin/history

## Constructed model

For a native same-body P-reader orbit, separate absolute origin r into

```
phase   = r mod 2
winding = floor(r/2)
r       = 2*winding + phase
```

A native advance changes phase 0->1 at fixed winding, or phase 1->0 while
incrementing winding. The geometric PNE reference and coefficient permutation
repeat after two advances; absolute occurrence indices and the full operation
word remain distinct.

All 24 seed markings were regenerated through origin 10: 264 reader records.
Every origin and every absolute occurrence index is recovered exactly. The
source operation word is retained, not replaced by phase or winding alone.

The native model begins at r=0 and only advances forward. Thus its realized
history is a one-sided lift with an initial boundary, not by itself a full
integer covering space or a license for negative-origin operations. Extending
the index set to all integers would be a separate mathematical construction.

## Proposed base topology

Take the chosen periodic realization chart and the transverse reader-link
circle. Their product was explicitly triangulated with 12 vertices, 36 edges
and 24 triangular faces. An independent Python checker computes exact rational
Betti numbers **(1,2,1)** and checks boundary squared is zero. This constructed
base is a torus.

For a simplicial presentation, the two-edge realization circle is subdivided
into four edges. Its intermediate vertices are triangulation auxiliaries, not
extra native half-origin records. The link circle is the three-edge cycle of
selected P/N/E facets around the common reference edge.

## Important identification still open

The two constructed circles are **periodic realization phase** and **transverse
reader-link phase**. They have not been identified separately with M and C.
Therefore this is a consistent periodic-chart prototype motivated by the
observed return, not yet a derivation of the original M/C-torus-in-R conjecture.
Nor is it the topology of the whole native packet universe, where NN motion,
branching and unbounded retained histories remain present.

The co-moving link coordinate and identity seam are chosen in this prototype;
endpoint reference return supports that choice, but does not derive a unique
continuous transport between phases or settle field sewing. A phase-only
identification would erase the origin grading and is explicitly rejected.

Production/viewer unchanged.

```sh
node research/strominger/checkers/check_realization_periodic_cover.mjs
python research/strominger/checkers/check_realization_cover_topology.py
```

Evidence: `results/realization-periodic-cover/verification.json` and
`topology-verification.json`.
