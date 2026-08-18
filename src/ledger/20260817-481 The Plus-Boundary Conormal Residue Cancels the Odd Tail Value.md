# Entry 481 — The Plus-Boundary Conormal Residue Cancels the Odd Tail Value

Entry 480 shows that ordinary restriction of the odd Bockstein image retains
the unwanted boundary value

\[
h|_{b=1}=6a^3,
\qquad h=3a^3(1+b).
\]

The derived boundary complex has a source-native candidate for its connecting
term: the conormal residue of the already established deformation-factor
class

\[
g=a^3(1-b^2).
\]

## Plus-boundary identity

Along \(b=1\), use the declared normal parameter \(b-1\).  Then

\[
\operatorname{Res}_{b=1}(g)
=\left.\frac{a^3(1-b^2)}{b-1}\right|_{b=1}
=-2a^3.
\]

Consequently

\[
\boxed{
h|_{b=1}+3\operatorname{Res}_{b=1}(g)
=6a^3-6a^3=0.
}
\]

The coefficient three is not fitted: it is the coefficient in the
source-derived mixed class \(h=3a^3(1+b)\) from Entry 477.  Since
\(b^j|_{b=1}=1\), the same identity cancels the ordinary boundary value of
every filtered generator \(b^jh\).

Thus the one residual tail direction left by Entry 480 is killed at the plus
boundary once the conormal connecting term is retained.  This is precisely
the behavior that ordinary restriction missed.

## Remaining two-endpoint gate

At the other boundary,

\[
h|_{b=-1}=0,
\qquad
\operatorname{Res}_{b=-1}(g)
=\left.\frac{a^3(1-b^2)}{b+1}\right|_{b=-1}
=2a^3.
\]

Therefore the same unspecialized conormal class has a nonzero minus-boundary
residue even though the mixed tail already vanishes there.  Entry 481 proves
the plus-boundary cancellation only.  A full two-endpoint complex must explain
whether the minus residue is killed by its lattice transition, maps to a
different degree, or survives as a boundary defect.  Simply applying the
coefficient three at both ends would be incorrect.

The next gate is to transport the conormal generator through the odd lattice
whose transition divisor is \(3[1]+4[-1]\), and compute the minus-boundary
component in that intrinsic frame.

The executable audit is
`research/voevodsky/check_soft_axis_odd_conormal_boundary_cancellation.py`.
