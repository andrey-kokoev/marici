# WITHDRAWN: the sparse-subsequence count missed the full optimizing degree range

This note is withdrawn. The prime-power grid remains within a fixed multiplicative factor of the optimizer for every sufficiently large degree, so the coefficient tail `m^(-3/4)` occurs throughout a parity subsequence, not only at exponentially sparse degrees. The correct threshold is `alpha<1/4`, and the Euler resolvent does **not** preserve `Dom N^(1/2)`. See:

- `the-one-prime-euler-resolvent-has-number-regularity-threshold-one-quarter-and-does-not-preserve-the-number-form-domain.md`

## Superseded analysis

## Prime-resolvent vacuum

Let

\[
B_p=
(I-p^{-1/2}e^{i(\log p)X})^{-1}
\]

on the archimedean cyclic carrier, and let `e_0` be the degree-zero polynomial vector.

The exact `SU(1,1)` coefficient calculation shows that along degrees

\[
m_k\asympp^{2k}
\]

the contribution of the `k`-th prime-power displacement has size

\[
\boxed{
|(B_pe_0)_{m_k}|
\asymp
m_k^{-3/4}.
}
\]

The same scale appears in the Poisson Gram column. The resolvent orientation changes phases but not the threshold calculation.

## Fractional number domains

For `alpha>=0`,

\[
\operatorname{Dom}N^\alpha
=
\left\{
(a_m):
\sum_{m
greater than or equal to0}
(1+m)^{2\alpha}|a_m|^2
<\infty
\right\}.
\]

Along the geometric subsequence `m_k asymp p^(2k)`, the weighted contribution is

\[
(1+m_k)^{2\alpha}
|(B_pe_0)_{m_k}|^2
\asymp
m_k^{2\alpha-3/2}.
\]

Because `m_k` grows geometrically, the subsequence sum converges exactly when

\[
2\alpha-\frac32<0,
\]

i.e.

\[
\boxed{
\alpha<\frac34.
}
\]

At `alpha=3/4`, the selected terms remain of constant size, and for larger `alpha` they grow.

Subject to matching upper bounds for the intervals between the optimizing subsequence, this gives the sharp threshold

\[
\boxed{
B_pe_0
\in
\operatorname{Dom}N^\alpha
\quad(\alpha<3/4),
}
\]

\[
\boxed{
B_pe_0
\notin
\operatorname{Dom}N^\alpha
\quad(\alpha\ge3/4).
}
\]

The lower-bound half is rigorous from the selected subsequence. The membership half requires a global upper bound, supplied below at the level of the prime-power sum.

## Global upper-bound optimization

For one prime-power displacement `x=k log p`, the ground coefficient obeys

\[
|M_{m0}(x)|
\le
Cm^{-1/4}
e^{-x/2}
\exp(-cme^{-2x})
\]

for `x>=1`, with the finitely many smaller `x` absorbed into an exponentially decaying remainder in `m`.

Multiplying by the Euler coefficient `p^(-k/2)=e^(-x/2)` gives

\[
|(\text{k-th term})_m|
\le
Cm^{-1/4}
e^{-x}
\exp(-cme^{-2x}).
\]

Summing over the geometric grid `e^(-x)=p^(-k)` and comparing it with the integral in `y=e^(-x)` gives

\[
\sum_{k
greater than or equal to0}
e^{-k\log p}
\exp(-cm e^{-2k\log p})
\le
C_pm^{-1/2}.
\]

Therefore

\[
\boxed{
|(B_pe_0)_m|
\le
C_pm^{-3/4}
}
\]

for even `m`, with odd coefficients handled by the corresponding phase/parity orientation. This proves the upper half of the fractional-domain threshold.

## Form-domain consequence

The quadratic form of `N` has domain

\[
\operatorname{Dom}N^{1/2}.
\]

Since

\[
\frac12<\frac34,
\]

we obtain

\[
\boxed{
B_pe_0
\in
\operatorname{Dom}N^{1/2}
}
\]

although

\[
B_pe_0
\notin
\operatorname{Dom}N.
\]

Thus the Euler transform is compatible with number energy at quadratic-form level on the vacuum, even though it fails at operator level.

This validates the move from operator curvature to form curvature.

## Fixed excited polynomial vectors

For fixed `n`, the matrix coefficient

\[
M_{mn}(x)
=
\langle e_m,e^{ixX}e_n\rangle
\]

is obtained from the ground coefficient by applying finitely many raising/lowering operators. The exact `SU(1,1)` formula expresses it as the same hyperbolic envelope multiplied by a degree-`n` Jacobi/hypergeometric factor.

In the transition regime

\[
m e^{-2x}
\asymp1,
\]

that fixed-degree factor is bounded by a constant depending on `n`; it does not change the power of `m` in the normalized coherent-state envelope. This predicts

\[
|(B_pe_n)_m|
\le
C_{p,n}m^{-3/4}

equal
\]

and hence

\[
B_pe_n
\in
\operatorname{Dom}N^\alpha
\qquad(\alpha<3/4)
\]

for every fixed `n`.

A fully rigorous proof requires writing the standard finite-degree `SU(1,1)` matrix-coefficient formula and bounding its Jacobi factor uniformly in the transition regime. This is now a finite special-function estimate, not an unknown semilocal asymptotic.

## Dense common form core

If the fixed-`n` estimate is established, then

\[
\mathcal P_{fin}
=
\operatorname{span}
\{e_n:n
greater than or equal to0\}
\]

satisfies

\[
B_p\mathcal P_{fin}
\subset
\operatorname{Dom}N^{1/2}.
\]

Since `P_fin` is dense, it supplies a dense source core on which both the original and Euler-transported number forms are finite.

For a finite prime set, products of resolvents require a multi-frequency version of the same transition estimate. The geometric coefficient decay remains, but near-canceling logarithmic frequencies must be controlled.

## Relative order suggested by the threshold

The threshold `alpha=3/4` indicates that the Euler cyclic transform loses slightly less than three quarters of a number derivative on the vacuum. It is therefore unreasonable to expect an order-zero perturbation of `N`.

A plausible form bound is of fractional order strictly above `1/2` and below `3/4`. The prolate comparison should be sandwiched by enough powers to absorb this loss.

This is heuristic for the full transported degree form; the threshold of one column does not determine the optimal global operator order.

## Disposition

The one-prime Euler resolvent has the sharp ground-state regularity threshold

\[
\boxed{
B_pe_0
\in
\operatorname{Dom}N^\alpha
\text{ for }\alpha<3/4,
\qquad
B_pe_0
\notin
\operatorname{Dom}N^{3/4}.
}
\]

In particular the number quadratic form is well-defined on the transformed vacuum. Establishing the same `m^(-3/4)` envelope for every fixed polynomial vector would provide a dense common form core and clear the first domain gate.
