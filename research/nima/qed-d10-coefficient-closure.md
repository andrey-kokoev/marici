# One-loop QED D10 coefficient closure

At transverse kinematics, the exact all-incoming amplitudes isolate the cubic
low-energy coefficients without a crossing assumption. A high-precision
small-energy extrapolation gives the stripped values

\[
g_3=\frac1{630},\qquad f_3=-\frac1{252},\qquad
h_3=-\frac1{2520}.
\]

Restoring the source normalization \(8\alpha^2\),

\[
\boxed{
g_3=\frac{4\alpha^2}{315},\qquad
f_3=-\frac{2\alpha^2}{63},\qquad
h_3=-\frac{\alpha^2}{315}.
}
\]

The independently normalized nonforward electron-cut moments reproduce
\(f_3\) and \(h_3\) after applying the corrected bra/crossing adapter. The
dispersive extraction of \(g_3\) remains intentionally open because the
\(\Phi_1\) right cut must be completed by its crossed left cut.

This is the coefficient packet needed by the D10 Bell-boundary calculation;
it is not yet a claim that every coefficient has an independent dispersive
derivation.

Reproduce with `research/nima/check_qed_d10_coefficient_closure.py`.
