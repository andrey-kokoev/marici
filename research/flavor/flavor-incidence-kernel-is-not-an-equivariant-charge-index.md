# The Primitive Incidence Kernel Is Not an Equivariant Charge Index

## Question

Does WP820's incidence complex itself derive the representation-valued
character required by WP846?

## Two distinct roles for the numbers

WP820 uses

\[
B=
\begin{pmatrix}
2&-1&0\\
3&0&-1
\end{pmatrix},
\qquad
Bq=0,
\qquad
q=(1,2,3)^T.
\]

Here (q) is a primitive coefficient vector in the kernel of an integer
relation. WP846 instead treats (1,2,3) as eigenvalues of a charge operator

\[
Q=\operatorname{diag}(1,2,3)
\]

and forms the character (z+z^2+z^3). These interpretations coincide only if
the incidence complex is equivariant for that charge action.

## Exact equivariance obstruction

For an infinitesimal target action (A), equivariance would require

\[
AB=BQ.
\]

Because (Bq=0), this implies the necessary condition

\[
BQq=0.
\]

But

\[
Qq=(1,4,9)^T,
\qquad
BQq=(-2,-6)^T\ne0.
\]

Hence no (2\times2) target generator (A) can make (B) equivariant. The
kernel line is not (Q)-stable either, since (Qq) is not proportional to
(q).

## What index the complex actually supplies

The matrix (B) has rank two, a one-dimensional kernel, and zero cokernel.
Its ordinary Euler index is therefore one. Without an independently supplied
equivariant grading, the complex yields this integer index, not the
three-term character (z+z^2+z^3).

The character used in WP846 is valid labelled spectrum data once the charge
operator is admitted. It is not derived by taking the equivariant index of the
current WP820 incidence complex.

## Required repair

A source-derived representation-valued threshold memory needs a new typed
object:

1. a domain and codomain carrying admitted (U(1)) representations;
2. an equivariant differential intertwining those representations;
3. an oriented equivariant index whose character contains the primitive
   charge support;
4. a threshold theorem sewing the heavy index remainder to the active index.

Simply relabelling kernel coefficients as weights violates the interface
constructor and would manufacture the desired character from presentation
coordinates.

## Disposition

Negative derivation result. WP846 remains a conditional threshold repair, but
its character is not sourced by WP820's existing incidence matrix. The
smallest exact falsifier is (BQq=(-2,-6)^T). A genuinely equivariant source
complex must be constructed independently before holonomy probes receive
source authority.

## Verification

Run:

```text
uv run --with sympy python research/flavor/checkers/wp847_incidence_kernel_not_equivariant_charge_index.py
```
