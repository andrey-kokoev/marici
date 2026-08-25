# Theta cubic effective-quartic discriminator

Status: live scope-audit packet.

## 1. The tangent theorem and its limitation

The predecessor proved that, near a Gaussian source and within the cone of
positive-coefficient analytic radial perturbations, the unique nonlinear
direction tangent to cubic coherence is quartic:

\[
 \Phi_\delta(u)=e^{-u^2-\delta c_2u^4}.
\]

This is an exact local classification.  It does not yet imply that the
completed theta source is an effective quartic deformation.

To make that claim one would need a source-derived path

\[
 \lambda\longmapsto\Phi_\lambda,
 \qquad
 \Phi_0=\Phi_{\mathrm{Gaussian}},
 \quad
 \Phi_1=\Phi_{\theta},                                 \tag{1}
\]

together with a canonical Gaussian scale.  Neither datum is presently
supplied by theta geometry.  Geometric interpolation, additive interpolation,
and interpolation of potentials have different tangent coefficients and can
change the apparent quartic component.

Therefore:

\[
\boxed{
 \text{the local quartic tangent is invariant once a deformation is fixed,
 but ``theta is effectively quartic'' is not yet a typed statement.}
}                                                       \tag{2}
\]

## 2. Why the primitive label is not a Gaussian baseline

With

\[
 x=\pi e^{2u},
\]

the completed theta source has labelled ratios

\[
 r_n(x)
 =n^2\frac{2n^2x-3}{2x-3}e^{-(n^2-1)x}.               \tag{3}
\]

The primitive label contains the nonquadratic scale dependence

\[
 (2x-3)e^{-x}
\]

together with a common exponential prefactor in \(u\).  It is neither an
even completed source on its own nor a Gaussian in the moment variable
\(u\).  Declaring it the baseline would break the modular completion before
the comparison begins.

Likewise, the identity

\[
 \Phi=\phi_1(1+r_2+T_3)
\]

is a useful far-chart factorization but not a physical decomposition into a
Gaussian carrier and a perturbing potential.  The logarithm mixes every
label through logistic cumulants.

## 3. Path-independent discriminator

The invariant coordinates require no interpolation:

\[
 \varepsilon_t
 =\log\frac{2t+1}{2t-1}
  -\log\frac{Z_{t+1}Z_{t-1}}{Z_t^2},                  \tag{4}
\]

and

\[
 F(\varepsilon_t)=\frac1{\sqrt{1-e^{-\varepsilon_t}}}. \tag{5}
\]

The exact theta discriminator is therefore

\[
\boxed{
 \mathfrak Q_{34}
 :=1-|F(\varepsilon_4)-F(\varepsilon_3)|.
}                                                       \tag{6}
\]

The cubic interface holds exactly when

\[
 \mathfrak Q_{34}\ge0.                                \tag{7}
\]

No Gaussian path, chamber cut, or label baseline enters this definition.

The tangent theorem remains useful only as a hostile comparison class:

- quartic perturbations have coherent leading normalized slack;
- positive sextic-or-higher perturbations have singularly incoherent slack;
- theta must be tested by \(\mathfrak Q_{34}\), not assigned to either class
  by analogy.

## 4. Exact two-route theorem strategy

There are now only two admissible explanatory routes.

### Route A: direct relative-flux control

Prove

\[
 -\Xi_{34}
 \le\mathcal B(\varepsilon_3),                         \tag{8}
\]

using the completed source throughout.  In continuous form this is the
triangular variance-deficit/skewness comparison from the predecessor.

### Route B: source-derived coherent deformation

Derive, rather than choose, a path (1) from an actual theta operation such as
label activation, modular heat flow, or reciprocal-scale transport.  Then
show that its tangent remains inside the cubic cone.  A fitted interpolation
whose only motivation is satisfying the gate is inadmissible.

Route B has the stronger explanatory payoff but also the sharper authority
gate.  Until such a path exists, Route A is the theorem target.

