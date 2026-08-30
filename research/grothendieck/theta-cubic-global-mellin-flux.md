# Theta cubic global Mellin flux

Status: live successor packet.

## 1. Bounded question

The predecessor packet reduced the unique hostile cubic interface to the
global moment curvatures

\[
 \eta_t
 =\log\frac{Z_{t+1}Z_{t-1}}{Z_t^2},
 \qquad
 C_t=2t+1-(2t-1)e^{\eta_t}.
\]

This packet asks whether removing the universal Gaussian moment curvature
turns the cubic gate into a one-variable transport theorem for the completed
theta source.

No chamber cut, conditional hazard, or seam term is admitted as primitive.

## 2. Gaussian-relative curvature slack

Put

\[
 g_t=\log\frac{2t+1}{2t-1}
\]

and define

\[
\boxed{
 \varepsilon_t=g_t-\eta_t.
}                                                       \tag{1}
\]

The proved degree-two theorem is exactly

\[
 \varepsilon_t>0.                                     \tag{2}
\]

Indeed, if

\[
 b_t=\frac{Z_t}{\Gamma(t+1/2)},
\]

then

\[
 \varepsilon_t
 =-\bigl(\log b_{t+1}-2\log b_t+\log b_{t-1}\bigr).    \tag{3}
\]

Thus \(\varepsilon_t\) is the strict log-concavity slack of the
Gaussian-normalized theta moments.  It contains only the deviation from the
Gaussian carrier already removed by the normalization.

## 3. Quadratic reserves become a universal response function

Since

\[
 (2t-1)e^{g_t}=2t+1,
\]

the covariance reserve factors as

\[
\boxed{
 C_t=(2t+1)(1-e^{-\varepsilon_t}).
}                                                       \tag{4}
\]

Consequently the normalized inverse reserve is

\[
\boxed{
 L_t=\sqrt{\frac{2t+1}{C_t}}
 =F(\varepsilon_t),
 \qquad
 F(\varepsilon)=\frac1{\sqrt{1-e^{-\varepsilon}}}.
}                                                       \tag{5}
\]

The function \(F\) is universal, positive, and strictly decreasing from
infinity to one.  Every source-dependent quantity has collapsed into the
single scalar \(\varepsilon_t\).

## 4. Exact cubic gate after quotienting the Gaussian carrier

The degree-three condition is therefore

\[
\boxed{
 |F(\varepsilon_{t+1})-F(\varepsilon_t)|\le1.
}                                                       \tag{6}
\]

At the exceptional interface,

\[
 |F(\varepsilon_4)-F(\varepsilon_3)|\le1.              \tag{7}
\]

This proves that the factors \(7\) and \(9\) in the raw gate are not
independent arithmetic structure.  They belong entirely to the Gaussian
moment carrier.  The theta content is the adjacent motion of its relative
slack.

## 5. Relation to global Mellin-curvature flux

Let

\[
 \Omega_3^{\mathrm{glob}}=\eta_3-\eta_4.
\]

Then

\[
\boxed{
 \varepsilon_4-\varepsilon_3
 =\Omega_3^{\mathrm{glob}}+\log\frac{45}{49}.
}                                                       \tag{8}
\]

The constant drift

\[
 \log\frac{45}{49}<0
\]

is the exact change of the Gaussian reference curvature from tilt three to
tilt four.  Hence the raw Mellin flux is not itself the physical comparison:
it must be measured relative to this universal drift.

Define the Gaussian-relative flux

\[
\boxed{
 \Xi_{34}
 :=\varepsilon_4-\varepsilon_3.
}                                                       \tag{9}
\]

The complete hostile gate is now a statement about the displacement of one
positive scalar under one adjacent source tilt.

## 6. Exact admissible interval for the relative flux

Let \(e=\varepsilon_3\) and \(q=F(e)>1\).  Since \(F\) is decreasing, (7)
is equivalent to

\[
 \max(1,q-1)\le F(e+\Xi_{34})\le q+1.                 \tag{10}
\]

The inverse function is

\[
\boxed{
 F^{-1}(y)=-\log(1-y^{-2}),
 \qquad y>1.
}                                                       \tag{11}
\]

