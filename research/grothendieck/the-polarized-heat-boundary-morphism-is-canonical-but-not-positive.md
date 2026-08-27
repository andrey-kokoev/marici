# The polarized heat boundary morphism is canonical but not positive

## Positive regulated kernels

Let \(\rho\) be a nonnegative rapidly decreasing heat profile. For
\(\epsilon>0\), define

\[
K_{\rho,\epsilon}(s,w)
=
\sum_{n\geq1}n^{-s-\bar w}\rho(\epsilon n^2).
\]

Every such kernel is positive definite wherever the sum is defined. Indeed,
for a finite spectral packet,

\[
\sum_{i,j}a_i\overline{a_j}K_{\rho,\epsilon}(s_i,s_j)
=
\sum_{n\geq1}\rho(\epsilon n^2)
\left|\sum_i a_i n^{-s_i}\right|^2
\geq0.
\]

Thus heat regularization moves the exterior constant observer into an
ordinary positive Gram system.

## Canonical relative boundary value

Write \(z=s+\bar w\). Mellin analysis separates a heat boundary term

\[
B_{\rho,\epsilon}(z)
=
\frac12\widehat\rho\!\left(\frac{1-z}{2}\right)
\epsilon^{(z-1)/2}.
\]

For the admitted heat profiles, the regulator-independent finite part is

\[
\operatorname{FP}_{\epsilon\downarrow0}
\bigl(K_{\rho,\epsilon}(s,w)-B_{\rho,\epsilon}(s+\bar w)\bigr)
=
\zeta(s+\bar w).
\]

This answers the previous path-dependence question at the scalar polarized
level: the heat approach supplies a canonical boundary morphism after its
source-derived divergent wall is retained.

## Positivity is lost by the boundary quotient

Can this finite-part morphism extend the positive Gram order? No. Take the
Gaussian profile \(\rho(x)=e^{-\pi x}\) at the exterior diagonal
\(s=w=0\). The regulated diagonal is strictly positive:

\[
K_\epsilon(0,0)
=
\sum_{n\geq1}e^{-\pi\epsilon n^2}>0.
\]

Jacobi inversion gives the exact decomposition

\[
\sum_{n\geq1}e^{-\pi\epsilon n^2}
=
\frac{1}{2\sqrt\epsilon}-\frac12
+
\frac1{\sqrt\epsilon}
\sum_{m\geq1}e^{-\pi m^2/\epsilon}.
\]

After removing the canonical heat wall, the finite part is

\[
\operatorname{FP}K_\epsilon(0,0)=-\frac12=\zeta(0).
\]

A positive diagonal has become negative. Therefore the canonical heat
finite-part map is not positive, and hence cannot be completely positive.

## Categorical meaning

The exterior observer is not obtained by adding one more Hilbert vector to
the interior Gram space. It is a relative boundary object. Its datum is the
pair

\[
(K_{\rho,\epsilon},B_{\rho,\epsilon}),
\]

not merely their finite difference. Taking the difference and then asking it
to remain positive erases the wall that made the limit meaningful.

This supplies the requested pullback correction. The useful square is not a
pullback inside the category of positive kernels. It must live in a relative
or boundary-bearing category whose morphisms retain both the positive bulk
Gram form and the signed heat boundary current.

## Scope

This theorem concerns the polarized zeta kernel. It does not decide whether
the fully completed theta object admits a larger positive energy after
reciprocal sewing. It does prove that such positivity cannot be inherited by
applying scalar finite-part extraction to the heat-regulated Gram kernel.
Completion would have to add a complementary boundary channel rather than
declare the finite part itself positive.

## Consequence for the RH programme

The canonical-observer gate closes, but the orientation gate remains. The
next construction should keep a relative Gram pair:

- positive regulated bulk;
- explicit heat wall;
- primitive and square conormal currents;
- reciprocal theta sewing;
- a Green pairing on the whole boundary-bearing object.

The sharp falsifier for that enlarged construction is a negative direction
of its completed relative energy after every named wall is retained. The
negative value \(\zeta(0)=-1/2\) is not itself that falsifier; it is evidence
that the scalar boundary quotient is the wrong carrier of positivity.

## Result

Heat regularization canonically realizes the Riemann readout as a relative
boundary value of positive polarized kernels. The canonical finite-part map
is nevertheless not positivity preserving. The fifth wall is therefore not
another positive comparison vector: it is the signed boundary coordinate
that must remain paired with the positive bulk.
