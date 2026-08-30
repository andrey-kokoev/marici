# Cardinality-weighted merge transports the independent Gaussian Wick defect

Entry 1650 gives the scalar-cubic Gaussian Cut defect

\[
[C,D](p_1q_3)=-\nu q_2,
\]

where \(\nu\) is the variance of the internal occurrence. For an internal
block of \(N\) independent labelled occurrences, the normalized collective
coordinate has variance

\[
\nu_N=\frac1N\sum_{i=1}^N\nu_i.
\]

Under the cardinality-weighted merger of blocks \(m,n\),

\[
\nu_{m+n}
=\frac{m\nu_m+n\nu_n}{m+n}.
\]

This operation is associative and returns the same arithmetic mean under every
binary bracketing. Consequently the pushed-forward defect

\[
-\nu_Nq_2
\]

is natural under unequal independent block mergers.

The exact checker tests 36 rational variance patterns and all 247,500 ordered
binary bracketings through twelve internal occurrences.

This result does not cover correlated blocks. Cross-covariance contributes an
additional quadratic term and must be retained by conditional Gaussian
pushforward, as in Entry 1652.

