# Global quartic root monodromy has two repeated collision types

## Question

What based-path and Hurwitz information can be computed directly from the four-point quartic family before embedding its vanishing cycles into the del Pezzo Picard lattice?

## Root cover

Write

\[
u=t^2,
\qquad
u_\pm=\frac{h\pm\sqrt D}{2x^2},
\]

where

\[
h=x^2+y^2-(E-x-y)^2
\]

and

\[
D=-E(2x-E)(2y-E)(2x+2y-E).
\]

The four labelled roots are

\[
t_{\epsilon,\sigma}
=\epsilon\sqrt{\nu_\sigma},
\qquad
\epsilon,\sigma\in\{+,-\}.
\]

Because

\[
\nu_+\nu_-=\frac{y^2}{x^2},
\]

neither \(u\)-root crosses zero away from the soft loci. A small loop around any one of the four simple critical values changes the sign of \(\sqrt D\), hence exchanges \(\nu_+\) and \(\nu_-\). On the four roots its permutation is

\[
(t_{+,+}\ t_{+,-})(t_{-,+}\ t_{-,-}).
\]

Thus each base puncture has the same double-transposition permutation shadow. The product of the four puncture permutations is the identity, as required for the loop at infinity in this finite root cover.

## Two repeated collision fibers

Exact specialization gives

\[
F(t;x,y,0)=F(t;x,y,2x+2y)=(xt^2+y)^2,
\]

while

\[
F(t;x,y,2x)=F(t;x,y,2y)=(xt^2-y)^2.
\]

Hence the four critical values divide into two repeated collision types:

- \(0\) and \(2(x+y)\) collide at \(t^2=-y/x\);
- \(2x\) and \(2y\) collide at \(t^2=+y/x\).

This is stronger than the unordered critical-value list: remote punctures reproduce the same two nodal fiber equations.

## Based paths and Hurwitz moves

For positive unequal \(x,y\), the real critical order is either

\[
0<2x<2y<2(x+y)
\]

or its middle transposition. Crossing \(x=y\) exchanges the two middle punctures and applies one Hurwitz move to any distinguished path system. At the level of root permutations the two factors are identical, so this move is invisible.

Likewise, choosing above versus below detours from a physical basepoint changes the braid lift while preserving the same double-transposition permutation. Therefore root permutations alone do not determine the integral Picard--Lefschetz matrices.

## Missing lift

A full Hurwitz computation requires collision arcs in the compactified fiber and their oriented intersection numbers. Those data lift the common permutation shadow to Dehn twists or Picard--Lefschetz transvections. The quartic equation supplies collision locations but no source-normalized embedding of those arcs into the rank-nine Picard lattice.

## Disposition

The global root-cover monodromy and chamber transition are computed: four identical double-transposition shadows, grouped into two repeated collision fibers, with a middle Hurwitz exchange at \(x=y\). The unresolved part is precisely the braid-to-integral-Picard lift; permutation monodromy cannot determine the two ambient parity intersections.
