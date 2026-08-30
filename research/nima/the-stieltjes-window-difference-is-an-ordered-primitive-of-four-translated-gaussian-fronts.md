# The Stieltjes window difference is exactly an ordered primitive of four translated Gaussian fronts

## Window derivative

Let

\[
H'(q)=-f_0(q),
\qquad
f_0(q)=e^{-\pi q^2},
\]

and

\[
W_t(q)=H(q+t)-H(q-t).
\]

With the translation convention

\[
(U_af)(q)=f(q+a),
\]

differentiation in \(q\) gives

\[
DW_t
=
U_{-t}f_0-U_tf_0.
\]

For \(L=\log p\), define

\[
d_p=W_{2L}-W_L.
\]

Then

\[
Dd_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

Write this four-front boundary packet as

\[
b_p
=
U_{-2L}f_0-U_{2L}f_0-U_{-L}f_0+U_Lf_0.
\]

## Wall cancellation

Every translate of \(f_0\) has the same total mass. The four coefficients of
\(b_p\) sum to zero, so

\[
\int_{\mathbb R}b_p(q)\,dq=0.
\]

Thus \(b_p\) lies in the wall-killed sector on which the ordered bilateral
Volterra port is an unambiguous inverse derivative.

## Exact ordered-port factorization

The source ordered port satisfies

\[
DS_{\mathrm{ord}}=-2I
\]

on the rapid wall-killed core. Since \(Dd_p=b_p\) and \(d_p\) decays at both
ends, the integration constant is fixed. Therefore

\[
d_p
=
-\frac12S_{\mathrm{ord}}b_p.
\]

Equivalently,

\[
W_{2L}-W_L
=
-\frac12S_{\mathrm{ord}}
\left(
U_{-2L}-U_{2L}-U_{-L}+U_L
\right)f_0.
\]

This is an exact constructor identity before theta completion or Green
polarization.

## Reciprocal character

Reflection sends \(U_a\) to \(U_{-a}\), hence

\[
Rb_p=-b_p.
\]

The ordered port is also reciprocal odd. Their composite is reciprocal even,
as required for the scalar window difference:

\[
Rd_p=d_p.
\]

Thus the orientation is not lost in the final even scalar. It is carried by
two independently odd constructors whose characters multiply to the even
window character.

## Relation to the first Adams edge

The raw Stieltjes target is no longer an opaque endpoint function. It factors
through the same ordered history constructor already used to resolve the
connection curvature:

\[
\text{four translated fronts}
\longrightarrow
S_{\mathrm{ord}}
\longrightarrow
d_p.
\]

The remaining comparison with the wall-subtracted theta packet can therefore
be moved one derivative earlier. Instead of comparing two primitive histories
directly, it suffices to compare:

\[
b_p
\]

with the differentiated relative theta packet, while separately checking that
both use the same ordered inverse and wall convention.

This removes the integration-constant ambiguity from the final
constructor-identification theorem.

## Fourier check

Under the convention in which translation has multiplier \(e^{ia\xi}\),

\[
\widehat b_p(\xi)
=
2i\left(
\sin(L\xi)-\sin(2L\xi)
\right)\widehat f_0(\xi).
\]

The multiplier vanishes at \(\xi=0\), confirming zero mass. Division by
\(i\xi\) is therefore regular at the origin and recovers the Fourier transform
of \(d_p\).

## Hostile

Comparing \(d_p\) to the theta bulk after applying unrelated one-sided
primitives can match derivatives but differ by a constant wall. The exact
factorization through \(S_{\mathrm{ord}}\) forbids that ambiguity and retains
the reciprocal orientation hidden by the final even scalar.
