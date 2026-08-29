# Twisted theta histories give exact normalized completion trace columns

## Theta precursor and completion

Let

\[
h(u)=\frac12e^{u/2}\vartheta(e^{2u}),
\qquad
\Phi=\left(\partial_u^2-\frac14\right)h.
\]

Modularity makes \(h\) even. Its asymptotics are

\[
h(u)\sim\frac12e^{u/2}
\quad(u\to+\infty),
\]

and

\[
h(u)\sim\frac12e^{-u/2}
\quad(u\to-\infty).
\]

Define the two Wronskian traces

\[
\mathcal B_-(h;u)
=
e^{-u/2}
\left(h'(u)+\frac12h(u)\right),
\]

\[
\mathcal B_+(h;u)
=
e^{u/2}
\left(h'(u)-\frac12h(u)\right).
\]

Then

\[
\mathcal B_-(h;+\infty)=\frac12,
\qquad
\mathcal B_-(h;-\infty)=0,
\]

and

\[
\mathcal B_+(h;+\infty)=0,
\qquad
\mathcal B_+(h;-\infty)=-\frac12.
\]

## Exact weighted moments

The relative Green identities give

\[
M_-(\Phi)
=
\int_{\mathbb R}e^{-u/2}\Phi(u)\,du
=
\Delta\mathcal B_-(h)
=
\frac12,
\]

and

\[
M_+(\Phi)
=
\int_{\mathbb R}e^{u/2}\Phi(u)\,du
=
\Delta\mathcal B_+(h)
=
\frac12.
\]

Thus the completed theta forcing has exact even trace column

\[
v_0=
\begin{pmatrix}
\frac12\\
\frac12
\end{pmatrix}.
\]

For the reciprocal-odd companion \(\Phi'\), integration by parts yields

\[
M_-(\Phi')
=
\frac12M_-(\Phi)
=
\frac14,
\]

and

\[
M_+(\Phi')
=
-\frac12M_+(\Phi)
=
-\frac14.
\]

Hence

\[
v_1=
\begin{pmatrix}
\frac14\\
-\frac14
\end{pmatrix}.
\]

The normalized determinant is exact:

\[
\det(v_0,v_1)=-\frac14.
\]

## Even and odd ports

Under the normalized Hadamard pushforward,

\[
w_{1/2}
=
\frac{M_-+M_+}{\sqrt2},
\qquad
j_{1/2}
=
\frac{M_+-M_-}{\sqrt2},
\]

one obtains

\[
\Phi:
\quad
(w_{1/2},j_{1/2})
=
\left(\frac1{\sqrt2},0\right),
\]

and

\[
\Phi':
\quad
(w_{1/2},j_{1/2})
=
\left(0,-\frac1{2\sqrt2}\right).
\]

Thus the twisted history pair separates the completion wall and reciprocal jump with source-fixed normalization and sign.

## Linking consequence

The odd Wronskian coordinate of the source derivative is exactly

\[
j_{1/2}(\Phi')
=
-\frac1{2\sqrt2}.
\]

Any Euler-ratio or Adams odd port claiming to represent the same constructor must map to this value after applying the frozen arithmetic coefficient and sheet convention. The proportionality constant is no longer free.

## Remaining analytic gate

The algebraic linking normalization is closed. What remains is to construct the exponentially twisted relative graph spaces for the two first-order histories and prove closure, primewise assembly, and Mellin transport without losing this endpoint normalization.
