# General Gaussian internal-state pushforward remains a strict observed map

Write the cubic jump as a tensor product between the observed leg and the two
internal occurrences,

\[
L_{p;qk}=C_{p;qk}\,a_p^\dagger\otimes
(a_q^\dagger a_k^\dagger).
\]

For an initially split observed/internal state, tracing a fixed internal
Gaussian density matrix produces the scalar

\[
\mu_{qk}
=\operatorname{Tr}
\left[
\rho_{qk}(a_q a_k)(a_q^\dagger a_k^\dagger)
\right]
=\langle(N_q+1)(N_k+1)\rangle.
\]

Gaussian Wick reduction gives

\[
\boxed{
\mu_{qk}
=(n_q+1)(n_k+1)
+|c_{qk}|^2
+|\beta_{qk}|^2,
}

where \(c_{qk}=\langle a_q^\dagger a_k\rangle\) and
\(\beta_{qk}=\langle a_q a_k\rangle\).

The scalar is positive and symmetric under \(q\leftrightarrow k\).  The
observed trace-balanced generator is therefore

\[
\mu_{qk}(N_p+1)[f(N_p+1)-f(N_p)],
\]

which preserves observed moment degree.

The result assumes the initial observed mode is split from the internal pair.
If the source Gaussian covariance directly correlates \(p\) with \(q\) or
\(k\), the reduced dynamics need not be a state-independent completely
positive map.  Translational invariance confines such correlations to labelled
coincidence/opposite-momentum supports, which require a separate supported
test rather than a generic correction.
