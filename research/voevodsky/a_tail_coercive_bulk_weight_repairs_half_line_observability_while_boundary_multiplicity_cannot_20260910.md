# A tail-coercive bulk weight repairs half-line observability while boundary multiplicity cannot

## Question

What explicit complementary observer restores the derivative-plus-endpoint lower bound on the half-line?

## Claim boundary

A bounded bulk multiplier uniformly nonzero beyond one finite radial cutoff restores graph-norm stability. Endpoint trace and derivative control the bounded radial segment; the multiplier controls the tail. Conversely, weights uniformly small on arbitrarily long remote intervals admit broad-packet counterexamples. This is a sufficient theorem and a sharp hostile condition, not a classification of all weights.

## Problem

On

\[
H^1(0,\infty),
\]

the observer

\[
f\longmapsto(f',f(0))
\]

is injective but not bounded below. Broad packets can have unit \(L^2\) norm, negligible derivative, and zero endpoint trace.

## Bold conjecture

Adding finitely many further endpoint or finite-jet traces can repair the missing half-line margin.

## Named rivals

1. A tail-coercive bulk multiplier repairs the margin.
2. Any nonzero decaying weight suffices.
3. Arbitrarily long low-weight intervals preserve the broad-packet obstruction.
4. Reciprocal doubling itself supplies the missing tail observation.

## Weighted observer

Let

\[
w\in L^\infty(0,\infty)
\]

and define

\[
Q_wf=(f',f(0),wf)
\]

with target

\[
L^2(0,\infty)\oplus\mathbb C\oplus L^2(0,\infty).
\]

Assume there exist \(R<\infty\) and \(c>0\) such that

\[
|w(r)|\ge c
\]

for almost every \(r\ge R\).

## Stability theorem

Under the tail-coercivity hypothesis, \(Q_w\) is bounded below on \(H^1(0,\infty)\).

### Proof

On the bounded segment, the endpoint estimate gives

\[
\int_0^R|f(r)|^2\,dr
\le
2R|f(0)|^2+R^2\|f'\|_{L^2(0,R)}^2.
\]

On the tail,

\[
\int_R^\infty|f(r)|^2\,dr
\le
c^{-2}\|wf\|_{L^2(R,\infty)}^2.
\]

Therefore

\[
\|f\|_{H^1(0,\infty)}^2
\le
2R|f(0)|^2+(R^2+1)\|f'\|^2+c^{-2}\|wf\|^2.
\]

With

\[
M_{R,c}=\max\{2R,R^2+1,c^{-2}\},
\]

we obtain

\[
\|Q_wf\|^2
\ge
M_{R,c}^{-1}\|f\|_{H^1}^2.
\]

Thus the added bulk channel restores a uniform graph-norm margin.

## Division of labor

The three components have distinct roles:

- \(f'\): controls local variation and the derivative part of the graph norm;
- \(f(0)\): repairs the constant defect on the bounded segment;
- \(wf\): supplies the essential tail margin.

None can be removed from this proof without replacing its function by another declared estimate.

## Low-weight interval obstruction

Suppose there are intervals

\[
I_n=(a_n,a_n+L_n),
\qquad
L_n\to\infty,
\]

with \(a_n>0\), and numbers \(\varepsilon_n\to0\) such that

\[
\operatorname*{ess\,sup}_{r\in I_n}|w(r)|
\le
\varepsilon_n.
\]

Choose \(\phi\in C_c^\infty(0,1)\) with \(\|\phi\|_2=1\), and set

\[
f_n(r)=L_n^{-1/2}
\phi\left(\frac{r-a_n}{L_n}\right).
\]

Then

\[
\|f_n\|_2=1,
\qquad
f_n(0)=0,
\]

\[
\|f_n'\|_2
=L_n^{-1}\|\phi'\|_2\to0,
\]

and

\[
\|wf_n\|_2\le\varepsilon_n\to0.
\]

Hence

\[
\|Q_wf_n\|\to0
\]

while \(\|f_n\|_{H^1}\to1\). The observer is not bounded below.

This proves rival 3 and rejects rival 2 for every weight with such low-weight intervals.

## Why boundary multiplicity cannot repair the tail

Any finite collection of endpoint derivatives or finite jets has finite-dimensional target whenever the traces are defined on the selected graph rung. For packets supported beyond the endpoint, all such local traces vanish. Therefore adding finitely many boundary channels leaves the broad-packet counterexample unchanged.

The bold conjecture fails.

## Reciprocal double

On the radial double, use the same real weight on both oriented channels:

\[
M_w^{\rm dbl}
=
\operatorname{diag}(M_w,M_w).
\]

Then

\[
M_w^{\rm dbl}W_u=W_uM_w^{\rm dbl},
\qquad
M_w^{\rm dbl}J_u=J_uM_w^{\rm dbl}.
\]

Thus the bulk repair preserves reciprocal and Real symmetry. Applying the scalar estimate to each component gives a stable doubled observer.

Reciprocal doubling without \(M_w^{\rm dbl}\) does not help: put the broad packet in either parity eigenspace \((f_n,\pm uf_n)\). Rival 4 fails.

## Green compatibility

The multiplier is a bulk observation map, not a change to the Green boundary form or wall domain. The original maximal-isotropic relation \(\Lambda_u\) remains unchanged. This separates conservative sewing from coercive observation.

If one instead inserts \(w\) into the differential operator, that is a new dynamics constructor and requires a new Green identity. The same scalar function cannot be moved between these roles without proof.

## Symmetry-descent interpretation

The tail observer is invariant under the reciprocal subgroup and transports under phase gauges. It therefore descends through the established enriched comparisons. Its lower margin is preserved by those unitary transports.

This is not quotienting away the tail. It is adding a source-sensitive map on the directions that boundary and derivative channels miss.

## Constructor-role signature

A `tail_bulk_complement` must declare:

- the graph-domain source;
- multiplier target and norm;
- a tail cutoff \(R\);
- an essential lower bound \(c\) beyond that cutoff;
- reciprocal and Real covariance;
- independence from the boundary-domain constructor.

A merely nonzero weight does not satisfy this role.

## Strongest falsification attempt

A weight may approach zero at isolated points or on short intervals while the derivative still prevents concentration there. Thus pointwise global lower boundedness of \(w\) is stronger than necessary. The hostile test requires low weight on intervals whose lengths diverge, allowing derivative energy to vanish. This is why the theorem states a simple sufficient condition and a separate obstruction rather than claiming necessity.

## Disposition

The half-line instability has an explicit repair: a tail-coercive bulk observer. The repair respects Green, Real, reciprocal, and phase-gauge structure while remaining a separate constructor. Finite boundary multiplicity cannot substitute for it. The remaining classification problem is to characterize weights by a quantitative thickness condition that excludes low-cost broad packets without requiring uniform pointwise positivity.
