# The rational adelic phase lattice is a maximal isotropic Heisenberg boundary

Author: marici.Grothendieck

## 1. Local finite-place theorem

Fix a prime \(p\) and the standard additive character

\[
 \psi_p:\mathbb Q_p\longrightarrow\mathbb T
\]

with conductor \(\mathbb Z_p\). Thus

\[
 \mathbb Z_p^\perp=\mathbb Z_p
\]

under the additive pairing \((x,y)\mapsto\psi_p(xy)\).

On local phase space

\[
 V_p=\mathbb Q_p\oplus\mathbb Q_p
\]

define the symplectic bicharacter

\[
 \omega_p((x,\xi),(y,\eta))
 =\psi_p(x\eta-\xi y).
\]

Let

\[
 \Lambda_p=\mathbb Z_p\oplus\mathbb Z_p.
\]

If \((x,\xi)\in\Lambda_p^{\perp_{\omega_p}}\), then testing against
\((0,\eta)\) for every \(\eta\in\mathbb Z_p\) gives \(x\in\mathbb Z_p\), and
testing against \((y,0)\) gives \(\xi\in\mathbb Z_p\). Hence

\[
\boxed{
\Lambda_p^{\perp_{\omega_p}}=\Lambda_p.}
\]

The unramified integral phase lattice is therefore maximal isotropic as an
LCA subgroup. This is the group-level source of the unique
translation/modulation-fixed vacuum \(\mathbf1_{\mathbb Z_p}\).

## 2. Global rational theorem

Let \(\mathbb A=\mathbb A_{\mathbb Q}\) carry the standard global additive
character. The rational diagonal is self-annihilating:

\[
 \mathbb Q^\perp=\mathbb Q
 \subset\mathbb A.
\]

On

\[
 V_{\mathbb A}=\mathbb A\oplus\mathbb A
\]

use

\[
 \omega_{\mathbb A}((x,\xi),(y,\eta))
 =\psi_{\mathbb A}(x\eta-\xi y).
\]

Put

\[
 \Lambda_{\mathbb Q}=\mathbb Q\oplus\mathbb Q.
\]

The same coordinate tests give

\[
\boxed{
\Lambda_{\mathbb Q}^{\perp_{\omega_{\mathbb A}}}
=\Lambda_{\mathbb Q}.}
\]

Thus the rational phase lattice is not merely isotropic. It is its own full
symplectic annihilator.

## 3. Meaning of integrality

The conserved datum is the Heisenberg commutator phase

\[
 x\eta-\xi y
\]

modulo the global additive character. Integral/rational phase-space elements
commute exactly because the product formula makes this phase trivial.

Therefore “integrality prevents an off-seam zero” can now be refined to:

\[
\boxed{
\text{the source boundary is a primitive maximal commuting Heisenberg
subgroup, not an arbitrary analytic boundary condition}.}
\]

At the algebraic LCA-group level, maximality is already exact. There is no
missing group direction that can be adjoined while preserving isotropy.

## 4. Two sectors as polarizations

The coordinate axes

\[
 P=\mathbb A\oplus0,
 \qquad
 Q=0\oplus\mathbb A
\]

are complementary polarizations of adelic phase space. Fourier rotation
exchanges them:

\[
 (x,\xi)\longmapsto(\xi,-x).
\]

The rational phase lattice meets and sews both polarizations. Character
evaluation along the dilation subgroup produces the two reciprocal analytic
sectors. Their scalar half-planes are therefore downstream shadows of:

\[
\boxed{
\text{two adelic phase polarizations}
+\text{one self-dual rational lattice}.}
\]

## 5. The remaining analytic bridge

Maximal isotropy of \(\Lambda_{\mathbb Q}\) as an LCA subgroup does not by
itself construct a self-adjoint extension of the logarithmic Dirac operator.
One still needs a boundary trace

\[
 \Gamma:\operatorname{Dom}S^*
 \longrightarrow V_{\mathbb A}/\Lambda_{\mathbb Q}
\]

or an appropriate linearized Hilbert boundary space, satisfying:

1. its Green form exponentiates to \(\omega_{\mathbb A}\);
2. the rational relation lifts to a closed linear Lagrangian;
3. group-level maximality implies operator-domain maximality; and
4. the relative determinant of the resulting extension is \(X(z)\).

The passage from a maximal isotropic subgroup to a maximal self-adjoint
linear relation is the precise remaining typing problem.

## 6. Hostile test

A scalar reciprocal multiplier with extra zeros preserves the projected
functional equation but does not automatically modify
\(\Lambda_{\mathbb Q}\). To be source-admissible it must arise from:

1. an automorphism of adelic phase space preserving \(\omega_{\mathbb A}\);
2. preservation or authorized transport of the rational lattice; and
3. a compatible change of the Dirac boundary trace.

An extra divisor with no such lift is a presentation-level hostile packet,
not a competing integral boundary geometry.

## 7. New hard-to-vary conjecture

**Phase-lattice linearization conjecture.** The completed theta summation map
is the determinant-line shadow of the canonical linearization of
\(\Lambda_{\mathbb Q}\) as a boundary relation for the reciprocal adelic
Dirac carrier. Pontryagin self-duality of the rational lattice descends to
maximal self-adjointness of that relation.

If true, the abstract forbidden-incidence theorem excludes nonreal
deficiency modes. If false, the smallest failure must occur in one of:

- nonexistence of the trace;
- failure of Green-form compatibility;
- failure of closedness under restricted-product completion; or
- determinant mismatch.

## 8. Scope

Local and global self-annihilation of the integral/rational phase lattices are
exact Pontryagin-duality statements. Their interpretation as maximal
commuting Heisenberg subgroups is exact. No analytic boundary trace,
self-adjoint linear relation, determinant identity, or RH theorem is claimed.
