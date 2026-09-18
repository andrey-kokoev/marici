# Many-many arithmetic mode assignment

Enumerate prime-power labels `lambda=(p,k)` by increasing displacement

$$
L_{p,k}=k\log p,
$$

with lexicographic tie-breaking. Let `r(p,k)` be the resulting rank and choose disjoint frequency bands

$$
\Omega_{p,k}=[r(p,k),r(p,k)+1).
$$

The assignment

$$
(p,k)\longmapsto\Omega_{p,k}
$$

is injective because prime-power displacements are distinct under unique factorization. Fix the ordered source shell catalogue and let `j(p,k)` be its declared shell index for the label `(p,k)`, while `r(p,k)` remains the mode rank. Define

$$
(\widetilde V_t f)|_{\Omega_{p,k}}=t^{j(p,k)}f|_{\Omega_{p,k}}.
$$

The rank controls mode placement; the source shell index controls attenuation.

This realizes a label-faithful countable attenuation model. Pair labels `(n,m)` are retained as an internal multiplicity fiber over each shell band.

The assignment is synthetic and measurable. Its attenuation agrees with the shell coherencer exactly when the declared catalogue index `j(p,k)` is the source exponent. A canonical physical assignment requires an independent source principle selecting the frequency coordinate and rank convention.

Status: explicit arithmetic-to-mode assignment constructed; canonical physical calibration remains open.
