# Theta physical-port high-frequency reduction

## Correction target

The preceding adjacent-block asymptotic held \(\alpha\) and \(\beta\) fixed
while sending \(b\) to infinity. The physical angular problem does not permit
that limit. Its coefficients are

\[
\alpha=2a-\frac{a}{2(a^2+b^2)},
\qquad
\beta=2b+\frac{b}{2(a^2+b^2)}.
\]

This packet computes the corrected source gate.

## Exact block folding

With \(L=\pi/b\), the canonical two-lobe block is

\[
I(a,L)=\beta I_J(a,L)+\alpha I_W(a,L),
\]

where

\[
I_J(a,L)=\int_0^{2L}J_a(r)\cos(\pi r/L)\,dr,
\]

and

\[
I_W(a,L)=\int_0^{2L}rW_a(r)\sin(\pi r/L)\,dr.
\]

Smooth evenness gives

\[
I_J(a,L)=\frac{2J_a''(0)}{\pi^2}L^3+O(L^5),
\]

and

\[
I_W(a,L)=-\frac{2W_a(0)}{\pi}L^2+O(L^4).
\]

## Physical port scaling

Substituting \(b=\pi/L\) into the source coefficients gives

\[
\beta=\frac{2\pi}{L}+\frac{L}{2\pi}+O(L^3),
\]

and

\[
\alpha=2a-\frac{aL^2}{2\pi^2}+O(L^4).
\]

Therefore the physical block has the leading expansion

\[
I(a,L)
=
\frac{4}{\pi}
\left[J_a''(0)-aW_a(0)\right]L^2
+O(L^4).
\]

The apparent one-order mismatch has disappeared. Both source channels enter
at order \(L^2\).

## Energy form of the gate

Since \(W_a\) is the autocorrelation of \(f_a\),

\[
W_a(0)=\lVert f_a\rVert_2^2,
\qquad
W_a''(0)=-\lVert f_a'\rVert_2^2.
\]

As \(J_a=\partial_aW_a\),

\[
J_a''(0)=-\partial_a\lVert f_a'\rVert_2^2.
\]

Hence the leading physical coefficient is

\[
-\frac{4}{\pi}
\left[
\partial_a\lVert f_a'\rVert_2^2
+a\lVert f_a\rVert_2^2
\right].
\]

The high-frequency band problem is therefore no longer a competition between
different asymptotic orders. It is one source-energy derivative inequality.

## Corrected result

The fixed-port high-frequency falsifier does not apply to the physical angular
map. The physical map supplies exactly the missing \(1/L\) amplification of
the positive-current port.

Amplification alone does not establish the desired sign. The sharp native
gate is

\[
J_a''(0)-aW_a(0)\mathrel{?}\ge0.
\]

Equivalently,

\[
\partial_a\lVert f_a'\rVert_2^2
+a\lVert f_a\rVert_2^2
\mathrel{?}\le0.
\]

## The source-energy gate is negative near the seam

Put

\[
g(x)=\Phi(|x|),
\qquad
N(a)=\lVert f_a\rVert_2^2,
\qquad
E(a)=\lVert f_a'\rVert_2^2.
\]

Integration by parts gives

\[
E(a)
=
\int_{\mathbb R}e^{2ax}g'(x)^2\,dx-a^2N(a).
\]

Both \(E\) and \(N\) are even in \(a\). Therefore, for

\[
Q(a)=J_a''(0)-aW_a(0)=-E'(a)-aN(a),
\]

one has \(Q(0)=0\) and

\[
Q'(0)
=
N(0)-4\int_{\mathbb R}x^2g'(x)^2\,dx.
\]

The boundary decay of the theta source permits integration of
\((xg(x)^2)'\):

\[
N(0)=-2\int_{\mathbb R}xg(x)g'(x)\,dx.
\]

Cauchy--Schwarz then yields

\[
N(0)
\le
2N(0)^{1/2}
\left(
\int_{\mathbb R}x^2g'(x)^2\,dx
\right)^{1/2},
\]

and hence

\[
N(0)
\le
4\int_{\mathbb R}x^2g'(x)^2\,dx.
\]

Equality would require \(xg'=-g/2\) almost everywhere, whose nonzero
solutions are not regular and square-integrable at the origin. The theta
source therefore gives strict inequality:

\[
Q'(0)<0.
\]

Consequently there exists \(a_0>0\) such that

\[
Q(a)<0,
\qquad 0<a<a_0.
\]

For every such fixed \(a\), the physical canonical block is negative for all
sufficiently large \(b\).

## Final result

The physically coupled one-block mechanism is falsified in a genuine outer
regime: small positive horizontal tilt and sufficiently large phase
frequency. The source coefficient relation removes the naive order mismatch,
but the strict source Hardy inequality orients the resulting equal-order
combination negatively.

This does not falsify the original scalar Pick/angular inequality. It
falsifies one proposed adjacent-band cancellation explanation. A successful
transport theorem must use a larger source-derived block or act before this
two-lobe projection.

## Deutschian update

The surprise in the failed falsifier is itself explanatory. The geometrically
defined port vector rotates with phase frequency so that two apparently
different orders meet exactly. Treating its components as independent erased
the physical meaning. The next invariant is not either port separately but
their source-fixed leading combination.

## Sharp falsifier

The source argument above supplies an interval of values satisfying

\[
J_a''(0)-aW_a(0)<0
\]

and therefore realizes the proposed falsifier without numerical scouting.
