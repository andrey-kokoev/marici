# The order-three Hausdorff corner is strictly positive

The degree-seven interval-series engine derives

\[
 A_6\approx7.83460650425438\,10^{-17},\qquad
 A_7\approx3.90722729912466\,10^{-19}.
\]

It includes the required `L^8/1209600` endpoint-cancellation coefficient,
regular eta quotient through seventh order, gamma-factor zeta values through
`zeta(8)`, the `(2s-1)^(-1)` normalization, and the Catalan coordinate change
through `h^7`.

All three `4x4` determinant intervals have positive lower endpoints:

\[
\begin{aligned}
\det H^{(3)}&\in[1.1609648767758,1.1609648769498]10^{-41},\\
\det H_u^{(3)}&\in[9.0828384571582,9.0832045231950]10^{-54},\\
\det H_{4-u}^{(3)}&\in[2.9660424971675,2.9660424980243]10^{-39}.
\end{aligned}
\]

The lower-support determinant remains the smallest margin. Its relative box
width is now about `4.1e-5`, much larger than at order two but still decisively
separated from zero. This is the first quantitative warning that higher-order
certification will require adaptive precision and tighter tail boxes.

## Scope

Three complete finite corners now pass unconditionally without zero data.
This neither proves the unbounded Hausdorff hierarchy nor RH, and it makes no
physical relative-chain claim.

## Durable verification

- Checker: `checkers/quarter_point_order_three_interval.py`
- Result: `results/quarter-point-order-three-interval.json`
- Eta input: `results/eta-order-eight-decimal-interval.json`
