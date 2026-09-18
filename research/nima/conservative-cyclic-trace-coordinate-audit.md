# Conservative / cyclic trace coordinate audit

For a consecutive shell `p<q`, compare the conservative five-port response with the cyclic bordered packet.

| Coordinate | Cyclic trace side | Conservative side | Comparison status |
|---|---|---|---|
| ordinary `rho(0)` | `p^(-2s) rho_g(0)` shellwise | `Phi 1_(log p,log q]` paired with the Evans history | Source-normalized and executable |
| derivative–wall pair | cyclic action commutes with the complete bordered response | explicit endpoint difference in both Hermitian and analytic-transpose lanes | Native formula closed; independent conservative trace identification open |
| wall `E` | `p^(-2s) E_g` | fixed even wall column `w_theta=(1/2,1/2)` | Included in the explicit endpoint pair; conservative trace identification open |
| Wronskian/linking `W` | `p^(-2s) W_g` | odd column `j_theta=(1/4,-1/4)` and `K_link=-J_link/2` | Linear and metric blocks constructed; oriented trace equality open |
| Laplace/reciprocal `R` | `p^(-2s) R_g` | stratified reciprocal response transport | Transport constructed; conservative trace equality open |

The ordinary consecutive-shell term is

$$
S_{p,q}^{(0)}(z)
=\int_{\log p}^{\log q}\Phi(t)u(t;z)\,dt
$$

in the analytic lane, with conjugation inserted only in the Hermitian lane.

The derivative–wall pair is already

$$
I_{p,q,{\rm an}}^{({\rm end})}(z)
=\Phi(\log q)u_z(\log q)-\Phi(\log p)u_z(\log p)
$$

in the analytic-transpose lane, with the conjugated version in the Hermitian lane. Therefore no bordered coordinate lacks a native formula. The remaining gate is one common source comparison: prove that the independent conservative functional restricts to these cyclic-trace formulas, with oriented linking and reciprocal variance retained.

Status: cyclic and native bordered coordinate formulas complete; conservative functional identification remains open as a single naturality cell.