## 5. A canonical flow candidate and its falsifier

The theta series itself suggests one non-arbitrary deformation: activate
nonprimitive labels by their source weights,

\[
 \Phi_\lambda(u)
 =\phi_1(u)+\sum_{n\ge2}\lambda^{\nu(n)}\phi_n(u),
 \qquad0\le\lambda\le1,                               \tag{9}
\]

where \(\nu(n)\) must be derived from an arithmetic filtration rather than
fitted.  Prime-factor count, label size, and heat time give inequivalent
flows; none is selected yet.

The cheapest falsifier is independence failure: if two equally source-natural
filtrations yield opposite tangent orientations for \(\mathfrak Q_{34}\),
then label activation does not canonically explain cubic coherence.

The undecomposed endpoint theorem could still hold, but the deformation story
would be presentation-dependent.

## 6. Disposition

The effective-quartic coincidence is retained as a mathematically sharp clue,
not promoted to a theta mechanism.  It teaches that cubic coherence has a
one-dimensional positive tangent at Gaussian degeneracy and that generic
higher radial stiffening fails.  It does not select a path from the Gaussian
source to theta.

The immediate research priority is therefore:

\[
\boxed{
 \text{attack the path-independent reserve }\mathfrak Q_{34}
 \text{ directly; admit a deformation explanation only if theta supplies
 the deformation.}
}                                                       \tag{10}
\]

## 7. Canonical heat deformation selects a neutral tangent

There is one deformation derived directly from the fixed transform source:

\[
\boxed{
 \Phi_\lambda(u)=e^{\lambda u^2}\Phi(u),
}                                                       \tag{11}
\]

on the interval of \(\lambda\) for which the moment integrals converge.
Multiplication by the quadratic Fourier-side weight is the source operation
corresponding to heat evolution of the entire transform.  Unlike label
activation, it requires no ordering of arithmetic labels.

Let

\[
 Z_t(\lambda)=\int_0^\infty u^{2t}\Phi_\lambda(u)\,du,
 \qquad
 A_t(\lambda)=\frac{Z_{t+1}(\lambda)}{Z_t(\lambda)}.
\]

Then

\[
 \partial_\lambda\log Z_t=A_t,                        \tag{12}
\]

and the Gaussian-relative curvature responds by

\[
\boxed{
 \partial_\lambda\varepsilon_t
 =-\Theta_t,
 \qquad
 \Theta_t=A_{t+1}-2A_t+A_{t-1}.
}                                                       \tag{13}
\]

Thus the canonical heat tangent is governed by the discrete curvature of the
adjacent moment means.

For a Gaussian source \(e^{-aR}\),

\[
 A_t=\frac{t+1/2}{a}
\]

is affine in \(t\), hence

\[
 \Theta_t=0.                                           \tag{14}
\]

The heat direction is therefore exactly one of the neutral Gaussian-scale
directions quotiented out by the tangent-cone theorem.  It does not select the
quartic ray.

This gives a firm disposition:

\[
\boxed{
 \text{the source-canonical deformation is heat-neutral at Gaussian
 degeneracy; the quartic tangent is a hostile geometric clue, not the
 theta-selected flow.}
}                                                       \tag{15}
\]

## 8. Heat response of the cubic discriminator

The adjacent relative flux evolves according to

\[
\boxed{
 \partial_\lambda(\varepsilon_4-\varepsilon_3)
 =-(\Theta_4-\Theta_3).
}                                                       \tag{16}
\]

Equivalently,

\[
 \Theta_4-\Theta_3
 =A_5-3A_4+3A_3-A_2,                                  \tag{17}
\]

the third finite difference of the moment-mean sequence.

For

\[
 \mathfrak Q_{34}
 =1-|F(\varepsilon_4)-F(\varepsilon_3)|,
\]

the one-sided derivative away from equality is explicitly

