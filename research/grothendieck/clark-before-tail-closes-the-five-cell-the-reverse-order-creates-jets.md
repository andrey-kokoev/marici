# Clark before tail closes the five-cell; the reverse order creates jets

## Question

Does the Clark or scale constructor force the five-component Fourier tail
cell into an infinite boundary-jet tower?

The answer depends on operation order.

## Two orders

Let

\[
(Tf)(q)=\int_q^\infty f(v)\,dv
\]

and let \(M\) multiply the source coordinate:

\[
(Mf)(v)=vf(v).
\]

For a Gaussian-rigging source, the source-first composite is

\[
(TMf)(q)=\int_q^\infty vf(v)\,dv.
\]

It again has finite limits at both ends. After subtracting its left
asymptote, it belongs to the same tail type as \(Tf\). Its Fourier transform
therefore has the same delta plus principal-value boundary typing. No delta
jet is created.

The reversed composite is

\[
(MTf)(q)=q\int_q^\infty f(v)\,dv.
\]

If the source mass

\[
m_0=\int_{\mathbb R}f(v)\,dv
\]

is nonzero, then

\[
(MTf)(q)\sim m_0q
\qquad(q\to-\infty).
\]

This leaves the constant-asymptote extension. On the Fourier side,
multiplication by \(q\) differentiates the half-delta and creates a
\(\delta_0'\) boundary jet.

## The braid residual

The two composites differ by

\[
([M,T]f)(q)
=
q\int_q^\infty f(v)\,dv
-
\int_q^\infty vf(v)\,dv.
\]

This is not a central scalar anomaly. For nonzero source mass it has a linear
left asymptote, so it changes the boundary capability and the graph domain.
The pair does not commute on the five-cell.

For the canonical Gaussian, \(m_0=1\) and the first moment is zero. Hence

\[
TM\phi(q)=\frac{e^{-\pi q^2}}{2\pi}
\]

stays in the Gaussian bulk, whereas

\[
MT\phi(q)=qH(q)\sim q
\]

creates the first jet wall. This is the smallest exact hostile witness.

## Why Clark differentiation uses the safe order

For the spectral tail

\[
G_z(q)=\int_q^\infty f(v)e^{izv}\,dv,
\]

spectral differentiation gives

\[
\partial_zG_z(q)
=
i\int_q^\infty vf(v)e^{izv}\,dv.
\]

Thus the source-native Clark operation is \(TM\), not \(MT\). It changes the
source before applying the tail constructor. The five-component boundary
type is preserved at every finite Clark order because polynomial multiples
of a Gaussian-rigging source remain in the bulk test space.

An infinite delta-jet tower appears only if one authorizes multiplication of
the already completed tail by the scale coordinate. That is a different
constructor with a larger domain and boundary signature.

## Categorical consequence

The five-cell is stable under the directed composite

\[
\text{source multiplication}\longrightarrow\text{tail completion},
\]

but not under its reversal. The missing structure is therefore not a sixth
simultaneous wall. It is a precedence relation. Treating the two operations
as commuting erases a nonzero boundary-jet residual.

This supplies the first exact dependency entry for the boundary compiler:

- `precedes`: Clark source multiplication precedes tail completion;
- `commutes_with`: false for tail completion;
- `domain_after`: the five-component Fourier tail extension;
- `boundary_delta`: zero in the admitted order, delta-prime in the reverse;
- `completion_scope`: Gaussian bulk plus constant/delta and odd tail/PV
  planes;
- `residual_capability`: first boundary jet.

## Result

The actual Clark-before-tail constructor closes on the five-component type.
The reverse order forces a delta-jet prolongation. The next arithmetic audit
may therefore use the finite five-type cell, provided every source formula
respects this precedence before restricted-product completion.
