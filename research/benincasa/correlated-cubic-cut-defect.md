# Correlated Gaussian cubic Cut defect

Write the labelled pair defect as

\[
\Theta=\sum_{i<j}c_{ij}Q_iQ_j
\]

and let `A_ij=<Q_iQ_j>` be any positive-semidefinite joint covariance,
including singular matrices.  Gaussian Wick contraction gives

\[
\langle\Theta\rangle=\sum_{i<j}c_{ij}A_{ij},
\]

\[
\operatorname{Cov}(Q_iQ_j,Q_kQ_l)
=A_{ik}A_{jl}+A_{il}A_{jk}.
\]

Hence the centered defect variance is a polynomial quadratic form in `A` and
the labelled pair coefficients.  No covariance inverse occurs.  It therefore
extends regularly to singular positive-semidefinite covariance strata.

This does not remove the Rees geometry required for Gaussian conditioning;
it shows that direct mixed-pair evaluation does not invoke that operation.
