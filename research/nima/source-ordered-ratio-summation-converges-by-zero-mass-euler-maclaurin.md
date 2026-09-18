# Source-ordered ratio summation converges by zero-mass Euler–Maclaurin

Fix `t` and, for each `n`, write

$$
h_n=\frac{e^t}{n}.
$$

The inner ratio sum enters as

$$
S_n(t)
=\frac1n\sum_{m\ge1}\kappa(h_nm)
=e^{-t}h_n\sum_{m\ge1}\kappa(h_nm).
$$

The profile `kappa` is smooth on `[0,infinity)`, decays as `r^-3`, and has integrable derivatives of every positive order. Its expansion at the origin contains only even powers beginning with `r^2`, so

$$
\kappa(0)=\kappa'(0)=\kappa^{(3)}(0)=\cdots=0.
$$

Euler–Maclaurin gives

$$
h\sum_{m\ge1}\kappa(hm)
=
\int_0^\infty\kappa(r)\,dr
-rac h2\kappa(0)
-
\sum_{j=1}^{M}
\frac{B_{2j}}{(2j)!}h^{2j}\kappa^{(2j-1)}(0)
+R_M(h).
$$

Every displayed term vanishes because the profile has zero mass and vanishing odd endpoint jets. Standard remainder estimates therefore give, for any fixed admissible order `M`,

$$
|S_n(t)|\le C_{M,t}n^{-2M}
$$

once enough derivatives are used.

Hence

$$
\sum_{n\ge1}S_n(t)
$$

converges in the source order and locally uniformly in `t` after the corresponding derivative bounds. The divergent common-gcd ray grouping is an impermissible rearrangement of this conditionally cancelled sum.

This supplies a completion prescription: sum the ratio variable `m` at fixed source label `n` using the zero-mass profile, then sum over `n`. It is compatible with the original ordered theta expansion and preserves the seam moment corrections.

Status: source-ordered completion of the ratio kernel established by Euler–Maclaurin cancellation; compatibility with prime-grade regrouping remains to be proved.
