# Kinetic identification: a coordinate-invariant conditional interaction

## What this test adds

The [tensor-sewing logarithm](comparison-tensor-sewing-logarithm.md) had different
fourth derivatives in different probe coordinates. A potential coefficient alone
was not an interaction prediction. This test constructs a kinetic metric from the
already declared counting pairing and checks a complete tree four-point vertex.

The result is conditional but positive: three coordinates give the same on-shell
quartic once derivative interactions are included. The kinetic readout, spacetime
assignment and scales are stated explicitly; none is silently inferred from the
existence of a source fibration.

## Typed source plane and metric

The existing swap P acts on the real probe space `Point -> R`, with its counting
inner product. Its odd eigenspace is one-dimensional. Let

\[
v_0=e_{00},\qquad w=(e_{01}-e_{10})/\sqrt2.
\]

Here v0 is the basis vector of the selected source point, P v0=v0 and P w=-w.
The plane is `span(v0) + image(1-P)`; choosing the sign of w changes no result.
"Odd" means swap-anti-invariant, not fermionic statistics.

Normalize the probe in that plane:

\[
n(\theta)=\cos\theta\,v_0+\sin\theta\,w.
\]

Direct source evaluation gives

\[
\langle n,n\rangle=1,\qquad
\langle n,Pn\rangle=\cos2\theta,\qquad
\langle dn,dn\rangle=d\theta^2.
\]

Thus the induced counting metric is flat in the angle coordinate. This is a
local description on the unit sphere, or equivalently on real probe rays with a
chosen local lift. The positive-overlap branch is `|theta|<pi/4`.

`ComparisonKineticReadout.agda` proves source stability of the plane and its norm,
overlap and tangent pairing over a generic commutative ring, without trigonometry:
for the probe `(a,b,-b,0)` these are `a^2+2b^2`, `a^2-2b^2`, and `ac+2bd`.
Trigonometric normalization and differential geometry are checked symbolically.

## The same overlap readout supplies a neighboring-probe metric

Extend the already used scalar formula to two unit probes with positive overlap:

\[
D(n,m)=-\tfrac12\log\langle n,m\rangle.
\]

The potential readout is exactly `A(n)=D(n,Pn)`. For nearby probes on the plane,

\[
D(n(\theta),n(\theta+\epsilon))
=-\tfrac12\log\cos\epsilon
=\tfrac14\epsilon^2+O(\epsilon^4).
\]

Twice its diagonal Hessian therefore recovers the counting metric. For independent
unit probes, overlap multiplication makes D additive under tensor products, and
its induced metric is the sum of the factor metrics. The checker tests this
metric sewing, including the absence of mixed tangent terms.

**New physical identification:** use changes of probe assignment between nearby
spacetime points to define kinetic variation. Probe variations are not new source
fillers; this is a readout of functions on the existing source. Spacetime and its
metric are not constructed by the finite swap. A lattice of nearby probes with
edge cost proportional to D gives the quadratic gradient term in its continuum
expansion, but the lattice, continuum limit and normalization are additional data.

## Conditional scalar action and canonical field

With the usual real-scalar Lorentzian kinetic prescription, write

\[
\mathcal L=\frac{F^2}{2}(\partial\theta)^2-U A(\theta),\qquad
A(\theta)=-\tfrac12\log\cos2\theta.
\]

F and U are positive undetermined scales. In four dimensions F has mass dimension
one and U dimension four. Defining the canonical field `varphi=F theta` gives

\[
V(\varphi)=U\left[
\frac{\varphi^2}{F^2}+\frac{2\varphi^4}{3F^4}
+\frac{32\varphi^6}{45F^6}+\cdots\right].
\]

In the convention `V=m^2 varphi^2/2 + lambda varphi^4/4! + g6 varphi^6/6! + ...`,

\[
m^2=\frac{2U}{F^2},\qquad
\lambda=\frac{16U}{F^4},\qquad
g_6=\frac{512U}{F^6}=\frac{4\lambda^2}{m^2}.
\]

The scalar has no cubic vertex. Under the standard tree prescription its four-point
vertex is `-i lambda`. The sextic relation is a conditional canonical single-field
potential relation, not a computed full six-point amplitude or a loop statement.
This is not an exact quartic-only model.

The relation `lambda F^2/m^2=8` fixes the shape, not an absolute coupling. Any
positive pair (mass squared, quartic coupling) can be accommodated by choosing F
and U. Higher coefficients then cease to be independent. At finite F, setting the
mass to zero also sets this model's quartic to zero; an interacting massless
quartic theory is not obtained without changing the construction or taking a
singular limit.

## Coordinate test, including the missing derivative vertex

