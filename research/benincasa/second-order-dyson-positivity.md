# Second-order Dyson positivity is filtered, not global

Take

\[
H=\sigma_x,
\qquad
\rho=|0\rangle\langle0|.
\]

The real-plus-virtual second-order Dyson map is

\[
\Phi^{[2]}_g(\rho)
=
\rho-ig[H,\rho]
+g^2\left(H\rho H-\frac12\{H^2,\rho\}\right).
\]

Explicitly,

\[
\Phi^{[2]}_g(\rho)
=
\begin{pmatrix}
1-g^2&ig\\
-ig&g^2
\end{pmatrix}.
\]

It has exact trace one, but

\[
\det\Phi^{[2]}_g(\rho)=-g^4.
\]

Therefore the polynomial truncation is not positive for any finite (g\ne0).  The failure begins two orders beyond the retained grade.  The real Cut term and virtual anticommutator do provide the correct conditional positivity through order (g^2); they do not license treating the truncated polynomial as an exact CP map.

The correct statement is consequently filtered/Rees: the second-order packet is the grade of an exact positive superchannel, or it must be supplied with a positivity-preserving completion.  This distinction applies equally on the correlated intervention cone of Entry 1641.
