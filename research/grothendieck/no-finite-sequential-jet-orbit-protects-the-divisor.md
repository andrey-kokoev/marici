# No finite sequential jet orbit protects the divisor

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact hostile interpolation theorem

## Question

The first-jet arrow functor remembers multiplication and flux transport but
does not constrain the distinguished scalar section. Can a finite sequential
orbit of higher jets repair that loss?

It cannot.

## Construction

Fix finitely many real probe points (x_1,\ldots,x_m), prescribed jet depths
(r_1,\ldots,r_m), and the completion endpoints (\pm1/2). Define a real
even polynomial

\[
V(z)=
(z^2-1/4)^R
\prod_{j=1}^{m}(z^2-x_j^2)^{r_j+1},
\]

where (R\ge1) is as large as the endpoint normalization requires.

Choose a desired hostile point

\[
w=\alpha+i\beta,
\qquad
\alpha\beta\ne0,
\]

away from the probe set. Since

\[
\operatorname{Im}(w^2)=2\alpha\beta\ne0,
\]

the real vectors (1) and (w^2) form a basis of the complex plane. There
are therefore unique real numbers (a,b) satisfying

\[
a+bw^2=-\frac1{V(w)}.
\]

Set

\[
H(z)=1+V(z)(a+bz^2).
\]

Then (H) is real and even, (H(w)=0), and reality plus parity supplies the
quartet (\pm w,\pm\bar w). At every probe (x_j),

\[
H(z)-1=O((z-x_j)^{r_j+1}),
\]

and similarly at (-x_j). The completion endpoints remain normalized.

## Consequence for a distinguished section

For any analytic section (F), the hostile section (F_H=HF) has exactly the
same jets as (F) through the prescribed finite depths at every probe:

\[
F_H^{(k)}(\pm x_j)=F^{(k)}(\pm x_j),
\qquad 0\le k\le r_j.
\]

Yet (F_H) contains the inserted off-seam zero quartet. Thus no finite
sequential jet history, no matter how deep or how many real probes it uses,
protects the divisor.

This theorem strengthens the earlier first-jet hostile multiplier. The defect
is not insufficient jet order. It is finite observation of an infinite source
law.

## What survives

The next invariant must constrain an entire function-valued orbit, not a
finite jet packet. Viable forms include:

1. the complete labelled theta translate recurrence;
2. a source-generated differential or difference equation with rigid global
   solution space;
3. an infinite conservation law whose domain includes the endpoint currents;
4. a uniqueness theorem for the completed source state under all authorized
   constructors.

Merely adding a sixth observer or another finite wall cannot work.

## Falsifier and verification

The theorem would fail if the real interpolation equations for (a,b) became
singular at a genuine off-axis point, or if the constructed multiplier failed
to preserve one requested jet. The determinant of the interpolation system is

\[
\operatorname{Im}(w^2)=2\alpha\beta,
\]

so singularity occurs only when the proposed zero lies on one of the two axes.
The exact checker verifies a nontrivial degree-26 example with three probes,
second jets, endpoint normalization, and the full hostile quartet.
