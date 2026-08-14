# Road-Polygon Hodge Resolution and the Common Transfer Operation

## Record

Date: 2026-08-13

Status: the all-\(m\) circuit resolution of entry 61 is exactly the augmented
cellular chain complex of the oriented road polygon \(C_m\).  Its canonical
rational split is the discrete Green current, and its integral obstruction is
the graph Jacobian

\[
\operatorname{Jac}(C_m)\cong\mathbb Z/m.
\]

This identifies the denominator-\(m\) phenomenon, the three-tag marked-theta
relation, and the earlier inverse-Laplacian QTDS contact flow as instances of
one discrete Hodge-transfer pattern.

The mathematical identification is exact.  The claim that this Hodge transfer
is a primitive scalar-master operation common to NLSM and YM is a strong
inference and a new falsification target.

Forward correction: entry 63 identifies the invariant primitive as the
integral flow torsor, or derived fiber of the cellular boundary map.  The
Green current below is its rational zero-circulation section, not the
primitive operation itself.

## The circuit resolution is a cellular chain complex

Let \(C_m\) be the oriented cycle whose vertices are the \(m\) road labels
and whose oriented edges are the adjacent-road tags \(t_i\).  Its cellular
groups are

\[
C_1(C_m;\mathbb Z)=\mathbb Z^m_{\rm tags},
\qquad
C_0(C_m;\mathbb Z)=\mathbb Z^m_{\rm roads},
\]

with boundary

\[
\partial t_i=e_i-e_{i+1}.
\]

The reduced zero-chains are

\[
\widetilde C_0(C_m;\mathbb Z)
=
\left\{
a\in\mathbb Z^m:\sum_i a_i=0
\right\}
\cong A_{m-1}.
\]

Therefore the exact sequence of entry 61 is simply

\[
\boxed{
0\longrightarrow H_1(C_m;\mathbb Z)
\longrightarrow C_1(C_m;\mathbb Z)
\xrightarrow{\partial}
\widetilde C_0(C_m;\mathbb Z)
\longrightarrow0.}
\]

Under the graph-homology identification

\[
\widetilde C_0(C_m)
\cong
H_1(K_{2,m}),
\]

the Ward circuit tags are the polygon edges and their diagonal relation is
the fundamental cycle of \(C_m\).

Adjoining one oriented \(m\)-gon cell \(P_m\) with

\[
\partial P_m=t_0+\cdots+t_{m-1}
\]

gives the minimal free cellular resolution of the additive Ward sector.  For
\(m=3\), this is the triangle relation of entries 59--60.  It has the same
cell shape as a Farey \(3S\) triangle, but an identification with the physical
pants-complex cell still requires an incidence map.

## The Green-current section

Let

\[
\delta=\partial^{T}:C_0(C_m)\longrightarrow C_1(C_m)
\]

be the cellular coboundary and

\[
\Delta=\partial\delta
\]

the graph Laplacian on road zero-chains.  On the rational reduced subspace,
\(\Delta\) is invertible.  The unique rotation-equivariant, sum-zero section
of \(\partial\) is

\[
\boxed{
\sigma_{\mathbb Q}
=
\delta\,\Delta^{-1}:
\widetilde C_0(C_m;\mathbb Q)
\longrightarrow
C_1(C_m;\mathbb Q).}
\]

Indeed,

\[
\partial\sigma_{\mathbb Q}
=
\partial\delta\Delta^{-1}
=1
\]

on reduced zero-chains.  This is precisely a discrete Green current solving a
prescribed divergence with the constant zero mode removed.

For \(m=3\), the numerator of this formula is

\[
(p-q,\ p+2q,\ -2p-q),
\]

divided by three, agreeing with the exact marked-theta audit.

## The integral obstruction is the graph Jacobian

The sum-zero edge lattice satisfies

\[
\widetilde C_1(C_m)
=
\ker\left(\sum_i:C_1\to\mathbb Z\right)
=
\operatorname{im}\delta.
\]

Consequently

\[
\partial\widetilde C_1
=
\partial\delta C_0
=
\Delta C_0.
\]

The index-\(m\) quotient of entry 61 is therefore

\[
\boxed{
\frac{\widetilde C_0(C_m)}
{\partial\widetilde C_1(C_m)}
=
\frac{\operatorname{Div}^0(C_m)}
{\Delta C_0(C_m)}
=
\operatorname{Jac}(C_m)
\cong\mathbb Z/m.}
\]

