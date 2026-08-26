# Determinant nonvanishing controls coercivity only with a cofactor bound

Owner: `marici.Kitaev`

## Bounded question

Can a scalar determinant or completed section control the least singular value
of a genuinely source-derived higher-rank detector without simply restating
scalar nonvanishing?

## Exact bridge

Let \(D:V\to W\) be an operator between Hermitian spaces of equal finite rank
\(r\), with singular values

\[
\sigma_1\ge\cdots\ge\sigma_r\ge0.
\]

Then

\[
|\det D|=\prod_{j=1}^r\sigma_j,
\qquad
\lVert\Lambda^{r-1}D\rVert=prod_{j=1}^{r-1}\sigma_j.
\]

Whenever \(D\) is invertible,

\[
\sigma_{\min}(D)
=
\frac{|\det D|}{\lVert\Lambda^{r-1}D\rVert}.
\]

Thus a determinant lower bound yields coercivity precisely when the
codimension-one exterior power, equivalently the cofactor operator, has a
uniform upper bound.

The weaker but often convenient estimate is

\[
\sigma_{\min}(D)
\ge
\frac{|\det D|}{\lVert D\rVert^{r-1}}.
\]

## Determinant alone fails

The rank-two family

\[
D_N=\operatorname{diag}(N,N^{-1})
\]

has determinant one for every cutoff, yet

\[
\sigma_{\min}(D_N)=N^{-1}\longrightarrow0.
\]

The missing information escapes through
\(\lVert\Lambda^1D_N\rVert=\lVert D_N\rVert=N\). Therefore even a constant,
nonzero completed determinant cannot certify a uniform graph estimate unless
operator growth is controlled independently.

## Higher-rank source content

This bridge is not a scalar reformulation if all of the following are supplied
before determinant projection:

1. a source-derived rank-\(r\) operator complex;
2. frozen Hermitian or graph norms on source and target;
3. a typed detector differential \(D_N(s)\);
4. an independently proved uniform bound on
   \(\Lambda^{r-1}D_N(s)\); and
5. identification of the scalar Tate section with \(\det D_N(s)\).

Then scalar divisor avoidance plus the cofactor bound implies source-line
conservativity. Without item 4, determinant control is insufficient. Without
items 1--3 and 5, the construction is not source-authorized.

On a one-dimensional detector, \(\Lambda^0D=1\), so the identity reduces to
\(\sigma_{\min}(D)=|\det D|\). It adds no information there and must not be
presented as an explanation of scalar nonvanishing.

## Frame covariance

Under \(D'=BDA^{-1}\), determinant and cofactor norms change separately.
Uniformly bounded invertible source and target frames preserve the existence
of determinant lower bounds, cofactor upper bounds, and hence coercivity, up
to fixed constants. Unbounded frames can transfer growth between determinant
and cofactor channels and are not authorized equivalences.

## Finite falsifiers

- determinant bounded away from zero while cofactor norm diverges;
- determinant identification fitted only after scalar projection;
- operator rank changes with cutoff;
- cofactor estimate uses an unbounded source trivialization;
- determinant and detector live in unmatched coefficient or norm conventions.

## Disposition

The first genuinely higher-rank route is a determinant--cofactor theorem, not
a bare determinant theorem. It provides an independently testable operator
datum: bounded codimension-one exterior transport. No such typed theta/Tate
operator complex or cofactor estimate is currently supplied, so this is a
compiler target rather than an RH result.

## Claim strength

Exact finite-dimensional singular-value theorem and source-typing compiler.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_determinant_coercivity.py`.
The result is written to
`research/kitaev/results/theta-determinant-coercivity.json`.

