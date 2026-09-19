# Canonical theta bordering removes the Stokes line without a left-kernel section

## Correction to the two-sided proposal

The previous right-splitting audit left a source-derived section of
`ker D(z)^dagger` as the next gate. Prior research supplies a stronger
reduction that does not require such a choice.

Use the retained decomposition

\[
X=X_0\oplus\mathbb C_\theta,
\qquad
X_0=H\oplus U_{\mathrm{ar}},
\]

and write the constructed three-port pencil as

\[
D(z)=
\begin{pmatrix}
P(z)&-w\\
-w^\dagger&0
\end{pmatrix},
\]

where

\[
P(z)=
\begin{pmatrix}
\partial_q-z&-B_\Sigma\\
-B_\Sigma^\dagger&D_U(z)
\end{pmatrix}.
\]

The retained theta coordinate gives both canonical border maps:

\[
e_\theta=(0,1),
\qquad
\ell_\theta(x,a)=a.
\]

## Bordered operator

Define

\[
G_\theta(z)=
\begin{pmatrix}
D(z)&e_\theta\\
\ell_\theta&0
\end{pmatrix}.
\]

On `X_0 direct-sum C_theta direct-sum C_aux`, this is

\[
G_\theta(z)=
\begin{pmatrix}
P(z)&-w&0\\
-w^\dagger&0&1\\
0&1&0
\end{pmatrix}.
\]

For data `(f,g,c)`, the equations are

\[
Px-wa=f,
\qquad
-w^\dagger x+b=g,
\qquad
a=c.
\]

If `P` is invertible, these have the unique solution

\[
x=P^{-1}(f+wc),
\qquad
a=c,
\qquad
b=g+w^\dagger x.
\]

Conversely, any kernel or cokernel obstruction of `P` propagates to
`G_theta`. Therefore

\[
G_\theta(z)\text{ is invertible}
\quad\Longleftrightarrow\quad
P(z)\text{ is invertible}.
\]

No left-kernel frame is chosen.

## Determinant line

At finite stage, direct block elimination gives

\[
\det G_\theta(z)=-\det P(z),
\]

independently of the Stokes coupling column `w`. In the Fredholm setting the
same elimination canonically identifies the determinant lines up to the fixed
border orientation unit.

Thus canonical theta bordering removes the global Stokes section without a
holomorphic choice of cokernel line and without a guessed arithmetic
transpose symmetry.

## Ordered-port survival

The reduction deletes only the retained scalar theta coordinate. The history
block `H`, arithmetic block `U_ar`, and their incidence `B_Sigma` remain in
`P(z)`. Since the ordered port is the odd bilateral-history coordinate, its
endpoint, Hardy, and full relative-response data survive in the transverse
pencil.

On a resolvent chart for `partial_q-z`, the remaining characteristic is

\[
M_U(z)
=
D_U(z)
+B_\Sigma^\dagger(\partial_q-z)^{-1}B_\Sigma,
\]

with signs fixed by the declared block convention.

## Revised frontier

The left Grushin normalization is not an open gate. The actual remaining
obligations are:

1. prove `P(z)` is a holomorphic Fredholm family of fixed index zero on the
   completed retained rigging;
2. construct the correctly graded arithmetic diagonal `D_U(z)`;
3. prove determinant-class control and cutoff convergence;
4. identify the relative determinant of `M_U` with a holomorphic unit times
   Xi.

This reduction is algebraically exact but supplies no Xi or RH conclusion by
itself.
