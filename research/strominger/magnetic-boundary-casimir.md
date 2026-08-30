# The even Schur pivot is a quadratic grade Casimir

Let

\[
L_a(t)=(1+t)^{-a}
=\sum_{g\ge0}(-1)^ga^{\overline g}\frac{t^g}{g!}
\]

be the left-endpoint grade-generating function, and let

\[
\Theta=t\frac{d}{dt}.
\]

The minus and odd-plus pivots are first-order boundary characters:

\[
u_g=[t^g/g!]\,[-(\Theta+a+q-1)L_a],
\]

\[
v_g^{\mathrm{odd}}
=[t^g/g!]\,[(\Theta+a-q-1)L_a].
\]

These give

\[
u_g=(-1)^{g+1}(a+g+q-1)a^{\overline g},
\]

\[
v_g^{\mathrm{odd}}
=(-1)^g(a+g-q-1)a^{\overline g}.
\]

For the even lane, introduce the boundary primitive

\[
J_a(t)=-\int_0^tL_a(u)\,du
=\sum_{g\ge1}(-1)^ga^{\overline{g-1}}\frac{t^g}{g!}.
\]

Then the renormalized plus pivot is

\[
\boxed{
v_g^{\mathrm{even}}
=[t^g/g!]\,q\Theta(\Theta+h-1)J_a.
}
\]

Since

\[
\Theta(\Theta+h-1)\frac{t^g}{g!}
=g(g+h-1)\frac{t^g}{g!},
\]

one obtains directly

\[
v_g^{\mathrm{even}}
=(-1)^gqg(g+h-1)a^{\overline{g-1}}.
\]

At the rigid offset `h=4`, the eigenvalue is

\[
\boxed{g(g+3)}.
\]

Thus the even collision does not merely introduce an unexplained adjacent
coefficient.  After Schur elimination it integrates once along the endpoint
sequence and then applies the quadratic grade Casimir.  Odd transport remains
first order because no endpoint collision occurs.

The quadratic operator is minimal: no affine function of `Theta` can reproduce
`g(g+h-1)` for all grades.  This explains why the even lane contains genuinely
more local response than odd endpoint localization.

The checker proves all coefficient identities formally, with audits through
grade 50.  What remains for the unbounded matrix theorem is to identify this
boundary Casimir action directly inside the order-four Schur elimination,
rather than recognizing its resulting pivot character afterward.
