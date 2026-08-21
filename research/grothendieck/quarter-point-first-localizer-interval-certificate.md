# End-to-end certificate for the first Hausdorff localizers

The regular eta-jet intervals can be propagated without importing numerical
constants. The triangular eta system encloses `gamma_0,...,gamma_3`.
Machin's formula

\[
 \pi=16\arctan(1/5)-4\arctan(1/239)
\]

is enclosed by exact-rational alternating bounds, while Apéry's series

\[
 \zeta(3)=\frac52\sum_{n\ge1}
 \frac{(-1)^{n-1}}{n^3{2n\choose n}}
\]

provides an exponentially convergent exact-rational enclosure of `zeta(3)`.
Outward decimal arithmetic then evaluates the completed source coefficients,
the moments `A_0,...,A_3`, and both order-one endpoint localizers.

The certified determinant intervals are

\[
\det H_u^{(1)}\in
[3.83670803159143268259,\;3.83670803159143269371]10^{-15}
\]

and

\[
\det H_{4-u}^{(1)}\in
[3.103052637561763441065,\;3.103052637561763441072]10^{-8}.
\]

Both lower endpoints are strictly positive. This closes the first complete
quarter-point Hausdorff corner using only source-side formulas and certified
elementary/Dirichlet evaluations; no zero locations enter.

## Meaning

This is the first unconditional coupled positivity certificate in the compact
quarter-point program: the ordinary order-one moment matrix and both order-one
support localizers pass. It is stronger than the earlier floating regression
because rounding and analytic tails are enclosed end to end.

It remains finite-dimensional. RH requires every order of all three
localizer families, so this result proves neither RH nor the existence of the
full positive measure. Its value is to validate the normalization, remove the
first plausible low-order falsifier, and provide a reusable certification
architecture for higher jets.

## Durable verification

- Checker: `checkers/quarter_point_end_to_end_interval.py`
- Eta checker: `checkers/eta_jet_decimal_interval.py`
- Tail checker: `checkers/eta_euler_tail_bound.py`
- Result: `results/quarter-point-end-to-end-interval.json`
