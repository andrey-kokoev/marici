# Theta macroscopic band block reduces to a terminal endpoint current

## Bounded question

The fixed finite-block theorem leaves one band mechanism alive: let the block
count diverge as \(L\to0\) so that its total separation width remains
macroscopic. Does that scaling introduce a genuinely global positive bulk?

## Macroscopic aligned block

Fix \(R>0\) and take a sequence \(L\to0\) for which

\[
R=2mL
\]

with integer \(m\). Thus the endpoint always lies after a complete number of
phase periods. Put \(k=\pi/L\), so \(kR=2m\pi\). The block is

\[
I_R(a,L)
=
\beta\int_0^R J_a(r)\cos(kr)\,dr
+
\alpha\int_0^R rW_a(r)\sin(kr)\,dr.
\]

## Oscillatory endpoint expansion

Because \(J_a\) is even, \(J_a'(0)=0\). Repeated integration by parts at the
aligned endpoints gives

\[
\int_0^R J_a(r)\cos(kr)\,dr
=
\frac{J_a'(R)}{k^2}+O_R(k^{-3}).
\]

For \(h_a(r)=rW_a(r)\), one has \(h_a(0)=0\), and the corresponding sine
moment is

\[
\int_0^R h_a(r)\sin(kr)\,dr
=
-\frac{h_a(R)}{k}+O_R(k^{-3}).
\]

The physical ports satisfy

\[
\beta=2k+O(k^{-1}),
\qquad
\alpha=2a+O(k^{-2}).
\]

Therefore

\[
I_R(a,L)
=
\frac{2L}{\pi}
\left[J_a'(R)-aR W_a(R)\right]
+O_R(L^2).
\]

The leading bulk has collapsed to one terminal endpoint current.

## Connection to the local Hardy obstruction

Define

\[
Q_a(R)=J_a'(R)-aR W_a(R).
\]

Smooth evenness gives

\[
Q_a(R)
=
R\left[J_a''(0)-aW_a(0)\right]+O(R^3).
\]

For all sufficiently small positive \(a\), the bracket is strictly negative
by the source Hardy theorem. Hence there is a source-dependent \(R_0(a)>0\)
such that

\[
Q_a(R)<0,
\qquad 0<R<R_0(a).
\]

For every such fixed macroscopic width, the aligned growing block remains
negative at sufficiently high frequency.

## Result

Letting the number of bands diverge is not enough. A high-frequency block of
fixed physical width is governed by its terminal endpoint, not by an
accumulated positive interior. Near the seam, that endpoint inherits the same
strict Hardy obstruction as every finite block.

Any surviving consecutive-band theorem must therefore do at least one of the
following:

1. extend beyond the first source-dependent sign-transition radius of
   \(Q_a(R)\);
2. take \(R\to\infty\), so the terminal source current decays and a different
   asymptotic order becomes visible;
3. introduce a non-endpoint modular sewing current before oscillatory
   projection.

## Explanation

This exposes what finite regrouping was missing. Rapid phase transport is an
endpoint extractor. A merely larger block does not recover global source
meaning; it transports the same local orientation to a terminal separation.
Global theta structure can matter only when the terminal boundary reaches a
distinguished source scale or disappears at infinity.

## Sharp next test

Determine the sign changes of the exact source endpoint current

\[
Q_a(R)=J_a'(R)-aR W_a(R)
\]

without bandwise fitting. If it never becomes positive, every bounded-width
consecutive-band mechanism is closed. If it does, the first zero defines the
minimal source-derived coherence length required by any viable transport.
