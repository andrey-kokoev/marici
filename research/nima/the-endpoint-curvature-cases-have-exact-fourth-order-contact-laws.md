# The endpoint curvature cases have exact fourth-order contact laws

Event 10295 introduced

\[
y=\frac{kA_2}{M_2},
\qquad
k=2\sqrt{\pi t},
\]

and proved that a zero-character contact can survive quadratically only for

\[
-1\le y\le0.
\]

At the endpoint values \(y=0,-1\), the quadratic ellipse coefficient
vanishes, so the quartic terms decide feasibility.

Write

\[
A(t,\xi)
=
A_0+\frac{A_2}{2}\xi^2+\frac{A_4}{24}\xi^4+O(\xi^6),
\]

with the scalar contact normalization

\[
A_0=\frac{M_0}{k}.
\]

The archimedean contact ratio expands as

\[
\mathcal L(t,\xi)
=
1+
\frac{M_2}{M_0}y(1+y)\xi^2
+
L_4\xi^4
+
O(\xi^6),
\]

where

\[
L_4
=
\frac{y^2}{4}\left(\frac{M_2}{M_0}\right)^2
+
\frac{kA_4}{12M_0}(1+4y).
\]

The prime ellipse boundary is

\[
1-\mathcal D(t,\xi)
=
1-c_4\xi^4+O(\xi^6),
\]

with

\[
c_4
=
\frac{M_0M_4-M_2^2}{4M_0^2}.
\]

Hence endpoint feasibility requires

\[
L_4\le-c_4.
\]

## Upper endpoint: \(y=0\)

Here \(A_2=0\), and

\[
L_4=\frac{kA_4}{12M_0}.
\]

Therefore a contact requires

\[
A_4
\le
-\frac{3(M_0M_4-M_2^2)}{kM_0}.
\]

So if the archimedean fourth derivative is not sufficiently negative, the
prime quartic margin excludes the \(A_2=0\) endpoint.

## Lower endpoint: \(y=-1\)

Here

\[
A_2=-\frac{M_2}{k},
\]

and

\[
L_4
=
\frac14\left(\frac{M_2}{M_0}\right)^2
-
\frac{kA_4}{4M_0}.
\]

The inequality \(L_4\le-c_4\) simplifies exactly to

\[
A_4\ge\frac{M_4}{k}.
\]

This is not an accidental bound. At \(y=-1\),

\[
\partial_\xi^2\Theta(t,0)
=
A_2+\frac{M_2}{k}
=
0.
\]

Since

\[
\partial_\xi^4\Theta(t,0)
=
A_4-\frac{M_4}{k},
\]

the fourth-order minimum condition is precisely

\[
A_4\ge\frac{M_4}{k}.
\]

Thus the quartic ellipse condition and the fourth-order first-contact
condition coincide exactly at the lower curvature endpoint.

## Consequence

The zero-character contact audit now has a complete local jet taxonomy:

1. \(y\notin[-1,0]\): excluded at quadratic order.
2. \(-1<y<0\): survives locally; global or higher constraints are needed.
3. \(y=0\): requires the explicit negative fourth-derivative bound.
4. \(y=-1\): requires a degenerate fourth-order minimum,
   \(A_4\ge M_4/k\).

This equality between the prime ellipse and contact-minimum laws shows that
the moment hierarchy is correctly typed: at each saturated lower-order
margin, the next prime moment becomes the next geometric contact derivative.

The next source calculation should evaluate \(A_2,A_4\) on scalar-contact
candidates and test these endpoint inequalities before any broad numerical
scan.
