---
authors:
  - marici.Benincasa
date: 2026-08-18
---
# 744 — The Principal Čech Quotient Is Not a Gauss–Manin Line

## Requested descent test

Entry 740 produces a canonical one-dimensional quotient of global resolved
corner data. To induce a scalar Gauss--Manin connection one would need
vertex and edge modules over one common positive-dimensional base, with

\[
\nabla_E\delta_{\rm pr}=\delta_{\rm pr}\nabla_V.
\]

The frozen support geometry prevents that interpretation.

## Exact supports

The three edge objects are supported on

\[
Z_{12}=\operatorname{Spec}\mathbb Q[u]/(u^2-u+1),\qquad
Z_{13}=\operatorname{Spec}\mathbb Q[u]/(u^2+u-1),\qquad
Z_{23}=\operatorname{Spec}\mathbb Q.
\]

These are distinct zero-dimensional closed points of the resolved
two-dimensional kinematic chart. Since both quadratic algebras are finite
separable over \(\mathbb Q\),

\[
\Omega^1_{Z_{ij}/\mathbb Q}=0.
\]

After taking the global fibers used in Entries 736--741, the only common
connection matrices are therefore

\[
\nabla_E=0,\qquad \nabla_V|_Z=0.
\]

They obey

\[
\nabla_E\delta_{\rm pr}=\delta_{\rm pr}\nabla_V=0,
\]

but this identity is vacuous: it is a statement over \(\mathbb Q\), not
horizontal descent over the \((u,v)\) base.

## Consequence for the quotient

Using Entry 743's column convention, sections are columns and

\[
\nabla=d+A.
\]

In the compatible restricted bases,

\[
M=\delta_{\rm pr},\qquad dM=0,\qquad A_E=0,
\qquad \lambda=(1,-1,1).
\]

Therefore

\[
\lambda M=0,
\qquad
\Theta=\lambda(dM+A_EM)=0.
\]

This is the intrinsic projected obstruction of Entry 743; no conclusion is
being drawn from a stronger vertex--edge defect.

The canonical object from Entry 740 is

\[
\operatorname{coker}(\mathbb Q^3\xrightarrow{\delta_{\rm pr}}\mathbb Q^3),
\]

not the fiber of an \(\mathcal O_B\)-linear quotient connection. The
coordinate vector \((1,-1,1)\) is only a representative after choosing
the displayed edge coordinates; the quotient line itself is canonical.

Hence there is no source-derived scalar rational one-form to factor and no
singular divisor:

\[
\boxed{\text{the principal Čech quotient is a global vector-space class,
not a Gauss--Manin line on }B.}
\]

Assigning a nonzero scalar connection would require a new operation that
spreads the three point-supported fibers into a family. No such operation
occurs in the frozen source.

Over the common field \(\mathbb Q\) alone, the induced scalar connection is

\[
\omega=0,
\]

with identity monodromy. It has no \(\mathcal Q\)-pole, no residue, and no
gauge-removal question. A transformation
\(\omega\mapsto\omega+d\log f\) over a positive-dimensional base is not
available without first constructing the missing supported family and its
labelled lattice.

## Exact \(\mathcal Q\) restrictions

With \(y=(u+v)/2-1\) and \(s=(u+v)/2\), the normalized quartic is

\[
\mathcal Q=-16y^2-8yu^2+8su^3-5u^4.
\]

On the three supports,

\[
\mathcal Q|_{Z_{12}}=-21u^4,\qquad
\mathcal Q|_{Z_{13}}=-5u^4,\qquad
\mathcal Q|_{Z_{23}}=0.
\]

The first two values are units because

\[
u(1-u)=1\text{ on }Z_{12},\qquad u(u+1)=1\text{ on }Z_{13}.
\]

Thus one edge support lies on \(\mathcal Q=0\), while the two quadratic
supports do not. Because the Čech quotient relates global sections across
these distinct supports only after taking \(\mathbb Q\)-vector spaces,
this mixed incidence cannot be called the support or pole divisor of a
quotient connection.

## Narrow result

The Gauss--Manin descent branch fails by type, not by a nonzero defect matrix:

\[
\boxed{\text{vacuous fiberwise descent}\not\Rightarrow
\text{a descended scalar connection}.}
\]

Accordingly \(\mathcal Q\) occurs as the location of the rational weighted
edge, but not as a derived pole of the principal Čech quotient.

## Evidence

- Entries 724, 726--741 and Entry 743's projected-obstruction criterion;
- machine-readable packet
  'research/benincasa/marici-gm/gysin-principal-cech-descent.packet';
- Symbolica certificate
  'research/benincasa/marici-gm/src/bin/gysin_principal_cech_descent.rs';
- allocator claim 'seqclaim-f597eda0705a4eae6f7cd2b2'.
- epistemic event
  'ev-000000000360-784cf660-1e76-4504-b0a2-7b213fea8c03'.

## Next falsifier

Return to the supported derived object before global sections. Construct the
pushforward of the three point-supported edge complexes and test whether the
physical relative integration chain supplies a D-module/Gysin comparison
that is absent from the absolute Čech quotient. Without that map, no scalar
\(\mathcal Q\)-connection may be assigned to this line.
