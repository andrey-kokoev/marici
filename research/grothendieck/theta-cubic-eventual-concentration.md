# Theta cubic eventual concentration

Status: live bounded successor to theta-cubic-curvature-slack.md.

## 1. Setting

For the midpoint law, put

\[
 b=2t+1,\qquad
 \Psi_t(u)=b\log u-V(u).
\]

Above the explicit saddle threshold established in the preceding packet,
there is a unique \(u_t>1/2\) satisfying

\[
 \Psi_t'(u_t)=0,\qquad u_tV'(u_t)=b.                    \tag{1}
\]

On the entire far chamber,

\[
 V''(u)>0.
\]

## 2. A universal quadratic barrier

The negative Hessian of the log density is

\[
 -\Psi_t''(u)=\frac b{u^2}+V''(u)>\frac b{u^2}.         \tag{2}
\]

For \(1/2\le u\le2u_t\), every point between \(u\) and \(u_t\) is at most
\(2u_t\).  Taylor's integral formula therefore gives

\[
 \boxed{
 \Psi_t(u_t)-\Psi_t(u)
 \ge\frac{b}{8u_t^2}(u-u_t)^2
 \qquad(1/2\le u\le2u_t).
 }                                                       \tag{3}
\]

This bound uses only positivity of the completed-source curvature.  It does
not discard arithmetic labels or replace the source.

Although weaker than the formal saddle curvature \(4t/u_t\), it already
gives the scale

\[
 \frac{u_t^2}{b}
 =O\left(\frac{(\log t)^2}{t}\right),                   \tag{4}
\]

which tends to zero and is sufficient in principle for an eventual theorem.

## 3. The right tail is exponentially subordinate

Integrating (2) from \(u_t\) to \(2u_t\) gives

\[
 \Psi_t'(2u_t)
 \le-\int_{u_t}^{2u_t}\frac b{s^2}\,ds
 =-\frac b{2u_t}.                                      \tag{5}
\]

