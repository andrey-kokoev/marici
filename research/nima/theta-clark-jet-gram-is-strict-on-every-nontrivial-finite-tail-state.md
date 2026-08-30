# The Clark-jet Gram is strict on every nontrivial finite tail state

## Status

Exact finite-cutoff definiteness theorem. Once the spectral derivative of the
source tail is retained, the Clark feature pair cannot vanish on a nontrivial
forced tail state. This proves state-class strictness of the positive Clark
bulk for every nonzero normal parameter.

The RH-bearing gap is no longer finite positivity of this feature packet. It is
the operator identity placing the Clark Gram into the doubled Green balance,
the typed closure of the remaining defect currents, and stability under
completion.

## Source tail and its spectral jet

Let \(f_X\) be a nonzero finite-cutoff source and let the constant source
channel \(c_X\neq0\) be independent of \(z\). The tail state satisfies

\[
(\partial_q+z)G_X=-f_Xc_X.
\]

Differentiate this identity with respect to \(z\):

\[
(\partial_q+z)\partial_zG_X+G_X=0.
\]

This spectral-jet equation is forced by the same source operator. It is not an
extra fitted constraint.

## Clark feature map

For real normal coordinate \(a\neq0\), define

\[
J_{X,a}(G_X,c_X)
=
\left(
G_X+f_Xc_X,
a\partial_zG_X
\right).
\]

Its Gram energy is

\[
\mathcal E_{X,a}
=
2\lVert G_X+f_Xc_X\rVert^2
+2a^2\lVert\partial_zG_X\rVert^2.
\]

This is exactly the positive bulk obtained by summing the two native Clark
sheets.

## Strictness theorem

Suppose

\[
\mathcal E_{X,a}=0.
\]

Both nonnegative terms must vanish:

\[
G_X+f_Xc_X=0,
\qquad
\partial_zG_X=0
\]

almost everywhere.

Insert the second equality into the spectral-jet equation. It gives

\[
G_X=0.
\]

The first equality then gives

\[
f_Xc_X=0.
\]

This contradicts \(f_X\neq0\) and \(c_X\neq0\). Therefore

\[
\mathcal E_{X,a}>0
\]

for every nontrivial forced tail state and every \(a\neq0\).

No zero location, scalar logarithmic derivative, global kernel positivity, or
primewise sign assumption enters the proof.

## Stronger than generic faithfulness

The earlier Clark Gram identity established faithfulness on the abstract
feature pair

\[
(G_X+f_Xc_X,a\partial_zG_X).
\]

The spectral-jet equation now proves that the actual source-state map into this
pair is injective on every nontrivial forced tail state. This removes the
finite PBH-style invisible-state possibility for the Clark bulk.

The proof is source-local and survives arbitrary finite label aggregation as
long as differentiation in \(z\) commutes with the finite source sum.

## Seam degeneration is correctly typed

At

\[
a=0
\]

the derivative feature is multiplied away. The theorem intentionally makes no
strictness claim there. This is compatible with the objective: the balance law
needs strict energy to exclude \(a\neq0\), while zeros are permitted on the
critical seam.

The degeneration is therefore structural rather than a defect.

## What this does not prove

The theorem does not yet show that \(\mathcal E_{X,a}\) is the energy appearing
in the exact doubled Green identity. That requires the source-fixed coefficient
of the reflection correction.

It also does not show that the defect packet

\[
\mathcal R_X^{(1)},
\quad
\mathcal R_X^{(2)},
\quad
\mathcal R_X^{(\geq3)},
\quad
\mathcal R_X^{(\infty)},
\quad
\mathcal R_X^{(\rm seam)}
\]

closes into boundary flux or into this Gram energy.

Finally, finite strictness supplies no uniform completion bound. A sequence of
normalized source states could still have Clark energy tending to zero unless
the arithmetic completion controls the spectral jet.

## Revised finite-cutoff target

The finite calculation should no longer spend effort testing positivity of the
Clark feature matrix. It should prove or falsify the exact identity

\[
2a\,\mathcal E_{X,a}
=
-\partial_q\mathcal J_X
+\mathcal R_X^{\rm defect}
\]

with source-fixed normalization.

The route advances if

\[
\mathcal R_X^{\rm defect}=0
\]

as a typed distribution after every declared current is included. A single
nonzero residual is the finite falsifier.

## Completion gate

Let \(x_X\) be admissible zero-states normalized in the constructor-generated
coefficient topology. The remaining positivity problem is precisely whether

\[
\mathcal E_{X,a}(x_X)\longrightarrow0
\]

can occur for fixed \(a\neq0\) while the zero-state constraints survive.

Preventing that escape requires continuity of the spectral-jet row and a
uniform lower bound on the zero-state class. It is not supplied by the finite
argument alone.

## Decisive conclusion

The source tail equation and its spectral derivative make the native Clark
Gram strictly positive on every nontrivial finite forced state away from the
seam. The finite orientation problem has therefore moved entirely to defect
closure and coefficient normalization in the doubled Green identity.

If exact Fourier--Tate sewing places this Gram into the balance and completion
preserves its strictness, the zero-state identity forces the critical seam. If
the typed residual survives, the route closes at that residual rather than at
positivity.
