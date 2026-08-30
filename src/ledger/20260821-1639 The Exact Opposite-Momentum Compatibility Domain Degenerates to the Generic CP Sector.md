# 1639 — The Exact Opposite-Momentum Compatibility Domain Degenerates to the Generic CP Sector

## Question

Entry 1638 derived only the ordinary positive-semidefinite gate for a frozen opposite-momentum Gaussian correlation.  Determine the exact quantum compatibility domain and test whether it has a canonical product degeneration.

## Frozen covariance

Use

\[
V(x)=
\begin{pmatrix}
xI&cZ\\
cZ&aI
\end{pmatrix},
\qquad
c^2=a^2-1,
\]

with vacuum covariance normalized to (I).  Physicality requires

\[
V+i\Omega\succeq0.
\]

## Exact Schur complement

For (a>1),

\[
(aI+iJ)^{-1}=\frac{aI-iJ}{a^2-1},
\qquad ZJZ=-J.
\]

The quantum Schur complement is therefore

\[
xI+iJ-cZ(aI+iJ)^{-1}cZ
=(x-a)I.
\]

Hence

\[
\boxed{V(x)+i\Omega\succeq0\quad\Longleftrightarrow\quad x\ge a.}
\]

The source marginal (x=a) is exactly the boundary point.  Entry 1638's condition (xa\ge c^2) remains a valid ordinary necessary condition but is not sufficient quantum mechanically.

## Product degeneration

As (c\to0), the pure-support relation forces (a\to1).  The compatibility domain becomes

\[
x\ge1,
\]

which is the complete physical isotropic one-mode covariance domain.  Thus the supported correlated domain degenerates canonically to the generic product sector; no interpolation or fitted restriction map is needed at covariance level.

## Narrow result

\[
\boxed{
\text{Opposite-momentum Gaussian support is a proper quantum compatibility domain }x\ge a,
\text{ with the generic CP sector as its }c\to0\text{ degeneration.}
}
\]

This refines the proposed coefficient architecture: the supported object and the generic CP channel are not unrelated models.  They are neighboring strata of one support-sensitive Gaussian assignment geometry.

It does not yet construct a linear process-tensor Choi operator, prove complete positivity under arbitrary interventions, or identify the interacting restriction map after one cubic step.

## Durable artifacts

- `research/benincasa/checkers/quantum_correlated_compatibility_domain.rs`
- `research/benincasa/results/quantum-correlated-compatibility-domain.json`
- `research/benincasa/quantum-correlated-compatibility-domain.md`

## Next falsifier

Construct a one-step Gaussian intervention/process-tensor object over the exact domain (x\ge a).  Test positivity of the global cubic Cut evolution for every admitted Gaussian intervention and verify that its restriction at (c=0,a=1) agrees with Entry 1637's generic CP channel.  A failure of this degeneration at the interacting level would falsify the proposed common supported coefficient family.
