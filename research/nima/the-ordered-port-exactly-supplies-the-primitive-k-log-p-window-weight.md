# The ordered port exactly supplies the primitive `k log p` window weight

## Differentiated front and primitive window

Let `W_t` be the source primitive window and

\[
q_t=DW_t
\]

its differentiated front. On the retained rapid/wall graph, the ordered port
satisfies

\[
SD=-2I.
\]

Therefore

\[
Sq_t=SDW_t=-2W_t.
\]

No inverse choice or fitted integration constant occurs: the constant wall is
already a separate retained coordinate, and reciprocal oddness fixes the
ordered inverse derivative.

## Source-authorized primitive metric

Define the ordered primitive seminorm on differentiated fronts by pullback
through the ordered port:

\[
\|q\|_{\mathrm{ord}}^2
=\frac14\|Sq\|_{\u0001mathrm{res}}^2.
\]

For the source atoms this gives the exact identity

\[
\|q_t\|_{\mathrm{ord}}^2
=\|W_t\|_{\mathrm{res}}^2.
\]

Thus the primitive scale weight is not inserted to repair boundedness. It is
the graph norm of the already constructed ordered inverse derivative.

## Asymptotic label weight

The ordinary primitive window obeys

\[
\|W_t\|_2^2
=2t-\frac{\sqrt2}{\pi}+O(e^{-2\pi t^2}).
\]

The selected resolved norm contains this positive term and hence

\[
\|q_t\|_{\mathrm{ord}}^2
=\|W_t\|_{\mathrm{res}}^2
\asymp t
\]

on the arithmetic range `t>=log 2`, provided the already declared resolved
upper estimate is used together with its lower estimate.

At label `(p,k)`, where

\[
t=k\log p,
\]

the source metric therefore supplies

\[
\omega_{p,k}^2
:=\|q_{k\log p}\|_{\mathrm{ord}}^2
=\|W_{k\log p}\|_{\mathrm{res}}^2
\asymp k\log p.
\]

This is exactly the weight required by the primitive gamma-field comparison.

## Weighted gamma-field

The differentiated comparison sends `q_(p,k)` to the constant-norm cut atom
`u_(p,k)`. After equipping the source with the ordered primitive norm, a
bi-bounded primitive realization must transport the same scale to the target:

\[
\gamma_\theta^{\mathrm{prim}}e_{p,k}
=\omega_{p,k}u_{p,k}.
\]

Equivalently, retain the unweighted cut atoms but put the diagonal weight
`omega_(p,k)^2` in their Green metric. Merely weighting the source while
leaving the target norm constant would preserve continuity in one direction
but lose the inverse lower bound.

The primitive kernel becomes

\[
K_\theta^{\mathrm{prim}}(\alpha,\beta)
=
\omega_\alpha\omega_\beta
\langle u_\beta,u_\alpha\rangle_G.
\]

Finite-cutoff positivity is immediate as a Gram identity. The weight now has
source provenance from `S`, rather than from post-hoc norm balancing. A
separate constructor-naturality check must verify that this weighted target
is the actual primitive cut realization, not only an equivalent renorming.

## Reciprocal and dilation typing

Reflection gives

\[
RSR=-S,
\]

so the squared ordered norm is reciprocal-even while its unsquared current
retains odd orientation. Dilation gives

\[
U_a^{-1}SU_a=a^{-1}S,
\]

which is precisely the inverse-scale behavior expected of the primitive
window coordinate. Hence the weighted metric does not erase the ordered
Fourier--Tate signature.

## Consequence and remaining estimate

The previously missing source derivation of the primitive `k log p` weight is
closed algebraically:

\[
q_t\xmapsto{\ S\ }-2W_t.
\]

To complete the interior-profile gamma-field theorem one must still prove the
uniform resolved two-sided estimate

\[
c\,t
\le
\|W_t\|_{\mathrm{res}}^2
\le
C\,t,
\qquad t\ge\log2,
\]

and then verify projective cutoff convergence and Weyl-kernel covariance with
this weighted source topology. The lower bound follows from the displayed
ordinary window term; the unresolved analytic part is the uniform resolved
upper bound and its compatibility with the theta-cut synthesis.
