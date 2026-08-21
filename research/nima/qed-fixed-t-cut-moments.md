# Crossing-corrected fixed-\(t\) QED cut moments

The physical Breit--Wheeler cut matrix and the all-incoming helicity basis are
not the same presentation. After applying the bra/crossing adapter,

\[
(\operatorname{Im}\Phi_1,\operatorname{Im}\Phi_2,
\operatorname{Im}\Phi_5)
=
(C_{++,++},C_{--,++},-C_{+-,++}).
\]

We integrate the right-hand electron cut with

\[
C_2(t)=\frac{2}{\pi}\int_4^\infty
\frac{\operatorname{Im}\Phi(s,t)}{(s+t/2)^3}\,ds .
\]

For the crossing-even sectors, the near-forward jet obeys

\[
C_2^{\Phi_2}(t)=2f_2-f_3t+O(t^2),\qquad
C_2^{\Phi_5}(t)=-h_3t+O(t^2).
\]

The numerical reconstruction is independently gated by the source low-energy
coefficients

\[
f_2=-\frac{\alpha^2}{15},\qquad
h_3=-\frac{\alpha^2}{315}.
\]

The \(\Phi_1\) right-cut integral is retained as a diagnostic only. Its
fixed-\(t\) crossing completion requires the left cut, so it cannot by itself
be called \(g_2\) or \(g_3\).

Reproduce with
`research/nima/check_qed_fixed_t_cut_moments.py`.
