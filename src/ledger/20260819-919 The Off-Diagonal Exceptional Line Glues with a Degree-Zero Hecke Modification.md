# 919 — The Off-Diagonal Exceptional Line Glues with a Degree-Zero Hecke Modification

## Globalization problem

Entry 918 constructs the off-diagonal exceptional image in the (a)-chart of

\[
E=\mathbf P(n_a,n_y,n_q),
\]

where

\[
n_a=A_4-1,
\qquad
n_y=Y-1,
\qquad
n_q=Q-1.
\]

Its scalar factor is (1/U), with

\[
U=\frac{n_y}{n_a}.
\]

The projective image is constant locally. The remaining question is whether this line glues over all three standard Rees charts.

## Chart factors

Use the following coordinates.

On the (a)-chart:

\[
U=\frac{n_y}{n_a},
\qquad
V=\frac{n_q}{n_a},
\qquad
f_a=\frac1U.
\]

On the (y)-chart:

\[
A=\frac{n_a}{n_y},
\qquad
W=\frac{n_q}{n_y},
\qquad
f_y=A.
\]

On the (q)-chart:

\[
C=\frac{n_a}{n_q},
\qquad
D=\frac{n_y}{n_q},
\qquad
f_q=\frac CD.
\]

## Exact overlap audit

The Symbolica checker verifies

\[
f_y\big|_{a\cap y}=A=\frac1U=f_a,
\]

\[
f_q\big|_{a\cap q}=\frac{1/V}{U/V}=\frac1U=f_a,
\]

and

\[
f_q\big|_{y\cap q}=\frac{A/W}{1/W}=A=f_y.
\]

No additional unit or sign appears. Therefore the rank-one projective image of Entry 918 glues globally on (E).

## Global divisor

The common rational factor is

\[
f=\frac{n_a}{n_y}.
\]

Its divisor is

\[
\boxed{\operatorname{div}(f)=D_a-D_y,}
\]

where

\[
D_a=\{n_a=0\},
\qquad
D_y=\{n_y=0\}.
\]

The (q)-direction has coefficient zero. The divisor has projective degree zero.

Thus the globally typed coefficient object is a constant projective line with a degree-zero Hecke/Cartier lattice modification:

\[
\boxed{
\mathcal L_{\rm off}^{\rm mer}
=
\mathbf Q\langle r_{\rm tan}\rangle
\otimes
\mathcal O_E(D_a-D_y).
}
\]

## Correction to the local description

Entry 918's (a)-chart pole at (U=0) is the (D_y) part of this divisor. The complementary zero on (D_a) lies outside that affine chart and becomes visible only after gluing. The global datum is therefore (D_a-D_y), not merely a single local pole.

## Narrow conclusion

The off-diagonal order dependence is completely absorbed by the existing Rees exceptional geometry:

\[
\boxed{
\text{constant projective line}
+
\text{degree-zero lattice modification }D_a-D_y.
}
\]

No new carrier cell, divisor, or fitted normalization is introduced.

## Next falsifier

Test the reflected (z)-flag and the reflection overlap. The expected divisor is

\[
D_a-D_z.
\]

The decisive question is whether the (y)- and (z)-lines are exchanged strictly by the source reflection or require an additional sign/unit on their common exceptional atlas.
