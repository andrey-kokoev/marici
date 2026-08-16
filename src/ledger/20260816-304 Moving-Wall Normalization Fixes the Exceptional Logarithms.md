---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Moving-Wall Normalization Fixes the Exceptional Logarithms

## Result

Although Entry 303 proves that the central-fiber primitives cannot be
transplanted to the moving exceptional interval, the frozen source wall
normalizations already determine the two endpoint logarithms canonically.

For the two mixed walls, Entry 263 gives

\[
K_E(t,E-x)=R_1(t)^2,
\qquad
K_E(E-y,t)=R_2(t)^2.
\]

On the physical \((--)\) enhanced chart their normalized wall residues have
the limits

\[
\boxed{
\rho_{101}
=\frac{da}{R_1(a)}
\longrightarrow
-\frac{1}{2xy}\frac{dr}{r-1},
}
\]

\[
\boxed{
\rho_{110}
=\frac{db}{R_2(b)}
\longrightarrow
-\frac{1}{2xy}\frac{dr}{r+1}.
}
\]

Thus the logarithmic coefficients and their occurrence-resolved locations
\(r=1\) and \(r=-1\) are source-derived. No choice of a bulk
Griffiths--Dwork primitive is involved.

## Exact first wall calculation

Write \(s=x+y\), \(z=E-s\). The source square root on

\[
W_1:\quad b=y+z=E-x
\]

is

\[
\begin{aligned}
R_1(t)
={}&xt^2-z^3-yz^2+y^2z+y^3\\
&-2xz^2-2xyz-xy^2-x^2z-x^2y.
\end{aligned}
\]

Substitution of \(z=E-s\) gives the exact normal form

\[
\boxed{
R_1(t)
=
xt^2-xy^2-2xyE+(x+2y)E^2-E^3.
}
\]

On the \(n=0\) slice of the physical weighted chart,

\[
a=-y-Er,\qquad da=-E\,dr.
\]

Therefore

\[
\boxed{
R_1(-y-Er)
=
E\left[
2xy(r-1)
+E(xr^2+x+2y-E)
\right].
}
\]

Consequently

\[
\frac{da}{R_1(a)}
=
-\frac{dr}
{2xy(r-1)+E(xr^2+x+2y-E)}
\]

and the stated \(E\to0\) logarithm follows.

## Exact second wall calculation

The source square root on

\[
W_2:\quad a=x+z=E-y
\]

reduces exactly to

\[
\boxed{
R_2(t)
=
yt^2-x^2y-2xyE+(2x+y)E^2-E^3.
}
\]

On the same chart,

\[
b=-x+Er,\qquad db=E\,dr,
\]

so

\[
\boxed{
R_2(-x+Er)
=
E\left[
-2xy(r+1)
+E(yr^2+2x+y-E)
\right].
}
\]

Hence

\[
\frac{db}{R_2(b)}
=
\frac{dr}
-2xy(r+1)+E(yr^2+2x+y-E)}
\longrightarrow
-\frac{1}{2xy}\frac{dr}{r+1}.
\]

## Integral occurrence vector

Stripping the common source normalization \(-1/(2xy)\), the two wall
residues are the logarithmic occurrence covectors at

\[
p_+=\{r=1\},
\qquad
p_-=\{r=-1\}.
\]

The physical Leray interval is oriented \(p_-\to p_+\). Its boundary is

\[
\partial[p_-,p_+]=[p_+]-[p_-],
\]

so the endpoint pairing is governed by the already established integral
occurrence vector

\[
\boxed{(-1,1)}
\]

in the ordered basis \((p_-,p_+)\), with the common rational normalization
kept in the coefficient object.

This identifies the parity/occurrence part of the eventual Stokes boundary
pairing before any bulk lift is selected.

## What this does and does not solve

The endpoint logarithms are now fixed. The remaining lifting problem is to
construct a bulk one-form \(\eta_i(E)\) satisfying the moving-family relative
cocycle equation and restricting to these wall-normalized boundary classes.
Different bulk representatives may differ by relative exact gauge, but they
cannot move the poles away from \(p_\pm\) or change their source
normalization.

In particular, the central logarithm at \(r=0\) from Entry 303 is not a third
physical occurrence. It is the specialization artifact of collapsing the
moving wall before performing the weighted blowup.

## Classification

| Datum | Classification |
|---|---|
| \(R_1,R_2\) | frozen square-root normalization on existing source walls |
| \(dr/(r-1),dr/(r+1)\) | occurrence-resolved boundary coefficient data |
| \((-1,1)\) | existing integral Cut/Leray incidence |
| \(r=0\) pole of the central primitive | noncommuting-specialization artifact |
| compatible bulk primitive | still-uncomputed relative coefficient lift |
| new carrier datum | none |

## Deutsch--Popperian update M2.47

Entry 303 falsified direct central pullback. The smaller surviving claim is
now stronger than mere existence:

\[
\boxed{
\text{the frozen moving-wall normalization uniquely fixes the exceptional
logarithmic boundary classes, while only their bulk relative lift remains
to be computed.}
}
\]

## Next hostile test

Solve the relative Griffiths--Dwork lifting equation with these two boundary
conditions. After quotienting exact gauge, its exceptional restriction must
have no poles except \(r=\pm1\), soft support, and the predeclared
Cayley--Menger/conductor strata. Any unavoidable additional pole is the next
finite carrier-level falsifier.
