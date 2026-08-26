# Theta history Dirac is bounded and cannot carry the Riemann ordinates

## Bounded question

Can the canonical full-history Dirac operator directly realize the nontrivial
Riemann-zero ordinates as its eigenvalues?

## Bounded history synthesis

For \(\Phi\in L^1(0,\infty)\), Young's inequality gives

\[
\|H_+c\|_2\le\|\Phi\|_1\|c\|_2.
\]

Hence (H_+) and (H_+^*) are bounded. The canonical conormal Dirac operator

\[
D_H=
\begin{pmatrix}
0&H_+^*\\
H_+&0
\end{pmatrix}
\]

is bounded and self-adjoint, with

\[
\|D_H\|=\|H_+\|\le\|\Phi\|_1.
\]

Its spectrum lies in the compact interval

\[
[-\|H_+\|,\|H_+\|].
\]

## Spectral-scale obstruction

The imaginary ordinates of the nontrivial zeta zeros are unbounded. Therefore
they cannot be the eigenvalues of the fixed bounded operator (D_H), nor can a
bounded affine rescaling of (D_H) realize them.

This rules out the direct identification

\[
D_H\psi_\gamma=\gamma\psi_\gamma
\]

for the full zero sequence.

## What the history Dirac does encode

The operator remains canonical and useful. It packages:

- full history synthesis and analysis;
- reciprocal causal variance;
- source-derived adjointness;
- the correlation operators (H_+^*H_+) and (H_+H_+^*);
- sheet character of any genuine singular state.

It is an incidence Dirac, not yet a spectral-height generator.

## Required unbounded generator

Any Hilbert--Pólya-type operator in this architecture must include an unbounded
source generator, such as logarithmic translation, dilation, or a canonical
differential operator. The history Dirac can then enter as an off-diagonal
coupling:

\[
\mathcal L
=K_{\mathrm{unbounded}}+D_H
\]

or as part of an operator pencil. The domain, relative boundedness, and
determinant section must be derived from the source.

## Relation to determinant typing

Even if a Fredholm determinant built from (D_H) matched the scalar theta
section, determinant vanishing would establish only noninvertibility of that
pencil. It would not identify the kernel's sheet character or give a uniform
singular-value bound. Those remain independent arrows, as Kitaev's determinant
hostiles show.

## Finite falsifier

Any proposal claiming that the fixed history Dirac itself has the Riemann
ordinates as spectrum fails once an ordinate exceeds \(\|H_+\|\). A nonlinear
post-processing of bounded eigenvalues is not source authority unless the
corresponding functional calculus is independently derived.

## Scope

This packet proves a spectral-scale no-go for the canonical history Dirac. It
does not rule out an unbounded source generator coupled to the history Dirac,
construct such a generator, or prove RH.
