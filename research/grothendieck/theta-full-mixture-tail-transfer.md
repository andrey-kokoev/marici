# Theta full-mixture tail transfer

Author: `marici.Grothendieck`
Status: quantitative transfer gate isolated
Predecessors: `theta-H-local-bochner-moments.md`, `theta-Q-bounded-interval-majorant.md`

## Question

Does the exact two-component local Bochner margin survive restoration of the theta components \(n\ge3\)?

## Baseline margin

Every single component satisfies

\[
e_n+4c_n^2>0.
\]

The elementary proof actually gives the uniform coarse margin

\[
e_n+4c_n^2>112
\qquad(n^2x\ge6),
\]

because the lower comparison \(16y^2-|e_n|\) is minimized at \(y=6\), where it equals \(112\). The exact two-component decomposition adds only nonnegative terms after the proved inequality \(Q>0\). Therefore

\[
g_2^{(4)}+4(g_2'')^2>112
\qquad(x\ge6).
\]

## Tail scale

Relative to \(T_1\), the first omitted weight satisfies

\[
R_3(x)
=9\frac{9x-3}{x-3}e^{-4x}
\le153e^{-24}
\qquad(x\ge6),
\]

and all later weights have an additional superexponential gap. The previously derived fourth-order absolute tail sum, when started at \(n=3\), has leading term

\[
32\cdot3^4\cdot52^4e^{-24}<1.
\]

Thus the obstruction that made the \(n=2\) fourth-cumulant bound exceed \(900\) disappears after the dominant pair is grouped.

## Aggregate perturbation identity

Write

\[
\Phi=\Phi_2(1+r),
\qquad
\Phi_2=T_1+T_2,
\qquad
r=\frac{\sum_{n\ge3}T_n}{\Phi_2},
\qquad
h=\log(1+r).
\]

Then \(g=g_2+h\), so the sufficient pointwise margin obeys the exact identity

\[
\left(g^{(4)}+4(g'')^2\right)
-
\left(g_2^{(4)}+4(g_2'')^2\right)
=h^{(4)}+8g_2''h''+4(h'')^2.
\]

All separate covariance and cumulant terms have recombined into derivatives of the single tail ratio. Since the last term is nonnegative, the certified baseline survives whenever

\[
|h^{(4)}|+8|g_2''|\,|h''|<112.
\]

This is the exact aggregate tail-transfer criterion. It is strictly weaker than separately bounding every fourth-order mixture cumulant and retains cancellations internal to the omitted tail.

## Tail-ratio derivative majorant

Set

\[
A=\sum_{n\ge3}R_n,
\qquad r=\frac{A}{1+R_2},
\qquad
\delta_n=(\log R_n)'.
\]

For \(m=n^2-1\) and \(x\ge6\), the component formulas give

