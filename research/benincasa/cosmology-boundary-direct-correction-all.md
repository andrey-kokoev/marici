# Direct degree-12-to-16 corrections exist for all 48 boundary coordinates

All 48 degree-12 boundary q representatives were translated by `(0,4)` and
compared with their degree-16 targets. Every difference was back-substituted
exactly into the degree-16 `T+S_K` source basis with full coefficients retained.

The direct correction profile is uniform within each K pole:

- pole 0: 24 records, each with trace 28 and 40 source rows split as 33 tangent plus 7 special-K;
- pole 1: 24 records, each with trace 44 and 66 source rows split as 52 tangent plus 14 special-K.

This removes the missing-direct-word blocker for candidate-wide coherence. The
remaining test must construct each adjacent composite in the same degree-16
basis and compare its coefficient dictionary with the corresponding direct
word.
