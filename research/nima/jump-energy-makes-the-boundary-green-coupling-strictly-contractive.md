# Jump energy makes the boundary Green coupling strictly contractive

## Relative norm in wall-jump coordinates

Use the relative history norm

\[
\|f\|_{\mathrm{rel}}^2
=
\int_{\mathbb R}w(u)|f'(u)|^2\,du
+
|f(-\infty)|^2
+
|f(+\infty)|^2,
\]

with

\[
w(u)=(1+|u|)^{1+\epsilon},
\qquad
\epsilon>0.
\]

Write normalized endpoint coordinates

\[
a=
\frac{f(-\infty)+f(+\infty)}{\sqrt2},
\qquad
b=
\frac{-f(-\infty)+f(+\infty)}{\sqrt2}.
\]

Then the endpoint contribution is

\[
|a|^2+|b|^2.
\]

The wall coordinate \(a\) can be represented by a constant history with zero derivative energy. The jump coordinate \(b\) cannot.

## Optimal jump energy

The endpoint difference is

\[
f(+\infty)-f(-\infty)
=
\sqrt2,b
=
\int f'(u)\,du.
\]

Let

\[
I_w=
\int_{\mathbb R}w(u)^{-1}\,du.
\]

Cauchy--Schwarz gives

\[
2|b|^2
\le
I_w
\int w|f'|^2.
\]

Equality is attained by a derivative proportional to \(w^{-1}\). Hence the optimal derivative cost for a prescribed jump is

\[
\inf
\int w|f'|^2
=
\frac{2|b|^2}{I_w}.
\]

Therefore the reduced endpoint energy is exactly

\[
E_{\partial}(a,b)
=
|a|^2
+
\left(1+\frac2{I_w}\right)|b|^2.
\]

For the polynomial weight,

\[
I_w
=
2\int_0^\infty(1+u)^{-1-\epsilon}\,du
=
\frac2\epsilon.
\]

Thus

\[
E_{\partial}(a,b)
=
|a|^2+(1+\epsilon)|b|^2.
\]

## Boundary Green operator

In the wall-jump basis, the endpoint Green matrix exchanges the two coordinates:

\[
\Omega_{wj}
=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}
\]

up to the frozen orientation sign.

Normalize by the reduced endpoint energy. The resulting operator has norm

\[
\|K_{\partial}\|
=
\frac1{\sqrt{1+\epsilon}}.
\]

Hence the boundary coupling is strictly contractive:

\[
\delta_{\mathrm{aux}}
=
1-
\frac1{\sqrt{1+\epsilon}}
>0.
\]

Because the odd operator factors through boundary traces, this is also the full bulk norm; there is no dark interior contribution.

## Transport and completion

Translated weights preserve \(I_w\), so the same constant holds on every Mellin-displaced label fiber. Euler coefficients scale both the source and boundary form and do not change the normalized contraction.

Thus the margin is uniform over primes, grades, and cutoffs.

## Authority qualification

The numerical margin depends on the chosen weight exponent \(\epsilon\). The theorem is source-authorized only if this weighted derivative energy is the declared Green rigging or is uniformly equivalent to it with controlled constants.

If the source permits the critical weight \(w(u)=1+|u|\), then \(I_w=\infty\), the jump can be spread with arbitrarily small energy, and the strict margin collapses.

## Consequence

Analytically, any supercritical relative weight \((1+|u|)^{1+\epsilon}\) closes the auxiliary contraction gate exactly. The remaining question is whether the theta source fixes such a supercritical weight rather than merely allowing it as a convenient topology.
