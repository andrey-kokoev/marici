# Theta H local Bochner moments

Author: `marici.Grothendieck`
Status: fourth-derivative gate reduced to theta log-curvature moments
Predecessor: `theta-nonlocal-convolution-kernel-test.md`

## Question

Does the theta source prove the local fourth-derivative condition required by the equally spaced three-point Bochner determinant for the derived density \(H\)?

## Exact reduction

Write \(g=\log\Phi\). After the substitution \(d=2x\),

\[
H(s)=2\int_{\mathbb R}x^2
\Phi\!\left(x+\frac s2\right)
\Phi\!\left(x-\frac s2\right)dx.
\]

Taylor expansion of the logarithm at fixed \(x\) gives

\[
g\!\left(x+\frac s2\right)
+g\!\left(x-\frac s2\right)
=2g(x)+\frac{s^2}{4}g''(x)
+\frac{s^4}{192}g^{(4)}(x)+O(s^6).
\]

Consequently,

\[
\begin{aligned}
H(0)&=2I,\\
H''(0)&=I\,\mathbb E_\mu[g''],\\
H^{(4)}(0)&=I\,\mathbb E_\mu\!\left[
\frac14g^{(4)}+\frac32(g'')^2
\right],
\end{aligned}
\]

where

\[
I=\int_{\mathbb R}x^2\Phi(x)^2dx,
\qquad
d\mu=I^{-1}x^2\Phi(x)^2dx.
\]

Thus the local three-point condition

\[
H(0)H^{(4)}(0)\ge H''(0)^2
\]

is exactly

\[
\frac12\mathbb E_\mu[g^{(4)}]
+3\mathbb E_\mu[(g'')^2]
\ge
\mathbb E_\mu[g'']^2.
\]

Strict log-concavity supplies \(g''<0\), but no sign for \(g^{(4)}\). Cauchy--Schwarz controls the square term and reduces a sufficient condition to

\[
\mathbb E_\mu[g^{(4)}]
+4\mathbb E_\mu[g'']^2\ge0.
\]

## Integration-by-parts audit

Let \(h=g''\) and \(w=x^2e^{2g}\). Two integrations by parts, with theta decay removing the boundary terms, give

\[
\int w g^{(4)}dx
=
\int e^{2g}
\left(
2h+8xg'h+2x^2h^2+4x^2(g')^2h
\right)dx.
\]

The identity contains two sign-controlled positive terms,

\[
8xg'h\ge0,
\qquad
2x^2h^2\ge0,
\]

