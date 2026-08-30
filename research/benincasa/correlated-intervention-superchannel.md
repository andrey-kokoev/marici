# Correlated intervention superchannel

Let (ho_{PE}\succeq0) be the frozen correlated state of an observed occurrence (P) and its supported partner (E).  For a local CP intervention

\[
\mathcal A(X)=\sum_r K_rXK_r^\dagger
\]

and subsequent global unitary (U), define

\[
\mathfrak T_{\rho,U}(\mathcal A)
=
\operatorname{Tr}_E\!left[
U(\mathcal A\otimes\operatorname{id})(\rho_{PE})U^\dagger
\right].
\]

This is linear and completely positive as a map of intervention Choi operators.  In a factorization (ho_{PE}=RR^\dagger), its output is a partial trace of

\[
\sum_r UK_rR(UK_rR)^\dagger,
\]

and is therefore positive.  No assignment of the frozen correlation to arbitrary observed states is used.

If (ho_{PE}=\rho_P\otimes\rho_E), then

\[
\mathfrak T_{\rho,U}(\mathcal A)
=
\operatorname{Tr}_E\!left[
U(\mathcal A(\rho_P)\otimes\rho_E)U^\dagger
\right],

the ordinary reduced channel after the intervention.  Thus the process object has the exact product degeneration demanded by Entry 1639.

For cosmology, the labelled cubic Cut evolution supplies the global positive/unitary step, while opposite-momentum support supplies (ho_{PE}).  This construction establishes the type and positivity mechanism.  It does not yet derive a finite Gaussian Choi covariance for the non-Gaussian cubic interaction or prove renormalized continuum existence.
