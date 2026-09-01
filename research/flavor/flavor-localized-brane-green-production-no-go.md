# Localized-brane Green function is not the production kernel: WP1116

## Question

Can a localized-brane Green function source the six-row production kernel?

## Exact gate

All six soft branches have the same threshold response

\[
\frac{R(p^2)}{R(0)}=\frac12.
\]

A common brane Green function is therefore a scalar common factor, not a
\(6\times6\) coupling matrix. Used universally, it preserves

\[
q=\frac1{23}(6,8,1,4,2,2)
\]

rather than producing \((1/4)^6\), and its gain is \(1\), not \(3/2\). It also
does not select between WP1056's exchange-symmetric quartet choices. Zero
brane-to-physical16 coupling entries are currently sourced.

## Classification

Negative gate. Common Green response, threshold degeneracy, or endpoint
localization cannot be promoted to production reweighting.

Checker: `research/flavor/checkers/wp1116_localized_brane_green_production_no_go.py`

Result: `results/wp1116_localized_brane_green_production_no_go.json`
