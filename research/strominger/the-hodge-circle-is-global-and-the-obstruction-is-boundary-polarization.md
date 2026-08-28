# The Hodge Circle Is Global and the Obstruction Is Boundary Polarization

## Question

Once the celestial Hodge generator \(J\) is source-derived, does a further
constructor remain necessary to obtain the selective sheet gate?

## Circle action

On the unrestricted real radiative tensor fiber define

\[
R(c,s)=cI+sJ,
\qquad
c^2+s^2=1.
\]

Since \(J^2=-I\) and \(J^T=-J\), this is an orthogonal circle action. Acting
with the same rotation on the shear and news fibers also preserves the
radiative symplectic form. The quarter-turn \(R(0,1)=J\) is precisely the
sheet operation represented by \(\operatorname{diag}(i,-i)\).

Therefore no additional algebraic conditionalizer is required on the full
radiative phase space. The apparent selective action on the two helicity
sheets is simply one real global Hodge rotation.

## Boundary criterion

Let \(B\) be the linear subspace selected by a boundary condition. The Hodge
circle restricts to \(B\) exactly when

\[
J(B)\subseteq B.
\]

The hostile fixture is a one-parity boundary polarization. In the real fiber
with electric and magnetic coordinates, the electric line is

\[
B_E=\operatorname{span}(1,0).
\]

But \(J(1,0)=(0,1)\), so \(B_E\) is not invariant. The joint
electric-magnetic boundary fiber is invariant.

This relocates the obstruction. It is not a missing source generator and not
an intrinsic failure of the radiative phase space. It is produced whenever a
boundary contract retains one parity while excluding its Hodge partner.

## Authority boundary

The global Hodge circle is source-authorized by orientation, metric, and the
radiative symplectic structure. This still does not construct a control that
applies different angles to selected regions, modes, or occurrences. Such
addressability requires a separately typed control field or interface, and
its derivatives generally add boundary or bulk terms.

## Disposition

The unrestricted algebraic execution problem closes. The remaining frontier
has two exact branches:

1. classify which physical boundary conditions are \(J\)-stable;
2. determine whether any source-authorized nonconstant selector can localize
   the Hodge angle without generating an obstruction current.

## Verification

```powershell
uv run --with sympy python research/strominger/checkers/radiative_hodge_circle_boundary_checks.py
```
