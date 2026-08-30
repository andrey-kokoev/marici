# Even Fourier completion does not supply reverse source incidence

Author: marici.Grothendieck

Date: 2026-08-26

Status: exact separation of boundary and bulk constructors

## Question

Reflection-even completion makes the normalized Fourier transform a
self-adjoint involution and its graph a Lagrangian boundary relation. Could
the same involution also turn the one-way theta forcing into the missing
adjoint backreaction?

## Exact finite answer

On the minimal even boundary chart, write

\[
F_+=
\begin{pmatrix}
1/\sqrt3&\sqrt{2/3}\\
\sqrt{2/3}&-1/\sqrt3
\end{pmatrix}
\]

and let the forward source incidence be

\[
N_f=\begin{pmatrix}0&f\\0&0\end{pmatrix}.
\]

Direct conjugation gives

\[
F_+N_fF_+-N_f^*
=
\frac f3
\begin{pmatrix}
\sqrt2&-1\\
-1&-\sqrt2
\end{pmatrix}.
\]

For nonzero \(f\), this residual has rank two. Therefore even Fourier
transport does not supply the missing lower incidence.

## Meaning

Two advances must remain separate:

- Fourier evenness selects a maximal isotropic boundary relation.
- Reciprocal adjoint incidence would make the driven bulk system symmetric.

The first does not imply the second. Boundary phase rigidity cannot repair a
one-way internal coupling.

This prevents a false closure of the RH programme. The normalized Fourier
graph may be the correct boundary condition, yet there is still no fixed
self-adjoint carrier whose Cauchy data can meet that graph.

## Remaining constructor

The missing object is now irreducibly a reverse source map

\[
G\longmapsto fG
\]

into the source channel, with the correct primitive, square, seam, and
archimedean typing. It must be derived independently from the labelled
theta/Tate source. Neither modular symmetry, evenness, nor metaplectic phase
normalization produces it.

## Falsifier for any proposed repair

At the smallest finite boundary chart, form the complete forward coupling
and the claimed source-derived reverse coupling. Their adjoint residual must
vanish as a typed matrix before scalar projection. A metric fitted after the
calculation or a cancellation using the target determinant is inadmissible.

## Scope

The full-rank residual is exact in the minimal even Fourier chart. A richer
source module may contain an additional reverse-incidence channel; this result
shows that it is not already contained in Fourier conjugation of the forward
tail coupling.

## Verification

The checker verifies the even Fourier involution and computes the exact
full-rank conjugation residual.
