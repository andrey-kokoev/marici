# Deuterium: reverse the boundary, retain the geometry

All 24 saved deuterium markings pass the fixed-geometry reverse-reader test.
Forward entry/exit is P/E; reversed entry/exit is old E/old P. Reverse traversal
uses inverse NE then inverse PN. Coordinates are unchanged.

Example with five distinct coefficients:

```
Forward P: [11,23,37,41,59]
        N: [41,23,37,11,59]
        E: [41,59,37,11,23]

Reverse E: [41,59,37,11,23]
        N: [41,23,37,11,59]
        P: [11,23,37,41,59]
```

Context-aware M/C reversal, index reflection i -> 2-i and P/E reader exchange
turn old E/N/P into new P/N/E. The two reversed face identifications pass the
existing local phase-frame/combination audit. Applying the frame reversal twice
restores the original frames.

The total five-slot permutation is `[3,4,2,0,1]` in either direction: it is
self-inverse. Therefore the final coefficient map alone cannot distinguish
forward from backward. Direction is carried by the ordered path and its marked
entry/exit boundary. This separates reading direction from the sign of the
previous 4D vertex deformation.

These are reversed-reader certificates on fixed geometry. They do not register
outgoing E operations in the original forward generator or resolve the separate
regular/split geometry-role convention. Production and viewer are unchanged.

```sh
node research/strominger/checkers/probe_deuterium_reverse_reading.mjs
```

Evidence: `results/deuterium-reverse-reading/verification.json`, with all
markings, boundaries, coordinate records, coefficient traces and frame audits.
