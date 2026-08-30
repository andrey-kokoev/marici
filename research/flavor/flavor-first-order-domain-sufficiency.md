# First-order domain sufficiency (WP340)

## Frozen source grammar

For independent identically distributed Bernoulli domains with probability
(p), every normalized coincidence moment is

\[
u_j=p^j.
\]

The first moment (u_1=p) is already faithful to the sole source parameter.
Through the calibrated WP338 detector channel,

\[
p=\frac{r_1-\alpha}{\gamma}.
\]

Higher coincidences add no identification power inside this frozen family.
They also suffer the contrast amplification exposed by WP339.

## Hostile family expansion

First-order sufficiency is relative to the admitted domain. An independent
two-domain count law ((1/4,1/2,1/4)) and a perfectly correlated count law
((1/2,0,1/2)) both have first normalized moment (1/2), while their second
moments are (1/4) and (1/2).

Thus first order cannot test independence or reconstruct broader correlation
structure. The full tower becomes relevant only after expanding the source
grammar beyond the one-parameter independent family.

## Instrument disposition

This reduces the minimal physical probe burden: calibrated first-order domain
counts suffice if independence and identical preparation are independently
derived or validated. It does not select (p), and it does not authorize the
independence assumption from first-order agreement alone.

Run `uv run --with sympy python
research/flavor/checkers/wp340_first_order_domain_sufficiency.py` to regenerate
the exact sufficiency audit.
