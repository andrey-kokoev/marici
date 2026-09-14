# The completed endpoint polarization is the swap form with one positive and one negative parity channel

## Fourier polarization of a convolution square

Let

\[
f=g*g^*,
\qquad
g^*(x)=\overline{g(-x)}.
\]

For the Fourier--Laplace transform convention

\[
\widehat g(z)=\int g(x)e^{-izx}dx,
\]

one has

\[
\widehat f(z)
=
\widehat g(z)
\overline{\widehat g(\bar z)}.
\]

The two completed zeta endpoints correspond to the off-real spectral points

\[
z=+i/2,
\qquad z=-i/2.
\]

Put

\[
a=\widehat g(i/2),
\qquad
b=\widehat g(-i/2).
\]

Then

\[
\widehat f(i/2)=a\bar b,
\qquad
\widehat f(-i/2)=b\bar a.
\]

Therefore the endpoint sum in the explicit formula is

\[
\boxed{
\widehat f(i/2)+
\widehat f(-i/2)
=
2\operatorname{Re}(a\bar b).
}
\]

## Endpoint coefficient matrix

On the endpoint coordinate vector

\[
v=(a,b)^T,
\]

the polarization is

\[
Q_{end}(v)=v^*J_{end}v,
\qquad
\boxed{
J_{end}=
\begin{pmatrix}
0&1\\
1&0
\end{pmatrix}.
}
\]

Thus the source-fixed endpoint form is not the positive identity matrix. It is the exchange/Krein form.

Its eigenvectors are

\[
v_{even}=
\frac1{\sqrt2}
\binom{1}{1},
\qquad
v_{odd}=
\frac1{\sqrt2}
\binom{1}{-1},
\]

with eigenvalues

\[
+1,
\qquad -1.
\]

Hence

\[
\boxed{
Q_{end}(v)
=|a_{even}|^2-|a_{odd}|^2.
}
\]

The completed endpoint contains one positive and one negative parity channel before coupling to gamma and primes.

## Incorporating the Paley--Wiener evaluation metric

At support radius `L`, the evaluation Gram matrix is

\[
G_{end}(L)=
\begin{pmatrix}
2\sinh L&2L\\
2L&2\sinh L
\end{pmatrix}.
\]

Because `G_end` commutes with `J_end`, the metric-weighted endpoint operator is

\[
C_L=
G_{end}(L)^{1/2}
J_{end}
G_{end}(L)^{1/2}
=
G_{end}(L)J_{end}.
\]

Therefore

\[
\boxed{
C_L=
\begin{pmatrix}
2L&2\sinh L\\
2\sinh L&2L
\end{pmatrix}.
}
\]

Its parity eigenvalues are

\[
\lambda_{even}=2(\sinh L+L)>0,
\]

\[
\boxed{
\lambda_{odd}=2(L-\sinh L)<0
\qquad(L>0).
}
\]

The negative endpoint energy grows in magnitude like `e^L` under support exhaustion.

## Even-observer reduction

If `g` is even, then

\[
\widehat g(-z)=
\widehat g(z),
\]

so

\[
a=b.
\]

The odd endpoint coordinate vanishes and

\[
Q_{end}=2|a|^2\ge0.
\]

Thus a scalar positive endpoint model is valid on the reflection-even observer subspace. It is not valid for arbitrary translated Gaussian packets, which generally excite both parity channels.

This distinction explains why an archimedean theorem formulated for even functions can use one positive endpoint evaluation while the full translation-generated Weil criterion cannot.

## Odd-observer obstruction

If `g` is odd, then `a=-b`, and

\[
Q_{end}=-2|a|^2\le0.
\]

Therefore the endpoint sector alone already has a negative square. Gamma and prime terms must couple to this channel before positivity can hold. Adding endpoint evaluations as orthogonal positive lines changes the source form.

## Correct block positivity problem

Because `C_L` is indefinite, the ordinary positive Schur-complement criterion with `C_L>=0` does not apply. The completed form must instead be organized relative to the parity fundamental symmetry

\[
J_{end}=
P_{even}-P_{odd}.
\]

A positive completion must provide a bulk feature `B_{odd,L}` whose contribution dominates the negative endpoint square:

\[
\boxed{
Q_{bulk,L}(g)
+
2\operatorname{Re}Q_{cross,L}(g)

\ge
2(\sinh L-L)|a_{odd}(g)|^2.
}
\]

The inequality cannot be proved by treating endpoint and bulk independently, because the right side grows exponentially and the cancellation is encoded in the cross term.

## Minimal square completion

Algebraically, the odd block can be repaired if the bulk contains a vector-valued feature `F_Lg` and a contraction-compatible endpoint embedding `R_L` such that

\[
F_Lg=R_La_{odd}(g)+F_L^\perp g.
\]

Then

\[
\|F_Lg\|^2
-
\|R_La_{odd}(g)\|^2
=
\|F_L^\perp g\|^2
+
2\operatorname{Re}
\langle R_La_{odd},F_L^\perp g\rangle,
\]

so positivity requires an additional orthogonality/Green identity eliminating the final cross term. Merely matching the norm of `R_L` to `2(sinh L-L)` is insufficient.

The source must therefore identify the negative endpoint line as an actual subfeature of the gamma--prime bulk with the correct orthogonal decomposition.

## Relation to the endpoint atom audit

The earlier heat-side analysis found a positive endpoint atom at negative generator energy, rejected by the shifted kernel. The present calculation is its polarized analytic counterpart: reciprocal endpoint pairing is positive on even parity and negative on odd parity. Both show that ordinary endpoint positivity is the wrong requirement; the completed generator must remove one forbidden direction through coupling.

## Disposition

The first missing source datum is now computed:

\[
\boxed{
J_{end}=
\begin{pmatrix}0&1\\1&0\end{pmatrix},

\qquad
Q_{end}=|a_{even}|^2-|a_{odd}|^2.
}
\]

At finite Paley--Wiener radius, the negative odd eigenvalue is

\[
-2(\sinh L-L).
\]

Therefore the endpoint cannot be attached as a positive orthogonal summand. The next constructor must embed this odd endpoint evaluation into the gamma--prime bulk and derive the required orthogonal Green decomposition from the source.
