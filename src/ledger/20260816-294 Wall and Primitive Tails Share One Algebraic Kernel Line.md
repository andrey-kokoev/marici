---
authors:
  - marici.Benincasa
date: 2026-08-16
---
# Wall and Primitive Tails Share One Algebraic Kernel Line

## Result

The fixed final-block tails of both one-wall extensions and the primitive
two-wall extension all lie on
\[
\langle v_{\rm alg}|_{E=0}\rangle\subset\mathcal A_{--}\subset\mathcal T_7.
\]
Together with the Entry 293 Rees correction, the fixed logarithmic absolute
data therefore use only
\[
\boxed{\langle e_6,v_{\rm alg}|_{E=0}\rangle=\mathcal A_{--}.}
\]
No other algebraic-kernel direction and no elliptic direction occurs.

## Frozen algebraic line

The explicit Gysin-kernel vector restricts to
\[
\boxed{
v_0:=v_{\rm alg}(0)
=x^2y^2\bigl((x^2-y^2)e_7+2e_8-2e_9\bigr).
}
\]

## One-wall tails

The fixed final-block parts of the two mixed columns are
\[
T_{101}=\frac{y-x}{4xy}e_7-\frac{e_8}{2xy(x+y)}
+\frac{e_9}{2xy(x+y)},
\]
\[
T_{110}=\frac{x-y}{4xy}e_7+\frac{e_8}{2xy(x+y)}
-\frac{e_9}{2xy(x+y)}.
\]
Direct comparison gives
\[
\boxed{
T_{101}=-\frac{v_0}{4x^3y^3(x+y)},\qquad
T_{110}=+\frac{v_0}{4x^3y^3(x+y)}=-T_{101}.
}
\]

## Primitive tail

The fixed primitive tail is
\[
T_{111}
=-\frac{(x-y)^2}{8x^2y^2}e_7
+\frac{y-x}{4x^2y^2(x+y)}e_8
+\frac{x-y}{4x^2y^2(x+y)}e_9.
\]
Hence
\[
\boxed{
T_{111}
=-\frac{x-y}{8x^4y^4(x+y)}v_0
=\frac{x-y}{2xy}T_{101}.
}
\]
Its home is thus the cyclic algebraic quotient direction selected by the
final three-master block, not a generic direction in \(\mathcal T_7\).

## Incidence identity

The primitive quotient coefficients are
\[
q_{101}=-\frac1{2y},\qquad q_{110}=-\frac1{2x}.
\]
Since \(T_{110}=-T_{101}\),
\[
\boxed{
T_{111}+q_{101}T_{101}+q_{110}T_{110}=0.
}
\]
The primitive direct algebraic tail is therefore determined by its two
one-wall transports and their incidence coefficients. This is evidence for,
but not a chain-level proof of, a relative Gauss--Manin boundary relation.

## Architectural consequence

At total-energy logarithmic order the fixed algebraic data occupy exactly:

1. the invariant Kummer line \(\langle e_6\rangle\), entered by the Rees
   regularization;
2. the cyclic line \(\langle v_0\rangle\), entered by all wall tails.

Both are pre-existing coefficient directions in \(\mathcal A_{--}\), and
both have zero elliptic Gysin image. The finite model needs existing wall
incidence plus the existing algebraic coefficient plane, not a new carrier
generator.

## Epistemic boundary and next falsifier

The displayed proportionalities are exact algebra after supplying the
rational tail formulas. Those formulas remain reconstructions from exact
generic-fiber reductions; a universal cleared Griffiths--Dwork certificate
over \(\mathbb Q(x,y)\) is still required.

The universal computation must reproduce this single-line identity or
expose another fixed direction. An extra direction within \(\mathcal T_7\)
changes the coefficient-extension architecture; a direction outside the
frozen relative surface and wall geometry is the carrier-level falsifier.
