# The Clark Derivative Row Is Injective on the Source Tail-Forcing Sector

## Source tail equation

For a source forcing \(f\), define

\[
G_s(q)
=
e^{-sq}\int_q^\infty f(v)e^{sv}\,dv.
\]

Direct differentiation in \(q\) gives

\[
(\partial_q+s)G_s=-f.
\]

The forcing is independent of the spectral parameter. Differentiating the
flow with respect to \(s\) therefore gives

\[
(\partial_q+s)\partial_sG_s=-G_s.
\]

For \(s=a+iz\) with fixed \(a\),

\[
\partial_zG_s=i\partial_sG_s.
\]

## Exact kernel theorem

Suppose the Clark derivative feature vanishes identically:

\[
\partial_zG_s=0.
\]

Then \(\partial_sG_s=0\). The differentiated flow immediately yields

\[
G_s=0.
\]

The original flow then yields

\[
f=0.
\]

Thus the Clark derivative row alone is injective on the source-tail forcing
sector. In particular, simultaneous vanishing of

\[
G_s+f=0,
\qquad
\partial_zG_s=0
\]

has only the zero source state.

No genericity assumption is needed. The extra differential identity mentioned
in the earlier Clark packet is exactly the differentiated source flow, and it
forces the state to vanish.

## Operator form

Write

\[
L_s=\partial_q+s.
\]

Then

\[
L_sG_s=-f,
\qquad
L_s\partial_sG_s=-G_s.
\]

The implication

\[
\partial_sG_s=0
\Longrightarrow
G_s=0
\Longrightarrow
f=0
\]

does not require inversion of \(L_s\). It therefore remains valid on any
common domain where both source identities hold.

## Scope of the theorem

This closes state-feature injectivity for the continuous source-tail forcing
sector. It does not automatically include independently adjoined arithmetic
boundary currents, seam states, or corona classes. Those directions require
their own incidence rows.

It also does not prove a completion lower bound. Injectivity of an unbounded
operator relation does not imply closed range or uniform observability. The
remaining analytic gate is an estimate controlling the admitted state norm by

\[
\lVert G_s+f\rVert
+\lVert\partial_zG_s\rVert
\]

together with the separately typed seam and arithmetic rows.

## Finite model

For a finite generator \(L\), the resolvent model gives

\[
G=-(L+sI)^{-1}f,
\qquad
\partial_sG=(L+sI)^{-2}f.
\]

Whenever \(L+sI\) is invertible, the derivative row has full column rank. The
checker verifies this exactly on a rational three-mode generator and confirms
that adding the \(G+f\) row does not create a kernel.
