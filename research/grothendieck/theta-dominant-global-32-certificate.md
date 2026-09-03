# Global exact dominant residual theorem

For

`q in [3/10,1/2]`, `y in [1/1000,1/28]`,

the approved dominant residual quotient satisfies

`D(q,y)>32`.

## Proof

The exact Chart-1 certificate proves `D_q>0` and `D_y<0` for
`q in [3/10,7/16]`. The exact Chart-2 certificate proves the same fixed-`y`
derivative signs for `q in [7/16,1/2]`; its `(q,z)` expression
`D_q|z+(z/q)D_z` is exactly `D_q|y`.

Thus on the joined rectangle, `D` is increasing in `q` and decreasing in `y`.
Its minimum is therefore at `(q,y)=(3/10,1/28)`. The exact corner certificate
gives

`D(3/10,1/28)>=32.16694268137721>32`.

Hence `D(q,y)>32` throughout the full domain.

## Evidence

- `theta-chart1-sign-certificate.md`
- `theta-chart2-sign-certificate.md`
- `theta-dominant-corner-certificate.md`
- `checkers/theta_dominant_global_32.py`
- `results/theta-dominant-global-32.json`

The aggregate checker verifies durable exact-certification manifests; all
acceptance inequalities in the producing checkers use rational arithmetic.
