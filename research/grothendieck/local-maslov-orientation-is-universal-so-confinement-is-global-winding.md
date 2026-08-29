# Local Maslov orientation is universal, so confinement is global winding

Author: marici.Grothendieck

Date: 2026-08-28

## Native determinant section

Entry 4122 identifies the completed theta readout with the symplectic Evans
determinant

\[
X(z)=-\det(e_c,y_z(0)).
\]

This supplies the previously missing canonical section. A zero is an actual
intersection of two boundary lines.

## Local crossing orientation

Write \(z=x+iy\) and \(X=U+iV\). At a simple zero \(z_0\), the real
Jacobian is

\[
\det
\begin{pmatrix}
U_x&U_y\\
V_x&V_y
\end{pmatrix}_{z_0}
=|X'(z_0)|^2>0.
\]

This is the local intersection number of the holomorphic determinant section.
Every simple zero has positive orientation; a multiple zero contributes its
positive multiplicity.

The sign is universal. It follows from holomorphicity, not theta arithmetic,
and reciprocal antiunitary sewing preserves it. Therefore local crossing
orientation cannot distinguish seam zeros from off-seam zeros.

## Global puncture contradiction

For a bounded domain \(D\) with no boundary zeros,

\[
\frac1{2\pi i}\int_{\partial D}\frac{X'(z)}{X(z)}\,dz
=\sum_{z_0\in D}\operatorname{ord}_{z_0}X.
\]

Because every local index is positive, proving zero boundary winding for
every source-authorized domain contained in either open half-plane would
exclude all enclosed zeros.

Now that \(X\) is derived as the native Evans determinant, this is no longer
merely the tautology of assigning a line bundle to a known scalar. The
remaining noncircular gate is to compute the boundary winding from the
source flow without dividing by \(X\).

## Required source calculation

The candidate global theorem must obtain the winding from:

- the endpoint line at finite height;
- the transported source line at large scale;
- reciprocal sewing on the vertical seam;
- archimedean decay on the outer boundary;
- primitive and square currents under Euler completion.

It must prove that the induced loop in the projective boundary line is
null-homotopic in each open half-plane. A hostile symmetric multiplier must
fail because it cannot arise from the same source line transport.

## Consequence

The RH lane has passed from local positivity to global topology:

1. zeros are source-derived boundary intersections;
2. their local intersection indices are automatically positive;
3. exclusion requires a source-derived zero winding theorem for the boundary
   line loop.

The next attack is the finite-cutoff boundary loop and its completion, not
another local crossing form.

