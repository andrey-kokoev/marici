# One S-lemma block certifies the full affine route margin

## Question

Can the base norm, omitted-route width, and base–remainder coherence be certified together without separately bounding three quantities?

## Affine route problem

Let \(b\) be the complete route image of a base lift, \(R\) the route variation, and let admissible displacements satisfy

\[
w^*Hw\le1,
\qquad
H>0.
\]

The exact target is

\[
\|b+Rw\|^2\le\rho^2
\]

for every admissible \(w\), with \(\rho<1\).

Expanding gives

\[
\|b\|^2
+2\operatorname{Re}\langle R^*b,w\rangle
+w^*R^*Rw
\le\rho^2.
\]

## Augmented certificate

By the S-lemma, because the ellipsoid has an interior point, the affine route bound is equivalent to existence of \(\lambda\ge0\) such that

\[
\begin{pmatrix}
\rho^2-\|b\|^2-\lambda & -b^*R\\
-R^*b & \lambda H-R^*R
\end{pmatrix}
\ge0.
\]

This single positive-semidefinite block includes the base norm, route width, and coherence cross term. It can certify cases where separately maximizing each term is conservative.

## Exact scalar model

Take

\[
H=1,
\qquad
b=\frac12,
\qquad
R=\frac14.
\]

Over \(|w|\le1\), the exact maximum is

\[
\max\left|\frac12+rac14w\right|^2
=\frac9{16}.
\]

At \(\rho^2=9/16\), the multiplier \(\lambda=3/16\) makes the augmented block positive semidefinite with zero determinant. A smaller target \(\rho^2=1/2\) fails.

## Source and support gates

The matrix entries must be formed from one physical target inner product and one source-derived admissibility form. Independent bounds substituted into the block do not establish its cross terms.

For semidefinite \(H\), one must first quotient or constrain its null directions; otherwise the interior hypothesis fails and unbounded route-visible directions may remain. A generalized S-lemma requires its own hypotheses and cannot be assumed from the positive-definite case.

## Prime-uniform gate

A confinement theorem needs one \(\rho<1\) and admissible multipliers \(\lambda_p\) for every prime. The multipliers may depend on the prime, but the certified \(\rho\) must not approach one.

## Verification

`research/aspect/checkers/check_affine_route_s_lemma.py` verifies the sharp augmented block, zero determinant at the optimum, direct endpoint maximum, and failure of a smaller target using exact rationals.

## Disposition

The strongest compressed owner target is now the augmented block inequality. It supersedes separate estimates of \(q_0\), \(\gamma\), and \(\kappa\) when the complete affine route data \((b_p,R_p,H_p)\) are available.
