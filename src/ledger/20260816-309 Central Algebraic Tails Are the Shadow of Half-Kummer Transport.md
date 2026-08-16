---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Central Algebraic Tails Are the Shadow of Half-Kummer Transport

## Result

The three central algebraic tails computed in Entries 291--294 are not
independent ambient extension data. Their incidence coefficients are exactly
the total-energy specialization of the primitive half-Kummer connection
derived in Entry 308.

Consequently the \(v_{\rm alg}\) tail cancels when the primitive top class
is transported horizontally. The surviving central ambient datum is the
filtered \(e_6/[8(x+y)]\) Rees class of Entry 297, not a new
\(\mathcal Q\)-supported line.

## Half-Kummer coefficients at total energy zero

Entry 307 gives

\[
a_1=-\frac12d\log\Delta_1,
\qquad
a_2=-\frac12d\log\Delta_2.
\]

Along the total-energy normal,

\[
a_1(\partial_E)\big|_{E=0}=-\frac1y,
\qquad
a_2(\partial_E)\big|_{E=0}=-\frac1x.
\]

Entry 308 proves

\[
\nabla\widetilde g_{111}
=
\frac12a_1\,g_{101}
+\frac12a_2\,g_{110}.
\]

Therefore its central mixing coefficients are

\[
\boxed{
\frac12a_1(\partial_E)\big|_{E=0}
=-\frac1{2y}=q_{101},
\qquad
\frac12a_2(\partial_E)\big|_{E=0}
=-\frac1{2x}=q_{110}.
}
\]

These are exactly the coefficients reconstructed independently in Entry
294.

## Exact tail cancellation

Write \(s=x+y\) and

\[
v_0
=
x^2y^2\bigl[
(x^2-y^2)e_7+2e_8-2e_9
\bigr].
\]

The frozen central reductions give

\[
T_{101}
=
-\frac{v_0}{4x^3y^3s},
\qquad
T_{110}
=
\frac{v_0}{4x^3y^3s},
\]

\[
T_{111}
=
-\frac{x-y}{8x^4y^4s}v_0.
\]

Direct substitution gives

\[
\boxed{
T_{111}
+\frac12a_1(\partial_E)\big|_{E=0}T_{101}
+\frac12a_2(\partial_E)\big|_{E=0}T_{110}
=0.
}
\]

Thus the incidence identity

\[
T_{111}+q_{101}T_{101}+q_{110}T_{110}=0
\]

is precisely the central specialization of horizontality for
\(\widetilde g_{111}\). It is not an accidental rational relation among
three fitted columns.

## Role of the complement primitives

Entry 296 proves

\[
\Theta_{101}^{\rm fix}=d\eta_{101},
\qquad
\Theta_{110}^{\rm fix}=d\eta_{110}
\]

using meromorphic primitives with only the frozen wall poles. Entry 297
constructs the corresponding two-wall primitive. In the corrected type of
Entry 306, these are complement exact gauges, not forms on a pair boundary.

Their central algebraic tails therefore record how ordinary specialization
of a moving logarithmic class fails to commute with residue transport. Once
the quotient Kummer connection is restored, the primitive \(v_{\rm alg}\)
tail cancels by the displayed identity.

This does not imply that the full ambient localization extension splits.
The filtered survivor

\[
\boxed{
\frac{e_6}{8(x+y)}
}
\]

is not removed by the ordinary complement primitive. It is a genuine
higher-normal/Rees coefficient class in the algebraic kernel.

## Classification

| Datum | Classification |
|---|---|
| \(q_{101},q_{110}\) | half-Kummer quotient-connection coefficients |
| \(T_{101},T_{110},T_{111}\) | central specialization tails on \(v_{\rm alg}\) |
| their incidence cancellation | residue-compatible horizontality |
| \(\eta_{101},\eta_{110},\eta_{111}^{\rm rat}\) | complement exact gauges |
| \(e_6/[8(x+y)]\) | higher-normal/Rees algebraic coefficient datum |
| \(\mathcal Q\) | absent at this central grade |
| new carrier datum | none |

## Deutsch--Popperian update M2.52

The hard-to-vary claim

\[
\text{the three }v_{\rm alg}\text{ tails are independent mixed ambient
extension columns}
\]

is falsified. The smaller surviving theorem is

\[
\boxed{
\text{they are the central shadow of the half-Kummer conductor transport
and cancel in the horizontal primitive top combination.}
}
\]

## Consequence for the ambient frontier

At the central associated grade, the ambient localization problem has been
reduced from three algebraic tails to one filtered survivor on the
\(e_6\) line. The next hostile test is to transport that survivor through
second Rees order and determine its extension with the generic
\(\langle e_6,v_{\rm alg}\rangle\) algebraic plane.

Entry 299 already falsifies the simplest candidate

\[
\frac12d\log(-\mathcal Q)
\]

for its canonical \(e_6\) coordinate. What remains is to decide whether the
survivor defines a nontrivial extension with \(v_{\rm alg}\), or is removed
by a residue-compatible higher-Rees gauge. A forced pole outside the frozen
supports remains the carrier-level falsifier.
