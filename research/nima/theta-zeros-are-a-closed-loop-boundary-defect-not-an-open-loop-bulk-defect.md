# Theta zeros are a closed-loop boundary defect, not an open-loop bulk defect

## Control-theoretic typing

A source-derived tail or Volterra operator can be canonically solvable even when the completed scalar section has zeros. This is not a contradiction. The bulk operator describes the open system; the endpoint and reciprocal seam close a feedback loop.

Write a source operator in block form:

\[
\mathcal D(z)
=
\begin{pmatrix}
A(z) & B(z)\\
C(z) & D(z)
\end{pmatrix}.
\]

Here:

- \(A(z)\) is the causal tail or bulk evolution;
- \(B(z)\) injects boundary data into the bulk;
- \(C(z)\) reads the propagated bulk state at the boundary;
- \(D(z)\) is the direct endpoint–seam channel.

If \(A(z)\) is invertible, eliminating the bulk gives the boundary Schur complement

\[
S_{\partial}(z)
=
D(z)-C(z)A(z)^{-1}B(z).
\]

In finite dimensions,

\[
\det\mathcal D(z)
=
\det A(z)\det S_{\partial}(z).
\]

The Fredholm or determinant-line version has the same architectural meaning when its domains and determinant class are properly declared.

## Open-loop contraction is insufficient

Causal Volterra operators are often quasinilpotent. Their resolvents may be constructed by a convergent Neumann–Volterra series without any zero information.

That proves

\[
\ker A(z)=0.
\]

It does not prove

\[
\ker\mathcal D(z)=0.
\]

A zero may arise entirely from

\[
\ker S_{\partial}(z)\ne0.
\]

Therefore a canonical contracting homotopy for the tail complex alone cannot imply RH. It contracts the open-loop bulk while leaving the closed-loop boundary defect untouched.

## Location of the scalar section

The completed scalar section must be derived, up to a nonvanishing unit, from the closed boundary object:

\[
\Xi(z)
=
u(z)\det S_{\partial}(z),
\qquad
u(z)\ne0.
\]

This is consistent with the earlier provenance result: endpoint, gamma, and prime flux combine only after the boundary closure.

If instead \(\Xi\) is attached to \(A(z)\), the model has erased the endpoint–seam feedback where the antidiagonal zero-state actually lives.

## Exact feedback form

When the direct boundary block is normalized to the identity, define the loop operator

\[
L(z)=C(z)A(z)^{-1}B(z).
\]

Then

\[
S_{\partial}(z)=I-L(z).
\]

An off-seam zero is a closed-loop state satisfying

\[
L(z)v=v.
\]

Thus the missing orientation theorem is an independently derived exclusion of the eigenvalue \(1\) for the source-defined loop operator in each open half-plane.

This is more precise than generic positivity or acyclicity.

## Noncircular sufficient mechanisms

Three source-derived laws could exclude the closed-loop state without dividing by \(\Xi\):

1. Small gain:
   \[
   \|L(z)\|<1.
   \]

2. Strict dissipativity:
   \[
   \operatorname{Re}\langle v,(I-L(z))v\rangle>0
   \]
   for nonzero admissible \(v\).

3. Causal triangularity or grading:
   \(L(z)\) strictly raises a well-founded source grade, so it cannot have eigenvalue \(1\) on the completed admissible module.

Each law must include boundary and seam channels. Establishing it only for \(A(z)\) is irrelevant to the divisor.

## Why the earlier lanes stalled

The recurring obstructions now have one control interpretation:

- positive Clark bulk proves internal plant energy;
- the seam reconstruction failure says the output channel is independent state;
- the forcing current is the feedback cross term;
- the completed Pick/Weil kernel is the closed-loop boundary form;
- hostile multipliers alter the feedback closure while preserving open-loop symmetry;
- model-space defects are closed-loop unobservable or unreachable modes, depending on variance.

This does not solve RH, but it locates the missing law in one operator.

## Source construction required

The next legitimate object is not another scalar kernel. It is the typed realization

\[
(A(z),B(z),C(z),D(z))
\]

derived from the doubled theta tail, seam retention, arithmetic incidence, and archimedean endpoint.

The realization must specify:

- state and boundary spaces;
- domains and riggings;
- reciprocal-sector variance;
- cutoff bonding;
- the exact endpoint orientation;
- the determinant-line comparison with \(\Xi\).

Only after this realization exists may one test small gain, dissipativity, grading, controllability, or observability.

## Finite falsifier

At any finite labelled cutoff, compute

\[
R_X(z)
=
S_{\partial,X}(z)
-
\left(D_X(z)-C_X(z)A_X(z)^{-1}B_X(z)\right).
\]

A nonzero residual rejects the claimed realization.

If the identity holds, test the smallest singular value of \(I-L_X(z)\), the numerical radius of \(L_X(z)\), and any proposed grade-raising law. A single eigenvalue \(1\), nonpositive dissipativity minor, or grade-preserving cycle falsifies the corresponding orientation mechanism.

## Disposition

The source-derived acyclicity programme survives only as a closed-loop theorem. Bulk Volterra contraction is real but non-RH-bearing.

The decisive object is the boundary loop

\[
L(z)=C(z)A(z)^{-1}B(z).
\]

RH-strength progress requires a source-local reason that \(1\) cannot enter its spectrum off the critical seam.
