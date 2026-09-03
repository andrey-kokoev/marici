# Second tangent-generator replay

## Question

Do the exact certificate-local source spans that absorb `nx` also absorb the independent tangent `(3,0,-1)` and derived unit normal `(-2,0,1)`?

## Result

Exact characteristic-zero replay was performed for all 1,224 certified targets. Both new directions are reconstructed within the existing local certificate span for 834 targets and fail local reconstruction for the same 390 targets:

| family | failures per direction |
|---|---:|
| IBP | 6 |
| K | 0 |
| q | 384 |

The tangent and normal failure sets coincide exactly, as required by

\[
(-2,0,1)=(1,0,0)-(3,0,-1)
\]

and exact absorption of the `nx` target.

## Claim boundary

A local-certificate-span failure is not a nonzero quotient class: each certificate basis was selected to reconstruct its `nx` target, not to span the full special exact image. The 390 targets therefore remain unresolved until tested against the full image. No geometric normal bundle or exceptional comparison is involved.

## Disposition

This is an unresolved observation rather than a defect or a nonzero-class discovery. It is reproducible, affects full normal-choice independence, and is concentrated in 6 IBP and 384 q targets. The discriminating test is full-image membership for these 390 tangent targets; the corresponding unit-normal answer then follows from the exact identity.

## Verification

- `research/voevodsky/check_cosmology_second_tangent_normal_exact_replay.py` — exit 0
- `research/voevodsky/results/cosmology_second_tangent_normal_exact_replay.json`