Since \(\Psi_t'\) is strictly decreasing on the far chamber,

\[
 \boxed{
 \Psi_t(u)
 \le\Psi_t(u_t)-\frac b8
 -\frac b{2u_t}(u-2u_t)
 \quad(u\ge2u_t).
 }                                                       \tag{6}
\]

Thus the entire far-right tail lies below the saddle by an initial
\(e^{-b/8}\) factor followed by an explicit exponential slope.
The true theta tail is superexponential, but that additional strength is not
needed for basic mass concentration.

## 4. The bounded chamber is also separated

At the seam endpoint, (3) gives

\[
 \Psi_t(u_t)-\Psi_t(1/2)
 \ge\frac b{8u_t^2}(u_t-1/2)^2.                        \tag{7}
\]

For large \(t\), the right side is asymptotic to \(b/8\).  The remaining
interval \(0<u<1/2\) is compact in the source factor and has the explicit
power suppression \(u^b\).  A rigorous bound can therefore be obtained from

\[
 \int_0^{1/2}u^b\Phi(u)\,du
 \le
 \frac{\sup_{[0,1/2]}\Phi}{b+1}\,2^{-(b+1)}.            \tag{8}
\]

To turn (8) into a probability estimate, one still needs a lower bound on
the normalization near \(u_t\).  That is the sole role of the forthcoming
upper-curvature envelope.

## 5. Exact second-derivative envelope

For \(x=\pi e^{2u}\), mixture differentiation gives

\[
 V''=\sum_nw_nV_n''-\operatorname{Var}_w(V_n').
                                                               \tag{9}
\]

Using

\[
 \frac{\phi_n}{\phi_1}\le2n^4e^{-(n^2-1)x},
\qquad
 |V_n'-V_1'|\le3n^2x,
\]

and the elementary far-chamber bound
\[
 |V_n''-V_1''|\le5n^2x,
\]

one obtains

\[
 \boxed{
 |V''(u)-V_1''(u)|
 \le
 10x\sum_{n\ge2}n^6e^{-(n^2-1)x}
 +18x^2\sum_{n\ge2}n^8e^{-(n^2-1)x}
 =:\mathcal E_2(x).
 }                                                       \tag{10}
\]

Here

\[
 V_1''(u)=4x+\frac{24x}{(2x-3)^2}.                     \tag{11}
\]

Equations (10)--(11), together with the saddle envelope for \(x_t\), provide
an explicit upper bound on \(-\Psi_t''\) in a small saddle window.  Integrating
that upper bound yields the missing normalization lower bound.

## 6. Remaining eventual-theorem lemma

Choose a window

\[
 |u-u_t|\le
 \rho_t,\qquad
 \rho_t=c\sqrt{\frac{u_t}{t}},
\]

with a fixed rational \(c>0\).  The next lemma must prove, from (10) and the
first-derivative saddle envelope,

\[
 \Psi_t(u_t)-\Psi_t(u)\le Cc^2
 \quad\text{on the window},                             \tag{12}
\]

for an absolute rational \(C\).  It would imply

\[
 \int e^{\Psi_t(u)}du
 \ge2\rho_te^{\Psi_t(u_t)-Cc^2}.                        \tag{13}
\]

Combined with (3), (6), and (8), this gives normalized central and endpoint
mass bounds.  The same decomposition can then be applied simultaneously to
\(Y_t\) and \(Y_t^{-1}\), preserving their midpoint product.

The hard frontier has therefore narrowed to one local upper-curvature lemma;
global saddle uniqueness and both tail barriers are already analytic.

## 7. The local normalization lemma closes

The explicit series in (10) admits the coarse far-chamber estimate

\[
 \mathcal E_2(x)\le\frac{x}{100}\qquad(x\ge8).           \tag{14}
\]

Indeed, for \(n\ge2\),

\[
 n^2-1\ge3(n-1),\qquad n\le2^{n-1}.
\]

Using \(e>2\) and the fact that \(xe^{-(n^2-1)x}\) decreases for \(x\ge8\)
gives

\[
 \sum_{n\ge2}n^6e^{-(n^2-1)x}
 \le\sum_{m\ge1}2^{-18m}
 =\frac1{2^{18}-1},
\]

and

\[
 x\sum_{n\ge2}n^8e^{-(n^2-1)x}
 \le8\sum_{m\ge1}2^{-16m}
 =\frac8{2^{16}-1}.
\]

Consequently

\[
 \frac{\mathcal E_2(x)}x
 \le\frac{10}{2^{18}-1}
 +\frac{144}{2^{16}-1}
 <\frac1{100},
\]

which proves (14) without decimal input.

Also, directly from (11),

\[
 V_1''(u)\le5x\qquad(x\ge8),
\]

so

\[
 \boxed{V''(u)\le6x\qquad(u\ge1/2).}                    \tag{15}
\]

The same estimates give
\(\mathcal E_1(x)<1\) for \(x\ge8\), while
\(4x/(2x-3)<5/2\).  The first-derivative saddle envelope therefore gives the
coarse implication

\[
 2x_t\le\frac b{u_t}+6.                                \tag{16}
\]

Assume the explicit eventual conditions

\[
 b\ge6u_t,\qquad
 \rho_t=c\sqrt{\frac{u_t}{t}}
 \le\min\left\{\frac14,\frac{u_t}{2}\right\}.           \tag{17}
\]

Then (16) gives \(x_t\le b/u_t\).  On the window
\(|u-u_t|\le\rho_t\),

\[
 x=x_te^{2(u-u_t)}
 \le e^{1/2}x_t<2x_t\le\frac{2b}{u_t}.                 \tag{18}
\]

Equations (15), (17), and \(u_t\ge1/2\) now yield

\[
\begin{aligned}
 -\Psi_t''(u)
 &=\frac b{u^2}+V''(u)\\
 &\le\frac{4b}{u_t^2}+\frac{12b}{u_t}
 \le\frac{20b}{u_t}.
\end{aligned}                                           \tag{19}
\]

Taylor's integral formula therefore proves

\[
\begin{aligned}
 \Psi_t(u_t)-\Psi_t(u)
 &\le\frac{10b}{u_t}(u-u_t)^2\\
 &\le10\frac bt c^2
 \le30c^2,
\end{aligned}                                           \tag{20}
\]

because \(b/t=2+1/t\le3\).  Thus (12) holds with the absolute rational
constant \(C=30\), and

\[
 \boxed{
 \int_0^\infty e^{\Psi_t(u)}\,du
 \ge
 2c\sqrt{\frac{u_t}{t}}\,
 e^{\Psi_t(u_t)-30c^2}.
 }                                                       \tag{21}
\]

Finally, the conditions in (17) are genuinely eventual rather than assumed
asymptotics.  The primitive far bound \(V'(u)\ge x=\pi e^{2u}\) gives at the
saddle

\[
 u_te^{2u_t}\le\frac b\pi,                              \tag{22}
\]

so \(u_t=O(\log b)\).  Hence both \(b\ge6u_t\) and
\(\rho_t\le\min\{1/4,u_t/2\}\) hold beyond a finite symbolic threshold.

The midpoint law now has a rigorous normalization lower bound, a quadratic
central barrier, an exponential right-tail barrier, and a power-suppressed
bounded chamber.  What remains for the eventual cubic theorem is to insert
the explicit growth envelopes for \(Y_t^{\pm1}\) into these three regions and
compare the resulting midpoint moments with the exact corridor interval.

## 8. Upgrade to the natural saddle scale

The coarse estimates already proved contain a stronger lower-curvature
statement.  From (10), (11), and (14),

\[
 V''(u)\ge V_1''(u)-\mathcal E_2(x)
 \ge4x-\frac{x}{100}>3x.                               \tag{23}
\]

At the saddle, the first-derivative identity gives

\[
 2x_t-\frac b{u_t}
 =\frac52+\frac{4x_t}{2x_t-3}+\varepsilon_t,
 \qquad |\varepsilon_t|<1.
\]

The right side is positive for \(x_t\ge8\), so

\[
 \boxed{x_t>\frac b{2u_t}.}                             \tag{24}
\]

If \(|u-u_t|\le1/4\), then

\[
 x=x_te^{2(u-u_t)}
 \ge e^{-1/2}x_t>\frac{x_t}{2}
 >\frac b{4u_t}.
\]

Therefore

\[
 \boxed{
 -\Psi_t''(u)
 \ge V''(u)
 >\frac{3b}{4u_t}
 \qquad(|u-u_t|\le1/4).
 }                                                       \tag{25}
\]

Taylor's formula now yields the natural Gaussian barrier

\[
 \boxed{
 \Psi_t(u_t)-\Psi_t(u)
 \ge\frac{3b}{8u_t}(u-u_t)^2
 \qquad(|u-u_t|\le1/4).
 }                                                       \tag{26}
\]

The concentration width is consequently

\[
 \sigma_t=\sqrt{\frac{u_t}{b}},                         \tag{27}
\]

matching the formal saddle calculation.

## 9. Exponential shoulders outside the central window

At \(u_t+1/4\), integration of (25) gives

\[
 \Psi_t'(u_t+1/4)\le-\frac{3b}{16u_t},
\]

and at \(u_t-1/4\),

\[
 \Psi_t'(u_t-1/4)\ge\frac{3b}{16u_t}.                  \tag{28}
\]

Since \(\Psi_t'\) decreases throughout the far chamber, the density beyond
the central window has one-sided exponential shoulders:

\[
 \Psi_t(u)
 \le\Psi_t(u_t+1/4)
 -\frac{3b}{16u_t}(u-u_t-1/4)
 \quad(u\ge u_t+1/4),                                  \tag{29}
\]

and

\[
 \Psi_t(u)
 \le\Psi_t(u_t-1/4)
 -\frac{3b}{16u_t}(u_t-1/4-u)
 \quad(1/2\le u\le u_t-1/4).                           \tag{30}
\]

Moreover, (26) gives the shoulder-entry penalty

\[
 \Psi_t(u_t)-\Psi_t(u_t\pm1/4)
 \ge\frac{3b}{128u_t}.                                 \tag{31}
\]

Because \(u_t=O(\log b)\), this penalty tends to infinity like
\(b/\log b\).  Thus all far-chamber mass outside the fixed central window is
exponentially negligible relative to the saddle.

## 10. Sharpened normalization window

Choose

\[
 \rho_t=c\sqrt{\frac{u_t}{b}}.
\]

Under the same eventual conditions as before,
\(\rho_t\le1/4\), while the upper Hessian bound (19) gives

\[
 \Psi_t(u_t)-\Psi_t(u)
 \le10c^2\qquad(|u-u_t|\le\rho_t).                     \tag{32}
\]

Hence the sharper normalization estimate is

\[
 \boxed{
 \int_0^\infty e^{\Psi_t(u)}\,du
 \ge
 2c\sqrt{\frac{u_t}{b}}\,
 e^{\Psi_t(u_t)-10c^2}.
 }                                                       \tag{33}
\]

We now have concentration at the correct scale.  The next required estimate
is local multiplicative regularity of

\[
 Y_t(u)=\frac{V''(u)}u+\frac{2t}{u^3}
\]

on \(O(\sigma_t)\) windows.  The exact relative form of (10), rather than its
coarse \(x/100\) consequence, should make
\(\log Y_t\) uniformly Lipschitz there.

## 11. Local multiplicative regularity closes without \(V'''\)

Retain the relative form of the second-derivative envelope.  Define

\[
 \eta(x)=
 \frac{6}{(2x-3)^2}
 +\frac{\mathcal E_2(x)}{4x}.                           \tag{34}
\]

Equations (10)--(11) give

\[
 \boxed{
 \left|\frac{V''(u)}{4x}-1\right|\le\eta(x).
 }                                                       \tag{35}
\]

On \(|u-u_t|\le1/4\), set

\[
 \eta_t=\sup_{x\ge x_t/2}\eta(x).
\]

The explicit series shows \(\eta_t\to0\).  Introduce the positive primitive
comparison

\[
 \overline Y_t(u)=\frac{4x}{u}+\frac{2t}{u^3}.          \tag{36}
\]

Since the second summand is unchanged and positive, (35) implies

\[
 \left|\frac{Y_t(u)}{\overline Y_t(u)}-1\right|
 \le\eta_t.                                             \tag{37}
\]

For \(\eta_t\le1/2\),

\[
 |\log Y_t(u)-\log\overline Y_t(u)|\le2\eta_t.          \tag{38}
\]

Write \(h=u-u_t\).  The two summands of (36), relative to their values at the
saddle, change by the factors

\[
 e^{2h}\frac{u_t}{u},
 \qquad
 \left(\frac{u_t}{u}\right)^3.                          \tag{39}
\]

A ratio of positive weighted sums lies between the minimum and maximum of
the component ratios.  For the eventual range \(u_t\ge1\) and
\(|h|\le1/4\),

\[
 \left|\log\frac{u}{u_t}\right|
 \le\frac43|h|.
\]

Consequently

\[
 |\log\overline Y_t(u)-\log\overline Y_t(u_t)|
 \le4|h|.                                               \tag{40}
\]

Combining (38) at \(u\) and \(u_t\) proves

\[
 \boxed{
 |\log Y_t(u)-\log Y_t(u_t)|
 \le4|u-u_t|+4\eta_t
 \qquad(|u-u_t|\le1/4).
 }                                                       \tag{41}
\]

Under the midpoint law, the central fluctuation scale is
\(\sigma_t=\sqrt{u_t/b}\).  Hence (41) identifies the exact small parameter

\[
 \boxed{
 \omega_t=
 4\sqrt{\frac{u_t}{b}}+4\eta_t\longrightarrow0.
 }                                                       \tag{42}
\]

This proves local reciprocal coherence of \(Y_t\) and \(Y_t^{-1}\) without a
third-derivative mixture formula.  The remaining integration step is to show
that the exponentially suppressed shoulders contribute \(o(1)\) to both
reciprocal moments; then

\[
 \Gamma_t=1+O(\omega_t^2)
\]

and the midpoint wall center has the corresponding saddle asymptotic.
