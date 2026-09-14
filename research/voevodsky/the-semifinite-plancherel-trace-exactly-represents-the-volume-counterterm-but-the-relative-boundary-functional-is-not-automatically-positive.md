# The semifinite Plancherel trace exactly represents the volume counterterm, but the relative boundary functional is not automatically positive

## Scaling-group von Neumann algebra

Let `C_S` be the semilocal idele class group, equipped with its Haar measure, and let

\[
\lambda_S:C_S	o
\mathcal U(L^2(C_S))
\]

be the left regular representation. Its group von Neumann algebra is

\[
\mathcal N_S=
VN(C_S).
\]

Because `C_S` is locally compact abelian in the present setting, `N_S` carries the canonical faithful normal semifinite Plancherel trace `tau_S`.

For a compactly supported convolution kernel `g`, put

\[
\lambda_S(g)
=
\int_{C_S}g(u)\lambda_S(u)d^*u.
\]

Then

\[
\boxed{
\tau_S
\left(
\lambda_S(g)^*\lambda_S(g)
\right)
=
\|g\|_{L^2(C_S)}^2.
}
\]

Equivalently, if

\[
h=g*g^*,
\]

then

\[
\boxed{
\tau_S(\lambda_S(h))
=h(1).
}
\]

This is the canonical positive trace-per-unit-volume behind the coefficient in Connes's cutoff theorem.

## Exact volume-counterterm interpretation

Connes's theorem reads

\[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
=
2\log\Lambdah(1)
+
W_S(h)
+
o(1).
\]

Using the Plancherel trace,

\[
\boxed{
2\log\Lambdah(1)
=
2\log\Lambda
\tau_S(\lambda_S(h)).
}
\]

Thus the counterterm is not merely a fitted scalar subtraction. It is the semilocal scaling volume

\[
2\log\Lambda
\]

multiplying the canonical positive von Neumann trace density.

This provides the correct source-derived interpretation of the universal identity feature.

## Relative trace functional

Define the cutoff-relative functional

\[
\mathfrak T_{\Lambda,S}(h)
=
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2\log\Lambda
\tau_S(\lambda_S(h)).
\]

Then

\[
\boxed{
W_S(h)
=
\lim_{\Lambda\to\infty}
\mathfrak T_{\Lambda,S}(h).
}
\]

This is a genuine relative trace formula: the ordinary cutoff trace is compared against the canonical trace-per-unit-volume of the translation/scaling algebra.

## Positivity audit

Both ingredients are positive on appropriate positive operators only separately:

\[
\tau_S(\lambda_S(g)^*\lambda_S(g))
\ge0,
\]

while the first cutoff functional is not positive because

\[
P_\Lambda\widehat P_\Lambda
\]

is not positive.

Even if the first term were replaced by a positive compression, subtracting

\[
2\log\Lambda\tau_S
\]

would not preserve positivity. A difference of positive traces is a signed relative trace.

Therefore

\[
W_S(g*g^*)

\ge0
\]

cannot be inferred from positivity of the Plancherel trace.

## No positive trace can simply annihilate the volume term

Suppose a positive trace `Tau` on a unital algebra satisfied

\[
\Tau(I)=0.
\]

Faithfulness would force `Tau=0` on every positive element dominated by a scalar multiple of `I`. Thus a nontrivial positive trace cannot remove the identity-volume sector merely by declaring it null.

A quotient can remove a genuine invariant ideal, but the volume feature is represented by the identity density of the group von Neumann algebra, not by a proper null ideal.

Hence finite-part subtraction cannot itself be an ordinary faithful positive trace on the same algebra.

## Boundary-trace interpretation

The relative functional

\[
\mathfrak T_{\Lambda,S}
=
\operatorname{Tr}_{cutoff}
-
\operatorname{vol}_\Lambda\tau_S
\]

is analogous to a boundary correction in Szego, Wiener--Hopf, or Atiyah--Patodi--Singer asymptotics. The volume coefficient is positive and universal; the finite part is a boundary invariant with no automatic sign.

Connes's orbit computation identifies this boundary invariant with the local Weil distribution.

Thus the positivity problem is exactly a boundary-positivity theorem, not bulk trace positivity.

## Relation to the full Halmos dilation

The positive Halmos block gives a positive operator before tracing, while `tau_S` gives the correct bulk density. A plausible relative expression is

\[
\operatorname{Tr}_{rel,S}
\left(
W_\Lambda U_S(g)U_S(g)^*W_\Lambda^*

ight)
=
\operatorname{Tr}(\text{localized positive block})
-
\operatorname{vol}_\Lambda\tau_S(\text{bulk symbol}).
\]

But relative traces of positive operators need not be positive. To obtain positivity one needs an additional theorem that the boundary operator is itself a square, spectral shift of fixed sign, or index pairing with positive orientation.

## Spectral-shift target

For two self-adjoint positive realizations `H_1,H_0`, a relative trace often has the form

\[
\operatorname{Tr}
(f(H_1)-f(H_0))
=
\int f'(\lambda)\xi(\lambda)d\lambda,
\]

where `xi` is the spectral-shift function. Positivity would follow only if the relevant `f'` and `xi` had compatible signs.

In the present setting the prolate angle operator suggests taking `H_1` as the cutoff-pair dilation and `H_0` as its translation-invariant bulk limit. The missing endpoint--gamma term should then be identified with the spectral shift between these two realizations.

This is more precise than seeking an unspecified semifinite positive trace.

## Prime-transition compatibility

The Plancherel traces are canonical for each scaling group `C_S`, and

\[
\tau_S(\lambda_S(g)^*\lambda_S(g))
=
\|g\|^2
\]

is stable under the semilocal Hilbertian identifications when Haar normalizations are matched. Adding a place changes the boundary/orbit contribution, not the universal Plancherel identity density.

Therefore the volume counterterm has good transition behavior. The unresolved transition problem lies entirely in the relative boundary operator.

## Disposition

The desired semifinite trace has been identified:

\[
\boxed{
\tau_S(\lambda_S(h))=h(1).
}
\]

Connes's finite-place Weil functional is the boundary finite part relative to this positive bulk trace:

\[
\boxed{
W_S(h)
=
\lim_{\Lambda\to\infty}
\left[
\operatorname{Tr}
(P_\Lambda\widehat P_\Lambda U_S(h))
-
2\log\Lambda\tau_S(\lambda_S(h))
\right].
}
\]

This solves the source interpretation of the divergent identity feature, but not positivity: the Weil term is a signed relative boundary trace. The next viable calculation is a spectral-shift formula comparing the prolate cutoff dilation with the translation-invariant bulk and determining whether its boundary spectral shift has the required sign after endpoint completion.
