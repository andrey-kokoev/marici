# The Clark two-sheet identity polarizes to a genuine positive kernel

Author: `marici.Nima`

Date: 2026-08-26

Status: exact mixed-height Clark kernel; full transfer-defect identity remains

## Source amplitudes

In the common Clark frame, write

\[
E_+(z)=X(z)+iY(z),
\qquad
E_-(z)=X(z)-iY(z).
\]

Here (X) contains the retained Green-plus-source feature and (Y) contains
the Clark derivative feature with its source-fixed coefficient.

Because these are vector identities before taking norms, they admit exact
sesquilinear polarization.

## Mixed-height identity

For two spectral parameters (z,w),

\[
E_+(w)^*E_+(z)+E_-(w)^*E_-(z)
=
2X(w)^*X(z)+2Y(w)^*Y(z).
\]

The spin-two cross terms cancel at unequal heights exactly as they do on the
diagonal. Therefore

\[
K_{\mathrm{Clark}}(w,z)
=
2X(w)^*X(z)+2Y(w)^*Y(z)
\]

is a genuine positive kernel.

For any finite collection of heights (z_j) and coefficients (c_j),

\[
\sum_{j,k}\bar c_j
K_{\mathrm{Clark}}(z_j,z_k)c_k
=
2\left\lVert\sum_jX(z_j)c_j\right\rVert^2
+2\left\lVert\sum_jY(z_j)c_j\right\rVert^2.
\]

This is nonnegative without invoking the completed theta scalar or its zeros.

## Exact gain

The Clark bulk has now passed three distinct gates:

1. positive energy at one height;
2. exact common-frame polarization across heights;
3. positive semidefinite Gram matrices for every finite height packet.

This is enough to serve as one feature block in a lurking-isometry
construction.

## What it does not supply

The Clark kernel alone is not yet the transfer defect

\[
I-\Theta(w)^*\Theta(z).
\]

The complete source identity must include:

- the seam feature;
- primitive and square boundary currents;
- archimedean completion;
- mixed terms created by their interaction;
- the factor (1-\bar wz) associated with sector evolution.

The outstanding residual is

\[
\mathcal R_X(z,w)
=
I-\Theta_X(w)^*\Theta_X(z)
-(1-\bar wz)
\left(
K_{\mathrm{Clark},X}(w,z)
+K_{\mathrm{boundary},X}(w,z)
\right).
\]

No positivity theorem is needed for the Clark summand. The research frontier
has moved to constructing the boundary kernel and proving this exact
conservation identity.

## Strictness gate

Even the positive Clark kernel may have a null direction on admissible states
if both (X) and (Y) vanish. The seam and arithmetic ports may repair that
observability defect.

Thus the completed theorem still needs injectivity of the full feature map and
a completion-stable lower bound. Positivity of the Clark block is established;
strict observability of the complete source system is not.

## Finite falsifier

At any cutoff, form the mixed-height Gram matrix from the explicit
(X(z_j)) and (Y(z_j)). A negative minor would contradict the common-frame
identity. More importantly, compute its nullspace and test whether the typed
boundary features detect every Clark-invisible direction.

