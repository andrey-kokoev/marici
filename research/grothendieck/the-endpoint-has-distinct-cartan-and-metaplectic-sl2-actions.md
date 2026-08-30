# The Endpoint Has Distinct Cartan and Metaplectic sl2 Actions

## Correction

The previous representation audit compared two differently typed actions.
They must be separated.

On each fixed endpoint grade

\[
H_l=\operatorname{Sym}^{2l}\mathbb C^2,
\]

the ordinary spinor Cartan action is

\[
E_C=u\partial_v,\qquad F_C=v\partial_u,\qquad
H_C=u\partial_u-v\partial_v.
\]

It preserves grade and has Casimir

\[
\Omega_C=4l(l+1)I.
\]

On the full even-Veronese algebra, choosing the source-labelled spinor
coordinate \(u\) gives another action:

\[
E_M=\frac{u^2}{2},\qquad F_M=-\frac{\partial_u^2}{2},\qquad
H_M=u\partial_u+\frac12.
\]

This action changes endpoint grade, preserves the exponent of \(v\), and has

\[
\Omega_M=H_M^2+2H_M+4F_ME_M=-\frac34I.
\]

It is the same metaplectic `sl2` representation used by the theta control
system, with the \(v\)-exponent acting as spectator multiplicity.

## Meaning of the two actions

The Cartan action rotates the two spinor coordinates inside one homogeneous
grade. The metaplectic action performs quadratic creation and annihilation
along one selected spinor axis and therefore moves between grades. Their
Casimirs differ because they answer different questions.

Consequently the difference

\[
4l(l+1)+\frac34
\]

is not an anomaly that a seam must absorb. It is the difference between two
central characters belonging to two distinct actions. Its half-integer
factorization is algebraically true but does not authorize a boundary state.

## Surviving bridge

The operator-level bridge is stronger than the corrected audit allowed:

- theta and endpoint share the metaplectic control algebra;
- they share its central character;
- the endpoint carries spectator multiplicity indexed by the untouched
  spinor exponent;
- choosing the active spinor coordinate remains source data;
- theta's seam and completion data remain unmatched.

The next comparison must therefore test whether the theta stage arrows act
diagonally on the endpoint spectator multiplicity and whether reciprocal
sewing changes the selected spinor axis. Casimir matching is no longer the
obstruction.

## Falsifier

The correction fails if the operators \(E_M,F_M,H_M\) do not preserve the
even-Veronese algebra, fail the `sl2` commutators, or have a Casimir other than
\(-3/4\). Exact monomial checks test all three claims.
