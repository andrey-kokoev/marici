# qRB microstep 78: normalized Gram to Douglas bound

For a fixed finite observer packet `E_0`, suppose

$$
V_\Lambda^{-1}G_\Lambda\to G_0
$$

in operator norm relative to the positive Plancherel Gram `G_0`. Then, for every `epsilon` in `(0,1)`, eventually

$$
(1-\varepsilon)V_\Lambda G_0
\preceq G_\Lambda
\preceq(1+\varepsilon)V_\Lambda G_0.
$$

Hence the cutoff transitions on that packet admit bounded Douglas maps, with comparison constants controlled by

$$
\frac{1+\varepsilon}{1-\varepsilon}.
$$

This gives eventual finite-packet promotion and kernel stability. It does not provide a bound uniform over all packets, nor does it remove the common volume factor.

Status: finite-packet residual promotion reduced to normalized Gram convergence; global uniformity remains open.
