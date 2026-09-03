# The hard-edge connection coefficient is a discrete Wronskian

## Question

How can the polynomial solution’s \(p=-1\) amplitude be defined without choosing a limit-circle extension?

Write the alternating hard-edge recurrence in Jacobi form and let \(F,G\) be exact solutions normalized by

\[
F_n=n^{-1}(1+o(1)),
\qquad
G_n=n^{-2}(1+o(1)).
\]

For any two solutions define

\[
\mathcal W_n(U,V)
=a_{n+1}(U_nV_{n+1}-U_{n+1}V_n).
\]

The recurrence implies

\[
\mathcal W_n(U,V)=\mathcal W_{n-1}(U,V),
\]

so this discrete Wronskian is independent of \(n\). If \(a_n\sim A_0n^4\), then the chosen asymptotic normalization gives

\[
\mathcal W(F,G)=-A_0.
\]

Let \(P\) be the polynomial solution fixed by the finite-index Jacobi initial data. In the asymptotic basis,

\[
P=C_{-1}F+C_{-2}G,
\]

and therefore

\[
C_{-1}
=rac{\mathcal W(P,G)}{\mathcal W(F,G)}.
\]

This is independent of representing measure and of the index at which it is evaluated.

## Disposition

Resolve the type and normalization of the connection coefficient. The required branch statement is now exactly

\[
\mathcal W(P,G)\ne0.
\]

The next leaf is `weibull-minimal-solution-separation`: construct \(G\) from the truncated Weibull recurrence with controlled \(n^{-2}\) asymptotics and prove that the polynomial initial data are not proportional to it.

## Claim boundary

The formula does not prove nonvanishing. Existence of exact solutions with the stated asymptotics still requires a discrete asymptotic theorem with summable coefficient errors.
