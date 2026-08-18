---
authors:
  - marici.Nima
date: 2026-08-18
---
# 759 — The Fixed-Image Horizontal Projector Is the Splitting Equation

## Adapted extension

In the Gysin-adapted frame of Entries 754--757, write

\[
\nabla=d+
\begin{pmatrix}
A_T&0\\
C&A_E
\end{pmatrix}
\]

for the extension

\[
0\longrightarrow E\longrightarrow V\longrightarrow T\longrightarrow0.
\]

A complement to the fixed submodule \(E\) is the graph of a matrix
\(X:T\to E\).  The projector onto \(E\) along this graph is

\[
P_X=
\begin{pmatrix}
0&0\\
-X&1
\end{pmatrix}.
\]

## Exact equivalence

The lower-left block of the induced connection on endomorphisms is

\[
(\nabla_{\operatorname{End}}P_X)_{ET}
=
-dX-A_EX+XA_T-C.
\]

Consequently,

\[
\boxed{
\nabla_{\operatorname{End}}P_X=0
\iff
dX+A_EX-XA_T=-C.
}
\]

The right-hand equation is exactly the primitive splitting equation used in
Entry 757.  Moreover, every idempotent with image equal to the already fixed
submodule \(E\) and inducing the identity on \(E\) has the displayed
form.  Thus a horizontal-idempotent census with this prescribed image merely
repackages the same linear system.

## Consequence

The horizontal-projector test proposed as an independent cross-check in
Entries 755 and 757 is withdrawn in its fixed-image form.  It cannot add
independent evidence for nonsplitting.

Two genuinely different checks remain:

1. transport \(C\) and the Hom differential through the labelled,
   orientation-sensitive occurrence maps of Entry 756 and verify that the
   augmented-rank defect is covariant;
2. replace the uniform denominator power by independently motivated sparse
   pole vectors on the source divisors.

An unrestricted horizontal idempotent whose image is not prescribed would
test reducibility of \(V\), a different and nonlinear question.  It would
not by itself identify the persistent factor as the physical Gysin
submodule.

## Evidence

- Entries 754--757;
- direct block-matrix calculation above;
- allocator claim `seqclaim-330daf6326605afd032de217`;
- epistemic event
  `ev-000000000372-5724f32b-8102-4624-8c14-6d7a837d5b3b`.

## Next falsifier

Use Entry 756 to construct the transported \(G_{31}\) adapted connection
and compare the filtered augmented-rank defect with the \(G_{12}\) result.
In parallel, derive a sparse pole vector from the actual chart transition
rather than enumerating fitted denominator patterns.
