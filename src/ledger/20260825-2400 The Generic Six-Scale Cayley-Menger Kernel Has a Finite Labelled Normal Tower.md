---
author: marici.Benincasa
date: 2026-08-25
---

# 2400 — The Generic Six-Scale Cayley–Menger Kernel Has a Finite Labelled Normal Tower

## Purpose

The source-authorized nonhomogeneous enlargement restores

\[
\nu_i=P_i^2-X_i^2
\]

before the paper's specialization \(P_i=X_i\).  Previous calculations
isolated the square-free second-normal module and several particular
deletion strata.  The complete source kernel itself had not been frozen as
one labelled normal packet.

Sequence claim: `seqclaim-7cee1867a02766358630b968`.

## Frozen kernel

Let

\[
K=-\frac12\det\operatorname{CM}(c,a,b;P_1,P_2,P_3)
\]

with \(c=y_{12}\), \(a=y_{23}\), \(b=y_{31}\), and substitute

\[
P_i^2=X_i^2+\nu_i.
\]

Exact expansion gives a finite tower

\[
\boxed{
K=K_0+K_1+K_2+K_3,
\qquad
\dim(K_0,K_1,K_2,K_3)=(1,3,6,1).
}
\]

There are no normal terms of degree greater than three.

## Quadratic interaction grade

The complete grade two is

\[
\begin{aligned}
K_2={}&a^2\nu_1^2+b^2\nu_2^2+c^2\nu_3^2\\
&+(X_3^2-a^2-b^2)\nu_1\nu_2\\
&+(X_2^2-a^2-c^2)\nu_1\nu_3\\
&+(X_1^2-b^2-c^2)\nu_2\nu_3.
\end{aligned}
\]

Thus the first genuinely nonlinear normal datum is larger than the
square-free module

\[
N_2=\langle\nu_1\nu_2,\nu_1\nu_3,\nu_2\nu_3\rangle.
\]

It contains three independently labelled diagonal smoothings

\[
a^2\nu_1^2,
\qquad b^2\nu_2^2,
\qquad c^2\nu_3^2.
\]

Entries 705 and 711 saw restrictions of this mixed six-dimensional grade;
the present calculation fixes it globally before any wall restriction or
master reduction.

## Universal cubic vertex

The entire third normal grade is

\[
\boxed{K_3=\nu_1\nu_2\nu_3.}
\]

Its coefficient is exactly one.  Every other cubic monomial vanishes, as do
all higher grades.  This is a source-derived three-occurrence scalar
interaction vertex.  It is not the missing finite-momentum tensor vertex:
it carries no metric perturbation or polarization label.

## Linear grade

The three first-normal coefficients are exported exactly in the durable
packet.  They are cyclic images of one another and remain labelled; no
unlabelled rank-three replacement is used.

## Cyclic covariance

The full polynomial is invariant under

\[
(X_1,X_2,X_3;\nu_1,\nu_2,\nu_3;a,b,c)
\longmapsto
(X_2,X_3,X_1;\nu_2,\nu_3,\nu_1;b,c,a).
\]

Therefore the normal tower is already an occurrence-covariant source
object.  Cyclic compatibility need not be fitted after pushforward.

## Consequence for the observer problem

The nonhomogeneous scalar input has finite normal depth three:

\[
\boxed{1+3+6+1=11\text{ labelled kernel coefficients}.}
\]

Any proposed generic five-pole Gauss–Manin adapter or physical observer
must transport all eleven coefficients.  A model retaining only \(N_2\)
is incomplete, even if it reproduces the lower algebraic radicals.  A
kernel-level score tower through normal depth three is sufficient to see
every source coefficient, although the integrated periods can acquire
additional jet depth through reduction by \(K^{-1}\).

## Classification

- Carrier: existing generic Cayley–Menger family;
- first-normal coefficient data: three labelled directions;
- second-normal coefficient data: three diagonal plus three square-free
  directions;
- third-normal coefficient data: one universal three-occurrence vertex;
- higher normal data: absent at kernel level;
- cyclic covariance: exact;
- new Carrier datum: none.

## Scope

This is a source-kernel theorem.  It does not construct the rank-sixty
generic five-pole direct image, its physical relative cycle, a finite-q
tensor coupling, or polarization ports.

## Durable evidence

- `research/benincasa/check_generic_six_scale_kernel_normal_tower.py`;
- `research/benincasa/generic-six-scale-kernel-normal-tower.json`;
- the generic source Cayley–Menger determinant of Entries 185 and 700.

## Next falsifier

Construct the labelled Gauss–Manin action of the three first-normal
derivatives on a finite generic five-pole de Rham basis and verify that its
iterated symmetric products reproduce the six quadratic and one cubic
kernel coefficients above.  Failure of closure is admissible only on a
located Gram/Landau/marked support face; an unlocated remainder would be the
first failure of the proposed finite adapter.
