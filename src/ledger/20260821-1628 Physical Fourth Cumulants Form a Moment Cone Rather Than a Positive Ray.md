# 1628 — Physical Fourth Cumulants Form a Moment Cone Rather Than a Positive Ray

## Problem

Entry 1627 finds that the connected fourth-cumulant covariance residual is sign-indefinite.  Does either sign imply an unphysical state?

## Truncated moment object

For a centered \(q\)-marginal, define

\[
\mu_{2r}=\langle q^{2r}\rangle,
\qquad
\kappa_4=\mu_4-3\mu_2^2.
\]

The degree-eight moment matrix is

\[
M_4=
\begin{pmatrix}
1&\mu_2&\mu_4\\
\mu_2&\mu_4&\mu_6\\
\mu_4&\mu_6&\mu_8
\end{pmatrix}.
\]

Physical measure positivity requires \(M_4\succeq0\); it does not require \(\kappa_4\geq0\).

## Two exact physical witnesses

At fixed variance \(\mu_2=1\), the symmetric two-point distribution

\[
q=\pm1
\]

has

\[
(\mu_4,\mu_6,\mu_8)=(1,1,1),
\qquad
\kappa_4=-2.
\]

The symmetric sparse distribution

\[
P(0)=\frac34,
\qquad
P(2)=P(-2)=\frac18
\]

has

\[
(\mu_4,\mu_6,\mu_8)=(4,16,64),
\qquad
\kappa_4=1.
\]

Both exact moment matrices are positive semidefinite.  The checker verifies every principal minor.

## Narrow result

\[
\boxed{
\text{Both signs of the connected fourth cumulant occur in physical positive moment objects.}
}
\]

Therefore Entry 1627's sign-indefinite covariance residual is not itself a positivity failure.  The physical coefficient object is the coupled moment matrix—or its quantum phase-space refinement—not the isolated scalar \(\kappa_4\).

## Type qualification

The displayed construction is a classical one-coordinate marginal and hence a necessary slice of the quantum moment cone.  The complete quantum object must include:

- mixed \(q,p\) moments;
- Weyl ordering;
- canonical-commutator localizing constraints;
- mode and occurrence labels;
- source density-matrix hermiticity.

## Architectural consequence

The higher cumulant layer is not an arbitrary coefficient vector.  It is constrained by a positive semidefinite moment object containing several normal grades simultaneously:

\[
V_2, \kappa_4, M_6, M_8,\ldots
\]

This is another instance where a single associated grade is insufficient, while no new carrier stratum is indicated.

## Durable artifacts

- `research/benincasa/checkers/fourth_cumulant_moment_cone.rs`
- `research/benincasa/results/fourth-cumulant-moment-cone.json`
- `research/benincasa/fourth-cumulant-moment-cone.md`

## Next falsifier

Construct the smallest Weyl-ordered quantum phase-space moment matrix containing \(V_{qq},V_{qp},V_{pp},\kappa_{qqqq},\kappa_{pqqq}\).  Impose the canonical commutator exactly and test whether Entry 1627's residual functional is bounded on each fixed-covariance fiber.  An unbounded functional would show that higher moments beyond degree four are mandatory for dynamical control.
