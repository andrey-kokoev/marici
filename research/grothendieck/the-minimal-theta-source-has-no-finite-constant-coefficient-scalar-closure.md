# The minimal theta source has no finite constant-coefficient scalar closure

Author: `marici.Grothendieck`

Date: 2026-08-26

Status: exact no-go theorem

## Question

Can the missing doubled Green conservation law close on finitely many scalar
derivatives of the completed theta source with constant coefficients?

## Primitive label

On the positive chart put

\[
x=\pi e^{2u}.
\]

Up to a positive constant, the primitive theta label is

\[
\phi_1(u)=x^{1/4}(4x^2-6x)e^{-x}.
\]

Writing (D=\partial_u=2x\partial_x), every derivative has the form

\[
D^j\phi_1=x^{1/4}e^{-x}q_j(x),
\]

where

\[
q_{j+1}=2xq_j'+\left(\frac12-2x\right)q_j.
\]

If (q_j) has degree (j+2), the last term raises the degree by one and
multiplies its leading coefficient by (-2). Therefore

\[
\deg q_j=j+2,
\qquad
[x^{j+2}]q_j=4(-2)^j.
\]

## No finite scalar annihilator

Let

\[
P(D)=a_0+a_1D+\cdots+a_rD^r,
\qquad a_r\ne0.
\]

In (P(D)\phi_1), only the highest derivative contributes to degree (r+2).
Its coefficient is

\[
4a_r(-2)^r\ne0.
\]

Hence

\[
P(D)\phi_1\ne0
\]

for every nonzero constant-coefficient differential operator (P(D)).

The same is true for the full positive-chart source

\[
\Phi(u)=\sum_{n\ge1}n^{-1/2}\phi_1(u+\log n).
\]

As (u\to+\infty), the (n=1) term of (P(D)\Phi) has exponential scale
(e^{-\pi e^{2u}}), while every (n\ge2) term has scale at most
(e^{-4\pi e^{2u}}) times a polynomial. The tail is therefore negligible
relative to the nonzero leading polynomial of the first label. It cannot
cancel that label identically. Thus

\[
P(D)\Phi\ne0
\]

for every nonzero (P).

## Consequence

The completed theta source cannot be replaced by a finite scalar state vector

\[
(\Phi,D\Phi,\ldots,D^r\Phi)
\]

whose evolution closes through a constant matrix. Any source-derived Green
system of that type discards essential label information.

This makes the labelled or infinite-dimensional lift mandatory for the
current RH programme. The primitive, square, seam, and archimedean channels
cannot all be encoded by adding finitely many constant-coefficient scalar
jets of the aggregate.

## Scope

The theorem excludes finite constant-coefficient linear scalar closure. It
does not exclude variable-coefficient equations, nonlinear differential
identities, finite systems with independently retained arithmetic variables,
or infinite labelled operator systems. It does not prove RH.

## Falsifier

One nonzero polynomial (P) satisfying (P(D)\Phi=0) would falsify the
claim. The leading-degree calculation prevents this. The checker also tests
an exponential control source, for which a first-order annihilator exists,
so failure is not built into the test harness.

