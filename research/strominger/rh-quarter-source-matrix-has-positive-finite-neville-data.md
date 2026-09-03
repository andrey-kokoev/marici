# Quarter source matrix has positive finite Neville data

## Question

Can the finite total-positivity evidence be reorganized into positive elimination data suitable for an all-size factorization?

## Claim boundary

The test covers size ten and shifts zero through six. Positive finite Neville data do not supply closed formulas or prove positivity at arbitrary size.

## Disposition

Exact Neville elimination of each source matrix and its transpose produces 45 positive multipliers in each orientation and positive diagonal pivots. All six gates pass; a deliberate row reversal breaks positive Neville data. This strengthens the factorization route beyond a raw minor census. The next executable leaf is `quarter-solid-minor-factorization`, factoring low-order contiguous minors symbolically in the shift variable to determine whether their positivity follows from explicit positive factors.
