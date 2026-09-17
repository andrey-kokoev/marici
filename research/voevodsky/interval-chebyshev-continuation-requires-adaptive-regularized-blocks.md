# Interval-Chebyshev continuation requires adaptive regularized blocks

Between consecutive support thresholds, rescaling `[-L,L]` to `[-1,1]`
makes every active translation overlap and every archimedean matrix entry
analytic in `L`. For a finite regularized dangerous packet, map a slab
`[L_-,L_+]` to `t in [-1,1]` and write

\[
M(t)=\sum_{k=0}^m M_kT_k(t)+E_m(t).
\]

A directed continuation certificate consists of:

1. Arb values at Chebyshev--Lobatto nodes;
2. directed DCT coefficients `M_k`;
3. a complex-ellipse bound
   `sup_t ||E_m(t)|| <= 4 M_rho rho^{-m}/(rho-1)`;
4. interval Clenshaw evaluation on adaptive subintervals;
5. interval `LDL*` of the resulting matrix balls;
6. a leakage/residual Gram controlling motion outside the chosen packet.

A degree-4 pilot on `[.55,.65]`, using a fixed 20-dimensional packet from the
right endpoint, fails despite positivity at all five nodes: its interpolating
matrix develops minimum `-1.87e-7`. The highest coefficient norm is `0.1045`.
This is not evidence of negativity of the true form; it shows that a fixed
low-degree packet interpolation is unsuitable near a rapidly rotating
near-null space.

The implementation must therefore combine adaptive slab subdivision with the
regularized residual construction. Interpolate `J(L)`, `R(L)^*R(L)`, and the
complement floor, rather than raw large matrix entries or independently sorted
eigenvalues. Subdivide whenever the coefficient-tail bound is not small
relative to the local Schur margin.
