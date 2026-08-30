# 1670 — Singular Gaussian Conditioning Has a Covariance-Rees Direction

## Singular-boundary falsifier

Entry 1669 proves correlated Gaussian Cut descent when the conditioned
covariance block is invertible. Approach the first singular stratum and test
whether positivity and the ordinary limiting covariance determine the
Schur-complement limit.

Take

\[
\Sigma(t)=
\begin{pmatrix}
a&t\gamma\\
t\gamma&t^2\beta
\end{pmatrix},
\qquad
\beta>0.
\]

Its determinant is

\[
\det\Sigma(t)=t^2(a\beta-\gamma^2),
\]

so positivity permits

\[
0\le\frac{\gamma^2}{\beta}\le a.
\]

For every (t\ne0), the conditional covariance is

\[
\Sigma_{A\mid B}
=a-\frac{(t\gamma)^2}{t^2\beta}
=a-\frac{\gamma^2}{\beta}.
\]

Yet all families have the same ordinary limit

\[
\Sigma(0)=
\begin{pmatrix}a&0\\0&0\end{pmatrix}.
\]

Therefore the finite conditional limit depends on the exceptional coordinate

\[
\lambda=\frac{c^2}{b}=\frac{\gamma^2}{\beta}.
\]

If instead (c=t^2\gamma), then (lambda\to0) and the conditional covariance
specializes to (a). The rate of approach is genuine filtered data.

The exact checker audits 4,008 positive Rees families and 8,400 faster-decay
families. Each of twenty tested ordinary boundary points admits multiple
positive Schur limits.

## Narrow result

\[
\boxed{
\text{singular Gaussian conditioning has no canonical ordinary specialization; it requires the coefficient direction }c^2/b.
}
\]

This is a weighted/Rees refinement of the Gaussian coefficient object. It is
not evidence for a new cosmological Cut stratum: the underlying support remains
the existing singular covariance divisor. A physical value of \(\lambda\)
requires a source-derived approach or relative-cycle prescription.

## Durable artifacts

- `research/benincasa/checkers/singular_covariance_rees_conditioning.rs`
- `research/benincasa/results/singular-covariance-rees-conditioning.json`
- `research/benincasa/singular-covariance-rees-conditioning.md`

## Next falsifier

Construct the weighted covariance chart with coordinates

\[
b=t^2\beta,
\qquad
c=t\gamma,
\qquad
\lambda=c^2/b,
\]

and test nested conditioning for a three-block covariance matrix. Determine
whether all Schur complements glue as rational functions of the exceptional
coefficient coordinates, or whether overlap coherence produces a supported
secondary class.
