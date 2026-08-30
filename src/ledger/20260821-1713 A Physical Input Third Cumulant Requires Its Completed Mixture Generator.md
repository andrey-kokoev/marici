# 1713 — A Physical Input Third Cumulant Requires Its Completed Mixture Generator

## Non-Gaussian-input falsifier

Entry 1712 closes cubic evolution of Gaussian input at every Rees grade.  Add a
predeclared, density-representable connected third cumulant and test whether it
is a closed coefficient extension.

## Physical finite mixture

Begin with a physical Gaussian density state and form the convex mixture of
two `Q`-displaced copies:

\[
\mu_1=2d,
\qquad p_1=\frac13,
\qquad
\mu_2=-d,
\qquad p_2=\frac23.
\]

The mixture is centered.  With common within-component variance `a`, its
connected coefficients are

\[
A=a+2d^2,
\]

\[
\kappa_3(Q)=2d^3,
\qquad
\kappa_4(Q)=-6d^4.
\]

Thus a physical nonzero third cumulant already arrives with a source-fixed
higher tower.

## Complete evolved generator

Let

\[
D=1+2aty.
\]

Exact Gaussian integration in each mixture component gives

\[
\boxed{
M(x,y)=e^{by^2/2+tAy}D^{-1/2}
\sum_{j=1}^2p_j
\exp\!\left(
\frac{ax^2+2\mu_jx-2ty\mu_j^2}{2D}
\right).
}
\]

The cumulant generator is the Gaussian rational/logarithmic term plus one
finite log-sum-exp factor.

The first cubic response satisfies

\[
\boxed{
\kappa_{QQ\Pi}
=-t\left(2A^2+\kappa_4(Q)\right).
}
\]

It depends on the tied fourth cumulant, not on `kappa_3` alone.

## Narrow result

\[
\boxed{
\text{a standalone physical input third cumulant is not dynamically closed; the minimal tested completion is the full finite-mixture generating factor.}
}
\]

The extra datum is a sector-specific completed coefficient object.  It does
not introduce a new carrier incidence.  Finite atomic mixtures remain finitely
presented, but the Gaussian presentation itself is not universal.

## Durable artifacts

- `research/benincasa/checkers/nongaussian_input_cubic_generator.rs`
- `research/benincasa/results/nongaussian-input-cubic-generator.json`
- `research/benincasa/nongaussian-input-cubic-generator.md`

## Next falsifier

Test Cut descent of finite mixture generators.  Determine whether independent
mixtures close under labelled Cartesian product and cardinality-weighted merge,
and whether the number of mixture components multiplies without requiring a
new carrier operation.  Then test correlated mixture labels separately.
