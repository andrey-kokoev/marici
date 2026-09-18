# Forcing reservoir is the Laplace transform of theta autocorrelation

For the right-stable tail

$$
G_z(q)=-\int_q^\infty e^{z(q-r)}\Phi(r)\,dr,
$$

assume the declared decay permits Fubini. Then

$$
\begin{aligned}
\langle\Phi,G_z\rangle
&=-\int dq\,\overline{\Phi(q)}
  \int_q^\infty e^{z(q-r)}\Phi(r)\,dr\\
&=-\int_0^\infty e^{-zt}
  \left(\int \overline{\Phi(q)}\Phi(q+t)\,dq\right)dt.
\end{aligned}
$$

Define the one-sided autocorrelation

$$
A_\Phi(t)
=\int\overline{\Phi(q)}\Phi(q+t)\,dq,
\qquad t\ge0.
$$

Then

$$
\langle\Phi,G_z\rangle
=-\mathcal L A_\Phi(z).
$$

Consequently the two-height forcing reservoir is

$$
\mathcal F(w,z)
=-\mathcal L A_\Phi(z)
-\overline{\mathcal L A_\Phi(w)}
$$

in the Hermitian lane, with the corresponding bilinear expression in the analytic-transpose lane.

Thus the global current-decomposition theorem can be tested against one explicit source function `A_Phi`. Prime/grade, seam, and archimedean currents must jointly reproduce its Laplace transform, not merely its diagonal values.

At finite cutoff the coefficientwise residual becomes

$$
-\mathcal L A_{\Phi,X}(z)
-\overline{\mathcal L A_{\Phi,X}(w)}
-
\sum_r\mathcal F_X^{(r)}(w,z).
$$

This representation removes the stable-history resolvent from the comparison and reduces the remaining source calculation to an autocorrelation/current identity.

Status: forcing reservoir reduced exactly to theta autocorrelation; arithmetic decomposition of that autocorrelation remains open.
