# Theta cubic adjacent size bias

Status: live bounded successor to `theta-cubic-mean-transport.md`.

## 1. Exact discrete carrier gate

For the tilted source law `Q_t`, write

\[
 R=u^2,qquad W=V'(u)/u,qquad
 C_t=\operatorname{Cov}_{Q_t}(R,W).
\]

Integration by parts gives the universal normalization

\[
 B_t=\mathbb E_{Q_t}(RW)=2t+1.
\]

Hence the inverse separation length is

\[
 L_t=\sqrt{\frac{2t+1}{C_t}},                           \tag{1}
\]

and the exact cubic Jensen gate is

\[
 \boxed{|L_{t+1}-L_t|\le1.}                            \tag{2}
\]

No real-tilt derivative estimate is required.

## 2. Adjacent tilt is one product size bias

Let `mu_t` be the positive separation law

\[
 d\mu_t(u_1,u_2)
 =\frac{(R_1-R_2)(W_1-W_2)}{2C_t}
   dQ_t(u_1)dQ_t(u_2).
\]

Put `p=u_1u_2`, and let

\[
 A_t=\mathbb E_{Q_t}R.
\]

Since `Q_{t+1}` is the `R`-size bias of `Q_t`, direct normalization gives

\[
 \boxed{
 \frac{C_{t+1}}{C_t}
 =\frac{\mathbb E_{\mu_t}(p^2)}{A_t^2}.
 }                                                       \tag{3}
\]

Thus the entire adjacent change in quadratic reserve is the normalized RMS
product scale seen by the oriented separation pair.

Define

\[
 S_t=\frac{\sqrt{\mathbb E_{\mu_t}(p^2)}}{A_t},
 \qquad
 \epsilon_t=\sqrt{\frac{C_t}{2t+1}}=\sqrt{\delta_t}.
                                                        \tag{4}
\]

Then

\[
 \frac{L_{t+1}}{L_t}
 =\sqrt{\frac{2t+3}{2t+1}}\frac1{S_t}.                 \tag{5}
\]

Dividing (2) by `L_t` yields the exact local theorem

\[
 \boxed{
 \left|
 \sqrt{\frac{2t+3}{2t+1}}\frac1{S_t}-1
 \right|\le\epsilon_t.
 }                                                       \tag{6}
\]

Equivalently,

\[
 \boxed{
 \frac{\sqrt{(2t+3)/(2t+1)}}{1+\epsilon_t}
 \le S_t\le
 \frac{\sqrt{(2t+3)/(2t+1)}}{1-\epsilon_t}.
 }                                                       \tag{7}
\]

This is not a sufficient surrogate: it is precisely the cubic gate.

## 3. The product moment also collapses by parts

Let

\[
 A_t^{(2)}=\mathbb E_{Q_t}(R^2).
\]

Expanding the two-copy determinant gives

\[
\begin{aligned}
 \mathbb E_{\mu_t}(p^2)
 &=\frac1{2C_t}
   \mathbb E[(R_1-R_2)(W_1-W_2)R_1R_2]\\
 &=\frac{
 A_t\mathbb E(R^2W)-A_t^{(2)}\mathbb E(RW)}{C_t}.
\end{aligned}                                           \tag{8}
\]

The same score integration by parts gives

\[
 \mathbb E(RW)=2t+1,qquad
 \mathbb E(R^2W)=(2t+3)A_t.
\]

Therefore

\[
 \boxed{
 \mathbb E_{\mu_t}(p^2)
 =\frac{(2t+3)A_t^2-(2t+1)A_t^{(2)}}{C_t}.
 }                                                       \tag{9}
\]

In particular positivity of the separation law forces

\[
 \frac{A_t^{(2)}}{A_t^2}<\frac{2t+3}{2t+1}.            \tag{10}
\]

This is the next quadratic moment gate in its unnormalized source form.

## 4. Hard-to-vary explanation target

Equation (6) says:

\[
 \boxed{
 \text{the separation pair's RMS product scale must track the universal
 carrier dilation within the existing separation reserve.}
 }                                                       \tag{11}
\]

The three quantities are all source-derived:

