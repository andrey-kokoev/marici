# The odd theta-to-window compression is the unique normalized reflection intertwiner

## Frozen source data

On the reciprocal theta endpoint plane, use

\[
e_{\mathrm{wall}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
1
\end{pmatrix},
\qquad
e_{\mathrm{jump}}
=
\frac1{\sqrt2}
\begin{pmatrix}
1\\
-1
\end{pmatrix}.
\]

The independently normalized odd Wronskian current is

\[
j_\theta
=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}
=
\frac1{2\sqrt2}e_{\mathrm{jump}}.
\]

On the Stieltjes side, the independently constructed odd boundary is

\[
d_p=W_{2\log p}-W_{\log p}.
\]

Both change sign under reciprocal reflection.

## Canonical odd covector

The source metric on the theta endpoint plane gives the normalized odd
coordinate functional

\[
\ell_{\mathrm{jump}}(y)
=
2\sqrt2\,
\langle e_{\mathrm{jump}},y\rangle.
\]

It satisfies

\[
\ell_{\mathrm{jump}}(j_\theta)=1,
\qquad
\ell_{\mathrm{jump}}(e_{\mathrm{wall}})=0.
\]

No coefficient is fitted here: the factor \(2\sqrt2\) is forced by the exact
Wronskian normalization \(j_\theta=(1/4,-1/4)^T\).

## Rank-one compression

Define

\[
K_p^{\mathrm{odd}}
=
d_p\otimes\ell_{\mathrm{jump}},
\]

so that

\[
K_p^{\mathrm{odd}}y
=
\ell_{\mathrm{jump}}(y)d_p.
\]

Then

\[
K_p^{\mathrm{odd}}j_\theta=d_p,
\qquad
K_p^{\mathrm{odd}}e_{\mathrm{wall}}=0,
\]

and

\[
K_p^{\mathrm{odd}}e_{\mathrm{jump}}
=
2\sqrt2\,d_p.
\]

This map is reflection equivariant because both its covector and target
generator are odd.

## Uniqueness theorem

Let \(K:E_p^\theta\to\operatorname{span}\{d_p\}\) be linear and satisfy:

1. \(K\) intertwines reciprocal reflection;
2. \(K\) annihilates the even wall line;
3. \(Kj_\theta=d_p\).

Then \(K=K_p^{\mathrm{odd}}\).

Indeed, reflection equivariance and wall annihilation force \(K\) to factor
through the one-dimensional odd quotient. The normalization on the nonzero
vector \(j_\theta\) fixes the remaining scalar.

Thus there is exactly one finite coefficient-level comparison compatible with
the frozen source data.

## Norm and completion direction

Its norm is

\[
\|K_p^{\mathrm{odd}}\|
=
2\sqrt2\,\|d_p\|_{\mathrm{win}}.
\]

The established Stieltjes estimate implies

\[
\|K_p^{\mathrm{odd}}\|
\le
C'
(\log p)^{-1/2}
\exp\left[
-\frac\pi8(\log p)^2
\right].
\]

Hence

\[
\sum_p\|K_p^{\mathrm{odd}}\|<\infty.
\]

The prime direct sum of odd compressions is trace class from the retained
theta odd carrier into the raw Stieltjes disagreement carrier.

Its inverse on each finite odd line exists algebraically but has
super-polynomially growing norm. Therefore no completed inverse is admitted.

## Endpoint-loaded formula

Since

\[
V_pe_{\mathrm{jump}}
=
\lambda_{\mathrm{jump},p}e_{\mathrm{jump}},
\qquad
\lambda_{\mathrm{jump},p}
=
\frac12(1-p^{-1}),
\]

we obtain

\[
K_p^{\mathrm{odd}}V_pe_{\mathrm{jump}}
=
\sqrt2(1-p^{-1})d_p.
\]

Equivalently,

\[
K_p^{\mathrm{odd}}V_pj_\theta
=
\frac12(1-p^{-1})d_p.
\]

This is the exact coefficient-level endpoint-to-Stieltjes odd comparison.

## Authority boundary

The rank-one map is source-derived in the coefficient category once the
following are admitted:

- the theta endpoint metric;
- the exact Wronskian current \(j_\theta\);
- reciprocal reflection;
- the Stieltjes generator \(d_p\);
- tensor evaluation and synthesis.

This does not yet prove that the analytic causal-history constructor realizes
the same map. That remaining statement is the commutative square

\[
\operatorname{Tr}_{\mathrm{win}}
\mathfrak S_{1,p}
=
K_p^{\mathrm{odd}}
\operatorname{Tr}_{\theta}
\]

on the declared history core.

The left side is an analytic trace of the source Volterra/Stokes constructor.
The right side is now completely fixed. Their equality is falsifiable and has
no adjustable scalar.

## Hostiles

Changing \(j_\theta\) to \(-j_\theta\) reverses the compression sign while
leaving all even energies unchanged.

Replacing \(d_p\) by a scalar multiple preserves reflection character but
violates the source Stieltjes normalization.

Adding a wall component violates reflection equivariance.

These exhaust the finite rank-one freedoms.

## Verdict

The coefficient-level odd comparison is no longer missing. It is the unique
normalized reflection intertwiner

\[
K_p^{\mathrm{odd}}
=
d_p\otimes
\left(
2\sqrt2\,\langle e_{\mathrm{jump}},\cdot\rangle
\right).
\]

It is trace class across primes and has the correct completion direction. The
next gate is solely analytic: prove that the causal-history trace implements
this already-fixed rank-one map.
