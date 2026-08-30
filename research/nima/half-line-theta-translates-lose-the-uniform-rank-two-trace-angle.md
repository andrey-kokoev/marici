# Half-line theta translates lose the uniform rank-two trace angle

## Exact truncated translation law

Let

\[
g=\mathcal C h,
\qquad
\mathcal C=\partial_u^2-\frac14,
\]

and form the half-line translate

\[
g_L(u)=g(u+L),
\qquad u\ge 0.
\]

Its two relative Wronskian moments are not the moments of a bilateral translate. They are

\[
M_-(L)
=
e^{L/2}A(L),
\qquad
A(L)=\int_L^\infty e^{-v/2}g(v)\,dv,
\]

and

\[
M_+(L)
=
e^{-L/2}B(L),
\qquad
B(L)=\int_L^\infty e^{v/2}g(v)\,dv.
\]

Thus the half-line boundary terms are exactly the two weighted tails. The candidate primitive and square columns at \(L=\log p\) and \(2L\) are

\[
c(L)=
\begin{pmatrix}
e^{L/2}A(L)\\
e^{-L/2}B(L)
\end{pmatrix},
\qquad
c(2L)=
\begin{pmatrix}
e^LA(2L)\\
e^{-L}B(2L)
\end{pmatrix}.
\]

## Theta-tail asymptotics

For one theta summand, put

\[
x=\pi n^2e^{2u},
\qquad
f_n(u)=e^{u/2}e^{-x}.
\]

A direct calculation gives

\[
\mathcal C f_n
=
(4x^2-6x)f_n.
\]

The negative weighted tail is exact:

\[
\int_L^\infty e^{-u/2}\mathcal C f_n(u)\,du
=
(2x_L-1)e^{-x_L},
\qquad
x_L=\pi n^2e^{2L}.
\]

For the positive weighted tail, endpoint Laplace asymptotics give

\[
\int_L^\infty e^{u/2}\mathcal C f_n(u)\,du
=
e^L(2x_L-1)e^{-x_L}
\left(1+O(x_L^{-1})\right).
\]

The \(n=1\) summand dominates uniformly as \(L\to\infty\). Hence for the complete theta forcing,

\[
\frac{B(L)}{A(L)}
=
e^L\left(1+O(e^{-2L})\right).
\]

It follows that

\[
\frac{M_+(L)}{M_-(L)}
=
1+O(e^{-2L}).
\]

After normalizing their lengths, both \(c(L)\) and \(c(2L)\) converge to the same ray spanned by

\[
\begin{pmatrix}1\\1\end{pmatrix}.
\]

## Consequence for the proposed rank margin

For every fixed finite prime scale the two columns may be linearly independent, but their angular separation collapses as \(p=e^L\to\infty\):

\[
\sigma_{\min}
\left(
\frac{c(L)}{\|c(L)\|},
\frac{c(2L)}{\|c(2L)\|}
\right)
\longrightarrow0.
\]

The unnormalized smallest singular value also collapses because both theta tails are superexponentially small.

Therefore the raw pair of half-line theta translates at \(\log p\) and \(2\log p\) cannot supply a cutoff-uniform rank-two relative trace frame. The universal relative trace functor still has rank two, but this particular source orbit approaches a single endpoint-localized ray.

## Interpretation

This is not merely a bad normalization. Source-fixed scalar rescaling of each column can remove its size but cannot repair the vanishing angle. The collapse is caused by endpoint localization: both weighted moments sample the same increasingly narrow theta tail near their lower boundary.

A second source-authorized direction must change shape, not only scale location. Viable candidates must include one of:

- a completion-compatible scale derivative before truncation;
- a reciprocal or bilateral packet retaining the opposite tail;
- a primitive/square constructor with genuinely different local profiles;
- an independently typed Wronskian or wall-relative feature.

Any proposed repair must be tested by the normalized determinant or smallest singular value, since raw nonzero finite determinants conceal this completion failure.

## Next gate

Construct the smallest source-authorized shape-changing companion to the theta precursor and compute its two weighted tail moments. The required theorem is a uniform angular frame bound, not finite rank alone.
