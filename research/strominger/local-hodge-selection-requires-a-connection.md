# Local Hodge Selection Requires a Connection

## Question

Can the global Hodge circle be made region-, mode-, or occurrence-selective by
replacing its constant angle with a source-dependent function \(\alpha\)?

## Universal obstruction

Let

\[
R_\alpha=\cos\alpha\,I+\sin\alpha\,J.
\]

Since \(J^2=-I\), differentiation gives

\[
d(R_\alpha C)
=R_\alpha\,dC+(d\alpha)J R_\alpha C.
\]

The second term is the exact selector current. It vanishes for a constant
angle and is generically nonzero for any localized selector. Consequently a
variable angle is not an endomorphism of the original derivative-defined
radiative construction.

## Minimal repair

Introduce a one-form \(A\) acting through the Hodge generator and define

\[
D_A=d+AJ.
\]

Then the transformation laws

\[
C\mapsto R_\alpha C,
\qquad
A\mapsto A-d\alpha
\]

give the exact covariance identity

\[
D_{A-d\alpha}(R_\alpha C)=R_\alpha D_A C.
\]

Thus local Hodge selection is not merely a finer use of the existing global
circle. It requires a new connection-valued constructor. The sign of its
transformation is forced: the opposite sign doubles rather than cancels the
selector current.

## Claim boundary

The calculation determines the minimal type and covariance law of the missing
constructor. It does not prove that asymptotically flat gravity supplies such
a Hodge connection. Adding an arbitrary compensator would be authority
laundering. The next physical question is whether an existing normal-bundle,
spin, duality, or boundary connection induces this exact action on the
radiative parity fiber.

## Disposition

Global execution is intrinsic. Local execution is a gauging problem. Its
first obstruction and its unique minimal connection repair are explicit.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/local_hodge_selector_connection_checks.py
```
