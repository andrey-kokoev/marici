# The forward/backward crossing defect is the missing antisymmetric base coordinate for the two-by-four packet

## Typed correction

The persistent numerical value

\[
-0.1508512190587392007
\]

belongs to the unchanged-Evans adjoint Hilbert residual. That state has the
wrong source type for the corrected pair, so the decimal cannot be imported as
a correction coefficient. It can identify the missing role: an oriented
crossing-defect coordinate.

Use the authoritative maps

\[
\Delta=U_{\rm G4}-T_{\rm PB}
\]

and define the corrected defect state

\[
d_z:=\Delta e_z.
\]

The opposite orientation carries `-d_z`. For any authorized dual row `ell`,

\[
\ell(-d_z)=-\ell(d_z).
\]

Thus the observed signs arise from orientation of one state, rather than from
inserting a fitted scalar.

## Two-by-four packet

For `X in {S,A,C,G}`, retain both directed presentations

\[
X_+(e_z)=X(U_{\rm G4}e_z),
\qquad
X_-(e_z)=X(T_{\rm PB}e_z).
\]

Assemble

\[
\Theta(e_z)=
\begin{pmatrix}
S_+&A_+&C_+&G_+\\
S_-&A_-&C_-&G_-
\end{pmatrix}.
\]

Its row codiagonal and row boundary are

\[
X_{\rm sym}=\frac{X_++X_-}{2},
\qquad
X_{\rm def}=X_+-X_-=X(d_z).
\]

The antisymmetric row therefore retains a common nonzero base coordinate until
crossing closure is proved.

## Complexity increase

The correct carrier is the mapping cone of the crossing map,

\[
\operatorname{Cone}(\Delta)
=
\mathcal H_{\rm out}\oplus\mathcal H_{\rm in}[1].
\]

A filler is no longer merely equality of two scalar responses. It is a
source-derived null-homotopy `h` satisfying the appropriate chain identity

\[
\partial h+h\partial=\Delta.
\]

Applying `S,A,C,G` gives four presentations of the same homotopy and produces
the full two-row packet. This is the precise sense in which retaining the
forward/backward difference raises coherence complexity.

## Finite source test

The correction must be evaluated before scalar projection. On the rank-two
Evans source basis `e_1,e_2`, require the four identities

\[
\mathfrak G_p^{\rm St}(e_j,e_k)
=
\mathfrak G_p^\theta
(Q_p^{\rm lin}e_j,Q_p^{\rm lin}e_k),
\qquad j,k\in\{1,2\}.
\]

Equivalently, the complete `2 by 2` Gram defect matrix must vanish. Cancellation
of one dual evaluation, including the `0.150851...` projection, is only one
matrix entry and is insufficient.

## Relation to the rung-four residual

After lower sewing, the Hermitian evaluation of the antisymmetric base is the
placewise defect

\[
\mathcal R_p(b_z)
=(1-p^{-2\operatorname{Re}z})E_p(b_z).
\]

The proposed higher cell must therefore map the cone boundary to this residual
without defining its coefficient from `R_p`. If the theta-history
sesquilinear matrix constructs `Q_p^{lin}` and satisfies all four Gram
identities, the antisymmetric base becomes null-homotopic. Otherwise the
construction stops at a well-typed nonzero defect.

## Current gate

The repository does not materialize the complete theta-history sesquilinear
coefficients. Those four coefficients, rather than the scalar decimal, are the
minimal data needed for the test.