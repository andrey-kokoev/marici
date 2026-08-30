# The source Green concomitant gives the wall module a canonical Krein signature

## Scope

The indicial calculation produced a two-step boundary module on each logarithmic end but did not determine its Green form. The shifted even-potential operator supplies that form directly through its Lagrange boundary concomitant.

Let

\[
Q_-=
\partial_q^2-2\partial_q+\frac34.
\]

Its formal \(L^2(dq)\) adjoint is

\[
Q_-^\sharp=
\partial_q^2+2\partial_q+\frac34.
\]

## Green identity

For smooth \(g,f\),

\[
(Q_-g)\overline f
-
g\,\overline{Q_-^\sharp f}
=
\partial_q\,\mathcal B(g,f),
\]

where

\[
\mathcal B(g,f)
=
g'\overline f
-
g\overline{f'}
-
2g\overline f.
\]

Thus \(\mathcal B\) is the source-derived boundary pairing between a \(Q_-\) mode and an adjoint mode.

## Primal and reciprocal indicial bases

The primal homogeneous modes are

\[
w_0=e^{q/2},
\qquad
w_1=e^{3q/2}.
\]

The adjoint homogeneous modes are

\[
v_0=e^{-q/2},
\qquad
v_1=e^{-3q/2}.
\]

These are exactly the reflected reciprocal modes.

Direct substitution gives

\[
\mathcal B(w_0,v_0)=-1,
\]

\[
\mathcal B(w_0,v_1)=0,
\]

\[
\mathcal B(w_1,v_0)=0,
\]

\[
\mathcal B(w_1,v_1)=1.
\]

Therefore, in the ordered bases \((w_0,w_1)\) and \((v_0,v_1)\), the boundary pairing matrix is

\[
J_{\partial}
=
\begin{pmatrix}
-1&0\\
0&1
\end{pmatrix}.
\]

The pairing is nondegenerate and has signature \((1,1)\).

## Interpretation

The two boundary coordinates are not two positive-energy directions. They form a canonical Krein pair:

- the constant-wall mode has negative boundary sign;
- the conjugate linear mode has positive boundary sign;
- the cross-pairings vanish in the indicial frame.

This sign pattern is fixed by the drift term \(-2\partial_q\) in \(Q_-\). It is not an arbitrary metric choice.

The reciprocal modes are not optional duplicates. They are the adjoint test modes required to evaluate the boundary form.

## Relation to the derivative chain

The derivative incidence satisfies

\[
w_1\mapsto w_0\mapsto0.
\]

Thus the positive boundary mode maps into the negative wall mode. The chain is therefore not positive in its native boundary geometry.

A positive auxiliary Green block cannot be obtained by simply declaring both coefficients positive. It must arise from a source-authorized polarization, causal-history doubling, or Schur construction that converts this Krein boundary data into a positive completed energy.

## Sewing constraint

Any reciprocal sewing map \(S\) between primal and adjoint boundary fibers must preserve the concomitant:

\[
\mathcal B(Sg,S^\sharp f)=\mathcal B(g,f).
\]

In coefficient form, if the same frame is used on both sides, the sewing matrix must satisfy the corresponding \(J_{\partial}\)-unitarity law

\[
S^*J_{\partial}S=J_{\partial}.
\]

Thus admissible sewing belongs to a \(U(1,1)\)-type geometry before any positive polarization is chosen.

Scalar endpoint agreement does not enforce this law.

## Finite interval orientation

On an interval \([a,b]\), Green's identity reads

\[
\langle Q_-g,f\rangle
-
\langle g,Q_-^\sharp f\rangle
=
\mathcal B(g,f)\big|_{a}^{b}.
\]

Reversing interval orientation reverses the full boundary form. This supplies the reciprocal sign convention without inserting an external phase.

## Result

The wall-plus-partner module now has a source-fixed nondegenerate geometry:

\[
J_{\partial}=\operatorname{diag}(-1,1).
\]

This closes the finite-dimensional boundary-form calculation. It also rules out a direct positive wall Gram. The next constructor must explain how causal/history polarization turns this Krein boundary pair into the positive auxiliary block required by the Adams Schur cell.
