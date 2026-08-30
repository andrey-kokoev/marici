# The Q-D tail mate square closes by the spectral tangent

## Tail resolvent

For the one-sided source \(f\), write

\[
(R_sf)(q)
=G_s(q)
=e^{-sq}\int_q^\infty f(v)e^{sv}\,dv.
\]

Let \(Q\) denote multiplication by the scale coordinate and let \(D\) denote
its derivative:

\[
(Qf)(v)=vf(v),
\qquad
(Df)(v)=f'(v).
\]

These are the native phase-space rows already selected by Mellin transport
and Fourier conjugation.

## Strict derivative square

Integration by parts gives

\[
R_s(Df)(q)
=-f(q)-sG_s(q).
\]

The tail equation gives the same expression:

\[
D_qG_s(q)=-f(q)-sG_s(q).
\]

Therefore

\[
R_sD=D_qR_s.
\]

The derivative mate square commutes strictly.

## Position square and its exact residual

Differentiating the tail with respect to the spectral parameter gives

\[
\partial_sG_s(q)
=e^{-sq}\int_q^\infty (v-q)f(v)e^{sv}\,dv.
\]

Meanwhile,

\[
R_s(Qf)(q)
=e^{-sq}\int_q^\infty vf(v)e^{sv}\,dv.
\]

Splitting \(v=q+(v-q)\) yields

\[
R_sQ=QR_s+\partial_sR_s.
\]

Thus the position mate square is not strictly commutative. Its entire residual
is the canonical spectral tangent. No fitted boundary term is required.

## Endpoint zero-state

Let

\[
F(s)=G_s(0)=\int_0^\infty f(v)e^{sv}\,dv.
\]

Endpoint evaluation gives

\[
E_0R_s(Qf)=F'(s),
\]

and

\[
E_0R_s(Df)=-f(0)-sF(s).
\]

At a scalar zero \(F(s_0)=0\), the phase-space endpoint packet becomes

\[
\bigl(F'(s_0),-f(0)\bigr).
\]

For the completed theta primitive, the boundary value \(f(0)\) is fixed by
the chosen source convention. When it is nonzero, the graph packet cannot
vanish even at a multiple scalar zero. The position component separately
measures transversality through \(F'(s_0)\).

## Meaning

The source-derived rank-two observer and the zero-state are now connected by
an exact higher coherence law:

- the \(D\) wall commutes with tail propagation;
- the \(Q\) wall commutes up to the spectral-tangent homotopy
  \(\partial_sR_s\);
- endpoint evaluation turns that homotopy into the derivative of the scalar
  readout.

This is the next coherence rung anticipated by the multi-tower programme. It
does not confine zeros. It explains how scalar loss of meaning is lifted to a
nonvanishing phase-space boundary packet.

## Remaining RH gate

The new packet is an observer of zero multiplicity and boundary provenance,
not an orientation law. To obtain confinement, reciprocal sewing would have
to relate the two sector copies of
\(\bigl(F'(s_0),-f(0)\bigr)\) through a conserved Green or symplectic form
whose nonzero value is incompatible with \(\operatorname{Re}(s_0-1/2)\neq0\).

That identity must be derived on the full boundary-bearing packet. Merely
noting that the endpoint vector is nonzero does not constrain where its scalar
parent vanished.

## Falsifier

For any proposed reciprocal phase-space conservation law, insert a generic
positive source with an off-seam transform zero. If the same \(Q/D\)
commutator identities and endpoint packet satisfy the law, it has no
theta-specific RH force. The discriminator must use labelled modular or
arithmetic sewing beyond this universal resolvent calculus.