Use either `u=tan(theta)` or `z=sin(theta)`. Their metrics and dimensionless
potentials are

| Coordinate | Induced metric | A |
|---|---|---|
| theta | 1 | `-log(cos(2 theta))/2` |
| u | `1/(1+u^2)^2` | `log((1+u^2)/(1-u^2))/2` |
| z | `1/(1-z^2)` | `-log(1-2z^2)/2` |

All three have metric one at the vacuum. Let v=F times the respective coordinate,
and write the quartic terms as

\[
\mathcal L_4=a\,v^2(\partial v)^2-\lambda_{\rm pot}v^4/24.
\]

With all momenta incoming and signature +---, the derivative vertex is
`-4 i a sum_{i<j} p_i dot p_j`. The checker enumerates all 24 assignments of legs
to the two differentiated and two undifferentiated factors. Momentum conservation
and `p_i^2=m^2` give the sum `-2m^2`. The full on-shell coefficient is therefore

\[
\lambda_{\rm eff}=\lambda_{\rm pot}-8a m^2.
\]

| Coordinate | lambda_pot | a | lambda_eff |
|---|---|---|---|
| theta | `16 U/F^4` | 0 | `16 U/F^4` |
| u | 0 | `-1/F^2` | `16 U/F^4` |
| z | `24 U/F^4` | `1/(2F^2)` | `16 U/F^4` |

Thus the vanished quartic in u did **not** remove the interaction. It moved it
into the kinetic term. Agda also proves the generic algebraic invariance under
`v=w+beta*w^3`: `lambda_pot` changes by `24 m^2 beta`, while a changes by `3 beta`.
Their on-shell combination is unchanged. The Fourier and on-shell interpretation
is a declared conventional physics layer, not part of that ring proof.

## Does the source select this kinetic readout?

The round metric follows exactly if kinetic cost is the diagonal Hessian of the
same normalized counting-overlap D. Source symmetry alone is weaker. For example,

\[
g_\alpha=(1+\alpha\sin^2\theta)\,g_{\rm round}
\]

is P-invariant, has the same vacuum norm and is positive for alpha>=0. It changes
the quartic to `(16-8 alpha) U/F^4`; alpha=2 cancels it. An even stronger local
choice `g=A'(theta)^2/(4A(theta))`, smoothly extended at zero, makes the scalar
potential exactly quadratic in `sign(theta)*sqrt(A(theta))`.

These are **not** rival metrics satisfying all of the strengthened readout rules.
They fail independent tensor-metric sewing. Hold one factor at residual e and vary
a second through its vacuum. A conformal metric `f(e) g_round` on the product
assigns the second tangent coefficient f(e), while separate sewing requires f(0).
Hence this ansatz must have constant f, and vacuum normalization forces f=1.
At theta=pi/6, the alpha family's discrepancy is alpha/4.

This rules out that entire conformal family under the strengthened criterion; it
is not a uniqueness theorem for every possible source-dependent metric. The
physical identification of neighboring probes with kinetic variation remains a
requirement of this model, not a consequence of comparison typing alone.

## Additional fields and scope

The full unit-probe target has three tangent directions. Its potential Hessian at
v0 has eigenvalues `(2,0,0)` before the scales are restored: two even directions
remain massless. The source-selected scalar plane is a great circle, and the
potential gradient stays in it. The checker verifies vanishing normal force and
normal geodesic acceleration, so it is a consistent **classical** truncation.
This does not prove quantum decoupling of the other modes.

We now have a coordinate-independent tree interaction in an explicit conditional
kinetic model, rather than merely a quartic Taylor coefficient. Still unresolved:
physical spacetime/statistics and quantum prescription, selection of the full
neighboring-probe readout, F and U, additional-mode treatment, and the global
zero/negative-overlap sectors. No fixture coupling or physical action is claimed
as derived without these inputs.

## Verification

```text
pwsh -NoProfile -File research/nima/checkers/check_comparison_kinetic_readout.ps1 -Fresh
uv run --with sympy python research/nima/checkers/check_comparison_kinetic_readout.py
uv run --with sympy python research/aspect/scc/scc.py check nima-comparison-kinetic-readout
```

Fresh safe/cubical closure passes (27 local modules including the new root).
The transport call timed out at 120 seconds, but the completed headless receipt
records exit zero; the symbolic checker verifies its current source hashes.
Receipts: `results/agda-ComparisonKineticReadout.json` and
`results/comparison-kinetic-readout.json`. Symbolic checks cover the geometry,
three chart vertices, explicit momentum control, metric-sewing controls, extra
modes and the sextic coefficient. No formal spacetime or analytic-completion
theorem, independent review, commit or push is claimed.
