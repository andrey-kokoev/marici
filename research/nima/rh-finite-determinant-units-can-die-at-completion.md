# RH finite determinant units can die at completion

## Result

A nowhere-zero Schur–Evans comparison at every finite cutoff does not imply a nowhere-zero comparison after completion.

Let the transition from cutoff (n) to (n+1) be

\[
u_{n,n+1}=\frac{n}{n+1}.
\]

Every transition is invertible and the composites satisfy the exact cocycle law

\[
u_{m,k}=u_{n,k}u_{m,n}.
\]

But

\[
u_{1,N}=\prod_{n=1}^{N-1}\frac{n}{n+1}=\frac1N
\longrightarrow 0.
\]

Thus the completed comparison ceases to be a unit. A zero divisor can appear through completion even though no finite transition has a zero and every finite coherence square commutes.

## Consequence for the RH colligation

Suppose finite cutoff sections obey

\[
S_X=u_XF_X
\]

with (u_X) nowhere zero. This transports the divisor only at cutoff (X). To pass to the completed source, both (u_X) and (u_X^{-1}) require locally uniform control on the spectral domain.

A sufficient compact-local gate is: for every compact set (K) in an open half-plane, there are constants (0<c_K<C_K<\infty) such that

\[
c_K\le |u_X(z)|\le C_K
\]

for every cutoff (X) and every (z\in K), together with locally uniform convergence of the sections. Equivalently, the comparison must converge in the sheaf of holomorphic units, not merely in the sheaf of holomorphic functions.

## Categorical interpretation

Finite determinant lines and invertible transition cells form a diagram in a Picard groupoid. Ordinary completion in the ambient space of sections need not preserve that groupoid: an invertible sequence may converge to a noninvertible morphism.

The completion functor therefore needs an explicit unit-preservation law. It must preserve both a comparison and its inverse. This is the determinant-line version of the earlier tail–seam lesson that finite faithfulness does not imply closed range.

## DPC

Candidate: finite nowhere-zero comparison plus exact cocycle coherence.

Verdict: rejected by the telescoping sequence (u_{1,N}=1/N).

Candidate: pointwise nonzero limit.

Verdict: insufficient without locally uniform reciprocal control; zeros can enter through nonuniform convergence near spectral infinity or the boundary.

Surviving candidate: a source-derived comparison bounded as a unit on every compact spectral set, with its inverse controlled in the same constructor topology used for the full colligation.

## Immediate source test

For the primitive, square, seam, and archimedean increments, estimate the cumulative relative determinant transition rather than only each edge. The first decisive falsifier is a compact spectral window on which either

\[
\inf_X\inf_{z\in K}|u_X(z)|=0
\]

or

\[
\sup_X\sup_{z\in K}|u_X(z)|=\infty.
\]

If neither occurs and the cutoff sections converge locally uniformly, the Schur–Evans divisor comparison survives completion on that half-plane.
