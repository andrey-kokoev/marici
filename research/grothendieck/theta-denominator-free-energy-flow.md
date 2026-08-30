# Denominator-free theta cone as an energy-flow law

## Operator stimuli and discovery provenance

This reduction was not reached by an autonomous continuation of the existing
thimble program. The decisive operator interventions were:

1. after the relative-cycle mutation invariant was exposed, ask what had
   hidden the reduction and whether the same cause could be hiding anything
   else useful;
2. accept the diagnosis that decomposition coordinates had obscured a single
   invariant quantity; and
3. direct an immediate return to the undecomposed object: "yep. let's do".

Those prompts changed the research question from "how do the thimble terms
remain positive?" to "what does their invariant sum mean before choosing a
thimble basis?" The answer first produced the energy flux identity
\(Q=VE/2\), and inspection of the vector field then exposed the exact
linearization \(w=z^2\) and its quarter-centered characteristic circles.

The methodological lesson is **surprise propagation**:

> When a result is unexpectedly simpler or more invariant than its derivation,
> identify the representation that concealed it, then re-audit every adjacent
> claim whose interpretation depended on that representation.

This is stronger than merely seeking a generalization. It treats surprise as
evidence of a model mismatch. The audit asks, for each nearby object:

- was it intrinsic, or only a coordinate artifact?
- was an apparent hypothesis actually implied by the invariant statement?
- was a discontinuity physical, or only a basis mutation?
- can a multidimensional estimate be replaced by transport along invariant
  leaves?
- does the new invariant change the correct falsifier?

Here that audit successively reinterpreted component positivity, Stokes-wall
continuity, transform nonvanishing, the two-copy kernel, and finally the
two-dimensional cone inequality itself.

## Exact first-order reduction

Let

\[
B(z)=\int_{\mathbb R}e^{zu}\,d\nu(u),
\qquad z=a+ib,
\]

and put

\[
I=B(z),\qquad J=B'(z),\qquad E(a,b)=|B(a+ib)|^2.
\]

Analyticity gives

\[
\partial_aE=2\Re(J\overline I),
\qquad
\partial_bE=-2\Im(J\overline I).
\]

For

\[
\alpha=2a-\frac{a}{2(a^2+b^2)},
\qquad
\beta=2b+\frac{b}{2(a^2+b^2)},
\]

the denominator-free cone numerator is therefore

\[
\boxed{
Q(a,b)=\Re\!\left[(\beta-i\alpha)J\overline I\right]
=\frac12\left(\beta\partial_a-\alpha\partial_b\right)E(a,b).
}
\]

Thus the RH-strength cone target is a source-derived Lyapunov inequality:

\[
\boxed{V E>0,\qquad V=\beta\partial_a-\alpha\partial_b.}
\]

No quotient, thimble basis, saddle, or zero location occurs in this identity.

## Exact two-copy kernel

If \(U,V\) are independent under the positive \(a\)-tilted theta law, then,
up to its positive normalization,

\[
Q=\frac12\mathbb E_a\!\left[
\beta(U+V)\cos b(U-V)
+\alpha(U-V)\sin b(U-V)
\right].
\]

This is just the integral kernel of the energy derivative \(VE/2\). The
previous midpoint/relative-coordinate competition is therefore a coordinate
expansion of a single scalar flux, in the same way that the thimble self and
cross terms are a basis expansion of the same quadratic functional.

## Complex velocity

The vector field has complex velocity

\[
\dot z=\beta-i\alpha
=-i\left(2z-\frac1{2z}\right).
\]

Hence, along any characteristic \(z(s)\) satisfying this ODE,

\[
\boxed{
\frac{d}{ds}|B(z(s))|^2=2Q(z(s)).
}
\]

The coefficients are not fitted to the theta source: they come from the
quarter-centered Pick geometry. The source enters only through the energy
\(|B|^2\).

## Exact characteristic circles

The apparent nonlinear flow linearizes under

\[
w=z^2.
\]

Indeed,

\[
\dot w=2z\dot z
=-2iz\left(2z-\frac1{2z}\right)
=-4i\left(w-\frac14\right).
\]

Therefore

\[
\boxed{
w(s)-\frac14=left(w(0)-\frac14\right)e^{-4is}.
}
\]

Every characteristic is a clockwise circle centered at \(1/4\) in the
\(w=z^2\) plane, and

