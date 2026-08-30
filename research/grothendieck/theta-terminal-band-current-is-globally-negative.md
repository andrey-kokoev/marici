# Theta terminal band current is globally negative

## Bounded question

The macroscopic-block theorem reduced high-frequency orientation to

\[
Q_a(R)=J_a'(R)-aR W_a(R).
\]

Does this endpoint current change sign at a finite source coherence length?

## Centered correlation source

Let

\[
g(x)=\Phi(|x|)
\]

and define

\[
P_R(y)=g(y+R/2)g(y-R/2).
\]

Then

\[
W_a(R)=\int_{\mathbb R}e^{2ay}P_R(y)\,dy,
\]

and

\[
J_a(R)=\partial_aW_a(R)
=
2\int_{\mathbb R}y e^{2ay}P_R(y)\,dy.
\]

The function \(P_R\) is even in \(y\).

## Log-concavity orients separation transport

Put \(\ell=\log g\). The completed theta source is strictly log-concave, so
\(\ell'\) is strictly decreasing. For \(R>0\),

\[
\delta_R(y)
:=
\partial_R\log P_R(y)
=
\frac12
\left[
\ell'(y+R/2)-\ell'(y-R/2)
\right]
<0.
\]

Because \(g\) is even, \(\delta_R\) is even. Differentiating the first-moment
current with respect to separation gives

\[
J_a'(R)
=
2\int_{\mathbb R}
y e^{2ay}P_R(y)\delta_R(y)\,dy.
\]

Pairing \(y\) and \(-y\) yields the exact half-line form

\[
J_a'(R)
=
4\int_0^\infty
yP_R(y)\delta_R(y)\sinh(2ay)\,dy.
\]

Every factor except \(\delta_R\) is positive for \(a,R,y>0\). Therefore

\[
J_a'(R)<0
\qquad
(a,R>0).
\]

Since \(W_a(R)>0\), it follows immediately that

\[
Q_a(R)
=
J_a'(R)-aR W_a(R)
<0
\qquad
(a,R>0).
\]

## Result

The terminal current has no finite sign-transition radius. For every positive
tilt and every finite positive macroscopic width, the aligned high-frequency
consecutive-band block is eventually negative.

This closes all bounded-width consecutive-band mechanisms, including widths
chosen after deriving a source coherence scale. The only remaining limits in
this family must send the terminal separation to infinity as the frequency
grows.

## Explanation

Strict log-concavity says that increasing the separation decreases every
centered two-copy density. The positive Mellin tilt then makes the signed
midpoint moment decrease as well: the positive half-line receives the larger
tilt weight, while the separation score is negative and reflection-even.

Thus the endpoint obstruction is not an accidental local Hardy effect. It is
the global order induced by the source. Every finite terminal boundary points
the wrong way for the proposed cancellation.

## Remaining route

The consecutive-band programme has only one possible asymptotic escape:

\[
R(L)\longrightarrow\infty
\qquad
(L\longrightarrow0).
\]

In that joint limit, the terminal current decays and the leading endpoint law
can become silent. The next honest calculation must compare the decay of
\(Q_a(R(L))\) with the next integration-by-parts terms. Equivalently, one may
return directly to the full undecomposed oscillatory integral, where no
finite artificial terminal boundary remains.

This theorem concerns the failure of a proposed bandwise explanation. It does
not decide the full scalar angular inequality.
