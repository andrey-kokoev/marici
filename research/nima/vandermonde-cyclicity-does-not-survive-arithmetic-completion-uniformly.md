# Vandermonde cyclicity does not survive arithmetic completion uniformly

## Finite result and completion question

The centered scale-moment tower is cyclic on every finite conductor fiber with
distinct labels. This is an algebraic statement. Completion requires a uniform
lower bound, and that stronger statement already fails on two-point fibers.

Take scale values

\[
\lambda_n=\log n,
\qquad
\lambda_{n+1}=\log(n+1),
\]

and let \(E\) average the two coordinates. The first centered moment is

\[
v_n=(1-E)
\begin{pmatrix}
\lambda_n\\
\lambda_{n+1}
\end{pmatrix}
=
\frac{\delta_n}{2}
\begin{pmatrix}
-1\\
1
\end{pmatrix},
\]

where

\[
\delta_n=\log(1+1/n).
\]

Therefore

\[
\lVert v_n\rVert=\frac{|\delta_n|}{\sqrt 2}\longrightarrow0.
\]

The finite moment map has full rank for every \(n\), but its smallest
singular value collapses. Algebraic cyclicity does not give completion-stable
observability.

## Divided-difference temptation

One can normalize the direction by dividing by the gap:

\[
\widetilde v_n=\frac{v_n}{\delta_n}.
\]

This restores a constant norm on each pair. But the normalization multiplier
grows like \(n\). It is not bounded in the unweighted completion.

Thus divided differences are a possible source rigging, not a free repair. They
must be authorized as constructors and their graph norm must be part of the
coefficient topology.

## Determinant consequence

The Vandermonde sign can remain coherent while its magnitude collapses. Hence
orientation and stability separate:

- ordered scale values determine a finite determinant sign;
- gap collapse destroys a uniform determinant-frame bound;
- no sign choice alone prevents states from escaping at completion.

For larger fibers, every close pair contributes a small factor to the
Vandermonde product. Raw monomial jets therefore become increasingly
ill-conditioned as arithmetic labels accumulate logarithmically.

## Exact next gate

The source must choose between:

1. a divided-difference or Newton-jet rigging with explicit graph norm;
2. a discrete valuation port retaining label separation;
3. a completion that accepts redundancy and quotients only after all
   source-authorized currents are continuous.

The finite falsifier for any proposed completion is the adjacent-label sequence:
if its normalized antisymmetric state has vanishing moment output, the claimed
uniform observability is false.