Therefore the universally valid lower constraint is

\[
\boxed{
 \Xi_{34}
 \ge
 F^{-1}(q+1)-e.
}                                                       \tag{12}
\]

When \(q>2\), there is also the upper constraint

\[
\boxed{
 \Xi_{34}
 \le
 F^{-1}(q-1)-e.
}                                                       \tag{13}
\]

If \(1<q\le2\), the lower endpoint in (10) is one and the upper constraint
is automatic.  The hostile direction predicted by the predecessor is exactly
\(\Xi_{34}<0\): loss of normalized curvature slack makes \(F\) increase and
can cross the upper response boundary \(q+1\).

## 7. First invariant theorem target

Substituting \(q=F(\varepsilon_3)\), define

\[
\boxed{
 \mathcal B(e)
 =e-F^{-1}(F(e)+1)>0.
}                                                       \tag{14}
\]

Then the unique hostile inequality is

\[
\boxed{
 -\Xi_{34}\le\mathcal B(\varepsilon_3).
}                                                       \tag{15}
\]

Equivalently,

\[
\boxed{
 -\Omega_3^{\mathrm{glob}}-\log\frac{45}{49}
 \le\mathcal B(\varepsilon_3).
}                                                       \tag{16}
\]

This is the Gaussian-quotiented version of the cubic theorem.  Its data are:

1. one already positive degree-two slack \(\varepsilon_3\);
2. its adjacent relative flux \(\Xi_{34}\);
3. one universal nonlinear budget \(\mathcal B\).

The sharp falsifier is

\[
 -\Xi_{34}>\mathcal B(\varepsilon_3).
\]

No cut-coordinate positivity statement can substitute for this inequality.

## 8. Immediate research consequence

The source theorem should not try to prove monotonicity of raw moment
curvature.  It should prove a modulus of continuity for the strict
log-concavity slack of the Gaussian-normalized moment sequence:

\[
\boxed{
 \varepsilon_t>0
 \quad\Longrightarrow\quad
 |F(\varepsilon_{t+1})-F(\varepsilon_t)|\le1.
}                                                       \tag{17}
\]

At all sufficiently large tilts this already follows from the saddle theorem
in the programme.  The only live bounded instance is \(t=3\).  A successful
explanation must derive (15) directly from the completed theta source; a
generic positive or log-concave source need not satisfy it.

## 9. Continuous Gaussian-relative curvature density

Extend the moment index continuously:

\[
 Z(\tau)=\int_0^\infty u^{2\tau}\Phi(u)\,du,
 \qquad \tau>-\frac12,
\]

and put

\[
 \mathfrak a(\tau)
 =\log Z(\tau)-\log\Gamma(\tau+1/2).
\]

Under the continuous tilt law \(Q_\tau\), differentiation gives

\[
 \frac{d^2}{d\tau^2}\log Z(\tau)
 =\operatorname{Var}_{Q_\tau}(\log R).                 \tag{18}
\]

Define the Gaussian-relative curvature density

\[
\boxed{
 \kappa(\tau)
 =-\mathfrak a''(\tau)
 =\psi_1(\tau+1/2)
  -\operatorname{Var}_{Q_\tau}(\log R),
}                                                       \tag{19}
\]

where \(\psi_1\) is the trigamma function.  Thus \(\kappa\) measures the
deficit of theta log-scale variance relative to the Gaussian moment carrier.

The discrete slack is its exact triangular average:

\[
\boxed{
 \varepsilon_t
 =\int_{-1}^{1}(1-|s|)\kappa(t+s)\,ds.
}                                                       \tag{20}
\]

No pointwise sign of \(\kappa\) is asserted here.  The proved degree-two
theorem establishes positivity of the triangular averages at the integer
tilts required by the Jensen problem.

The adjacent relative flux is therefore

\[
\boxed{
 \Xi_{34}
 =\int_{-1}^{1}(1-|s|)
  \bigl(\kappa(4+s)-\kappa(3+s)\bigr)\,ds.
}                                                       \tag{21}
\]

The exact cubic target (15) now says:

