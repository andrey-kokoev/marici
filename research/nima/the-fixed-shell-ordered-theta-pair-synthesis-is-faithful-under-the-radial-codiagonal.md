# The fixed-shell ordered theta-pair synthesis is faithful under the radial codiagonal

## Question

Can off-diagonal ordered theta pairs cancel after the source radial codiagonal on one fixed shell?

## Claim boundary

No on the rapidly convergent ordered-pair source. Positive separation first extracts the least shifted label. If its whole row had zero endpoint asymptotics, analyticity forces the corresponding unshifted-label synthesis to vanish on the shell. Independence of the completed atoms then removes every coefficient in that row. Iteration removes all rows.

## Ordered-pair packet

Fix a nontrivial shell \([a,b]\) and write

\[
F(t)=
\sum_{n,m\ge1}c_{nm}\rho_{nm}^{[a,b]}(t),
\qquad
\rho_{nm}^{[a,b]}(t)
=
\int_a^b\Phi_n(u)\Phi_m(u+t)\,du.
\]

Assume the coefficient matrix has enough Gaussian or projective decay for absolute locally uniform summation and termwise endpoint asymptotics. The source theta coefficients satisfy this condition because each atom already carries Gaussian label decay on a fixed compact shell.

Regroup by the shifted label:

\[
F(t)=
\sum_{m\ge1}
\int_a^b f_m(u)\Phi_m(u+t)\,du,
\qquad
f_m(u)=\sum_{n\ge1}c_{nm}\Phi_n(u).
\]

Every \(f_m\) is analytic on a neighborhood of the shell.

## Least shifted-label extraction

Suppose \(F=0\) and let \(m_0\) be the least shifted label with a nonzero coefficient row. If \(f_{m_0}\) is not identically zero, it has a finite vanishing order \(r\) at \(a\). Watson endpoint localization and the explicit completed atom give

\[
\int_a^b f_{m_0}(u)\Phi_{m_0}(u+t)\,du
=
B_{m_0,r}(t)
\exp\left[-\pi m_0^2e^{2a}e^{2t}\right]
\left(1+o(1)\right),
\]

with a nonzero finite-power prefactor.

Every row \(m>m_0\) carries instead

\[
\exp\left[-\pi m^2e^{2a}e^{2t}\right].
\]

After division by the \(m_0\) scale, the higher rows vanish. The exact polynomial factors admit a Gaussian-in-\(m\) summable majorant, so the limit passes through the infinite row sum. This contradicts \(F=0\).

Therefore \(f_{m_0}\) must vanish to every order at \(a\). Analyticity then gives

\[
f_{m_0}(u)=0
\]

throughout the shell.

## Independence inside one row

The completed atoms are linearly independent on every open interval. Indeed, analytic continuation extends any relation

\[
\sum_n d_n\Phi_n(u)=0
\]

to the positive tail. There the least active label \(n_0\) has the slowest factor

\[
\exp\left[-\pi n_0^2e^{2u}\right],
\]

while every \(n>n_0\) is smaller by

\[
\exp\left[-\pi(n^2-n_0^2)e^{2u}\right].
\]

Gaussian domination permits passage through an infinite convergent synthesis. Hence all \(d_n\) vanish. Applied to \(f_{m_0}=0\), this proves

\[
c_{nm_0}=0
\]

for every \(n\), contradicting the choice of the row.

Repeating the argument over shifted labels proves \(c_{nm}=0\) for all ordered pairs.

## Result

On a fixed shell,

\[
\ker(DJ_{\rm or})
\cap
\mathcal A_{\rm ordered\ pair}^{[a,b]}
=\{0\}.
\]

Positive separation alone is sufficient; the opposite orientation supplies a consistency check but is not needed for injectivity.

## Strength boundary

The proof is source-level and assumes the declared rapidly convergent ordered-pair synthesis. It does not identify:

- a G4 metric radical;
- a quotient imposed after source codiagonalization;
- cross-shell coefficients when several shell intervals are codiagonalized into one unlabelled history without retaining endpoint order.

The last item can be attacked by ordering first by shell lower endpoint, then by shifted label, then by unshifted-atom independence.

## G4 consequence

Neither diagonal nor off-diagonal theta-label mixing creates a fixed-shell source radical. A G4 quotient that kills such a packet must expose an additional relation after the radial source map; it cannot attribute the null direction to the endpoint–Wronskian codiagonal itself.

## Disposition

The fixed-shell source kernel audit is complete for the full ordered theta-pair family. The next depth-first extension is the joint cross-shell ordered-pair packet, using lexicographic endpoint and label scales. No RH conclusion is authorized.
