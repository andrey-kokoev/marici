# Minimal fixed-energy angular adapter for the photon Bell coefficients

> **Typing correction.** Despite the legacy filename, this is not a fixed-\(t\)
> dispersion adapter. It compares two angles at one fixed nonzero \(s\).

Assume the nonforward absorptive amplitude has already been supplied with its
source-derived phase connection. Put

\[
x=\frac ts,\qquad \frac us=-1-x.
\]

Then the dimension-eight/ten coefficient dependence is

\[
\Phi_2(x)=s^2\bigl[1+x^2+(1+x)^2\bigr]f_2
-s^3x(1+x)f_3,
\]

\[
\Phi_5(x)=-s^3x(1+x)h_3.
\]

Evaluate \(\Phi_2\) at \(x=-1/2\) and \(x=-1/3\). The resulting coefficient
matrix has determinant

\[
-\frac{s^5}{18},
\]

so it is invertible away from the soft locus. A single nonforward value of
\(\Phi_5\) fixes \(h_3\). Thus the information lost by forward dispersion is
recovered by the minimal packet

\[
\boxed{
\Phi_2(-1/2),\quad \Phi_2(-1/3),\quad \Phi_5(-1/2).
}
\]

This is a canonical fixed-energy interpolation map once the angular coordinate
and amplitude normalization are fixed. It does not solve the harder fixed-\(t\)
problem, for which the crossing coordinate is \(\nu=s+t/2\) and \(t\) must
remain constant while \(\nu\) varies.

In Marici language, the forward sum rule is a nonfaithful projection of the
coefficient lens. The two-angle packet is the smallest faithful local frame
for the \((f_2,f_3,h_3)\) part of that lens.

Reproduce with
`research/nima/check_nonforward_dispersive_coefficient_adapter.py`.
