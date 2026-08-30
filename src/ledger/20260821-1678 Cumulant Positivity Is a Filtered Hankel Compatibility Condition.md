# 1678 — Cumulant Positivity Is a Filtered Hankel Compatibility Condition

## Realizability falsifier

Entry 1677 proves algebraic descent of the complete joint cumulant tensor. Test
whether an arbitrary finite cumulant packet defines a positive moment
functional after descent.

Moments and cumulants obey

\[
m_n
=
\sum_{k=1}^n
\binom{n-1}{k-1}\kappa_km_{n-k},
\qquad m_0=1.
\]

Therefore positivity couples cumulant orders through the Hankel matrices

\[
H_d=(m_{i+j})_{0\le i,j\le d}.
\]

For a centered packet with

\[
\kappa_2=1,
\]

the order-four moment matrix is positive semidefinite exactly when

\[
\boxed{\kappa_4\ge-2.}
\]

If additionally (kappa_4=0), the order-six matrix is positive semidefinite
exactly when

\[
\boxed{\kappa_6\ge-6.}
\]

Thus the packet

\[
\kappa_2=1,
\qquad
\kappa_4=0,
\qquad
\kappa_6=-7
\]

is positive through order four and fails at order six.

The exact checker verifies all principal minors for 25 fourth-order boundary
values and 61 sixth-order boundary values, together with positive and failing
extension examples.

## Narrow result

\[
\boxed{
\text{cumulant positivity is filtered Hankel compatibility, not species-local data.}
}

A finite grade has a finite positivity cone. Global positivity requires a
compatible inverse system across all grades, matching Entry 1648's infinite
filtered moment object. This does not prevent useful finite positive
truncations; it prevents treating arbitrary species coefficients as
independently admissible.

No new carrier structure appears. Positivity is an additional constraint on
the sector-specific coefficient object.

## Durable artifacts

- `research/benincasa/checkers/filtered_hankel_cumulant_positivity.rs`
- `research/benincasa/results/filtered-hankel-cumulant-positivity.json`
- `research/benincasa/filtered-hankel-cumulant-positivity.md`

## Next falsifier

Test whether cardinality-weighted independent Cut merge maps each finite
Hankel cone into the corresponding cone at the same grade. Prove this directly
as a positive pullback on truncated polynomial squares, rather than inferring
it from an assumed underlying probability measure.
