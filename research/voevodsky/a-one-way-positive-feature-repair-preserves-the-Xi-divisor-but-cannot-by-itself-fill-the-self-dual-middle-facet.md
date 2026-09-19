# A one-way positive feature repair preserves the Xi divisor but cannot by itself fill the self-dual middle facet

A source-derived arithmetic feature `h(z)` can repair a negative radiation
kernel through a triangular enlargement

\[
T_+(z)=
\begin{pmatrix}
F_\Xi(z)&B(z)\\
0&E(z)
\end{pmatrix},
\qquad E(z)\ \text{zero-free}.
\]

Its determinant is

\[
\det T_+=\det F_\Xi\det E,
\]

so the Xi divisor is preserved while the auxiliary feature contributes
positive energy.  This is a valid orientation repair.

The self-dual middle facet imposes an additional constraint.  Reciprocal
adjoint duality sends the upper-triangular channel to the opposite orientation

\[
\mathbb D(T_+)=
\begin{pmatrix}
F_\Xi^\times&0\\
B^\times&E^\times
\end{pmatrix}.
\]

Therefore one triangular channel is not fixed by the anti-simplicial duality.
There are only two formal completions:

1. add both off-diagonal directions in one block; this creates a Schur term and
   generically moves the Xi divisor;
2. take the hyperbolic object `T_+ direct-sum D(T_+)[1]`; this is shifted
   self-dual, but its determinant contribution is canonically neutralized by
   the opposite shift and supplies no new Xi divisor comparison.

Hence one-way positivity separates divisor compilation from energy orientation
but does not provide the independent self-dual `CG` mate.  It can be an
auxiliary positive flag attached to the middle facet only after the
characteristic-to-Green correspondence is independently constructed.

The remaining bulk equation is unchanged:

\[
2aE_{\rm ar}(x)+2P=0,
\]

with `E_ar>=0` and `P` the theta forcing pairing, sourced independently.  The
one-way feature gives a candidate positive `E_ar`; it does not prove that its
boundary current equals `-P` on the lifted Xi state.
