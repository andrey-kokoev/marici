---
id: 554
date: 2026-08-18
title: Gysin Variance Does Not Select One Kummer Resonance Grade
authors:
  - marici.Nima
---

# Gysin Variance Does Not Select One Kummer Resonance Grade

Entries 552--553 locate the supported lower object at the coefficient divisor
\(\lambda=0\), with normal complex

\[
N=[R\xrightarrow{\lambda}R],
\qquad R=\mathbb Q[\lambda].
\]

Entry 544 includes both ordinary and extraordinary restriction in its
mixed-variance kernel calculus. This entry tests whether choosing Gysin
variance already selects one of the two resonant normal grades.

Let \(i:\{\lambda=0\}\hookrightarrow\mathbb A^1_\lambda\). Derived ordinary
restriction gives

\[
Li^*N
=
[\,\mathbb Q\xrightarrow{0}\mathbb Q\,].
\]

For a regular codimension-one embedding and a perfect complex, purity gives

\[
i^!N
\simeq
Li^*N\otimes\det(N_i)[-1].
\]

The determinant twist and cohomological shift change typing, but not the
number of nonzero normal grades. Therefore

\[
\boxed{
\dim H(Li^*N)=(1,1),
\qquad
\dim H(i^!N)=(1,1)
\text{ up to shift}.
}
\]

Neither star nor shriek variance canonically discards one copy.

## Consequence

Entry 544 supplies the correct six-functor operations, but its variance data
alone does not close Entry 552's selection problem. A single rank-five
tangential grade requires an additional datum:

- a declared perverse or ordinary \(t\)-structure truncation;
- a nearby/vanishing-cycle convention with a specified degree;
- or a physical relative-chain boundary condition that realizes one of those
  truncations.

Without such data, applying \(i^!\) merely because the desired operation is
called Gysin would hide rather than solve the doubled-grade problem.

This is a cross-sector boundary of H2:

\[
\boxed{
\text{shared six-functor calculus}
\quad\not\Rightarrow\quad
\text{shared canonical truncation}.
}
\]

The next admissible calculation must extract the truncation from the physical
integration-chain complex or from an independently declared perverse
normalization. It may not be selected by rank matching.

The executable audit is
\`research/benincasa/check_generic_lower_resonant_variance.py\`.
