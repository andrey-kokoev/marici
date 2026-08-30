# Conditional fixed-\(t\) dispersive adapter

At fixed \(t\), use the crossing coordinate

\[
\nu=s+\frac t2,
\qquad s\leftrightarrow u: \nu\mapsto-\nu.
\]

The crossing-even dimension-ten amplitudes become

\[
\Phi_2=rac32f_2t^2+rac14f_3t^3
+\nu^2(2f_2-f_3t),
\]

\[
\Phi_5=rac14h_3t^3-\nu^2h_3t.
\]

For an even fixed-\(t\) dispersion kernel,

\[
\frac{2\nu'}{\nu'^2-\nu^2}
=\frac2{\nu'}+\frac{2\nu^2}{\nu'^3}+O(\nu^4).
\]

Therefore, provided no independent \(\nu^2\) subtraction polynomial is
allowed,

\[
C_2(t)=\frac2\pi\int_{\nu_0(t)}^\infty
\frac{\operatorname{Im}F_+(\nu',t)}{\nu'^3}\,d\nu'.
\]

For \(\Phi_2\), \(C_2(t)=2f_2-f_3t\); for \(\Phi_5\),
\(C_2(t)=-h_3t\). Values at \(t=-m^2,-2m^2\) give an invertible
two-by-two system with determinant \(2m^2\).

This is the correctly typed fixed-\(t\) replacement for the earlier
fixed-energy angular interpolation packet.

## Open gate

The formula is not yet an unconditional QED sum rule. We must establish from
the helicity amplitude's high-energy behavior and Ward/crossing constraints
that the relevant crossing-even combination admits no free \(\nu^2\)
subtraction. If such a subtraction exists, the absorptive data determines the
coefficient only up to that local polynomial.

Reproduce with
`research/nima/check_fixed_t_dispersive_moment_adapter.py`.
