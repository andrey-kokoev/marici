# Complex projectivization forgets the Evans winding

## Correction

Let

\[
\ell_0=\operatorname{span}(0,1),
\qquad
L_X=\operatorname{span}(X,1).
\]

The intersection condition remains exact:

\[
L_X=\ell_0
\quad\Longleftrightarrow\quad
X=0.
\]

However, the topology of the unframed line does not retain the winding of
the Evans determinant.  The transverse-line space is

\[
\mathbf{CP}^1\setminus\{\ell_0\}\cong\mathbf C.
\]

It is contractible.  Consequently every loop of complex lines transverse to
\(\ell_0\) has a null-homotopy in the transverse-line space, independently of
the winding of \(X\).

For the hostile loop \(X(\theta)=e^{i\theta}\), use the affine coordinate
\(y=X^{-1}\).  Then

\[
L_X=\operatorname{span}(1,y),
\qquad
y_r(\theta)=(1-r)e^{-i\theta},
\qquad 0\le r\le1.
\]

Every \(y_r\) is finite, so the homotopy never reaches \(\ell_0\).  At
\(r=1\) the loop is constant.  Yet the framed determinant loop
\(X:S^1\to\mathbf C^\times\) has winding one.

## Typed consequence

There are two different objects:

1. the projective boundary line \(L_X\), which detects a zero pointwise but
   forgets divisor winding;
2. the framed determinant value \(X\in\mathbf C^\times\), which retains the
   integer winding.

The forgetful map from a framed vector to its projective line kills the
topological obstruction.  Therefore a source-derived contraction of the
unframed line loop is too weak to confine zeros: such a contraction always
exists.

The global Maslov route survives only after one of the following is derived
from the source:

- a determinant-line framing whose transition law preserves the Evans
  divisor;
- a real Lagrangian reduction with a genuine Maslov class;
- another nonprojective lift carrying the same integer index.

Without one of these lifts, identifying the argument-principle winding with
the homotopy class of the complex projective line is false.

## Finite falsifier

The single loop \(X(\theta)=e^{i\theta}\) suffices:

- its determinant winding is one;
- its projective boundary-line loop contracts while remaining transverse.

Any theorem equating these two invariants without additional framed or real
structure is disproved by this witness.

## Frontier

The next source question is no longer whether the boundary line contracts.
It is which theta/Tate constructor preserves a determinant frame, or supplies
a real Lagrangian reduction, through restricted-product completion.

Grothendieck's positive reciprocal finite-cutoff example independently shows
that positivity, reciprocity, real structure, and the native symplectic Evans
bridge do not supply this missing lift.

