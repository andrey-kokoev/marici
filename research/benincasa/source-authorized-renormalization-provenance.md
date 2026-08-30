# Source-authorized renormalization provenance

## Question

Does the frozen one-loop three-site source determine a finite subtraction map
whose action on the rank-seven interaction quotient can be tested?

## Primary source

The frozen source is Benincasa--Brunello--Mandal--Mastrolia--Vazão,
arXiv:2408.16386v2.

Its equation (5) retains an interaction order (k), coupling
(lambda_k), and cosmological Mellin exponent.  Equation (6) defines the
general cosmological integral but explicitly omits coupling-dependent factors
and permits an unspecified polynomial numerator
(mathfrak n_\delta) of degree (delta).  Equations (12)--(17) introduce
analytic regulators for the twisted-period calculation.  Equations
(51)--(52) specialize the denominator geometry of the homogeneous one-loop
three-site graph.

The paper contains no counterterm basis, subtraction coefficients, finite
normalization condition, or map from its regulated master system to a
scheme-independent finite observable.  The directly cited construction
papers arXiv:1709.02813 and arXiv:1909.02517, and the cited (i\epsilon)
analysis arXiv:2305.19686, likewise do not define such a map.

## Loop/contact type correction

On the already derived rank-seven interaction basis

\[
(L_1,L_2,L_3,D_1,D_2,D_3,U),
\]

cyclic covariance leaves the three-dimensional polynomial module

\[
\left\langle
L_1+L_2+L_3,
D_1+D_2+D_3,
U
\right\rangle.
\]

Fixing the overall normalization removes at most (U).  Two independent
nonconstant cyclic loop-polynomial directions remain:

\[
\left\langle
L_1+L_2+L_3,
D_1+D_2+D_3
\right\rangle.
\]

These polynomials depend on the loop coordinates (a,b,c).  They are
therefore not spacetime-local counterterms.  A local counterterm has no loop
integration variable and enters the fixed-cycle observer through the contact
port.  Quotienting by either loop polynomial would be a category error.

The direct fixed-cycle calculation predeclared that contact port.  At both
generic unequal-energy samples,

\[
\operatorname{rank}(\text{ten responses})=10,
\qquad
\operatorname{rank}(1\oplus\text{responses})=11.
\]

Hence the score image has zero intersection with the loop-independent contact
port.  Any source-authorized local finite counterterm may translate the
contact readout but cannot identify two rank-seven interaction classes.

## Classification

The graph-period source determines the regulated coefficient object but not
action-level counterterm coefficients.  Nevertheless, locality itself protects
the rank-seven quotient: action-level local shifts lie in a disjoint contact
port.

This is not a Carrier obstruction.  It is failure of the forgetful map

\[
\{
\text{theory, regulator, counterterms, renormalization condition}
\}
\longrightarrow
\{
\text{regulated marked graph period}
\}
\]

to be injective on finite readout maps.

## Graph-local finiteness correction

For the particular three-site graph tested here, no UV subtraction is needed.
On the primary fixed cycle (Gamma_\ell=\mathbb R^3), the weakest sector
used by the complete score audit has density

\[
\rho(\ell)
=
\frac{1}{q_{\mathfrak g_1}q_{\mathfrak g_2}
q_{\mathfrak g_3}q_{\mathcal G_{23}}}.
\]

At generic positive nonsoft energies all four walls are bounded away from
zero, and each is (O(|\ell|)) at infinity.  Hence

\[
d^3\ell\,\rho(\ell)=O(r^{-2})\,dr.
\]

Normal differentiation through cubic order does not worsen the infinity
degree.  Near a moving norm center, the third derivative is at worst
(O(r^{-2})), which remains locally integrable against (r^2dr).  The
complete cubic score tower therefore shares the open convergence strip

\[
2<\operatorname{Re}d<4.
\]

The source value (d=3+2\epsilon) has (epsilon=0) strictly inside this
strip.  Thus the graph-local source-authorized finite map is ordinary
evaluation at (epsilon=0), and its counterterm space is zero.  It acts as
the identity on the rank-seven interaction quotient.

## Next source gate

Freeze one primary theory-level source specifying:

1. the action and field content;
2. the interaction and derivative orders;
3. the regulator and local counterterm basis;
4. the renormalization conditions or physical normalization observable.

Only then can genuine scheme transformations be quotiented and rank-seven
renormalized faithfulness be tested.
