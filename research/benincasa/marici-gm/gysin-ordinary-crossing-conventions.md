# Ordinary Gysin crossing convention packet

- source connection: `gysin-adapted-reconstruction-d12.json`
- basis order: `(e6, v_alg, omega0, omega2)`
- divisors: `D1=v-u`, `D2=(u+v)/2-1-u^2`, `D3=(u+v)/2-1+u^2`
- `u` chart: `u=u0+e`, `v=u0+e*t`
- `v` chart: `u=u0+e*s`, `v=u0+e`
- overlap: `e_v=e_u*t`, `s=1/t`
- forced exceptional weights: `(0,0,1,1)`
- sheared-frame overlap: `diag(1,1,t,t)`
- arithmetic orbits:
  - `D1-D2`: `u0^2-u0+1=0`, conjugation `u0 -> 1-u0`
  - `D1-D3`: `u0^2+u0-1=0`, conjugation `u0 -> -1-u0`
- replication prime: `2305843009213693951`
- accepted packet for each of four crossings and each of two charts:
  `exceptional_rank=3 kernel=1 cokernel=1 L1_kernel=2 strict_L1=(2,2)`

The generated full matrix packet is `gysin-ordinary-crossing-blowup.json`; it
is reproducible with `../gysin_ordinary_crossing_blowup.py` and intentionally
not treated as a source object.
