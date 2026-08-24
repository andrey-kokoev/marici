# Clark fold repair is an arithmetic positive commutator cocycle

Status: exact algebraic mechanism; Hardy/de Branges positivity remains open

For `n>=1`, define the source scale transport on half-line profiles by

\[
 (S_nf)(u)=n^{-1/2}f(u+\log n).                       \tag{1}
\]

The labelled theta modes satisfy

\[
 \phi_n=S_n\phi_1,                                   \tag{2}
\]

and the transports form an exact representation of the multiplicative
monoid:

\[
 \boxed{S_mS_n=S_{mn}.}                               \tag{3}
\]

Let the Clark fold observable be multiplication by

\[
 M_a=1-au,qquad a>0.                                 \tag{4}
\]

## Exact positive commutator

Direct calculation gives

\[
 \begin{aligned}
 (M_aS_n-S_nM_a)f(u)
 &=[1-au-(1-a(u+\log n))]S_nf(u)\\
 &=a\log n\,S_nf(u).
 \end{aligned}
\]

Therefore

\[
 \boxed{[M_a,S_n]=a\log n\,S_n.}                     \tag{5}
\]

Applied to the positive theta source, (5) is precisely the scale-displaced
fold repair found in the prime recursion:

\[
 M_aS_n\phi_1
 =S_nM_a\phi_1+a\log n\,S_n\phi_1.                  \tag{6}
\]

The final term is pointwise positive for `n>1`.  It is not fitted and cannot
be removed without breaking multiplicative covariance.

## The repair is a semigroup one-cocycle

Put

\[
 c_a(n)=a\log n\,S_n.                                 \tag{7}
\]

Then (3) and `log(mn)=log m+log n` give

\[
 \boxed{
 c_a(mn)=c_a(m)S_n+S_m c_a(n).
 }                                                     \tag{8}
\]

Thus the repair currents across different primes are compatible pieces of
one arithmetic `1`-cocycle.  Prime-by-prime repairs cannot be chosen
independently; unique factorization transports the same logarithmic cocycle
through every valuation filtration.

## Global labelled decomposition

Summing (6) over all labels yields, wherever the positive half-line source
sum is absolutely convergent,

\[
 \boxed{
 (1-au)\Phi(u)
 =\sum_{n\ge1}S_n[(1-au)\phi_1](u)
 +a\sum_{n\ge2}\log n\,S_n\phi_1(u).
 }                                                     \tag{9}
\]

The second sum is strictly positive.  The first is the complete orbit of one
primitive signed defect.  Hence all arithmetic complexity separates as

\[
 \text{one transported primitive fold}
 +\text{one positive logarithmic cocycle}.            \tag{10}
\]

This is the first decomposition in the Clark lane where the signed part is
not replicated as unrelated defects at every label.

## Fourier-side critical-strip covariance

On a Fourier--Laplace character `e^{izu}`, the scale transport has multiplier

\[
 \chi_z(n)=n^{-1/2}e^{-iz\log n}=n^{-1/2-iz}.         \tag{11}
\]

For `z=x+iy`,

\[
 |\chi_z(n)|=n^{y-1/2}.                               \tag{12}
\]

Every nontrivial arithmetic scale is strictly contractive exactly for
`y<1/2`, and its infinitesimal loss is controlled by the same `log n` that
appears in the repair cocycle:

\[
 \partial_y\chi_z(n)=\log n\,\chi_z(n).              \tag{13}
\]

Equations (5) and (13) identify the real-space fold repair with the normal
derivative of scale transport in the spectral plane.  This is the precise
bridge to the desired normal-modulus current.

## Positive-commutator target

The architecture now resembles a source-derived Mourre estimate:

\[
 \text{fold observable }M_a
 \quad\text{has oriented commutator with every }S_n.
\]

But (5) is not itself a Hilbert-space positive operator inequality: `S_n` is
not self-adjoint, and the primitive orbit in (9) remains signed.  The missing
step is to build the bilateral Hardy/de Branges energy in which the cocycle
polarization becomes

\[
 |E_a(z)|^2-|E_a^*(z)|^2
 =\sum_{n\ge2}(1-|\chi_z(n)|^2)\|R_{n,z}\|^2
 +\text{primitive boundary term},                    \tag{14}
\]

with the final term nonnegative after modular sewing.

The sharp falsifier is now algebraic rather than numerical: if exact
polarization of (9) leaves cross-prime terms that cannot be organized by the
cocycle identity (8) into a positive kernel or a canonical boundary term,
then arithmetic positive commutators do not close the Clark admission.

## Meaning

The hostile two-atom source has a fold but no multiplicative scale
representation and no logarithmic cocycle.  The completed theta source adds
exactly the missing explanatory structure:

\[
 \boxed{
 \text{signed fold}
 +\text{arithmetic scale covariance}
 =\text{forced oriented repair current}.
 }                                                     \tag{15}
\]

Whether that current dominates the coherently transported primitive defect
is the remaining RH-equivalent theorem.

## Faithful quotient coordinate gives stopped Dirichlet packets

The half-line labelled source has a more economical exact presentation.  In
the `n`th term set