Thus the denominator is not caused by a poor basis or arbitrary averaging.
It is the critical/sandpile group of the road cycle.  Insisting on a symmetric
section asks the Green operator to invert this finite integral obstruction.
Retaining the cellular resolution avoids that demand.

## Link to the earlier QTDS transfer

The six-point QTDS construction used a triangle carrier with a contact vector

\[
c=(c_1,c_2,c_3),
\qquad
\sum_i c_i=0,
\]

and solved for an edge flow whose boundary is \(c\).  That was also an
inverse-Laplacian problem on a three-cycle.  The present Ward calculation has
the same grammar:

\[
\text{source/contact zero-chain}
\xrightarrow{\ \Delta^{-1}\ }
\text{potential}
\xrightarrow{\ \delta\ }
\text{transport current}.
\]

The two applications differ in their physical coefficient systems:

- QTDS uses scalar rank-jump contact redistribution and Jordan polarity;
- YM uses first-jet Ward/contact transport and oriented circuit states.

But both require:

1. a compatibility graph or cell complex;
2. a zero-sum source;
3. removal of the constant mode;
4. a Green current;
5. retention of an integral cellular resolution when equivariant division is
   unavailable.

This suggests a candidate primitive operation of the scalar master:

\[
\boxed{
\operatorname{HodgeTransfer}_{\mathcal K}
(c)
=
\delta_{\mathcal K}
\Delta_{\mathcal K}^{-1}c,}
\]

understood derived-integrally as a cellular resolution and only rationally as
an inverse Laplacian.

## Revised operation picture

The NLSM and YM sectors remain different normal extractions:

\[
\operatorname{gr}_R
\qquad\text{versus}\qquad
H_{\rm gauge}J_F^1.
\]

What may be common is the mechanism that turns local source defects into
factorization-natural transport:

\[
\begin{matrix}
\operatorname{gr}_R\mathrm{Scalar}
&\xrightarrow{\text{contact source}}&
\operatorname{HodgeTransfer}
&\xrightarrow{}&
\text{QTDS/Jordan current},
\\
J_F^1\mathrm{Scalar}
&\xrightarrow{\text{Ward source}}&
\operatorname{HodgeTransfer}
&\xrightarrow{}&
\text{Ward--circuit current}.
\end{matrix}
\]

This is stronger and more precise than saying both calculations use a
Laplacian.  The proposed common datum is the integral cellular resolution
together with its zero-mode, symmetry character, and Cut-natural boundary
map.  A Green function is a presentation of its rational contraction, not the
fundamental object.

## Evidence boundary

Proved mathematically:

- the road-polygon cellular identification;
- the Green-current formula for the unique rational equivariant section;
- the Jacobian/critical-group interpretation of the \(\mathbb Z/m\)
  obstruction;
- the \(m=3\) agreement with the exact circuit certificate.

Established earlier:

- the six-point QTDS triangle flow is an inverse-Laplacian contact
  redistribution.

Strong inference:

- both are realizations of one scalar-derived
  \(\operatorname{HodgeTransfer}\) operation.

Not proved:

- a common chain functor producing both coefficient systems;
- compatibility of \(\operatorname{HodgeTransfer}\) with arbitrary Cut;
- the all-arity QTDS carrier as the same road-polygon family;
- a scalar-derived \(K_{2,4}\) Ward coefficient map;
- identification of the triangle polygon cell with the physical \(3S\) cell.

## Next falsifier

Build one typed comparison square at \(m=3\):

\[
\begin{matrix}
\text{scalar QTDS contact complex}
&\longrightarrow&
C_*(C_3)
\\
\downarrow&&\downarrow
\\
\text{scalar first-jet Ward complex}
&\longrightarrow&
C_*(C_3;\chi_{\rm rel}).
\end{matrix}
\]

Both horizontal maps must produce their already verified currents, and the
vertical comparison must commute with one physical Cut.  If the two source
vectors or orientation systems cannot be related without adding external
data, then the common-Hodge-operation hypothesis is false even though the
two lattice calculations remain valid.

## Internal dependencies

- Entries 19--24: six- and eight-point QTDS inverse-Laplacian transport.
- Entries 57 and 59--61: Ward graph homology and circuit resolutions.
- Working context: research/nima/ward_brauer_math_context.md.
