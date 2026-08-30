# The rational magnetic zeros are oppositely oriented route crossings

Retain the analytically continued two-route packet

\[
R(d)=(A(d),B(d))
\]

before scalar augmentation. The scalar and complementary characters are

\[
S(d)=A(d)+B(d),
\qquad
D(d)=A(d)-B(d).
\]

At both grade-six rational roots,

\[
d_-=\frac{17}{3},
\qquad
d_+=\frac{37}{3},
\]

the packet is nonzero and anti-diagonal:

\[
B(d_\pm)=-A(d_\pm)\ne0.
\]

Thus \(S(d_\pm)=0\) is destructive interference, while
\(D(d_\pm)=2A(d_\pm)\ne0\) retains the route distinction.

## Crossing invariant

Define the route Wronskian

\[
\Omega(d)=A(d)B'(d)-B(d)A'(d).
\]

On the anti-diagonal locus \(B=-A\),

\[
\Omega=A(A'+B')=A\,S'.
\]

Therefore \(\Omega\ne0\) is equivalent to a transverse scalar crossing when
the route amplitude remains nonzero.

Exact differentiation gives

\[
S'\!\left(\frac{17}{3}\right)
=
\frac{11322837995356160000}{27}>0,
\]

and

\[
S'\!\left(\frac{37}{3}\right)
=
-\frac{7191518846729584640000}{27}<0.
\]

The Wronskians are respectively negative and positive because \(A<0\) at both
points. Hence the two scalar-dark fibers are simple crossings with opposite
orientation.

The residual obstruction polynomial carries the same simplicity, although
its chosen normalization reverses the displayed scalar orientation:

\[
P_d\!\left(6,\frac{17}{3}\right)=-240,
\qquad
P_d\!\left(6,\frac{37}{3}\right)=240.
\]

## Separation from route loss

At the integral exception \((g,d)=(2,5)\), both route amplitudes vanish. There
is no nonzero anti-diagonal packet and no route Wronskian crossing. This
distinguishes the grade-two route-loss class from the two grade-six analytic
interference crossings.

## Framing boundary

The sign of \(\Omega\) requires two orientations:

1. an ordering of the route basis;
2. an orientation of the parameter used for differentiation.

The route ordering is inherited from the reflected left/right construction.
The depth variable \(d\), however, is originally a discrete exponent-lattice
label. Its continuous orientation belongs only to analytic continuation until
an enlarged source constructor supplies a genuine family over \(d\).

Therefore this is an exact theorem about the continued local route packet, not
yet a physical magnetic crossing theorem. It identifies the correct datum that
a source lift must preserve: the framed Wronskian, rather than a fitted
full-kernel portal.

The next falsifier is a source-authorized enlarged family whose induced
orientation reverses, annihilates, or fails to descend the Wronskian. If no
such family exists, the crossings remain analytic shadows excluded by the
integral source grammar.

Replay:

\`python research/strominger/checkers/magnetic_route_wronskian_checks.py\`
