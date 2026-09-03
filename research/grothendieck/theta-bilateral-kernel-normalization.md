# Theta bilateral-kernel normalization

Author: `marici.Grothendieck`
Status: exact normalization derived
Predecessor: `source-current-row-programme-synthesis.md`

## Question

Does the theta envelope used in the common-forcing construction have an exact bilateral transform equal to the completed Riemann scalar, rather than equality only up to an unspecified factor or coordinate rescaling?

## Claim boundary

Use the completed function

\[
\xi(s)=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)
\]

and the standard theta kernel

\[
\Phi(u)=\sum_{n\ge1}
\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)
 e^{-\pi n^2e^{2u}}.
\]

After even continuation of \(\Phi\), the classical cosine representation is

\[
\xi\!\left(\tfrac12+it\right)
=\int_0^\infty\Phi(u)\cos(tu)du
=\tfrac12\int_{-\infty}^{\infty}\Phi(u)e^{itu}du.
\]

Analytic continuation with \(t=-iz\) gives

\[
\xi\!\left(\tfrac12+z\right)
=\tfrac12\int_{-\infty}^{\infty}\Phi(u)e^{-zu}du.
\]

Set

\[
a_\theta(q)=\Phi(2q).
\]

The change of variables \(u=2q\) then yields the exact identity

\[
\xi\!\left(\tfrac12+z\right)
=\int_{-\infty}^{\infty}e^{-2zq}a_\theta(q)dq.
\]

No additional completion factor remains, and the factor of two in the sheet exponent is fixed by the logarithmic-coordinate rescaling.

Because the theta kernel decays sufficiently at both ends, integration by parts gives

\[
\int_{-\infty}^{\infty}e^{-2zq}a_\theta'(q)dq
=2z\,\xi\!\left(\tfrac12+z\right).
\]

Thus every noncentral zero of \(\xi\) annihilates exactly the two-endpoint compatibility residual for

\[
b'(q)=e^{-2zq}a_\theta'(q).
\]

At the central point \(z=0\), the derivative moment vanishes independently because it is the integral of a total derivative; this degeneracy must not be counted as scalar-zero evidence.

## Positivity and total-positivity gate

Pointwise positivity and evenness of a bilateral kernel do not confine transform zeros to the imaginary axis. The positive even measure

\[
\mu=\delta_{-a}+c\delta_0+\delta_a,
\qquad c>2,
\]

has bilateral transform

\[
M(z)=2\cosh(az)+c.
\]

Its zeros satisfy

\[
az=\pm\operatorname{arcosh}(c/2)+(2k+1)i\pi,
\]

so they have nonzero real parts. Convolution with a sufficiently narrow positive even Gaussian gives a positive even smooth rapidly decreasing kernel whose transform multiplies \(M\) by a zero-free Gaussian factor and retains the same off-axis zeros. Positivity, evenness, smoothness, and rapid decay therefore cannot force zero work or critical-line confinement.

A Pólya-frequency or strict total-positivity theorem would be materially stronger: it constrains all translation minors, not only point values. No such theorem is currently derived for \(\Phi\). The first executable test is the order-two minor, equivalently log-concavity where \(\Phi>0\); failure at any point rules out total positivity already at order two, while passage would not establish higher orders.

## Order-two total-positivity tail test

For a positive translation kernel, order-two total positivity requires log-concavity:

\[
\Delta(u)=\Phi(u)\Phi''(u)-\Phi'(u)^2\leq0.
\]

As \(u\to+\infty\), the \(n=1\) summand dominates and

\[
\Phi(u)=4\pi^2e^{9u/2}e^{-\pi e^{2u}}
\left(1+O(e^{-2u})+O(e^{-3\pi e^{2u}})\right).
\]

Therefore

\[
(\log\Phi)''(u)
=-4\pi e^{2u}+O(e^{-2u})+O(e^{4u-3\pi e^{2u}})<0
\]

for sufficiently large \(u\). Even continuation gives the same conclusion as \(u\to-\infty\). Hence the theta kernel passes the necessary order-two test on both tails; any log-concavity failure is confined to a compact interval.

This is only a localization result. Tail log-concavity neither proves log-concavity on the compact remainder nor establishes higher translation minors. The next executable test is a certified compact-interval sign analysis of \(\Delta\), with truncation bounds for the theta series and its first two derivatives.

## Order-two center estimate

