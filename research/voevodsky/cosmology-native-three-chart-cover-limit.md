# Native three-chart cover limit for the p-normal filler

## Question

Would a native three-chart marked-fiber cover, by itself, kill the current \(\Xi_{\log}\) cokernel obstruction?

## Claim boundary

This packet tests only the abstract column shape of a native three-chart cover before adding any logarithmic comparison. It does not construct the cover, a comparison to \(\Xi_{\log}\), a Bockstein class, global contour, or physical period.

## Disposition

The formal target rows are

\[
(\Xi_{\log},-\sigma_{123}),
\]

and the required \(\tau_p\) column is

\[
(1,1).
\]

A native three-chart cover can source a Čech triple face. Without an added logarithmic comparison, every such column has form

\[
(0,n),\qquad n\in\mathbb Z.
\]

This only enlarges the already sourced Čech axis. It does not touch the cokernel generator

\[
(1,0),
\]

the \(\Xi_{\log}\) coordinate.

The checker tests sample columns \((0,-2),(0,-1),(0,1),(0,2)\). Over \(\mathbb F_{101}\) and \(\mathbb F_{103}\), their span has rank \(1\); adjoining the required \((1,1)\) column raises the rank to \(2\). Therefore the \(\Xi_{\log}\) obstruction survives.

Thus a native three-chart cover is necessary for a sourced \(\sigma_{123}\) face but not sufficient. The added datum must be a comparison assigning \(\Xi_{\log}\) coefficient \(\pm1\) to one native cover cone cell.

## Reproducibility

Checker:

- `research/voevodsky/check_cosmology_native_three_chart_cover_limit.py`

Result:

- `research/voevodsky/results/cosmology_native_three_chart_cover_limit.json`

Command:

- `python research/voevodsky/check_cosmology_native_three_chart_cover_limit.py`
