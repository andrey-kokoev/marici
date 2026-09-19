# The Clark-defect primitive admits a prime-loaded moving-seam rigged completion

## Moving primitive

Translate the fixed-seam primitive by `a`:

\[
K_a(x)
=-\frac12|x-a|+\delta_a.
\]

Then

\[
D_a:=\partial_xK_a
=-\frac12\operatorname{sgn}(x-a)+\delta_a'.
\]

Translation is exact:

\[
K_a=\tau_aK_0,
\qquad
D_a=\tau_aD_0,
\qquad
\partial_x\tau_a=\tau_a\partial_x.
\]

Thus the null-homotopy is natural under moving-seam transport before any prime
assembly.

## Concrete rigging

Choose

\[
s>\frac12,
\qquad
m>\frac32,
\]

and use the boundary-enlarged dual rung

\[
\mathcal E_{s,m}
=
L^2\!\left(\mathbb R,(1+x^2)^{-m}dx\right)
+H^{-s}(\mathbb R).
\]

The growing part belongs to the weighted summand because

\[
\int_{\mathbb R}|x-a|^2(1+x^2)^{-m}dx<\infty
\]

for `m>3/2`. The point mass belongs to `H^{-s}` for `s>1/2`. Hence

\[
K_a\in\mathcal E_{s,m}
\]

for every finite seam position.

Its derivative lies one rung lower:

\[
D_a\in
L^2((1+x^2)^{-m}dx)+H^{-s-1}(\mathbb R).
\]

Translation norms grow at most polynomially in `1+|a|` on these weighted
rungs.

## Prime loading

At prime-power seams

\[
a_{p,k}=k\log p,
\]

the source endpoint loading already contains the convergent scale
`p^{-3/2-sigma}` in the primitive channel. Therefore, for every fixed
polynomial translation order `N`,

\[
\sum_p
p^{-3/2-\sigma}(1+\log p)^N<\infty
\]

uniformly for `sigma>=0` on compact parameter sets. The same statement holds
at each fixed jet and prime-power grade after including its declared
exponential/half-density attenuation.

Consequently the family of loaded primitives

\[
\bigl\{
\omega_{p,k}K_{k\log p}
\bigr\}_{p,k}
\]

is summable in the corresponding projective rigged dual whenever the existing
source weights satisfy the frozen prime-power majorant.

## Cutoff and differential compatibility

Finite-prime restriction commutes termwise with translation and derivative.
Absolute convergence gives

\[
\partial_x
\sum_{p,k}\omega_{p,k}K_{k\log p}
=
\sum_{p,k}\omega_{p,k}D_{k\log p}
\]

in the lower dual rung, and cutoff limits commute with this identity.

## What closes

The canonical defect primitive now has:

- moving-seam naturality;
- a concrete boundary-enlarged rigged domain;
- prime/cutoff compatibility under the existing Euler majorant;
- a continuous differential into the defect rung.

## Remaining gate

This does not yet prove that the Clark/Grushin comparison maps preserve the
chosen rigging or that the complete arithmetic column uses this primitive.
The next finite-domain test is continuity of the six-channel projection and
odd-doubled Grushin differential on `E_(s,m)`, including the singular
`delta_a` component.