because \(xg'\le0\) and \(h<0\). It also contains the negative terms

\[
2h<0,
\qquad
4x^2(g')^2h<0.
\]

Thus integration by parts does not turn the fourth-derivative expectation into a sum of squares. The exact remaining task is a weighted domination of these two negative contributions by the positive curvature terms; strict log-concavity alone supplies signs but not that domination.

## Positive-mixture curvature audit

For the positive theta mixture \(\Phi=\sum_nT_n\), write

\[
\ell_n=(\log T_n)',\quad
c_n=(\log T_n)'',\quad
d_n=(\log T_n)''',\quad
e_n=(\log T_n)^{(4)}.
\]

Differentiating the log-sum-exp identity through fourth order gives

\[
g^{(4)}=
\mathbb E[e]
+4\operatorname{Cov}(\ell,d)
+3\operatorname{Var}(c)
+6\kappa(\ell,\ell,c)
+\kappa_4(\ell),
\]

where

\[
\kappa(\ell,\ell,c)
=\mathbb E[(\ell-\mathbb E\ell)^2(c-\mathbb Ec)]

after the standard cumulant centering, and

\[
\kappa_4(\ell)
=\mathbb E[(\ell-\mathbb E\ell)^4]
-3\operatorname{Var}(\ell)^2.
\]

The PF2 proof bounded only \(\operatorname{Var}(\ell)\) and the negative component curvatures \(c_n\). It supplies no sign or magnitude control for \(\mathbb E[e]\), \(\operatorname{Cov}(\ell,d)\), the mixed third cumulant, or the fourth cumulant. Therefore its tail majorant cannot be reused to prove the local Bochner inequality without a new fourth-order estimate.

## Fourth-cumulant majorant test

For any center \(a\),

\[
\mathbb E|\ell-\mathbb E\ell|^4
\le16\mathbb E|\ell-a|^4.
\]

Taking \(a=\ell_1\) and reusing the PF2 tail bounds yields

\[
\mathbb E|\ell-\mathbb E\ell|^4
\le
\sum_{n\ge2}
32n^4(mx+4)^4e^{-mx/2},
\qquad m=n^2-1.
\]

Together with \(\operatorname{Var}(\ell)<2\), this gives

\[
|\kappa_4(\ell)|
\le
\sum_{n\ge2}
32n^4(mx+4)^4e^{-mx/2}+12.
\]

Unlike the quadratic PF2 sum, this fourth-order sum is not small at the worst endpoint \(x=6\). Its \(n=2\) term alone is

\[
7{,}496{,}192e^{-9}>900.
\]

Thus the direct absolute-value extension of the PF2 majorant loses more than two orders of magnitude and cannot prove the required curvature domination. A viable fourth-order proof must preserve cancellations among \(\mathbb E[e]\), covariance, mixed-cumulant, and fourth-cumulant terms rather than bound them separately.

## Two-component cancellation test

For the dominant truncation \(\Phi_2=T_1+T_2\), set

\[
p=\frac{T_2}{T_1+T_2},
\qquad q=1-p,
\qquad \Delta=\log T_2-\log T_1.
\]

Then \(g_2=\log\Phi_2=\log T_1+\log(1+e^\Delta)\), and exact differentiation gives

\[
\begin{aligned}
g_2^{(4)}={}&e_1+p\Delta^{(4)}
+4pq\Delta'\Delta'''
+3pq(\Delta'')^2\\
&+6pq(1-2p)(\Delta')^2\Delta''
+pq(1-6pq)(\Delta')^4.
\end{aligned}
\]

At the worst PF2 endpoint, \(T_2/T_1=28e^{-9}<1/200\), so \(pq<1/200\) and

\[
1-6pq>\frac{97}{100}.
\]

The large fourth-power contribution that destroyed the absolute cumulant majorant therefore enters the grouped two-component formula with a positive coefficient. It is not itself an obstruction; the unresolved terms are the signed derivative couplings \(\Delta'\Delta'''\) and \((\Delta')^2\Delta''\), together with the component fourth derivative.

The correct next estimate must bound this grouped expression, not the cumulants separately.

## Two-component grouped-sign test

For \(n=2\),

\[
\Delta(x)=
\log\!\left(4\frac{4x-3}{x-3}\right)-\frac{3x}{2},
\qquad D=2x\frac d{dx}.
\]

Hence

\[
\Delta'=-3x+\frac{8x}{4x-3}-\frac{2x}{x-3},
\]

\[
\Delta''=-6x-rac{48x}{(4x-3)^2}
+rac{12x}{(x-3)^2}.
\]

For \(x\ge6\), \(\Delta'<0\), \(\Delta''<0\), and direct differentiation gives \(\Delta'''<0\). Therefore

\[
4pq\Delta'\Delta'''>0,
\qquad 3pq(\Delta'')^2>0.
\]

The last two interaction terms combine as

\[
pq(\Delta')^2
\left((1-6pq)(\Delta')^2
+6(1-2p)\Delta''\right).
\]

Using \(pq<1/200\), \(|\Delta'|>3x-3/10\), and \(|\Delta''|<6x+1\), the bracket is positive at \(x=6\) and increasing thereafter. Thus every interaction term in the two-component fourth derivative is positive. The only unresolved contribution is the weighted component block

\[
(1-p)e_1+pe_2.
\]

## Component fourth-derivative test

For a single theta component, put \(y=n^2x\). Its logarithmic curvature is

\[
c_n=-2y-\frac{12y}{(y-3)^2}.
\]

Applying \(D=2y\,d/dy\) twice gives the exact fourth derivative

\[
e_n=D^2c_n
=-8y-
\frac{48y(y^2+12y+9)}{(y-3)^4}<0
\qquad(y\ge6).
\]

Thus the weighted component block in the grouped mixture formula is strictly negative. The positive interaction terms do not prove \(g^{(4)}\ge0\), nor is that sign required by the local Bochner condition. The actual target remains

\[
\frac12\mathbb E_\mu[g^{(4)}]
+3\mathbb E_\mu[(g'')^2]
\ge \mathbb E_\mu[g'']^2.
\] The curvature-square margin can absorb a negative component fourth derivative; testing that grouped margin is the next nonredundant gate.

## Single-component local margin

Although \(e_n<0\), every component satisfies the stronger pointwise margin

\[
e_n+4c_n^2>0
\qquad(y=n^2x\ge6).
\]

Indeed, \(|c_n|>2y\), so \(4c_n^2>16y^2\). The required comparison \(|e_n|<16y^2\) is equivalent to

\[
1+6\frac{y^2+12y+9}{(y-3)^4}<2y.
\]

At \(y=6\), the left side is \(29/3<12\); its rational term decreases for \(y\ge6\), while the right side increases. Hence the inequality holds on the complete theta range.

Thus a single positive theta component passes the sufficient local Bochner margin. Any failure must be created by mixture perturbations, despite the positivity of their fourth-order interaction block.

## Two-component margin perturbation

Let

\[
C=(1-p)c_1+pc_2,
\qquad V=pq(\Delta')^2,
\qquad g_2''=C+V.
\]

Combining the exact fourth derivative with the identity

\[
(1-p)c_1^2+pc_2^2=C^2+pq(\Delta'')^2
\]

gives

\[
\begin{aligned}
g_2^{(4)}+4(g_2'')^2
={}&(1-p)(e_1+4c_1^2)+p(e_2+4c_2^2)\\
&+pq\,Q(x,p)+4V^2,
\end{aligned}
\]

where

\[
\begin{aligned}
Q={}&4\Delta'\Delta'''-(\Delta'')^2\\
&+\left(6(1-2p)\Delta''+8C\right)(\Delta')^2\\
&+(1-6pq)(\Delta')^4.
\end{aligned}
\]

The first line is positive by the single-component theorem, and \(4V^2\ge0\). Thus the complete two-component sufficient margin reduces to the explicit rational-exponential inequality

\[
Q(x,p(x))\ge0,
\qquad
p(x)=\frac{R_2(x)}{1+R_2(x)},
\qquad x\ge6.
\]

This retains every cancellation lost by the cumulant majorant and isolates one scalar sign test.

## Endpoint and asymptotic test for \(Q\)

At \(x=6\), the exact derivative data are

\[
\Delta'=-\frac{138}{7},
\qquad
\Delta''=-\frac{1404}{49},
\qquad
\Delta'''=-\frac{40584}{343},
\]

and

\[
p=\frac{28e^{-9}}{1+28e^{-9}}<\frac1{200}.
\]

Substitution into the residual, using \(e^9>8000\), gives the strict endpoint margin

\[
Q(6,p(6))>2.5\times10^4.
\]

For large \(x\),

\[
\Delta'=-3x+O(x^{-1}),
\quad
\Delta''=-6x+O(x^{-1}),
\quad
\Delta'''=-12x+O(x^{-1}),
\quad
C=-2x+O(1),
\]

while \(p=O(e^{-3x/2})\). Hence

\[
Q(x,p(x))=81x^4-468x^3+O(x^2),
\]

which is positive for all sufficiently large \(x\).

The two-component residual therefore passes the worst endpoint and the asymptotic tail. A bounded intermediate interval remains; closing it requires an exact monotonicity or polynomial-majorant argument rather than a new conceptual premise.

## Disposition

The fourth-derivative Bochner gate is not a consequence of strict log-concavity alone. It has been reduced to one explicit weighted theta log-curvature inequality. Establishing or refuting that inequality is the next source-level test; no zero data enter it.
