# Theta canonical adjacent block has a high-frequency falsifier

## Scope correction

The fixed-port asymptotic theorem below is correct, but its original
interpretation as a falsifier for the physical angular problem is retracted.
In the physical parameter map, \(\beta\) grows linearly with \(b=\pi/L\), so
the \(J\)-channel is promoted from order \(L^3\) to order \(L^2\). The exact
physical leading gate is derived in
[Theta physical-port high-frequency reduction](theta-physical-port-high-frequency-reduction.md).

Accordingly, this packet falsifies only a model with coefficients held fixed
as \(b\to\infty\). It does not decide the source-derived angular block.

## Bounded question

Can integration over one canonical pair of consecutive phase bands repair the
pointwise negative weighted-correlation lobe found at the band entrance?

## Exact folding of the block

Let

\[
L=\frac{\pi}{b}
\]

and integrate the conditional adjacent-band residual over
\(0<D<L\). Its two terms fold exactly to

\[
\begin{aligned}
I_J(a,L)
&=
\int_0^{2L}J_a(r)\cos\!\left(\frac{\pi r}{L}\right)\,dr,\\
I_W(a,L)
&=
\int_0^{2L}rW_a(r)\sin\!\left(\frac{\pi r}{L}\right)\,dr.
\end{aligned}
\]

Thus the complete block integral is

\[
I(a,L;\alpha,\beta)
=
\beta I_J(a,L)+\alpha I_W(a,L).
\]

This identity uses only the canonical half-period \(L\); no band endpoint is
chosen after inspecting the sign.

## Small-block asymptotics

The correlation \(W_a\) and its tilt derivative \(J_a=\partial_aW_a\) are
smooth even functions of the separation. Hence, uniformly for
\(0\le r\le2L\),

\[
W_a(r)=W_a(0)+O(r^2),
\qquad
J_a(r)=J_a(0)+\frac12J_a''(0)r^2+O(r^4).
\]

The constant part of the cosine moment cancels, while the constant part of
the weighted sine moment does not:

\[
\int_0^{2L}\cos\!\left(\frac{\pi r}{L}\right)dr=0,
\]

\[
\int_0^{2L}r\sin\!\left(\frac{\pi r}{L}\right)dr
=-\frac{2L^2}{\pi}.
\]

Also,

\[
\int_0^{2L}r^2\cos\!\left(\frac{\pi r}{L}\right)dr
=\frac{4L^3}{\pi^2}.
\]

Therefore

\[
I_J(a,L)
=
\frac{2J_a''(0)}{\pi^2}L^3+O(L^5),
\]

whereas

\[
I_W(a,L)
=
-\frac{2W_a(0)}{\pi}L^2+O(L^4).
\]

Since \(W_a(0)=\lVert f_a\rVert_2^2>0\), for every fixed
\(a>0\), \(\alpha>0\), and finite \(\beta\ge0\),

\[
I(a,L;\alpha,\beta)<0
\]

for all sufficiently small positive \(L\), equivalently for all sufficiently
large \(b\).

## Result

Canonical integration over one adjacent positive-negative band pair does not
repair the weighted-correlation obstruction in the artificial fixed-port
limit. The negative weighted channel is order \(L^2\), while the
translation-defect current before physical port scaling is order \(L^3\).

The existing Pólya theorem does not contradict this result. It orients an
infinite cosine transform of an autocorrelation tail. The present observable
is a finite two-lobe moment of \(rW_a(r)\), with a nonzero endpoint-scale
contribution of different parity.

## Scope correction

The following proposed mechanisms are closed only for independently fixed
ports:

1. pointwise adjacent-band positivity;
2. positivity of one canonically integrated adjacent-band pair;
3. repair by the positive \(J\)-current at arbitrarily high \(b\) with fixed
   \(\alpha/\beta\).

For the physical port map, the first possibility below actually occurs and
must be retained. The smallest surviving possibilities are:

1. the physical parameter map forces \(\beta/\alpha\) to grow at least on the
   scale \(1/L\);
2. a source-derived block spanning more than two lobes cancels the order
   \(L^2\) term;
3. the requested outer domain has an independently derived upper bound on
   \(b\).

Any of these must be derived before examining the desired sign.

## Deutschian meaning

The surprise is that the newly proved boundary repair is one asymptotic order
too weak. Its source meaning is now precise: translation-defect curvature is
a genuine oriented coordinate, but it is not the conserved quantity of the
full band transport. The missing explanation must act before the
high-frequency projection produces its order-\(L^2\) weighted channel.

## Circularity boundary

This theorem is an explicit response of the fixed source incidence
\(1-\tau_D\). It is not a homogeneous line equation for the scalar completed
section and makes no divisor claim. A native Clark/Tate connection capable of
confining zeros would still have to be constructed before scalar projection;
otherwise regular divisibility of a section by its covariant derivative is
equivalent to assuming zero-freeness.