\[
\boxed{
 \int_{-1}^{1}(1-|s|)
  \bigl(\kappa(3+s)-\kappa(4+s)\bigr)\,ds
 \le
 \mathcal B\!\left(
  \int_{-1}^{1}(1-|s|)\kappa(3+s)\,ds
 \right).
}                                                       \tag{22}
\]

This is the first source-level, cut-free formulation of the exceptional
cubic theorem.  It compares two adjacent observations of one variance-deficit
field.  The Gaussian carrier supplies both the reference variance and the
universal nonlinear response budget; theta arithmetic must control only the
translation loss of \(\kappa\).

## 10. Hard-to-vary explanation and next falsifier

The candidate explanation is now:

> Gaussian normalization exposes the completed theta source as a strict
> log-scale variance deficit.  Cubic hyperbolicity holds because one unit of
> Mellin transport cannot remove that deficit faster than the universal
> inverse-reserve response permits.

The weakest useful next conjecture is not pointwise monotonicity of
\(\kappa\).  It is precisely the triangular transport inequality (22).
Pointwise monotonicity may fail while the weighted theorem survives.

A local falsifier is correspondingly exact: exhibit a subinterval of
\([2,5]\) whose negative translated curvature mass already exceeds
\(\mathcal B(\varepsilon_3)\), even after the maximum possible positive mass
on the complementary intervals is retained.  Such a certificate would kill
the transport explanation without requiring numerical evaluation of any
Riemann zero.

## 11. The universal three-halves speed law

The nonlinear budget has an elementary closed form.  Put

\[
 p=\sqrt{1-e^{-e}}=\frac1{F(e)}\in(0,1).
\]

Using (11) and (14),

\[
\boxed{
 \mathcal B(e)
 =\log\frac{1+2p}{(1-p)(1+p)^3}.
}                                                       \tag{23}
\]

Expansion at the degenerating quadratic boundary \(e\downarrow0\) gives

\[
\boxed{
 \mathcal B(e)=2e^{3/2}+O(e^2).
}                                                       \tag{24}
\]

Therefore positivity of adjacent quadratic reserves is far from sufficient.
When the Gaussian-relative reserve is small, its permitted one-step loss is
only of three-halves order:

\[
\boxed{
 -\Xi_{t,t+1}
 \lesssim2\varepsilon_t^{3/2}.
}                                                       \tag{25}
\]

This explains why the cubic layer is genuinely stronger than degree two.
Degree two proves \(\varepsilon_t>0\); degree three constrains the discrete
velocity of that positive slack increasingly strongly as the slack approaches
zero.  A merely multiplicative estimate

\[
 -\Xi_{t,t+1}=O(\varepsilon_t)
\]

has the wrong scale near degeneracy and cannot close the theorem.

The source-level target (22) must consequently exhibit a square-root gain:
the negative translated mass of \(\kappa\) must be controlled by the
three-halves power of its preceding triangular mass.  This is the precise
analytic signature to seek in the theta curvature certificate.

## 12. Continuous unit-speed sufficient theorem

Define the continuously translated triangular slack

\[
 E(t)=\int_{-1}^{1}(1-|s|)\kappa(t+s)\,ds,
 \qquad E(n)=\varepsilon_n.                            \tag{26}
\]

Differentiating the universal response gives

\[
 |F'(e)|
 =\frac{e^{-e}}{2(1-e^{-e})^{3/2}}.                   \tag{27}
\]

Therefore, assuming first that \(E(t)>0\) throughout \([3,4]\), the
pointwise differential inequality

\[
\boxed{
 |E'(t)|
 \le
 2e^{E(t)}(1-e^{-E(t)})^{3/2}
 \qquad(3\le t\le4)
}                                                       \tag{28}
\]

implies

\[
 \left|\frac d{dt}F(E(t))\right|\le1.                 \tag{29}
\]

Integration over one unit then proves the cubic gate directly:

\[
 |F(\varepsilon_4)-F(\varepsilon_3)|\le1.             \tag{30}
\]

Only the decreasing-slack direction is hostile.  Hence the weaker one-sided
condition

\[
\boxed{
 -E'(t)
 \le
 2e^{E(t)}(1-e^{-E(t)})^{3/2}
}                                                       \tag{31}
\]

is sufficient for the lower-reserve boundary studied here.