Evenness gives \(\Phi'(0)=0\), so the order-two minor at the center has the sign of \(\Phi''(0)\). For

\[
T_n(u)=\left(4\pi^2n^4e^{9u/2}-6\pi n^2e^{5u/2}\right)e^{-\pi n^2e^{2u}},
\]

direct differentiation at zero gives

\[
T_n''(0)=e^{-c_n}\left[
4\pi^2n^4\left((\tfrac92-2c_n)^2-4c_n\right)
-6\pi n^2\left((\tfrac52-2c_n)^2-4c_n\right)
\right],
\qquad c_n=\pi n^2.
\]

A hand interval estimate, using

\[
\frac{333}{106}<\pi<\frac{355}{113},
\]

claimed the bounds

\[
T_1''(0)<-17,
\qquad
0< T_2''(0)<\frac34,
\qquad
\sum_{n\ge3}|T_n''(0)|<\frac1{100}.
\]

Hence

\[
\Phi''(0)<-\frac{1624}{100}<0.
\]

Since \(\Phi(0)>0\),

\[
\Delta(0)=\Phi(0)\Phi''(0)<0.
\]

The displayed rational enclosures were not materialized in a checker or expanded into auditable remainder inequalities. They are therefore unverified. Floating-point differentiation independently supports \(\Phi''(0)<0\), but the center result is numerical evidence rather than a certified theorem.

## Conditional center neighborhood

The theta series and all of its derivatives converge locally uniformly, so

\[
\Delta(u)=\Phi(u)\Phi''(u)-\Phi'(u)^2
\]

is continuous. Conditional on a certified strict center bound \(\Delta(0)<0\), continuity implies that there is an \(\varepsilon>0\) such that

\[
\Delta(u)<0
\qquad\text{for }|u|<\varepsilon.
\]

Combined with eventual strict negativity on both tails, this reduces every possible order-two total-positivity obstruction to a closed annulus

\[
\varepsilon\le |u|\le U
\]

for some finite \(U\). This is a qualitative compact reduction: neither endpoint is numerically certified yet, so it does not authorize a finite subdivision claim. The next evidence-bearing step is to derive explicit rational \(\varepsilon,U\) from derivative and tail bounds before any interval subdivision.

## Unverified explicit annulus proposal

A coarse hand estimate asserted

\[
|\Delta''(u)|<10^{12}
\qquad (|u|\leq10^{-6}).
\]

Together with the center bounds \(\Phi(0)>89/100\) and \(\Phi''(0)<-1624/100\), evenness and Taylor's theorem yield

\[
\Delta(u)<-13
\qquad (|u|\leq10^{-6}).
\]

For \(u\geq1\), write \(\Phi=T_1(1+\rho)\). The first summand factors as

\[
T_1=4\pi^2e^{9u/2}e^{-\pi e^{2u}}
\left(1-\frac{3}{2\pi}e^{-2u}\right),
\]

whose logarithmic second derivative is strictly smaller than \(-4\pi e^{2u}\). The ratio of every \(n\geq2\) summand to \(T_1\), together with its first two derivatives, contains the factor

\[
e^{-\pi(n^2-1)e^{2u}}.
\]

At \(u=1\), rational exponential bounds give \(|\rho|+|\rho'|+|\rho''|<10^{-12}\), and the bound decreases with \(u\). Hence the perturbation of \((\log T_1)''\) is smaller than one, while \(-4\pi e^{2u}<-84\). Thus

\[
\Delta(u)<0
\qquad (|u|\geq1).
\]

If every asserted remainder bound above is verified, every possible order-two failure is confined to

\[
10^{-6}\leq |u|\leq1.
\]

## Compact-annulus exploratory scan

A direct 10,001-point scan on \(0\leq u\leq1\), summing \(n=1,\ldots,19\) and differentiating each summand analytically, found

\[
\min\Delta=-14.946925678645503
\quad\text{at }u=0,
\]

and

\[
\max\Delta=-7.073257911829256\times10^{-12}
\quad\text{at }u=1.
\]

No positive sample occurred. Execution reference: `structured_command_execution:e_19044_1788224903155706500_2`.

This is floating-point exploratory evidence, not a checker or interval proof. Its smallest margin occurs at the tail endpoint because \(\Phi\) itself is extremely small there; absolute residual subdivision would therefore be ill-conditioned. The exact certification should instead bound

\[
(\log\Phi)''=\frac{\Delta}{\Phi^2},
\]

whose tail margin grows in magnitude, using rational interval bounds and an explicit theta-series remainder.

## Positive-mixture PF2 candidate

For \(u\geq0\), every summand is positive and can be written

\[
T_n(u)=2\pi n^2e^{5u/2}e^{-\pi n^2e^{2u}}
\left(2\pi n^2e^{2u}-3\right).
\]

Let \(w_n=T_n/\Phi\), \(\ell_n=(\log T_n)'\), and \(c_n=(\log T_n)''\). The logarithmic curvature of the sum is

\[
(\log\Phi)''=
\sum_n w_nc_n+
\operatorname{Var}_w(\ell_n).
\]

Putting \(E=e^{2u}\geq1\), direct differentiation gives

\[
c_n=-4\pi n^2E-
\frac{24\pi n^2E}{(2\pi n^2E-3)^2}
<-4\pi E.
\]

The proposed proof claims that the relative tail is maximized at \(E=1\) and applies exponential bounds to

\[
\frac{T_n}{T_1}
=n^2\frac{2\pi n^2E-3}{2\pi E-3}
 e^{-\pi(n^2-1)E}.
\]

The unmaterialized bounds are

\[
\sum_{n\ge2}\frac{T_n}{T_1}<\frac1{400},
\qquad
\operatorname{Var}_w(\ell_n)<2.
\]

The polynomial growth of the slope differences is dominated uniformly by the same Gaussian tail; its maximum also occurs at \(E=1\). Consequently

\[
(\log\Phi)''<-4\pi+2<-10
\qquad (u\geq0).
\]

The exact mixture identity and formula for \(c_n\) are valid, but the uniform tail maximum and variance estimate were asserted without a termwise proof or exact checker. Global strict log-concavity is therefore not established. The 10,001-point scan supports it numerically; PF2 remains an unverified conjecture.

## Order-three coalescent center test

For the translation kernel \(K(x,y)=\Phi(x-y)\), the coalescent order-three minor is governed, up to the standard positive factorial and orientation factors, by

\[
-H_3(u),
\qquad
H_3(u)=\det\bigl[\Phi^{(i+j)}(u)\bigr]_{i,j=0}^{2}.
\]

At the even center, odd derivatives vanish and

\[
H_3(0)=\Phi''(0)
\left(\Phi(0)\Phi^{(4)}(0)-\Phi''(0)^2\right).
\]

Termwise analytic differentiation through order four and a 19-term exploratory evaluation gave

\[
\Phi(0)=0.8933938009342468,
\quad
\Phi''(0)=-16.730500774703245,
\quad
\Phi^{(4)}(0)=812.1628334554266,
\]

and therefore

\[
-H_3(0)=7456.308791178048>0.
\]

Execution reference: `structured_command_execution:e_19044_1788225167149876900_4`. This is a non-certifying floating-point test, but the margin is not close to zero. The coalescent center does not falsify order-three total positivity. Noncoalescent three-point minors remain independent and are the next discriminating test.

## Noncoalescent order-three search

A seeded exploratory search evaluated

\[
D_3(x,y)=\det[\Phi(x_i-y_j)]_{i,j=1}^{3}
\]

for 200,000 randomly generated strictly ordered triples, using 19 theta terms and scaling each matrix by its largest entry before taking the determinant. No negative determinant was found. The smallest normalized value was

\[
1.8451007491924083\times10^{-104}
\]

at

\[
x=(0.9997095170,1.7063623764,2.1514574927),
\]

\[
y=(0,0.0033579818,0.1137271103).
\]

Execution reference: `structured_command_execution:e_19044_1788225281746941000_5`.

This is non-certifying evidence. The minimum occurs near a partially coalescent and tail-scaled configuration, where ordinary floating-point determinants are ill-conditioned. It supplies no proof of PF3, but it redirects the falsification attempt to high-precision or interval evaluation of that explicit configuration and its neighborhood rather than another untargeted search.

## Disposition

The theta-to-endpoint-closure map is source-normalized exactly. This strengthens only bare endpoint closure. The Hermitian work identity still gives

\[
R_\theta=-\operatorname{Re}(z)B_\theta
\]

on scalar-zero closed endpoints, so the normalization result does not prove work sewing or confinement. Order-two total positivity has passed only exploratory numerical tests; the unmaterialized uniform tail and variance estimates prevent a global theorem. Higher translation minors remain separate and are not implied by log-concavity.
