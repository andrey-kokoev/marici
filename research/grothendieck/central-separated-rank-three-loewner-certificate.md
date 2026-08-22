# A separated central rank-three Loewner minor is positive

For `(t1,t2,t3)=(0,0.005,0.01)`, a directed centered Xi-log jet through order
49 gives `F` through degree 23. The certified bound `|F'|<6.038308` bounds the
omitted contribution to every divided difference by
`6.038308(0.01)^23/(1-0.01)<6.10e-46`.

Directed evaluation gives

\[
 \det(K_F(t_i,t_j))\in[8.0788046991,9.3301006308]\times10^{-34}>0.
\]

This is genuinely separated rank-three positivity. Achieving the resolution
also exposed an omitted highest `F'` coefficient in the earlier degree-11 `H`
implementation. Carrying `F` beyond that dependency repairs it; the continuum
concavity certificate was rerun and remains valid. One positive triple is not
universal Loewner positivity or RH.

## Durable verification

- Jet checker: `checkers/central_H_degree_eleven_interval.py`
- Rank-three checker: `checkers/central_separated_rank_three_loewner.py`
- Results: `results/central-H-degree-eleven-interval.json` and
  `results/central-separated-rank-three-loewner.json`

On the eleven-point grid `{0,0.001,...,0.01}`, all 165 separated rank-three
minors are directed-positive. The weakest is `(0.008,0.009,0.01)`, with
determinant in `[5.5699262074e-38,5.5699262200e-38]`. This tests overlapping
compressions but does not prove positivity between grid points.

- Grid checker: `checkers/central_rank_three_loewner_grid.py`
- Grid result: `results/central-rank-three-loewner-grid.json`
