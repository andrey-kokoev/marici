# Q_D census conventions

This packet fixes the conventions used by `q_d_census.py` and its Rust port.

- Coefficients: the prime field with `P = 2305843009213693951`; rational
  coefficients are mapped by denominator inversion.
- Ring: sparse polynomials in `(u,a,b)` with `u^2=0`, imported unchanged
  from `check_soft_axis_deck_orbit_completion.py`.
- Sectors: `(1,1)`, `(1,0)`, `(0,1)`, `(0,0)`, with
  `e_a=2-s_a`, `e_b=2-s_b`.
- Orbit completion: both `L2_minus=a-u/2` and `L2_plus=a+u/2` are included;
  `L1=b+1-u` is fixed.
- Gradient frames: `(e_a,e_b,e_u)` have deck characters `(-,+,+)`.
- Plus projection: a row is retained exactly when the coefficient parity in
  `a`, multiplied by the frame character, is `+1`.
- Target basis: `(component,u_degree,a_degree,b_degree)` with `u_degree<=1`
  and `a_degree+b_degree<=D`.
- Source basis: every monomial `a^i b^j` with `i+j<=D`, for every sector,
  both orbit lattices, and both `p/q` labels.
- Exact lift: `Hhat=H+C*(a/4,0,u/2)`, where `C` is the source-fixed
  coefficient of `K` and `H_p=(0,3m/2,0)`, `H_q=(-3m/2,0,0)`.
- Principal image: all admitted columns `p*(a/4,0,u/2)`.
- Admission: a column is admitted only when its complete, unprojected support
  has `u_degree<2` and total `(a,b)` degree at most `D`. Components are never
  truncated independently.
- `Q_D`: the plus gradient target modulo the span of the admitted `Hhat` and
  principal Euler columns. No degree-two Koszul columns are included in this
  definition.
- `Q_D/uQ_D`: specialize the same admitted columns to their `u^0` rows; do
  not independently regenerate a frozen source matrix.
- Torsion count: `t_D=2 dim(Q_D/uQ_D)-dim(Q_D)`.

Required regression table:

| D | dim Q_D | dim Q_D/uQ_D | t_D |
|---:|---:|---:|---:|
| 12 | 105 | 68 | 31 |
| 16 | 155 | 106 | 57 |
| 20 | 213 | 152 | 91 |
| 24 | 279 | 206 | 133 |
