# The quartic reflection is not the elliptic deck involution

## Question

Is the symmetry \(t\mapsto-t\) of the infinity quartic the Geiser/deck involution, and can its action on the elliptic quotient select a parity?

## Two distinct involutions

The regular infinity curve has affine model

\[
C_E:\quad w^2=F(t),
\]

with \(F\) even in \(t\). Its hyperelliptic deck involution is

\[
j(t,w)=(t,-w).
\]

The quartic reflection has two lifts

\[
r_+(t,w)=(-t,w),
\qquad
r_-(t,w)=(-t,-w)=jr_+(t,w).
\]

Neither lift equals \(j\): both change the base coordinate \(t\), whereas \(j\) fixes it.

## Action on elliptic homology

For generic nonzero \(x,y\), \(r_+\) fixes the two points over \(t=0\), where \(w=\pm y\), and the two points over \(t=\infty\), where \(w/t^2=\pm x\). It therefore has four fixed points. Riemann--Hurwitz gives genus zero for the quotient \(C_E/r_+\), so the invariant part of \(H^1(C_E;\mathbb Z)\) vanishes and

\[
r_+^*=-I.
\]

The lift \(r_-=jr_+\) has no fixed points on a regular generic curve: at the fixed base points it would require \(w=0\), excluded by \(xy\ne0\). Its quotient has genus one, and it acts as a two-torsion translation on the elliptic curve. Hence

\[
r_-^*=I
\]

on \(H^1(C_E;\mathbb Z)\).

Both actions reduce to the identity modulo two.

## Surface-lift gate

This determines the action on the rank-two elliptic quotient but not on the rank-seven algebraic kernel of the del Pezzo complement. Extending \(r_+\) or \(r_-\) from the one-dimensional infinity section to the surface requires a global branch-curve equation and a compatible automorphism of the anticanonical double cover.

The one-variable quartic section does not supply that extension. Consequently node exchange on \(C_E\) cannot be promoted to a Picard action on \(e_6,v_{\rm alg}\).

## Combined disposition

The automorphism route now has the following result:

- visible site exchange is identity on the support plane modulo two;
- Geiser is identity on the algebraic kernel modulo two;
- both lifts of quartic reflection are identity on elliptic homology modulo two;
- no source supplies the reflection's action on the algebraic kernel.

Thus no known symmetry selects among \((1,0),(0,1),(1,1)\). The branch reopens only with a global del Pezzo branch equation or an explicit rank-nine Picard matrix lifting the quartic reflection.