\[
 v=u+\log n.
\]

Since `u>=0`, a label contributes over a fixed `v` precisely when
`n<=exp(v)`.  Exchanging the absolutely convergent source sum and integral
therefore gives

\[
 \boxed{
 F_+(z)=\int_0^\infty\phi_1(v)e^{izv}D_v(z)\,dv,
 }                                                     \tag{16}
\]

where

\[
 \boxed{
 D_v(z)=\sum_{n\le e^v}n^{-1/2-iz}.
 }                                                     \tag{17}
\]

Thus all arithmetic labels are the finite fiber of one faithful quotient
coordinate `v`; the fiber readout is a stopped Dirichlet polynomial.  The
cutoff `n<=exp(v)` is physical incidence data and must not be replaced by the
analytically divergent infinite Dirichlet series in the critical strip.

For the folded Clark density, `u=v-log n`, so

\[
 1-au=(1-av)+a\log n.                                 \tag{18}
\]

Consequently its half-line transform is

\[
 \boxed{
 E_{a,+}(z)=\frac12\int_0^\infty\phi_1(v)e^{izv}
 \left[(1-av)D_v(z)+ai\,\partial_zD_v(z)\right]dv.
 }                                                     \tag{19}
\]

The identity

\[
 i\partial_zD_v(z)
 =\sum_{n\le e^v}\log n\,n^{-1/2-iz}                \tag{20}
\]

shows that Nima's positive repair current is precisely the spectral
derivative of the stopped arithmetic packet.  No separate prime cross terms
remain outside `D_v`; they are organized by the finite fiber itself.

## New boundary localization

The function `D_v` is constant as a function of the label set on each cell

\[
 \log N\le v<\log(N+1),                               \tag{21}
\]

and jumps by the single character `N^(-1/2-iz)` at `v=log N`.  Hence the
remaining modular sewing can be formulated as a discrete boundary-current
problem across consecutive logarithmic cells.

The desired Hardy energy must combine:

1. the positive primitive density `phi_1(v)`;
2. the contractive characters `n^(-1/2-iz)` for `y<1/2`;
3. the derivative repair `i partial_z D_v`; and
4. the rank-one packet ingress at every `v=log N`.

This is a sharper attack surface than prime-by-prime polarization.  A proof
would be an exact summation-by-parts identity in `N` whose bulk is the
contractive character loss and whose jumps reproduce the Clark current.

Individual positivity of every `D_v` is not assumed and would be too strong:
finite positive-coefficient Dirichlet polynomials can retain destructive
phase interference.  Only the source-weighted, derivative-repaired sequence
of packet ingresses has physical meaning.

## Tail feature restores the Hilbert-space typing

The bare infinite character vector `(chi_z(n))_(n>=1)` is not in ordinary
`ell^2` for `y>0`, since

\[
 \sum_{n\ge1}|\chi_z(n)|^2
 =\sum_{n\ge1}n^{2y-1}=\infty.                        \tag{22}
\]

The stopped fibers above avoid this divergence by retaining the physical
incidence `n<=exp(v)` under the superexponentially decreasing primitive
weight.  Equivalently, integrate the source tail before sampling.  Put

\[
 G(q,z)=e^{-(1/2+iz)q}
 \int_q^\infty\phi_1(v)e^{izv}dv.                    \tag{23}
\]

For `q=log n`, the change of variables `v=u+log n` and
`phi_n(u)=n^(-1/2)phi_1(u+log n)` give the exact identity

\[
 \boxed{
 G(\log n,z)=\int_0^\infty\phi_n(u)e^{izu}du.
 }                                                     \tag{24}
\]

Thus `G` is the faithful transformed label feature.  It contains both the
arithmetic character and the source tail that makes sampling summable.

Differentiating in the scale variable gives Nima's forced flow

\[
 \boxed{
 \partial_qG(q,z)=-(1/2+iz)G(q,z)-e^{-q/2}\phi_1(q).
 }                                                     \tag{25}
\]

The forcing is real and strictly negative in this orientation; moving it to
the opposite side gives the positive boundary input `e^(-q/2)phi_1(q)`.

## Clark fold and repair are one differential feature

Let the `n`th half-line Clark contribution be

\[
 H_{n,a}(z)=\int_0^\infty(1-au)\phi_n(u)e^{izu}du.    \tag{26}
\]

Spectral differentiation of (24) yields

\[
 i\partial_zG(\log n,z)
 =-\int_0^\infty u\phi_n(u)e^{izu}du.
\]

Consequently

\[
 \boxed{
 H_{n,a}(z)=(1+ia\partial_z)G(\log n,z).
 }                                                     \tag{27}
\]

This is the correctly typed form of the positive-commutator mechanism.  The
signed primitive fold and the logarithmic displacement repair are not two
independent summands after transformation; they are the two components of
one source-derived differential feature.

The full bilateral Clark denominator is obtained by adding the reflected
feature at `-z` with the opposite fold orientation.  Nima's Green-identity
calculation can therefore work entirely with (25)--(27), sum only after
source-tail completion, and avoid both the divergent bare character Gram and
the false poles produced by dividing prime multipliers.
