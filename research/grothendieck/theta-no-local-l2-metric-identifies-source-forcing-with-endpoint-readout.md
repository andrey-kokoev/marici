# Theta no local L2 metric identifies source forcing with endpoint readout

## Bounded question

Can a natural change of state metric make the scalar endpoint readout the
Hilbert adjoint of the theta source-control port?

## Current ports

The boundary-control Evans system has control map

\[
bc=cf
\]

and scalar observation

\[
\ell(G)=G(0).
\]

In ordinary (L^2),

\[
b^*G=\langle f,G\rangle,
\]

so \(R_{\mathrm{port}}=\ell-b^*\ne0\).

## Weighted L2 no-go

Let the state metric be any local weighted form

\[
\langle G,H\rangle_w
=\int_0^\infty G(q)\overline{H(q)}w(q)\,dq
\]

with an ordinary positive weight (w). If \(\ell=b^*\) in this metric, then
for every compactly supported smooth test function (G),

\[
G(0)=\int_0^\infty G(q)\overline{f(q)}w(q)\,dq.
\]

Distributionally this requires

\[
w\overline f=\delta_0.
\]

The left side is an ordinary locally integrable function for the theta source;
the right side is a boundary distribution. Equality is impossible.

Therefore no local weighted (L^2) metric turns smooth source forcing into
endpoint evaluation.

## Sobolev graph metrics

Endpoint evaluation is continuous in suitable Sobolev graph spaces. Its Riesz
representer is then a Green kernel of the graph operator. For the theta forcing
vector (f) itself to represent the endpoint trace, it must satisfy the
corresponding homogeneous adjoint equation in the interior and the correct
boundary jump.

This can be a valid source theorem only if the graph operator is derived before
the comparison with (f). Defining an operator from (f'/f), or otherwise
choosing its coefficients so that (f) becomes the representer, is a fitted
bridge.

## Required port split

The source architecture naturally contains two distinct scalar capabilities:

- an interior source-control port (c\mapsto cf);
- a boundary trace port (G\mapsto G(0)).

They should remain separately typed. A symmetric colligation may include both,
but it must derive the comparison between them through a Green boundary form,
not declare them adjoint by changing the metric.

## Finite falsifier

Choose a smooth state (G) supported away from the origin with
\(\langle f,G\rangle_w\ne0\). Then

\[
\ell(G)=0,
\qquad
b^*G\ne0.
\]

This witness rejects every declared weighted (L^2) identification of the two
ports.

## Scope

This packet proves the weighted-local-metric no-go and states the independent
Green-kernel gate for Sobolev metrics. It does not rule out a source-derived
boundary triple with separate ports or prove RH.