The derivative has an exact cumulant interpretation.  If

\[
 \mu_{3,\tau}
 =\mathbb E_{Q_\tau}
  \left[(\log R-\mathbb E_{Q_\tau}\log R)^3\right],
\]

then

\[
 \kappa'(\tau)=\psi_2(\tau+1/2)-\mu_{3,\tau},          \tag{32}
\]

and consequently

\[
\boxed{
 -E'(t)
 =\int_{-1}^{1}(1-|s|)
  \bigl(\mu_{3,t+s}-\psi_2(t+s+1/2)\bigr)\,ds.
}                                                       \tag{33}
\]

The next source theorem can now be stated without moments of unrelated
orders:

> The triangularly averaged excess log-scale skewness of the completed theta
> tilt over its Gaussian carrier is bounded by the nonlinear three-halves
> response of the triangularly averaged variance deficit.

This is a self-concordance-type inequality for the Gaussian-relative Mellin
potential.  It is stronger than log-concavity but exactly matched to the
cubic response, rather than chosen as a generic functional inequality.

Its pointwise version may be false; (31) only needs the triangular averages.
Continuous positivity of \(E\) is an additional obligation; integer
degree-two positivity does not supply it automatically.  The cheapest
analytic attack is therefore to reuse the two-label curvature
certificate to bound the averaged third cumulant and variance deficit on the
single compact tilt interval \([2,5]\), keeping their common source labels
paired throughout.

## 13. Hostile convex-power family

The radial-curvature theorem behind degree two is not sufficient for the
three-halves speed law.  Consider the exact family

\[
 \Phi_p(u)=e^{-u^{2p}},
 \qquad p>1.                                           \tag{34}
\]

Its radial potential is

\[
 \varphi_p(R)=R^p,
\]

which is strictly convex.  Equivalently,

