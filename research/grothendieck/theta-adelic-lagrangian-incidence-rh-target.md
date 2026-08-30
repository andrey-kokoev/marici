# RH as forbidden nonreal incidence in an adelic boundary phase space

Author: marici.Grothendieck

## 1. The primary object is boundary phase space

Let \(S\) be a densely defined closed symmetric realization of the doubled
logarithmic Dirac carrier. Its maximal adjoint domain has a boundary trace

\[
 \Gamma u=(\Gamma_0u,\Gamma_1u)
\]

into a boundary space \(\mathcal B\oplus\mathcal B\). Green's identity has the
form

\[
\begin{aligned}
 \langle S^*u,v\rangle-\langle u,S^*v\rangle
 ={}&
 \langle\Gamma_1u,\Gamma_0v\rangle_{\mathcal B}\\
 &-\langle\Gamma_0u,\Gamma_1v\rangle_{\mathcal B}.
\end{aligned}
\]

The right side is the Hermitian symplectic form

\[
 \Omega((x,y),(x',y'))
 =\langle y,x'\rangle-\langle x,y'\rangle.
\]

This boundary phase space is primary. A self-adjoint boundary condition is a
maximal \(\Omega\)-isotropic, hence Lagrangian, subspace

\[
 L_{\mathrm{src}}\subset\mathcal B\oplus\mathcal B.
\]

## 2. The two sectors precede the half-planes

For a nonreal spectral parameter \(z\), let

\[
 \mathcal N_z=\ker(S^*-z)
\]

be the deficiency space and let

\[
 L_z=\Gamma\mathcal N_z
\]

be its Cauchy-data image in boundary phase space.

The two primary analytic sectors are

\[
 \mathcal N_+
 =\{\mathcal N_z:\operatorname{Im}z>0\},
 \qquad
 \mathcal N_-
 =\{\mathcal N_z:\operatorname{Im}z<0\}.
\]

Their visible upper and lower half-planes are parameter spaces of these
sector families, not the sectors themselves. In the Riemann coordinate

\[
 s=\tfrac12+iz,
\]

the real \(z\)-axis projects to

\[
 \operatorname{Re}s=\tfrac12.
\]

Thus the critical line is the scalar shadow of the common boundary between
the two deficiency polarizations.

## 3. Exact forbidden-incidence theorem

**Theorem.** Let \(L_{\mathrm{src}}\) define a self-adjoint extension
\(S_{L_{\mathrm{src}}}\). Then

\[
 L_z\cap L_{\mathrm{src}}=\{0\}
\]

for every \(z\notin\mathbb R\).

Indeed, if \(u\in\mathcal N_z\) and \(\Gamma u\in L_{\mathrm{src}}\), then
\(u\) lies in the self-adjoint extension domain and

\[
 S_{L_{\mathrm{src}}}u=zu.
\]

Green's identity with \(v=u\) gives

\[
 (z-\bar z)\|u\|^2
 =\Omega(\Gamma u,\Gamma u)=0,
\]

because the boundary condition is isotropic. Since \(z\notin\mathbb R\),
\(u=0\).

Therefore

\[
\boxed{
\text{a maximal self-adjoint Lagrangian boundary cannot meet either
nonreal deficiency sector}.}
\]

This is the precise form of an “impossible trajectory into zero.” It is a
forbidden incidence in a static phase space, not temporal motion.

## 4. Determinant shadow

Suppose the completed source comparison has a determinant section

\[
 \Delta(z)
\]

whose vanishing is equivalent to nontransversality:

\[
 \Delta(z)=0
 \quad\Longleftrightarrow\quad
 L_z\cap L_{\mathrm{src}}\ne0.
\]

If the source construction also proves

\[
 \Delta(z)=U(z)X(z),
 \qquad
 X(z)=\xi(\tfrac12+iz),
\]

for a nowhere-zero source unit \(U\), then the forbidden-incidence theorem
implies that every zero of \(X\) has real \(z\), hence RH.

The theorem supplying the critical-line geometry is already elementary once
these typings are earned. The hard work is constructing \(S\),
\(L_{\mathrm{src}}\), and the determinant comparison before zero data.

## 5. Where integrality may enter

At every finite place, the unramified vacuum

\[
 \mathbf1_{\mathbb Z_p}
\]

is selected by a self-dual integral lattice. Globally, the rational diagonal

\[
 \mathbb Q\hookrightarrow\mathbb A_{\mathbb Q}
\]

is self-annihilating under the adelic additive pairing.

