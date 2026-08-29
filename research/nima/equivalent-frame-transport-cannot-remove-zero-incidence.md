# Equivalent frame transport cannot remove zero incidence

## Setup

Let \(V_X\) and \(V_Y\) be two-dimensional boundary carriers.  Each has a
distinguished endpoint line \(\ell_X\), \(\ell_Y\) and a source-fixed framed
state \(e_X\), \(e_Y\).  A zero is the incidence

\[
e_X\in\ell_X.
\]

Suppose a transport \(T:V_X\to V_Y\) is invertible and preserves both typed
objects:

\[
T(\ell_X)=\ell_Y,
\qquad
T(e_X)=a e_Y,
\qquad
a\ne0.
\]

Then

\[
e_X\in\ell_X
\quad\Longleftrightarrow\quad
e_Y\in\ell_Y.
\]

The scalar \(a\) may carry a determinant-frame cocycle, but it cannot change
incidence while it remains nonzero.

## Categorical form

The zero object is the pullback of the framed-state map and the endpoint-line
inclusion.  An equivalence preserves that pullback.  Hence an equivalence-based
coherencer can transport, type, and orient the divisor, but it cannot delete a
divisor point.

This separates two claims:

1. source-fixed framing prevents projective type erasure;
2. frame-preserving equivalence does not confine zeros.

The first is genuine provenance.  The second is a no-go theorem for using
finite invertible descent as the missing RH mechanism.

## Completion consequence

If finite reciprocal sources contain off-seam incidences while the completed
source does not, the completion map cannot be a conservative equivalence on
the incidence diagram.  At least one of the following must occur:

- zeros escape every fixed compact set;
- the frame transport becomes singular or unbounded;
- the endpoint object changes under completion;
- the completion functor fails to preserve the incidence pullback.

Locally uniform holomorphic convergence sharpens the first alternative.  By
Hurwitz's theorem, an isolated finite zero cannot simply disappear inside a
compact region where the nonzero limiting section is defined.  It must leave
the region, meet a singular degeneration, or be excluded by a source-specific
change of object.

## Finite falsifier

Use

\[
\ell=\operatorname{span}(0,1),
\qquad
e_0=(0,1),
\qquad
T=\begin{pmatrix}a&0\\b&c\end{pmatrix},
\qquad ac\ne0.
\]

Every invertible \(T\) preserving \(\ell\) maps \(e_0\) back into \(\ell\).
For a nonzero determinant value \(x\),

\[
\det\bigl(T(x,1),T(0,1)\bigr)=\det(T)x.
\]

Thus transport multiplies the Evans determinant by a unit and preserves its
zero locus.  Any claimed finite descent that removes a zero while satisfying
these hypotheses is algebraically impossible.

## Frontier

The missing constructor is not another invertible coherence cell.  It is a
source-authorized completion law whose controlled nonconservativity explains
why finite reciprocal incidences do not survive, while retaining the complete
theta/Tate boundary germ.  That law must identify its exact failure of
pullback preservation; otherwise it merely hides the zero-bearing datum.

