# 1696 — Correlated Cubic Cut Defects Extend Polynomially across Singular Covariance

## Correlated-block falsifier

Entry 1695 proves unequal-block coherence for independent Gaussian blocks.
Admit a joint covariance and test whether the mixed pair defect requires the
Schur/Rees correction found for singular Gaussian conditioning.

## Joint Wick calculation

Write

\[
\Theta=\sum_{i<j}c_{ij}Q_iQ_j,
\]

where the cubic Cut coefficients are

\[
c_{ij}=-2tw_iw_j.
\]

For an arbitrary centered Gaussian joint covariance

\[
A_{ij}=\langle Q_iQ_j\rangle,
\]

one has

\[
\langle\Theta\rangle=\sum_{i<j}c_{ij}A_{ij}
\]

and

\[
\boxed{
\operatorname{Cov}(Q_iQ_j,Q_kQ_l)
=A_{ik}A_{jl}+A_{il}A_{jk}.
}
\]

Thus `Var(Theta)` is polynomial in `A`.  The exact checker evaluates positive
semidefinite covariances of ranks one, two, and three and finds nonnegative
variance throughout.

## Narrow result

\[
\boxed{
\text{the correlated cubic Cut defect is completely evaluated by the joint Gaussian covariance and extends regularly across singular covariance.}
}
\]

No inverse covariance or Schur complement occurs.  Consequently the Rees
coordinate of Entry 1670 is required for **conditioning**, but not for direct
evaluation of this mixed-pair coefficient.  These two operations must remain
typed separately.

No new carrier stratum is indicated.

## Durable artifacts

- `research/benincasa/checkers/correlated_cubic_cut_defect.rs`
- `research/benincasa/results/correlated-cubic-cut-defect.json`
- `research/benincasa/correlated-cubic-cut-defect.md`

## Next falsifier

Condition one correlated block before evaluating the cubic pair defect and
compare with evaluation followed by conditional pushforward.  Compute the
commutator on the singular covariance boundary using the frozen Rees
coordinate.  This is the first point where the direct polynomial observable
and support-sensitive Gaussian conditioning genuinely meet.
