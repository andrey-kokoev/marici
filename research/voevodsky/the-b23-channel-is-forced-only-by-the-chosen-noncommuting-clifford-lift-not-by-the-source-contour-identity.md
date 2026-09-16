# The B23 channel is forced only by the chosen noncommuting Clifford lift, not by the source contour identity

## Correction

The exact matrix calculation

\[
[B_{12},B_{13}]=-2B_{23}
\]

is correct. The conclusion that \(B_{23}\) is therefore the missing physical
Green coupling is not established.

## Source differential is additive

The completed source contour differential is

\[
\Omega_S(z)
=
V_{loc,S}(z)
+
\varepsilon_{end}\frac{2z}{z^2+1/4}.
\]

Its two scalar components commute. The source identity requires their sum and
endpoint residues; it does not require an ordered product of two noncommuting
rotors.

Assigning the local term to \(B_{12}\), the endpoint term to \(B_{13}\), and
then multiplying their exponentials is an additional Clifford lift. Under that
chosen lift, closure indeed introduces \(B_{23}\). A different commuting block
lift would not.

## Exact conjugation shows the added data

For a boost parameter \(u\),

\[
e^{-uB_{13}}B_{12}e^{uB_{13}}
\]

contains hyperbolic \(B_{12}\) and \(B_{23}\) coefficients. Those coefficients
are absent from the original additive contour differential. Therefore they
cannot be identified with the physical mixed Green form without a separate
source comparison theorem.

## Valid conclusion

What is established is only:

\[
\boxed{
\text{the minimal noncommuting Cl(2,1) lift of the two source channels closes
through }B_{23}.}
\]

This makes \(B_{23}\) a canonical **candidate** mixed channel within that lift,
not a source-forced physical map.

## Required identification

To promote it, one must prove on the common source core that the physical mixed
Green pairing equals the \(B_{23}\)-coefficient of the lifted connection. This
is precisely the missing analytic comparison; it cannot be inferred from the
Clifford commutator alone.

The executable Clifford checker remains valid as an algebra audit, but its
claim boundary must remain strictly algebraic.