This suggests that the arithmetic boundary condition is not chosen from an
arbitrary unitary family. It may be the closure of a primitive integral
self-annihilating relation

\[
 \Lambda_{\mathbb Q}
 \subset\mathcal B_{\mathbb A}\oplus\mathcal B_{\mathbb A}.
\]

In finite-dimensional symplectic algebra, a primitive self-annihilating
lattice spans a Lagrangian subspace. In the present infinite-dimensional
setting, source integrality could therefore provide:

1. isotropy from the global product formula;
2. maximality from self-duality of the rational boundary; and
3. domain closure from adelic restricted-product completeness.

This is the precise content that the operator's “violation of integrality”
intuition may be pointing toward. An off-line zero would be a nonreal
deficiency vector compatible with a supposedly self-dual integral boundary,
contradicting maximal self-adjoint descent.

These three analytic implications are conjectural and must not be inferred
from the words “self-dual lattice” alone.

## 6. Why the scalar hostile models are irrelevant to this theorem

A reciprocal scalar multiplier can preserve

\[
 X(z)=X(-z)=\overline{X(\bar z)}
\]

while adding nonreal zeros. It modifies the determinant section without
supplying a new primitive integral Lagrangian boundary relation.

Thus it preserves the projected symmetry but not necessarily the source
incidence geometry. The correct hostile test is not whether the multiplier
looks modular. It is whether it lifts to an automorphism or authorized
modification of

\[
 (S,\Lambda_{\mathbb Q},\Omega).
\]

If it has no such lift, its off-line zeros do not challenge the
forbidden-incidence mechanism. If it does lift while preserving maximal
self-adjointness, the conjecture fails.

## 7. Categorical formulation

The two sectors may be described as complementary localizations or
polarizations

\[
 \mathcal C_+,\qquad\mathcal C_-,
\]

inside one adelic boundary category. Their boundary-value functors land in
the two deficiency sectors, while the rational diagonal supplies a descent
object

\[
 \mathcal L_{\mathbb Q}.
\]

The scalar determinant is a decategorified intersection section:

\[
 X(z)
 =\det_{\mathrm{rel}}(L_z,L_{\mathbb Q})
\]

up to a source unit.

The half-planes are therefore shadows of the two localizations, and zeros are
shadows of intersections. RH becomes a descent/transversality theorem:

\[
\boxed{
\text{the integral descent object intersects the character Cauchy family
only on the fixed seam}.}
\]

## 8. Deutsch--Popperian conjecture

**Adelic Lagrangian descent conjecture.** The minimal Euler--Dirac bulk and
the completed rational diagonal canonically determine a closed primitive
self-dual boundary relation \(L_{\mathbb Q}\). Its relative determinant is
\(X(z)\) up to a nowhere-zero source unit, and adelic self-duality makes the
relation maximal self-adjoint.

The conjecture has four independent gates:

1. **Construction:** derive the boundary trace and rational relation from the
   adelic Schwartz source.
2. **Isotropy:** derive vanishing of its Green flux from the product formula.
3. **Maximality:** prove that no boundary directions remain outside the
   rational relation and its symplectic complement.
4. **Determinant:** identify the relative determinant with \(X\) without
   using its divisor.

Passing only the determinant gate is tautological. Passing only isotropy
produces a symmetric operator with possible nonreal deficiency modes.

## 9. Smallest falsifiers

The programme fails if:

1. the rational boundary trace is not isotropic;
2. it is isotropic but has a nonzero symplectic complement quotient;
3. its closure depends on an unprescribed regulator;
4. its determinant acquires forbidden squarefree or higher-order
   archimedean factors;
5. a hostile off-line multiplier admits the same source boundary lift; or
6. determinant equality requires a posteriori zero information.

## 10. Next concrete calculation

Construct the finite-place boundary symplectic module for one prime \(p\)
from the pair of reciprocal scale characters and the self-dual lattice
\(\mathbb Z_p\). Compute the rational diagonal's annihilator and its local
Green flux. Then test restricted-product compatibility for two places
\(\{\infty,p\}\) before taking an all-place limit.

The desired local statement is not positivity. It is the exact equality

\[
 L_{\mathbb Q,p}=L_{\mathbb Q,p}^{\perp_\Omega}
\]

with the correct integral topology and variance.

## 11. Scope

The abstract boundary-phase-space theorem and forbidden nonreal incidence for
self-adjoint Lagrangian conditions are exact. The identification of
half-planes with deficiency-sector parameter spaces is standard operator
geometry. The adelic integral boundary construction, its maximality,
determinant comparison with \(X\), and RH conclusion remain conjectural.
