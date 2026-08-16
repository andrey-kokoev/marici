---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Moving-Wall Residues Carry Canonical Kummer Connections

## Result

The two one-wall terms in the normalized logarithmic residue complex have
canonical rank-one Kummer Gauss--Manin connections. No bulk primitive is
needed to derive them.

In the physical enhanced chart, Entry 304 gives

\[
\rho_1=-\frac{dr}{D_1(E,r)},
\qquad
D_1=Exr^2+2xyr-2xy+E(x+2y-E),
\]

\[
\rho_2=\frac{dr}{D_2(E,r)},
\qquad
D_2=Eyr^2-2xyr-2xy+E(2x+y-E).
\]

Their quadratic discriminants are

\[
\boxed{
\Delta_1
=
4x\bigl[
xy^2+2Exy-E^2(x+2y-E)
\bigr],
}
\]

\[
\boxed{
\Delta_2
=
4y\bigl[
x^2y+2Exy-E^2(2x+y-E)
\bigr].
}
\]

On the locus where \(E\,x\,y\,\Delta_1\Delta_2\neq0\), put
\(\alpha_i^2=\Delta_i\). For any quadratic
\(D=ar^2+br+c\), with \(\alpha^2=b^2-4ac\),

\[
\frac{dr}{D}
=
\frac1\alpha
d\log\frac{2ar+b-\alpha}{2ar+b+\alpha}.
\]

Therefore the periods of \(\rho_i\) around the two moving punctures are a
constant integral logarithmic period multiplied by \(\Delta_i^{-1/2}\).
In the source residue basis,

\[
\boxed{
\nabla[\rho_i]
=
-\frac12\,d\log\Delta_i\,[\rho_i].
}
\]

This is a direct computation of the one-wall Gauss--Manin connection, not an
inference from monodromy.

## Residue compatibility

Let \(\Omega_i\) be the corresponding logarithmic surface class. Since
residue commutes with the absolute de Rham differential and with
differentiation in the smooth base,

\[
\boxed{
\operatorname{Res}_{W_i}(\nabla\Omega_i)
=
\nabla_{W_i}(\operatorname{Res}_{W_i}\Omega_i)
=
-\frac12d\log\Delta_i\,\rho_i
\quad\text{in }H^1(W_i).
}
\]

Any remaining term is exact on the normalized wall. This proves the
residue-compatibility gate separately on both one-wall summands.

## Total-energy normal expansion

At \(E=0\),

\[
\Delta_1=4x^2y^2,
\qquad
\Delta_2=4x^2y^2.
\]

The two connection forms along the total-energy normal are

\[
-\frac12\partial_E\log\Delta_1
=
-\frac1y
+\frac{3x+2y}{xy^2}E
+O(E^2),
\]

\[
-\frac12\partial_E\log\Delta_2
=
-\frac1x
+\frac{2x+3y}{x^2y}E
+O(E^2).
\]

Thus the one-wall Kummer sector already has a nonzero first normal
connection. This does not conflict with the fact that the algebraic
quartic \(\mathcal Q\) begins at second normal order: \(\mathcal Q\) belongs
to the unresolved algebraic/top-extension sector, not to either pure
one-wall line.

## Singular support

The only finite singular support introduced by these connection forms is

\[
x\,y\,\Delta_1\,\Delta_2=0.
\]

Here \(x=0\) and \(y=0\) are soft support, while
\(\Delta_i=0\) is collision of the two punctures on the already frozen
normalized source wall. It is conductor/coefficient support, not a new
surface incidence generator.

The total-energy divisor \(E=0\) is regular for these two Kummer lines at
generic \(xy\neq0\); it appears in the chosen quadratic coefficient but not
in \(\Delta_i^{-1}d\Delta_i\).

## Orientation-twisted frame

Tensoring by the source orientation line
\(\mathfrak o_{ab}=\chi_{\epsilon\delta}\) changes the occurrence character
as in Entry 305 but does not alter the scalar Kummer connection. Hence the
two diagonal entries in the enhanced frame are now fixed:

\[
\mathcal K_{\Delta_1^{-1/2}}
\oplus
\mathcal K_{\Delta_2^{-1/2}}.
\]

Entry 308 computes the remaining part of the rank-three conductor quotient:
the connection/extension involving the primitive top class
\(\widetilde g_{111}\).

## Classification

| Datum | Classification |
|---|---|
| \(\Delta_i=0\) | conductor collision/coefficient support |
| \(-\tfrac12d\log\Delta_i\) | Tate/Kummer coefficient connection |
| \(x=0\), \(y=0\) | soft support |
| orientation twist | existing occurrence coefficient line |
| top-class extension | forced half-Kummer extension, computed in Entry 308 |
| new carrier datum | none |

## Deutsch--Popperian update M2.50

The hard-to-vary claim

\[
\text{the one-wall residue transport requires a separately chosen bulk
relative primitive}
\]

is falsified. The smaller surviving theorem is

\[
\boxed{
\text{each moving-wall residue line is canonically }
\mathcal K_{\Delta_i^{-1/2}},
\text{ and residue commutes with its Gauss--Manin transport.}
}
\]

## Next hostile test

Entry 308 performs this test and finds that \(J\) diagonalizes the complete
rank-three quotient connection without introducing any support. The next
hostile test is therefore the ambient localization extension

\[
0\to H^2(S_E)\to H^2(S_E\setminus W_E)
\to H^1(W_E)(-1)\to0,
\]

not another internal conductor calculation.
