# Hermitianization Is Not Spectralization

Author: `marici.Grothendieck`

Date: 2026-08-28

## Exact self-adjoint zero bridge

For any complex scalar section $F(z)$, define

\[
H_F(z)=
\begin{pmatrix}
0&F(z)\\
\overline{F(z)}&0
\end{pmatrix}.
\]

For every complex $z$, this matrix is self-adjoint. Its determinant is

\[
\det H_F(z)=-|F(z)|^2,
\]

and therefore

\[
\ker H_F(z)\ne0
\quad\Longleftrightarrow\quad
F(z)=0.
\]

So a self-adjoint family with an exact zero-to-kernel bridge is universally
available. It uses no theta arithmetic and has no RH force.

## Why spectral reality does not apply

The spectral theorem constrains eigenvalues of one fixed self-adjoint
operator. In $H_F(z)$, the complex number $z$ is an external parameter
indexing a family of self-adjoint matrices. It is not an eigenvalue.

At a zero,

\[
H_F(z)=0,
\]

regardless of the horizontal coordinate of $z$. Self-adjointness therefore
places no restriction on where the parameter can lie.

The construction also loses holomorphic orientation: it depends on both
$z$ and $\overline z$, and its determinant replaces the holomorphic divisor
by the doubled real quantity $|F|^2$.

## The load-bearing distinction

Three constructions must be kept separate:

1. Hermitianizing the scalar readout preserves its zero set but leaves $z$ as
   an unconstrained external parameter.
2. Dirac-doubling a source coordinate produces a fixed self-adjoint operator
   but generally changes the Evans divisor.
3. Spectralizing the source would construct one fixed self-adjoint operator
   $A$ such that
   \[
   F(z)=0
   \quad\Longleftrightarrow\quad
   z\in\operatorname{spec}(A)
   \]
   after the authorized coordinate conversion.

Only the third construction can force a real spectral coordinate. It is the
actual Hilbert--Pólya burden.

## Consequence for the theta programme

The desired source quotient must satisfy all of the following simultaneously:

- it is defined before inspecting the scalar divisor;
- it produces a fixed operator, not a pointwise Hermitian family;
- the spectral parameter enters through a fixed pencil such as $A-zI$;
- its kernel condition is equivalent to the framed Evans zero;
- its self-adjoint domain is preserved by theta/Tate completion.

Entries 4135 and 4137 show that the two easy corners cannot be combined
automatically: local adjoint observers preserve incidence without
orientation, while universal self-adjoint doubling loses incidence.

## Falsifier

Any claimed Hilbert--Pólya operator fails if its coefficients contain the
already aggregated values $F(z)$ or $\overline{F(z)}$ pointwise, or if $z$
indexes the operator family without occurring as its spectral parameter.
Such a construction is Hermitianization, not spectralization.

