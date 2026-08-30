# 1618 — The Symmetric Finite-EFT Cut Measure Preserves the Gaussian Dyson Norm

## Frozen question

Does Entry 1617's integrand-level factorization

\[
R N R^\dagger=(RC)(RC)^\dagger
\]

survive integration over the finite excited-state EFT domain, without adding a fitted support prescription?

## Source-derived domain

The finite-EFT prescription of Entry 1603 restricts each internal excited occurrence separately.  For a cut pair with positive energies \(q\) and \(k\), freeze

\[
\mathcal D_\Lambda
=
\{q>0, k>0, q\leq\Lambda, k\leq\Lambda\}
\]

and the positive phase-space density

\[
d\mu_{qk}
\propto
\frac{d^3q}{(2q)(2k)}.
\]

Both the domain and density are invariant under the labelled occurrence exchange \(q\leftrightarrow k\).  A one-sided restriction such as \(q\leq\Lambda\) without the corresponding \(k\)-condition is not admitted.

## Finite check

The checker verifies positivity and exchange invariance on a deterministic positive grid:

\[
d\mu_{qk}>0,
\qquad
\mathbf 1_{\mathcal D_\Lambda}(q,k)
=
\mathbf 1_{\mathcal D_\Lambda}(k,q).
\]

Therefore, for every test vector \(v\),

\[
v^\dagger
\left[
\int_{\mathcal D_\Lambda}
d\mu_{qk},(RC)(RC)^\dagger
\right]v
=
\int_{\mathcal D_\Lambda}
d\mu_{qk}\,
\left|(RC)^\dagger v\right|^2
\geq0.
\]

The ordered-occurrence factor and identical-pair symmetry factor remain those of Entry 1617; the symmetric domain does not disturb their cancellation.

## Narrow result

\[
\boxed{
\text{At finite source EFT cutoff, the labelled cubic Dyson--Cut contribution integrates to a positive-semidefinite Gaussian covariance correction.}
}
\]

This closes the measure-level qualifier left by Entry 1617.

It does **not** prove:

- positivity of a renormalized, subtracted contribution considered in isolation;
- existence or positivity of a cutoff-free limit;
- that the interacting state is globally Gaussian;
- a complete nonlinear unitarity theorem.

## Architectural consequence

The second-Rees completion found in Entries 1607--1610 is compatible with the existing labelled Cut carrier at finite EFT resolution:

\[
\text{marked first jet}
\xrightarrow{\text{Dyson propagation}}
\text{labelled Cut norm}
\xrightarrow{\int_{\mathcal D_\Lambda}d\mu}
\text{positive covariance grade}.
\]

No new cosmological carrier cell is required for this finite regulated step.  The new information is coefficient/state data carried by the Cut pairing.

## Durable artifacts

- `research/benincasa/checkers/finite_eft_cut_measure.rs`
- `research/benincasa/results/finite-eft-cut-measure.json`

## Next falsifier

Test whether the same labelled Cut norm, with the source finite-time boundary terms retained, obeys the covariance uncertainty inequality after the allowed local counterterm comparison.  Counterterms must be frozen before evaluating the inequality; a subtraction chosen to restore positivity is prohibited.
