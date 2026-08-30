# A Two-Dimensional Coherence Factor Is the Minimal Conditional Completion

## Constructive escape

Let (H_{mathrm{mag}}) be the magnetic endpoint space and attach an independent
two-dimensional coherence factor (C). On

\[
H_{mathrm{ext}}=H_{mathrm{mag}}\otimes C,
\]

define the selector projector

\[
P=I_{\mathrm{mag}}\otimes |1\rangle\langle1|.
\]

Every magnetic operation (A\otimes I_C) commutes with (P), including
operations that are irreducible on (H_{mathrm{mag}}). The earlier Schur
obstruction disappears because the selector now lives in the multiplicity
factor, not inside the irreducible magnetic representation.

## Complete conditional instrument

The four capabilities have exact tensor-factor representatives:

```text
coherent preparation       I magnetic tensor Hadamard port
protected magnetic action  A magnetic tensor I coherence
relative central sign      I magnetic tensor Z
complementary readout       I magnetic tensor Hadamard port
```

Using unnormalized vectors, the prepared route state is

\[
|+\rangle=\begin{pmatrix}1\\1\end{pmatrix}.
\]

The selective central sign gives (|-\rangle=(1,-1)^T), and complementary
readout separates them exactly:

\[
H|+\rangle=\begin{pmatrix}2\\0\end{pmatrix},
\qquad
H|-\rangle=\begin{pmatrix}0\\2\end{pmatrix}.
\]

No one-dimensional factor can contain two linearly independent route states,
so dimension two is minimal.

## What has and has not been solved

This is a mathematical completion of the capability packet, conditional on a
source supplying two items:

1. the coherence factor itself;
2. authority for the metaplectic loop to act selectively so that its central
   sign becomes (Z) on that factor.

Neither follows from the magnetic endpoint representation. The construction
therefore identifies the missing object exactly but does not manufacture its
authority.

## Categorical meaning

The coherence factor converts the nonrepresentable horizontal port into an
ordinary operation on a new tensor factor without placing it in the magnetic
commutant. Protection and interference coexist because they act on commuting
factors. This is the minimal algebraic realization of the partial double
category found in Entry 3756.

## Evidence replay

```powershell
C:\Users\andrey\.local\bin\python.exe research/strominger/checkers/minimal_coherence_factor_completion_checks.py
```
