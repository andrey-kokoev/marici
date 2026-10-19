# Cut independence of the paired comparison seeds

## Result

All ten constructions—five 2/3 cut pairs and two uniform composition orders—are equivalent as retained paired arrow histories. The checker publishes explicit label rotations, output exchanges and six-occurrence permutations for each equivalence.

- Moving the cut uses rotations of the original five-cycle and preserves both output mode planes and phase updates.
- Changing first-two to last-two composition uses whole-pair path reversal, electron/positron ownership exchange and output exchange.
- Every original history remains recorded; no endpoint-only collapse is used.

Thus the paired **seed configuration is independent of these choices**, modulo the recorded symmetries.

## Mode-transport distinction

Whole-pair reversal changes endpoint incidence into its transpose, up to the published occurrence permutation. It does not directly carry its right eigenmode plane to the target right eigenmode plane.

The first exact inverse-phase residual on the real two-mode basis has rank two:

    [[-3/2,  1/2],
     [ 3/2,  1/2],
     [   0,    0],
     [ 3/2, -1/2],
     [-3/2, -1/2],
     [   0,    0]].

This distinguishes two questions: equivalence of retained seed/history configurations, which passes, and transport of a prepared mode through reversal, which needs its left/right identification computed. Recomputing target eigenvectors is not the same as transporting the prepared source vector.

## Verification

Seven exact checks pass. Explicit witnesses cover all ten paired constructions and all twenty output occurrence maps.

```sh
python research/strominger/checkers/check_two_output_cut_independence.py
```

Result: `research/strominger/results/two_output_cut_independence.json`.

Next calculation: use the retained positive metric and existing spectral projectors to compute the left/right mode identification under whole-pair reversal.
