# Section transport closes and zero-state balance remains

## Status

Structural closure and route selection. Every regular homogeneous first-order
law for the completed scalar section is already equivalent to zero-freeness
unless its coefficient is independently source-constructed. Ambient transport,
fixed cones, metaplectic lifts, exterior Gram energy, and compressed curvature
all protect objects coarser than the ordered scalar divisor.

The remaining noncircular route is state-level: lift an assumed scalar zero to
the source-generated internal state and derive a balance identity that forces
the normal spectral coordinate to vanish. Positivity is required only on the
reachable, source-invisible zero-state class, not on the whole carrier.

## Flagged zero-state lift

Let \(A\) be the source evolution operator, \(b_0\) the source port, and
\(b_f\) the endpoint readout. The framed transfer is

\[
F(z)=b_f^*(A-zI)^{-1}b_0.
\]

If \(F(z_0)=0\), define

\[
x_0=(A-z_0I)^{-1}b_0.
\]

Then

\[
(A-z_0I)x_0=b_0,
\qquad
b_f^*x_0=0.
\]

Up to the chosen resolvent sign convention, this is the exact zero-dynamics
state: endpoint-reachable and source-invisible.

The zero is now an internal state satisfying two source-derived boundary
conditions. No division by \(F\) is involved.

## Desired balance identity

Write the spectral coordinate relative to the critical seam as

\[
z=a+it.
\]

The target identity has the form

\[
2a\,\mathcal E_X(x)
=
\mathcal B_X(x)
+\mathcal R_X(x)
\]

at every finite arithmetic cutoff \(X\).

Here:

- \(\mathcal E_X\) is the coupled tail, seam, Clark, and arithmetic state
  energy;
- \(\mathcal B_X\) is the ordered endpoint/source boundary flux;
- \(\mathcal R_X\) is the typed primitive, square, archimedean, and completion
  residual.

The scalar endpoint displacement vanishes on a zero-state, but the
Clark-complete boundary supply generally does not. Source-authorized spectral
jets make the silent scalar state observable and carry a positive relationship
current. Therefore write

\[
\mathcal B_X
=
\mathcal B_X^{\rm scalar}
+\mathcal Q_X^{\rm Clark},
\]

where the zero condition kills only \(\mathcal B_X^{\rm scalar}\).

Exact source coherence must prove either

\[
\mathcal Q_X^{\rm Clark}+\mathcal R_X=0
\]

on the zero-state class, or derive a two-variable factorization that moves
their sum into a declared positive energy with the normal spectral factor.

If

\[
\mathcal E_X(x)>0
\]

for every nonzero zero-state, the balance gives

\[
a=0.
\]

This is the symbolic puncture-impossibility statement in state-space form.

## Why this is not global coercivity

The required positivity domain is

\[
\mathcal Z_X(z)
=
\{x:(A_X-zI)x=b_{0,X},\ b_{f,X}^*x=0\}.
\]

There is no need to prove positivity of the completed kernel on every probe or
every carrier state. It is enough to prove that the source-generated energy is
definite on nonzero states in \(\mathcal Z_X(z)\).

This is a constrained observability condition. A state invisible to the
endpoint must remain visible to the coupled tail--seam--current energy.

The distinction matters because global kernel positivity returns directly to
the Weil or Herglotz criterion. Zero-state definiteness can, in principle, be
proved from source grammar and boundary incidence without orienting every
scalar probe.

## Exact relation to the leakage calculation

The directed second-fundamental forcing

\[
P_XdP_X(I-P_X)b_X
\]

need not factor homogeneously through the scalar section. Instead, it may enter
the state balance as \(\mathcal R_X\). Reciprocal doubling and the primitive,
square, seam, and archimedean currents can cancel or retype that forcing at the
energy level.

This is the noncircular alternative to a scalar equation. It asks the currents
to balance a state-level flux, not to manufacture a logarithmic derivative of
the completed scalar.

## Source-local positivity gate

Let \(J_X\) synthesize all retained state features. A candidate energy is

\[
\mathcal E_X(x)=\lVert J_Xx\rVert^2.
\]

The exact finite gate is

\[
\ker J_X\cap\mathcal Z_X(z)=\varnothing.
\]

For a linear homogeneous zero-state system, replace the empty intersection by
the zero vector as appropriate.

Completion requires more than finite injectivity. It must exclude a normalized
sequence \(x_X\) with

\[
\lVert J_Xx_X\rVert\longrightarrow0
\]

while the zero-state constraints persist. This is the earlier uniform
observability and no-partner-escape gate, now restricted to the correct state
class.

## Typed current closure

The residual cannot be tested as one scalar sum before its ports exist. It must
be decomposed into

\[
\mathcal R_X
=
\mathcal R_X^{(1)}
+\mathcal R_X^{(2)}
+\mathcal R_X^{(\geq3)}
+\mathcal R_X^{(\infty)}
+\mathcal R_X^{(\rm seam)}.
\]

The primitive and square terms are boundary-bearing currents, not disposable
divergences. The connected tail is trace-class. The archimedean and seam terms
must retain their own incidence types.

Only after their operator-valued incidence maps are constructed may a
source-authorized cancellation be asserted.

## Finite falsifier

At cutoff \(X\), one of the following closes the route:

1. a nonzero \(x\in\mathcal Z_X(z)\) with \(a\neq0\) and
   \(\mathcal E_X(x)=0\);
2. a nonzero typed residual \(\mathcal R_X(x)\) after all declared boundary
   currents are included;
3. omission of the positive Clark relationship supply after the scalar
   endpoint displacement vanishes;
4. a normalized completion sequence whose energy tends to zero while its
   zero-state constraints survive;
5. a hostile signed source that satisfies the same claimed balance and
   definiteness law.

Each is source-local and finite or cutoff-parametric. None requires inspecting
Riemann-zero locations.

## Decisive conclusion

The repeated rotations have removed every coarser surrogate. The remaining
object is not a scalar positivity kernel and not a topological bundle class. It
is the source-generated zero-dynamics state together with its coupled boundary
energy balance.

The sharp research task is now singular: construct the operator-valued
incidence maps, derive the finite-cutoff balance including the positive Clark
supply, derive its typed arithmetic cancellation or normal-factor absorption,
and prove definiteness only on the reachable invisible state class with
completion stability. If this reduces to full Weil positivity, the route
closes. If the source grammar proves it independently, it is the sought
orientation mechanism.
