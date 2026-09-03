# The Schur gate is an endpoint atom and Christoffel bound

## Question

What does the distinguished endpoint feature become in the moment and Jacobi presentations?

## Finite Christoffel form

Fix `t,h` and rank `N+1`. Let

\[
A_N=(L_{\Gamma+\mathbb P}(t,h)_{ij})_{0\le i,j\le N},
\qquad
y_E=e^{h/4},
\qquad
v_N=(1,y_E,\ldots,y_E^N)^T.
\]

Assume first that `A_N` is positive definite. The matrix determinant lemma gives

\[
\frac{\det(A_N-cv_Nv_N^*)}{\det A_N}
=
1-c\,v_N^*A_N^{-1}v_N.
\]

If `p_0,...,p_N` are the orthonormal polynomials for the remainder moment functional, then

\[
K_N(y_E,y_E)
=
v_N^*A_N^{-1}v_N
=
\sum_{k=0}^N|p_k(y_E)|^2.
\]

Hence endpoint subtraction is admissible at rank `N+1` exactly when

\[
cK_N(y_E,y_E)\le1.
\]

The singular case uses the same range condition and pseudoinverse kernel.

## Infinite-rank meaning

For a determinate positive representing measure `mu_R`, the Christoffel kernels increase with `N`. At a point atom,

\[
K_N(y_E,y_E)\uparrow\frac1{\mu_R(\{y_E\})};
\]

without an atom at `y_E`, the limit diverges under the usual density hypotheses.

Therefore coherent subtraction of `c delta_(y_E)` is not merely an abstract norm estimate. It asks the positive remainder measure to contain the endpoint atom with mass at least `c`:

\[
\mu_R(\{e^{h/4}\})\ge
(e^{h/4}-1)e^{t/4}.
\]

After subtracting that atom, the residual measure must lie in the contraction support `[0,1]`.

## Jacobi and J-fraction target

The Christoffel kernel is computable from the Jacobi recurrence. The source-level induction can therefore be split into:

1. positive Jacobi recurrence coefficients for the remainder localizer;
2. a distinguished pole of its Stieltjes transform at `y_E=e^(h/4)`;
3. residue at least `c`;
4. residual support contained in `[0,1]`.

This is more informative than a search for arbitrary positive J-fraction coefficients: it identifies the pole and residue that completion must supply.

## Conditional spectral check

Under RH, the remainder localizer measure is exactly the positive zero-side localizer measure plus `c delta_(y_E)`. The atom has mass exactly `c`; endpoint subtraction removes it and leaves the zero-side contraction measure. This explains why the Schur inequality is the correct boundary condition.

## Falsifiers

The route fails if the remainder Hankel cone is indefinite, if its determinate measure lacks the endpoint atom, if the atom has mass below `c`, or if residual support extends beyond `[0,1]`.

## Boundary

No positive remainder measure or J-fraction has been constructed from the endpoint--gamma--prime source. The atom statement is an equivalent target once positivity and determinacy are available, not independent evidence for them.

## Disposition

Replace the generic distinguished-feature search by a sharper prior-research query: find a remainder J-fraction or Stieltjes transform with an explicit pole at `e^(h/4)`, residue `c`, and a residual contraction measure. This directly connects the endpoint completion term to the order-two Stieltjes/Jacobi branch.