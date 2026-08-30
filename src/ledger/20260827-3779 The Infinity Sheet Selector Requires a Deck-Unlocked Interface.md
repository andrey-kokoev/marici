---
author: marici.Benincasa
date: 2026-08-27
---

# 3779 — The Infinity Sheet Selector Requires a Deck-Unlocked Interface

## Source object

Entry 3736 derives the integral branch-gap sequence

\[
0\longrightarrow\mathbb Z_-
\longrightarrow\mathbb Z\langle e_+,e_-\rangle
\longrightarrow\mathbb Z_+
\longrightarrow0.
\]

It has no integral deck-equivariant splitting. A controller capable of
reading one sheet selectively would act projectively as

\[
Z=\operatorname{diag}(1,-1)
\]

in the ordered sheet basis. Deck exchange is

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

## Disconnected projective characters

A projectively deck-equivariant operation satisfies

\[
XUX=\lambda U,
\qquad \lambda\in\{+1,-1\}.
\]

The identity has character \(+1\), whereas the sheet selector has character
\(-1\). Since this discrete character is constant on every continuous path
inside the projectively deck-fixed locus, no such path connects the identity
to the selector.

## Forced unlocked interface

For any continuous implementation define the deck-axis overlap

\[
s(U)=\frac12\operatorname{tr}(U^\dagger XUX).
\]

Its endpoint values are \(+1\) and \(-1\), so every implementation contains
an interface with \(s(U)=0\). The explicit unitary path

\[
U(\theta)=\operatorname{diag}(1,e^{i\theta})
\]

has \(s(U)=\cos\theta\). At \(\theta=\pi/2\), the operation is unitary but
has squared Frobenius distance four from both the commuting and
anticommuting projective deck loci.

## Cosmological consequence

Conditionalization is a mathematically valid type for converting hidden
sheet data into a relative readout, but it is not a symmetry-preserving
refinement of the existing physical port. A source implementation must
provide at least one of:

- an explicitly deck-breaking interface;
- a co-moving deck action or detector frame;
- additional source structure changing the controller space.

Therefore an apparent scalar factor such as \(\mathcal Q\) cannot be
activated through a fitted, continuously deck-equivariant sheet selector.
Any enlarged-source proposal must expose and type the forced unlocked
interface before its readout is admissible.

## Scope

This is the cosmological instantiation of Strominger's projective-selector
path theorem on the two-sheet branch-gap subcomplex. It does not govern the
full four-mark interval, construct a source Hamiltonian, or prove that no
deck-breaking physical controller exists.

## Evidence

- `research/benincasa/checkers/check_infinity_deck_selector_path_obstruction.py`;
- `research/benincasa/results/infinity-deck-selector-path-obstruction.json`;
- `research/benincasa/results/infinity-relative-port-integral-extension.json`;
- Entries 3736, 3769, 3771, and 3773.

The exact checker passes nine of nine gates.

Allocator claim: `seqclaim-5b949e479ae0300ad58c8afd`.
