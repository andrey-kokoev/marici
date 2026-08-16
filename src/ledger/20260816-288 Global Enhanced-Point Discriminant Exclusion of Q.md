---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Global Enhanced-Point Discriminant Exclusion of Q

## Result

The four enhanced points of the total-energy central fiber do not generate
the source quartic through their global collision discriminant on the
normalized double conic.

Let

\[
C:\qquad xa^2+yb^2=xy(x+y)
\]

be the affine double locus at \(E=0\).  Put

\[
A=\frac ay,\qquad B=\frac bx,
\]

so that

\[
yA^2+xB^2=x+y.
\]

The normalization through \((A,B)=(1,1)\) is

\[
d=y+xt^2,
\]

\[
A(t)=\frac{xt^2-2xt-y}{d},
\qquad
B(t)=\frac{y-2yt-xt^2}{d}.
\]

The four enhanced points occur at

\[
t=0,\qquad t=1,\qquad t=\infty,\qquad t=-\frac yx.
\]

Restrict the frozen compact branch polynomial \(K_E\) to this normalized
central conic and clear the fixed denominator:

\[
G_{x,y}(t,E)
=
d^4K_E\bigl(yA(t),xB(t)\bigr).
\]

Because \(K_0\) vanishes identically on \(C\), \(E\) divides \(G\).
Define the source-fixed moving divisor polynomial

\[
H_{x,y}(t,E)=\frac{G_{x,y}(t,E)}{E}.
\]

It has degree eight in \(t\).  Its projective collision locus is detected
by

\[
\Delta_C(x,y,E)
=
\operatorname{Res}_t
\left(
H_{x,y},
\partial_tH_{x,y}
\right).
\]

At the generic nonsoft specialization

\[
x=2,\qquad y=3,
\]

exact fraction-free elimination gives

\[
\deg_E\Delta_C(2,3,E)=51.
\]

The source quartic specializes to

\[
\mathcal Q_{2,3}(E)
=
-576-48E^2+40E^3-5E^4.
\]

Exact polynomial reduction gives a nonzero remainder.  A compact finite
certificate is obtained modulo \(101\):

\[
\boxed{
\Delta_C(2,3,E)
\bmod
\bigl(\mathcal Q_{2,3},101\bigr)
=
78+98E+77E^2+19E^3
\neq0.
}
\]

Therefore

\[
\mathcal Q_{2,3}\nmid\Delta_C(2,3,E).
\]

If the symbolic source quartic were a canonical factor of
\(\Delta_C(x,y,E)\), divisibility would survive every specialization at
which the frozen parametrization and source units remain defined.
The point \((x,y)=(2,3)\) avoids

\[
xy(x+y)(x-y)=0
\]

and all four normalized marked parameters are distinct.  Hence this one
exact generic specialization is a finite falsifier:

\[
\boxed{
\mathcal Q
\text{ is not the global collision discriminant of the four enhanced}
\text{ points on the normalized total-energy double conic.}
}
\]

## Frozen construction

No section or carrier component was introduced after seeing
\(\mathcal Q\).  The calculation uses only:

1. the source branch polynomial \(K_E(a,b)\);
2. the central double conic \(C\) derived in entry 286;
3. its canonical rational normalization through a source point;
4. the total-energy normal \(E\);
5. the ordinary resultant of the resulting divisor with its fiber
   derivative.

The resultant is computed before comparison with \(\mathcal Q\).

The ordinary degree-eight resultant also detects projective loss of degree:
a root moving to \(t=\infty\) forces degeneration of the leading
coefficient and is not omitted by the fixed-degree Sylvester determinant.

## Relation to the local audit

Entry 287 excluded \(\mathcal Q\) from the second Rees smoothing at the
physical point \(P_{--}\).  The present calculation is stronger in a
different direction.  It retains the complete degree-eight moving divisor
on the normalized central conic and therefore simultaneously tests:

