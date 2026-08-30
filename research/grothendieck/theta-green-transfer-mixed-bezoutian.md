# Green transfer closes to a mixed theta Bezoutian

## Half-line source transforms

Retain

\[
K(u)=\cosh(u/2)-\frac12e^{u/2}\Theta(e^{2u}),
\qquad
\Phi=(1/4-\partial_u^2)K.
\]

For

\[
\phi_w(u)=\cosh(\sqrt w\,u),
\qquad
\psi_w(u)=\partial_w\phi_w(u),
\]

define

\[
I(w)=\int_0^\infty K(u)\phi_w(u)\,du,
\qquad
J(w)=\int_0^\infty K(u)\psi_w(u)\,du,
\]

and

\[
P(w)=\int_0^\infty\Phi(u)\psi_w(u)\,du.
\]

Put \(c=1/4\) and \(\zeta_w=w-c\).

## Exact Green identities

The transform kernels obey

\[
(c-\partial_u^2)\phi_w=-\zeta_w\phi_w,
\]

and, after differentiation in \(w\),

\[
(c-\partial_u^2)\psi_w
=-\phi_w-\zeta_w\psi_w.
\]

At \(u=0\), evenness gives

\[
K'(0)=\phi_w'(0)=\psi_w'(0)=0,
\qquad \psi_w(0)=0.
\]

At infinity, the renormalized precursor and the admissible strip make the
Green boundary form vanish. Hence transfer of
\(c-\partial_u^2\) is exact and gives

\[
\boxed{
\int_0^\infty\Phi(u)\phi_w(u)\,du=-\zeta_w I(w),
}
\]

and

\[
\boxed{P(w)=-I(w)-\zeta_wJ(w).}
\]

No residual endpoint term remains after the canonical null-mode subtraction.

## Mixed Bezoutian identity

The precursor pullback of the denominator-free Loewner kernel was

\[
L_C(x,y)=
\frac{\zeta_x\zeta_y}{x-y}
\left[
\zeta_xJ(x)I(y)-\zeta_yJ(y)I(x)
\right].
\]

Substituting \(\zeta J=-I-P\), the pure \(I(x)I(y)\) terms cancel exactly:

\[
\boxed{
L_C(x,y)=
\frac{\zeta_x\zeta_y}{x-y}
\left[I(x)P(y)-P(x)I(y)\right].
}
\]

Equivalently,

\[
L_C(x,y)=
\frac{\zeta_x\zeta_y}{x-y}
\int_0^\infty\!\!\int_0^\infty
K(u)\Phi(v)
\left[
\phi_x(u)\psi_y(v)-\psi_x(v)\phi_y(u)
\right]du\,dv.
\]

Thus Green transfer replaces the \(K\)-\(K\) derivative coupling by a mixed
\(K\)-\(\Phi\) Bezoutian. It preserves the full sign information and the
centered multipliers.

## What this decides

The simplest hoped-for mechanism was:

\[
\text{source operator} + \text{integration by parts}
\Longrightarrow \text{manifest square}.
\]

That mechanism does not occur. Green transfer cancels the null-mode and pure
precursor pieces, but the surviving determinant is still antisymmetric before
division by \(x-y\). No pointwise-positive integrand or immediate norm square
appears.

This is a mechanism falsifier, not a falsifier of Loewner positivity. The
mixed Bezoutian may still be positive after complete integration because of a
stronger comparison relation between \(K\) and \(\Phi\).

## Revised source theorem

Where \(I\ne0\), define

\[
R(w)=\frac{P(w)}{I(w)}.
\]

The Green identity immediately gives \(R=-H\). Thus this ratio is a faithful
pullback, not a new simplification of the unknown function. Its convergent
positive-precursor form is restricted to \(0<x<1/4\), where diagonal Loewner
positivity becomes an explicit positive-response versus variance inequality;
it is not automatic. See `theta-central-strip-diagonal-variance-gate.md`.

Then

\[
L_C(x,y)=
\zeta_x\zeta_y I(x)I(y)
\frac{R(y)-R(x)}{x-y}.
\]

Consequently a source-side Gram theorem is equivalent, away from transform
zeros, to matrix monotone **decrease** of the mixed response ratio
\(R=P/I\): the displayed divided difference has diagonal value \(-R'(x)\).
The factors \(\zeta_xI(x)\) act only by real congruence on each zero-free
interval. This ratio is not an arbitrary reconstruction: its numerator and
denominator are paired by the Green operator.

The next admissible attack is to derive a comparison theorem for the pair
\((K,\Phi)\), possibly from increasing curvature of the modular source or a
Sturm comparison principle. Reapplying integration by parts without new
source information will only reproduce the same Bezoutian.

## Falsifiers

1. A negative finite Loewner minor of \(L_C\) falsifies the global theorem.
2. A failure of monotonicity for \(R\) on a zero-free real interval falsifies
   the proposed mixed-response mechanism there.
3. A pointwise sign failure of the double integrand does not count; only the
   fully integrated Bezoutian is the source object.
