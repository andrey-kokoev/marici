# 1680 — Correlated Cut Positivity Is a Joint-Moment Congruence

## Correlated positivity falsifier

Entry 1679 proves positivity of independent Cut merge using

\[
H_X\otimes H_Y.
\]

Replace independence by a complete correlated joint moment functional and
determine which data are required.

Let (M_{XY}) be the multivariate moment matrix indexed by monomials

\[
x^iy^j,
\qquad i+j\le d.
\]

For

\[
Z=\alpha X+\beta Y,
\]

substitution of (z^k) defines a matrix (T). Direct evaluation gives

\[
\boxed{
H_Z=T^TM_{XY}T.
}
\]

Therefore the complete joint positive functional descends by positive
congruence exactly as in the independent case.

## Marginal falsifier

Take three centered Rademacher pairs:

- independent (X,Y);
- perfectly correlated (Y=X);
- perfectly anticorrelated (Y=-X).

All three have identical marginal moments at every order. Yet

\[
\operatorname{Var}(\alpha X+\beta Y)
=
\begin{cases}
\alpha^2+\beta^2,&\text{independent},\\
(\alpha+\beta)^2,&Y=X,\\
(\alpha-\beta)^2,&Y=-X.
\end{cases}
\]

For nonzero (alpha,\beta), these values differ. Marginal Hankel matrices
therefore cannot reconstruct the merged state.

The exact checker verifies 36 correlated positive cases through degree four,
486 multivariate congruence entries, 486 positive Gram entries, and equality of
the marginal moments through order eight.

## Narrow result

\[
\boxed{
\text{correlated Cut positivity requires the joint moment matrix and then descends by congruence.}
}
\]

The missing information in a marginal treatment is exactly the labelled mixed
moment/cumulant sector identified in Entry 1677. This remains coefficient data
over the existing occurrence carrier; no correlation-specific Cut cell is
needed.

## Durable artifacts

- `research/benincasa/checkers/correlated_moment_congruence.rs`
- `research/benincasa/results/correlated-moment-congruence.json`
- `research/benincasa/correlated-moment-congruence.md`

## Next falsifier

Test nonlinear scalar-cubic evolution against these finite positive cones.
Compute whether the truncated generator is conditionally positive/tangent to
the Hankel cone at its boundary, or whether preserving positivity necessarily
requires coupling to the next moment grade.