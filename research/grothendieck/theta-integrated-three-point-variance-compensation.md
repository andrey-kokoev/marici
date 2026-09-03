# Theta integrated three-point variance compensation

Author: `marici.Grothendieck`
Status: direct integrated route isolated
Predecessor: `theta-full-mixture-tail-transfer.md`

## Question

Can the equally spaced three-point Bochner determinant be proved directly, without the stronger pointwise four-evaluation hierarchy?

## Exact decomposition

Retain

\[
F(s)=\mathbb E_\nu[X_s],
\qquad
F(2s)=\mathbb E_\nu[X_{2s}].
\]

The normalized determinant factor is

\[
D_3(s)=1+F(2s)-2F(s)^2.
\]

Adding and subtracting \(2\mathbb E_\nu[X_s^2]\) gives the exact identity

\[
D_3(s)=
\mathbb E_\nu\!\left[
1+X_{2s}-2X_s^2
\right]
+2\operatorname{Var}_\nu(X_s).
\]

The pointwise route discarded the strictly nonnegative variance term by Jensen and therefore imposed the stronger condition

\[
1+X_{2s}(d)-2X_s(d)^2\ge0
\]

for every \(d\). Its recursive sixth- and higher-derivative gates are not necessary for the integrated determinant.

## Variance and automatic-spacing gates

For independent \(d,e\sim\nu\),

\[
2\operatorname{Var}_\nu(X_s)
=\mathbb E_{\nu\otimes\nu}
\left[(X_s(d)-X_s(e))^2\right].
\]

Thus compensation is an explicit positive double source integral, not an abstract probabilistic remainder.

Moreover, each integrand defining \(H(s)\) is even and strictly decreasing for \(s>0\), by strict concavity of \(\log\Phi\). Hence \(F(s)=H(s)/H(0)\) is strictly decreasing from one to zero. Whenever

\[
F(s)\le\frac1{\sqrt2},
\]

the determinant is automatic because

\[
D_3(s)=1+F(2s)-2F(s)^2\ge1-2F(s)^2\ge0.
\]

Only the bounded interval before the unique threshold \(F=1/\sqrt2\) requires variance compensation or a direct determinant estimate.

## Threshold-interval sweep

A positive-quadrature sweep of the direct source integral found the threshold

\[
F(s)=\frac1{\sqrt2}
\]

between mesh points immediately below \(s=0.245\); at that point the sampled value was

\[
F(0.245)\approx0.7022353914.
\]

The smallest sampled determinant residual was

\[
8.4297209435\times10^{-8}
\]

at \(s=0.005\), again in the certified infinitesimal regime. Execution: `structured_command_execution:e_19044_1788266633937232400_24`.

This is non-evidential quadrature. It identifies

\[
0<s<\frac14
\]

as a candidate interval containing the only nonautomatic region, but exact certification of \(F(1/4)<1/\sqrt2\) remains required. After that check, an exact proof can combine the local fourth-order lower bound near zero with interval arithmetic or derivative control on a fixed compact interval; no unbounded-spacing estimate remains.

## Exact automatic-spacing bound

The proved PF2 estimate gives the uniform curvature bound

\[
g''(u)<-10
\qquad(u\in\mathbb R).
\]

For \(a=s/2\), the second-difference integral therefore yields

\[
g(x+a)+g(x-a)-2g(x)
\le-10a^2.
\]

Hence every four-evaluation ratio obeys

\[
X_s(d)\le e^{-5s^2/2},
\]

and averaging gives

\[
F(s)\le e^{-5s^2/2}.
\]

Consequently

\[
F(s)\le\frac1{\sqrt2}
\]

whenever

\[
s\ge s_*=\sqrt{\frac{\log2}{5}}.
\]

The determinant is therefore proved for all \(s\ge s_*\). The sharper numerical threshold near \(0.245\) is not needed for an exact compact reduction; the remaining interval is

\[
0<s<s_*<\frac38.
\]

## Quantitative local determinant margin

Write

\[
F(s)=1+as^2+bs^4+O(s^6).
\]

Then

\[
D_3(s)=1+F(2s)-2F(s)^2
=(12b-2a^2)s^4+O(s^6).
\]

In terms of \(H\),

\[
12b-2a^2
=
\frac{H(0)H^{(4)}(0)-H''(0)^2}{2H(0)^2}.
\]

The pointwise full-mixture theorem gives

\[
g^{(4)}+4(g'')^2>112-0.05977>111.
\]

Averaging under \(\mu\) and using

\[
\mathbb E[(g'')^2]-\mathbb E[g'']^2\ge0
\]

therefore yields the explicit normalized coefficient bound

\[
12b-2a^2>\frac{111}{16}>6.9.
\]

Thus

\[
D_3(s)>6.9s^4+O(s^6).
\]

The compact-interval proof now has a quantitative local margin. It remains to bound the sixth-order remainder on a small exact interval and cover the separated interval up to \(s_*\).

## Sixth-order determinant coefficient

Extend the normalized expansion to

\[
F(s)=1+as^2+bs^4+cs^6+O(s^8).
\]

Direct substitution into

\[
D_3(s)=1+F(2s)-2F(s)^2
\]

gives

\[
D_3(s)=
(12b-2a^2)s^4
+(60c-4ab)s^6+O(s^8).
\]

In source derivatives,

\[
60c-4ab
=
\frac{
H(0)H^{(6)}(0)-H''(0)H^{(4)}(0)
}{12H(0)^2}.
\]

Thus the sixth-order remainder is governed by one new mixed derivative determinant. The fourth-order theorem supplies no sign or bound for this quantity. An exact local radius requires a quantitative estimate of

