# 1672 — Rank-One Covariance Has an Intrinsic Restriction but a Secondary Normal Grade

## Rank-one falsifier

Entry 1671 reduces weighted three-block conditioning to the exceptional
determinant

\[
bd-z^2=0.
\]

Distinguish restriction to the exact rank-one stratum from specialization of
nearby positive covariance families.

Choose an adapted basis in which

\[
K_0=\begin{pmatrix}k&0\\0&0\end{pmatrix},
\qquad k>0.
\]

For the full covariance

\[
\begin{pmatrix}
a&x&y\\
x&k&0\\
y&0&0
\end{pmatrix},
\]

positivity of the principal minor on the first and null coordinates gives

\[
-y^2\ge0,
\]

and therefore (y=0). The cross vector lies in the image of (K_0), so the
Moore--Penrose correction

\[
\frac{x^2}{k}
\]

is intrinsic on the exact rank-one stratum.

Now approach it through

\[
K_t=\begin{pmatrix}k&0\\0&t^2\beta\end{pmatrix},
\qquad
v_t=(x,t\gamma).
\]

The Schur correction is

\[
v_t^TK_t^{-1}v_t
=\frac{x^2}{k}+\frac{\gamma^2}{\beta}.
\]

All such families share the same ordinary rank-one boundary value, but the
second term survives as a flagged normal coordinate.

The exact checker verifies 820 exact-stratum positivity tests and 174,376
positive nearby families. It finds multiple limits at 2,652 identical rank-one
boundary points.

## Narrow result

\[
\boxed{
\text{rank-one restriction is intrinsic, but nearby conditioning carries a secondary normal grade.}
}
\]

There is no new carrier divisor: the support remains the exceptional
determinant already identified in Entry 1671. What grows is the filtered
Gaussian coefficient object. Ordinary restriction and nearby specialization
must not be identified.

## Durable artifacts

- `research/benincasa/checkers/rank_one_exceptional_covariance_normal.rs`
- `research/benincasa/results/rank-one-exceptional-covariance-normal.json`
- `research/benincasa/rank-one-exceptional-covariance-normal.md`

## Next falsifier

Determine whether successive covariance-rank drops are governed uniformly by
the complete flag of null directions. Formulate the rank-\(r\) local normal
model and test whether each new finite Schur correction is exactly one
quadratic Rees ratio per newly vanishing eigen-direction. A failure would be
the first indication that covariance coefficients require structure beyond
flagged normal geometry.