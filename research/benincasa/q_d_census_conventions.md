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
- Koszul audit: use the frozen gradients
  `(K_a,K_b,K_u)=(4a^3,0,a^2(1-b^2))` and the elementary columns
  `s_ab=(-K_b,K_a,0)`, `s_bu=(0,-K_u,K_b)`,
  `s_au=(-K_u,0,K_a)`.  Admit their monomial multiples by the same
  whole-column cutoff and plus-character projection as the exact columns.
- Cycle gate: before interpreting `S_0=<s_ab,s_bu>` or
  `S_1=S_0+<s_au>` on `H(Q_D,u)`, require `uS_i` to lie in the exact image
  `I_D`.  Failure is measured by `rank(I_D+uS_i)-rank(I_D)`.
- Formal filtration ranks are printed only as a diagnostic shadow when the
  cycle gate fails; they do not define subspaces of `H(Q_D,u)`.

Required regression table:

| D | dim Q_D | dim Q_D/uQ_D | t_D |
|---:|---:|---:|---:|
| 12 | 105 | 68 | 31 |
| 16 | 155 | 106 | 57 |
| 20 | 213 | 152 | 91 |
| 24 | 279 | 206 | 133 |

The frozen elementary-Koszul cycle gate fails:

| D | cycle defect S0 | cycle defect S1 | formal F0 | formal F1/F0 | formal H/F1 |
|---:|---:|---:|---:|---:|---:|
| 12 | 15 | 22 | 5 | 20 | 6 |
| 16 | 21 | 32 | 7 | 42 | 8 |
| 20 | 27 | 42 | 9 | 72 | 10 |
| 24 | 33 | 52 | 11 | 110 | 12 |

Thus the proposed filtration is not typed on `H(Q_D,u)`.  Even its formal
shadow has `dim(H/F1)=D/2`, rather than the required stable value one.
