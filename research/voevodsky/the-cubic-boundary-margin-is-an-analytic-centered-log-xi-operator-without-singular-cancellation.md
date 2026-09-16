# The cubic boundary margin is an analytic centered log-Xi operator without singular cancellation

## Objective

Construct the correct central chart for the remaining interval

\[
0<x<0.085.
\]

Direct evaluation of the boundary margin loses precision because two order-\(x\) terms cancel, leaving an order-\(x^3\) result. Centered even coordinates remove that cancellation exactly.

## Even logarithmic coordinate

Put

\[
t
=
x^2
\]

and define

\[
L(t)
=
\frac{
\Xi'(x)
}
{
2x
\Xi(x)
}.
\]

Because \(\Xi\) is even, \(\Xi'/\Xi\) is odd, so \(L\) is analytic at \(t=0\).

It is the centered logarithmic derivative

\[
L(t)
=
\frac d{dt}
\log
\Xi(
\sqrt t
).
\]

The boundary mean is

\[
m(x)
=
\frac{
\Xi'(x)
}
{
\Xi(x)
}
=
2xL(t).
\]

Differentiating gives

\[
m'(x)
=
2L(t)
+
4tL'(t).
\]

## Exact cancellation

Recall

\[
G(x)
=
(
1+4x^2
)
m(x)
-
x(
1-4x^2
)m'(x).
\]

Substitute \(m=2xL\) and \(m'=2L+4tL'\):

\[
\begin{aligned}
G(x)
={}&
2x(
1+4t
)L
-
x(
1-4t
)
[
2L+4tL'
]\\
={}&
4x^3
\left[
4L(t)
-
(
1-4t
)L'(t)
\right].
\end{aligned}
\]

Therefore

\[
\boxed{
\frac{
G(x)
}
{
x^3
}
=
4
\left[
4L(t)
-
(
1-4t
)L'(t)
\right],
\qquad
t=x^2.
}
\]

This identity removes every division by a small \(x\) and every cancellation between separately enclosed order-\(x\) terms.

## Central coefficient

Write

\[
L(t)
=
\ell_0
+
\ell_1t
+
\ell_2t^2
+
\cdots.
\]

Then

\[
\frac{
G(x)
}
{
x^3
}
=
4
[
4\ell_0
-
\ell_1
]
+
O(t).
\]

Hence

\[
\boxed{

g_0
=
4
(
4\ell_0-
\ell_1
).
}
\]

The high-precision and Arb point computations give

\[

g_0
=
0.369828580243844611\ldots
>0.
\]

This is the same branch-point margin previously expressed through the theta moments \(M_2,M_4\).

## Directed jet compatibility

The existing centered Xi jet checker constructs the coefficients of

\[
L(t)
=
\frac{
\Xi'(x)
}
{
2x\Xi(x)
}
\]

through degree five with directed intervals.

Therefore the normalized margin coefficients are obtained by the exact linear recurrence

\[
q_n
=
4
\left[
4\ell_n
-
(
n+1
)
\ell_{n+1}
+
4n
\ell_n
\right],
\]

or

\[
\boxed{
q_n
=
4
\left[
4(
n+1
)
\ell_n
-
(
n+1
)
\ell_{n+1}
\right]
=
4(
n+1
)
(
4\ell_n-
\ell_{n+1}
).
}
\]

Thus

\[
\frac{
G(x)
}
{
x^3
}
=
\sum_{n\ge0}
q_nt^n.
\]

No nonlinear interval division is needed after the \(L\)-jet has been constructed.

## Certification target

Let

\[
Q_N(t)
=
\sum_{n=0}^N
q_nt^n.
\]

If a remainder bound

\[
\left|
\sum_{n>N}
q_nt^n
\right|
\le
R_N(T)
\]

is available for \(0\le t\le T\), then positivity follows from

\[
\inf_{0\le t\le T}
Q_N(t)
-
R_N(T)
>0.
\]

For the remaining central boundary interval,

\[
T
=
0.085^2
=
0.007225.
\]

A degree-five jet should be numerically ample; the missing component is a rigorous analytic remainder bound.

## Cauchy remainder route

Choose a complex radius \(R>T\) in the \(t\)-plane on which \(\Xi(\sqrt t)\) is certified nonzero and let

\[
M_R
=
\max_{|t|=R}
\left|
4
[
4L(t)-
(
1-4t
)L'(t)
]
\right|.
\]

Cauchy's estimate gives

\[
R_N(T)
\le
M_R
\frac{
(
T/R
)^{N+1}
}
{
1-T/R
}.
\]

The required nonvanishing circle can be chosen well inside the first known zero radius and certified from the theta integral or the directed centered Xi series.

## Theta-moment route

Alternatively, construct the coefficients \(\ell_n\) from the positive theta moments and bound their tails using the superexponential Riemann kernel. This avoids any zero-location input but requires bookkeeping for logarithmic-series division.

## Tetrahedral interpretation

The normalized function

\[
\widetilde G(t)
=
4
[
4L(t)-(
1-4t
)L'(t)
]
\]

is the central boundary curvature coordinate of the Loewner face. Its positivity closes the real-boundary rotor aperture near the branch point.

## Disposition

The remaining cubic cancellation has been removed algebraically:

\[
\boxed{
G(x)
=
4x^3
[
4L(x^2)-(
1-4x^2
)L'(x^2)
].
}
\]

The final central certification task is now a standard directed Taylor-remainder problem for one analytic function on \([0,0.007225]\).
