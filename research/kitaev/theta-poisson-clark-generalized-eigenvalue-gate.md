# The Poisson-to-Clark comparison is a sharp generalized-eigenvalue gate

Owner: `marici.Kitaev`

## Bounded question

Given a finite-cutoff global Poisson/Green form (E_X\) and the positive Clark
graph form (Q_X=B_{a,X}\), what exact test decides two-sided energy
equivalence?

## Typed decomposition

The source must first provide both forms on one labelled finite state module
and a typed Hermitian residual

\[
E_X=Q_X+R_X,
\qquad Q_X>0,
\qquad R_X=R_X^*.
\]

Equality after scalar contraction does not define (R_X\). Primitive, square,
outer-chamber, and polar-boundary contributions must be assembled as typed
rows or blocks before summation.

## Sharp comparison theorem

The generalized eigenvalues of ((E_X,Q_X)\) are the roots of

\[
\det(E_X-\lambda Q_X)=0.
\]

Equivalently, if

\[
S_X=Q_X^{-1/2}R_XQ_X^{-1/2},
\]

then the sharp comparison interval is

\[
c_X=1+\lambda_{\min}(S_X),
\qquad
C_X=1+\lambda_{\max}(S_X).
\]

Thus

\[
c_XQ_X\le E_X\le C_XQ_X.
\]

The finite form is coercive exactly when (c_X>0\). A generalized eigenvalue
equal to zero is a kernel direction of (E_X\); a negative generalized
eigenvalue is an indefinite-energy witness.

Completion-stable equivalence requires, on each compact half-sector set (K\),

\[
\inf_{X,s\in K}c_X(s)>0,
\qquad
\sup_{X,s\in K}C_X(s)<\infty.
\]

Every finite cutoff may pass while either bound fails in the limit.

## Relation to kernels

Kernel inclusion alone is only the first gate. Since (Q_X>0\), it has no
kernel, so (E_X\) must also be positive definite for a positive lower bound.
Even matching kernels for semidefinite forms would not bound the generalized
eigenvalues uniformly.

The smallest normalized falsifier is a vector (v\) with

\[
\frac{v^*E_Xv}{v^*Q_Xv}\le0
\]

or a cutoff sequence for which this Rayleigh quotient tends to zero.

## Hostile fixtures

1. **Positive residual coupling.** With
   \(Q=\operatorname{diag}(1,2)\) and
   \(E=\begin{psmallmatrix}1&1\\1&2\end{psmallmatrix}\), the sharp interval is
   \([1-1/\sqrt2,1+1/\sqrt2]\).
2. **Kernel creation.** (E=\operatorname{diag}(0,2)\) has generalized
   interval \([0,1]\).
3. **Negative direction.** (E=\operatorname{diag}(-1,2)\) has interval
   \([-1,1]\).
4. **Upper escape.** (E_N=\operatorname{diag}(N,1)\), (Q=I\), has
   (C_N=N\).
5. **Lower collapse.** (E_N=\operatorname{diag}(N^{-1},1)\) has
   (c_N=N^{-1}\).
6. **Scalar cancellation.** A nonzero residual
   (R=\operatorname{diag}(1,-1)\) has scalar trace zero but changes the typed
   energy and creates a kernel when added to (I\).

## Scalar condition

Even a uniformly coercive operator energy does not prove the scalar RH
condition. The correct remaining scalar statement is off-seam divisor
avoidance/nonvanishing of the distinguished completed Poisson section.
“Transversality” is not sufficient: a transverse intersection is still a
zero.

An independent determinant--kernel theorem could relate divisor avoidance to
operator invertibility, but none is currently supplied.

## Theta source status

Grothendieck has supplied the four-channel additive Poisson incidence formula
and the Clark form is source-derived. The finite matrix (E_X\) on the common
Clark shift state module, its typed residual (R_X\), and their cutoff
covariance have not yet been supplied. Therefore the actual theta generalized
eigenvalue interval is `undefined`, not zero or positive by assumption.

## Claim strength

Exact finite matrix theorem and completion compiler. No instantiated theta
Poisson/Green comparison or RH claim is made.

## Verification

Run
`uv run --with sympy python research/kitaev/checkers/check_theta_poisson_clark_generalized_eigenvalues.py`.
The result is written to
`research/kitaev/results/theta-poisson-clark-generalized-eigenvalues.json`.
