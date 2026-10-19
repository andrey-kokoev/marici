# Which seam does native realization supply?

Tested two consecutive same-body reader advances for every one of the 24
hydrogen seed markings, regenerating the native PNE reference at each P reader.

## Results

- All 24 P readers admit two advances.
- Their original cell, local aliases, full five-coefficient permutation and
  regenerated six-vertex PNE reference return exactly after two steps.
- The absolute origin increases by 2; the final packet is distinct.
- Eight N readers admit the same two-step same-body advance; those also return
  their geometry/aliases/permutation while increasing origin by 2.
- The one-step P advance changes the common C1/M1 edge. A single advance is not
  already an identification of the old fixed transverse link with itself.

## Native advance versus reflection

The two-step geometric return induces identity on the restored reference
labels. It is not the separate M/C reflection that exchanges b/c on the link.
Therefore choosing that geometric return as a closing identification would
supply an orientation-preserving endpoint seam, compatible with the untwisted
torus prototype rather than the reflection-twisted Klein-bottle prototype.

The present source grammar does not make that identification: origin r and
r+2 remain different. One may retain a repeated geometric chart together with
an integer history/winding label, but interpreting that chart repetition as an
actual circular base requires an explicit additional quotient/atlas rule.

This test does not identify the longitudinal common-edge coordinate with the
realization coordinate. Nor does endpoint identity establish a continuous
framing or rule out path-level twisting. The earlier torus/Klein constructions
remain closure prototypes until the chosen base and full transport are supplied.

Only same-body reader advances were tested. Spatial NN advances, branches and
sewing across the whole assembly remain separate. Production/viewer unchanged.

```sh
node research/strominger/checkers/probe_realization_seam.mjs
```

Evidence: `results/realization-seam/verification.json`.
