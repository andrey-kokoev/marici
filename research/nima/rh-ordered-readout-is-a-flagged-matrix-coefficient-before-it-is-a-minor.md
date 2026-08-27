# The RH ordered readout is a flagged matrix coefficient before it is a minor

Author: `marici.Nima`

Date: 2026-08-26

Status: exact ordered-port correction and finite zero witness

## Readout type

Let (xin V) be the source port and (yin V^*) the endpoint observer. For
the relative transporter (M(a,b,c)), the ordered scalar readout is

\[
f_{y,x}(a,b,c)=y(M(a,b,c)x).
\]

This is a matrix coefficient of the relative-flag transport. It becomes one
matrix entry only when both ports are aligned with the chosen basis. It
becomes a higher generalized minor only after passing to an exterior-power
representation with separately authorized wedge ports.

Therefore the current theta source-to-endpoint scalar cannot simply be named
as one of the (A_2) minors. Its source and observer flags must first be
constructed in the same frame.

## Exact expansion

Write

\[
x=(x_1,x_2,x_3)^T,
\qquad
y=(y_1,y_2,y_3).
\]

For

\[
M(a,b,c)=
\begin{pmatrix}
1&a+c&ab\\
0&1&b\\
0&0&1
\end{pmatrix},
\]

the readout is

\[
f_{y,x}
=
y_1x_1+y_2x_2+y_3x_3
+y_1x_2(a+c)
+y_1x_3ab
+y_2x_3b.
\]

Using the minor coordinates (P=ab), (Q=b), and (R=a+c), this becomes

\[
f_{y,x}=C_0+C_RR+C_PP+C_QQ,
\]

with coefficients fixed by the ordered ports. The fourth minor (S=bc)
enters after a chart transition through the exchange law (QR=P+S).

This is the categorical role of the ordered flag: it selects the linear
functional on the minor algebra.

## Coherence still permits zeros

The transporter always has determinant one, and its generalized minors obey
the exact exchange relation. Nevertheless a nonconstant ordered coefficient
can vanish.

For the basis ports (x=e_2) and (y=e_1^*),

\[
f_{y,x}=a+c=R.
\]

Taking (a=2), (b=3), and (c=-2) gives

\[
f_{y,x}=0,
\qquad
\det M=1.
\]

The relative flag is regular and the exchange relation remains valid. Only
the selected ordered coefficient vanishes.

For (x=e_3) and (y=e_1^*), the readout is (P=ab), producing a different
divisor. Thus even basis-aligned port choices select inequivalent zero loci.

## Required theta bridge

The finite bridge to RH now has four typed parts:

1. construct the rank-three relative transporter from theta/Tate operations;
2. construct the source vector and endpoint covector independently of its
   zeros;
3. prove that their matrix coefficient equals the completed theta section up
   to a nowhere-vanishing authorized factor;
4. derive a source law preventing that coefficient from vanishing off seam.

The first three identify the correct divisor. Only the fourth carries
zero-confinement content.

Neither the determinant-one condition, the Plücker exchange relation, nor the
pentagon can replace the ordered-port identification.

## Falsifier

Any proposed categorical RH theorem fails if it proves regularity of the
relative flag or positivity of its full Gram state but does not control the
specific coefficient selected by the source and observer ports. The exact
(R=0), (det M=1) witness is the smallest such counterexample.

