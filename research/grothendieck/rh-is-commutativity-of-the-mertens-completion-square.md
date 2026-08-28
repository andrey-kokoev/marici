# RH is commutativity of the Mertens--completion square

## The source-side finite-cutoff path

Let `T` have the centered Cauchy distribution of scale `1/2`, and let

\[
Z_X(t)=\prod_{p\le X}(1-p^{-1/2-it})^{-1}.
\]

The exact finite-cutoff calculation gives

\[
\mathbb E\log|Z_X(T)|
=
\sum_{p\le X}-\log(1-p^{-1}).
\]

Mertens' product theorem therefore supplies the source-side normalization

\[
\lim_{X\to\infty}
\left(
\mathbb E\log|Z_X(T)|-log\log X-\gamma
\right)
=0.
\]

This route uses finite prime labels, the Cauchy character pairing, and the
classical Mertens normalization. It does not continue the Euler logarithm
through its convergence boundary.

## The completed-boundary path

Analytically complete the Euler object first, remove the endpoint pole, and
then take the critical-boundary Cauchy expectation. The result is

\[
\mathcal D_{\mathrm{BSY}}
=
\frac1{2\pi}
\int_{-\infty}^{\infty}
\frac{\log|\zeta(\tfrac12+it)|}
     {\tfrac14+t^2}\,dt.
\]

Poisson--Jensen gives

\[
\mathcal D_{\mathrm{BSY}}
=
\sum_{\Re\rho>1/2}
m_\rho\log\left|\frac\rho{1-\rho}\right|.
\]

Thus the discrepancy from the zero source-side finite part is exactly the
positive off-seam divisor entropy.

## The square

There are two paths from finite labelled Euler data to a scalar finite part:

```text
finite labelled Euler products
    |                         |
    | Cauchy expectation      | theta--Tate completion
    v                         v
positive Mertens sum         completed critical boundary
    |                         |
    | subtract universal      | Cauchy expectation
    | log-log divergence      |
    v                         v
    0              versus     D_BSY
```

Let `C=0` denote commutativity of these two routes. Then

\[
\mathrm{RH}
\quad\Longleftrightarrow\quad
\mathcal D_{\mathrm{BSY}}=0
\quad\Longleftrightarrow\quad
C=0.
\]

## Why this is useful

This isolates the missing theorem as a compatibility statement between two
independently meaningful normalizations. A proof need not estimate individual
zeros. It must show that completed theta--Tate sewing preserves the finite
part selected by finite labelled Euler reconstruction and Mertens
normalization.

A hostile reciprocal and conjugation-symmetric multiplier inserting an
off-line quartet leaves superficial functional-equation metadata unchanged
but adds a positive lower-path anomaly. A successful source theorem must
reject that multiplier or detect its anomaly before inspecting its zeros.

## Noncircular acceptance contract

A valid commutativity theorem must:

1. construct every finite Euler cutoff from labelled prime-power data;
2. derive the Cauchy pairing before completion;
3. retain primitive, square, connected-tail, endpoint, and archimedean
   channels separately;
4. derive completion from theta--Tate sewing;
5. compare the two limits in one declared boundary-bearing topology;
6. explain why Mertens subtraction removes only the universal prime-current
   divergence and not divisor information;
7. avoid division by zeta, zero locations, or an RH-equivalent inequality.

The divergent unrenormalized expectations remain the first falsifier. Any
argument that silently interchanges cutoff, logarithm, boundary continuation,
expectation, and completion fails before reaching the divisor question.

## Rejected shortcut

An earlier draft used an Abel-damped logarithmic Dirichlet series and sent its
damping parameter to zero. That series is source-defined by absolute
convergence only while the shifted exponent remains to the right of `1`.
Continuing it to zero would import the very analytic continuation under audit.
The present finite-cutoff/Mertens formulation removes that circularity.

## Scope

This packet derives the two scalar paths and identifies their discrepancy
with the classical BSY sum. It reformulates RH as one source-normalized
commutativity theorem. It does not prove that theorem or RH.
