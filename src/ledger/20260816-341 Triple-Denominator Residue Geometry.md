---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Triple-Denominator Gysin Class Has Only Existing Energy Support

## Question

Ledger entry 340 found one proper full-support grade for the frozen
three-denominator family

\[
(q_{\mathfrak g_1},q_{\mathfrak g_2},q_{\mathcal G_{12}})
\]

but did not construct its representative or any canonical map.

The next hard-to-vary conjecture was

\[
\boxed{
\text{the unique proper \(111\) class requires incidence data beyond the
frozen denominator and Cayley--Menger arrangement.}
}
\]

This conjecture is falsified.

## Frozen source geometry

Keep the source normalization

\[
q_{\mathfrak g_1}=x+c+b,\qquad
q_{\mathfrak g_2}=y+c+a,\qquad
q_{\mathcal G_{12}}=E+c,
\]

where \(E=x+y+z\) and \((c,a,b)=(y_{12},y_{23},y_{31})\).

No divisor, cell, or support summand is added. The three hyperplanes have
the unique common point

\[
\boxed{
P:\quad c=-E,\qquad a=x+z,\qquad b=y+z.
}
\]

Moreover,

\[
\det
\frac{\partial(q_{\mathfrak g_1},q_{\mathfrak g_2},
q_{\mathcal G_{12}})}
{\partial(c,a,b)}
=-1.
\]

Thus the intersection is transverse over the entire parameter space.

## Exact Cayley--Menger restriction

Direct substitution into the frozen Cayley--Menger polynomial gives

\[
\boxed{
K(P)=
\left[(x+y+z)(-x+y+z)(x-y+z)\right]^2.
}
\]

This polynomial identity was checked by exact symbolic expansion in the Rust
certificate, not fitted from samples. It evaluates to \(18225\) at
\((x,y,z)=(2,3,4)\), and to \(200704\) at \((x,y,z)=(3,5,6)\).

The lower-pair line \(q_{\mathfrak g_1}=q_{\mathfrak g_2}=0\) has
parametrization

\[
c=t,\qquad a=-y-t,\qquad b=-x-t.
\]

On this line,

\[
\boxed{
K|_{12}=t^2(-x+y+z)^2(x-y+z)^2.
}
\]

The third denominator marks \(t=-E\). Consequently the triple collision
with the branch divisor occurs precisely on

\[
E(-x+y+z)(x-y+z)=0.
\]

Every factor is already a site-energy or signed-energy letter.

## Canonical logarithmic and Gysin class

Choose the ordered logarithmic generator

\[
\eta_{111}
=
d\log q_{\mathfrak g_1}\wedge
d\log q_{\mathfrak g_2}\wedge
d\log q_{\mathcal G_{12}}.
\]

Its three codimension-one residues are

\[
\operatorname{Res}_{q_{\mathfrak g_1}=0}\eta_{111}
=
d\log q_{\mathfrak g_2}\wedge d\log q_{\mathcal G_{12}},
\]

\[
\operatorname{Res}_{q_{\mathfrak g_2}=0}\eta_{111}
=
-d\log q_{\mathfrak g_1}\wedge d\log q_{\mathcal G_{12}},
\]

\[
\operatorname{Res}_{q_{\mathcal G_{12}}=0}\eta_{111}
=
d\log q_{\mathfrak g_1}\wedge d\log q_{\mathfrak g_2}.
\]

Hence the oriented face vector is

\[
\boxed{(1,-1,1).}
\]

The iterated residue at \(P\) is a unit. The proper rank-one \(111\) grade
from entry 340 therefore has a canonical geometric representative: it is
the triple-denominator logarithmic class, equivalently the Gysin/Thom class
of the transverse marked point \(P\).

This identification comes from the divisor geometry. It does not come from
choosing a complement to the rank cube.

## Coefficient line

For the source square-root measure \(\mathcal K=K^{-1/2}\), restriction to
the triple stratum gives

\[
\boxed{
\mathcal K|_P
=
\frac{\pm1}{E(-x+y+z)(x-y+z)}.
}
\]

