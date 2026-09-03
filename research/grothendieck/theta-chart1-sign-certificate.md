# Exact Chart-1 dominant sign certificate

On `q in [3/10,7/16]`, `y in [1/1000,1/28]`, set `z=qy`, so
`z<=1/64`. Write

`D=q^2*R/z^2`, `H=z*R_z-2R`, `J=q*R_q+z*R_z`.

Then positive prefactors give `sign(D_y)=sign(H)` and
`sign(D_q|y)=sign(J)`.

The exact degree-13 local-`q` coefficient cover consists of 484 accepted base
cells and 56 accepted bisected cells, with no unresolved cell. Its finite
scaled bounds satisfy

- `H/z^3 <= -2307.197783550278`, and
- `J/z^2 >= 0.7193849674159921` on base accepted cells, while refined cells
  have lower bound at least `8.228517039919803`.

The exact Cauchy checker on complex `|z|<=1/8` bounds omitted tails by

- `|tail(H/z^3)| <= 13.512375074823701`, and
- `|tail(J/z^2)| <= 0.6966342070829276`.

Thus the finite margins dominate both tails, proving `H<0`, `J>0`, and hence
`D_y<0`, `D_q>0` throughout Chart 1. Durable evidence is in
`results/theta-chart1-scaled-taylor-q-cover.json`,
`results/theta-chart1-scaled-taylor-refine.json`, and
`results/theta-chart1-scaled-tail.json`. Decimal values render exact rational
acceptance tests; floating point is not used for certification.