\[
 \frac{V_p'(u)}u=2p\,u^{2p-2}
\]

is strictly increasing.  Thus it satisfies the same strict source-curvature
condition used to prove the quadratic layer.

Its moments are explicit:

\[
\boxed{
 Z_t(p)=\frac1{2p}
 \Gamma\left(\frac{t+1/2}{p}\right).
}                                                       \tag{35}
\]

Put \(q=1/p\) and \(a=t+1/2\).  The raw moment curvature is

\[
 \eta_t(p)
 =\log\Gamma(q(a+1))+log\Gamma(q(a-1))
  -2\log\Gamma(qa).                                   \tag{36}
\]

At the Gaussian endpoint \(p=1\), recurrence of the gamma function gives

\[
 \eta_t(1)=g_t,
 \qquad \varepsilon_t(1)=0.                           \tag{37}
\]

Differentiate (36) with respect to \(q\).  At \(q=1\), the digamma
recurrences yield

\[
\begin{aligned}
 \left.\frac{d\eta_t}{dq}\right|_{q=1}
 &=(a+1)\psi(a+1)+(a-1)\psi(a-1)-2a\psi(a)\\
 &=\frac1a.
\end{aligned}                                          \tag{38}
\]

Since

\[
 q=1-(p-1)+O((p-1)^2),
\]

one obtains the exact first-order asymptotic

\[
\boxed{
 \varepsilon_t(p)
 =\frac{p-1}{t+1/2}+O((p-1)^2).
}                                                       \tag{39}
\]

Using \(F(e)=e^{-1/2}+O(e^{1/2})\) as \(e\downarrow0\),

\[
\boxed{
 F(\varepsilon_t(p))
 =\sqrt{\frac{t+1/2}{p-1}}+O(\sqrt{p-1}).
}                                                       \tag{40}
\]

Therefore

\[
\begin{aligned}
 &F(\varepsilon_4(p))-F(\varepsilon_3(p))\\
 &\quad=
 \frac{\sqrt{9/2}-\sqrt{7/2}}{\sqrt{p-1}}
 +O(\sqrt{p-1})
 \longrightarrow+\infty                              \tag{41}
\end{aligned}
\]

as \(p\downarrow1\).  Hence the cubic gate fails for every sufficiently
small positive \(p-1\), despite strict radial curvature and strict quadratic
positivity.

## 14. Disposition of the generic self-concordance conjecture

The broad conjecture

\[
 \text{strict convexity of }\varphi(R)
 \Longrightarrow
 |F(\varepsilon_{t+1})-F(\varepsilon_t)|\le1
\]

is analytically falsified.  The failure mechanism is precise: near the
Gaussian boundary, the relative slack is only first order in the deformation,

\[
 \varepsilon_t\sim\frac{p-1}{t+1/2},
\]

while the inverse reserve magnifies its tilt dependence by
\((p-1)^{-1/2}\).  Strict positivity supplies no uniform coherence as the
quadratic reserve degenerates.

This leaves a sharper theta-specific obligation.  The completed theta source
must be separated quantitatively from the Gaussian degeneracy, or its
adjacent slacks must share a stronger common leading term that cancels the
singular response.  Modular completion and the discrete label architecture
are now demonstrably necessary; monotone radial stiffening alone cannot
explain the cubic layer.

The next attack should identify which theta invariant forbids the hostile
power-law deformation (34).  Candidate discriminators are:

1. reciprocal modular symmetry of the completed source;
2. the exact two-label logistic transition;
3. the nonperturbative primitive-to-tail separation at the modular seam;
4. an absolute lower bound for \(\varepsilon_3\) paired with a bound for its
   translated loss.

Only a discriminator derived before inspecting the cubic answer is
admissible.

## 15. Analytic even hostile family closes the regularity loophole

For nonintegral \(p\), the convex-power family is not analytic at the origin.
That regularity defect is not responsible for the failure.  Consider instead

\[
\boxed{
 \Phi_\delta(u)=e^{-u^2-\delta u^6},
 \qquad \delta>0.
}                                                       \tag{42}
\]

This source is positive, even, and entire.  Its stiffness is

\[
 \frac{V_\delta'(u)}u=2+6\delta u^4,
\]

which is strictly increasing for \(u>0\).  It therefore satisfies the full
analytic reflection and strict radial-curvature package.

At \(\delta=0\), let \(a=t+1/2\).  Differentiation under the integral gives

\[
 \left.\frac d{d\delta}\log Z_t(\delta)\right|_{\delta=0}
 =-\frac{\Gamma(a+3)}{\Gamma(a)}
 =-(a)_3.                                              \tag{43}
\]

For

\[
 f(a)=(a)_3=a(a+1)(a+2),
\]

the centered second difference is

\[
 f(a+1)+f(a-1)-2f(a)=6(a+1).                          \tag{44}
\]

Consequently

\[
\boxed{
 \varepsilon_t(\delta)
 =6\left(t+\frac32\right)\delta+O(\delta^2).
}                                                       \tag{45}
\]

The inverse reserves satisfy

\[
\boxed{
 F(\varepsilon_t(\delta))
 =\frac1{\sqrt{6(t+3/2)\delta}}+O(\sqrt\delta).
}                                                       \tag{46}
\]

Hence

\[
\begin{aligned}
 &|F(\varepsilon_4(\delta))-F(\varepsilon_3(\delta))|\\
 &\quad=
 \frac1{\sqrt{6\delta}}
 \left|
  \frac1{\sqrt{11/2}}-\frac1{\sqrt{9/2}}
 \right|
 +O(\sqrt\delta)
 \longrightarrow+\infty.                             \tag{47}
\end{aligned}
\]

Thus the cubic gate fails for every sufficiently small \(\delta>0\).

This removes three proposed generic explanations at once:

\[
\boxed{
 \text{even reflection}
 +\text{entire analyticity}
 +\text{strict radial stiffening}
 \not\Longrightarrow
 \text{cubic hyperbolicity}.
}                                                       \tag{48}
\]

The quadratic perturbation \(e^{-u^2-\delta u^4}\) is exceptional: its
first-order normalized slack is independent of \(t\), so the singular leading
response cancels between adjacent tilts.  The sextic perturbation is the first
analytic even deformation whose curvature slack varies at first order, and it
immediately activates the cubic falsifier.

Therefore reciprocal reflection by itself cannot be the missing modular
theorem.  The surviving discriminator must use the theta source's labelled
exponential architecture or another quantitative identity not shared by
generic even entire log-concave sources.

## 16. Tangent-cone classification at the Gaussian boundary

Consider a general analytic radial perturbation

\[
 \Phi_\delta(u)
 =\exp\bigl(-u^2-\delta P(u^2)\bigr),
 \qquad
 P(R)=\sum_{m\ge0}c_mR^m.                              \tag{49}
\]

Assume first that the series and its first variation may be integrated term
by term against the relevant Gaussian tilts.  Let \(a=t+1/2\).  Then

\[
 \left.\frac d{d\delta}\log Z_t(\delta)\right|_0
 =-\mathbb E_{\Gamma(a)}P(R)
 =-\sum_{m\ge0}c_m(a)_m.                              \tag{50}
\]

Therefore

\[
\boxed{
 \varepsilon_t(\delta)
 =\delta d_t(P)+O(\delta^2),
}
                                                               \tag{51}
\]

where

\[
 d_t(P)
 =\sum_{m\ge0}c_m
 \bigl((a+1)_m+(a-1)_m-2(a)_m\bigr).                  \tag{52}
\]

The rising-factorial difference has the exact form

\[
\boxed{
 (a+1)_m+(a-1)_m-2(a)_m
 =m(m-1)(a+1)_{m-2}.
}                                                       \tag{53}
\]

Thus

\[
\boxed{
 d_t(P)=\sum_{m\ge2}c_m m(m-1)(t+3/2)_{m-2}.
}                                                       \tag{54}
\]

Whenever \(d_t(P),d_{t+1}(P)>0\), the adjacent cubic response has leading
term

\[
\boxed{
 |F(\varepsilon_{t+1})-F(\varepsilon_t)|
 =\frac1{\sqrt\delta}
  \left|d_{t+1}(P)^{-1/2}-d_t(P)^{-1/2}\right|
  +O(\sqrt\delta).
}                                                       \tag{55}
\]

Consequently a necessary condition for cubic coherence in every sufficiently
small deformation is

\[
\boxed{
 d_{t+1}(P)=d_t(P).
}                                                       \tag{56}
\]

This is the tangent equation of the cubic cone at the Gaussian boundary.

## 17. The unique positive analytic safe ray

The adjacent change of (54) is

\[
\boxed{
 d_{t+1}(P)-d_t(P)
 =\sum_{m\ge3}c_m m(m-1)(m-2)(t+5/2)_{m-3}.
}                                                       \tag{57}
\]

If \(c_m\ge0\) for every \(m\ge2\), all terms in (57) are nonnegative, and
every term with \(m\ge3\) is strictly positive.  Hence

\[
 d_{t+1}(P)=d_t(P)
 \quad\Longleftrightarrow\quad
 c_m=0\quad(m\ge3).                                   \tag{58}
\]

The affine terms \(c_0+c_1R\) merely renormalize mass and Gaussian scale.
Modulo those neutral directions, the only positive-coefficient analytic
deformation tangent to the cubic cone is

\[
\boxed{
 P(R)=c_2R^2,
 \qquad c_2>0.
}                                                       \tag{59}
\]

Equivalently, the unique nonlinear safe tangent is the quartic source
deformation

\[
 e^{-u^2-\delta c_2u^4}.
\]

Every positive sextic-or-higher radial component changes the adjacent
quadratic slack at first order and is magnified by the singular inverse
reserve into a cubic failure.

This is a local theorem at the Gaussian boundary, not a classification of
all sources satisfying cubic hyperbolicity.  Signed coefficients can satisfy
the single tangent equation by cancellation, and a source far from the
Gaussian boundary need not lie on a perturbative ray.  Nevertheless, it
identifies an unexpectedly rigid geometry:

\[
\boxed{
 \text{the positive analytic tangent cone of cubic coherence is
 one-dimensional after neutral Gaussian directions are quotiented.}
}                                                       \tag{60}
\]

The theta-specific question is now sharper.  Does modular label sewing make
the completed theta source behave, in Gaussian-relative moment curvature, as
an effective quartic deformation even though its pointwise potential is not
quartic?  If so, the coincidence must appear as equality or controlled
near-equality of the adjacent first-variation coordinates \(d_3,d_4\), not as
generic convexity.