\[
\begin{aligned}
R_n&\le2n^4e^{-mx/2},\\
|\delta_n|&\le mx+4,\\
|\delta_n'|&\le2mx+9,\\
|\delta_n''|&\le4mx+50,\\
|\delta_n'''|&\le8mx+420.
\end{aligned}
\]

Therefore

\[
|A''|
\le\sum_{n\ge3}R_n
\left((mx+4)^2+2mx+9\right)

after replacing each \(R_n\) by its displayed majorant, and

\[
\begin{aligned}
|A^{(4)}|
\le\sum_{n\ge3}R_n\big(&
(mx+4)^4
+6(mx+4)^2(2mx+9)\\
&+3(2mx+9)^2
+4(mx+4)(4mx+50)\\
&+8mx+420\big).
\end{aligned}
\]

Every summand decreases with \(x\ge6\); both bounds reduce to their \(x=6\) series. Quotient differentiation of \(r=A/(1+R_2)\), followed by

\[
h''=\frac{r''}{1+r}-\frac{(r')^2}{(1+r)^2},
\]

and the corresponding fourth derivative, converts these two series together with the already explicit \(R_2\) derivatives into the aggregate transfer bound. No unknown functional sign remains; the residual task is exact arithmetic evaluation of convergent positive series.

## Exact tail-series certification

An exact `Fraction` checker evaluates the positive-series bounds, the quotient derivatives of \(r=A/(1+R_2)\), and the logarithmic derivatives of \(h=\log(1+r)\). It proves

\[
|h''|<1.72654\times10^{-5},
\qquad
|h^{(4)}|<0.05645,
\]

and therefore

\[
|h^{(4)}|+8|g_2''||h''|
<0.05977<112.
\]

The complete theta mixture consequently satisfies the pointwise sufficient margin

\[
g^{(4)}+4(g'')^2>0
\qquad(u\in\mathbb R).
\]

Checker: `research/grothendieck/checkers/theta_tail_transfer_bound.py`.
Result: `research/grothendieck/results/theta_tail_transfer_bound.json`.
Execution: `structured_command_execution:e_19044_1788237313570362200_18`.

The deliberate-failure test scales the admitted tail envelope by \(2000\); its bound becomes \(119.52\ldots>112\), exhibiting the predicted loss of transfer.

## Finite-spacing three-point reduction

Normalize

\[
F(s)=\frac{H(s)}{H(0)}.
\]

The equally spaced three-point determinant is nonnegative exactly when

\[
2F(s)^2\le1+F(2s).
\]

Using the probability measure

\[
d\nu(d)=
\frac{d^2\Phi(d/2)^2}{4H(0)}\,dd
\]

with the normalization adjusted to the fixed Fourier convention, define

\[
X_s(d)=
\frac{
\Phi((s+d)/2)\Phi((s-d)/2)}
{
\Phi(d/2)^2}.
\]

Then

\[
F(s)=\mathbb E_\nu[X_s].
\]

Jensen gives \(F(s)^2\le\mathbb E_\nu[X_s^2]\). Hence a sufficient source-level finite-spacing condition is

\[
2X_s(d)^2\le1+X_{2s}(d)
\]

for every \(s,d\). This pointwise inequality is strictly stronger than the determinant and involves only four evaluations of the theta envelope. The proved local fourth-derivative margin is its integrated infinitesimal shadow, not a proof at finite spacing.

## Pointwise four-evaluation sweep

A bounded sweep evaluated

\[
P(s,d)=1+X_{2s}(d)-2X_s(d)^2
\]

for \(0.01\le s\le4\) and \(0\le d\le8\) on a mesh of spacing \(0.01\), using the positive theta mixture. No negative value occurred. The smallest sampled residual was

\[
P(0.01,0)
\approx7.867367179947848\times10^{-7}.
\]

Execution: `structured_command_execution:e_19044_1788237559830200100_19`.

This floating-point sweep is non-evidential and does not prove the pointwise inequality. Its minimum occurs near the infinitesimal regime already controlled by the local fourth-derivative theorem, and it identifies no finite-spacing oddball. The next analytic gate is a curvature-ratio bound for

\[
\varphi_d(s)=\log X_s(d),
\]

strong enough to compare \(\varphi_d(2s)\) with \(\varphi_d(s)\).

## Four-evaluation curvature ratio

Set

\[
\varphi_d(s)=\log X_s(d),
\qquad
a_d(s)=-\varphi_d(s),
\qquad
k_d(s)=-\varphi_d''(s)>0.
\]

Evenness gives \(a_d(0)=a_d'(0)=0\), and

\[
a_d(s)=\int_0^s(s-t)k_d(t)dt,
\]

with

\[
k_d(s)=-\frac14\left[
g''\!\left(\frac{s+d}{2}\right)
+g''\!\left(\frac{s-d}{2}\right)\right].
\]

The pointwise four-evaluation inequality is automatic when

\[
a_d(s)\ge\frac{\log2}{2}.
\]

In the remaining range it is exactly equivalent to

\[
a_d(2s)
\le
-\log\!\left(2e^{-2a_d(s)}-1\right).
\]

Thus only the bounded low-deficit region requires curvature control. A sufficient source criterion is obtained by bounding the weighted curvature integral on \([0,2s]\) relative to that on \([0,s]\); its admissible ratio is the explicit increasing function

\[
\frac{-\log(2e^{-2a}-1)}{4a},
\]

which tends to \(1\) as \(a\downarrow0\) and diverges as \(a\uparrow(\log2)/2\).

## Low-deficit ratio sweep and local gate

A log-sum-exp sweep over \(0.001\le s\le0.4\), \(0\le d\le8\) found no ratio above one in the low-deficit region. The largest sampled value was

\[
0.9999957955552004
\]

at \((s,d)=(0.001,0)\). Execution: `structured_command_execution:e_19044_1788237788404122300_21`. This is non-evidential.

The approach to one identifies a pointwise local gate distinct from the integrated theorem. Writing

\[
a_d(s)=\alpha s^2+\beta s^4+O(s^6)
\]

gives

\[
\alpha=\frac{k_d(0)}2,
\qquad
\beta=\frac{k_d''(0)}{24}.
\]

Expansion of the exact admissible bound yields

\[
-\log(2e^{-2a}-1)-a_d(2s)
=
\left(k_d(0)^2-rac12k_d''(0)\right)s^4
+O(s^6).
\]

Therefore the pointwise route requires

\[
2k_d(0)^2\ge k_d''(0)
\]

for every \(d\).

## Identification with the proved pointwise margin

The curvature definitions give

\[
k_d(0)=-\frac12g''\!\left(\frac d2\right),
\qquad
k_d''(0)=-\frac18g^{(4)}\!\left(\frac d2\right).
\]

Hence

\[
2k_d(0)^2-k_d''(0)
=\frac18\left(
g^{(4)}\!\left(\frac d2\right)
+4g''\!\left(\frac d2\right)^2
\right)>0.
\]

The exact full-mixture tail-transfer theorem already proved this pointwise margin for every argument. Thus the infinitesimal pointwise four-evaluation gate is closed; the remaining problem is uniform continuation from small positive \(s\) through the low-deficit interval.

## First-crossing test

Define the low-deficit slack

\[
S_d(s)=
-\log\!\left(2e^{-2a_d(s)}-1\right)-a_d(2s).
\]

At a hypothetical first positive crossing, \(S_d=0\) and \(S_d'\le0\). Direct differentiation gives

\[
S_d'(s)=
\frac{4e^{-2a_d(s)}}{2e^{-2a_d(s)}-1}
a_d'(s)-2a_d'(2s).
\]

Since

\[
a_d'(s)=\int_0^s k_d(t)dt,
\]

a first crossing is excluded by the explicit curvature-mass ratio

\[
\frac{
\int_0^{2s}k_d(t)dt}
{
\int_0^s k_d(t)dt}
<
\frac{2e^{-2a_d(s)}}{2e^{-2a_d(s)}-1}.
\]

The right side tends to \(2\) in the infinitesimal regime and diverges at the automatic large-deficit threshold. Thus the continuation problem is reduced to a bounded integral-curvature comparison with increasing admissible slack.

## Curvature-mass ratio sweep

The curvature masses require no numerical quadrature:

\[
a_d'(s)=-\frac12\left[
g'\!\left(\frac{s+d}{2}\right)
+g'\!\left(\frac{s-d}{2}\right)
\right].
\]

Thus the first-crossing criterion is another four-evaluation source inequality, now for \(g'\). A sweep over the same low-deficit grid found no violation. The smallest sampled slack was

\[
1.681795533814423\times10^{-5}
\]

at \((s,d)=(0.001,0)\), where the two sides were approximately

\[
2.0000019092
\quad\text{and}\quad
2.0000187272.
\]

Execution: `structured_command_execution:e_19044_1788238097846634400_22`.

This is non-evidential. It confirms that the tight regime is again the already certified infinitesimal boundary and exposes no interior first-crossing candidate. Exact continuation still requires a uniform derivative inequality, not denser sampling.

## First-crossing slack derivative

Let

\[
A_d(s)=a_d'(s)=\int_0^s k_d(t)dt
\]

and define the ratio slack

\[
\Sigma_d(s)=
\frac{2e^{-2a_d(s)}}{2e^{-2a_d(s)}-1}
-rac{A_d(2s)}{A_d(s)}.
\]

Exact differentiation gives

\[
\begin{aligned}
\Sigma_d'(s)={}&
\frac{4e^{-2a_d(s)}A_d(s)}
{(2e^{-2a_d(s)}-1)^2}\\
&-
\frac{2k_d(2s)A_d(s)-A_d(2s)k_d(s)}
{A_d(s)^2}.
\end{aligned}
\]

Therefore monotonicity of the first-crossing slack is reduced to an endpoint-curvature inequality involving only \(k_d(s)\), \(k_d(2s)\), and the two accumulated curvature masses. The source terms are explicit combinations of four values of \(g''\) and four values of \(g'\). No higher derivatives or spectral-zero data enter this gate.

## Endpoint-curvature sweep

A direct sweep of the exact slack-derivative formula, using mixture formulas for \(g'\) and \(g''\), found no negative value on the low-deficit grid. The smallest sampled derivative was

\[
0.03363644651254208
\]

at \((s,d)=(0.001,0)\). Execution: `structured_command_execution:e_19044_1788238300500492800_23`.

The minimum again lies at the infinitesimal boundary rather than at an interior separation. This supports, but does not certify, monotonicity of the first-crossing slack. An exact proof should factor the derivative by its vanishing power of \(s\) and reduce the remaining factor to the already positive pointwise margin plus a controlled finite-spacing remainder.

## Local factorization of the ratio slack

The original finite-spacing slack \(S_d\) and the first-crossing ratio slack \(\Sigma_d\) satisfy the exact identity

\[
S_d'(s)=2A_d(s)\Sigma_d(s).
\]

From the previous expansion,

\[
S_d(s)=
\frac18\left(
g^{(4)}\!\left(\frac d2\right)
+4g''\!\left(\frac d2\right)^2
\right)s^4+O(s^6),
\]

while

\[
A_d(s)=k_d(0)s+O(s^3).
\]

Therefore

\[
\lim_{s\downarrow0}
\frac{\Sigma_d(s)}{s^2}
=
\frac{
g^{(4)}(d/2)+4g''(d/2)^2
}{4k_d(0)}>0.
\]

This identifies the exact vanishing factor and shows that the certified pointwise margin is the leading coefficient of the derivative slack, explaining the sampled minimum at small \(s\). A finite-spacing proof must control only the normalized remainder after this positive \(s^2\) term is removed.

## Normalized slack remainder

Expand the curvature integral as

\[
a_d(s)=\alpha s^2+\beta s^4+\gamma s^6+O(s^8),
\]

where

\[
\alpha=\frac{k}{2},
\qquad
\beta=\frac{k''}{24},
\qquad
\gamma=\frac{k^{(4)}}{720}
\]

at \(s=0\). Using

\[
-\log(2e^{-2a}-1)=4a+4a^2+8a^3+O(a^4)
\]

and dividing the derivative slack by its exact \(s^2\) factor gives

\[
\frac{\Sigma_d(s)}{s^2}
=
\frac{g^{(4)}(d/2)+4g''(d/2)^2}{4k}
+C_6(d)s^2+O(s^4),
\]

with

\[
C_6=
3k^2+rac{k''}{6}
-rac{k^{(4)}}{4k}
+rac{(k'')^2}{6k^2}.
\]

Here

\[
k^{(4)}(0)=-\frac1{32}g^{(6)}\!\left(\frac d2\right).
\]

Thus the first normalized remainder introduces a genuine sixth-derivative condition. The fourth-order margin closes only the leading term; iterating local factorization recreates a higher-derivative hierarchy rather than proving finite-spacing continuation.

## Disposition

The full-mixture local fourth-derivative Bochner gate is proved. This establishes only the local necessary condition extracted from the equally spaced three-point determinant. It does not prove the determinant for finite spacing, full positive-definiteness of \(H\), the complete Laguerre hierarchy, or scalar-zero confinement. This is not yet a transfer theorem: the covariance, mixed-cumulant, component-fourth-derivative, and curvature-square perturbations must be bounded together. The next test is a single exact aggregate tail bound below \(112\), not separate sign claims for each omitted component.
