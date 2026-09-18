# Many-many infinite detector coupler bound

Let the embedded shell mode be `iota_j x_j` and let the shell history coupler be `C_j`. Define the row operator

$$
C(x_j)_{j\ge1}=\sum_{j\ge1}C_j\iota_jx_j.
$$

A sufficient Hilbert bound is

$$
\sum_{j\ge1}\|C_j\iota_j\|^2<\infty.
$$

Indeed, Cauchy–Schwarz gives

$$
\|Cx\|
\le
\left(\sum_j\|C_j\iota_j\|^2\right)^{1/2}
\left(\sum_j\|x_j\|^2\right)^{1/2}.
$$

The existing shell majorant supplies this condition whenever the source amplitudes have exponential moments and the shell response norms grow at most exponentially. The attenuated couplers `C V_t` satisfy the same bound uniformly for `0<t<1`.

Thus the infinite detector extension is bounded under the stated majorant, with loss effect retained separately.

Status: infinite detector-coupler extension reduced to and closed under the square-summable shell-response majorant.