\[
\boxed{\left|z^2-\frac14\right|=\text{constant}}
\]

is its first integral. Thus the energy-flow formulation exactly recovers the
quarter-centered angular geometry; it does not introduce a new family of
curves.

Consequently the two-dimensional cone target decomposes into a one-parameter
family of one-dimensional statements: on every admissible centered circle,
the lifted energy

\[
\mathcal E(w)=|B(\sqrt w)|^2
\]

must increase in the clockwise direction along the relevant arc.
Because the completed source is even, this energy is independent of the
choice of square-root branch. If

\[
w=\frac14+Re^{i\vartheta},
\]

then \(\dot\vartheta=-4\), and hence

\[
\boxed{Q=-2\,\partial_\vartheta\mathcal E.}
\]

Strict cone positivity is exactly strict decrease of \(\mathcal E\) with
counterclockwise angle—or strict increase along the clockwise physical flow.

## Polar form in the lifted coordinate

Write \(z=re^{i\theta}\). Direct calculation gives

\[
\frac{d}{ds}r^2=\frac{2ab}{r^2}=\sin(2\theta),
\]

and

\[
\frac{d\theta}{ds}
=-2+\frac{a^2-b^2}{2r^4}
=-2+\frac{\cos(2\theta)}{2r^2}.
\]

Equivalently the complex vector field is generated by the derivative of

\[
F(z)=z^2-\frac12\log z,
\qquad \dot z=-iF'(z).
\]

Although \(F\) itself is not constant, the substitution \(w=z^2\) above gives
the elementary first integral and the exact orbit geometry.

## What this removes

Picard--Lefschetz analysis remains useful for evaluating and certifying the
energy flux, but it is not part of the statement to be proved. All chamber
defect ratios are auxiliary coordinates. A global proof may instead establish
that \(E\) is strictly increasing along every admissible \(V\)-characteristic
through the target domain.

Moreover,

\[
B(z_0)=0\quad\Longrightarrow\quad E(z_0)=Q(z_0)=0.
\]

Thus strict flux positivity excludes transform zeros directly. There is no
separate denominator condition.

## Candidate proof routes

The exact reduction leaves three source-level possibilities:

1. **Energy transport:** compare \(E\) at the two endpoints of each
   characteristic and prove strict monotonicity from the completed theta
   functional equation.
2. **Symmetrized kernel:** integrate the displayed two-copy kernel by parts
   against the exact theta density until it becomes a positive square plus a
   controlled boundary term.
3. **Moment evolution:** differentiate \(VE\) along \(V\). Analyticity closes
   the resulting expression using only \(I,J,K\), potentially producing a
   second-order Lyapunov inequality without thimble coordinates.

After passing to \(w=z^2\), the normalized current becomes the imaginary part
of \((w-1/4)C'(w)/C(w)\). The desired energy law is therefore exactly a
Herglotz property. A zero-product expansion makes the positive Poisson-kernel
mechanism transparent but is conditional on RH; the live task is to derive
the same representation from the theta source. See
`theta-angular-current-herglotz-gate.md`.

The geometric multiplier itself is source-derived:
\(\Phi=(\partial_u^2-1/4)A\), so bilateral transformation produces
\(w-1/4\). This identifies the circle center with the spectral shift of the
theta source operator. The precursor transform is meromorphic, however, and
its endpoint pole cannot be dropped in an integration-by-parts proof. See
`theta-source-operator-quarter-center.md`.

The characteristic geometry is now exact. Full orbits are closed circles in
the \(w\)-plane, but the target quadrant selects arcs whose endpoints lie on
its boundary. The next hostile test is therefore sharper: classify those arc
endpoints and determine whether the completed-theta functional equation
controls the ingress value and derivative strongly enough to force clockwise
energy growth on the whole arc.

That classification is now explicit. Inner arcs connect two positive-real
points; outer arcs enter tangentially from the critical axis. Symmetry makes
the first ingress derivative vanish. The exact second derivative is a
geometrically weighted Laguerre expression plus a drift term; see
`theta-quarter-centered-arc-ingress.md`.

## Falsifiers

The Lyapunov mechanism is falsified by any target-domain point with

\[
VE\le0.
\]

The proposed boundary-transport proof is separately falsified by a target arc
whose ingress data are uncontrolled, or by an interior reversal of clockwise
energy monotonicity. Such a failure would not itself falsify every possible
cone proof; it would falsify this explanation of it.
