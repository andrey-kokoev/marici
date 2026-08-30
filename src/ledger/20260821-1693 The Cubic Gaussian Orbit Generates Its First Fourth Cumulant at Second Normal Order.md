# 1693 — The Cubic Gaussian Orbit Generates Its First Fourth Cumulant at Second Normal Order

## Frontier

Entry 1692 identifies the connected third cumulant as the first tangent of the
exact cubic density-state orbit.  Compute its first genuinely fourth-cumulant
grade and retain the full density-state completion.

## Exact calculation

For an initially diagonal centered Gaussian, write

\[
\langle Q^2\rangle=a,
\qquad
\langle P^2\rangle=b,
\qquad
\Pi_t=P-t(Q^2-a).
\]

Wick contraction gives

\[
\langle \Pi_t^2\rangle=b+2t^2a^2,
\]

and

\[
\langle Q^2\Pi_t^2\rangle=ab+10t^2a^3.
\]

Hence

\[
\boxed{
\kappa_{QQ\Pi\Pi}=8t^2a^3.
}
\]

The pure momentum fourth cumulant starts only at fourth order:

\[
\kappa_{\Pi\Pi\Pi\Pi}=48t^4a^4.
\]

## Narrow result

\[
\boxed{
\text{the first source-derived connected fourth cumulant occurs at second cubic normal order and is fixed by the exact density-state orbit.}
}
\]

Its degree-six and degree-eight completion is not an independent extension
problem: every moment is evaluated in

\[
\rho_t=U_t\rho_0U_t^\dagger.
\]

This provides one physical fourth-cumulant ray inside the ordered moment cone.
It does not identify Entry 1630's arbitrary `Z` direction with that ray.

## Architectural consequence

The source coefficient filtration begins

\[
\text{Gaussian covariance}
\longrightarrow
\kappa_3\text{ at order }t
\longrightarrow
\kappa_4\text{ at order }t^2.
\]

The first-jet calculus therefore cannot control the first source-derived
fourth-cumulant deformation.  This mirrors the three-site elliptic warning:
higher integrated/coefficient structure can begin at second normal order while
the carrier remains unchanged.

## Durable artifacts

- `research/benincasa/checkers/gaussian_cubic_second_grade.rs`
- `research/benincasa/results/gaussian-cubic-second-grade.json`
- `research/benincasa/gaussian-cubic-second-grade.md`

## Next falsifier

Test Cut compatibility of this source-derived second-grade cumulant.  For two
independent Gaussian blocks followed by cardinality-weighted merge, compare
the merged `kappa_QQPiPi` with the cumulant partition law.  Then repeat with a
nonzero cross covariance to determine whether the complete joint-cumulant
object of Entry 1677 is sufficient without a new carrier operation.
