# Multiplicative Reciprocal RG Domain Audit

## Question

Is WP871's reciprocal gradient compatible with the multiplicative
renormalization required by WP870's conserved-current coupling, and can a
compatible repair still make a nonzero portal unavoidable?

## WP871 compatibility defect

WP871 used

\[
\Phi_{\cosh}(y)=\cosh y,
\qquad
\dot y=-\sinh y,
\qquad
y=\log(\Delta x),
\qquad x=g^2.
\]

In the physical coupling coordinate this gives

\[
\beta_x^{\cosh}
=\frac1{2\Delta}-\frac{\Delta}{2}x^2.
\]

Hence

\[
\beta_x^{\cosh}(0)=\frac1{2\Delta}\ne0.
\]

The quotient \(\beta_x^{\cosh}/x\) has a pole at the decoupled point. This
cannot be the beta function of a multiplicatively renormalized Ward coupling
on a source domain containing \(x=0\): it generates the interaction from exact
decoupling without a declared additive source. WP871's magnitude and
positive-domain basin remain correct, but its claim to a Ward-compatible
physical coupling flow is withdrawn.

## Exact reciprocal repair

Replace the potential by

\[
\Phi_{\log}(y)=\log\cosh y.
\]

It is even and strictly convex, and its gradient flow is

\[
\dot y=-\tanh y.
\]

In the \(x\) coordinate,

\[
\beta_x
=-x\tanh\log(\Delta x)
=x\frac{1-\Delta^2x^2}{1+\Delta^2x^2}.
\]

This beta function is analytic at zero and has an explicit factor \(x\).
It is exactly covariant under reciprocal inversion

\[
x\longmapsto\frac1{\Delta^2x}.
\]

Its nonzero fixed point remains

\[
x_*=\frac1\Delta,
\qquad
g_*=\frac1{\sqrt\Delta}.
\]

The Lyapunov derivative is

\[
\dot\Phi_{\log}=-\tanh^2y,
\]

and the exact solution is

\[
\sinh y(\tau)=e^{-\tau}\sinh y(0).
\]

Thus every \(x>0\) converges to \(1/\Delta\), with normalized linear exponent
\(-1\). For \(\Delta=2\), the selected portal remains \(1/\sqrt2\).

## The admitted-domain obstruction

Multiplicative compatibility restores

\[
\beta_x(0)=0.
\]

Therefore the decoupled state is a fixed point. The reciprocal map is defined
only on \(x>0\), where zero is an ideal boundary or cusp. The repaired
principle makes the magnitude unavoidable only on the admitted nonzero
duality domain.

This is not a semantic detail. There are two distinct claims:

1. Conditional selection: every admitted \(x>0\) flows to \(1/\Delta\).
2. Portal inevitability: the complete physical source domain excludes
   \(x=0\).

The first is proved. The second requires an independent source theorem.
Declaring duality only on invertible couplings does not by itself prove that
the decoupled theory is physically inadmissible. If zero remains a legitimate
source state, the portal is not unavoidable.

## Gate classification

- Relative sign: supplied conditionally by the odd marked boundary.
- Magnitude: \(1/\sqrt2\) on the \(\Delta=2\) nonzero domain.
- Coupling basin: the entire strictly positive line.
- Exact zero seed: remains zero.
- Threshold and readout: retain the WP869--WP870 conditional Kato/Ward
  construction.
- Remaining source gate: prove exclusion of the decoupled cusp and derive the
  reciprocal flow as the physical flavor RG.
- Calibration: the finite-width 'physical16' instrument remains absent.

## Smallest exact falsifier

The initial condition \(x(0)=0\) is the smallest falsifier of unconditional
portal inevitability. It satisfies the repaired beta law and remains zero,
while every positive initial condition converges to \(1/\Delta\).

## Disposition

Correction and sharpening of WP871. The log-cosh reciprocal gradient is the
first Ward-compatible, coefficient-free global selector of the portal
magnitude on \(x>0\). It does not generate a portal from exact decoupling. The
next source question is no longer which beta coefficient gives
\(1/\sqrt2\), but whether the microscopic source category excludes the
zero-coupling cusp for a reason independent of the desired answer.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp872_multiplicative_reciprocal_rg_domain_audit.py
~~~
