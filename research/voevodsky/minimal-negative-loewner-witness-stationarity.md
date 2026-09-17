# Stationarity equations for a minimal negative Loewner witness

Let

\[
L(x,y)=a(x)a(y)q(x,y),\qquad
a(x)=(x-1/4)I(x),
\]

where, on a zero-free real interval,

\[
q(x,y)=\frac{R(y)-R(x)}{x-y},\qquad R=P/I=-H.
\]

Congruence by the real diagonal matrix `diag(a(x_i))` shows that a negative
Loewner witness for `L` is equivalent to one for `q`, provided no node is a
zero of `a`. Thus the node geometry can be studied using `q` without the
outer theta amplitudes.

## What minimal rank already forces

Choose a negative witness with the least possible matrix size `n`. Every
proper principal submatrix is then positive semidefinite; otherwise deleting
the complementary nodes gives a smaller witness. Cauchy interlacing therefore
shows that the full matrix has exactly one negative eigenvalue (though it may
also have zero eigenvalues).

If `v` is an eigenvector for that negative eigenvalue, every coordinate of
`v` is nonzero. Indeed, if `v_i=0`, deleting coordinate `i` preserves the same
negative Rayleigh quotient and contradicts minimality.

A minimal witness also has distinct nodes. If `x_i=x_j`, rows `i` and `j` are
identical. Combining their coefficients replaces `(v_i,v_j)` by the single
coefficient `v_i+v_j` without changing the quadratic form; if that sum
vanishes, the duplicated pair contributes nothing. Either way a negative
witness of smaller size results.

These conclusions require no minimization over node positions.

## Exact one-step obstruction

Separate the last node and write the minimal witness as

\[
Q_n=\begin{pmatrix}A&b\\b^T&d\end{pmatrix},
\qquad A\succeq0.
\]

The generalized Schur-complement criterion gives exactly two possible
failures:

\[
\boxed{b\notin\operatorname{ran}A}
\]

or

\[
\boxed{b\in\operatorname{ran}A,
\qquad d-b^TA^\dagger b<0.}
\]

Here `A^dagger` is the Moore--Penrose inverse. In the nonsingular case the
second alternative is simply

\[
q(x_n,x_n)<b^TA^{-1}b.
\]

Thus every minimal violation is already a failed one-point extension of a
positive `(n-1)`-node packet. In RKHS language, the old packet assigns to the
new evaluation vector a minimum interpolation norm larger than its declared
squared norm `q(x_n,x_n)=-R'(x_n)`. This is a sharper target than arbitrary
matrix negativity: a proof may establish the one-point extension inequality
directly from the theta source.

## Interior extremizer equations

Fix a rank `n`, distinct interior nodes `x_1<...<x_n`, and let

\[
Q_{jk}=q(x_j,x_k).
\]

Suppose its smallest eigenvalue `lambda<0` is simple and locally minimal as a
function of all nodes. Choose a real normalized eigenvector `v`. Eigenvector
variation gives

\[
\boxed{\sum_k q(x_j,x_k)v_k=\lambda v_j.}
\]

Node variation gives

\[
\frac{\partial\lambda}{\partial x_i}
 =2v_i\sum_jv_j\partial_1q(x_i,x_j).
\]

After deleting any zero coordinate of `v` (which would give a lower-rank
witness), minimal rank forces `v_i != 0`. Hence every interior node obeys

\[
\boxed{\sum_jv_j\partial_1q(x_i,x_j)=0.}
\]

For `x != y`,

\[
\partial_1q(x,y)=
\frac{-(x-y)R'(x)-R(y)+R(x)}{(x-y)^2},
\]

while analytic confluence gives

\[
q(x,x)=-R'(x),\qquad
\partial_1q(x,x)=-\frac12R''(x).
\]

Thus any attained simple interior minimal counterexample must solve the finite
nonlinear system

\[
\sum_jv_j\frac{R(x_j)-R(x_i)}{x_i-x_j}=\lambda v_i,
\]

with diagonal value `-R'(x_i)`, together with

\[
-\frac12v_iR''(x_i)
+\sum_{j\ne i}v_j
\frac{-(x_i-x_j)R'(x_i)-R(x_j)+R(x_i)}{(x_i-x_j)^2}=0.
\]

Substitution `R=P/I` rewrites every term using the paired theta transforms

\[
I(x)=\int_0^\infty K(u)\phi_x(u)du,
\qquad
P(x)=\int_0^\infty\Phi(u)\psi_x(u)du.
\]

These are the exact equations that a theta-source contradiction would need to
exclude.

## What this does not yet justify

Minimal rank alone does not imply stationarity in the node variables and does
not guarantee that the node infimum is attained: nodes may collide, approach
a transform zero, or escape to an endpoint or infinity. A complete
contradiction proof must therefore handle four strata:

1. distinct interior nodes (the equations above);
2. confluent nodes, producing derivative Loewner matrices;
3. nodes at zeros of `a`, where the congruence reduction is singular;
4. endpoint or infinite escape.

Nor may simplicity of the lowest eigenvalue be assumed globally. For a
multiple lowest eigenvalue, stationarity is a convex-subgradient condition on
the compressed derivative matrices.

Accordingly, the next useful theorem is a compactification lemma: every
negative Loewner witness either yields an attained interior extremizer of the
form above or yields an explicit negative confluent/zero/escape witness. Only
after that lemma does exclusion of the displayed stationary system prove
absence of all violations.
