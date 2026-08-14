# Flow Torsors and the Harmonic Defect of Cut Naturality

## Record

Date: 2026-08-13

Status: exact homological theorem, followed by a conditional identification of
the common NLSM/YM transport primitive.

Forward refinement: entry 64 proves that at six points the strongest bridge is
the Mayer--Vietoris suspension.  The flow torsor controls the choice of each
local QTDS primitive; the difference of the two polarity primitives is then
transgressed canonically to a Ward cycle.  Thus shared divergence resolution
and polarity-to-Ward transgression are related but distinct operations.

Entry 62 identified the same discrete Green-current formula in the six-point
QTDS polarity flow and the marked-theta Ward circuit resolution.  The correct
invariant is one categorical level above that formula:

\[
\boxed{
\operatorname{Flow}_{K}(c)
=
\operatorname{hofib}_{c}
\bigl(\bar\partial:C_1(K)/B_1(K)
\longrightarrow B_0(K)\bigr).}
\]

It is the derived space of currents with prescribed divergence.  A Green
operator chooses one point in this space after imposing a metric and a gauge.
The flow object is integral and functorial; the chosen Green point generally
is neither.

The proposed common scalar-master primitive should therefore be called
**derived divergence resolution**, or a **flow torsor**, rather than an
inverse-Laplacian operator.

## Canonical flow extension

Let \(K\) be a finite connected cellular complex over a commutative coefficient
ring \(R\).  Write

\[
B_i(K)=\operatorname{im}\partial_{i+1},
\qquad
Z_i(K)=\ker\partial_i.
\]

For a realizable zero-chain source \(c\in B_0(K)\), define

\[
\operatorname{Flow}_K(c)
=
\{j\in C_1(K):\partial j=c\}/B_1(K).
\]

