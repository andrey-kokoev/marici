# The Composite Polarization Connection Is Local and Singular

## Question

Can the radiative tensor itself construct the active duality connection needed
for local Hodge selection?

## Construction on the nonzero locus

Write the real polarization fiber as a two-vector \(C\) with Hodge generator
\(J\). Wherever \(C\neq0\), define

\[
A_C=-\frac{\langle JC,dC\rangle}{\lVert C\rVert^2}.
\]

Under a local Hodge rotation \(C\mapsto R_\alpha C\), exact calculation gives

\[
A_{R_\alpha C}=A_C-d\alpha.
\]

Thus the existing field constructs a connection with precisely the covariance
law required by Entry 3789.

## What the construction does

In polar fiber coordinates \(C=r(\cos\theta,\sin\theta)\),

\[
A_C=-d\theta,
\qquad
(d+A_CJ)C=dr(\cos\theta,\sin\theta).
\]

The covariant derivative removes all polarization-phase variation. Hence this
connection does not provide independent control over the phase. It declares
that phase to be gauge and retains only radial variation.

## Global obstruction

The denominator vanishes at every zero of \(C\). Around a unit-winding zero,

\[
\oint A_C=-2\pi.
\]

Consequently the composite connection is flat only on the punctured nonzero
locus and cannot extend regularly across a zero with nonzero winding. The
would-be repair converts zeros into connection defects carrying integral
holonomy.

## Authority boundary

The composite construction is source-derived but has the wrong capability
type. It is a gauge quotient constructed from the state being acted upon, not
an independently variable active connection. It cannot choose a local Hodge
rotation while retaining polarization phase as physical information.

An actual local selector still requires an independent connection or control
field. Such a field must also specify how its curvature and zero-locus defects
enter the gravitational boundary equations.

## Disposition

The composite candidate closes local covariance away from zeros but fails as
active control and fails globally across winding zeros. The missing
constructor is now more sharply typed: independent from \(C\), regular on the
declared state domain, and equipped with curvature and defect data.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/composite_polarization_connection_checks.py
```
