# Charge-Normalized Reciprocal Gradient Selector

## Question

Can the primitive charge normalization and reciprocal source action select the
remaining common coupling without inserting a fitted beta-function
coefficient?

## Claim boundary

Let the primitive source charge operator have frozen diameter

\[
\Delta_Q=2,
\]

as in WP841. For the positive portal coordinate \(x=g^2\), define

\[
z=\Delta_Qx,
\qquad
y=\log z.
\]

Reciprocity acts by

\[
z\longmapsto z^{-1},
\qquad
y\longmapsto-y.
\]

The normalized reciprocal mismatch action

\[
\Phi(y)=\cosh y
=\frac12\left(z+z^{-1}\right)
\]

is even, strictly convex, and has its unique minimum at \(y=0\). Its canonical
Euclidean gradient flow is

\[
\dot y=-\sinh y.
\]

This flow is equivariant under reciprocity and has Lyapunov function

\[
V(y)=\cosh y-1,
\qquad
\dot V=-\sinh^2y.
\]

Every finite \(y\) converges to zero. Equivalently, every \(x>0\) converges to

\[
x_*=\frac1{\Delta_Q}=\frac12,
\qquad
g_*=\frac1{\sqrt2}.
\]

The exact solution is

\[
\tanh\frac{y(\tau)}2
=e^{-\tau}\tanh\frac{y(0)}2.
\]

An arbitrary overall positive rate rescales \(\tau\) but changes neither the
selected value nor its basin. This replaces WP841's conjectured polynomial
beta law by the gradient of the same reciprocal source functional that fixes
the magnitude.

In the \(x\) coordinate,

\[
\dot x=\frac1{2\Delta_Q}-\frac{\Delta_Q}{2}x^2.
\]

The vector field obeys exact covariance under
\(x\mapsto(\Delta_Q^2x)^{-1}\).

## Integration with the portal chain

- WP859 and WP867 supply the normalized odd difference ray and relative sign,
  conditional on the marked boundary source.
- The primitive diameter fixes the reciprocal unit and hence the numerical
  magnitude.
- The reciprocal gradient supplies a global positive-coupling basin.
- WP866 supplies the state-channel basin; this is distinct from, and
  compatible with, the coupling basin above.
- WP869 transports the actual portal projector and detector frame through a
  gapped threshold.
- WP870 makes detector co-transport a shared-action Ward consequence and
  makes the terminal amplitude equal to the selected coupling.

These arrows form a coherent conditional constructor. Two authority gates
remain.

First, the primitive diameter must be retained by the complete source
character through thresholds. If an extremal charge is deleted and
\(\Delta_Q\) changes from two to one, the selected coupling changes from
\(1/\sqrt2\) to one. WP846--WP868 show that neither ordinary anomaly matching
nor an index alone suffices; the marked charge operator and detector
evaluation must be transported.

Second, the gradient parameter \(\tau\) is dimensionless. Calling it physical
flavor RG requires a source-derived orientation and normalization map to the
renormalization scale. The fixed point and basin do not depend on the rate,
but the claim that this flow is the physical coupling flow still requires a
microscopic derivation.

## Instrument boundary

Under WP870's Ward locking, the source-level detector amplitude at the fixed
point is \(1/\sqrt2\). A calibrated 'physical16' instrument must still identify
that dimensionless source coupling with a finite-width, background-controlled
detector response. The reciprocal action does not provide detector units,
efficiencies, or covariance.

## Smallest exact falsifiers

- Changing only the reciprocal normalization from \(\Delta=2\) to
  \(\Delta=3\) moves \(g_*\) from \(1/\sqrt2\) to \(1/\sqrt3\).
- Deleting the charge-one extremum changes the active diameter from two to one
  and moves \(g_*\) to one.
- Keeping the reciprocal gradient as an auxiliary flow without a physical RG
  map does not establish a flavor-scale trajectory.

## Disposition

Strongest conditional source selector in the current chain. A
charge-normalized reciprocal mismatch functional fixes the positive magnitude
and supplies a coefficient-free global basin. Combined with the odd boundary,
Kato transport, and Ward-locked detector, it conditionally fixes sign,
magnitude, basin, threshold frame, and source-level readout. It is not yet an
admitted microscopic flavor principle because source retention of
\(\Delta_Q\), physical RG typing, and calibrated 'physical16' realization are
unproved.

## WP872 correction

WP872 withdraws the interpretation of the displayed cosh-gradient as a
Ward-compatible physical coupling beta function because it is nonzero at
\(x=0\). The magnitude \(1/\sqrt2\) and global basin on \(x>0\) remain exact.
The multiplicative reciprocal replacement is the gradient of
\(\log\cosh y\); it has the same selected value and positive-domain basin but
leaves the decoupled cusp fixed.

## Verification

Run:

~~~text
uv run --with sympy python research/flavor/checkers/wp871_charge_normalized_reciprocal_gradient_selector.py
~~~
