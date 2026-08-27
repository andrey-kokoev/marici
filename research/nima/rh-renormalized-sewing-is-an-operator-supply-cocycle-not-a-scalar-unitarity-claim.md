# Renormalized RH sewing is an operator supply cocycle

Author: `marici.Nima`

Date: 2026-08-26

Status: exact finite balance law and typed dilation gate

## Sewing residual

For a finite-cutoff reciprocal sewing map

\[
J_X:\mathcal P_X^-\longrightarrow\mathcal P_X^+,
\]

define its operator supply residual by

\[
R_X=I-J_X^*J_X.
\]

Raw unitarity is the special case $R_X=0$. Off seam, local Tate transport
need not satisfy this condition.

The residual is a Hermitian form on the complete typed port packet. Its
matrix, kernel, and support contain information that its scalar trace or
determinant does not retain.

## Positive and negative supply ports

Write the Hermitian decomposition

\[
R_X=R_{X,+}-R_{X,-},
\]

where both terms are positive semidefinite and have orthogonal supports. Then

\[
J_X^*J_X+R_{X,+}=I+R_{X,-}.
\]

After factoring

\[
R_{X,+}=B_{X,+}^*B_{X,+},
\qquad
R_{X,-}=B_{X,-}^*B_{X,-},
\]

the balance becomes

\[
\lVert J_Xu\rVert^2
+\lVert B_{X,+}u\rVert^2
=
\lVert u\rVert^2
+\lVert B_{X,-}u\rVert^2.
\]

Thus a nonunitary sewing map can become lossless only after both emitted and
absorbed supply channels are retained.

The source must construct these channels. Spectrally splitting a completed
matrix after the fact would provide a dilation but no arithmetic explanation.

## Composition cocycle

For composable sewing maps (J) and (K), the residual of their product is

\[
R(JK)
=
I-K^*J^*JK.
\]

Insert and subtract (K^*K) to obtain

\[
R(JK)
=
R(K)+K^*R(J)K.
\]

This is the exact operator-valued supply cocycle. The second residual must be
transported into the new port frame before addition.

Scalar addition of local gain defects is therefore wrong unless the transport
action is trivial.

## Relation to arithmetic currents

The primitive and square endpoint currents are candidate low-order components
of $R_X$. The seam and archimedean channels are candidate complementary
components required to close the finite supply balance.

Their compiler obligation is now exact:

1. construct each typed residual form before scalar readout;
2. transport it by the preceding sewing maps;
3. verify the cocycle under every staged prime-power composition;
4. show that their total equals (I-J_X^*J_X);
5. descend the balance through the third-order completion.

This is stronger than reproducing the completed functional equation.

## Determinant-one hostile

Consider

\[
J=
\begin{pmatrix}
2&0\\
0&1/2
\end{pmatrix}.
\]

Its determinant is one, but

\[
I-J^*J
=
\begin{pmatrix}
-3&0\\
0&3/4
\end{pmatrix}.
\]

One direction injects supply while the other absorbs it. Scalar determinant
normalization sees neither direction. Both typed ports are required for the
lossless dilation.

## Revised two-sector theorem

The earlier passive zero-confinement argument applies after the full supply
packets of the two sectors are cross-connected so that their positive and
negative residual ports cancel through source-authorized unitary pairings.

If an unpaired negative supply direction remains, it can cancel the positive
interior defect and support an off-seam closed mode. Exact scalar functional
equation symmetry does not exclude this.

## Finite falsifiers

At each cutoff and each staged composition, reject the sewing compiler if:

- the declared residual differs from (I-J_X^*J_X);
- positive or negative support is omitted;
- a residual is added without conjugating it into the current frame;
- the supply cocycle fails;
- determinant-one normalization is treated as unitarity;
- the completion loses a residual direction.
