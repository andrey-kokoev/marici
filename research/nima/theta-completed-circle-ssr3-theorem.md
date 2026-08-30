# Completed circle spectral kernel is globally SSR3

## Result

For

\[
b(t,x)=t^{5/4}x(2\pi tx-3)e^{-\pi tx},
\qquad t\ge1,\quad x\ge1,
\]

the ordered minors have the reverse-sign-regular signs through order three:

\[
\operatorname{sgn}\det[b(t_i,x_j)]_{i,j=1}^k
=(-1)^{k(k-1)/2},
\qquad k=1,2,3,
\]

whenever \(t_1<\cdots<t_k\) and \(x_1<\cdots<x_k\).

Thus Grothendieck's source-derived completed-circle spectral family is
globally strict reverse-sign-regular of order three, not merely positive.

## Order one and two

Order one is the source inequality

\[
2\pi tx-3>0.
\]

Order two follows from monotonicity of the spectral ratio. With
\(q=\pi tx\),

\[
\phi(q)=\frac{2q}{2q-3}-q,
\qquad
\phi'(q)=-1-\frac6{(2q-3)^2}<0.
\]

Therefore, for \(x_2>x_1\),
\(b(t,x_2)/b(t,x_1)\) strictly decreases in \(t\), so every ordered
two-by-two minor is negative.

## Order-three Wronskian

Positive row and column factors do not change signs. Put \(y=\pi t\) and
consider

\[
f_y(x)=(2yx-3)e^{-yx}.
\]

Its first derivatives are

\[
f_y'(x)=y(5-2yx)e^{-yx},
\]

\[
f_y''(x)=y^2(2yx-7)e^{-yx}.
\]

For \(y_1<y_2<y_3\), factor the positive exponentials from their Wronskian.
The remaining alternant has columns

\[
2xy-3,\qquad 5y-2xy^2,\qquad 2xy^3-7y^2.
\]

Cauchy-Binet expansion in the monomial basis gives

\[
W
=e^{-x(y_1+y_2+y_3)}
\prod_{i<j}(y_j-y_i)\,P(z_1,z_2,z_3),
\]

where \(z_i=xy_i\) and

\[
P=105-30e_1(z)+12e_2(z)-8e_3(z).
\]

For example,

\[
\frac{\partial P}{\partial z_1}
=-30+12(z_2+z_3)-8z_2z_3.
\]

On \(z_2,z_3\ge3\), this derivative is at most its boundary value
\(-30\), because its derivatives in either remaining variable are
\(12-8z<0\). The same holds cyclically. Hence \(P\) is strictly decreasing
in every coordinate on the larger chamber \(z_i\ge3\). At its upper
boundary maximum,

\[
P(3,3,3)=105-270+324-216=-57<0.
\]

The actual source domain has \(z_i=\pi tx_i\ge\pi>3\), so \(W<0\)
everywhere.

The nonvanishing order-one, order-two, and order-three initial Wronskians
make the three functions an extended complete Chebyshev system in \(x\).
The generalized Vandermonde criterion therefore gives strictly negative
ordered three-by-three evaluation determinants.

## Verification

The exact checker:

1. expands the three derivative columns;
2. verifies the alternant identity
   \(D=V(105-30xe_1(y)+12x^2e_2(y)-8x^3e_3(y))\)
   on a separating rational test family;
3. checks the derivative boundary argument using exact integers;
4. retains the earlier 887-minor high-precision scan as hostile numerical
   evidence through order six.

The identity is algebraic; the scan is not used as proof.

## RH relevance and boundary

SSR3 is a source-local operator variation law derived before scalar trace.
It is therefore not another scalar positivity reformulation and is not
equivalent by construction to the Weil/Pick kernel.

However:

- SSR3 does not establish sign regularity of all orders;
- total positivity of the spectral kernel does not automatically transfer
  to a real-zero theorem for its infinite trace mixture;
- no RH conclusion follows without a precise variation-diminishing or
  Pólya-frequency theorem whose hypotheses include the completed cosine
  transform.

The next decisive target is order four. The previous bounded scan predicts
the positive sign, but the symbolic Wronskian gains another polynomial
factor whose sign must be proved or finitely falsified.

## Status

\[
\boxed{\mathrm{SSR}_3\text{ proved globally on }t\ge1,\ x\ge1.}
\]

