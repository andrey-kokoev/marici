# A zero-character first contact forces the archimedean curvature into one interval

Let the completed Gaussian source kernel be

\[
\Theta(t,\xi)=A(t,\xi)-C(t)R(t,\xi),
\qquad
C(t)=\frac1{2\sqrt{\pi t}}.
\]

Put

\[
k=2\sqrt{\pi t}=\frac1C.
\]

Because the archimedean-plus-endpoint term \(A(t,\xi)\) is even in \(\xi\),
write

\[
A(t,\xi)
=
A_0+\frac{A_2}{2}\xi^2+O(\xi^4).
\]

At a zero-character contact,

\[
\Theta(t,0)=0
\]

implies

\[
A_0=CM_0=\frac{M_0}{k}.
\]

The prime ellipse contact ratio is

\[
\mathcal L(t,\xi)
=
\left(\frac{kA}{M_0}\right)^2
+
\frac{(k\partial_\xi A)^2}{M_0M_2}.
\]

At the contact,

\[
\mathcal L(t,0)=1.
\]

Its quadratic expansion is

\[
\mathcal L(t,\xi)
=
1+
\left[
\frac{kA_2}{M_0}
+
\frac{k^2A_2^2}{M_0M_2}
\right]\xi^2
+
O(\xi^4).
\]

Introduce the normalized curvature

\[
y=\frac{kA_2}{M_2}.
\]

Then

\[
\mathcal L(t,\xi)
=
1+
\frac{M_2}{M_0}y(1+y)\xi^2
+
O(\xi^4).
\]

Event 10294 showed that the available prime deficit is only quartic:

\[
1-\mathcal D(t,\xi)
=
1-c_4(t)\xi^4+O(\xi^6),
\qquad
c_4(t)>0.
\]

Therefore the necessary ellipse inequality

\[
\mathcal L\le1-\mathcal D
\]

forces

\[
y(1+y)\le0,
\]

hence

\[
-1\le y\le0.
\]

Equivalently,

\[
-\frac{M_2}{2\sqrt{\pi t}}
\le
A_2
\le0.
\]

## Relation to first-contact curvature

At \(\xi=0\),

\[
\partial_\xi^2\Theta
=
A_2+CM_2
=
\frac{M_2}{k}(1+y).
\]

The first-contact minimum condition gives only

\[
y\ge-1.
\]

The ellipse adds the independent upper condition

\[
y\le0.
\]

Thus a zero-character first contact is possible only when the
archimedean-plus-endpoint character curvature is nonpositive but not more
negative than the prime second-moment curvature.

## Three local regimes

The scalar contact audit now splits into:

1. \(A_2>0\): excluded immediately by the ellipse, since
   \(\mathcal L>1\) quadratically.
2. \(A_2<-M_2/k\): excluded by the first-contact curvature condition.
3. \(-M_2/k\le A_2\le0\): survives the quadratic test.

At the endpoints \(y=0\) and \(y=-1\), the quadratic coefficient vanishes.
Then the quartic prime margin from event 10294 becomes decisive and must be
compared with the fourth-order expansion of \(A\).

For \(-1<y<0\), the contact ratio moves strictly inside the ellipse at
quadratic order, so the quartic phase gap alone cannot exclude a nearby
contact.

## Executable consequence

The next source calculation is only one scalar interval test:

\[
A_2(t)
\stackrel{?}{\in}
\left[
-\frac{M_2(t)}{2\sqrt{\pi t}},
0
\right]
\]

at every hypothetical zero-character solution

\[
A_0(t)=\frac{M_0(t)}{2\sqrt{\pi t}}.
\]

If the two equations cannot hold simultaneously, zero-character first
contact is excluded. This is narrower than a global positivity estimate and
uses only explicit gamma/endpoint derivatives and the positive prime moments
\(M_0,M_2\).
