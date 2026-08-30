# All-order positive corners force a unique analytic Weyl limit

Assume every Hausdorff corner is positive and let `mu_n` be the positive
`n`-node Gaussian measure. It is supported on `[0,4]`, has mass `A_0`, and
matches

\[
 \int u^k\,d\mu_n=A_k\qquad(0\le k\le2n-1).
\]

Positive fixed-mass measures on compact `[0,4]` are weakly compact. Every
subsequential limit has all source moments, since each fixed moment is
eventually matched exactly. The compact Hausdorff problem is determinate, so
all subsequential limits coincide and

\[
 \mu_n\Longrightarrow\mu.
\]

For

\[
 R_n(h)=\int_0^4\frac{d\mu_n(u)}{1+hu},
\]

the kernels are uniformly bounded on compact subsets of
`C minus (-infinity,-1/4]`. Weak convergence plus normal-family bounds gives
locally uniform analytic convergence to `R_mu` there.

Near zero the limit has source jet

\[
 R_\mu(h)=\sum_{k\ge0}(-1)^kA_kh^k.
\]

If the completed Xi source resolvent is analytic on the same connected domain,
the identity theorem identifies it with `R_mu`. Thus all-order positivity
automatically closes weak existence, uniqueness, local uniform convergence,
and source identification.

Jacobi coefficient asymptotics remain important for explaining the Sommerfeld
counting law, but are not needed to manufacture the limiting measure.

## Scope

This is conditional on every corner. Four certified corners do not prove RH.

## Durable verification

- `quarter-point-degree-nine-truncated-measure-theorem.md`
- `results/quarter-point-pade-gaussian-identity.json`
- `results/jacobi-positive-resolvent-monotonicity.json`