If \(j\) and \(j'\) solve the same boundary equation, then
\(j-j'\in Z_1(K)\).  Quotienting by \(B_1(K)\) therefore gives a free and
transitive action of \(H_1(K)\).  Equivalently, every source is the fiber of
the canonical exact sequence

\[
\boxed{
0\longrightarrow H_1(K;R)
\longrightarrow C_1(K;R)/B_1(K;R)
\xrightarrow{\ \bar\partial\ }
B_0(K;R)
\longrightarrow0.}
\]

Thus \(\operatorname{Flow}_K(c)\) is an \(H_1(K;R)\)-torsor.  There is no
preferred current unless additional data trivialize this torsor.

This theorem separates three objects that had been partially conflated:

1. the source \(c\);
2. the integral derived fiber \(\operatorname{Flow}_K(c)\);
3. a chosen representative such as the Green current.

## Strict functoriality exists before choosing a section

For a cellular chain map \(f:C_*(K)\to C_*(L)\),

\[
[j]\longmapsto[f_1j]
\]

defines a canonical map

\[
\operatorname{Flow}_K(c)
\longrightarrow
\operatorname{Flow}_L(f_0c).
\]

It is strictly compatible with composition.  Hence divergence resolution is
already functorial at the torsor level.  No Green function, spanning tree, or
basepoint is required.

This is the form in which the operation could be Cut natural.  The word
"could" remains necessary because the actual scalar QTDS and first-jet Ward
coefficient maps into a common cellular complex have not yet both been
constructed.

## Green sections and their harmonic defect

Over \(\mathbb Q\) or \(\mathbb R\), choose cellular inner products.  Let

\[
\delta=\partial^\dagger,
\qquad
\Delta_0=\partial\delta.
\]

On \(B_0(K)\), the Green operator gives the orthogonal or minimum-norm
section

\[
s_K^{G}=\delta\Delta_0^{-1}.
\]

For a chain map \(f:K\to L\), define its Green-section defect by

\[
\boxed{
\kappa_f(c)
=
\bigl[f_1s_K^{G}(c)-s_L^{G}(f_0c)\bigr]
\in H_1(L;\mathbb Q).}
\]

Its boundary vanishes identically:

\[
\partial\kappa_f(c)=f_0c-f_0c=0.
\]

Modulo cellular boundaries it is therefore a harmonic class.  It is not an
error term in the flow construction.  It measures the failure of two chosen
torsor trivializations to be natural.

For composable maps
\(K\xrightarrow{f}L\xrightarrow{g}M\), the defects obey

\[
\boxed{
\kappa_{g f}(c)
=
g_*\kappa_f(c)+\kappa_g(f_0c).}
\]

Changing sections by homology-valued maps

\[
s'_K=s_K+a_K
\]

changes the defect by

\[
\kappa'_f
=
\kappa_f+f_*a_K-a_Lf_0.
\]

Consequently the family \(\kappa\) is a categorical one-cocycle, and its
class is the obstruction to a natural strictification.  Higher sewing-order
curvatures are the next coherences of this same descent problem.

## When strict Green naturality is expected

The Green section commutes strictly with \(f\) only when the map preserves the
chosen Hodge splitting.  A sufficient condition is compatibility with the
inner products, adjoints, and Laplacians.  An arbitrary deletion, Cut, or
factorization map need not have this property.

If \(H_1(L)=0\), the torsor has no harmonic ambiguity and every defect class
vanishes.  More generally, equality after a scalar or physical augmentation
can kill \(\kappa_f\) without making it zero in the resolved carrier.

Therefore:

- zero final curvature is expected after an augmentation that forgets closed
  circuits;
- nonzero resolved harmonic curvature is not automatically an anomaly;
- only a nonzero class that cannot be filled in the admitted cyclic/Cut
  complex is a genuine obstruction.

This gives the precise interpretation of the earlier marked-theta result:
strict equality of the closed scalar polynomial does not decide whether the
unaugmented Ward--Brauer dictionary is strict or merely coherent.

## The road polygon as the universal example

For the oriented road cycle \(C_m\),

\[
C_1(C_m;\mathbb Z)=\mathbb Z^m_{\rm tags},
\qquad
B_0(C_m;\mathbb Z)=A_{m-1},
\qquad
H_1(C_m;\mathbb Z)=\mathbb Z.
\]

The canonical flow extension becomes exactly the all-arity circuit resolution
of entry 61:

\[
0\longrightarrow\mathbb Z
\xrightarrow{1\mapsto(1,\ldots,1)}
\mathbb Z^m_{\rm tags}
\xrightarrow{\partial}
A_{m-1}
\longrightarrow0.
\]

Integral solutions exist because \(\partial\) is surjective, but choosing one
breaks cyclic symmetry.  The Green section subtracts the mean circulation.  A
universal denominator \(m\) appears, and the obstruction to an integral
gradient representative is

\[
\operatorname{Jac}(C_m)
=
\operatorname{Div}^0(C_m)/\Delta C_0(C_m)
\cong\mathbb Z/m.
\]

This must be stated carefully: the Jacobian does not obstruct arbitrary
integral flows.  It obstructs the symmetric zero-circulation or gradient
choice represented by the Green section.

Adjoining an oriented polygon cell \(P_m\) kills the diagonal cycle:

\[
\partial P_m=t_0+\cdots+t_{m-1}.
\]

Then \(H_1\) vanishes and the flow torsor becomes canonically contractible in
the derived quotient.  This is why retaining the relation cell is better than
dividing by \(m\).

## Consequence for the NLSM--YM comparison

At six points the QTDS polarity source

\[
c_i=\frac{N_i^+-N_i^-}{X_i},
\qquad
\sum_i c_i=0,
\]

and the marked-theta Ward circuit source both live abstractly in an
\(A_2\) module.  In both calculations the displayed rational current is the
Green section for \(C_3\):

\[
\delta\Delta^{-1}:A_2\otimes\mathbb Q
\longrightarrow C_1(C_3;\mathbb Q).
\]

This proves equality of the transport grammar.  It does not yet identify the
physical source maps.  A genuine common operation requires a diagram

\[
\begin{matrix}
\mathcal C_{\rm QTDS}^{\rm source}&\longrightarrow&A_2\\
\downarrow&&\downarrow\\
\mathcal C_{\rm Ward}^{\rm source}&\longrightarrow&A_2\otimes\chi
\end{matrix}
\]

that fixes:

1. the map between scalar contact coefficients and first-jet Ward
   coefficients;
2. the identification of polarity deck reversal with the Ward orientation
   local system;
3. the lift of the polygon relation cell;
4. one physical Cut square.

Without these data, any isomorphism between the two rank-two lattices is a
choice of basis, not a scalar-derived comparison.

## Revised primitive

Replace the provisional formula

\[
\operatorname{HodgeTransfer}_{K}(c)=\delta_K\Delta_K^{-1}c
\]

by the derived operation

\[
\boxed{
\operatorname{ResolveDiv}_{K}(c)
=
\left[C_1(K)/B_1(K)
\xrightarrow{\bar\partial}
B_0(K)ight]_c.}
\]

The Green formula is a rational presentation of
\(\operatorname{ResolveDiv}\), not its definition.  The candidate NLSM/YM
commonality is now:

\[
\begin{aligned}
\operatorname{gr}_R\mathrm{Scalar}
&\longrightarrow
\operatorname{ResolveDiv}_{\mathcal K_{\rm QTDS}},\\
H_{\rm gauge}J_F^1\mathrm{Scalar}
&\longrightarrow
\operatorname{ResolveDiv}_{\mathcal K_{\rm Ward}}.
\end{aligned}
\]

The two complexes need not be identical.  They must be related by a
factorization-natural chain comparison carrying sources, orientation systems,
and relation cells.

## Decision and next falsifier

Promote as exact:

> Prescribed-divergence transport is canonically a homology torsor, and any
> Green-section failure of Cut naturality is necessarily a harmonic cocycle.

Promote as a strong hypothesis:

> Derived divergence resolution is a common transport primitive used by both
> the scalar rank-jump/Jordan sector and the scalar first-jet/Ward sector.

The next falsifier is the typed \(m=3\) coefficient comparison.  It must do
more than recognize the same triangle Laplacian: it must construct the two
source maps, match their symmetry characters, lift the relation cell, and
commute with one already defined physical Cut.  Failure at any of these points
separates the two flow torsors despite their identical abstract incidence
matrices.

## Internal dependencies

- Entries 19--24: QTDS polarity flow and scalar contact transport.
- Entries 57 and 59--62: Ward homology, circuit tags, road polygons, and the
  Green/Jacobian calculation.
- `research/nima/ward_brauer_math_context.md`: persistent mathematical
  context.
