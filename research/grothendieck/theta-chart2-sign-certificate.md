# Exact Chart-2 dominant sign certificate

On `q in [7/16,1/2]`, `z=q*y in [q/1000,1/64]`, write

`D=q^2*R/z^2`, `H=z*R_z-2*R`, and `J=q*R_q+z*R_z`.

Positive prefactors give

- `sign(q*D_z)=sign(H)`, and
- `sign(D_q|z+(z/q)*D_z)=sign(J)`.

The exact 64-cell coefficient cover in
`results/theta-chart2-scaled-taylor-q-cover.json` proves for the degree-13
scaled polynomials

`H/z^3 <= -1645.3771197063104`,
`J/z^2 >= 5.325373831889643`.

The exact Cauchy checker `checkers/theta_chart2_scaled_tail.py`, with durable
output `results/theta-chart2-scaled-tail.json`, uses the complex disk
`|z|<=1/4` and proves absolute omitted-tail bounds

`|tail(H/z^3)| <= 1.6041496805722095`,
`|tail(J/z^2)| <= 0.09128319602310254`.

Therefore `H<0` and `J>0` throughout Chart 2, proving both required strict
signs. All decimal values above render exact rational inequalities checked by
the scripts; they are not floating-point acceptance tests.
