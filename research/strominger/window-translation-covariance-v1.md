# Testing repetition under window shifts

## Three distinct tests

### 1. Rigid lattice translation of a decorated neighborhood

Translate all marked points together by each of the 12 elementary sum-zero
lattice vectors e_i-e_j. For each of 24 seed markings, regenerate its native
operation graph through depth four at the translated location, using unchanged
production rules. Translate the results back and compare complete signatures:
geometry, aliases, species, absolute origin, five-slot permutations, faces,
operation kinds and grading increments.

All 288 translated runs match exactly: 6,336 state comparisons and 7,680 edge
comparisons. This tests translations of a whole decorated neighborhood, not
arbitrary independent placement of a window inside a fixed decoration.

### 2. Rigid translation of the geometric field construction

For the same twelve directions, translated geometric P patch eigenvectors
and N belt plane modes agree exactly with their untranslated values. There
are 144 P patch checks and 216 N patch checks.

The reason is structural, not fitted: the cyclic coefficients sum to zero,
and the N modes use centroid/endpoint differences. Centered rotation frames,
plane metrics and sector groupings translate unchanged. The previously verified
deterministic field constructors therefore give the same L/G/metric.

For this rigid-translation task, `U_s=I` in translated co-moving component
charts. It satisfies the field intertwining equations. This does not construct
U for a native reader change or NN step, and does not yet include E.

### 3. Actual native paths through depth 28

Independently explored the native operation graph to depth 28 from all 24
markings: 250,040 packet states in total (not claimed globally distinct across
seeds). Checked every transfer and retained absolute origins and representative
operation histories.

Among those edges were 76,928 NN spatial advances and 152,096 same-body reader
advances. Every sampled same-carrier advance preserved the ordered four-vertex
edge metric. Outside-context and full field transport are separate questions.

Distinct words reaching the same full packet were retained as distinct history
examples. No path equivalence or zero holonomy follows from endpoint equality.

The explicit 28-step same-body P reader paths return geometry/permutation at
every even checkpoint. Seven blocks of four and fourteen blocks of two both
work, but this is the already established period two; it does not establish
new order-seven or order-fourteen actions.

## Disposition

The conjecture passes its **rigid translation** form for the native graph and
the constructed P/N geometric field generators. Native window motion also
passes the sampled ordered-metric test.

The stronger statement that every allowed moving-window path transports the
full 36-component field consistently remains open: the corresponding field
maps, their compositions and their relation to marked chart monodromy still
need construction. Neither these checks nor translation invariance establish
a torus/vortex topology.

```sh
node research/strominger/checkers/check_window_translation_covariance.mjs
python research/strominger/checkers/check_field_translation_covariance.py
```

Evidence: `results/window-translation-covariance/verification.json` and
`field-verification.json`. Production/viewer unchanged.