- `sqrt((2t+3)/(2t+1))` is the exact carrier dilation;
- `S_t` is the response of the positive two-copy separation law to the
  canonical adjacent `p^2` size bias;
- `epsilon_t` is the already-proved quadratic reserve.

The next analytic attack should therefore avoid whole-CDF comparison unless
needed.  It should bound the single determinant moment (9) tightly enough to
place `S_t` in the interval (7).  Modular label pairing enters only through
`A_t`, `A_t^(2)`, and `C_t`; the carrier coefficients are exact.

The sharp falsifier is likewise local: one integer tilt for which the product
scale in (9) leaves the interval (7).  A failure would falsify cubic Jensen
hyperbolicity at that order, not merely this presentation.

## 5. The next reserve is an exact radial-variance deficit

Write

\[
 \operatorname{cv}_t^2(R)
 =\frac{\operatorname{Var}_{Q_t}(R)}{A_t^2}
 =\frac{A_t^{(2)}}{A_t^2}-1.                            \tag{12}
\]

Equation (9) becomes

\[
 \frac{\mathbb E_{\mu_t}(p^2)}{A_t^2}
 =\frac{2-(2t+1)\operatorname{cv}_t^2(R)}{C_t}.         \tag{13}
\]

Combining this with the exact adjacent transport (3) gives the unexpected
Stein recursion

\[
 \boxed{
 C_{t+1}=2-(2t+1)\operatorname{cv}_t^2(R).
 }                                                       \tag{14}
\]

It may also be checked directly from the two score integrations by parts,
but the separation-law derivation explains its meaning.  The next oriented
score covariance is exactly the amount by which the radial relative variance
falls below the universal ceiling

\[
 \operatorname{cv}_t^2(R)<\frac2{2t+1}.                \tag{15}
\]

Thus the proved quadratic theorem at tilt `t+1` is equivalent to this sharp
radial concentration inequality at tilt `t`.

The exact cubic gate now has the one-law form

\[
 \boxed{
 \left|
 \sqrt{
 \frac{2t+3}
 {2-(2t+1)\operatorname{cv}_t^2(R)}}
 -\sqrt{\frac{2t+1}{C_t}}
 \right|\le1.
 }                                                       \tag{16}
\]

This exposes the first coupled positivity theorem in familiar terms:

\[
 \boxed{
 \text{score stiffening reserve at }t
 \quad\leftrightarrow\quad
 \text{radial concentration reserve at }t.
 }                                                       \tag{17}
\]

Neither reserve alone suffices.  Cubic hyperbolicity asserts that their
inverse square-root coercivity lengths differ by at most one.

## 6. Revised analytic attack

The source-specific target is now an adjacent refinement of a variance
bound, not a generic total-positivity claim.  The useful order is:

1. derive the best one-dimensional Brascamp--Lieb or Stein bound for
   `Var_Qt(R)` from the exact potential
   `V(u)-2t log(u)`;
2. retain its deficit from the ceiling `2/(2t+1)`, rather than discarding the
   remainder after proving positivity;
3. compare that retained deficit with `C_t=Cov(R,W)` through (16);
4. demand the exact unit interval, not merely positivity of both sides.

This use of Brascamp--Lieb is now typed correctly.  Earlier it was asked to
control irrelevant variance of a three-copy logarithmic observable.  Here
the variance is itself exactly the next quadratic reserve, by (14).

## 7. Typed Brascamp--Lieb entry point

The tilted law has potential

\[
 \mathcal V_t(u)=V(u)-2t\log u,
 \qquad
 \mathcal V_t''(u)=V''(u)+\frac{2t}{u^2}.               \tag{18}
\]

Whenever this curvature is positive, the one-dimensional Brascamp--Lieb
inequality applied to `R=u^2` gives

\[
 \operatorname{Var}_{Q_t}(R)
 \le
 \mathbb E_{Q_t}
 \left[
 \frac{4u^2}{V''(u)+2t/u^2}
 \right]
 =
 \mathbb E_{Q_t}
 \left[
 \frac{4R^2}{2t+RW+uQ(u)}
 \right],                                               \tag{19}
\]

where