- the other three sign-enhanced points;
- collisions among all four enhanced loci;
- their global projective gluing on \(C\);
- the point at infinity of the normalization.

Thus the remaining possibility that the four pointwise jets combine into
\(\mathcal Q\) through their global conic discriminant is falsified.

This calculation is an independent surface-family audit.  Entries 209--212
already compute the generic algebraic connection, its extension, and the
physical relative-chain variation.  They exclude \(\mathcal Q\) from all
three.  Therefore the present result must not reopen those closed candidate
homes.

## Provenance partition after the test

Combining the earlier generic coefficient theorem with the present
surface-family calculation excludes \(\mathcal Q\) from:

1. the pure elliptic infinity-Gysin quotient;
2. the cyclic algebraic line \(L_1\);
3. the complete generic rank-seven algebraic kernel \(\mathcal T_7\);
4. the generic algebraic-plane extension class;
5. the generic physical relative-chain monodromy;
6. generic total-energy smoothing along the double conic;
7. the physical enhanced point's second Rees smoothing;
8. the combined projective collision discriminant of all four enhanced
   points.

Thus entry 212's classification is independently strengthened:

\[
\boxed{
\mathcal Q
\text{ is apparent cyclic/master-presentation alphabet data at generic}
\text{ nonsoft homogeneous kinematics.}
}
\]

The absolute surface-smoothing search is closed unless a later calculation
exhibits a source datum absent from the frozen \(K_E\)-family.  Remaining
work concerns intersections of true support divisors, integral
normalization, and the global marked rank-twelve extension—not another
generic home for \(\mathcal Q\).

## Classification

| Datum | Classification |
|---|---|
| normalized conic \(C\) | existing coefficient geometry |
| four enhanced parameters | existing marked incidence |
| \(\Delta_C=0\) | algebraic coefficient support |
| \(\mathcal Q\) in \(\Delta_C\) | absent |
| generic \(\mathcal Q\) provenance | apparent alphabet data |
| new carrier datum | none |

## Deutsch--Popperian update M2.31

The hard-to-vary claim

\[
\mathcal Q
\text{ is generated by global collision of the four enhanced smoothing}
\text{ points}
\]

is falsified by an exact generic specialization.

The smaller surviving statement is:

\[
\boxed{
\mathcal Q
\text{ has no intrinsic generic home in the frozen absolute, marked,}
\text{ algebraic, elliptic, extension, or physical-chain geometry tested.}
}
\]

This strengthens H2 without inventing a new primitive.  Every actual
surface singularity found remains coefficient geometry over the unchanged
energy/Cut carrier, while the printed quartic remains an apparent
presentation letter on the generic homogeneous locus.

## Correction note

The first committed version of this entry incorrectly listed
\(\mathcal T_7/L_1\), the algebraic--elliptic extension, and the physical
relative chain as surviving candidate homes.  Entries 209--212 had already
excluded all three generically.  The exact resultant calculation was
correct; only that historical interpretation and proposed next step were
wrong.  This revision repairs the frontier without changing the
calculation.

## Next hostile test

Use the split total-energy model of entry 286 and the finite collision
monodromy of entries 282--285 to compute the remaining rank-twelve marked
extension

\[
0\to H^2(S_E)
\to H^2(S_E\setminus W)
\to H^1(W)(-1)
\to0
\]

at \(E=0\).  In the rational conductor frame

\[
(g_{101},g_{110},g_{111}^{\rm inv}),
\]

derive the top-column nearby-cycle map and its integral lattice index.
Separate:

- the nodal elliptic rank-one nilpotent;
- the four enhanced-point semistable classes;
- the two conductor Kummer characters;
- the known occurrence \(2\)-torsion gluing.

The finite falsifier is a residual extension class whose support or
integral incidence cannot be generated from the frozen conic, marked walls,
and signed-energy degeneration.  Only that outcome can require a new
carrier datum.