\[
\boxed{
 \partial_\lambda\mathfrak Q_{34}
 =\operatorname{sgn}\!\bigl(F(\varepsilon_4)-F(\varepsilon_3)\bigr)
 \left[F'(\varepsilon_4)\Theta_4
       -F'(\varepsilon_3)\Theta_3\right].
}                                                       \tag{18}
\]

This is a path-derived stability observable.  It does not prove the endpoint
gate, but it asks a legitimate counterfactual question: does canonical heat
transport move the completed theta source toward or away from cubic failure?

The sharp structural target is now a third-difference theorem for \(A_t\),
weighted by the inverse-reserve susceptibilities \(F'(\varepsilon_t)\).
Unlike an arbitrary interpolation tangent, every term in (18) is determined
by the undecomposed theta moments.

The heat curvature also has an exact dispersion meaning.  Size bias gives

\[
 A_{t+1}-A_t
 =\frac{\operatorname{Var}_{Q_t}(R)}{A_t},             \tag{19}
\]

and hence

\[
\boxed{
 \Theta_t
 =\frac{\operatorname{Var}_{Q_t}(R)}{A_t}
  -\frac{\operatorname{Var}_{Q_{t-1}}(R)}{A_{t-1}}.
}                                                       \tag{20}
\]

Therefore the source-canonical stability problem is an acceleration law for
radial dispersion under adjacent size bias.  The Gaussian carrier has
constant dispersion increment and zero acceleration.  Theta arithmetic must
orient deviations from that neutral flow coherently with the already present
quadratic reserves.

## 9. Heat curvature is already encoded by adjacent reserves

The Stein recursion gives

\[
 \frac{\operatorname{Var}_{Q_t}(R)}{A_t^2}
 =\frac{2-C_{t+1}}{2t+1},                              \tag{21}
\]

while the global score identity gives

\[
 \frac{A_t}{A_{t-1}}
 =\frac{2t+1-C_t}{2t-1}.                               \tag{22}
\]

Substitution into (20) eliminates both variances and yields

\[
\boxed{
 \Theta_t
 =\frac{A_{t-1}}{(2t-1)(2t+1)}
 \left[
  (2t-1)C_t-(2t+1)C_{t+1}+C_tC_{t+1}
 \right].
}                                                       \tag{23}
\]

Thus heat curvature contains no new information beyond two adjacent
quadratic reserves and one scale factor.  Its dimensionless carrier is

\[
\boxed{
 \mathcal H_t
 =(2t-1)C_t-(2t+1)C_{t+1}+C_tC_{t+1}.
}                                                       \tag{24}
\]

Both the Gaussian boundary \(C_t=C_{t+1}=0\) and the asymptotic carrier
value \(C_t=C_{t+1}=2\) give \(\mathcal H_t=0\).  Heat curvature measures
departure from those two neutral profiles.

## 10. Hierarchy-shift obstruction

At the hostile interface,

\[
 \Theta_3
 =\frac{A_2}{35}
  (5C_3-7C_4+C_3C_4),                                 \tag{25}
\]

which is determined by the cubic pair under investigation, up to scale.  But

\[
 \Theta_4
 =\frac{A_3}{63}
  (7C_4-9C_5+C_4C_5).                                 \tag{26}
\]

Therefore the heat derivative of \(\mathfrak Q_{34}\) depends on \(C_5\).
The canonical deformation does not close the cubic gate from
\((C_3,C_4)\); it imports the next quadratic reserve.

This is a precise hierarchy-shift obstruction:

\[
\boxed{
 \text{heat differentiation of an adjacent-reserve theorem raises its
 required reserve depth by one.}
}                                                       \tag{27}
\]

Accordingly heat flow is a lawful stability probe but not yet a local
explanation of the \(t=3\to4\) gate.  Using it as a proof route would require
an independent theorem controlling \(C_5\), risking an infinite regress up
the Jensen tower.

The admissible escape is a closure relation that bounds \(\mathcal H_4\)
from \((C_3,C_4)\) by source structure.  Without such a relation, Route B is
strictly more expensive than the direct flux inequality and should be
deprioritized.
