# Native coefficient intensities do not retain the 1836 cost hierarchy

## Question and new source input

Can the existing complex coefficients fix relative response conductances, avoiding an arbitrary unit metric or fitted reservoir strength? This is a distinct executable test using source data ignored by the previous incidence-only model.

Keep the same retained 1836 arrows and interpret each exact coefficient z=a+b sqrt(-3) as conductance |z|^2=a^2+3b^2. Attach one common reservoir to every stage copy of the normalized collective mode, assigning each link the corresponding diagonal entry of N. These entries are 1/180 or 7/180; each stage sums to one. The source profiles use those same native intensities, rather than the earlier uniform per-layer fixtures. The opposite-source sign and conserved-flow readout remain explicit interpretation choices.

No independent reservoir multiplier or mass target enters the calculation. This is a proposed interpretation of native amplitudes, not a theorem that WG requires squared-amplitude conductances.

## Structural effect of the metric

The native projector coefficients give

| Stage | Nonzero arrows | Sum of squared coefficient magnitudes |
|---|---:|---:|
| L | 108 | 12 |
| G | 432 | 3 |
| N | 1296 | 1 |

For an orthogonal projector, the squared Hilbert-Schmidt norm equals its rank. Thus this metric retains normalized mode response rather than charging one unit per construction arrow. The sum 16 is not a new arrow count.

## Exact response

Reduction to stage and intensity class gives six potential variables. The checker then verifies all 109 unreduced boundary equations, including the reservoir. The resulting positive field costs are:

| Source | Exact cost | Decimal |
|---|---:|---:|
| Proton-like profile | 9287/48324 | 0.192181939 |
| Witness-like profile | 29560/132891 | 0.222437938 |
| Neutral pair | 75109/531564 | 0.141298132 |

The pair cost near 0.14 is not the binding correction. Subtracting the isolated costs gives -3302/12081. In units of the isolated witness cost:

- proton-like cost: 102157/118240, approximately 0.863980041;
- pair cost: 75109/118240, approximately 0.635224966;
- pair-minus-isolated correction: -18161/14780, approximately -1.228755074.

A common conductance scaling cancels from these ratios. It cannot turn the first ratio into 1836.

## Disposition

This rejects identifying the whole conserved-flow response cost with the 1836-to-one constituent hierarchy under this native-amplitude metric and reservoir construction. It does not reject the 1836 arrow-count theorem or the possibility of a separate interaction correction. Treating the computed response as such a correction would require a source law relating response cost to construction cost; that relation was not provided by normalizing the amplitudes.

The useful distinction is now exact: retained arrow count and normalized spectral response are different quantities on the same source. Stop this readout branch rather than adjusting conductances to restore the target. A new branch requires an independently specified rule relating those quantities.

## Verification

`python research/nima/checkers/check_native_coefficient_response_metric.py` passed via `structured_command_execution:e_32876_1791217327079672600_12`. Results: `results/native-coefficient-response-metric.json`, with source digest. Exact rational checks cover native coefficient identities, all port equations, energy/source-work equality and cancellation of a common metric scale. No commit or publication is claimed.
