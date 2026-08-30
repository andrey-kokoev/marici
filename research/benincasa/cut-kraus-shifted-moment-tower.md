# Labelled Cut is completely positive with a forced moment-filtration shift

After tracing the two internal occurrences, the cubic production channel has
labelled Kraus form

\[
\Phi_{\rm Cut}(\rho)
=
\sum_r C_r\rho C_r^\dagger.
\]

Complete positivity follows before summing or integrating labels:

\[
(\Phi_{\rm Cut}\otimes\operatorname{id})(X)
=
\sum_r(C_r\otimes I)X(C_r^\dagger\otimes I)\succeq0
\]

for every \(X\succeq0\).

For the observed cubic production channel, \(C_r\) contains one observed
creation operator.  The adjoint Heisenberg map is

\[
\Phi_{\rm Cut}^\dagger(O)
=
\sum_r C_r^\dagger O C_r.
\]

It raises the polynomial degree of an observed moment by two.  Consequently
the correctly typed truncation map is

\[
\boxed{
\Phi_D:\mathbb M_{\le D+2}\longrightarrow\mathbb M_{\le D},
}
\]

not a same-level endomorphism of \(\mathbb M_{\le D}\).

The checker verifies positivity of finite creation-incidence Kraus maps and
the degree-two shift.  Its integer raising weights differ from canonical Fock
normalization by positive diagonal rescaling, which does not affect the
positivity claim.

Continuum label integration remains completely positive when performed with
the positive symmetric finite-EFT measure of Entry 1618.