The sign is occurrence/sheet data. On a resolved sheet this is a rank-one
Tate/Kummer coefficient line; no new algebraic cover is generated.

Its generic singular support is contained in

\[
\boxed{
E=0,\qquad -x+y+z=0,\qquad x-y+z=0.
}
\]

These are existing energy-arrangement divisors.

## Correction to the map frontier

The rank cube by itself does not define maps

\[
\operatorname{gr}_{111}\mathcal M
\longrightarrow
\bigoplus_{|S|=2}\operatorname{gr}_{S}\mathcal M.
\]

The canonical object is instead the logarithmic Cousin/Gysin complex of the
frozen divisor arrangement. Its differential is the alternating Poincare
residue above, and its square vanishes by residue anticommutativity.

In particular, the fact that the proper \(011\) Mobius grade has rank zero
does not erase the geometric \(011\) intersection line. The \(111\) class is
the new marked-point class on that line when \(q_{\mathcal G_{12}}\) is
inserted. Confusing the Mobius grade with the stratum itself would lose the
canonical map.

## Classification

\[
\boxed{
\begin{array}{c|c}
\text{datum} & \text{home}\\
\hline
P & \text{existing denominator incidence}\\
K(P)=0 & \text{existing signed-energy support}\\
\eta_{111} & \text{relative/Gysin coefficient class}\\
\mathcal K|_P & \text{rank-one Tate/Kummer coefficient line}\\
\text{new carrier datum} & \text{none}
\end{array}
}
\]

Thus the unique top-support class strengthens H2:

\[
\boxed{
\text{shared carrier and Gysin calculus}
+
\text{sector-specific filtered coefficient object}.
}
\]

## Limits

This result does not prove:

- a canonical splitting of the 21-dimensional top system;
- the mixed-face connecting maps beyond their local residue incidence;
- the descent to the rank-nine \(q_{\mathcal G_{12}}\)-only module;
- compatibility with the physical relative integration chain;
- extension across simultaneous soft or signed-energy collisions.

The prime-field exponents used for the rank count remain generic regulators.
The geometric identification here instead uses the source divisor
normalization and the source \(K^{-1/2}\) measure.

## Exact evidence

- research/benincasa/marici-gm/src/bin/elliptic_top_support_geometry.rs;
- research/benincasa/elliptic-top-support-geometry.json;
- ledger entry 340 for the exact support ranks.

## Next hostile falsifier

Freeze the Cousin orientation and compute the two proper mixed-face lines

\[
\operatorname{gr}_{101}\mathcal M,\qquad
\operatorname{gr}_{110}\mathcal M
\]

as explicit puncture/Gysin coefficient systems.

Then test whether their connecting morphisms into the
\(q_{\mathcal G_{12}}\)-only rank-nine module are generated entirely by the
same denominator intersections and Cayley--Menger restriction.

The next finite falsifier is:

\[
\boxed{
\text{a mixed-face extension requires singular support or an incidence map
not generated by the frozen arrangement.}
}
\]

If it survives, H2 fails at the first such datum. If it is falsified, the
entire top-to-\(q\)-only extension remains inside sector-specific
coefficients over the shared carrier.

## Outcome contract

~~~json
{
  "claim": "The unique proper 111 class requires incidence data beyond the frozen denominator and Cayley-Menger arrangement.",
  "status": "falsified",
  "proper_top_rank": 1,
  "canonical_representative": "dlog(q_g1) wedge dlog(q_g2) wedge dlog(q_G12)",
  "incidence_jacobian": -1,
  "face_residue_signs": [1, -1, 1],
  "K_at_triple": "[(x+y+z)(-x+y+z)(x-y+z)]^2",
  "coefficient_type": "rank-one Tate/Kummer on the resolved occurrence sheet",
  "new_carrier_datum": false,
  "canonical_global_splitting_proved": false,
  "next_problem": "Construct both mixed-face coefficient lines and their connecting maps to the q-only rank-nine module."
}
~~~