\[
 Q(u)=uV''(u)-V'(u)>0                                  \tag{20}
\]

is exactly the source-stiffening quantity proved in the degree-two packet.
Thus the already-proved theorem enters the cubic problem as a positive term
in the denominator of the correct radial variance bound.

The exact cubic interval for the next reserve is obtained directly from
`|L_(t+1)-L_t|<=1`:

\[
 \boxed{
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}+1)^2}
 \le C_{t+1}\le
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}-1)^2}.
 }                                                       \tag{21}
\]

Using (14), (21) is a two-sided target for the retained Brascamp deficit.
The lower bound on `C_(t+1)` requires an upper variance estimate and is the
natural role of (19).  The upper bound requires a lower variance estimate;
it cannot come from Brascamp--Lieb and must instead arise from a source
comparison or the exact product transport.

This typing prevents a one-sided concentration theorem from being mistaken
for the whole cubic gate.  The immediate hostile test is analytic: determine
whether the right side of (19), with the proved lower bounds on `Q(u)`, is
already small enough to imply the lower inequality in (21).  Only if that
reserve fits should the Brascamp branch be pursued further.

## 8. The dual lower-variance channel

The tilted score is explicit:

\[
 \sigma_t(u)=\partial_u\log q_t(u)
 =\frac{2t}{u}-V'(u)
 =\frac{2t-RW}{u}.                                     \tag{22}
\]

For integer cubic tilts `t>=1`, the endpoint terms vanish and
`E_Qt(sigma_t)=0`.  Integration by parts with `R=u^2` gives

\[
 \mathbb E_{Q_t}(R\sigma_t)=-2\mathbb E_{Q_t}u.         \tag{23}
\]

Cauchy--Schwarz therefore yields the exact Cramer--Rao lower bound

\[
 \boxed{
 \operatorname{Var}_{Q_t}(R)
 \ge
 \frac{4(\mathbb E_{Q_t}u)^2}{\mathcal F_t},
 \qquad
 \mathcal F_t=\mathbb E_{Q_t}\sigma_t^2.
 }                                                       \tag{24}
\]

Together, (19) and (24) form a two-sided source corridor

\[
 \frac{4(\mathbb E u)^2}{\mathcal F_t}
 \le \operatorname{Var}(R)
 \le
 \mathbb E
 \left[\frac{4R^2}{2t+RW+uQ(u)}\right].                \tag{25}
\]

Transporting it through the exact recursion (14) reverses the order:

\[
\boxed{
 2-\frac{2t+1}{A_t^2}
 \mathbb E\left[\frac{4R^2}{2t+RW+uQ(u)}\right]
 \le C_{t+1}
 \le
 2-\frac{2t+1}{A_t^2}
 \frac{4(\mathbb E u)^2}{\mathcal F_t}.
}                                                       \tag{26}
\]

This supplies both orientations required by the cubic interval (21):

- the proved positive curvature `Q(u)` strengthens the lower endpoint through
  Brascamp--Lieb;
- the tilted Fisher information controls the upper endpoint through
  Cramer--Rao.

The next hostile test is no longer an open-ended search for “more
positivity.”  Compare the two explicit endpoints in (26) against those in
(21).  If both fit analytically, the cubic gate closes.  If either misses,
the residual gap identifies exactly which source refinement is required.

There is also a sharp equality diagnostic.  Cramer--Rao is exact only when
`R-A_t` is proportional to the score `sigma_t`; Brascamp--Lieb is exact only
for the corresponding affine mode in a quadratic effective potential.  The
theta source is not exactly in that carrier class, so any successful proof
must retain quantitative curvature corrections rather than invoke equality
heuristics.

## 9. One curvature field governs both walls

Fisher integration by parts gives

