# Compositional coherence of boundary corrections

## Result

For each K pole, the direct degree-12 to degree-16 lower-edge correction under exponent translation `(0,4)` was independently back-substituted to original `T` and `S_K` rows. It was compared with the composite of:

1. the degree-12 to degree-14 correction translated by `(0,2)`;
2. the degree-14 to degree-16 correction.

Both direct and composite words reconstruct the same q-representative boundary. More strongly, their original-source coefficient dictionaries are identical:

| K pole | direct rows | composite rows | nonzero syzygy coefficients |
|---:|---:|---:|---:|
| 0 | 40 | 40 | 0 |
| 1 | 66 | 66 | 0 |

Thus the valid compositional comparison closes strictly for these lower-edge representatives. The prior adjacent-word subtraction failed because it compared cells with different boundaries.

## Disposition

N3b5b5 is completed. The lower-edge boundary transition is coherent across the composable chain 12-to-14-to-16 at original-source coefficient level.

N3b5b remains active through N3b5b6: extend the direct-versus-composite test from the two lower-edge representatives to every degree-12 boundary coordinate and both poles. Passing would complete the tested finite boundary coherence layer; failure would localize coherence defects to specific cutoff faces.

## Reproducibility

- Checker: `research/voevodsky/check_cosmology_rank26_p_normal_K_q_correction_composition.py`
- Result: `research/voevodsky/results/cosmology_rank26_p_normal_K_q_correction_composition.json`
