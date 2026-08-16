---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Central Primitives Do Not Determine the Enhanced Stokes Pairing

## Result

The proposed direct pullback of the central-fiber primitives of Entries
296--297 to the enhanced exceptional intervals is not valid. The specialized
walls and the moving source walls meet the exceptional divisor at different
points.

For the physical \((--)\) chart set

\[
E=\tau^2,\qquad
a=-y-\tau^2r,\qquad
b=-x+\tau^2r-\tau^3n.
\]

The central walls used in Entries 296--297 obey

\[
\frac{b+x}{\tau^2}=r-\tau n,
\qquad
\frac{a+y}{\tau^2}=-r,
\]

and therefore meet the exceptional divisor at \(r=0\). The actual moving
source walls obey

\[
\frac{b+x-E}{\tau^2}=r-1-\tau n,
\qquad
\frac{a+y-E}{\tau^2}=-(r+1),
\]

and meet it at \(r=1\) and \(r=-1\), respectively.

Thus specialization at \(E=0\) and restriction to the weighted exceptional
divisor do not commute for these logarithmic primitives.

## Explicit finite witness from \(\eta_{101}\)

Entry 296 writes

\[
\eta_{101}
=
\frac{-B\,da+A\,db}
{4x^2y(x+y)(b+x)R},
\qquad
R=xa^2+yb^2-xy(x+y).
\]

On the \(n=0\) slice of the physical chart, put \(q=\tau^2\). Then

\[
a=-y-qr,\qquad b=-x+qr,
\]

and direct substitution gives the exact identities

\[
R=(x+y)q^2r^2
\]

and

\[
A+B
=
2x(x+y)^2q^2r^2
+(y^2-x^2)q^3r^3
+2(x+y)q^4r^4.
\]

Since

\[
da=-q\,dr,\qquad db=q\,dr,
\]

the tangential numerator is

\[
-B\,da+A\,db=q(A+B)\,dr.
\]

Therefore the leading exceptional restriction of the central primitive is

\[
\boxed{
\eta_{101}^{(0)}
\sim
\frac{1}{2xy}\frac{dr}{r}.
}
\]

Its logarithmic point is \(r=0\). The moving wall \(b+x-E=0\), however,
selects \(r=1\). A form with the required moving boundary behavior must be
obtained from an \(E\)-dependent primitive; replacing \(r\) by \(r-1\) after
the calculation would be a post hoc change of the frozen source object.

The symmetric calculation puts the central \(\eta_{110}\) pole at \(r=0\)
while its moving wall selects \(r=-1\).

## Falsified claim

The hard-to-vary claim

\[
\text{the central primitives can be pulled back directly to the enhanced
moving-wall intervals}
\]

is falsified by the three distinct exceptional points

\[
r=-1,\qquad r=0,\qquad r=1.
\]

Accordingly, Entry 302's stronger statement that only evaluation remained
has been corrected.

## Smaller surviving statement

The relative Stokes pairing remains the canonical comparison mechanism, but
its cochain input must be lifted through the total-energy normal direction:

\[
\boxed{
\text{central relative primitive}
\longrightarrow
\text{moving-wall normal/Rees primitive}
\longrightarrow
\text{exceptional boundary pairing}.
}
\]

This missing object is higher-normal relative coefficient data on the
already frozen marked family. It is not evidence for a new carrier stratum.

## Classification

| Datum | Classification |
|---|---|
| \(r=0\) | specialization of the central walls |
| \(r=\pm1\) | moving source-wall intersections with the exceptional divisor |
| central primitive | established central-fiber coefficient datum |
| moving-wall primitive | missing normal/Rees lift in the relative coefficient system |
| weighted exceptional divisor | existing higher-normal/Cut carrier |
| new carrier datum | none |

## Deutsch--Popperian update M2.46

The failure is narrow: central-fiber exactness does not furnish the
exceptional boundary value of a moving relative cocycle. The next admissible
object is fixed by a lifting problem, not by fitting a boundary answer.

## Next hostile test

Construct \(\eta_{101}(E)\), \(\eta_{110}(E)\), and the compatible two-wall
primitive over the frozen moving denominators

\[
b+x-E,\qquad a+y-E
\]

with:

1. the source normalization unchanged;
2. specialization to Entries 296--297 modulo relative exact gauge;
3. the exact moving-family cocycle equation;
4. no poles outside the frozen marked, Cayley--Menger, soft, and conductor
   divisors.

Then evaluate their exceptional boundary classes at \(r=\pm1\). A forced
pole on any other divisor is the next finite carrier-level falsifier.
