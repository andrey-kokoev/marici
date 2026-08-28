# Aspect Germ Audit of the Charge-Recursive Selector

## Question

Does WP849's charge-recursive vacuum selector survive Aspect's distinction
between a well-conditioned local germ and a source-authorized completion?

## Marked carrier germ

The native carrier is one charged-spurion configuration

\[
(s_1,s_2,s_3),\qquad \operatorname{wt}(s_j)=-j,
\]

with identity supplied by the three labelled charge lines, provenance supplied
by the declared recursive potential, and an unconsumed quotient port supplied
by the common \(U(1)\) action. The target is the projective kernel ray of the
lifted incidence map. The three recursive equations are not independent
unmarked observations: they must refer to the same spurion packet.

## Full complex germ

Write \(s_j=v(x_j+i y_j)\) and expand at the representative
\((x_1,x_2,x_3;y_1,y_2,y_3)=(1,1,1;0,0,0)\). For unit positive coefficients,
the real Hessian has rank five. Its unique null line is

\[
(0,0,0;1,2,3),
\]

which is exactly the infinitesimal \(U(1)\) orbit. The Hessian restricted
transversely to the orbit is positive. Thus WP849 passes the full complex
local-germ and quotient-tangent tests; its earlier real gauge-fixed Hessian was
correct but incomplete evidence.

## Full-fiber gate

For the declared sum-of-squares potential, positivity makes the global zero
locus exactly one full \(U(1)\) orbit. The projective kernel map is constant
on that orbit. This is stronger than a tangent-kernel claim and passes
Aspect's full-fiber requirement inside the declared model.

## Completion hostile

Gauge covariance and renormalizability alone also admit

\[
\delta V=\epsilon v^2|s_2|^2.
\]

This perturbation is not constant on the WP849 constraint completion. At the
selected representative its real gradient is proportional to \((0,2,0)\).
Implicit differentiation through the transverse Hessian gives

\[
\frac{d(x_1,x_2,x_3)}{d\epsilon}\bigg|_{\epsilon=0}
=\left(-\frac12,-2,-\frac52\right).
\]

Hence an arbitrarily small admitted invariant perturbation moves the VEV
ratios and the selected projective kernel ray. The finite positive Gram floor
therefore certifies a nondegenerate germ of one chosen potential, not a
source-forced completion of the invariant operator algebra.

## Verdict

WP849 passes Aspect's marked-carrier, quotient-tangent, and full-fiber tests
for its declared potential. It fails the source-completion gate. Its proper
classification remains a conditional selector, not yet an unavoidable flavor
selector. The smallest exact falsifier is the single allowed operator
\(\epsilon v^2|s_2|^2\), whose first-order displacement is nonzero.

The missing constructor is a source theorem that forbids this operator and
all other orbit-moving invariants, or fixes their coefficients so the same
orbit remains stationary. A positive Hessian cannot supply that authority.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp850_charge_recursive_selector_aspect_germ_audit.py
```
