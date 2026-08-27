# Archimedean completion retypes terminal forcing into precursor bulk and origin jets

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact archimedean comparison identity

## Decaying precursor

Use the pole-subtracted even precursor (K) satisfying

\[
\Phi=L K,
\qquad
L=\frac14-\partial_q^2.
\]

The precursor decays at infinity, and evenness gives (K'(0)=0). Define

\[
\rho_K(d)=2\int_0^\infty K(q)K(q+d)\,dq,
\]

and similarly (ho_\Phi).

## Source identity

Moving the completion operator through the half-line pairing gives

\[
\rho_\Phi(d)=L_d^2\rho_K(d)-2K(0)\Phi'(d).
\]

This is the exact archimedean comparison between terminal forcing for the
completed kernel and for its decaying precursor.

## Odd transform and endpoint jets

Let

\[
\mathcal K_h(z)=\int_0^\infty\rho_h(d)\sinh(zd)\,dd,
\qquad
C_\Phi(z)=\int_0^\infty\Phi(d)\cosh(zd)\,dd.
\]

Integration by parts gives

\[
\begin{aligned}
\mathcal K_\Phi(z)
={}&\left(\frac14-z^2\right)^2\mathcal K_K(z)\\
&+z\rho_K''(0)
-z\left(\frac12-z^2\right)\rho_K(0)
+2zK(0)C_\Phi(z).
\end{aligned}
\]

The last term is proportional to the completed scalar readout. On a
zero-state it vanishes exactly.

## Endpoint signs

The origin data are fixed source energies:

\[
\rho_K(0)=2\int_0^\infty K(q)^2\,dq>0,
\]

and, using (K'(0)=0),

\[
\rho_K''(0)=-2\int_0^\infty K'(q)^2\,dq<0
\]

for a nonconstant precursor.

## Meaning and remaining obstruction

The archimedean differential is the first source operation that treats
terminal forcing differently from horizontal energy. It converts the terminal
into a precursor odd bulk, two explicit origin jets, and a scalar-readout term
that disappears on the zero locus.

The precursor odd transform remains oscillatory. The next finite test is
whether the two origin jets dominate it on a source-generated hostile zero.
Failure would show that archimedean completion retypes but does not confine.

## Verification

The exact checker verifies both identities on a decaying Neumann precursor
with rational spectral parameter. No numerical approximation is used.