\[
\left|
H(0)H^{(6)}(0)-H''(0)H^{(4)}(0)
\right|

after normalization, followed by an eighth-order tail bound or interval remainder theorem. This is a bounded source-moment problem, not a zero-location premise.

## Sixth source-moment formula

Let

\[
h=g'',
\qquad q=g^{(4)},
\qquad r=g^{(6)}.
\]

Expanding

\[
g\!\left(x+\frac s2\right)
+g\!\left(x-\frac s2\right)

after exponentiation gives

\[
H^{(6)}(0)=I\,\mathbb E_\mu\!\left[
\frac1{16}r+rac{15}{8}hq+rac{15}{4}h^3
\right].
\]

Together with

\[
H''(0)=I\mathbb E_\mu[h],
\qquad
H^{(4)}(0)=I\mathbb E_\mu\!\left[
\frac14q+rac32h^2
\right],
\]

the normalized sixth coefficient is exactly

\[
\frac1{48}\left(
2\mathbb E_\mu\!\left[
\frac1{16}r+rac{15}{8}hq+rac{15}{4}h^3
\right]
-
\mathbb E_\mu[h]
\mathbb E_\mu\!\left[
\frac14q+rac32h^2
\right]
\right).
\]

This removes all derivatives of \(H\) from the gate. The remaining bound concerns explicit weighted moments of \(g''\), \(g^{(4)}\), and \(g^{(6)}\) under the already fixed theta measure \(\mu\).

## Elimination of the sixth derivative

With \(w=x^2e^{2g}\), two integrations by parts give

\[
\int w g^{(6)}dx
=
\int w''g^{(4)}dx,
\]

and

\[
\frac{w''}{w}
=
\frac2{x^2}+rac{8g'}x+2g''+4(g')^2.
\]

Substitution into the sixth source moment eliminates \(g^{(6)}\) exactly:

\[
\begin{aligned}
\mathbb E_\mu\!\left[
\frac1{16}g^{(6)}
+\frac{15}{8}g''g^{(4)}
+\frac{15}{4}(g'')^3
\right]
=
\mathbb E_\mu\!\Bigg[
&g^{(4)}\left(
\frac1{8x^2}+rac{g'}{2x}
+\frac{(g')^2}{4}+2g''
\right)\\
&+\frac{15}{4}(g'')^3
\Bigg].
\end{aligned}
\]

The apparent singular terms are integrable because \(d\mu\) contains \(x^2\). The sixth coefficient is therefore controlled entirely by weighted moments of \(g'\), \(g''\), and \(g^{(4)}\), all already available from the positive theta mixture.

## Absolute lower-derivative bound

Let

\[
A_4=\frac14g^{(4)}+\frac32(g'')^2
\]

and let \(A_6^{\rm IBP}\) denote the lower-derivative integrand obtained above. Cauchy--Schwarz gives the rigorous reduction

\[
|C_6|
\le
\frac1{48}\left(
2\mathbb E_\mu[|A_6^{\rm IBP}|]
+
\sqrt{\mathbb E_\mu[(g'')^2]}
\sqrt{\mathbb E_\mu[A_4^2]}
\right),
\]

where \(C_6\) is the coefficient of \(s^6\) in \(D_3\). Thus no sign theorem is required: certified upper bounds for three positive source moments suffice.

A high-precision reconnaissance attempt was blocked because `mpmath` was absent and the structured-command policy refused the ephemeral `uv --with mpmath` preflight. No numerical estimate is promoted from that attempt. The exact next gate is to bound the three displayed moments using the existing dominant-component plus tail-transfer decomposition.

## Component-polynomial tail transfer

For quantitative bounds it is preferable to leave logarithmic derivatives and return to the positive component expansion

\[
\Phi(u)=\sum_{n\ge1}T_n(u).
\]

Put \(y_n=2\pi n^2e^{2u}\) and

\[
\ell_n(y)=\frac52-y+\frac{2y}{y-3}.
\]

Every component derivative has the form

\[
T_n^{(j)}(u)=T_n(u)P_j(y_n),
\]

where

\[
P_0=1,
\qquad
P_{j+1}(y)=\ell_n(y)P_j(y)+2yP_j'(y).
\]

Therefore all derivatives through order eight required for a Taylor remainder are finite sums of positive exponential components multiplied by explicit rational functions. Differentiating the defining integral gives

\[
H^{(k)}(s)=
2^{-k-2}\int d^2
\sum_{j=0}^k(-1)^{k-j}\binom{k}{j}
\Phi^{(j)}\!\left(\frac{s+d}{2}\right)
\Phi^{(k-j)}\!\left(\frac{s-d}{2}\right)
\,dd.
\]

Taking absolute values termwise produces a direct majorant. The omitted \(n\ge3\) terms retain their exponential factor \(e^{-y_n}\), so the existing aggregate tail-ratio method applies after multiplication by the finite rational-polynomial factors \(|P_j|\). This avoids unstable bounds on ratios defining \(g^{(j)}\) and supplies exactly the derivative norms needed for the sixth- and eighth-order remainder estimates.

## Disposition

The direct theorem requires only

\[
2\operatorname{Var}_\nu(X_s)
\ge
\mathbb E_\nu\!\left[
\left(2X_s^2-1-X_{2s}\right)_+
\right].
\]

This variance-compensation inequality is strictly weaker than pointwise positivity and preserves the averaging structure of the source-derived density \(H\). It is the highest-value continuation branch; the pointwise hierarchy is frozen as an optional stronger route.
