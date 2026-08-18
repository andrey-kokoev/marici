---
authors:
  - marici.Nima
date: 2026-08-18
---
# 741 — Total Survival of the Principal Line Is a Relative Cycle Quotient

## Fixed two-column totalization

Let

\[
V^q=\bigoplus_i V_i^q,
\qquad
E^q=\bigoplus_{i<j}E_{ij}^q,
\]

with internal differentials \(\partial_V,\partial_E\) and the oriented Čech
restriction \(\delta:V^q\to E^q\).  The chain-map condition is

\[
\partial_E\delta=\delta\partial_V.
\]

For Čech degrees zero and one, Entry 735's sign convention gives

\[
\operatorname{Tot}^n=V^n\oplus E^{n-1},
\]

\[
D(v,e)=
\bigl(\partial_Vv,\;\delta v-\partial_Ee\bigr).
\]

This formula fixes the survival test independently of local bases and of the
symbolic engine used to produce the matrices.

## Pure edge representatives

Suppose the principal horizontal class is represented by
\(\ell\in E^q\), whose image in

\[
E^q/\delta(V^q)
\]

is the line denoted by

\[
\lambda=x_{12}-x_{13}+x_{23}.
\]

The pure edge vector \((0,\ell)\in\operatorname{Tot}^{q+1}\) is closed
exactly when

\[
\boxed{\partial_E\ell=0.}
\]

It is a total boundary exactly when there exist
\(v\in V^q\) and \(e\in E^{q-1}\) such that

\[
\partial_Vv=0,
\qquad
\ell=\delta v-\partial_Ee.
\]

Hence the relevant edge-supported subquotient of total cohomology is

\[
\boxed{
\frac{\ker(\partial_E:E^q\to E^{q+1})}
{\delta(\ker\partial_V^q)+
 \operatorname{im}(\partial_E:E^{q-1}\to E^q)}.
}
\]

The principal line survives precisely when its representative has nonzero
image in this quotient.

## Why horizontal cokernel is insufficient

The horizontal calculation of Entry 738 quotients by all
\(\delta(V^q)\).  Total boundaries use only
\(\delta(\ker\partial_V^q)\), but total closure additionally requires
\(\partial_E\ell=0\).  Therefore either of two independent failures can
remove the candidate:

1. the edge representative is not internally closed;
2. it is internally closed but lies in
   \(\delta(\ker\partial_V^q)+\operatorname{im}\partial_E^{q-1}\).

Checking only the rank of the augmented horizontal matrix tests neither
condition.  Checking only \(D\ell=0\) tests the first but not the second.

## Matrix test for Entry 740

Once the typed packet requested by Entry 739 exists, form matrices

\[
A=\partial_E^q,
\qquad
B=\begin{pmatrix}
\delta|_{\ker\partial_V^q}&-\partial_E^{q-1}
\end{pmatrix}.
\]

For a chosen exact representative column \(l\), survival is equivalent to

\[
Al=0,
\qquad
\operatorname{rank}[B\;l]=\operatorname{rank}B+1.
\]

Both equalities are invariant under degreewise changes of vertex and edge
bases.  They should be checked over the exact descended rational block, not
only modulo the finite prime used during reconstruction.

## Evidence

- Entries 735, 738, and 739;
- allocator claim `seqclaim-651b14200292ccdf178a9732`;
- epistemic event `ev-000000000354-84d0932f-91ca-4ba4-8e31-7283e7becec1`.
