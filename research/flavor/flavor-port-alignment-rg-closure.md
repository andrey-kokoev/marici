# Port-alignment RG closure

## Shared gauge representation

The connector rows and every flavor-adjoint component of \(X_i\) transform as
vectors of \(SO(3)_P\). Define

\[
G_S=S^TS,
\qquad
(G_X)_{ij}=\operatorname{Tr}(X_iX_j).
\]

WP493 includes their radial product

\[
I_{\rm rad}=\operatorname{Tr}(G_S)\operatorname{Tr}(G_X),
\]

but not their relative-alignment invariant

\[
I_{\rm align}=\operatorname{Tr}(G_SG_X).
\]

## Exact gauge-support identity

For two port vectors \(s,x\), the three real antisymmetric generators obey

\[
\sum_a(s^TL_ax)^2=|s|^2|x|^2-(s\cdot x)^2.
\]

Summing over connector rows and flavor-adjoint components gives

\[
I_{\rm rad}-I_{\rm align}.
\]

Thus port-gauge loops have exact support on the alignment invariant. Overall
loop prefactors are not asserted here.

## Hostile pair

Parallel and orthogonal unit vectors have the same radial product. Their
alignment invariants are respectively one and zero, and the gauge contraction
is respectively zero and one. Therefore no radial-coordinate completion can
represent the gauge counterterm.

At the isotropic WP484 vacuum, the radial and alignment values are
\(18s^2\mu^2\) and \(6s^2\mu^2\), so the generated combination is nonzero.
Adding this coupling changes the scalar potential quantitatively even though
the isotropic presentation remains admissible.

WP493 is therefore still nonradially incomplete. The alignment coefficient
must run independently, after which the remaining adjoint and cyclic-row
quartic invariants and the corrected vacuum/width cone must be audited.