\[
 \mathcal F_t
 =\mathbb E_{Q_t}\bigl[-\sigma_t'(u)\bigr]
 =\mathbb E_{Q_t}
 \left[V''(u)+\frac{2t}{u^2}\right].                   \tag{27}
\]

Define the dimensionless effective-curvature field

\[
 \mathcal K_t(u)
 =u^2\mathcal V_t''(u)
 =2t+RW+uQ(u).                                          \tag{28}
\]

Then the corridor (25) is

\[
 \boxed{
 \frac{4(\mathbb E\sqrt R)^2}
      {\mathbb E(\mathcal K_t/R)}
 \le \operatorname{Var}(R)
 \le 4\mathbb E\left(\frac{R^2}{\mathcal K_t}\right).
 }                                                       \tag{29}
\]

Thus the two walls are not separate mechanisms.  They are dual averages of
the same positive curvature field:

\[
 \text{Cramer--Rao wall}:\quad
 \mathbb E(\mathcal K_t/R),
 \qquad
 \text{Brascamp wall}:\quad
 \mathbb E(R^2/\mathcal K_t).                           \tag{30}
\]

The proved source inequality \(Q(u)>0\) enters both through the same positive
summand \(uQ(u)\).  The cubic theorem will close through this corridor only if
theta modular geometry controls the dispersion of \(\mathcal K_t\) relative
to \(R\), not merely its pointwise sign.

This is the next precise explanation target:

\[
 \boxed{
 \text{modular completion keeps the effective curvature sufficiently
 homogeneous across the radial tilt to trap the next reserve.}
 }                                                       \tag{31}
\]

A pointwise lower bound on \(\mathcal K_t\) can improve only the Brascamp
wall.  A two-sided oscillation or likelihood-ratio bound for
\(\mathcal K_t/R\) is required to move both walls coherently.  That
distinction determines the next source calculation.

## 10. The corridor slack is a positive two-copy determinant

Put

\[
 X_t=\frac{\mathcal K_t}{R}
 =V''(u)+\frac{2t}{u^2}.                               \tag{32}
\]

Denote the Cramer--Rao and Brascamp variance walls by

\[
 \mathsf L_t=
 \frac{4(\mathbb E\sqrt R)^2}{\mathbb E X_t},
 \qquad
 \mathsf U_t=4\mathbb E\left(\frac R{X_t}\right).
                                                               \tag{33}
\]

Their ratio is

\[
 \boxed{
 \Gamma_t:=\frac{\mathsf U_t}{\mathsf L_t}
 =\frac{\mathbb E(R/X_t)\,\mathbb E X_t}
        {(\mathbb E\sqrt R)^2}\ge1.
 }                                                       \tag{34}
\]

The excess is exactly

\[
\begin{aligned}
 &\mathbb E(R/X_t)\,\mathbb E X_t-(\mathbb E\sqrt R)^2\\
 &\qquad=
 \frac12\mathbb E\left[
 \left(
 \sqrt{\frac{R_1}{X_1}}\sqrt{X_2}
 -
 \sqrt{\frac{R_2}{X_2}}\sqrt{X_1}
 \right)^2
 \right].
\end{aligned}                                           \tag{35}
\]

Thus \(\Gamma_t-1\) is a canonical positive two-copy measure of effective
curvature heterogeneity.  Equality holds precisely when

\[
 \frac{X_t}{\sqrt R}
 =\frac{\mathcal K_t}{R^{3/2}}
\]

is constant on the source support.  The relevant notion of homogeneity is
therefore not constancy of \(\mathcal K_t\), but constancy of its
scale-normalized field \(\mathcal K_t/R^{3/2}\).

This supplies a hard falsifier for the corridor strategy.  Let

\[
 c_t^-=
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}+1)^2},
 \qquad
 c_t^+=
 \frac{2t+3}{(\sqrt{(2t+1)/C_t}-1)^2}.                 \tag{36}
\]

The two functional inequalities prove the cubic gate only if

\[
 \boxed{
 \mathsf U_t\le
 \frac{A_t^2}{2t+1}(2-c_t^-),
 \qquad
 \mathsf L_t\ge
 \frac{A_t^2}{2t+1}(2-c_t^+).
 }                                                       \tag{37}
\]

If (37) fails while the exact variance still lies in its required interval,
the failure belongs to the corridor slack \(\Gamma_t-1\), not to cubic
hyperbolicity.  The next source calculation should therefore bound
\(\Gamma_t\) before attempting elaborate estimates of the individual walls.
That bound is again a two-copy orientation problem, but now its positive
integrand and normalization are explicit.
